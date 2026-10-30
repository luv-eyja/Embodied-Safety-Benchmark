# -*- coding: utf-8 -*-
"""All library papers with benchmark-ish titles that are NOT yet in the table."""
import json, os, re

BASE = r'D:\study\Embodied'
lib = []
for f in ('papers', 'audited', 'screened'):
    lib += json.load(open(os.path.join(BASE, 'docs', '_data', f + '.json'), encoding='utf-8'))
rows = json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))
have = {r['title'].strip().lower() for r in rows}

seen, uniq = set(), []
for p in lib:
    k = (p.get('title') or '').strip().lower()
    if k in seen or k in have:
        continue
    seen.add(k)
    uniq.append(p)

BENCH_T = re.compile(r'bench|testbed|test bed|evaluation (?:platform|suite|framework|protocol)|'
                     r'\barena\b|\bsuite\b|leaderboard|challenge', re.I)
# 排除纯软件 agent / 非具身
NON_EMBODIED = re.compile(r'web agent|browser|mobile agent|code agent|software|database|sql|'
                          r'medical|clinical|chemistry|materials|finance|trading|'
                          r'chatbot|conversational|text-to-|recommendation', re.I)
EMBODIED = re.compile(r'robot|embodied|manipulat|drone|uav|humanoid|autonomous (?:vehicle|driving)|'
                      r'physical|cyber-?physical|vla|vlm|perception|navigation|locomotion|'
                      r'sensor|lidar|camera|point cloud|multi-agent|swarm', re.I)

out = []
for p in uniq:
    t = p.get('title') or ''
    if not BENCH_T.search(t):
        continue
    blob = t + ' ' + (p.get('abstract') or '')
    if NON_EMBODIED.search(t):
        continue
    if not EMBODIED.search(blob):
        continue
    out.append((p.get('year'), p.get('layer'), p.get('subcat'), t))

out.sort(key=lambda x: (str(x[0]), x[3]))
lines = ['%3d | %s | %-20s | %s' % (i, r[0], (r[2] or '-')[:20], r[3]) for i, r in enumerate(out)]
open(os.path.join(BASE, 'docs', '_bench_titles_left.txt'), 'w', encoding='utf-8').write('\n'.join(lines))
print('benchmark-titled, not in table:', len(out))
