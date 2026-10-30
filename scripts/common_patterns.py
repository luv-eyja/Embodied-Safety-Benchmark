# -*- coding: utf-8 -*-
"""Quantify structural commonalities across the 121 benchmarks."""
import json, os, re, collections, statistics

BASE = r'D:\study\Embodied'
REPO = os.path.join(BASE, 'Embodied-Safety-Benchmark')
reg = json.load(open(os.path.join(BASE, 'docs', '_bench_registry.json'), encoding='utf-8'))
rows = {r['title']: r for r in json.load(open(os.path.join(REPO, 'data', 'rows.json'), encoding='utf-8'))}

recs = []
for name, info in reg.items():
    src = [p for p in info['papers'] if p['self']]
    r = rows.get((src[0]['title'] if src else info['papers'][0]['title']), {})
    blob = ' '.join([name, info['desc'], r.get('dim', ''), r.get('summ', ''), r.get('obj', '')])
    recs.append({
        'name': name, 'tier': info['tier'], 'desc': info['desc'],
        'n_papers': len(info['papers']), 'n_others': len([p for p in info['papers'] if not p['self']]),
        'has_self': bool(src), 'year': r.get('year'), 'domain': r.get('domain') or '',
        'blob': blob, 'dim': r.get('dim', ''), 'summ': r.get('summ', ''),
    })

def pct(k, n):
    return '%.0f%%' % (100.0 * k / n) if n else '-'

N = len(recs)
print('基准数:', N)
print()

CHECKS = {
    '配对/孪生/对照设计': r'配对|孪生|twin|paired|matched|对照|同一场景|same-scene|controlled|控制变量',
    '形式化规约（LTL/STL/时序逻辑）': r'LTL|STL|时序逻辑|temporal logic|自动机|automaton|规约|specification',
    '使用 LLM 裁判': r'LLM-as-judge|LLM judge|judge|裁判|GPT-4o 打分|judged by',
    '真机验证': r'真机|real-world|real robot|physical robot|Franka|真实环境|硬件实验|real-robot',
    '过程级指标（代价/暴露时间/违规深度）': r'安全代价|累计.*代价|暴露时间|risk exposure|violation severity|VSI|SBU|过程|process-level|step-level',
    '只报成功率类单一指标': r'成功率|success rate|SR\b|ASR|完成率|accuracy',
    '对抗/攻击注入': r'攻击|对抗|adversar|attack|backdoor|jailbreak|注入',
    '注入式失败/故障': r'失败注入|failure inject|corrupt|退化|故障|fault|黑屏|遮挡',
    '跨本体': r'跨本体|cross-embodiment|多本体|multi-embodiment|embodiment',
    '实时/延迟约束': r'实时|real-time|延迟|latency',
    '统计检验/置信区间': r'统计检验|significance|置信区间|confidence interval|bootstrap|McNemar|p\s*<',
}
print('=== 构建与评测手法的出现频次（关键词检出，下界）===')
cnt = {}
for k, pat in CHECKS.items():
    c = sum(1 for r in recs if re.search(pat, r['blob'], re.I))
    cnt[k] = c
    print('%-38s %3d  %s' % (k, c, pct(c, N)))

print()
PLATFORMS = ['LIBERO', 'RoboTwin', 'RoboCasa', 'BEHAVIOR', 'ManiSkill', 'Isaac',
             'OmniGibson', 'SAPIEN', 'MuJoCo', 'Habitat', 'CARLA', 'SUMO', 'nuScenes', 'NAVSIM']
print('=== 平台依赖 ===')
for p in PLATFORMS:
    c = sum(1 for r in recs if re.search(p, r['blob'], re.I))
    if c:
        print('%-14s %3d  %s' % (p, c, pct(c, N)))

print()
print('=== 复用情况 ===')
one = sum(1 for r in recs if r['n_papers'] == 1)
print('仅 1 篇论文（提出者自己）:', one, pct(one, N))
print('被 >=2 篇使用:', N - one, pct(N - one, N))
print('被 >=3 篇使用:', sum(1 for r in recs if r['n_papers'] >= 3))

print()
print('=== 规模数字抽取（从描述里抓到的任务/场景/回合数）===')
nums = []
for r in recs:
    m = re.findall(r'(\d[\d,]{1,7})\s*(?:个)?\s*(?:任务|场景|实例|案例|回合|episodes|tasks|scenarios|cases|settings)', r['blob'], re.I)
    if m:
        v = max(int(x.replace(',', '')) for x in m)
        nums.append((v, r['name']))
nums.sort(reverse=True)
print('可解析出规模数字的基准:', len(nums), pct(len(nums), N))
if nums:
    vals = [v for v, _ in nums]
    print('规模中位数:', statistics.median(vals), '最大:', max(vals))
    print('Top 8:', [(n, v) for v, n in nums[:8]])

print()
print('=== 年份分布 ===')
yc = collections.Counter(r['year'] for r in recs)
for y in sorted(yc):
    print('  %s: %d' % (y, yc[y]))

print()
print('=== 分类分布 ===')
tc = collections.Counter(r['tier'] for r in recs)
for k, v in tc.most_common():
    print('  %-12s %d' % (k, v))
