"""Compute a transparent study evidence score. Standard library only.

Usage: python score.py passport.json [--as-of YYYY-MM-DD]
No writes, network, student accounts or third-party dependencies.
"""
from datetime import date
from pathlib import Path
import argparse
import json
import math

REF = Path(__file__).resolve().parents[1] / 'references'
AREAS = ('value','bonds','portfolio','capm','derivatives','crypto','behavioral')


def validate(passport, curriculum):
    if passport.get('schema_version') != 1:
        raise ValueError('Unsupported learning-passport version')
    if passport.get('curriculum_version') != '2026-11-23':
        raise ValueError('Curriculum changed: map competency IDs before scoring')
    ids = {x['id'] for x in curriculum}
    if not isinstance(passport.get('attempts'), list):
        raise ValueError('attempts must be a list')
    for a in passport['attempts']:
        required = ('competency','item','family','session','kind','fraction','hints','reasoning','date','delay_verified')
        if not all(k in a for k in required):
            raise ValueError('Incomplete attempt')
        if a['competency'] not in ids:
            raise ValueError('Unknown competency: '+str(a['competency']))
        if not all(isinstance(a[k],str) and a[k].strip() for k in ('item','family','session')):
            raise ValueError('Empty evidence identity')
        if isinstance(a['fraction'],bool) or not isinstance(a['fraction'],(float,int)) or not math.isfinite(a['fraction']) or not 0 <= a['fraction'] <= 1:
            raise ValueError('fraction must be finite and in [0,1]')
        if isinstance(a['hints'],bool) or not isinstance(a['hints'],int) or not 0 <= a['hints'] <= 4:
            raise ValueError('hints must be an integer in [0,4]')
        if a['kind'] not in ('diagnostic','practice','retrieval','transfer','mock','exposure'):
            raise ValueError('Unknown evidence kind')
        if not isinstance(a['reasoning'],bool) or not isinstance(a['delay_verified'],bool):
            raise ValueError('reasoning and delay_verified must be boolean')
        if a['date'] is not None:
            date.fromisoformat(a['date'])


def summarize(passport, curriculum, as_of=None):
    validate(passport,curriculum)
    as_of = date.fromisoformat(as_of) if as_of else None
    if as_of and any(a['date'] and date.fromisoformat(a['date'])>as_of for a in passport['attempts']):
        raise ValueError('Evidence date lies after as-of date')
    states = []
    for c in curriculum:
        rows = [a for a in passport['attempts'] if a['competency']==c['id'] and a['kind']!='exposure']
        level = None
        evidence = []
        # Preserve order: a failed unassisted check can lower earlier mastery.
        for a in rows:
            independent = a['fraction']==1 and a['hints']==0 and a['reasoning']
            if independent:
                evidence.append(a)
                level = max(3, level or 0)
                families = {x['family'] for x in evidence}
                delayed = any(x['kind']=='retrieval' and x['delay_verified'] and any(
                    p['session']!=x['session'] and p['family']!=x['family']
                    for p in evidence[:i]) for i,x in enumerate(evidence))
                if len(families)>=2 and delayed:
                    level=4
                if level==4 and len(families)>=3 and any(x['kind']=='transfer' for x in evidence):
                    level=5
            elif a['hints'] or a['fraction']>0:
                level = 2 if a['fraction']>=.5 else (1 if a['fraction']>0 else 0)
                evidence=[]
            else:
                level=0
                evidence=[]
        stale = False
        if rows and as_of and rows[-1]['date']:
            stale=(as_of-date.fromisoformat(rows[-1]['date'])).days>14
        effective = min(level,3) if level is not None and stale else level
        states.append(dict(id=c['id'],area=c['area'],title=c['title'],level=level,
                           effective_level=effective,stale=stale,attempts=len(rows)))
    area_rows=[]
    for area in AREAS:
        group=[x for x in states if x['area']==area]
        known=[x for x in group if x['level'] is not None]
        total=sum(min(x['effective_level'],4)/4 for x in known)
        area_rows.append(dict(area=area,assessed=len(known),total=len(group),
                              lower=100*total/len(group),
                              upper=100*(total+len(group)-len(known))/len(group)))
    lower=sum(x['lower'] for x in area_rows)/len(area_rows)
    upper=sum(x['upper'] for x in area_rows)/len(area_rows)
    return dict(label='Demonstrated readiness index; not a pass probability',
                assessed=sum(x['level'] is not None for x in states),total=len(states),
                score=round(lower,1) if any(x['level'] is not None for x in states) else None,
                unassessed_range=[round(lower,1),round(upper,1)],
                range_note='Unknown-area bounds, not a statistical confidence interval',
                weighting='Equal seven-area weight; equal competencies within each area',
                areas=area_rows,competencies=states)


def self_test(curriculum):
    def passport(rows):
        return dict(schema_version=1,curriculum_version='2026-11-23',attempts=rows)
    def a(item='a',family='f1',session='s1',kind='diagnostic',fraction=1,hints=0,reasoning=True,dt='2026-11-20'):
        return dict(competency='V01',item=item,family=family,session=session,kind=kind,
                    fraction=fraction,hints=hints,reasoning=reasoning,date=dt,delay_verified=kind=='retrieval')
    def level(rows,dt=None):
        return summarize(passport(rows),curriculum,dt)['competencies'][0]
    assert summarize(passport([]),curriculum)['score'] is None
    assert level([a()])['level']==3
    assert level([a(),a(item='b')])['level']==3  # same family cannot farm mastery
    assert level([a(),a('b','f2','s2','retrieval')])['level']==4
    assert level([a(),a('b','f2','s2','retrieval'),a('c','f3','s2','transfer')])['level']==5
    assert level([a(hints=1)])['level']==2
    assert level([a(reasoning=False)])['level']==2
    assert level([a(kind='exposure')])['level'] is None
    assert level([a(),a(fraction=0)])['level']==0
    assert level([a(fraction=0),a(fraction=.25)])['level']==1
    assert level([a(),a('b','f2','s2','retrieval')],'2026-12-10')['effective_level']==3
    for bad in (float('nan'),-1,1.1,True):
        try:
            summarize(passport([a(fraction=bad)]),curriculum)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid score accepted')
    # Full evidence in every area produces exactly 100, never more.
    rows=[]
    for c in curriculum:
        for fam,ses,kind in [('f1','s1','diagnostic'),('f2','s2','retrieval')]:
            attempt=a(family=fam,session=ses,kind=kind); attempt['competency']=c['id']; rows.append(attempt)
    assert summarize(passport(rows),curriculum)['score']==100


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('passport',nargs='?')
    parser.add_argument('--as-of')
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    curriculum=json.loads((REF/'curriculum.json').read_text(encoding='utf-8'))
    if args.self_test:
        self_test(curriculum); print('PASS: evidence scoring, unknowns, stale checks and invalid inputs')
    else:
        if not args.passport:
            parser.error('Supply a passport or --self-test')
        print(json.dumps(summarize(json.loads(Path(args.passport).read_text(encoding='utf-8-sig')),curriculum,args.as_of),indent=2))
