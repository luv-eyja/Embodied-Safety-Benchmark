# -*- coding: utf-8 -*-
"""Render the coverage matrix as a Markdown appendix."""
import json, os, collections

from benchmark_ontology import AXES, STAGES, classify

BASE = r'D:\study\Embodied'
REPO = os.path.join(BASE, 'Embodied-Safety-Benchmark')
reg = json.load(open(os.path.join(BASE, 'docs', '_bench_registry.json'), encoding='utf-8'))
rows = {r['title']: r for r in json.load(open(os.path.join(REPO, 'data', 'rows.json'), encoding='utf-8'))}

detail = {}
stat = {s: collections.Counter() for s in list(STAGES) + ['未标注']}
for name, info in reg.items():
    hs, ha = classify(name, info, rows)
    for s in hs:
        for a in ha:
            stat[s][a] += 1
    detail[name] = (hs, ha)

benchmark_count = len(reg)
stage_pair_counts = {s: sum(stat[s].values()) for s in STAGES}
axis_pair_counts = {a: sum(stat[s][a] for s in STAGES) for a in AXES}

L = ['# 附录：%d 个基准的覆盖矩阵' % benchmark_count, '',
     '本文件由 `scripts/coverage.py` 生成，用于支撑设计方案 §1.1 的缺口论证。', '',
     '## 统计口径', '',
     '- 对每个基准，取「提出论文」的 *评测维度* + *内容概要* + 基准定位描述，做关键词匹配',
     '- 一个基准可同时命中多个环节与多个安全属性，因此**行合计大于基准数**，属性合计为重复计数',
     '- 用途仅在于看**相对稀疏度**，不作为精确计量', '',
     '## 环节 × 安全属性', '',
     '| 环节 | ' + ' | '.join(AXES) + ' | 合计 |',
     '|---|' + '---|' * (len(AXES) + 1)]

for s in STAGES:
    cells = [str(stat[s][a]) for a in AXES]
    L.append('| %s | %s | **%d** |' % (s, ' | '.join(cells), sum(stat[s][a] for a in AXES)))

tot = collections.Counter()
for s in stat:
    for a in AXES:
        tot[a] += stat[s][a]
L.append('| **合计** | %s | %d |' % (' | '.join('**%d**' % tot[a] for a in AXES), sum(tot.values())))
L += ['', '## 关键读数', '',
      '- **终态/后果层仅 %d 个**（%d 个中），其中 %d 个触及物理/接触安全 —— 这是最大的空白' % (
          stage_pair_counts['终态/后果层'], benchmark_count, stat['终态/后果层']['物理/接触安全']),
      '- **实时/治理仅 %d 个**，真正把决策延迟当一等变量的只有 RT-Safe（城市导航）' % axis_pair_counts['实时/治理'],
      '- **规划层 %d 个**，是各环节中最稀疏的' % stage_pair_counts['规划层'],
      '- **对抗/后门 %d 个**，且多为攻击方法自带评测，不是可复用基准' % axis_pair_counts['对抗/后门安全'], '',
      '## 覆盖 4 类及以上安全属性的基准', '']
multi = [(n, len(a)) for n, (s, a) in detail.items() if len(a) >= 4]
L += ['| 基准 | 覆盖属性数 |', '|---|---|']
for n, k in sorted(multi, key=lambda x: -x[1]):
    L.append('| %s | %d |' % (n, k))
L += ['', '> 结论：**%d 个基准中只有 %d 个同时覆盖 4 类以上安全属性**，' % (benchmark_count, len(multi)),
      '没有任何一个覆盖全部 6 类。这直接支撑了设计方案 §1.1 的判断。', '',
      '## 覆盖 3 类安全属性的基准', '']
three = [n for n, (s, a) in detail.items() if len(a) == 3]
L.append('、'.join(sorted(three)) if three else '（无）')

open(os.path.join(REPO, 'design', 'coverage-matrix.md'), 'w', encoding='utf-8').write('\n'.join(L))
print('written; multi-axis benchmarks:', len(multi))
