# -*- coding: utf-8 -*-
"""Coverage matrix over the 121 benchmarks: stage x safety-property."""
import json, os, re, collections

BASE = r'D:\study\Embodied'
reg = json.load(open(os.path.join(BASE, 'docs', '_bench_registry.json'), encoding='utf-8'))
rows = {r['title']: r for r in json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))}

AXES = {
    '语义/指令安全': r'语义|semantic|语境|context|指令|language|歧义|歧义|指代|措辞|复述',
    '物理/接触安全': r'碰撞|接触|contact|碰撞|力|力矩|稳定|stability|形变|断裂|损伤|卫生|污染',
    '对抗/后门安全': r'对抗|adversar|攻击|attack|后门|backdoor|越狱|jailbreak|注入|inject|投毒|patch|补丁',
    '分布偏移鲁棒性': r'扰动|偏移|shift|鲁棒|robust|视角|光照|噪声|退化|硬件|标定|遮挡|退化',
    '失败恢复': r'失败|failure|恢复|recover|纠正|correct|回滚|rollback',
    '实时/治理': r'实时|real-time|延迟|latency|治理|governance|权限|审计|授权|监控|monitor',
}
STAGES = {
    '感知层': r'感知|视觉|visual|perception|观测|遮挡|相机|camera',
    '认知/语义层': r'语义|认知|指令|language|推理|reasoning|知识|context|歧义',
    '规划层': r'规划|plan|计划|task planning|长时程|long-horizon|子目标',
    '动作控制层': r'控制|动作|action|操作|manipulat|轨迹|trajectory|执行',
    '终态/后果层': r'终态|final|稳定|stability|残留|损伤|damage|污染|碰撞后',
}

stat = {s: collections.Counter() for s in list(STAGES) + ['未标注']}
detail = collections.defaultdict(list)

for name, info in reg.items():
    src = [p for p in info['papers'] if p['self']] or info['papers']
    r = rows.get(src[0]['title'], {})
    blob = ' '.join([info['desc'], r.get('dim', ''), r.get('summ', ''), name])
    hit_s = [s for s, p in STAGES.items() if re.search(p, blob, re.I)]
    hit_a = [a for a, p in AXES.items() if re.search(p, blob, re.I)]
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
