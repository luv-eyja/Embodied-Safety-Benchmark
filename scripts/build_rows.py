# -*- coding: utf-8 -*-
"""Build the VLA benchmark survey workbook."""
import json, os, re

BASE = r'D:\study\Embodied'

lib = []
for _f in ('papers', 'audited', 'screened'):
    lib += json.load(open(os.path.join(BASE, 'docs', '_data', _f + '.json'), encoding='utf-8'))


def find(key):
    kl = key.lower()
    hits = [p for p in lib if kl in (p.get('title') or '').lower()]
    if not hits:
        raise KeyError(key)
    order = {'curated': 0, 'audited': 1, 'screened': 2}

    def rank(p):
        t = (p.get('title') or '')
        if t.startswith(key):                      # 大小写完全一致的前缀
            pri = 0
        elif re.match(r'^%s\b' % re.escape(kl), t.lower()):   # 词边界匹配
            pri = 1
        else:                                      # 仅包含
            pri = 2
        return (pri, order.get(p.get('tier'), 9), -int(p.get('year') or 0))

    hits.sort(key=rank)
    return hits[0]


VENUE_MAP = {
    'NeurIPS': 'NeurIPS %s（神经信息处理系统大会）',
    'ICLR': 'ICLR %s（国际学习表征会议）',
    'ICCV': 'ICCV %s（IEEE/CVF 国际计算机视觉大会）',
    'EMNLP': 'EMNLP %s（自然语言处理经验方法会议）',
}

