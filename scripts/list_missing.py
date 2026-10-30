# -*- coding: utf-8 -*-
"""List VLA-related library papers NOT yet in the table, for manual review."""
import json, os, re

BASE = r'D:\study\Embodied'
lib = []
for f in ('papers', 'audited', 'screened'):
    lib += json.load(open(os.path.join(BASE, 'docs', '_data', f + '.json'), encoding='utf-8'))

have = {r['title'].strip().lower() for r in json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))}

seen = set()
uniq = []
for p in lib:
    k = (p.get('title') or '').strip().lower()
    if k in seen or k in have:
        continue
    seen.add(k)
    uniq.append(p)

VLA = re.compile(r'\bvla\b|vision-language-action|vision language action|vision-language action|'
                 r'vision-language-action|language-conditioned polic|vision-language polic|'
                 r'robot foundation model|embodied foundation model|generalist polic|'
                 r'world[- ]action model|\bwam\b', re.I)

cand = [p for p in uniq if VLA.search((p.get('title') or '') + ' ' + (p.get('abstract') or ''))]
cand.sort(key=lambda p: (str(p.get('year')), p.get('title') or ''))

out = []
for i, p in enumerate(cand):
    ab = re.sub(r'\s+', ' ', (p.get('abstract') or ''))[:300]
    out.append('[%d] %s | %s | %s/%s | %s\n    %s\n' % (
        i, p.get('year'), p.get('tier'), p.get('layer'), p.get('subcat'),
        p.get('title'), ab))

open(os.path.join(BASE, 'docs', '_review_vla.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('candidates not yet in table:', len(cand))
