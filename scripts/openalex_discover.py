import json, subprocess, time, urllib.parse, os

OUT = r'D:\study\Embodied\docs\_openalex_discover.json'
FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')

queries = [
 ('vla_benchmark', 'title_and_abstract.search:vision-language-action benchmark,from_publication_date:2024-01-01'),
 ('vla_safety', 'title_and_abstract.search:vision-language-action safety,from_publication_date:2024-01-01'),
 ('vla_robustness', 'title_and_abstract.search:vision-language-action robustness,from_publication_date:2024-01-01'),
 ('embodied_bench', 'title_and_abstract.search:embodied agent benchmark safety,from_publication_date:2024-01-01'),
 ('vla_jailbreak', 'title_and_abstract.search:jailbreak embodied robot,from_publication_date:2024-01-01'),
 ('vla_adversarial', 'title_and_abstract.search:adversarial attack vision-language-action,from_publication_date:2024-01-01'),
 ('robot_policy_eval', 'title_and_abstract.search:robot policy evaluation benchmark manipulation,from_publication_date:2024-01-01'),
 ('vla_backdoor', 'title_and_abstract.search:backdoor vision-language-action model,from_publication_date:2024-01-01'),
]

res = {}
if os.path.exists(OUT):
    res = json.load(open(OUT, encoding='utf-8'))

for name, filt in queries:
    if name in res:
        continue
    url = ('https://api.openalex.org/works?filter=%s&sort=cited_by_count:desc&per_page=25'
           '&select=title,publication_year,doi,primary_location,cited_by_count' % urllib.parse.quote(filt, safe=':,'))
    tmp = os.path.expandvars(r'%TEMP%\oa_d.json')
    subprocess.run(['node', FETCH, url, '-o', tmp], capture_output=True)
    try:
        d = json.load(open(tmp, encoding='utf-8'))
    except Exception as e:
        print('FAIL', name, e); continue
    rows = []
    for r in (d.get('results') or []):
        pl = r.get('primary_location') or {}
        rows.append({
            'title': r.get('title'), 'year': r.get('publication_year'),
            'venue': (pl.get('source') or {}).get('display_name'),
            'raw_source': pl.get('raw_source_name'), 'doi': r.get('doi'),
            'cites': r.get('cited_by_count')})
    res[name] = rows
    print('==', name, len(rows))
    for r in rows[:12]:
        print('   ', r['year'], '|', r['cites'], '|', r['venue'], '|', (r['title'] or '')[:88])
    time.sleep(0.4)

json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved')
