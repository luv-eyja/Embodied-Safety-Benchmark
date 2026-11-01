# -*- coding: utf-8 -*-
"""Build benchmark registry: for each benchmark, which table papers use/report it."""
import json, os, re, collections

BASE = r'D:\study\Embodied'
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))

# 人工核验的提出来源。对于“提出论文已在本库、但 benchmark 名称只出现在摘要中”的条目，
# 用 source_title 补足 self 角色，避免把提出论文误报成仅使用论文。
_audit_path = os.path.join(REPO, 'data', 'benchmark_source_audit.json')
SOURCE_AUDIT = {}
if os.path.exists(_audit_path):
    with open(_audit_path, encoding='utf-8') as _f:
        SOURCE_AUDIT = json.load(_f).get('entries', {})

# 论文全文语料（用于判定「用到了哪个基准」）
lib = {}
for f in ('papers', 'audited', 'screened'):
    for p in json.load(open(os.path.join(BASE, 'docs', '_data', f + '.json'), encoding='utf-8')):
        lib.setdefault(p['title'].strip().lower(), p)

ext_abs = {}
for f in ('_external_abs.json', '_oa_more.json'):
    fp = os.path.join(BASE, 'docs', f)
    if not os.path.exists(fp):
        continue
    d = json.load(open(fp, encoding='utf-8'))
    for k, v in d.items():
        if isinstance(v, dict):
            ext_abs[(v.get('title') or '').lower()] = v.get('abstract') or ''
        elif isinstance(v, list):
            for r in v:
                ext_abs[(r.get('title') or '').lower()] = r.get('abstract') or ''

for r in rows:
    t = r['title'].strip().lower()
    p = lib.get(t)
    r['abstract'] = (p.get('abstract') if p else '') or ext_abs.get(t, '') or ''

