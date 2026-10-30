import json, subprocess, time, urllib.parse, os

FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')
OUT = r'D:\study\Embodied\docs\_oa_bench.json'

names = [
 'RoboArena distributed real-world evaluation robot policies',
 'RoboEval evaluating language-conditioned robot manipulation',
 'VLA-Bench vision language action benchmark',
 'RoboBench benchmark robotic manipulation foundation models',
 'BEHAVIOR-1K benchmark embodied AI household activities',
 'BEHAVIOR Robot Suite',
 'AgiBot World Colosseo large-scale manipulation platform',
 'RoboFAC robustness benchmark vision language action',
 'ManiSkill unified benchmark robotic manipulation',
 'Robo2VLM visual question answering from robot trajectories',
 'Genie Envisioner unified platform robot policy evaluation',
 'WorldEval automated evaluation world models',
 'SafeAgentBench safety embodied LLM agents',
 'RoboTrust benchmark trustworthiness embodied',
 'Vision Language Action models survey evaluation benchmark',
]

res = {}
if os.path.exists(OUT):
    res = json.load(open(OUT, encoding='utf-8'))

for n in names:
    if n in res:
        continue
    url = ('https://api.openalex.org/works?search=%s&per_page=3'
           '&select=title,publication_year,doi,primary_location' % urllib.parse.quote(n))
    tmp = os.path.expandvars(r'%TEMP%\oa_b.json')
    subprocess.run(['node', FETCH, url, '-o', tmp], capture_output=True)
    try:
        d = json.load(open(tmp, encoding='utf-8'))
    except Exception:
        print('FAIL', n)
        continue
    rows = []
    for r in (d.get('results') or [])[:3]:
        pl = r.get('primary_location') or {}
        rows.append({'title': r.get('title'), 'year': r.get('publication_year'),
                     'venue': (pl.get('source') or {}).get('display_name'),
                     'doi': r.get('doi')})
    res[n] = rows
    print('##', n)
    for r in rows:
        print('   ', r['year'], '|', r['venue'], '|', (r['title'] or '')[:80])
    time.sleep(0.3)

json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved')