# (title_key, 类别, 中文题名, 评测对象, 维度与指标, 概要, venue_override)
LIB_ROWS = [
    # ── A. VLA 安全专用 Benchmark ──────────────────────────────────────────
    ('HazardArena', 'VLA 安全 Benchmark',
     'HazardArena：VLA 语义安全基准',
     'VLA 策略（操作类）',
     '语义安全；安全/不安全孪生场景下的动作选择正确率',
     '针对「动作执行正确但语义语境危险」这一系统性漏洞，构造物体、布局与动作要求完全一致、仅语义语境不同的安全/不安全孪生场景。发现仅在安全场景上训练的 VLA 在语义风险下往往无法保持安全，说明 VLA 的动作策略与视觉-语言语义耦合松散。',
     None),
    ('SafeStage', 'VLA 安全 Benchmark',
     'SafeStage：操作全生命周期安全基准',
     '视觉-语言条件机器人策略（VLA）',
     '三阶段安全：初始状态危害 / 执行期安全 / 终态危害',
     '把操作安全拆成「做之前、做的过程中、做完之后」三阶段，97 个专门设计的风险场景分别考察必须先行化解的初始状态危害、执行期的不安全接触/轨迹/区域进入/物体交互，以及名义任务完成后残留的不稳定或不安全状态，用于定位安全究竟在闭环操作的哪一环失效。',
     None),
    ('LIBERO-Plus', 'VLA 鲁棒性 Benchmark',
     'LIBERO-Plus：VLA 七维扰动鲁棒性分析',
     'VLA 基础模型（多个 SOTA）',
     '7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声',
     '对多个 SOTA VLA 施加受控扰动做系统脆弱性分析，揭示「表面胜任」下的脆弱：相机视角与机器人初始状态轻微扰动即可使成功率从约 95% 跌至 30% 以下，而模型对语言变化反而不敏感（进一步实验表明模型倾向忽略指令）。是当前最常被复用的 VLA 鲁棒性诊断基准之一。',
     None),
    ('LIBERO-X', 'VLA 鲁棒性 Benchmark',
     'LIBERO-X：VLA 分层鲁棒性试金石',
     'VLA 模型',
     '分层评测协议：空间泛化 / 物体识别 / 指令理解；配套高多样性示教数据',
     '指出既有基准因评测协议不足而对 VLA 能力给出有限甚至误导性判断，因而从评测与数据两方面重构：设计逐级加难的分层评测协议，对空间泛化、物体识别、任务指令理解三项核心能力分别度量，并采集高多样性人工遥操作数据，用于细粒度刻画性能随环境与任务复杂度的衰减。',
     None),
    ('LIBERO-Pro2.0', 'VLA 鲁棒性 Benchmark',
     'LIBERO-Pro2.0：具身基础模型鲁棒性基准',
     '具身基础模型 / VLA',
     '6 维度 22 种静态扰动 + 20 种运行时干预，1648 个偏移任务实例',
     '针对「LIBERO 高分不等于鲁棒」的问题，按条件、环境、观测、执行、机器人状态配置、语言六个维度构建 22 种静态扰动与 20 种运行时干预，生成 1648 个经六轮校验的偏移任务实例，并采集 39390 条轨迹支持面向鲁棒性的训练与评测。',
     None),
    ('LIBERO-RIG', 'VLA 鲁棒性 Benchmark',
     'LIBERO-RIG：硬件部署配置鲁棒性基准',
     'VLA 模型（9 个近期模型）',
     '11 条硬件扰动轴 × 5 个严重度 = 210 种条件；每条件 500 回合',
     '只扰动机器人自身硬件与部署配置（相机安装与光学、相机-机械臂标定、驱动增益、控制频率、本体感觉噪声、基座位姿、桌面高度、夹爪垫磨损等），完全固定 LIBERO 任务本身，从而把「任务分布偏移」与「硬件配置偏移」解耦。9 个 VLA 的汇总成功率在中等严重度降至 0.767、最高严重度降至 0.509，并配有统计检验。',
     None),
    ('LIBERO-VPro', 'VLA 鲁棒性 Benchmark',
     'LIBERO-VPro：闭环视觉鲁棒性基准',
     'VLA 与世界动作模型（WAM）',
     '视觉证据退化 / 相机陈旧 / 视觉源一致性 / 任务相关场景变化；12 类挑战 96 种设置',
     '标准基准默认执行过程中视觉观测干净、及时且一致，该基准专门扰动执行期的视觉证据：覆盖视觉证据退化、相机帧陈旧（staleness）、视觉源一致性与任务相关场景变化四个维度，共 12 类挑战、96 种设置、3296 个任务-条件案例，约 19.6 万仿真回合并辅以 200 次 Franka Research 3 真机 rollout。',
     None),
    ('LIBERO-MAX', 'VLA 鲁棒性 Benchmark',
     'LIBERO-MAX：任务中途变化的自适应基准',
     'VLA / 混合策略 / 世界动作模型（14 个策略）',
     '8 类中途事件；8000 对配对案例；事件前后成功率差',
     '关注「任务执行中世界发生变化」这一常被静态重置式基准忽略的时序挑战：8000 对配对案例覆盖几何、观测、外观、杂乱度与路径等 8 类中途事件，每对固定任务、初始状态、策略随机种子与事件前动作序列，从而把事件导致的退化与本就存在的失败分开；14 个策略在事件后成功率下降 11.0–25.7 个百分点。',
     None),
    ('LIBERO-RECOVER', 'VLA 鲁棒性 Benchmark',
     'LIBERO-RECOVER：失败恢复能力基准',
     'VLA 与世界动作模型',
     '失败识别与恢复成功率（相对纯任务成功率）',
     '指出 LIBERO 上已接近 100% 的成功率具有误导性：真实交互中必然出现抓取失败、碰撞与物体意外移动，机器人不仅要完成任务还要能识别并从中恢复，而这一能力此前基本未被度量。该基准在既有成功率之外补充失败恢复能力的评测，弥合基准成绩与真实可靠性之间的差距。',
     None),
    ('Beyond Single-Axis Testing', 'VLA 鲁棒性 Benchmark',
     'LIBERO-CTRL：复合鲁棒性配对评测',
     'VLA 策略',
     '单轴条件 vs 多轴同时条件的配对对比；涌现失败 / 补偿成功',
     '指出现有评测每次只施加一种扰动，而真实部署常同时存在多种偏移。基准给出六轴、每条初始状态都配「单轴条件 + 匹配的多轴同时条件」的配对设计，从而区分两类被总体成功率掩盖的现象：单轴全部成功而复合失败（涌现失败）、至少一个单轴失败而复合成功（补偿成功），说明复合鲁棒性不能由单轴结果简单推断。',
     None),
    ('RoboCasa-Shift', 'VLA 鲁棒性 Benchmark',
     'RoboCasa-Shift：长时程操作的阶段感知鲁棒性评测',
     'GR00T N1.5 等 VLA 策略',
     '单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度',
     '针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。',
     None),
    ('VLA-GAUGE', 'VLA 鲁棒性 Benchmark',
     'VLA-GAUGE：泛化与鲁棒性统一诊断框架',
     '12 个不同规模/动作建模范式的 VLA',
     '6 个能力套件的 ID/OOD 配对任务；单因子敏感度 + 组合扰动；诊断驱动改进',
     '把零样本泛化与扰动鲁棒性放进同一可执行任务表示下评测：用 6 个能力套件的分布内/分布外配对任务、单因子敏感度分析与组合扰动筛选、以及由诊断结果驱动的定向数据增强与微调，形成「诊断—改进」闭环；在统一协议下评测 12 个不同模型规模与动作建模范式的 VLA。',
     None),
    ('AttackVLA', '攻防评测框架',
     'AttackVLA：VLA 对抗与后门攻击统一评测',
     'VLA 模型（多种架构）',
     '数据构建/训练/推理三阶段的全谱系攻击；攻击成功率与真实场景有效性',
     '指出各 VLA 动作 tokenizer 不同导致攻击效果难以复现与公平比较、且多数攻击未在真实场景验证。框架对齐 VLA 开发生命周期（数据构建、模型训练、推理），统一动作 tokenizer 口径，集成针对 VLA 的既有攻击与适配的迁移攻击，并在真实环境中验证，为 VLA 攻防提供统一评测口径。',
     None),
    ('Manipulation Facing Threats', '攻防评测框架',
     'PVEP：端到端 VLA 物理脆弱性评测流水线',
     '端到端视觉-语言-动作模型（VLAM）',
     '视觉模态物理威胁：分布外、纹理/光照等；任务成功率与动作偏差',
     '结合多模态大模型安全研究与操作任务的实际场景，提出物理脆弱性评测流水线 PVEP，尽可能纳入视觉模态的物理威胁（分布外样本、纹理与光照变化等），系统评测端到端 VLA 模型在面对物理世界威胁时的鲁棒性与安全性。',
     'arXiv 预印本 (arXiv:2409.13174)'),
    ('VLSA', 'VLA 安全 Benchmark',
     'SafeLIBERO：安全关键操作基准（附 AEGIS 安全层）',
     'VLA + 安全约束层',
     '碰撞/安全违规率与指令遵循性能的权衡',
     '提出基于控制屏障函数的即插即用安全约束层 AEGIS，可与现有 VLA 直接组合并给出理论安全保证；为验证效果构建安全关键基准 SafeLIBERO，覆盖多种存在碰撞风险的操作场景，同时度量安全性与原有指令遵循性能。可作为「防御方法自带评测集」的典型样本。',
     None),
    ('TrapVLA', '攻防评测框架',
     'Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准',
     'VLA 模型',
     '配置失败保真度（如何失败）而非仅是否失败；四种失败模式',
     '提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。',
     None),
    ('Taming VLAs under Robot Execution Errors', 'VLA 鲁棒性 Benchmark',
     'RoboStress：执行误差压力测试基准',
     'VLA 策略',
     '7 种部署场景的执行误差；执行条件鲁棒性',
     '针对执行动作偏离指令（机械磨损、负载变化等导致）这一实际失效来源，提出部署期自补偿 VLA（无需任务奖励或标签，用指令动作与实际执行的残差在线更新策略）；并构建受控仿真基准 RoboStress，把摩擦、间隙、柔顺与重力补偿误差等关节级模型组合成 7 种部署场景，用于在物理机器人难以覆盖的执行条件下做鲁棒性压力测试。',
     None),
    ('ManiPhysicsBench', 'VLA 安全 Benchmark',
     'ManiPhysicsBench：物体保全的物理评测',
     '公开 VLA 检查点',
     '任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较',
     '指出刚体基准中的任务成功并不能说明模型是否保全了物体。ManiPhysicsZoo 汇总文献支撑的材质属性、3D 网格与参考文献形成可复用物体资产，再由基于求解器的评估依据几何、材质与抓取条件计算损伤阈值并与实测接触力比较，从而在 LIBERO 与 SimplerEnv 上区分「完成任务」与「安全完成任务」，公开 VLA 检查点在两者间存在显著差距。',
     None),
    ('Spa-Bench', 'VLA 能力 Benchmark',
     'Spa-Bench：VLA 空间接地真机基准',
     'VLA 模型',
     '六类空间描述（物体状态、相对大小、指代、关系放置、序数、计数）；ID/OOD 对比',
     '多数 VLA 评测只看物体、指令或环境变化下的总体操作成功率，难以判断策略能否把空间描述可靠地落到物理场景中。该真机基准覆盖物体状态、相对大小、指代描述、关系放置、序数位置与计数六类桌面任务，主要对比分布内与分布外表现，直接考察空间描述到行为的接地能力。',
     None),
    ('RoboIRGBench', 'VLA 能力 Benchmark',
     'RoboIRG-Bench：隐式指代接地基准',
     '不同记忆机制的 VLA',
     '直接 / 推理中介 / 空间 / 语境四类隐式指代',
     '既有基准通常假设任务相关信息在指令中被明确给出，而人类常以隐含方式指代物体、数量与关系。该基准把这一能力定义为隐式指代接地（IRG），基于 RoboMME 构建 40 个变体、覆盖 11 个任务与四类挑战，并评测采用不同记忆机制的代表性 VLA 在从语言与感知上下文恢复目标上的表现。',
     None),
    ('IndustrialVLA-Bench', 'VLA 能力 Benchmark',
     'IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测',
     '6 个已发布的 VLA 与世界动作模型（WAM）',
     '干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价',
     'VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。该基准在统一上报口径下对 6 个已发布系统分轴评测：LIBERO 上的干净能力、LIBERO-Plus 上的非语言鲁棒性、LIBERO-Para 上的指令敏感度以及实测执行代价，并聚合三个不同随机种子的完整评测。',
     None),
    ('VLA-Retain', 'VLA 鲁棒性 Benchmark',
     'VLA-Retain：视觉微调的跨维度影响基准',
     '5 个开源 VLA 及其微调检查点',
     '目标维度增益与目标外鲁棒性变化（分离遗忘与适配效应）',
     '针对「在目标域数据上微调视觉模块」这一常见做法，考察其在目标条件之外如何影响鲁棒性——既有鲁棒性基准只评测未微调模型，适配研究又只报告目标增益。该基准把 5 个开源 VLA 在相机视角或传感器噪声数据上微调后的检查点与其基座版本在 LIBERO-Plus 上对照，分离目标增益与目标外变化、适配效应与架构差异，并排除通用遗忘的干扰。',
     None),
    ('ROBORMBENCH', '评测方法与度量',
     'ROBORMBench：视觉语言奖励模型的复述脆弱性',
     '视觉语言奖励模型（VLM as reward）',
     '复述不变性：同一轨迹在语义等价目标描述下的奖励一致性',
     '视觉语言模型越来越多地充当机器人学习的奖励函数，这要求复述不变性：同一轨迹在语义等价的目标描述下应得同样奖励。该基准用 2390 条真机轨迹、真值进度标签与 21673 条经验证的复述（词汇、句法、动作目标改写）度量该性质，发现仅改写指令即可显著改变进度评分，甚至把同一行为在失败与成功之间翻转，且该不稳定不随模型规模或显式推理可靠降低。',
     None),
    ('Language2Drive', 'VLA 能力 Benchmark',
     'Language2Drive：驾驶 VLA 的指令遵循基准',
     '驾驶 VLA 模型',
     '配对反事实单元（固定场景只改指令）；四类指令遵循范围',
     '现有闭环驾驶基准主要度量路线完成度、安全性与规则符合度，却未回答「语言是否真正决定了车辆执行哪一种可行行为」。该基准以配对反事实单元为评测单位：固定初始驾驶场景、只改指令，从而把孤立的指令成功与配对反事实成功区分开，覆盖四种指令遵循范围，并可检验该区分是否在不同评测区间持续成立。',
     None),
    ('Successful but Unsafe', 'VLA 安全 Benchmark',
     'VLN-Safe：视觉语言导航碰撞安全基准',
     '视觉语言导航（VLN）智能体',
     '滑行 vs 阻塞两种评测机制下的成功率与接触率',
     'VLN 智能体通常只按「是否到达」与「路径效率」评测，几乎不反映碰撞行为；且连续 VLN 评测常用滑行机制，碰撞后可沿障碍滑动，掩盖不安全动作的后果。该基准在滑行与阻塞（碰撞动作禁止前进）两种机制下对比六个已发表智能体：R2R-CE 上 38.5–56.8% 的成功回合存在接触，改用阻塞机制后成功率下降 11.7–36.1 个百分点。',
     None),

    # ── B. 评测方法与诊断性研究 ────────────────────────────────────────────
    ('Validating, Not Sampling', '评测方法与度量',
     'H²V-M：区域级鲁棒性验证（非采样）',
     '6 个 VLM 与 5 个 VLA（Gemma/InternVL/LLaVA/Qwen；GR00T/OpenVLA/π 系列）',
     '连续扰动区域上的形式化验证；亮度偏移、相机旋转及其组合',
     '指出既有鲁棒性基准只是「采样」扰动，无法保证未测区域不存在失败。该工作对连续的光度与几何扰动区域（亮度偏移、相机旋转及其组合）做鲁棒性验证，覆盖 6 个 VLM 与 5 个 VLA，并提出 margin-aware 收敛规则 H²V-M，使 32B 参数规模下的验证在计算上可行。',
     None),
    ('Paraphrase Consensus', '评测方法与度量',
     '复述共识不等于自一致性：VLA 的指令依赖与鲁棒性',
     'OpenVLA 等 VLA 策略',
     '指令改写下的成功率；错误指令探针；复述共识与置信度选择',
     '揭示 LIBERO 微调与评测使用同十条指令串所带来的评测偏差：改写指令会使基座 OpenVLA 成功率下降 38.0 个点，测试期 prompt 集成无法恢复；取 K 条复述中位动作的「复述共识」在训练指令属于其中之一时反而再降 16.8 点，说明聚合只降低方差、去不掉复述共享的偏差。并提出错误指令探针度量策略对指令的依赖程度。',
     None),
    ('Encoded but Not in Control', '评测方法与度量',
     '编码但未受控：视觉-语言策略的指令接地缺口',
     'VLA 策略与世界动作模型（WAM）',
     '场景保持的指令干预：有效目标替换、任意名词、无关句子',
     '通过保持场景不变、只替换指令的干预实验回答「任务成功是否等于遵循指令」：当指令要求另一个可见物体时，所有被评测策略仍主要去抓取与场景绑定的原目标；并在仿真与真机上验证该现象，进一步分析其是否源于语言不敏感而非感知失败。',
     None),
    ('Do Vision-Language-Action Models Understand Instructions', '评测方法与度量',
     'VLA 真的理解指令吗：语言接地的机制可解释性研究',
     'π0.5、GR00T N1.7',
     '激活/归因修补（activation & attribution patching）；残差流干预',
     '在 VLA 缺乏显式接地模块、依赖视觉-语言主干固有能力的背景下，对 π0.5 与 GR00T N1.7 的动作生成模块残差流做受控机制可解释性研究：系统性破坏输入样本的任务指令，用激活与归因修补判断动作生成在多大程度上真正依赖语言，而非仅依赖视觉线索与表层相关性。',
     None),
    ('When Instructions Retrieve Trajectories', '评测方法与度量',
     '指令检索轨迹：VLA 泛化失败的诊断与缓解',
     '微调后的 π0.5、GR00T-N1.7',
     '反事实指令下的行为切换；指令-动作绑定（instruction-action binding）',
     '指出聚合鲁棒性分数会掩盖一种特定失败：策略同时响应语言与视觉，却不把两者结合来选择任务需要的动作——指令只是唤起熟悉的轨迹族，视觉反馈只调整其执行。行为分析显示失败回合常保留原任务行为或切换到另一已示范任务（说明语言并未被简单忽略），并通过读出与干预把这种选择关联到任务条件的内部状态。',
     None),
    ('Is Success All You Need', '评测方法与度量',
     '只有成功率够吗：扰动下 VLA 的行为鲁棒性度量',
     '3 个 SOTA VLA；LIBERO / LIBERO-Plus',
     '行为指标：运动平滑度、效率、夹爪行为及其变异性',
     '指出鲁棒性仍主要用任务成功率（TSR）衡量。该工作提出与基准无关的行为鲁棒性评测框架，刻画成功轨迹在扰动下「如何被执行」，包括运动平滑度、效率与夹爪行为等指标；在 LIBERO/LIBERO-Plus 的 4 个任务套件、3 个 VLA、7 种扰动条件下评测，发现扰动会改变成功行为的典型模式与其变异性。',
     None),
    ('Beyond Success Rate', '评测方法与度量',
     'IMEP：VLA 记忆能力的干预式评测协议',
     '具备记忆机制的 VLA 系统',
     '目标事实替换 / 保事实替换 / 最小数值扰动 / 完全复本；决策正确性与执行成功分离',
     '针对「说机器人用了记忆，但记忆是否真起作用」的问题，指出仅靠成功率消融会同时改变信息与计算、且平均率会掩盖相互抵消的增益与损失。协议在检索接口处做四类干预并分别评估决策正确性与电机执行成功，回答记忆是否有净收益、何时有益、改变记忆是否改变结果、效应是否特异于任务相关事实，覆盖回合内、跨回合与智能体式记忆。',
     None),
    ('VLA-Scope', '评测方法与度量',
     'VLA-Scope：偏移感知的失败预测',
     'OpenVLA（10 个 LIBERO 设置）',
     'OOD 检测 + 偏移类别分类 + 执行进度；失败风险预测',
     '指出 VLA 在分布外条件下仍可能成功，因此单靠 OOD 检测不足以预测执行失败。框架分两阶段：先用图像与语言的池化表示检测 OOD 输入并判定偏移类别，再对被标记为 OOD 的输入结合偏移类别、动作前缀特征与执行进度，用跨偏移共享的逻辑回归随执行过程更新失败风险。',
     None),
    ('Blackout vs. Freeze', '评测方法与度量',
     '黑屏与冻结：相机故障下 VLA 的物理失效模式',
     'π0.5、GR00T',
     '图像黑屏/画面冻结；关节行为、掉物率、本体感觉消融',
     '分析 π0.5 与 GR00T 在图像黑屏、画面冻结等输入故障下的行为，发现即使任务成功率相近，两种故障会产生不同的物理失效模式：冻结导致更极端的关节行为，夹爪闭合后的黑屏更易导致掉物（无本体感觉时最明显）。选择性干预实验显示本体感觉可部分补偿被移除的机器人本体信息，但难以在移除腕部视角物体信息时恢复任务成功；最后评测黑屏训练等两种缓解方案。',
     None),
    ('Anatomy of a Closed-Loop Collapse', '评测方法与度量',
     '闭环崩溃剖析：压缩 VLA 策略的因果案例',
     '压缩/蒸馏后的 Octo-Base 策略',
     '离线校验指标 vs 闭环成功率；配对动作轨迹取证',
     '指出「压缩策略可离线达标但闭环失败」已被先前工作确立，本文贡献的是单个自然发生案例的因果剖析：8 层蒸馏的 Octo-Base 保留 86% 参数、通过所有离线检查（教师比 0.996 与 1.000），但闭环仿真 pick-and-place 为 0/72（教师 40/72）。崩溃是结构化的：早期阶段逐步退化，搬送到目标阶段在全部训练变体中均为 0%；配对动作轨迹取证定位到晚期偏重的负 z 残差特征。',
     None),
    ('Beyond the Leaderboard', '评测方法与度量',
     '超越排行榜：域偏移下驾驶策略的反事实诊断',
     '6 个已发布的端到端/VLA 驾驶策略',
     'nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化',
     '指出排行榜名次只报告结果、不报告行为，因而难以预测策略在新地点的表现：nuScenes 开环误差或 NAVSIM 排名并不迁移到「新地点且行人位于自车走廊附近」的场景。提出反事实体检——数百帧真实画面各做两种编辑（移除行人、夜间重打光）并由独立检测器验证，把规划轨迹的变化当作诊断量而非分数，并从中读出两个因果轴、构造五项「考试」以分离被单一分数合并的行为差异。',
     None),
    ('Perceives but Doesn', '评测方法与度量',
     '看见了却不刹车：推理型驾驶 VLA 的感知-动作绑定缺口',
     '推理增强的驾驶 VLA',
     '匹配的仿真反事实与日志回放；危险编码与纵向规划响应',
     '刻画「感知-动作绑定缺口」：危险信息确实已在模型视觉表示中被编码，但对轨迹生成的控制力不足，纵向规划主要被自车速度历史主导，对危险接近度与模型自身推理链的响应都很弱。分析显示轨迹生成器有能力刹车却有时不刹；在不重训、不改权重的前提下，向冻结的 flow-matching 采样器注入危险条件能量即可诱发制动。',
     None),
    ('Uncovering Linguistic Fragility', '评测方法与度量',
     '多样性感知红队：VLA 的语言脆弱性挖掘',
     'VLA 模型',
     '自动红队；失败模式多样性、语言扰动下的失败率',
     '指出标准基于强化学习的自动红队因奖励最大化而严重模式坍缩，只收敛到少量琐碎或重复的失败模式，无法揭示有意义风险的完整图景。该工作提出多样性感知的红队方法来系统挖掘 VLA 对语言细微差异的脆弱性，弥补「测试用例覆盖不足导致安全评估失真」的问题。',
     None),
    ('Red-Teaming Vision-Language-Action Models', '评测方法与度量',
     'Q-DIG：质量-多样性指令生成红队',
     'VLA 模型',
     '自然且任务相关的对抗指令；失败诱发的多样性与覆盖度',
     '指出 VLA 表现对指令措辞高度敏感且失败难以预测，因而把质量-多样性（QD）优化作为红队框架，结合视觉语言模型生成大量自然、与任务相关却能诱发失败的指令（Q-DIG），在多个仿真基准上比基线找到更多样、更贴近真实使用的失败诱因。',
     None),
    ('No Free Checker', '综述',
     'No Free Checker：机器人策略验证器综述',
     '机器人策略验证器（约 150 个）',
     '可用性（代价/时延/密度）与可信性（可钻空子程度）两轴',
     '系统梳理约 150 个机器人策略验证器——从成功检测器、奖励模型到运行时监控器、安全过滤器与时序逻辑规约——并沿两个性质比较：可用性（一次判定要多少代价、多早到达、能多频繁地问）与可信性（高分对任务的说明力；判定越可被钻空子、越自利则可信性越低）。按判断来源分为人工、规则/形式化、学习/预训练、模型内在四类，指出「没有免费的对错裁判」。',
     None),
    ('Vision-Language-Action Safety', '综述',
     'VLA 安全：威胁、挑战、评测与机制',
     'VLA 系统（综述）',
     '攻击时机（训练期/推理期）× 防御时机两轴；评测方法梳理',
     '面向 VLA 安全的统一综述：指出具身性带来的不可逆物理后果、视觉-语言-状态多模态攻击面、防御的实时延迟约束、长时程轨迹上的误差传播以及数据供应链脆弱性，并以攻击时机与防御时机两条平行时间轴组织威胁，把每个威胁类别与其可介入阶段对应，串联机器人学习、对抗机器学习、AI 对齐与自主系统安全等原本分散的文献。',
     None),
    ('MINERVA', '评测方法与度量',
     'MINERVA：LIBERO 的任务容量下限',
     '刻意精简的视觉运动策略 vs 十亿参数 VLA',
     '参数规模—成功率曲线；架构/训练/推理因素消融',
     '用一个刻意精简的策略族测量 LIBERO 实际需要的模型容量：0.54M 参数策略在 4 个标准套件、2000 次 rollout 上取得 95.1% 平均成功率，仅比报告中的 LeRobot π0.5 低 2.4 个点（参数少 7700 倍），性能约在 1M 参数处饱和、低于 0.25M 崩溃。这一结果对「LIBERO 是否仍是有效的能力基准」提出了直接质疑。',
     None),
    ('Monkey See, Can Monkey Do', 'VLA 能力 Benchmark',
     'RoboReel：从观察学习（LfO）统一基准',
     '从人类视频学习策略的模型',
     '10 个操作任务；真机人类示范视频 + 仿真轨迹 + 评测环境',
     '从观察学习是机器人数据规模化的重要途径，但既有方法在假设、硬件与环境设置上差异很大，难以比较。该基准捆绑真机人类示范视频、仿真机器人轨迹与统一评测环境，覆盖 10 个操作任务，为「从人类视频学习操作技能」提供可比的评测底座。',
     None),
    ('Inspect Robots', '评测方法与度量',
     'Inspect Robots：具身智能能力与安全评测框架',
     '6 个基于前沿语言模型的策略',
     '模块化可复用抽象；评测的搭建、执行与终止自动化',
     '通用语言模型越来越多地直接控制机器人硬件，因而需要系统理解其「具身之后」的能力与安全。该框架把物理评测的规格描述与结果分析抽象为可复用组件，并用基础设施自动化评测的搭建、执行与终止；作者用它评测了 6 个基于前沿语言模型的策略，发布三个月下载量接近 10 万次。',
     None),

    # ── C. 具身智能体 / 规划层安全 Benchmark ────────────────────────────────
    ('AGENTSAFE', '具身智能体安全 Benchmark',
     'AGENTSAFE / SAFE：危险指令下的具身智能体安全',
     'VLM 驱动的具身智能体',
     '感知-规划-执行全过程；危险指令下的违规与失败模式',
     '指出既有安全基准危险范围窄、只看最终结果，忽略智能体完整的感知-规划-执行过程，从而掩盖关键失败模式。SAFE 含三部分：可扩展的对抗仿真沙箱 SAFE-THOR（通用适配器把 VLM 高层输出映射为底层具身控制，支持多种智能体工作流接入）、风险感知的 SAFE-VERSE 等，用于系统评估具身 VLM 智能体执行危险指令时的安全性。',
     None),
    ('EmbodiedBench', 'VLA 能力 Benchmark',
     'EmbodiedBench：视觉驱动具身智能体综合基准',
     '多模态大模型（MLLM）驱动的具身智能体',
     '1128 个任务 / 4 个环境；6 个能力子集',
     '针对 MLLM 具身智能体缺乏综合评测框架的问题，构建覆盖 4 个环境、1128 个测试任务的基准：从家务等高层语义任务到导航与操作等原子动作级任务，并设 6 个精选子集分别考察常识推理、复杂指令理解、空间意识、视觉感知与长期规划等核心能力。',
     None),
    ('IS-Bench', '具身智能体安全 Benchmark',
     'IS-Bench：日常家务中的交互安全评测',
     'VLM 驱动的具身智能体',
     '161 个场景 / 388 个安全风险；过程导向评测（风险感知与缓解步骤顺序）',
     '指出静态、非交互的评测范式无法评估交互环境中的风险：它无法模拟由智能体自身动作引发的动态风险，且依赖忽略中间步骤的事后评判。该基准提出「交互安全」——智能体感知涌现风险并按正确程序顺序执行缓解步骤的能力——含 161 个场景、388 个具体安全风险，并采用过程导向的评测核查中间步骤，发表于 AAAI 2026。',
     'AAAI 2026'),
    ('SafeAgentBench', '具身智能体安全 Benchmark',
     'SafeAgentBench：具身 LLM 智能体的安全任务规划基准',
     '具身 LLM 智能体',
     '安全任务规划；危险场景下的计划合规率',
     '面向具身 LLM 智能体的安全任务规划评测：在危险场景中检验智能体生成的执行计划是否满足安全要求，是「规划层安全」评测的代表性工作之一，常与 AGENTSAFE、IS-Bench 等一起作为具身智能体安全评测的基线集合。',
     'arXiv 预印本 (arXiv:2412.13178)'),
    ('Benchmarking and Aligning Task-Planning Safety', '具身智能体安全 Benchmark',
     'SafePlan-Bench / Safe-Align：任务规划安全的测量与对齐',
     'LLM 驱动的具身智能体',
     '2027 个日常任务、8 类危险（如火灾）；规划安全性',
     '提出测量与对齐一体的框架 Safe-BeAl：SafePlan-Bench 建立任务规划安全的综合基准，覆盖 2027 个日常任务及其对应环境，分布于 8 类危险之中；实证分析表明即便没有对抗输入或恶意意图，LLM 智能体也会表现出不安全行为。随后提出 Safe-Align，把物理世界安全知识注入智能体以缓解这些危险。',
     'arXiv 预印本 (arXiv:2504.14650)'),
    ('SafeMind', '具身智能体安全 Benchmark',
     'SafeMindBench：具身 LLM 智能体的四阶段安全基准',
     'LLM 驱动的具身智能体',
     '5558 个样本；四类任务 × 三类正交安全约束（事实/因果/时序）',
     '识别危险可能产生的四个关键推理阶段（任务理解、环境感知、高层计划生成、底层动作生成），并形式化三类正交的安全约束（事实性、因果性、时序性）以刻画潜在违规。据此构建 5558 个样本的多模态基准，覆盖 Instr-Risk、Env-Risk、Order-Fix、Req-Align 四类任务与破坏、伤害、隐私、违法等高风险场景；实验显示主流 LLM 与广泛使用的具身智能体仍存在显著风险。',
     'arXiv 预印本 (arXiv:2509.25885)'),
    ('Generating Robot Constitutions', '具身智能体安全 Benchmark',
     'ASIMOV Benchmark：语义安全基准与机器人宪法',
     '作为「机器人大脑」的基础模型（VLM）',
     '语义安全；大规模情景化安全判断数据集',
     '指出机器人安全研究长期聚焦碰撞回避与近身危害，而视觉语言模型使机器人具备高层语义理解与自然语言交互能力，其幻觉与被越狱等已知脆弱性一旦被交予可产生物理接触的机器人即形成直接危险。工作有两点贡献：给出可规模化生成「机器人宪法」的数据配方，并发布 ASIMOV Benchmark——用于评测与提升机器人基础模型语义安全的大规模数据集集合。',
     'arXiv 预印本 (arXiv:2503.08663)'),
    ('VestaBench', '具身智能体安全 Benchmark',
     'VestaBench：多约束与对抗下的安全长时程规划基准',
     '具身智能体（规划层）',
     '多约束满足、长时程规划、对抗条件下的安全性',
     '面向「多约束 + 对抗」双重压力下的安全长时程规划评测：在长时程任务中同时施加多条安全约束与环境对抗扰动，检验具身智能体能否在满足约束的前提下完成规划（EMNLP 2025）。',
     'EMNLP 2025'),
    ('HASARD', '具身智能体安全 Benchmark',
     'HASARD：视觉安全强化学习基准',
     '视觉驱动的安全强化学习智能体',
     '3 个难度等级、2 种动作空间；奖励-代价权衡',
     '指出既有基于视觉的 3D 基准只考虑简单导航任务，因而基于 Doom 构建多样化、复杂的任务套件，要求策略做策略性决策、理解空间关系并预测短期未来。基准含 3 个难度等级与 2 种动作空间，对主流基线方法的实证评估显示了其复杂度、独特挑战与奖励-代价权衡（ICLR 2025）。',
     'ICLR 2025'),
    ('Benchmarking the Safety of Large Language Models for Robotic Health Attendant Control', '具身智能体安全 Benchmark',
     '机器人健康陪护控制中 LLM 的安全性基准',
     '72 个 LLM（作为机器人控制组件）',
     '270 条有害指令 / 9 类被禁行为；违规率',
     '以美国医学会医学伦理原则为依据构造 270 条有害指令，覆盖 9 类被禁行为，并在基于 Robotic Health Attendant 框架的仿真环境中评测 72 个 LLM：平均违规率 54.4%，过半模型超过 50%；不同行为类别差异显著——「设备操作」「延误急救」这类表面合理的指令比明显破坏性的指令更难被拒绝。模型规模与发布时间是开放权重模型安全表现的主要决定因素。',
     'arXiv 预印本 (arXiv:2604.26577)'),
    ('RoboJailBench', '具身智能体安全 Benchmark',
     'RoboJailBench：具身机器人智能体越狱攻防基准',
     '具身机器人智能体（VLM 驱动）',
     '越狱攻击成功率 + 良性指令遵循；安全-有用性权衡',
     '指出既有具身越狱研究依赖临时数据集、指标有限，且只看攻击成功率而忽视对良性指令的遵循能力；现有基准要么面向聊天模型，要么只做非对抗的安全评测，都无法刻画具身越狱所需的风险、输入、后果与评价标准。该基准填补这一空白，统一衡量攻击有效性与良性任务能力之间的权衡。',
     None),
    ('Benchmarking Jailbreak Guardrails', '攻防评测框架',
     '具身智能体越狱护栏的系统评测',
     '6 种代表性护栏 × 固定具身智能体后端',
     '护栏接入点（感知/规划/控制）；模板化与自动化越狱攻击下的防御效果',
     '指出越来越多护栏方法被提出用于在执行前拦截危险行为，但现有安全基准评测的是具身模型本身，护栏在真实具身智能体上到底能防住多少并不清楚。该工作给出首个具身智能体越狱护栏系统评测：把智能体视为固定后端、护栏视为可在感知、规划或控制阶段介入的可插拔模块，在统一条件下对比 6 种代表性护栏。',
     None),
    ('RT-Safe', '具身智能体安全 Benchmark',
     'RT-Safe：实时约束下的具身智能体安全基准',
     '具身智能体（城市导航场景）',
     '决策质量 + 决策时延；移动行人、环境危险、交通规则',
     '指出具身安全不只是「选对安全动作」，还要在实时约束下做到——物理世界不会为推理暂停，推理期间行人移动、车辆逼近，观测时看似安全的动作在执行前可能已不安全。该仿真城市基准把导航任务与移动角色、环境危险和交通规则结合，同时度量决策质量与决策时延。',
     None),
    ('CAPSafe', '具身智能体安全 Benchmark',
     'CAPSafe：上下文相关的动作与计划安全推理基准',
     '9 个闭源与开源 LLM',
     '动作级 + 计划级双层评测；情境性危害、多危害共存、严重度分级',
     '面向 LLM 驱动的具身智能体，构建两个层次的安全推理评测：动作级数据集判断单个动作在给定环境语境下是否安全，计划级数据集考察智能体能否为复杂危险家务任务生成安全的长时程计划。基准显式建模「危害依赖物体属性而情境化」「同一环境中多危害可共存」「每类危害标注相对严重度」三种情形，对 9 个模型的评测显示危害识别与安全长时程规划之间存在明显落差。',
     None),
    ('EmbodiedGovBench', '具身智能体安全 Benchmark',
     'EmbodiedGovBench：具身系统的治理与演进安全基准',
     '具身智能体系统（策略+基础模型+运行时）',
     '7 个治理维度：未授权能力调用、运行时漂移、可恢复性、可审计性、演进安全等',
     '指出现有评测被任务成功率（完成率、操作精度）主导，无法回答具身系统是否「可治理」——是否尊重能力边界、执行策略约束、安全恢复、保留审计轨迹并响应人类监督。基准不再只问机器人能否完成任务，而是在真实扰动下考察系统是否保持可控、受策略约束、可恢复、可审计与演进安全，覆盖七个治理维度。',
     None),
    ('Agent-SafetyBench', '具身智能体安全 Benchmark',
     'Agent-SafetyBench：LLM 智能体安全基准',
     '16 个主流 LLM 智能体',
     '349 个交互环境、2000 个测试用例；8 类风险、10 种失败模式',
     '面向 LLM 作为智能体被部署后的新型安全挑战（工具使用、环境交互），构建 349 个交互环境与 2000 个测试用例，覆盖 8 类安全风险与 10 种常见失败模式。对 16 个流行 LLM 智能体的评测给出一个警示性结果：没有任何智能体安全分超过 60%。',
     'arXiv 预印本 (arXiv:2412.14470)'),
    ('Yes-Man Syndrome', '具身智能体安全 Benchmark',
     'RoboAbstention：具身机器人智能体的弃权评测',
     '作为高层规划器的 VLM / 具身智能体',
     '弃权分类法；歧义、物理不可行、错误前提、传感器不足四类情形',
     '指出已有弃权研究多针对纯文本 LLM，无法刻画具身机器人环境固有的感知接地与物理约束。工作在具身语境下给出弃权分类法，并构建可扩展、可审计的 RoboAbstention 框架，用来自五个机器人数据集的图像生成弃权指令，要求智能体识别指令歧义、物理上不可行、基于错误前提或受限于可用传感模态与上下文而无法解决的情形。',
     None),
    ('GuardianBench', '具身智能体安全 Benchmark',
     'GuardianBench：同场景指令对比的潜在语境风险基准',
     'SOTA 视觉语言模型（VLM）',
     '3024 个「同场景安全/不安全」配对样本；配对准确率',
     '指出具身场景中的风险可以是潜在的：一条良性指令与一个安全场景组合之后才变得危险。既有工作或改变视觉上下文、或评测执行期动态，而「固定场景、只改指令」这一互补轴向此前研究不足。基准以国际安全标准为依据构造 3024 组同场景安全/不安全对比样本，发现 VLM 的判定对指令不敏感（同场景两条指令常常都被批准），主模型平均配对准确率仅 24.1%。',
     None),
    ('MMA-SafetyBench', '具身智能体安全 Benchmark',
     'MMA-SafetyBench：多模态智能体安全的视觉语义劫持基准',
     '9 个多模态智能体（web/桌面 GUI/移动/文档/视频）',
     '1083 条对抗轨迹；攻击成功率（ASR）与语义妥协率（SCR）',
     '研究「视觉语义劫持」：伪造系统告警等语义合理但具欺骗性的界面元素使智能体偏离授权任务。提出轨迹引导流程定位候选注入点并把可复现的视觉载荷插入观测流，据此构建 1083 条对抗轨迹，覆盖 web 自动化、桌面 GUI 控制、移动导航、文档理解与视频处理；9 个模型上 ASR 达 87.96%、语义妥协率 98.09%，并用 1–3–5 打分区分目标匹配输出。',
     None),
    ('Embodied Agent Interface', 'VLA 能力 Benchmark',
     'Embodied Agent Interface：具身决策的模块化评测接口',
     'LLM 驱动的具身决策智能体',
     '目标解释、子目标分解、动作序列化、状态跟踪等环节的统一接口',
     '把 LLM 具身决策拆成若干可单独评测的环节，用统一接口连接不同仿真环境与模型，从而定位失败究竟出在目标解释、子任务分解、动作接地还是状态跟踪上，而不是只报告端到端成功率（NeurIPS 2024）。',
     'NeurIPS 2024'),
    ('MAGMA-Bench', '具身智能体安全 Benchmark',
     'MAGMA-Bench：动态多机器人长时程任务推理基准',
     '开放权重规划器与前沿模型（架构无关）',
     '长时程递增 + 在线扰动（执行失败、任务中断、任务更新）',
     '面向长时程具身智能体在动态多机器人环境中的「持续任务推理」：既考察随任务时程增长的信息保持与异构机器人协同，也考察受控在线扰动（执行失败、任务中断、任务更新）下的决策调整。基准采用结构化技能级接口，把任务层推理与感知、底层控制分离，便于公平比较不同架构的规划器。',
     None),
    ('Frontier LLMs Enter the World of Robotics', 'VLA 能力 Benchmark',
     'RoboColiseum：前沿 LLM 控制机器人的跨模型评测',
     'GPT-6 Astra、GPT-6.1 Sol、Claude Opus 5.5、Gemini 4 Argon',
     '四条赛道：指令遵循、空间推理、通用操作、鲁棒性',
     '在 RoboColiseum 上做多维对比评测，并实现 Agent2Act 控制框架，把四个前沿模型通过共享的观测、动作执行与反馈接口接入评测环境。统一任务设置与评分标准下，四个模型呈现一致的能力画像：指令遵循得分很高（其中三个接近满分）、空间推理较强，而通用操作得分明显低于其余三条赛道。',
     None),
    ('An Unexpected Robot Policy', 'VLA 能力 Benchmark',
     'LLM 作为策略：GPT-6 Astra 在 RoboDojo 的早期评测',
     '3 个 LLM 作为策略（无任务微调）；40 个公开策略作对照',
     'RoboDojo 全部 42 个任务；成功率与 Score（每任务 50 回合协议）',
     '追问「不做任务微调，LLM 能否直接充当机器人操作策略」。在 RoboDojo 全部 42 个任务、总计 2100 次试验上，GPT-6 Astra 取得 22.48% 平均成功率与 28.97 Score，超过所有公开条目；而同样后处理下 GPT-5.5 与 DeepSeek-Flash 仅 0.88% 与 1.92%。作者进一步指出 Astra 呈现高度两极化的能力分布。',
     None),
    ('Does Continual Imitation Learning Remain Grounded', '评测方法与度量',
     '语言扰动下的持续模仿学习任务保持基准',
     '持续模仿学习策略（LIBERO-Goal）',
     '保义/变义指令变体；任务能力与语言敏感性分离',
     '指出持续模仿学习通常只考察「不遗忘」，但保持任务表现并不保证行为仍受语言接地——策略可能依赖场景线索、物体关联或记忆中的任务结构。该基准为 LIBERO 的 Goal、Spatial、Object、Long 套件构造保义与变义指令变体，在每一持续学习阶段后用 Original 与 Paraphrase 指令评测，把任务胜任度与语言敏感性分开，作为标准学习指标的补充诊断。',
     None),

    # ── D. 攻击类（含评测协议/基准）────────────────────────────────────────
    ('Exploring the Adversarial Vulnerabilities', '攻防评测框架',
     'VLA 机器人对抗脆弱性系统评测',
     'VLA 模型（数字与物理攻击）',
     '两个无目标攻击目标（基于空间基础 destabilize 动作）+ 一个轨迹操控的有目标攻击；对抗补丁',
     '针对机器人执行的独特需求设计攻击目标：两个利用空间基础的无目标攻击目标用于破坏动作稳定性，一个有目标攻击目标用于操控机器人轨迹；并设计对抗补丁生成方法，把小块彩色补丁放入相机视野，从而在数字与物理两种设定下实施攻击，系统评估 VLA 的鲁棒性（ICCV 2025）。',
     'ICCV 2025'),
    ('BadVLA', '攻防评测框架',
     'BadVLA：目标解耦优化的 VLA 后门攻击',
     'VLA 模型',
     '后门攻击成功率、干净任务性能保持、触发器条件控制',
     '指出 VLA 紧耦合架构在「训练即服务」范式下暴露隐蔽、持久且现实的后门威胁。方法采用目标解耦优化：第一阶段显式分离特征空间，把触发器表示与良性输入隔开；第二阶段引入仅在触发器存在时激活的条件控制偏移，从而在保持名义性能的同时植入可控恶意行为（NeurIPS 2025）。',
     'NeurIPS 2025'),
    ('FreezeVLA', '攻防评测框架',
     'FreezeVLA：动作冻结攻击',
     '3 个 SOTA VLA；4 个机器人基准',
     '动作冻结率（攻击成功率）；指令被忽略的程度',
     '识别并形式化一类关键对抗脆弱性：对抗图像可以「冻结」VLA，使其忽略后续指令，从而在关键时刻造成不作为，实质切断机器人的数字心智与物理动作之间的联系。提出基于 min-max 双层优化的攻击生成与评测框架，在 3 个 SOTA VLA 与 4 个机器人基准上验证了较高的平均攻击成功率。',
     None),
    ('SilentDrift', '攻防评测框架',
     'SilentDrift：利用动作分块的隐蔽后门攻击',
     'VLA 模型（黑盒后门）',
     '攻击隐蔽性（运动学连续性）、攻击成功率',
     '指出现代 VLA 中「动作分块 + 增量位姿表示」共同造成块内视觉开环：机器人必须执行 K 步动作序列，逐步扰动可随积分累积。据此提出黑盒隐蔽后门攻击 SilentDrift，用 Smootherstep 构造具备 C² 连续性的扰动，保证轨迹边界处速度与加速度为零以满足严格运动学一致性约束；并通过关键帧攻击策略只污染关键的接近阶段以提升隐蔽性。',
     None),
    ('DropVLA', '攻防评测框架',
     'DropVLA：动作级后门攻击',
     'OpenVLA-7B（LIBERO 评测）',
     '指定动作原语的触发成功率；名义任务性能保持',
     '指出现有 VLA 后门研究主要关注无目标攻击或任务级劫持，对单个动作的细粒度控制尚属空白。方法在「流水线黑盒、仅有限数据投毒」的现实设定下，用窗口一致的重标注方案做分块微调，强制某个可复用动作原语（如开夹爪）在攻击者指定的决策点执行；在 OpenVLA-7B 与 LIBERO 上，仅视觉投毒即达到 98.67%–99.83% 的攻击成功率。',
     None),
    ('Model-agnostic Adversarial Attack and Defense', '攻防评测框架',
     'EDPA：模型无关的 VLA 对抗补丁攻击与防御',
     '多种 VLA 模型（无需架构先验）',
     '补丁攻击成功率；跨模型/跨机械臂迁移性',
     '提出嵌入破坏补丁攻击 EDPA：无需知道模型架构或被控机械臂即可生成可直接置于相机视野中的对抗补丁，其构造依据是破坏视觉-文本潜表示之间的语义对齐、并最大化潜表示的差异；同时给出相应的防御策略。该工作为「VLA 攻击的可迁移性与可复现评测」提供了基线。',
     None),
]

