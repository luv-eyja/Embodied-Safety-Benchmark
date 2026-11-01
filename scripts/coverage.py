# -*- coding: utf-8 -*-
"""Coverage matrix over the 121 benchmarks: stage x safety-property."""
import json, os, collections

from benchmark_ontology import AXES, STAGES, classify

BASE = r'D:\study\Embodied'
REPO = os.path.join(BASE, 'Embodied-Safety-Benchmark')
reg = json.load(open(os.path.join(BASE, 'docs', '_bench_registry.json'), encoding='utf-8'))
rows = {r['title']: r for r in json.load(open(os.path.join(REPO, 'data', 'rows.json'), encoding='utf-8'))}

stat = {s: collections.Counter() for s in list(STAGES) + ['未标注']}
detail = collections.defaultdict(list)

for name, info in reg.items():
    hit_s, hit_a = classify(name, info, rows)
    for s in hit_s or ['未标注']:
        for a in hit_a or ['未标注']:
            stat[s][a] += 1
    detail[name] = (hit_s, hit_a)

print('基准总数:', len(reg))
print()
hdr = ['环节'] + list(AXES) + ['合计']
print(' | '.join(h.rjust(12) for h in hdr))
for s in STAGES:
    row = [s] + [str(stat[s][a]).rjust(12) for a in AXES] + [str(sum(stat[s][a] for a in AXES)).rjust(12)]
    print(' | '.join(row))
print()
tot = collections.Counter()
for s in stat:
    for a in AXES:
        tot[a] += stat[s][a]
print('各安全属性覆盖数（含重复计数）:', dict(tot))

# 同时覆盖 >=4 个属性的基准
multi = [(n, len(a)) for n, (s, a) in detail.items() if len(a) >= 4]
print('\n覆盖 4 个及以上安全属性的基准:', len(multi))
for n, k in sorted(multi, key=lambda x: -x[1])[:15]:
    print('  %d维  %s' % (k, n))
json.dump({k: {'stages': v[0], 'axes': v[1]} for k, v in detail.items()},
          open(os.path.join(BASE, 'docs', '_coverage.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