# 基准名 -> (正则, 层级, 简述用途)  层级用于文档分类
BENCH = [
    # ── VLA 安全 ──
    ('HazardArena', r'HazardArena', 'VLA 安全', 'VLA 语义安全（安全/不安全孪生场景）'),
    ('SafeStage', r'SafeStage', 'VLA 安全', '操作全生命周期三阶段安全'),
    ('SafeVLA-Bench', r'SafeVLA-Bench', 'VLA 安全', 'STL 不变式下的成功-安全落差'),
    ('ForesightSafety-VLA', r'ForesightSafety-VLA', 'VLA 安全', '13 类安全 taxonomy 诊断基准'),
    ('ManiGuard-Bench', r'ManiGuard', 'VLA 安全', 'LTL_f 规约接地的操作安全'),
    ('SafeLIBERO', r'SafeLIBERO', 'VLA 安全', '安全关键操作（碰撞风险）'),
    ('ManiPhysicsBench', r'ManiPhysicsBench', 'VLA 安全', '物体保全的物理损伤评估'),
    ('VLA-Arena', r'VLA-Arena', 'VLA 安全', '四维任务结构的难度梯度（含 Safety 套件）'),
    ('ASIMOV Benchmark', r'ASIMOV', 'VLA 安全', '语义安全与机器人宪法'),
    ('RoboHarm', r'RoboHarm', 'VLA 安全', '有害机器人指令下的拒答率'),
    ('Trap-LIBERO / Trap-RoboTwin', r'Trap-LIBERO|Trap-RoboTwin', 'VLA 安全', '配置化失败后门'),

    # ── VLA 鲁棒性 ──
    ('LIBERO-Plus', r'LIBERO-Plus|LIBERO\+', 'VLA 鲁棒性', '七维扰动鲁棒性分析'),
    ('LIBERO-Pro2.0', r'LIBERO-Pro(?:2\.0)?', 'VLA 鲁棒性', '6 维度扰动 + 运行时干预'),
    ('LIBERO-RIG', r'LIBERO-RIG', 'VLA 鲁棒性', '11 条硬件扰动轴'),
    ('LIBERO-VPro', r'LIBERO-VPro', 'VLA 鲁棒性', '闭环视觉鲁棒性'),
    ('LIBERO-MAX', r'LIBERO-MAX', 'VLA 鲁棒性', '任务中途世界变化'),
    ('LIBERO-RECOVER', r'LIBERO-RECOVER', 'VLA 鲁棒性', '失败识别与恢复'),
    ('LIBERO-CTRL', r'LIBERO-CTRL', 'VLA 鲁棒性', '单轴 vs 复合扰动配对'),
    ('LIBERO-X', r'LIBERO-X', 'VLA 鲁棒性', '分层难度鲁棒性试金石'),
    ('LIBERO-Para', r'LIBERO-Para', 'VLA 鲁棒性', '指令复述敏感性'),
    ('RoboCasa-Shift', r'RoboCasa-Shift', 'VLA 鲁棒性', '阶段感知鲁棒性'),
    ('VLA-GAUGE', r'VLA-GAUGE', 'VLA 鲁棒性', '泛化 + 鲁棒性统一诊断'),
    ('VLA-Retain', r'VLA-Retain', 'VLA 鲁棒性', '视觉微调的跨维度影响'),
    ('RoboStress', r'RoboStress', 'VLA 鲁棒性', '执行误差压力测试'),
    ('BAVO-Bench', r'BAVO-Bench', 'VLA 鲁棒性', '遮挡下的主动视觉恢复'),
    ('DriveDegrade', r'DriveDegrade', 'VLA 鲁棒性', '图像退化容忍度（驾驶）'),
    ('VLN-Safe', r'VLN-Safe', 'VLA 鲁棒性', 'VLN 碰撞安全（滑行/阻塞）'),

    # ── VLA 能力 ──
    ('LIBERO（基础套件）', r'\bLIBERO\b(?!\s*[-–])|LIBERO-(?:Spatial|Object|Goal|Long|90|10)\b', 'VLA 能力', '终身学习与知识迁移（130 任务）'),
    ('CALVIN', r'\bCALVIN\b', 'VLA 能力', '语言条件长时程指令链'),
    ('SimplerEnv', r'SimplerEnv|SIMPLER\b', 'VLA 能力', '真机策略的仿真评测'),
    ('RoboCasa', r'\bRoboCasa\b', 'VLA 能力', '日常场景大规模仿真'),
    ('RoboCasa365', r'RoboCasa365', 'VLA 能力', '大规模日常任务训练与评测'),
    ('RoboTwin', r'\bRoboTwin\b', 'VLA 能力', '生成式数字孪生双臂基准'),
    ('VLABench', r'\bVLABench\b', 'VLA 能力', '长时程推理语言条件操作'),
    ('COLOSSEUM', r'COLOSSEUM', 'VLA 能力', '环境扰动下的泛化边界'),
    ('RoboMIND', r'\bRoboMIND\b', 'VLA 能力', '多本体操作'),
    ('ManiSkill / ManiSkill2', r'ManiSkill', 'VLA 能力', '可泛化操作技能统一基准'),
    ('BEHAVIOR-1K', r'BEHAVIOR-1K|BEHAVIOR-?Suite|BEHAVIOR-\d', 'VLA 能力', '家务长时程活动'),
    ('AgiBot World', r'AgiBot World', 'VLA 能力', '百万轨迹真机平台'),
    ('Open X-Embodiment', r'Open X-Embodiment|OpenX-Embodiment|\bOXE\b', 'VLA 能力', '跨本体真机数据'),
    ('RoboDojo', r'RoboDojo', 'VLA 能力', '42 任务真机评测'),
    ('RoboColiseum', r'RoboColiseum', 'VLA 能力', '前沿模型四条赛道评测'),
    ('Spa-Bench', r'Spa-Bench', 'VLA 能力', '空间接地真机基准'),
    ('RoboIRG-Bench', r'RoboIRG-?Bench', 'VLA 能力', '隐式指代接地'),
    ('RoboFollow', r'RoboFollow', 'VLA 能力', '高场景熵指令遵循诊断'),
    ('IndustrialVLA-Bench', r'IndustrialVLA-Bench', 'VLA 能力', 'VLA/WAM 多轴可追溯评测'),
    ('BiDex-100', r'BiDex-100', 'VLA 能力', '双手灵巧操作 106 任务'),
    ('ManiUnit', r'\bManiUnit\b', 'VLA 能力', '长时程移动操作技能'),
    ('X2Real', r'X2Real', 'VLA 能力', '可演化仿真基准'),
    ('RoboComb', r'RoboComb', 'VLA 能力', '技能组合泛化'),
    ('LongBench', r'\bLongBench\b', 'VLA 能力', '真机长时程操作'),
    ('PolaRiS', r'PolaRiS', 'VLA 能力', 'real-to-sim 可扩展评测'),
    ('RoboEval', r'RoboEval|Robo Eval', 'VLA 能力', '结构化行为指标（双臂）'),
    ('RoboChrono', r'RoboChrono', 'VLA 能力', '流式任务理解'),
    ('RoboVista', r'RoboVista', 'VLA 能力', 'VLM 空间理解 VQA'),
    ('RoboReel', r'RoboReel', 'VLA 能力', '从观察学习（LfO）'),
    ('HUGE-Bench', r'HUGE-Bench', 'VLA 能力', '无人机高层 VLA 任务'),
    ('Robo2Process', r'Robo2Process', 'VLA 能力', '过程感知理解'),

    # ── 具身智能体安全 ──
    ('AGENTSAFE / SAFE-THOR', r'AGENTSAFE|SAFE-THOR|SAFE-VERSE', '具身智能体安全', '危险指令下的智能体安全'),
    ('IS-Bench', r'IS-Bench', '具身智能体安全', '交互安全（过程导向）'),
    ('SafeAgentBench', r'SafeAgentBench', '具身智能体安全', '安全任务规划'),
    ('SafePlan-Bench / Safe-Align', r'SafePlan-Bench|Safe-BeAl', '具身智能体安全', '任务规划安全测量与对齐'),
    ('SafeMindBench', r'SafeMind', '具身智能体安全', '四阶段安全推理'),
    ('VestaBench', r'VestaBench', '具身智能体安全', '多约束与对抗下的安全长时程规划'),
    ('HASARD', r'HASARD', '具身智能体安全', '视觉安全强化学习'),
    ('EmbodiedBench', r'EmbodiedBench', '具身智能体安全', 'MLLM 具身智能体六能力'),
    ('Embodied Agent Interface', r'Embodied Agent Interface', '具身智能体安全', '具身决策模块化接口'),
    ('Agent-SafetyBench', r'Agent-SafetyBench', '具身智能体安全', 'LLM 智能体安全'),
    ('RT-Safe', r'RT-Safe|RT-SAFE', '具身智能体安全', '实时约束下的具身安全'),
    ('CAPSafe', r'CAPSafe', '具身智能体安全', '动作级 + 计划级安全推理'),
    ('GuardianBench', r'GuardianBench', '具身智能体安全', '同场景指令对比的潜在风险'),
    ('EmbodiedGovBench', r'EmbodiedGovBench', '具身智能体安全', '治理与演进安全'),
    ('RoboAbstention', r'RoboAbstention', '具身智能体安全', '弃权能力评测'),
    ('MAGMA-Bench', r'MAGMA-Bench', '具身智能体安全', '动态多机器人长时程推理'),
    ('MMA-SafetyBench', r'MMA-SafetyBench', '具身智能体安全', '视觉语义劫持'),
    ('RoboJailBench', r'RoboJailBench', '具身智能体安全', '越狱攻防（安全-有用性权衡）'),
    ('Inspect Robots', r'Inspect Robots', '具身智能体安全', '能力与安全评测框架'),
    ('DESPITE', r'DESPITE', '具身智能体安全', '具身规划的系统性安全风险'),
    ('TSHA', r'\bTSHA\b', '具身智能体安全', '家庭安全隐患评估'),
    ('MineAmongUs', r'MineAmongUs', '具身智能体安全', '具身社交欺骗'),
    ('STARS', r'\bSTARS\b', '具身智能体安全', '社会导航时空推理'),
    ('MemForm', r'MemForm', '具身智能体安全', '记忆形成投毒'),
    ('SkillSafetyBench', r'SkillSafetyBench', '具身智能体安全', '技能攻击面'),
    ('PASTABench', r'PASTABench', '具身智能体安全', '序贯轨迹主动安全监控'),
    ('ORBIT', r'\bORBIT\b', '具身智能体安全', '多智能体安全评测框架'),
    ('DUMA-Bench', r'DUMA-Bench', '具身智能体安全', '双控多智能体安全'),
    ('BLINDSPOT', r'BLINDSPOT', '具身智能体安全', '轨迹级安全与拒答校准'),
    ('INFUSE', r'INFUSE', '具身智能体安全', '间接提示注入全生命周期'),
    ('TALK-Dem', r'TALK-Dem', '具身智能体安全', '痴呆症沟通模式下的规划'),
    ('PhysAI-Bench', r'PhysAI-Bench', '具身智能体安全', 'UAV 智能体决策'),
    ('AeroIntent', r'AeroIntent', '具身智能体安全', 'UAV 任务意图识别'),
    ('PLCBENCH', r'PLCBENCH|PLCBench', '具身智能体安全', 'PLC 到物理影响（HIL）'),
    ('Words to World', r'Words to World', '具身智能体安全', '真实物理闭环交互'),
    ('HygieneRoboBench', r'HygieneRoboBench', '具身智能体安全', '卫生感知规划'),
    ('REVERSAL-BENCH', r'REVERSAL-BENCH', '具身智能体安全', '无重置 RL 可逆性'),
    ('MemTransfer', r'MemTransfer', '具身智能体安全', '记忆迁移'),
    ('GaugeBench', r'GaugeBench', '具身智能体安全', '表示鲁棒性（形态描述）'),
    ('ORDER', r'\bORDER\b(?!\s+by)', '具身智能体安全', '虚构世界领域适配'),
    ('LABIT', r'\bLABIT\b', '具身智能体安全', '工业长时程装配'),
    ('Peg-in-Bench', r'Peg-in-Bench', '具身智能体安全', '高精度插入'),
    ('Bench2Dex', r'Bench2Dex', '具身智能体安全', '跨灵巧手视触觉'),
    ('MSK-Bench', r'MSK-Bench', '具身智能体安全', '全身肌肉骨骼控制'),
    ('MotionForge', r'MotionForge', '具身智能体安全', '动态物体长时程操作'),
    ('RoboVAD', r'RoboVAD', '具身智能体安全', '机械臂操作视频异常检测'),

    # ── 具身安全（非 VLA，含自动驾驶/多机器人/人机）──
    ('SafeBench', r'SafeBench(?!.*LLM)', '具身安全', '自动驾驶安全评测平台'),
    ('Bench2Drive', r'Bench2Drive', '具身安全', '闭环端到端驾驶多能力'),
    ('NAVSIM', r'NAVSIM|NavSim', '具身安全', '数据驱动非反应式仿真'),
    ('CARLA / CARLA Leaderboard', r'\bCARLA\b', '具身安全', '城市驾驶仿真与排行榜'),
    ('nuScenes', r'nuScenes', '具身安全', '真实驾驶数据集（开环）'),
    ('ExceptionDrive', r'ExceptionDrive', '具身安全', '反事实边角案例'),
    ('TrafficSignBench', r'TrafficSignBench', '具身安全', '交通标志合规闭环'),
    ('VIPS', r'\bVIPS\b', '具身安全', '车路协同规划（伪仿真）'),
    ('Radar2Plan', r'Radar2Plan', '具身安全', '4D 雷达开环轨迹规划'),
    ('SIREN-Bench', r'SIREN-Bench', '具身安全', '紧急车辆交互'),
    ('DPed-VLN', r'DPed-VLN', '具身安全', '动态行人 VLN 社会安全'),
    ('R2R-CE', r'R2R-CE', '具身安全', '连续环境 VLN'),
    ('Balanced Multi-Robot Task Allocation Benchmark', r'Decentralized Multi-Robot Task Allocation', '具身安全', '通信退化下 MRTA'),
    ('Physics-Consistent HRI Benchmark', r'A Physics-Consistent Benchmark', '具身安全', '接触密集人机交互（助浴）'),
    ('ISO-based Humanoid Orchestrator Benchmark', r'How Long Until Your Robot Ignores You', '具身安全', '人形协作 LLM 编排器'),
    ('Everyday-Environment Robot Benchmarking', r'Benchmarking Robots for Everyday Environments', '具身安全', '公共环境真实部署'),
    ('COMPASS / X-Mobility', r'COMPASS', '具身安全', '学习型导航 sim-to-real'),
]