# 库外补充
EXT_ROWS = [
    ('VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models', 2025,
     'arXiv 预印本 (arXiv:2512.22539)', 'https://arxiv.org/abs/2512.22539',
     'VLA 安全 Benchmark', 'VLA 模型（含安全任务套件）',
     '三轴结构化难度（任务结构 / 语言指令 W0–W4 / 视觉观测 V0–V4）；11 个任务套件、170 个任务',
     '以结构化任务设计框架量化难度：任务结构维度含 Safety、Distractor、Extrapolation、Long Horizon 四个维度共 11 个套件 170 个任务，每个套件分 L0–L2 三级而微调只允许用 L0，以严格测泛化；语言与视觉扰动可作为任意任务上的诊断探针，区分稳健接地与表层模式匹配。评测主流 VLA 后发现记忆优于泛化、视觉感知流于表面、忽视安全约束，且 L0–L2 间出现模型排名反转，说明各难度级提供非冗余信息。'),
    ('ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models', 2026,
     'arXiv 预印本 (arXiv:2606.27079)', 'https://arxiv.org/abs/2606.27079',
     'VLA 安全 Benchmark', 'VLA 策略（5 种本体、66 个安全增强场景）',
     '13 类安全 taxonomy；累计安全代价 CC、风险暴露时间 RET、四象限分解',
     '把安全作为首要评测目标的诊断型基准：定义覆盖物理交互安全（Safe-Core）、指令侧安全（Safe-Lang）、感知侧安全（Safe-Vis）的 13 类安全 taxonomy，并在场景结构、语言指令、视觉观测三个受控变化维度下评测，使失败来源可被诊断而非被单一总分掩盖。除二元成功率外还度量过程级风险——累计安全代价与风险暴露时间——并给出安全/不安全成功与失败的四象限分解；在 RoboTwin 上实例化 66 个安全增强基础场景。结果表明即使最强策略也有不可忽视的安全代价与非安全的名义成功，且结构与视觉变化造成的安全退化远强于普通语言变化。'),
    ('MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement', 2026,
     'arXiv 预印本 (arXiv:2608.17386)', 'https://arxiv.org/abs/2608.17386',
     'VLA 安全 Benchmark', '零样本与微调的 VLA（仿真 + Franka 真机）',
     'LTL_f 自动机监控、物理谓词；200 基础任务 × 5 扰动 = 1000 锁定场景',
     '以「规约接地」方式判定安全：每个 rollout 由基于 LTL_f 的自动机监控器在物理谓词上运行时检查，而不依赖学习分类器或 LLM 裁判。ManiGuard-Bench 沿「技能 × 约束」分类法把 6 类接触密集家务任务组织为 200 个锁定基础任务，每任务在 1 个分布内与 4 个单轴 OOD 扰动下评测、安全规约保持不变。超过 23000 次 rollout 的结果显示：6–21% 的成功回合违反安全规约，安全必须与任务成功率独立评估；在其数据上微调可提升安全完成率，但仍有 21–42% 的「已介入」rollout 违规，且该差距不随示范规模扩大而闭合。'),
    ('LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks', 2026,
     'arXiv 预印本 (arXiv:2604.16788)', 'https://arxiv.org/abs/2604.16788',
     'VLA 能力 Benchmark', '6 个 SOTA 操作策略（真机）',
     '1000+ 真机回合；Context-Independent / Context-Dependent 两个区间',
     '真机长时程操作基准，含 1000 余个真实回合，分两个互补区间：完全可观测的 Context-Independent 与由歧义驱动的 Context-Dependent。任务被组织为能力子集与歧义子集，从而支持对执行鲁棒性、时间一致性与上下文依赖推理做机制感知的评测。评测 6 个 SOTA 策略显示长时程性能并非由单一因素决定：完全可观测设定下的表现与执行鲁棒性关联更强，而上下文难度因任务而异，且记忆类方法并未带来一致提升。'),
    ('Red-Teaming of Vision-Language-Action Models via Quality Diversity Environment Generation', 2026,
     'arXiv 预印本 (arXiv:2610.14415)', 'https://arxiv.org/abs/2610.14415',
     '评测方法与度量', '3 个代表性 VLA 模型',
     '质量-多样性环境生成；OOD 对抗环境下的鲁棒性、sim-to-real 迁移',
     '指VLA 在分布内表现良好但在物体位置、光照、纹理、相机位姿等轻微测试期偏移下常常失败。提出 Q-DEG：用质量-多样性优化搜索「高失败率且彼此多样」的对抗环境（用 VLA 的策略嵌入促进多样性），再把 VLA 放在自己成功 rollout 上做自模仿微调，从而把红队发现直接转化为鲁棒性提升；在 3 个 VLA 上优于基座模型与用两个红队基线数据微调的模型，并证明该改进有利于 sim-to-real 迁移。'),
    ('LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning', 2023,
     'NeurIPS 2023（神经信息处理系统大会，Datasets & Benchmarks）', 'https://arxiv.org/abs/2306.03310',
     'VLA 能力 Benchmark', '语言条件操作策略 / 终身学习智能体',
     '4 个任务套件（130 个任务）；知识迁移与终身学习指标',
     'VLA 领域使用最广的能力评测平台：把语言条件操作任务分为 LIBERO-Spatial、Object、Goal、Long 四个套件共 130 个任务，重点是「知识迁移」与「终身学习」——同一策略在任务序列上顺序学习后能否保持并迁移。几乎所有 VLA 论文都以 LIBERO 平均成功率作为主指标，也因此成为后续大量鲁棒性/安全性基准（LIBERO-Plus、LIBERO-Pro、LIBERO-X、LIBERO-MAX 等）的底座。'),
    ('CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks', 2022,
     'IEEE Robotics and Automation Letters (RA-L) 2022', 'https://arxiv.org/abs/2112.03227',
     'VLA 能力 Benchmark', '语言条件模仿学习策略',
     '34 个任务、1000+ 条长时程指令链；连续指令平均完成长度',
     '语言条件长时程操作的代表性基准：在仿真桌面环境中定义 34 个操作任务，并把它们串联成上千条由语言指令逐步给出的长时程序列，度量策略在连续指令下平均能正确完成多少步。其「指令链」设计使长时程语言遵循成为可量化指标，是 VLA 通用能力评测的经典基线之一。'),
    ('Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)', 2024,
     'arXiv 预印本 (arXiv:2405.05941)', 'https://arxiv.org/abs/2405.05941',
     'VLA 能力 Benchmark', '真实机器人操作策略（OpenVLA、RT-1 等）',
     '仿真-真机对齐；控制与视觉差异消解；与真机成功率的相关性',
     '直面「真机评测不可扩展且难复现」的问题：指出控制差异与视觉差异是仿真评测不可靠的两个关键来源，并提出无需构建全保真数字孪生的缓解手段，使仿真评测结果与真机表现对齐。该工作为 VLA 提供了一条低成本、可复现的能力评测路径，也是后续大量 VLA 论文采用的仿真评测协议来源。'),
    ('RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots', 2024,
     'arXiv 预印本 (arXiv:2406.02523)', 'https://arxiv.org/abs/2406.02523',
     'VLA 能力 Benchmark', '通用机器人操作策略',
     '大规模日常场景（以厨房为主）、数千场景与大量演示数据',
     '主张用高保真物理仿真来扩展机器人的环境、任务与数据规模，提供以厨房为主的大量日常场景与数千条演示，用于训练与评测通用操作策略。它把评测从「少数桌面任务」推向「日常环境中的大规模任务」，是长时程、多任务 VLA 评测的重要底座（RoboCasa365、RoboCasa-Shift 等即建立在其上）。'),
    ('RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins', 2025,
     'CVPR 2025（IEEE/CVF 计算机视觉与模式识别会议）', 'arXiv:2412.02960',
     'VLA 能力 Benchmark', '双臂机器人操作策略',
     '生成式数字孪生；双臂协同任务与真机迁移',
     '用生成式数字孪生构建双臂机器人基准：借助生成模型批量生成多样化物体与场景的数字孪生，从而在仿真中大规模构造双臂协同操作任务，并支持向真机迁移的评测。它填补了单臂基准之外的「双臂/高自由度协同」评测空白，也被多篇 VLA 安全基准（如 Trap-RoboTwin、ForesightSafety-VLA）复用为场景底座。'),
    ('VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning', 2025,
     'ICCV 2025（IEEE/CVF 国际计算机视觉大会）', 'arXiv:2412.02589',
     'VLA 能力 Benchmark', '语言条件操作策略 / VLA',
     '大规模任务集；长时程推理与组合泛化',
     '大规模语言条件操作基准，强调「长时程推理」与组合泛化：任务需要多步推理与常识知识才能完成，而不只是把一条指令映射为一次抓取。它把评测重心从单步操作成功率推向「推理—规划—执行」的整链能力，是 VLA 能力评测中较有代表性的高难度基准。'),
    ('THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation', 2024,
     'RSS 2024（Robotics: Science and Systems）', 'arXiv:2402.08191',
     'VLA 能力 Benchmark', '模仿学习策略（含 VLA）',
     '20+ 环境扰动因子；泛化边界刻画',
     '针对「模仿学习策略在训练分布外泛化能力不明」的问题，用 20 余种环境扰动因子（物体、纹理、光照、相机位姿、桌面高度等）系统性评测策略的泛化边界，并给出不同扰动对成功率的影响排序。它把「泛化」从单一数字拆解为可归因的扰动维度，是 VLA 鲁棒性基准（如 LIBERO-Plus、VLA-GAUGE）方法论的直接前身。'),
    ('RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation', 2025,
     'RSS 2025（Robotics: Science and Systems）', 'arXiv:2412.13877',
     'VLA 能力 Benchmark', '多本体操作策略',
     '跨本体大规模真机数据与统一评测',
     '面向「多本体」的操作基准与数据集：汇集多种机器人本体的大规模真机示范，并在统一协议下评测策略跨本体的迁移与泛化能力。它把 VLA 评测从单一本体推向跨本体一致性，是判断「策略学到的是任务还是本体特性」的重要工具。'),
    ('Jailbreaking LLM-Controlled Robots (RoboPAIR)', 2025,
     'ICRA 2025（IEEE 国际机器人与自动化会议）', 'DOI: 10.1109/ICRA55743.2025.11128119',
     '攻防评测框架', 'LLM 控制的机器人（自动驾驶 LLM、四足机器人等）',
     '越狱攻击成功率；攻击在真实物理系统上的可执行性',
     '首次系统展示「越狱」可以跨越数字边界作用于物理系统：提出 RoboPAIR 攻击算法，通过多轮对话诱导作为机器人控制器的 LLM 输出危险动作，在自动驾驶 LLM 与四足机器人等真实平台上取得很高攻击成功率，并可绕过系统提示与护栏。它确立了「具身越狱」这一评测问题，也成为 RoboJailBench、护栏评测等后续工作的参照点。'),
    ('BadRobot: Jailbreaking Embodied LLM Agents in the Physical World', 2024,
     'arXiv 预印本 (arXiv:2407.20242)', 'https://arxiv.org/abs/2407.20242',
     '攻防评测框架', '具身 LLM 智能体（机器人）',
     '语音等典型用户通道注入；越狱成功率与物理危害',
     '提出 BadRobot 攻击范式，考察具身 LLM 是否会做出违反安全与伦理约束的行为：通过语音等具身场景中典型的用户交互通道注入恶意指令，使作为任务规划器的 LLM 输出危险计划并驱动机器人执行。它把「越狱」与「物理危害」直接联系起来，是具身智能体安全评估的早期代表性工作。'),
]


