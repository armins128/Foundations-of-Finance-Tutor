"""Validate the distributed package without the private instructor archive."""
from pathlib import Path
import json
import re
import subprocess
import sys
from numerical_bank import bank

ROOT=Path(__file__).resolve().parents[1]
REF=ROOT/'skills/fof-coach/references'


def main():
    manifest=json.loads((ROOT/'plugin.json').read_text(encoding='utf-8'))
    assert manifest['name']=='foundations-of-finance'
    for native in ('.codex-plugin/plugin.json','.claude-plugin/plugin.json'):
        m=json.loads((ROOT/native).read_text(encoding='utf-8'))
        assert m['name']==manifest['name'] and m['version']==manifest['version'] and m['skills']=='./skills/',native
    codex=json.loads((ROOT/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
    assert (ROOT/codex['interface']['logo']).is_file()
    assert len(list((ROOT/'skills').glob('*/SKILL.md')))==14
    curriculum=json.loads((REF/'curriculum.json').read_text(encoding='utf-8'))
    byid={c['id']:c for c in curriculum}
    assert len(byid)==len(curriculum)==73
    def walk(key,trail):
        assert key not in trail,'Prerequisite cycle'
        for parent in byid[key]['prerequisites']:walk(parent,trail|{key})
    for key in byid:walk(key,set())
    items=json.loads((REF/'numerical-exercises.json').read_text(encoding='utf-8'))
    assert items==bank(),'Rebuild or review numerical bank after changing data'
    for item in items:assert set(item['competencies'])<=set(byid)
    for p in ROOT.rglob('*.md'):
        if 'Learning-Protokoll' in p.parts:continue
        text=p.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in link or link.startswith('#'):continue
            target=(p.parent/link.split('#')[0]).resolve()
            assert target.is_relative_to(ROOT.resolve()) and target.is_file(),(p,link)
    for script,args in [('score.py',['--self-test']),('journal.py',['self-test']),('fof_calc.py',['self-test'])]:
        subprocess.run([sys.executable,str(ROOT/'skills/fof-coach/scripts'/script),*args],check=True)
    for mode in ('fof-practice','fof-review','fof-mock'):
        assert 'task-generation.md' in (ROOT/'skills'/mode/'SKILL.md').read_text(encoding='utf-8'),mode
    print('PASS: 14 skills, 73 competencies, 36 numerical tasks, prerequisite graph and internal links')


if __name__=='__main__':main()
