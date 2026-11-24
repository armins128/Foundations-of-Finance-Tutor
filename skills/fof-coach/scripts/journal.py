"""Maintain Learning-Protokoll in a learner's workspace; standard library only."""
from pathlib import Path
from datetime import datetime
from contextlib import contextmanager
import argparse
import hashlib
import json
import os
import re
import tempfile
import uuid
import score

SKILL = Path(__file__).resolve().parents[1]
PLUGIN = SKILL.parents[1]
REF = SKILL/'references'


def encoded(obj):
    return json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+'\n'


def atomic(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name('.'+path.name+'.'+uuid.uuid4().hex+'.tmp')
    try:
        temp.write_text(text,encoding='utf-8')
        os.replace(temp,path)
    finally:
        temp.unlink(missing_ok=True)


def location(folder):
    workspace=Path(folder).resolve()
    if workspace==PLUGIN or workspace.is_relative_to(PLUGIN):
        raise ValueError('Choose a personal learner workspace outside the plugin installation')
    return workspace/'Learning-Protokoll'


@contextmanager
def locked(root):
    root.mkdir(parents=True,exist_ok=True)
    lock=root/'.write.lock'
    try:
        handle=lock.open('x',encoding='utf-8')
    except FileExistsError:
        raise ValueError('Learning protocol is busy; finish the other write or inspect a stale lock') from None
    try:
        handle.write(str(os.getpid()));handle.close()
        yield
    finally:
        handle.close();lock.unlink(missing_ok=True)


def safe_id(value):
    if not isinstance(value,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,100}',value):
        raise ValueError('IDs must use 1-100 letters, digits, hyphens or underscores')
    return value


def load_events(root):
    records=[json.loads(p.read_text(encoding='utf-8')) for p in (root/'events').glob('*.json')]
    records.sort(key=lambda e:e['sequence'])
    if len({e['sequence'] for e in records})!=len(records):
        raise ValueError('Conflicting event sequence; inspect the protocol before continuing')
    return records


def validate_plan(plan,curriculum):
    required=('schema_version','plan_id','version','updated_at','deadline','timezone','basis','constraints','blocks')
    if not all(k in plan for k in required) or plan['schema_version']!=1:
        raise ValueError('Incomplete or unsupported plan')
    safe_id(plan['plan_id'])
    if not isinstance(plan['version'],int) or plan['version']<1:
        raise ValueError('Plan version must be positive')
    deadline=datetime.fromisoformat(plan['deadline']).date() if plan['deadline'] else None
    if not isinstance(plan['blocks'],list) or not isinstance(plan['constraints'],dict):
        raise ValueError('Invalid blocks or constraints')
    known={c['id'] for c in curriculum}; seen=set(); usage={}
    for b in plan['blocks']:
        if not all(k in b for k in ('id','date','minutes','competencies','mode','task','success_criterion','status')):
            raise ValueError('Incomplete plan block')
        safe_id(b['id'])
        if b['id'] in seen: raise ValueError('Duplicate block ID')
        seen.add(b['id'])
        if isinstance(b['minutes'],bool) or not isinstance(b['minutes'],int) or b['minutes']<=0:
            raise ValueError('Block minutes must be positive integers')
        if not isinstance(b['competencies'],list) or not set(b['competencies'])<=known:
            raise ValueError('Unknown plan competency')
        if b['status'] not in ('planned','in-progress','completed','deferred'):
            raise ValueError('Unknown block status')
        if b['mode'] not in ('diagnose','learn','practice','review','mock'):
            raise ValueError('Unknown block mode')
        if b['date']:
            dt=datetime.fromisoformat(b['date']).date()
            if deadline and dt>=deadline: raise ValueError('Preparation must precede the exam date')
            if b['status']!='deferred':usage[dt]=usage.get(dt,0)+b['minutes']
        elif deadline:
            raise ValueError('Dated plan has an undated block')
    # Availability is explicitly learner-supplied; do not invent a daily budget.
    weekly=plan['constraints'].get('weekly_minutes',{})
    exceptions=plan['constraints'].get('date_minutes',{})
    for dt,minutes in usage.items():
        budget=exceptions.get(dt.isoformat(),weekly.get(str(dt.weekday())))
        if budget is None:
            raise ValueError('Missing confirmed availability for '+dt.isoformat())
        if isinstance(budget,bool) or not isinstance(budget,int) or budget<0:
            raise ValueError('Availability minutes must be nonnegative integers')
        if minutes>budget: raise ValueError('Overloaded study day: '+dt.isoformat())


def refresh(root):
    records=load_events(root)
    state=json.loads((REF/'passport-template.json').read_text(encoding='utf-8'))
    plan=None; pending=None; sessions={}
    for e in records:
        if 'base_state' in e:state=e['base_state']
        state['attempts'].extend(e.get('attempts',[]))
        for key in ('goal','misconceptions','next_tasks'):
            if key in e:state[key]=e[key]
        if 'pending_task' in e:pending=e['pending_task']
        if 'plan' in e:plan=e['plan']
        if e.get('completed_blocks'):
            if plan is None:raise ValueError('No plan exists for completed_blocks')
            blocks={b['id']:b for b in plan['blocks']}
            for key in e['completed_blocks']:
                if key not in blocks:raise ValueError('Unknown completed block '+key)
                blocks[key]['status']='completed';blocks[key]['completion_event']=e['id']
        sessions.setdefault((e['timestamp'][:10],e['session']),[]).append(e)
    curriculum=json.loads((REF/'curriculum.json').read_text(encoding='utf-8'))
    asof=records[-1]['timestamp'][:10] if records else None
    result=score.summarize(state,curriculum,asof)
    stamp=records[-1]['timestamp'] if records else 'No learning exchange recorded yet'
    state['last_updated']=stamp;state['pending_task']=pending
    atomic(root/'state.json',encoded(state))
    title=['# Current learning status',f'Last updated: {stamp}',f'Goal: {state["goal"]}',
           f'Coverage: {result["assessed"]}/{result["total"]} competencies assessed. '
           f'Demonstrated readiness: {result["score"] if result["score"] is not None else "not yet assessable"}. '
           f'Unknown-area range: {result["unassessed_range"]}. This is not a pass probability.',
           '| Area | Assessed / total | Demonstrated index |\n|---|---:|---:|']
    title += [f'| {a["area"]} | {a["assessed"]}/{a["total"]} | {a["lower"]:.1f}% |' for a in result['areas']]
    title += ['\n## Current misconceptions\n\n'+('\n'.join('- '+str(x) for x in state['misconceptions']) or 'None recorded; this does not mean all concepts were tested.'),
              '## Pending task\n\n'+(json.dumps(pending,ensure_ascii=False,indent=2) if pending else 'No pending task.'),
              '## Next steps\n\n'+('\n'.join('- '+str(x) for x in state['next_tasks']) or 'Choose the first relevant diagnostic or planned task.'),
              '## Competency evidence\n\n| ID | Topic | Level | Freshness |\n|---|---|---:|---|']
    title += [f'| {c["id"]} | {c["title"]} | {c["level"] if c["level"] is not None else "not assessed"} | {"retrieval due" if c["stale"] else "see event dates"} |' for c in result['competencies']]
    title += ['\nFull evidence and feedback are preserved under sessions/ and events/. Imported statements are learner-supplied, not independently authenticated.']
    atomic(root/'STATUS.md','\n\n'.join(title[:4])+'\n\n'+'\n'.join(title[4:])+'\n')
    if plan:
        validate_plan(plan,curriculum)
        atomic(root/'plan.json',encoded(plan))
        lines=['# Adaptive study plan',f'Plan {plan["plan_id"]}, version {plan["version"]}; updated {plan["updated_at"]}.',
               f'Deadline: {plan["deadline"] or "not yet known — provisional sequence"}. Timezone: {plan["timezone"] or "not yet specified"}.',
               'Evidence basis: '+plan['basis'],
               'Confirmed constraints:\n\n```json\n'+encoded(plan['constraints'])+'```',
               '| Date / order | Minutes | Activity | Competencies | Task / success criterion | Status |\n|---|---:|---|---|---|---|']
        clean=lambda s:str(s).replace('|','/').replace('\n',' ')
        for i,b in enumerate(plan['blocks'],1):
            lines.append(f'| {b["date"] or "Step "+str(i)} | {b["minutes"]} | {b["mode"]} | {", ".join(b["competencies"])} | {clean(b["task"])} / {clean(b["success_criterion"])} | {b["status"]} |')
        if plan.get('uncovered'):
            lines+=['\nUncovered objectives / capacity limits: '+clean(plan['uncovered'])]
        atomic(root/'LERNPLAN.md','\n\n'.join(lines[:6])+'\n'+'\n'.join(lines[6:])+'\n')
    elif not (root/'LERNPLAN.md').exists():
        atomic(root/'LERNPLAN.md','# Study plan pending\n\nAsk for the deadline, realistic availability, prior learning and whether to run a diagnostic. Do not invent dates.\n')
    for (day,session),events in sessions.items():
        chunks=[f'# Learning session {session}\n\nDate: {day}. Timestamps retain the observed timezone.']
        for e in events:
            chunks.append(f'## {e["timestamp"]} — {e["type"]}\n\nEvent: {e["id"]}\n\n```json\n'+encoded({k:v for k,v in e.items() if k not in ('sequence','base_state')})+'```')
        atomic(root/'sessions'/day/(session+'.md'),'\n\n'.join(chunks)+'\n')
    return result


def append(root,event):
    event=dict(event)
    for key in ('id','session'):safe_id(event.get(key))
    if event.get('type') not in ('task','attempt','hint','explanation','skip','plan','note','import','plan-completion'):
        raise ValueError('Unknown learning event type')
    stamp=event.get('timestamp')
    if not isinstance(stamp,str) or datetime.fromisoformat(stamp).tzinfo is None:
        raise ValueError('Use an observed ISO timestamp with timezone offset')
    records=load_events(root)
    if records and datetime.fromisoformat(stamp)<datetime.fromisoformat(records[-1]['timestamp']):
        # An exact idempotent retry may have an earlier timestamp.
        if event['id'] not in {e['id'] for e in records}:raise ValueError('Events must be appended in time order')
    target=root/'events'/(event['id']+'.json')
    if target.exists():
        old=json.loads(target.read_text(encoding='utf-8'));old.pop('sequence',None)
        if old!=event:raise ValueError('An event ID was reused with different content')
        return refresh(root)
    curriculum=json.loads((REF/'curriculum.json').read_text(encoding='utf-8'))
    passport=json.loads((REF/'passport-template.json').read_text(encoding='utf-8'))
    passport['attempts']=event.get('attempts',[]);score.validate(passport,curriculum)
    if any(a['date'] and a['date']>stamp[:10] for a in passport['attempts']):
        raise ValueError('Attempt date lies after its learning event')
    if 'base_state' in event:score.validate(event['base_state'],curriculum)
    if 'plan' in event:validate_plan(event['plan'],curriculum)
    if event.get('completed_blocks'):
        current_plan=None
        for previous in records:
            if 'plan' in previous:current_plan=previous['plan']
        if current_plan is None or not set(event['completed_blocks'])<={b['id'] for b in current_plan['blocks']}:
            raise ValueError('Unknown completed plan block')
    event['sequence']=len(records)+1
    target.parent.mkdir(parents=True,exist_ok=True)
    atomic(target,encoded(event))
    return refresh(root)


def initialize(root):
    (root/'events').mkdir(exist_ok=True)
    # Preserve a supplied passport as an explicit imported snapshot.
    if not load_events(root) and (root/'state.json').exists():
        base=json.loads((root/'state.json').read_text(encoding='utf-8'))
        append(root,dict(id='import-'+uuid.uuid4().hex,session='import',type='import',
                       timestamp=datetime.now().astimezone().isoformat(),base_state=base))
    return refresh(root)


def self_test():
    with tempfile.TemporaryDirectory(prefix='fof-journal-') as tmp:
        root=location(tmp)
        with locked(root):
            assert initialize(root)['assessed']==0
            e=dict(id='event-1',session='session-1',type='task',timestamp='2026-11-23T14:00:00+01:00',
                   question='What does NPV=0 mean?',pending_task={'item':'V02','question':'What does NPV=0 mean?'})
            append(root,e);append(root,e)
            assert len(load_events(root))==1
            assert json.loads((root/'state.json').read_text(encoding='utf-8'))['pending_task']
            a=dict(competency='V02',item='V02',family='npv-meaning',session='session-1',kind='diagnostic',
                   fraction=1,hints=0,reasoning=True,date='2026-11-23',delay_verified=False)
            result=append(root,dict(id='event-2',session='session-1',type='attempt',timestamp='2026-11-23T14:02:00+01:00',
                    student_answer='It earns the required return but creates no extra present value.',
                    feedback='Correct opportunity-cost interpretation.',attempts=[a],pending_task=None))
            assert result['assessed']==1
            assert len(json.loads((root/'state.json').read_text(encoding='utf-8'))['attempts'])==1
            assert 'Correct opportunity-cost' in (root/'sessions/2026-11-23/session-1.md').read_text(encoding='utf-8')
            refresh(root)
            assert len(load_events(root))==2
            try:safe_id('../escape')
            except ValueError:pass
            else:raise AssertionError('Unsafe ID accepted')
            plan=dict(schema_version=1,plan_id='p1',version=1,updated_at='2026-11-23',deadline='2026-11-25',
                      timezone='Europe/Berlin',basis='Self-report; diagnostic pending',
                      constraints={'weekly_minutes':{'1':30}},blocks=[dict(id='b1',date='2026-11-24',minutes=30,
                      competencies=['V01'],mode='learn',task='Practice PV',success_criterion='Independent fresh PV',status='planned')])
            append(root,dict(id='event-3',session='session-1',type='plan',timestamp='2026-11-23T14:03:00+01:00',plan=plan))
            assert 'Practice PV' in (root/'LERNPLAN.md').read_text(encoding='utf-8')
            append(root,dict(id='event-4',session='session-1',type='plan-completion',timestamp='2026-11-23T14:04:00+01:00',completed_blocks=['b1']))
            assert json.loads((root/'plan.json').read_text(encoding='utf-8'))['blocks'][0]['status']=='completed'
            plan['blocks'][0]['minutes']=31
            try:validate_plan(plan,json.loads((REF/'curriculum.json').read_text(encoding='utf-8')))
            except ValueError:pass
            else:raise AssertionError('Overloaded day accepted')
            try:
                with locked(root):pass
            except ValueError:pass
            else:raise AssertionError('Concurrent writer accepted')
    print('PASS: journal creation, complete events, idempotency, recovery, plan persistence and capacity checks')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['init','record','plan','refresh','self-test'])
    p.add_argument('--folder');p.add_argument('--event');p.add_argument('--plan')
    args=p.parse_args()
    if args.action=='self-test':self_test()
    else:
        if not args.folder:p.error('--folder is required')
        root=location(args.folder)
        with locked(root):
            if args.action=='init':result=initialize(root)
            elif args.action=='record':
                if not args.event:p.error('--event is required')
                result=append(root,json.loads(Path(args.event).read_text(encoding='utf-8-sig')))
            elif args.action=='plan':
                if not args.plan:p.error('--plan is required')
                plan=json.loads(Path(args.plan).read_text(encoding='utf-8-sig'))
                digest=hashlib.sha256(encoded(plan).encode()).hexdigest()[:16]
                event_id='plan-'+digest
                existing=root/'events'/(event_id+'.json')
                if existing.exists():
                    event=json.loads(existing.read_text(encoding='utf-8'));event.pop('sequence',None)
                else:
                    event=dict(id=event_id,session='planning',type='plan',
                         timestamp=datetime.now().astimezone().isoformat(),plan=plan)
                result=append(root,event)
            else:result=refresh(root)
        print(json.dumps(dict(folder=str(root),assessed=result['assessed'],total=result['total']),indent=2))