def venue_of(p, override):
    if override:
        return override
    v = (p.get('venue') or '').strip()
    if v in VENUE_MAP:
        return VENUE_MAP[v] % (p.get('year') or '')
    if v.lower().startswith('arxiv'):
        aid = (p.get('arxiv_id') or '').strip()
        return 'arXiv 预印本 (arXiv:%s)' % aid if aid else 'arXiv 预印本'
    if v:
        return v
    return 'arXiv 预印本'


def link_of(p):
    aid = (p.get('arxiv_id') or '').strip()
    if aid:
        return 'https://arxiv.org/abs/%s' % aid
    return p.get('url') or ''


TIER_LABEL = {
    'curated': '本论文库（人工精选目录）',
    'audited': '本论文库（作者复核）',
    'screened': '本论文库（自动筛查）',
}

# 元数据修正：库内条目缺 arXiv 号，或已确认被会议接收但库内只标了 arXiv
OVERRIDES = {
    'ANNIE: Be Careful of Your Robots': {
        'arxiv_id': '2509.03383', 'venue': 'arXiv 预印本 (arXiv:2509.03383)'},
    'Adversarial Attacks on Robotic Vision Language Action Models': {
        'arxiv_id': '2506.03350', 'venue': 'arXiv 预印本 (arXiv:2506.03350)'},
    'Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics': {
        'arxiv_id': '2609.39178', 'venue': 'ICRA 2026（IEEE 国际机器人与自动化会议）'},
    'VestaBench': {
        'venue': 'EMNLP 2025（Industry Track，产业赛道）'},
    'Embodied Agent Interface': {
        'venue': 'NeurIPS 2024（神经信息处理系统大会）'},
}