CASE_SENSITIVE = {
    'DESPITE', 'ORDER', 'COMPASS / X-Mobility', 'ORBIT', 'INFUSE', 'STARS',
    'BLINDSPOT', 'VIPS', 'R2R-CE', 'MineAmongUs', 'RoboHarm',
}

reg = {}
for name, pat, tier, desc in BENCH:
    # 缩写/易撞常用词的名称必须大小写敏感，否则 DESPITE / ORDER 会命中英文常用词
    flags = 0 if name in CASE_SENSITIVE else re.I
    rx = re.compile(pat, flags)
    users = []
    audit = SOURCE_AUDIT.get(name, {})
    source_title = audit.get('source_title') if audit.get('kind') == 'same_paper_in_registry' else None
    for r in rows:
        if rx.search(r['title']) or rx.search(r.get('abstract') or ''):
            users.append({'title': r['title'], 'zh': r['zh'], 'year': r['year'],
                          'venue': r['venue'], 'cat': r['cat'], 'link': r['link'],
                          'src': r['src'],
                          'self': bool(rx.search(r['title'])) or bool(source_title and r['title'] == source_title)})
    if users:
        reg[name] = {'tier': tier, 'desc': desc, 'papers': users}

json.dump(reg, open(os.path.join(BASE, 'docs', '_bench_registry.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
by_tier = collections.Counter(v['tier'] for v in reg.values())
print('benchmarks with >=1 paper:', len(reg))
for k, v in by_tier.most_common():
    print(' ', k, v)
print('\n单篇基准（只有自己）：',
      sum(1 for v in reg.values() if len(v['papers']) == 1))
