import json, subprocess, time, urllib.parse, os

FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')
OUT = r'D:\study\Embodied\docs\_oa_more.json'

names = [
 'SafeVLA-Bench success-safety gap vision-language-action',
 'PolaRiS scalable real-to-sim evaluations generalist robot policies',
 'RoboWorld fast reliable neural simulators generalist robot policy evaluation',
 'WorldEval world model real-world robot policies evaluator',
 'HUGE-Bench high-level UAV vision-language-action tasks',
 'Robo2Process process-aware understanding vision-language-action',
 'RoboChrono real robot benchmark streaming task understanding',
 'RoboVista evaluating vision language models diverse robot applications',
 'Robo Eval where robotic manipulation meets structured scalable evaluation',
 'TSHA benchmark visual language models trustworthy safety hazard assessment',
 'RoboInter holistic intermediate representation embodied world models',
 'FailSafe reasoning recovery failures vision-language-action',
 'RoboFAC comprehensive framework robotic failure analysis correction',
 'AgiBot World Colosseo large-scale manipulation platform',
 'ManiSkill2 unified benchmark generalizable manipulation skills',
]

res = {}
if os.path.exists(OUT):
    res = json.load(open(OUT, encoding='utf-8'))

for n in names:
    if n in res:
        continue
    url = ('https://api.openalex.org/works?search=%s&per_page=3'
           '&select=title,publication_year,doi,primary_location,abstract_inverted_index' % urllib.parse.quote(n))
    tmp = os.path.expandvars(r'%TEMP%\oa_m.json')
    subprocess.run(['node', FETCH, url, '-o', tmp], capture_output=True)
    try:
        d = json.load(open(tmp, encoding='utf-8'))
    except Exception:
        print('FAIL', n)
        continue
    rows = []
    for r in (d.get('results') or [])[:3]:
        pl = r.get('primary_location') or {}
        ai = r.get('abstract_inverted_index') or {}
        abstract = ''
        if ai:
            pos = []
            for w, idxs in ai.items():
                for i in idxs:
                    pos.append((i, w))
            pos.sort()
            abstract = ' '.join(w for _, w in pos)
        rows.append({'title': r.get('title'), 'year': r.get('publication_year'),
                     'venue': (pl.get('source') or {}).get('display_name'),
                     'doi': r.get('doi'), 'abstract': abstract})
    res[n] = rows
    print('##', n)
    for r in rows[:2]:
        print('   ', r['year'], '|', r['venue'], '|', (r['title'] or '')[:78])
        print('      abs:', (r['abstract'] or '(none)')[:200])
    time.sleep(0.3)

json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved')