ZH_EXT = {
    'VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models':
        'VLA-Arena：开源 VLA 基准框架',
    'ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models':
        'ForesightSafety-VLA：VLA 统一诊断式安全基准',
    'MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement':
        'ManiGuard：规约接地的操作安全评测与数据套件',
    'LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks':
        'LongBench：真机长时程操作基准',
    'Red-Teaming of Vision-Language-Action Models via Quality Diversity Environment Generation':
        'Q-DEG：质量-多样性环境生成红队',
    'LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning':
        'LIBERO：终身机器人学习与知识迁移基准',
    'CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks':
        'CALVIN：语言条件长时程操作基准',
    'Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)':
        'SimplerEnv：真机策略的仿真评测协议',
    'RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots':
        'RoboCasa：大规模日常任务仿真与评测底座',
    'RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins':
        'RoboTwin：生成式数字孪生的双臂机器人基准',
    'VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning':
        'VLABench：长时程推理的语言条件操作基准',
    'THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation':
        'COLOSSEUM：操作策略泛化性基准',
    'RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation':
        'RoboMIND：多本体操作基准与数据集',
    'Jailbreaking LLM-Controlled Robots (RoboPAIR)':
        'RoboPAIR：越狱 LLM 控制的机器人',
    'BadRobot: Jailbreaking Embodied LLM Agents in the Physical World':
        'BadRobot：越狱物理世界中的具身 LLM 智能体',
    'SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models':
        'SafeVLA-Bench：VLA 的「成功-安全」落差基准',
    'LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models':
        'LIBERO-Safety：VLA 物理与语义安全综合基准',
    'PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies':
        'PolaRiS：通用策略的可扩展 real-to-sim 评测',
    'RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation':
        'RoboWorld：面向通用策略评测的快速可靠神经仿真器',
    'WorldEval: World Model as Real-World Robot Policies Evaluator':
        'WorldEval：以世界模型作真机策略评测器',
    'dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model':
        'dWorldEval：离散扩散世界模型驱动的可扩展策略评测',
    'Active Real-World Factor-Based Evaluation for Generalist Robot Policies':
        '主动因子评测：通用策略的真机高效评测',
    'Robo Eval: Where Robotic Manipulation Meets Structured and Scalable Evaluation':
        'RoboEval：结构化可扩展的操作评测框架',
    'Robo2Process: Benchmarking and Learning Process-Aware Understanding in Vision-Language Robotic Manipulation':
        'Robo2Process：过程感知理解的基准与学习',
    'RoboChrono: A Real Robot Benchmark for Streaming Task Understanding':
        'RoboChrono：流式任务理解的真机基准',
    'RoboVista: Evaluating Vision Language Models for Diverse Robot Applications':
        'RoboVista：面向多样机器人应用的 VLM 评测',
    'TSHA: A Benchmark for Visual Language Models in Trustworthy Safety Hazard Assessment Scenarios':
        'TSHA：可信安全隐患评估的 VLM 基准',
    'AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems':
        'AgiBot World Colosseo：百万轨迹级操作平台',
    'ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills':
        'ManiSkill2：可泛化操作技能统一基准',
    'HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks':
        'HUGE-Bench：无人机高层 VLA 任务基准',
}

