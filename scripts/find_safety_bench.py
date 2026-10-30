# -*- coding: utf-8 -*-
"""Find embodied-safety benchmark papers in the library that are NOT yet in the table."""
import json, os, re

BASE = r'D:\study\Embodied'
lib = []
for f in ('papers', 'audited', 'screened'):
    lib += json.load(open(os.path.join(BASE, 'docs', '_data', f + '.json'), encoding='utf-8'))

have = {r['title'].strip().lower()
        for r in json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))}

seen, uniq = set(), []
for p in lib:
    k = (p.get('title') or '').strip().lower()
    if k in seen or k in have:
        continue
    seen.add(k)
    uniq.append(p)

# 提出 benchmark / 测试床 / 评测协议的信号
PROPOSE = re.compile(
    r'\bwe (?:introduce|present|propose|construct|build|release|develop|curate)\b[^.]{0,90}'
    r'(?:benchmark|testbed|test bed|evaluation (?:suite|framework|protocol|platform)|'
    r'dataset and benchmark|suite of|leaderboard|sandbox)', re.I)
NAME_SUFFIX = re.compile(r':\s*A\s+(?:[\w-]+\s+){0,4}(?:Benchmark|Bench|Testbed|Test Bed|Evaluation|Suite|Arena)\b', re.I)
TITLE_BENCH = re.compile(r'\bbench(?:mark)?s?\b', re.I)
TITLE_SAFE = re.compile(r'safe|safety|security|attack|adversar|robust|risk|hazard|threat|'
                        r'jailbreak|backdoor|poison|trust|verif|red.?team|vulnerab', re.I)
EMBODIED = re.compile(r'robot|embodied|manipulat|autonomous (?:vehicle|driving)|drone|uav|'
                      r'agent|vla|vlm|llm|physical|cyber-?physical|humanoid|swarm', re.I)

rows = []
for p in uniq:
    t = p.get('title') or ''
    ab = p.get('abstract') or ''
    blob = t + ' ' + ab
    if not EMBODIED.search(blob):
        continue
    is_bench_title = bool(TITLE_BENCH.search(t) or NAME_SUFFIX.search(t))
    proposes = bool(PROPOSE.search(ab))
    safety = bool(TITLE_SAFE.search(t)) or bool(TITLE_SAFE.search(ab[:400]))
    if (is_bench_title and safety) or (proposes and safety):
        score = (2 if is_bench_title else 0) + (2 if proposes else 0) + (1 if safety else 0)
        rows.append((score, p.get('year'), p.get('layer'), p.get('subcat'), t,
                     'T' if is_bench_title else '-', 'P' if proposes else '-',
                     'S' if safety else '-', p.get('tier')))

rows.sort(key=lambda x: (-x[0], str(x[1]), x[4]))
out = ['%3d | sc%s | %s | %-20s | %s%s%s | %s' % (
    i, r[0], r[1], (r[3] or '-')[:20], r[5], r[6], r[7], r[4]) for i, r in enumerate(rows)]
open(os.path.join(BASE, 'docs', '_safety_bench_cands.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('candidates:', len(rows))