rows = []
for key, cat, zh, obj, dim, summ, vo in LIB_ROWS:
    p = find(key)
    area = '%s › %s' % (p.get('layer') or '-', p.get('subcat') or '-')
    rows.append({
        'title': p['title'], 'zh': zh, 'year': p.get('year'), 'venue': venue_of(p, vo),
        'src': TIER_LABEL.get(p.get('tier'), '本论文库'), 'area': area, 'cat': cat,
        'obj': obj, 'dim': dim, 'summ': summ, 'link': link_of(p), 'tier': p.get('tier'),
    })

# 第二批：标题/摘要不含 benchmark 关键词、但实质在做 VLA 评测的论文
from new_rows import NEW_ROWS
for key, cat, zh, obj, dim, summ, vo in NEW_ROWS:
    p = find(key)
    area = '%s › %s' % (p.get('layer') or '-', p.get('subcat') or '-')
    rows.append({
        'title': p['title'], 'zh': zh, 'year': p.get('year'), 'venue': venue_of(p, vo),
        'src': TIER_LABEL.get(p.get('tier'), '本论文库'), 'area': area, 'cat': cat,
        'obj': obj, 'dim': dim, 'summ': summ, 'link': link_of(p), 'tier': p.get('tier'),
    })

for title, year, venue, link, cat, obj, dim, summ in EXT_ROWS:
    rows.append({
        'title': title, 'zh': ZH_EXT.get(title, ''), 'year': str(year), 'venue': venue,
        'src': '库外补充', 'area': '—（库外）', 'cat': cat, 'obj': obj, 'dim': dim,
        'summ': summ, 'link': link, 'tier': '—',
    })

# 第四批：库内非 VLA 的具身安全 / 鲁棒性基准
from rows3 import ROWS_3
for key, cat, zh, obj, dim, summ, vo in ROWS_3:
    p = find(key)
    area = '%s › %s' % (p.get('layer') or '-', p.get('subcat') or '-')
    rows.append({
        'title': p['title'], 'zh': zh, 'year': p.get('year'), 'venue': venue_of(p, vo),
        'src': TIER_LABEL.get(p.get('tier'), '本论文库'), 'area': area, 'cat': cat,
        'obj': obj, 'dim': dim, 'summ': summ, 'link': link_of(p), 'tier': p.get('tier'),
    })

# 第三批：通过 OpenAlex 检索补充的库外基准
from ext_rows2 import EXT_ROWS_2
for title, year, venue, link, cat, obj, dim, summ in EXT_ROWS_2:
    rows.append({
        'title': title, 'zh': ZH_EXT.get(title, ''), 'year': str(year), 'venue': venue,
        'src': '库外补充', 'area': '—（库外）', 'cat': cat, 'obj': obj, 'dim': dim,
        'summ': summ, 'link': link, 'tier': '—',
    })

for r in rows:
    for key, ov in OVERRIDES.items():
        if key.lower()[:40] in r['title'].lower():
            if ov.get('venue'):
                r['venue'] = ov['venue']
            if ov.get('arxiv_id'):
                r['link'] = 'https://arxiv.org/abs/%s' % ov['arxiv_id']
            break

# 标注范围：VLA 专项评测 vs 更广的具身安全/鲁棒性基准
from cats import split_cat
_non_vla = {ROWS_3[i][0].lower() for i in range(len(ROWS_3))}
for r in rows:
    t = r['title'].lower()
    r['scope'] = ('具身安全/鲁棒性基准（非 VLA 专项）'
                  if any(k in t for k in _non_vla) else 'VLA 评测')
    r['cat'], r['domain'] = split_cat(r['cat'])

json.dump(rows, open(os.path.join(BASE, 'docs', '_rows.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('rows:', len(rows), '| lib:', sum(1 for r in rows if r['src'].startswith('本论文库')),
      '| ext:', sum(1 for r in rows if r['src'] == '库外补充'))
