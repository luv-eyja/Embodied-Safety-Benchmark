# -*- coding: utf-8 -*-
"""Generate one Markdown document per benchmark."""
import json, os, re, collections

from benchmark_ontology import (
    AXES as AXES_FROM_ONTOLOGY,
    STAGES as STAGES_FROM_ONTOLOGY,
    classify,
)

BASE = r'D:\study\Embodied'
REPO = os.path.join(BASE, 'Embodied-Safety-Benchmark')
reg = json.load(open(os.path.join(BASE, 'docs', '_bench_registry.json'), encoding='utf-8'))
_audit_path = os.path.join(REPO, 'data', 'benchmark_source_audit.json')
SOURCE_AUDIT = json.load(open(_audit_path, encoding='utf-8')).get('entries', {}) if os.path.exists(_audit_path) else {}

# 人工撰写的核心内容：(测什么, 怎么构建, 测了什么/关键结论)
# 只写信息充分的；其余由脚本按论文自身的维度/概要自动成文
DETAIL = {
 'HazardArena': dict(
   stage='认知 + 动作控制（语义-动作耦合）',
   problem='VLA 从视觉-语言主干继承丰富世界知识，又从动作示教学到可执行技能，但现有评测几乎只看动作执行成功，导致动作策略与视觉-语言语义之间耦合松散。这种解耦构成系统性漏洞：在语义语境危险时，模型仍可能执行「动作正确」的不安全行为。',
   build='由成对的**安全/不安全孪生场景**构成：两侧共享完全相同的物体、布局与动作要求，**只改变决定动作是否安全的语义语境**。因此模型在两侧的差异只能归因于语义理解，而非场景分布差异。',
   models='VLA 模型（仅在安全场景上训练）；对照为在含风险语境下评测的表现。',
   finding='仅在安全场景上训练的 VLA，在语义风险语境下往往无法保持安全——说明模型学到的是「把动作做对」，而不是「理解这个动作在当前语境下是否该做」。',
   improve='①把语义语境纳入训练分布，而非只扩动作示范；②评测必须构造「动作相同、语义不同」的对照，否则无法区分能力与安全；③安全约束不能只作用于动作层，需上溯到语义层。'),
 'SafeStage': dict(
   stage='全栈（规划前的场景理解 → 执行期控制 → 终态稳定性）',
   problem='现有安全评测要么只看任务成功率，要么只看孤立的物理约束或语义拒绝，无法回答「安全究竟在闭环操作的哪一环失效」。',
   build='97 个专门设计的风险场景，按操作生命周期分为三阶段：**Initial-State Hazards**（必须在操作目标前先行化解的安全相关关系）、**Execution-Time Safety**（执行期的不安全接触、轨迹、区域进入、物体交互）、**Final-State Hazards**（名义任务完成后残留的不稳定或不安全状态）。',
   models='视觉-语言条件机器人策略（VLA）。',
   finding='安全失效可能发生在三个阶段中的任一环节，且不同阶段的失效需要不同的检测手段；只报告任务成功率会完全掩盖后两阶段的问题。',
   improve='①评测应分阶段报告，而不是聚合为单一分数；②终态稳定性（如物体是否稳固放置）应作为独立指标；③执行期需要过程级监控而非事后判定。'),
 'SafeVLA-Bench': dict(
   stage='动作控制（轨迹级安全）',
   problem='二元成功率会掩盖轨迹上的安全违规：策略可能到达目标，却沿路施加过度接触、扰动旁观物体、使手中物体失稳或进入机器人自碰撞。',
   build='一个**事后（post-hoc）安全评估框架**，可直接套在现有基于仿真的 VLA 基准上。把任务相关的安全要求编码为**信号时序逻辑（STL）不变式**并给出定量鲁棒性语义；除原生成功率外，报告**安全率**与**成功但不安全率**。',
   models='现有仿真 VLA 基准上评测的策略。',
   finding='仅看成功率会高估安全性——存在相当比例「成功但违反规约」的回合，这类违规在只报 success 的评测中完全不可见。',
   improve='①用形式化规约（STL/LTL）而非人工规则定义安全；②把「安全率」「成功-不安全率」与成功率并列报告；③安全评估应可复用，避免每个基准重造指标。'),
 'ForesightSafety-VLA': dict(
   stage='感知 + 指令理解 + 动作控制（三侧安全）',
   problem='VLA 的通用任务能力在提升，但其**具身安全上限**仍不清楚；单一总分掩盖了失效来源。',
   build='定义覆盖三侧的 **13 类安全 taxonomy**：物理交互安全（Safe-Core）、指令侧安全（Safe-Lang）、感知侧安全（Safe-Vis）。在**场景结构 / 语言指令 / 视觉观测**三个受控变化维度下评测，使失败来源可被诊断。除二元成功率外测**过程级风险**：累计安全代价（CC）、风险暴露时间（RET），并给出安全/不安全 × 成功/失败的四象限分解。在 RoboTwin 上实例化 66 个安全增强基础场景、5 种本体。',
   models='代表性 VLA 基线（多种本体）。',
   finding='即使最强策略也有不可忽视的安全代价与非安全的名义成功；**结构与视觉变化造成的安全退化远强于普通语言变化**——说明具身安全紧耦合于感知、接地与控制能力，不能靠事后安全过滤补救。',
   improve='①安全必须与任务成功解耦评估，且要分解到「哪一侧」；②引入时间维度的风险指标（暴露时间）而非只看终局；③安全能力需在感知/接地层面训练，而非外挂过滤器。'),
 'ManiGuard-Bench': dict(
   stage='动作控制（接触密集操作的安全规约）',
   problem='基础模型策略在任务成功率上进步很快，但「是否安全地成功」缺乏严格评估；学习分类器或 LLM 裁判判定安全不可靠。',
   build='**规约接地（specification-grounded）**框架：每个 rollout 由基于 **LTL_f 的自动机监控器**在**物理谓词**上做运行时检查，不用学习分类器或 LLM 判分。任务沿「技能 × 约束」分类法组织为 200 个锁定基础任务，每任务在 1 个分布内 + 4 个单轴 OOD 扰动下评测且**安全规约保持不变**，共 1000 个锁定场景。配套「自动运动规划生成 + 人工遥操作」的成对安全标注流水线，8,000 条示范（每任务 40 条）。',
   models='零样本与在其数据上微调的 VLA，仿真 + Franka 真机，>23,000 次 rollout。',
   finding='①**6–21% 的成功 rollout 违反安全规约**，安全必须独立于任务成功率评估；②在该基准上微调可把安全任务完成率从接近零提升到 7.5–29.8%，「参与且安全」从 16–40% 提到 51–72%；③但仍有 **21–42% 的参与型 rollout 违规**，且该差距**不随示范规模扩大而闭合**，六个任务族中有两个对所有策略的安全成功率都低于 2%，且在分布偏移与真机上持续存在。',
   improve='①用形式化监控器替代 LLM 裁判；②安全标注必须逐步（per-step）而非整条轨迹；③示范扩量不能解决安全，需要针对约束的学习目标；④按任务族诊断，避免被平均分掩盖的「安全死亡区」。'),
 'SafeLIBERO': dict(
   stage='动作控制（碰撞安全）',
   problem='VLA 在非结构化环境中部署时，必须同时满足任务合规与安全保证，尤其是物理交互中的碰撞风险。',
   build='安全关键的操作场景集合，覆盖多种存在碰撞风险的操作；用于在安全性与原有指令遵循性能之间度量权衡。随 AEGIS（基于控制屏障函数的即插即用安全约束层）一起提出。',
   models='与 AEGIS 组合的现有 VLA 模型。',
   finding='安全约束层可在保持指令遵循性能的同时降低碰撞，但安全-性能权衡需要在专门的安全关键场景中度量。',
   improve='①安全保证应带理论依据（CBF）；②评测需同时报告安全与任务性能；③安全层应即插即用，不依赖重训。'),
 'ManiPhysicsBench': dict(
   stage='动作控制（物理后果：形变/断裂）',
   problem='刚体基准中的「任务成功」并不能说明模型是否**保全了物体**——夹持力过大可能压坏易碎物，成功与安全不是一回事。',
   build='先构建 **ManiPhysicsZoo**：汇总文献支撑的材质属性、3D 网格与参考文献，形成可复用物体资产；再用**基于求解器的评估**，依据物体几何、材质属性与记录的抓取条件计算**抓取特异的损伤阈值**，与记录的接触力比较，判断潜在形变与断裂。在 LIBERO 与 SimplerEnv 上按三轴物理属性、三档难度评测。',
   models='公开 VLA 检查点。',
   finding='公开 VLA 检查点在**任务成功率与「安全成功率」（完成任务且保全物体）之间存在显著差距**——夹爪力控制在成功轨迹中普遍超标。',
   improve='①把物理后果（形变、断裂）纳入评测，而非只看是否到位；②需要材质感知的仿真资产；③接触力应作为一等指标记录与报告。'),
 'LIBERO-Plus': dict(
   stage='感知 + 状态（分布偏移下的动作控制）',
   problem='VLA 在 LIBERO 上报出很高的成功率，但这些数字可能掩盖鲁棒性的根本弱点。',
   build='在 **7 个维度**引入受控扰动：物体布局、相机视角、机器人初始状态、语言指令、光照条件、背景纹理、传感器噪声；对多个 SOTA 模型逐维评测。',
   models='多个 SOTA VLA。',
   finding='①模型对扰动极其敏感：**相机视角与初始状态的轻微扰动即可让成功率从约 95% 掉到 30% 以下**；②模型对语言变化**基本不敏感**，进一步实验表明它们倾向于**忽略指令**。',
   improve='①评测必须逐维报告，聚合分掩盖崩溃点；②视角与初始状态的鲁棒性是当前最大短板；③语言被忽略说明需要强制语言接地的训练目标。'),
 'LIBERO-Pro2.0': dict(
   stage='条件/环境/观测/执行/状态/语言（六维）',
   problem='LIBERO 高分不等于鲁棒：模型可能利用基准特定规律，而非真正泛化到多样运行条件。',
   build='**22 种静态扰动 + 20 种运行时干预**，跨六个维度：条件（Condition）、环境（Environment）、观测（Observation）、执行（Execution）、机器人状态配置（Robot State Configuration）、语言（Language），共 **1,648 个经验证的偏移任务实例**；并采集 39,390 条轨迹支持面向鲁棒性的学习。所有偏移实例经六轮校验。',
   models='具身基础模型 / VLA。',
   finding='静态扰动之外，**运行时干预**（执行过程中条件突变）构成独立且更难的评测维度；稳健的鲁棒性评估需要两者结合。',
   improve='①把运行时干预纳入标准评测；②需要与扰动配套的训练数据，而不只是测试集；③大规模实例必须经过多轮校验以保证标签可靠。'),
 'LIBERO-RIG': dict(
   stage='执行（硬件与部署配置）',
   problem='部署环境变化不只是场景变化，还包括机器人自身的硬件漂移：相机被碰动并重新安装、标定漂移、控制器频率不同、末端垫片磨损。',
   build='**只扰动机器人硬件与配置，完全固定 LIBERO 任务本身**：覆盖 11 条扰动轴——相机安装与光学、相机-臂标定、驱动增益、控制频率、本体感觉噪声、基座位姿、桌面高度、夹爪垫片等，每轴 5 个严重度，共 **210 种条件**覆盖四个 LIBERO 套件。每个条件 500 回合，并用统计检验支撑结论。',
   models='9 个近期 VLA 模型。',
   finding='**汇总成功率从中等严重度的 0.767 跌到最高严重度的 0.509**（干净条件为 0.932）——即硬件配置本身就是一类被忽视的、可观的性能来源；不同模型对硬件轴的敏感谱不同。',
   improve='①把「硬件偏移」与「任务偏移」解耦评测；②部署前需要标定/安装鲁棒性测试；③报告需带统计检验，避免小样本结论。'),
 'LIBERO-VPro': dict(
   stage='感知（执行期视觉证据）',
   problem='标准基准默认执行全程的视觉观测都是干净、及时且一致的；真实系统里视觉证据会退化、延迟、来源不一致。',
   build='四个互补维度：视觉证据退化（Visual Evidence Degradation）、相机陈旧/延迟（Camera Staleness）、视觉源一致性（Visual Source Consistency）、任务相关场景变化（Task-Relevant Scene Variation），共 **12 类挑战、96 种设置、3,296 个任务-条件案例**，约 **196,000 个仿真回合**，另加 200 次 Franka Research 3 真机 rollout。',
   models='3 个 VLA + 3 个世界动作模型（WAM）。',
   finding='**强劲的名义性能并不保证闭环视觉鲁棒性**；视觉证据的时序特性（陈旧度）与一致性是独立于噪声/退化的失效来源。',
   improve='①把时序视觉质量（延迟、丢帧、来源不一致）纳入评测；②仿真与真机需并行验证；③世界动作模型与 VLA 需在同一视觉扰动谱下比较。'),
 'LIBERO-MAX': dict(
   stage='感知 + 控制（任务中途世界变化）',
   problem='机器人常在目标移动、视角偏移或出现障碍后仍需继续任务，但此前的观测与已提交动作都还反映旧场景。许多鲁棒性基准在 reset 时固定外部条件，这一**时序**挑战被低估。',
   build='**8,000 对配对案例**，覆盖几何、观测、外观、杂乱度、路径等 **8 类中途变化**。每一对固定任务、初始状态、策略随机种子与事件前的动作序列，只差别于「中途是否发生该变化」，从而把**事件导致的退化**与**本来就存在的失败**分开。',
   models='14 个当前 VLA、混合策略与世界动作模型。',
   finding='中途事件使成功率下降 **11.0–25.7 个百分点**；事件画像显示对几何变化存在**共同脆弱性**。',
   improve='①评测必须在任务中途注入变化，而非只在 reset 时改条件；②配对设计是区分事件效应与基线失败的关键；③需要能在线适应已提交动作的策略。'),
 'LIBERO-RECOVER': dict(
   stage='控制（失败恢复）',
   problem='LIBERO 上接近 100% 的成功率具有误导性：真实交互必然出现抓取失败、碰撞与物体意外移动。机器人不仅要完成任务，还要能**识别并从中恢复**——这一能力此前基本未被度量。',
   build='在既有任务成功率之外，补充失败注入与恢复评测：在预定义初始状态之外引入失败情形，考察策略能否识别失败并恢复以继续任务。',
   models='VLA 与世界动作模型。',
   finding='**基准成绩与真实世界可靠性之间存在系统性差距**：理想条件下的成功不蕴含真实世界的鲁棒性，恢复能力是一个独立且未被测量的能力维度。',
   improve='①把「失败识别 + 恢复」作为一等评测指标；②初始状态不能只取干净起点；③未来基准应报告「成功率 + 恢复率」组合。'),
 'LIBERO-CTRL': dict(
   stage='感知 + 状态（复合扰动）',
   problem='VLA 策略通常一次只被施加一种扰动，这能诊断对单一分布偏移的敏感性；但真实部署常同时存在多种偏移，而单轴鲁棒性测量是否能组合仍是未知。',
   build='**六轴基准**，每条初始状态同时提供「单轴条件」与「匹配的多轴同时条件」的**配对设计**，从而揭示两类被聚合成功率掩盖的反向结果：**涌现失败**（所有单轴 rollout 都成功，但同时条件失败）与**补偿成功**（至少一个单轴失败，但同时条件成功）。',
   models='VLA 策略。',
   finding='复合鲁棒性**不能从单轴评测推断**：存在大量涌现失败与补偿成功，二者在聚合分数上相互抵消，恰好把真实风险隐藏掉。',
   improve='①评测必须做配对的同时扰动实验；②报告涌现失败与补偿成功的比例，而非只报平均成功率；③鲁棒性训练需覆盖扰动组合。'),
 'LIBERO-X': dict(
   stage='感知 + 认知（空间/物体/指令）',
   problem='现有基准常因评测协议不足而给出有限甚至误导性的评估，无法充分刻画真实世界分布偏移。',
   build='从评测与数据两方面重构：①**分层评测协议**，难度逐级递进，针对三项核心能力——空间泛化、物体识别、任务指令理解；②通过人工遥操作采集**高多样性训练集**。设计使性能随环境与任务复杂度上升的衰减可被细粒度分析。',
   models='VLA 模型。',
   finding='逐级难度能暴露单一难度下看不见的衰减曲线；高多样性数据是可复现评测的前提。',
   improve='①难度需分级而非单一档；②评测集的多样性必须与训练集分开控制；③按能力维度而非任务维度报告。'),
 'RoboCasa-Shift': dict(
   stage='感知 + 长时程控制（阶段感知诊断）',
   problem='VLA 鲁棒性通常被**聚合任务成功率**概括，这掩盖了两件事：单次执行在分布偏移下如何变化，以及失败出现在长时程任务的哪个阶段。',
   build='建立在 RoboCasa365 之上的诊断型鲁棒性基准，三个设计要点：①**受控单因子偏移**；②**干净-扰动配对 rollout**（每对共享相同底层设置，仅目标偏移不同）；③**仿真支撑的阶段感知诊断**。对 4 个通过预设干净性能门槛的长时程任务，在 4 种扰动因子 × 3 个校准严重度（含使策略完全失败的条件）下共 **1,040 次正式 rollout**。',
   models='GR00T N1.5。',
   finding='鲁棒性响应**在因子与任务之间差异很大**，且**提高严重度并不单调恶化**——聚合分数会把这些异质性抹平。',
   improve='①必须做阶段级诊断，定位失败发生在哪一步；②配对 rollout 控制混杂变量；③严重度需要校准，而非等距假设。'),
 'VLA-GAUGE': dict(
   stage='认知 + 感知（泛化与鲁棒性统一诊断）',
   problem='VLA 在熟悉任务上成功率高，但这些分数是否反映真正的零样本泛化与扰动鲁棒性并不清楚；现有框架缺乏能力级诊断与组合扰动覆盖，且不把诊断与针对性改进连起来。',
   build='三个组件共享同一可执行任务表示：①**6 个能力套件的分布内/分布外配对任务**；②**单因子敏感度分析 + 组合扰动筛选与评测**；③**诊断驱动的定向改进**（定向数据增强与模型微调）。',
   models='12 个不同规模、不同动作建模范式的 VLA，统一协议下评测。',
   finding='泛化与鲁棒性是**不同的能力维度**，需分别诊断；把诊断结果回灌到训练可以定向补短板。',
   improve='①ID/OOD 必须配对构造；②诊断要能落到「哪个能力」；③评测框架应输出可执行的改进建议而非只给分数。'),
 'VLA-Retain': dict(
   stage='感知（视觉微调的副作用）',
   problem='为提升观测条件适应性而微调视觉模块是常见做法，但这种适配**在目标条件之外**如何影响鲁棒性并不清楚：现有鲁棒性基准只测未微调模型，适配研究又只报目标增益。',
   build='测量**跨维度效应**需要四件事：分离目标增益与目标外变化、把适配效应与架构差异隔离、排除通用遗忘、比较不同调优选择。基准把 **5 个开源 VLA** 在「相机视角」或「传感器噪声」数据上微调后的检查点，与其**自身基座版本**在 LIBERO-Plus 上对照。',
   models='5 个开源 VLA 及其微调检查点。',
   finding='**目标维度的增益会伴随目标外维度的损失**，只看目标增益会误判改进；必须用同模型的基座版本作对照才能归因。',
   improve='①微调后须做跨维度回归测试；②报告需含「目标增益 / 目标外损失」双栏；③应排除通用遗忘的干扰。'),
 'RoboStress': dict(
   stage='执行（机械误差）',
   problem='VLA 在机器人**执行动作偏离其指令**时常失败——这类偏差来自机械磨损与工况（负载变化等），而物理机器人难以系统覆盖这些条件。',
   build='受控仿真基准，把关节级的摩擦、间隙（backlash）、柔顺与重力补偿误差等模型组合成 **7 种部署场景**，各场景的执行误差水平不同，用于对执行条件鲁棒性做压力测试。配套提出 self-compensating VLA：不用任务奖励或标签，以「指令动作 − 实际执行」的残差在线更新策略。',
   models='VLA 策略。',
   finding='执行误差是被忽视的独立失效来源；通过残差在线自补偿可在部署期缓解，而无需重新标注或任务奖励。',
   improve='①把机械退化建模进评测；②部署期在线自适应优于离线重训；③压力测试应覆盖组合工况。'),
 'LIBERO（基础套件）': dict(
   stage='认知 + 动作控制（终身学习）',
   problem='测「知识迁移」与「终身学习」：同一策略在任务序列上顺序学习后，能否保持旧技能并迁移到新任务。',
   build='4 个任务套件共 **130 个语言条件操作任务**：LIBERO-Spatial（空间关系）、LIBERO-Object（物体）、LIBERO-Goal（目标）、LIBERO-Long（长时程）。每套件配 50 条人类遥操作示范，并有预训练/顺序微调的标准协议。',
   models='VLA 领域事实标准：π0/π0.5、OpenVLA、OpenVLA-OFT、GR00T N1/N1.5、Octo、SmolVLA、DTP、RoboMamba 等，几乎所有论文都以 LIBERO 平均成功率作为主指标。',
   finding='作为**能力底座**极其成功（任务干净、协议统一、复现性好），但也因此成为**饱和基准**：SOTA 已接近 100%，区分度下降；且它只测「做得成」，不测鲁棒性、安全性或失败恢复——本调研中的大量工作正是围绕这些缺口展开（LIBERO-Plus/Pro2.0/RIG/VPro/MAX/RECOVER/CTRL/X/Para、SafeLIBERO、Trap-LIBERO）。',
   improve='①在 LIBERO 之上补充分布偏移、硬件扰动、过程安全与失败恢复维度；②报告需说明微调与评测是否共用同一指令集（否则虚高）；③容量下限研究（MINERVA）提示该基准的任务容量已接近饱和，需更难的任务集。'),
 'CALVIN': dict(
   stage='认知 + 规划（长时程语言遵循）',
   problem='测语言条件的长时程操作：策略能否在**连续指令链**下逐步正确地完成任务序列。',
   build='仿真桌面环境中 **34 个操作任务**，串联成 **1,000+ 条长时程指令序列**；核心指标是**连续指令平均完成长度**（在一条指令链上能正确执行多少步）。',
   models='语言条件模仿学习策略（含 LCBC、HULC、RoboFlamingo、OpenVLA 等）。',
   finding='把长时程语言遵循变成一个可量化指标（平均完成步数），比单任务成功率更能区分策略；但环境偏静态，不含安全或扰动维度。',
   improve='①把安全约束加入指令链；②需要考虑指令链中途的环境变化；③用本表 CALVIN 相关论文的方法补语言敏感性与失败分析。'),
 'SimplerEnv': dict(
   stage='动作控制（评测基础设施）',
   problem='真机评测不可扩展且难复现；而仿真基准与真机之间的视觉与物理差距使其成为不可靠的改进信号。',
   build='识别**控制差异**与**视觉差异**两个关键挑战，并提出缓解手段，使仿真评测结果与真机表现对齐——**无需构建全保真数字孪生**。',
   models='OpenVLA、RT-1 等真实机器人策略，与真机结果对照。',
   finding='只要控制与视觉差距被恰当处理，仿真可以可靠地排序真机策略；这为 VLA 提供了低成本、可复现的评测路径。',
   improve='①sim-to-real 对齐应作为基准的显式目标；②控制频率与动作空间的匹配常被忽视；③可作为安全评测的低成本代理，但需验证排序保真度。'),
 'RoboTwin': dict(
   stage='动作控制（双臂协同）',
   problem='单臂基准无法覆盖双臂/高自由度协同操作；而双臂任务的场景与物体多样性极难靠手工搭建。',
   build='用**生成式数字孪生**批量生成多样化物体与场景，从而在仿真中大规模构造双臂协同操作任务，并支持向真机迁移的评测。',
   models='双臂机器人操作策略（含 VLA）。',
   finding='生成式资产是解决场景多样性瓶颈的可行路径；双臂任务对协调性的要求暴露了单臂基准看不到的失败模式。',
   improve='①把双臂协调性作为独立指标；②生成的数字孪生需做真机一致性校验；③已被多篇安全基准复用为场景底座（Trap-RoboTwin、ForesightSafety-VLA）。'),
 'RoboCasa': dict(
   stage='动作控制（日常场景规模化）',
   problem='机器人规模化受制于缺乏大规模数据集；主张用高保真物理仿真来扩展环境、任务与数据。',
   build='以厨房为主的大规模日常场景，提供**数千个场景与大量人类示范**，用于训练与评测通用操作策略。',
   models='通用操作策略（含 VLA）。',
   finding='仿真规模化可显著扩展任务与数据；但场景真实性仍需校验，其扩展版 RoboCasa365 进一步扩大了任务规模。',
   improve='①把家居长时程任务纳入标准评测；②场景多样性需与真实世界分布对齐；③作为安全评测底座时可叠加阶段感知诊断（RoboCasa-Shift）。'),
 'VLABench': dict(
   stage='认知 + 规划（长时程推理）',
   problem='多数基准只要求把一条指令映射为一次抓取，缺少需要多步推理与常识才能完成的任务。',
   build='大规模语言条件操作基准，任务强调**长时程推理**与**组合泛化**，需要常识知识支撑才能完成。',
   models='语言条件操作策略 / VLA。',
   finding='把评测重心从单步操作成功率推向「推理—规划—执行」整链能力；组合泛化是当前模型的主要短板。',
   improve='①任务应要求多步推理而非单次操作；②需区分「看到了」与「推理出来了」；③组合泛化需要系统性任务设计。'),
 'COLOSSEUM': dict(
   stage='感知（泛化边界）',
   problem='模仿学习策略在训练分布外能否泛化并不清楚，而单一数字无法说明泛化失败的原因。',
   build='用 **20+ 种环境扰动因子**（物体、纹理、光照、相机位姿、桌面高度等）系统评测策略的泛化边界，并给出不同扰动对成功率的影响排序。',
   models='模仿学习策略（含 VLA）。',
   finding='泛化不是一个标量：它对不同扰动因子的敏感度差异极大，必须逐因子归因。',
   improve='①逐因子报告泛化；②扰动设计应贴近真实部署变化；③是后续 LIBERO-Plus、VLA-GAUGE 等方法论的直接前身。'),
 'ManiSkill / ManiSkill2': dict(
   stage='动作控制（可泛化技能）',
   problem='既有多数操作基准只是「一组可仿真环境」，缺乏物体级拓扑与几何变化、非完全动态仿真，或缺少对多类操作任务的原生支持。',
   build='SAPIEN 系列的下一代统一基准：提供**物体级拓扑与几何变化**、**完全动态仿真**、以及对抓取、移动、装配、软体等多类任务的原生支持。',
   models='强化学习与模仿学习策略（含 VLA 微调）。',
   finding='物体级变化与完全动态仿真是可泛化操作技能的必要条件；该平台被大量鲁棒性研究用作受控实验环境（如域随机化机制分析）。',
   improve='①需要物体级而非类别级变化；②动态仿真不可省略；③可作为安全约束注入的轻量实验床。'),
}

# 核心基准的本地全文核查补录。材料位于仓库同级的 docs/_fulltext，
# 只把全文中可直接核对的协议、数字和结论写入生成文档；没有全文的条目继续保持摘要级证据。
FULLTEXT_DETAILS = {
 'SafeStage': dict(
   source='SafeStage.txt',
   protocol='97 个专门设计任务：ISH 27、ETS 40、FSH 30。每个任务同时定义目标、主动安全条件、不安全路径和安全解；在 RoboLab GPU PhysX（120 Hz）中使用 7-DoF Franka Panda + Robotiq 2F-85，8D 绝对关节位置/夹爪动作，15 Hz 闭环执行。每个任务-策略-提示条件使用 3 个环境种子、每种子 10 次 rollout；提示分为默认、generic、specific。',
   quantitative='评估器使用位姿、接触、支撑、包含关系、区域、位移、朝向和速度等 privileged 信号；接触阈值为 >0.1 N 且需跨多帧持续。FSH 在任务完成后保持机器人姿态并继续观察 5 秒。对 240 条人工核验 rollout 的自动判分精度为 95.81%、召回率 98.77%、F1 97.26%；分阶段 F1 为 ISH 98.65、ETS 96.43、FSH 95.65。默认提示汇总 SR 33.74%、SSR 9.84%，成功但不安全的 rollout 占全部 23.90%；在默认成功 rollout 中 70.84% 不安全。',
   findings='specific 提示并未自动带来安全性提升：其成功执行中 73.16% 不安全；generic 提示下该比例为 69.98%。generic 条件的 ISH/FSH 成功 rollout 中不安全比例分别为 86.77%/82.17%，ETS 为 50.93%，说明初态与终态风险容易被任务成功率掩盖。',
   limits='全文报告的是 RoboLab 仿真和预训练策略的结果；提示词、模型清单与任务级结果需结合原文附录逐项复核，不能把 SSR 直接解释为真实部署事故率。'),
 'ManiGuard-Bench': dict(
   source='ManiGuard.txt',
   protocol='每条 rollout 由基于 LTL_f 的自动机监控器检查物理谓词，任务按“技能 × 约束”组织为 200 个锁定基础任务；每个任务包含 1 个分布内和 4 个单轴 OOD 扰动，共 1,000 个锁定场景。安全标注由自动运动规划与人工遥操作组成，8,000 条示范（每任务 40 条）；同时覆盖仿真和 Franka 真机。',
   quantitative='全文将零样本与微调策略放在超过 23,000 次 rollout 上比较。6–21% 的成功 rollout 违反安全规约；在该基准上微调后，安全任务完成率由接近 0 提升到 7.5–29.8%，参与且安全的比例由 16–40% 提升到 51–72%，但参与型 rollout 仍有 21–42% 违规。',
   findings='安全违规与任务成功并不等价，形式化监控器揭示了成功率无法看到的安全缺口；示范规模增加并没有自动闭合约束违规差距。六个任务族中有两个对所有策略的安全成功率低于 2%，且在 OOD 与真机上持续存在。',
   limits='全文中的比例按任务族、策略和微调设置分组；汇总范围不能替代逐任务规约和真机配置核对。'),
 'ForesightSafety-VLA': dict(
   source='ForesightSafety-VLA.txt',
   protocol='RoboTwin 中从已有资产与原语人工构造 66 个基础场景，覆盖 Safe-Core、Safe-Lang、Safe-Vis 三侧 13 类风险；通过 hazard injection、constraint tightening、temporal precondition insertion 三类算子增强。结构/布局 L0–L2、语言 W0–W4、视觉 V0–V4 三个变化维度分别控制难度，W3–W4 的语言由前沿 LLM 生成后人工核验；视觉扰动在推理时累积且不改变物理动力学。',
   quantitative='实验覆盖 5 种本体；每个模型-任务-设置共 50 个 evaluation episodes，分布于 3 个随机种子，另对 10 个代表场景做诊断子集。四个完整基线的累计安全代价 CC 为 OpenVLA-oft 0.18、RDT 0.29、DP 0.34、ACT 0.39；unsafe-success 比例为 0.06、0.10、0.10、0.12。OpenVLA-oft 总成功率 0.48，成功回合中 12.5% 不安全；RDT、DP、ACT 的总成功率分别为 25.0%、29.4%、37.5%。',
   findings='结构与视觉变化造成的安全退化明显强于普通语言变化；对抗性语言 W3–W4 会造成额外风险。代表性 lift_pot 场景中热风险暴露约 40%、空间边界约 60%、力风险低于 10%，但任一风险激活的 episode 占 62%；Thermal/Energy 最难，Temporal Sequence 相对容易。',
   limits='部分扩展模型和逐类结果只在全文表格中给出；CC、RET 与四象限结果需要保持其原始阈值和 episode 聚合方式，不能与普通 success rate 直接混合。'),
 'SafeVLA-Bench': dict(
   source='SafeVLA-Bench.txt',
   protocol='安全规约覆盖力、位移、倾斜、力矩和自碰撞等信号；LIBERO 的每个模型-套件单元为 200 episodes（10 个任务 × 20），RoboCasa 每任务 50 episodes，连续指标用 episode 级 10,000 次 bootstrap 给出 95% 区间。默认阈值为 200 N、5 mm、15°、87 N·m；严重阈值约为两倍（力矩 174 N·m、倾斜 30°、位移 10 mm、力 400 N）。',
   quantitative='LIBERO 代表性结果：OpenVLA-7B SR/Safety/SBU/VSI 为 69.4/77.4/10.8/0.174；Octo 为 93.9/77.5/19.2/0.140；GR00T-N1.7 为 94.2/72.0/24.0/0.169；UniVLA 为 94.8/79.5/17.1/0.127；InternVLA-M1 为 96.4/81.5/16.8/0.118；VLA-Adapter 为 97.6/82.0/17.0/0.104；OpenVLA-OFT-7B 为 97.8/80.1/18.1/0.122。RoboCasa 的成功率整体更低，例如 Xiaomi-Robotics-1 为 81.9/50.1/37.7/0.233。',
   findings='LIBERO 中成功率超过 90% 的策略仍留下约 10–22% 的不安全成功；在 58 个任务中有 26 个呈现结构性 unsafe-success floor，PickPlaceDrawerToCounter 对所有策略均出现 100% 不安全成功。力违规通常是 50–200 ms、最长连续 1–4 步的冲击，位移/倾斜则可持续约 24–57 步。DPO 后一个代表性策略的 SR/Safety/SBU/VSI 从 99.5/85.0/14.5/0.107 变为 100.0/94.5/5.5/0.034。',
   limits='表格包含 18 个 LIBERO 策略和 9 个 RoboCasa 策略；文档仅保留代表性行，完整排序、任务级分布和硬件 pilot 仍应回看全文。'),
 'LIBERO-RIG': dict(
   source='LIBERO-RIG.txt',
   protocol='在四个 LIBERO 套件中固定任务、指令、物体和成功谓词，只扰动机器人硬件/配置；覆盖 11 条轴、5 个严重度和 210 个条件。每个条件包含 10 个任务 × 50 个初始状态，即 500 episodes；共评测 9 个 VLA（其中 8 个覆盖四套件，LingBot-VA 只跑 LIBERO-10）。',
   quantitative='汇总成功率由 nominal 0.932 降至中等严重度 0.767，再降至最高严重度 0.509。严重度 3 的跨轴均值约为：camera position 0.448、camera orientation 0.596、robot base 0.692、frame rotation 0.752、FOV 0.777、control frequency 0.786、table height/pad 0.846、wrist 0.890、gain 0.908、proprio 0.931。五档严重度汇总约为 0.914、0.845、0.767、0.591、0.509。',
   findings='相机位姿是最强的硬件敏感源；公开控制器直接使用真状态时，本体感觉噪声几乎不改变结果（0.931 对 0.932），但把状态噪声注入 OpenVLA 控制器后，2 cm 条件可由 0.960 降至 0.470。OFT-Plus 对 camera orientation/position 的改善约为 0.867/0.787，相比 OpenVLA 的 0.701/0.590；latent 轴的收益在 0.02 内。统计使用 10,000 次 permutation、5,000 次 bootstrap，并按每套件 10 个任务聚类。',
   limits='这是单本体仿真中的硬件配置压力测试；“真状态”与“视觉估计状态”的差异会改变 proprio 结论，不能把所有轴视为同一种部署故障。'),
 'LIBERO-CTRL': dict(
   source='LIBERO-CTRL.txt',
   protocol='六个公开语言条件策略（另有 MINERVA 身份语言辅助对照）覆盖 LIBERO Spatial/Object/Goal/Long 四套件；每套件 10 个任务、每任务 50 个 released initial states。主实验从每任务抽 10 个状态，并固定 10 组扰动预设，形成 40×10=400 个匹配 task-configuration；每个严重度评测六个单轴条件和一个同时条件，三档严重度。六轴为 camera、lighting、robot pose、sensor、actuation、language。',
   quantitative='每个 checkpoint 先在四套件的 2,000 个 nominal rollouts 上复现；六个主策略包括 OpenVLA-OFT、UniVLA、SmolVLA、VLA-JEPA、PredVLA 和一项匿名公式模型。全文摘要给出：即使聚合差异无法显著区分，最多 29.0% 的匹配初始状态仍改变结果；最受影响的 policy-severity 条件变化率达 34.5%。统计用按任务聚类的 bootstrap，并对三种随机策略做独立随机种子复评。',
   findings='同时扰动条件下的 emergent failure（所有单轴成功、同时失败）与 compensated success（至少一个单轴失败、同时成功）方向相反，可能在总成功率中相互抵消；因此单轴边际或一个 signed difference 都不能描述复合鲁棒性，必须报告逐实例配对结果和两个方向的转移率。',
   limits='实验是在单一本体的仿真中对六轴全组合做受控测试；同时条件不能定位具体哪个低阶扰动子集触发转移，语言轴也是类别变量而非可度量严重度。'),
 'LIBERO-VPro': dict(
   source='LIBERO-VPro.txt',
   protocol='四个挑战维度为视觉证据退化、相机陈旧、视觉源一致性和任务相关场景变化，细分 12 类挑战、96 种设置、3,296 个任务-条件案例；覆盖四套 LIBERO 的 40 个任务，六个模型（3 个 VLA、3 个 WAM），每个案例 10 trials，约 196,000 个仿真 episodes。另在 Franka Research 3 上进行 200 次真机 rollout。',
   quantitative='视觉证据退化包含目标/容器遮挡比例 25/50/75/100% 与四种时序、交互线索遮挡、短时 blackout/noise 和视角不可用；相机陈旧包含 3 档固定延迟、冻结和历史回放；一致性包含跨视角矛盾和预测-现实分歧；场景变化包含 distractor、前置条件变化、视觉歧义以及 Taper/Multipeak/Twist/Asymmetric 几何。LingBot 的递归自预测总体成功率由 97.0 降至 53.8，Long 套件由 98 降至 22。',
   findings='交互线索遮挡通常比目标物体遮挡更致命；第三视角/腕部视角缺失和陈旧观测会造成严重退化；目标熟悉位置出现空间 distractor 可使多模型成功率崩溃，真实前置条件变化比单纯视觉歧义更难。真机在缺失视角、跨视角矛盾下接近全面失败，陈旧度的影响则依任务而变。',
   limits='真机只覆盖 Pick-and-Place 与 Move 两类任务；WAM 与 VLA 的观测接口不同，横向比较应按模型类别和具体设置分别解释。'),
 'HazardArena': dict(
   source='HazardArena.txt',
   protocol='从 2,000+ 物体资产和 75 个新建语境关键资产中组织 51 个任务，覆盖 food、property、chemical、privacy、fire、personal、electrical 七类风险。任务采用 Pick-Place、Insert、Pour、Camera-Explore 模板，安全/不安全 twin 共享场景、技能模板和动作要求，只改变 actor-target 绑定或 instruction；阶段标记 Attempt、Commit、Success，以区分危险意图/推进与终点成功。',
   quantitative='四个 VLA 在仿真主实验使用跨类别安全/不安全配对；VLA-Adapter 安全微调前 Safe SR/Unsafe SR/Unsafe Commit 为 0.25/0.22/0.44，加拒答数据后为 0.26/0.01/0.03；另一代表性模型由 0.36/0.33/0.61 变为 0.36/0.04/0.06。真机 Franka Panda 使用腕部和场景 RGB 相机，5 个任务族、每族 2 条安全和 1 条不安全指令、每条件 100 trials；平均 Safe SR 由 46.0% 变为 47.4%，Unsafe SR 由 39.6% 降至 0.4%。安全层 Qwen3-VL-32B 的平均 recall/FPR/F1 为 0.77/0.10/0.76。',
   findings='仅看终点 SR 会漏掉 Commit 阶段的危险推进；拒答微调几乎消除不安全成功，同时保持安全成功率。类别间存在明显差异，Electrical/Fire/Privacy 的安全层召回可达 1.00，而 Property 为 0.00，说明通用视觉安全层仍有语境盲区。',
   limits='仿真和真机使用不同样本规模与接口；安全层指标是分类器指标，不能替代实际策略的拒答和动作结果。'),
 'DESPITE': dict(
   source='DESPITE.txt',
   protocol='从 5 个异质来源构造 12,279 个具身规划任务，另设 1,044 个 hard split；形式验证器把计划分为 infeasible、feasible-unsafe、feasible-safe，并允许冗余但安全的计划。主要指标为 Feasibility、Safety、Safety Precision、Safety Intention；7 个模型完成全量任务，另比较 18 个 3B–671B 开源模型与 proprietary reasoning 模型。',
   quantitative='最佳规划模型的 infeasible 约 0.4%，但 dangerous plan 仍约 28.3%；开源模型 feasibility 为 0.4–99.3%，Safety Intention 约 37.6–56.9%，专有 reasoning 模型约 71–81%。hard split 中 GPT-5 的 feasibility 99.5、Safety Precision 81.4；高可行性难例中 physical danger 占 70.6–88.2%，高安全性/意图难例中 normative danger 占 18.4–40.0%/15.7–42.5%。加入 2–64 个无关动作后，feasibility 下降 21.0%、Safety Intention 下降 17.3%，联合安全退化 37.9%。',
   findings='规划可执行与规划安全是两个不同能力轴；模型即使能找到合法计划，也常未识别物理或规范危险。PDDL/基础问题格式会隐藏危险语境，确定性验证器和冗余安全计划设计是该基准可复核性的关键。',
   limits='该基准评测的是语言模型生成的具身计划和形式验证结果，不能直接代替 VLA 的连续控制安全；不同模型的提示、推理模式和输出预算仍需按原文协议解释。'),
 'RoboHarm': dict(
   source='RoboHarm.txt',
   protocol='5 个不安全任务（doll、burner、toaster、brick、pour）组成场景-指令对，覆盖直接伤害和需理解物体后果的潜在危险；在 MuJoCo 中重建 I2RT YAM 双臂机器人的仿真 twin，并在真机上复核。比较 text、Code as Policies、视觉 EEF pose、带对象清单的 EEF-N 与 joint-angle 接口；仿真每个模型-任务-接口 5 trials，文本单元 10 samples。',
   quantitative='文本拒答率为 user-framed 73%、robot-framed 84%，切换到 CaP/EEF/EEF-N/joint 后降至 25%/19%/18%/19%。真机 6 个模型完成 612 次 EEF 和 252 次 joint trials；真实 EEF 拒答 18%，joint 拒答 41%，与仿真 EEF 19%、joint 31% 同方向。burner/brick 在真机仅 8/254 拒答，toaster 为 0/120；doll 为 70/118。',
   findings='拒答从文本到动作接口大幅下降，且并非只由缺少对象信息导致：同一对象清单下 robot-framed text 对 burner/toaster/brick 的拒答为 51/70、53/70、68/70，而 EEF-N 对这些危险均无拒答。全文把失败归为感知不确定、感知错误、后果推理失败和价值/对齐失败；例如 21/22 次 EEF pour 识别 Clorox 与 ammonia 标签后仍有 18 次尝试。',
   limits='每个任务只有一种措辞，单元样本量较小，仿真 transcript 由 LLM judge 标注；评测知情效应可能高估拒答率，结果应解释为接口迁移缺口而非完整危害覆盖率。'),
}

# 面向 ESB-2 选型的复用角色。它们描述“可复用的评测思想”，不表示已经完成实现。
ESB2_ROLE = {
 'SafeStage': ('生命周期阶段诊断', '把初始态、执行期、终态分开判分，支持 S1/S2/S3 定位。'),
 'ManiGuard-Bench': ('形式化规约与运行时监控', '提供 LTL_f 自动机、逐步物理谓词和安全/能力解耦的判分范式。'),
 'ForesightSafety-VLA': ('过程级风险与四象限', '提供 Safe-Core/Lang/Vis 三侧分类、累计代价、暴露时间和安全/不安全成功失败分解。'),
 'SafeVLA-Bench': ('通用安全测量层', '提供 STL 规约、Safety/SBU/VSI 与跨 LIBERO/RoboCasa 的可移植指标。'),
 'LIBERO-RIG': ('latent 硬件偏移', '覆盖不改变图像的相机、控制器和本体配置扰动，补齐部署侧鲁棒性。'),
 'LIBERO-CTRL': ('复合扰动配对', '用匹配初始状态区分 emergent failure 与 compensated success，避免聚合抵消。'),
 'LIBERO-VPro': ('视觉证据时序', '覆盖遮挡、陈旧、跨视角矛盾和场景变化，连接视觉接地与动作适应。'),
 'HazardArena': ('语义孪生与 Commit 事件', '保持场景和动作要求不变，只改变风险语境，并记录危险推进阶段。'),
 'DESPITE': ('规划能力与安全双轴', '用确定性验证区分可行、危险和安全计划，适合 L3 规划层。'),
 'RoboHarm': ('接口迁移与具身拒答', '固定模型和危险任务，只切换文本、代码、末端位姿和关节接口。'),
}

ORDER = ['VLA 安全', 'VLA 鲁棒性', 'VLA 能力', '具身智能体安全', '具身安全']


def slug(name):
    s = re.sub(r'[^\w\u4e00-\u9fff]+', '-', name).strip('-')
    return s[:80]


ROWBY = {r['title']: r for r in json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))}


def compact(value, limit=None):
    """Make a field safe and readable in generated Markdown."""
    text = re.sub(r'\s+', ' ', str(value or '').strip()).replace('|', '／')
    if limit and len(text) > limit:
        return text[:limit - 1].rstrip() + '…'
    return text


def excerpt(value, limit=220):
    """Keep an abstract-level excerpt without pretending it is a full-text result."""
    text = compact(value)
    if not text:
        return '调研表未记录摘要级内容。'
    # Prefer complete sentences, but retain a useful prefix for entries without punctuation.
    parts = [p.strip() for p in re.split(r'(?<=[。！？；.!?])', text) if p.strip()]
    out = ''
    for part in parts:
        candidate = (out + part).strip()
        if len(candidate) > limit:
            break
        out = candidate
    return compact(out or text, limit)


def infer_tags(blob):
    """Infer broad tags from the existing structured text; these are discovery aids, not new labels."""
    rules = [
        ('语义/指令安全', r'语义|指令|语言|语境|semantic|instruction|language|context|grounding'),
        ('物理/接触安全', r'碰撞|接触|力|力矩|稳定|形变|断裂|损伤|污染|卫生|物理|contact|force|stability|damage'),
        ('分布偏移鲁棒性', r'扰动|偏移|鲁棒|视角|光照|噪声|退化|硬件|标定|遮挡|shift|robust|perturb|noise|hardware'),
        ('对抗/后门安全', r'对抗|攻击|后门|越狱|注入|投毒|adversar|attack|backdoor|jailbreak|inject'),
        ('失败恢复', r'失败|恢复|纠正|回滚|故障|recover|failure|recovery|fault'),
        ('实时/治理', r'实时|延迟|治理|权限|审计|授权|监控|real-time|latency|governance|audit'),
        ('任务能力', r'能力|成功率|任务完成|泛化|规划|操作|benchmark|success|generalization'),
    ]
    return [label for label, pattern in rules if re.search(pattern, blob, re.I)]


def infer_platform(blob):
    names = [
        'LIBERO', 'RoboTwin', 'RoboCasa', 'RoboCasa365', 'CALVIN', 'SimplerEnv',
        'ManiSkill', 'Isaac Sim', 'OmniGibson', 'SAPIEN', 'MuJoCo', 'Habitat',
        'CARLA', 'SUMO', 'nuScenes', 'NAVSIM', 'BEHAVIOR-1K', 'Franka',
        'RoboLab', 'PhysX', 'YAM',
    ]
    found = []
    for name in names:
        if re.search(re.escape(name), blob, re.I) and name not in found:
            found.append(name)
    return '、'.join(found) if found else '表内摘要未明确基础平台。'


def infer_scale(blob):
    patterns = [
        r'\b\d[\d,]{0,8}\s*(?:个|组|条|次|种|对)?[^。；，,\n]{0,30}(?:任务|场景|实例|案例|回合|设置|条件|样本|轨迹|示范|rollout|episodes?|tasks?|scenarios?|cases?|settings?)',
    ]
    hits = []
    for pattern in patterns:
        for hit in re.findall(pattern, blob, re.I):
            hit = compact(hit)
            if hit not in hits:
                hits.append(hit)
    return '；'.join(hits[:8]) if hits else '表内摘要未明确规模。'


def infer_execution(blob):
    sim = bool(re.search(r'仿真|模拟|simulation|simulator|digital twin|LIBERO|RoboTwin|CARLA', blob, re.I))
    real = bool(re.search(r'真机|真实环境|实体机器人|real[- ]world|real[- ]robot|physical robot|Franka|硬件实验', blob, re.I))
    if sim and real:
        return '摘要同时提到仿真与真机/实体机器人。'
    if real:
        return '摘要提到真机/实体机器人。'
    if sim:
        return '摘要提到仿真/模拟环境。'
    return '表内摘要未明确执行环境。'


def evidence_level(detail, self_paper):
    if detail:
        return 'A', '人工扩写字段 + 表内摘要；未逐篇精读全文'
    if self_paper:
        return 'B', '提出论文的结构化摘要记录；未逐篇精读全文'
    return 'C', '原始提出论文未单列；依据使用论文的摘要转述'


def suggested_followups(tier, tags, reused):
    """Generate explicitly labelled review prompts from known gaps in the survey fields."""
    prompts = []
    if '分布偏移鲁棒性' in tags:
        prompts.append('按扰动轴、严重度和 clean/OOD 对照分别报告结果，避免只保留聚合成功率。')
    if '物理/接触安全' in tags:
        prompts.append('补充约束定义、违规阈值和过程/终态指标，确认安全成功与任务成功是否分开统计。')
    if '语义/指令安全' in tags:
        prompts.append('核对安全/不安全语境或指令的配对构造，确认是否控制了视觉场景和动作要求。')
    if '对抗/后门安全' in tags:
        prompts.append('分别记录攻击成功率、干净任务性能和真实/仿真迁移，避免只报告单一攻击分数。')
    if '失败恢复' in tags:
        prompts.append('明确失败注入时刻、失败识别标准和恢复成功判据。')
    if '实时/治理' in tags:
        prompts.append('补充时延、审计、权限或监督介入的操作性定义与可复现实验协议。')
    if not reused:
        prompts.append('当前尚无跨论文复用证据，需由独立工作复测后再形成稳定的横向结论。')
    if not prompts:
        prompts.append('从原文补充任务划分、指标公式、基线配置和失败案例，以便独立复现。')
    return prompts


def write_comparison_outputs(cards):
    """Write machine-readable cards and a human-readable cross-benchmark comparison."""
    data_dir = os.path.join(REPO, 'data')
    analysis_dir = os.path.join(REPO, 'analysis')
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(analysis_dir, exist_ok=True)
    ordered = sorted(cards, key=lambda c: (ORDER.index(c['tier']) if c['tier'] in ORDER else 9, c['name']))
    payload = {
        'schema_version': 1,
        'generated_by': 'scripts/build_benchmark_docs.py',
        'benchmark_count': len(ordered),
        'fulltext_count': sum(1 for c in ordered if c['fulltext']['status']),
        'cards': ordered,
    }
    with open(os.path.join(data_dir, 'benchmark_cards.json'), 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write('\n')

    def cell(value, limit=120):
        return compact(value, limit).replace('\n', ' ')

    tier_rows = []
    for tier in ORDER:
        group = [c for c in ordered if c['tier'] == tier]
        if not group:
            continue
        tier_rows.append('| %s | %d | %d | %d | %d |' % (
            tier, len(group), sum(c['fulltext']['status'] for c in group),
            sum(c['reuser_count'] > 0 for c in group),
            sum(len(c['coverage']['axes']) >= 2 for c in group)))

    stage_counts = collections.Counter()
    axis_counts = collections.Counter()
    matrix = {stage: collections.Counter() for stage in STAGES_FROM_ONTOLOGY}
    for card in ordered:
        for stage in card['coverage']['stages']:
            if stage in matrix:
                stage_counts[stage] += 1
                for axis in card['coverage']['axes']:
                    if axis in AXES_FROM_ONTOLOGY:
                        matrix[stage][axis] += 1
        for axis in card['coverage']['axes']:
            if axis in AXES_FROM_ONTOLOGY:
                axis_counts[axis] += 1

    lines = [
        '# 基准卡片与跨基准比较', '',
        '> 本文件由 `scripts/build_benchmark_docs.py` 自动生成；用于从单篇 benchmark 文档进入横向选型。',
        '> 关键词分类是发现性下界，全文补录只覆盖 10 个核心基准，不能替代逐篇协议核查。', '',
        '## 1. 数据范围与用途', '',
        '- 基准：**%d** 个；关联论文：**%d** 篇。' % (len(ordered), len(ROWBY)),
        '- 全文核查补录：**%d** 个；至少有一篇后续使用论文：**%d** 个。' % (
            sum(c['fulltext']['status'] for c in ordered), sum(c['reuser_count'] > 0 for c in ordered)),
        '- “后续使用”只计同时有提出论文和非提出论文的条目；若本表只有使用论文，则保留为“原始提出论文未单列”。',
        '- `data/benchmark_cards.json` 是机器可读入口；`data/benchmark_source_audit.json` 记录提出来源核验；本文件保留分类口径、核心对照和选型建议。', '',
        '## 2. 按分类汇总', '',
        '| 分类 | 基准数 | 全文补录 | 有后续使用 | 覆盖至少 2 类安全属性 |',
        '|---|---:|---:|---:|---:|',
    ] + tier_rows + [
        '', '## 3. 环节 × 安全属性比较', '',
        '下表按每个基准的提出论文摘要和定位描述做关键词分类；一个基准可以命中多个环节和属性。', '',
        '| 环节 | ' + ' | '.join(AXES_FROM_ONTOLOGY) + ' | 基准数 |',
        '|---|' + '---:|' * (len(AXES_FROM_ONTOLOGY) + 1),
    ]
    for stage in STAGES_FROM_ONTOLOGY:
        lines.append('| %s | %s | %d |' % (
            stage,
            ' | '.join(str(matrix[stage][axis]) for axis in AXES_FROM_ONTOLOGY),
            stage_counts[stage],
        ))
    lines += [
        '', '**属性覆盖（去重计数）**：%s。' % '；'.join('%s %d' % (a, axis_counts[a]) for a in AXES_FROM_ONTOLOGY),
        '', '## 4. 核心全文基准对照', '',
        '| 基准 | 可复用评测角色 | 主要平台 | 规模线索 | 覆盖环节 | 覆盖属性 | 关键定量证据 | 文档 |',
        '|---|---|---|---|---|---|---|---|',
    ]
    for card in ordered:
        if not card['fulltext']['status']:
            continue
        lines.append('| %s | %s | %s | %s | %s | %s | %s | [%s](../benchmarks/%s) |' % (
            cell(card['name'], 42),
            cell(card['esb2_role']['label'] if card['esb2_role'] else '—', 60),
            cell(card['platform_hint'], 60), cell(card['scale_hint'], 80),
            cell('、'.join(card['coverage']['stages']), 70),
            cell('、'.join(card['coverage']['axes']), 90),
            cell(card['fulltext']['quantitative'], 230),
            cell(card['name'], 42), card['document'],
        ))
    lines += [
        '', '## 5. ESB-2 复用建议', '',
        '核心基准可以按“评测层”组合，而不是把它们当作互斥任务集：', '',
        '| 设计层 | 优先参考 | 应保留的协议思想 |',
        '|---|---|---|',
        '| 阶段定位 | SafeStage；ForesightSafety-VLA | 初始态、执行期、终态分开报告，并保留过程级风险。 |',
        '| 统一判分 | ManiGuard-Bench；SafeVLA-Bench | 公开物理谓词、形式化规约和可审计的安全/能力双轴。 |',
        '| 配对归因 | HazardArena；LIBERO-CTRL；LIBERO-RIG；LIBERO-VPro | 固定 task/seed/policy，只改变语境、组合扰动、硬件或视觉证据。 |',
        '| 规划与接口 | DESPITE；RoboHarm | 分离计划安全与动作安全，观察文本对齐向具身接口迁移时的损失。 |',
        '',
        '下一步实施时，优先把 SafeVLA-Bench 的规约层与 SafeStage 的阶段层组合，再用 HazardArena/LIBERO-CTRL 的配对协议做归因；LIBERO-RIG、LIBERO-VPro 和 RoboHarm 可作为部署侧扩展。',
        '', '## 6. 全量卡片索引', '',
        '| 基准 | 分类 | 环节 | 安全属性 | 平台 | 规模线索 | 全文 | 后续使用 | 文档 |',
        '|---|---|---|---|---|---|---|---:|---|',
    ]
    for card in ordered:
        lines.append('| %s | %s | %s | %s | %s | %s | %s | %d | [%s](../benchmarks/%s) |' % (
            cell(card['name'], 42), cell(card['tier'], 18),
            cell('、'.join(card['coverage']['stages']), 70),
            cell('、'.join(card['coverage']['axes']), 90),
            cell(card['platform_hint'], 50), cell(card['scale_hint'], 70),
            '是' if card['fulltext']['status'] else '—', card['reuser_count'],
            cell(card['name'], 42), card['document'],
        ))
    with open(os.path.join(analysis_dir, 'benchmark-comparison.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


outdir = os.path.join(REPO, 'benchmarks')
os.makedirs(outdir, exist_ok=True)
index = collections.defaultdict(list)
cards = []

for name, info in reg.items():
    tier, desc, papers = info['tier'], info['desc'], info['papers']
    audit = SOURCE_AUDIT.get(name)
    d = DETAIL.get(name)
    full = FULLTEXT_DETAILS.get(name)
    self_paper = [p for p in papers if p['self']]
    others = [p for p in papers if not p['self']]
    primary = self_paper[0] if self_paper else papers[0]
    primary_row = ROWBY.get(primary['title'], {})
    source_rows = [ROWBY.get(p['title'], {}) for p in papers]
    source_rows = [r for r in source_rows if r]
    blob_parts = [name, desc]
    for row in source_rows:
        blob_parts += [row.get('area', ''), row.get('domain', ''), row.get('obj', ''),
                       row.get('dim', ''), row.get('summ', '')]
    if d:
        blob_parts += [d.get('stage', ''), d.get('problem', ''), d.get('build', ''), d.get('finding', '')]
    blob = ' '.join(blob_parts)
    tags = infer_tags(blob)
    coverage_stages, coverage_axes = classify(name, info, ROWBY)
    hint_blob = blob + (' ' + full['protocol'] + ' ' + full['quantitative'] if full else '')
    evidence_code, evidence_text = evidence_level(d, self_paper)
    if full:
        evidence_text = evidence_text.replace('；未逐篇精读全文', '')
        evidence_text += '；另附本地全文核查补录'
    years = sorted({str(p.get('year') or '') for p in papers if p.get('year')}, key=lambda x: (x == '', x))
    sources = sorted({compact(ROWBY.get(p['title'], {}).get('src')) for p in papers
                      if ROWBY.get(p['title'], {}).get('src')})
    source_link = primary_row.get('link') or primary.get('link') or ''
    target = (d.get('models') if d else primary_row.get('obj')) or '表内摘要未明确被测对象。'
    dim = primary_row.get('dim') or '表内未记录评测维度与指标。'
    summary = primary_row.get('summ') or '表内未记录摘要概要。'
    build_text = d.get('build') if d else ('本仓库当前保存的是摘要级构建信息：%s' % dim)

    L = ['# %s' % name, '',
         '> **所属环节**：%s  ' % (d['stage'] if d else desc),
         '> **分类**：%s  ' % tier,
         '> **关联论文**：本表 %d 篇（提出者 %d 篇，使用者 %d 篇）' % (
             len(papers), len(self_paper), len(others)),
         '> **证据级别**：%s（%s）' % (evidence_code, evidence_text), '']

    L += ['## 0. 评测卡片', '',
          '| 字段 | 当前整理结果 |', '|---|---|',
          '| 首发/代表论文 | %s |' % compact(primary_row.get('title') or primary.get('title'), 120),
          '| 年份 | %s |' % ('、'.join(years) if years else '未记录'),
          '| 数据来源 | %s |' % ('、'.join(sources) if sources else '未记录'),
          '| 论文库分区 | %s |' % compact(primary_row.get('area') or '未标注'),
          '| 应用领域 | %s |' % compact(primary_row.get('domain') or '未标注'),
          '| 被测对象 | %s |' % compact(target, 180),
          '| 关注属性 | %s |' % ('、'.join(tags) if tags else '尚未从摘要识别'),
          '| 评测维度/指标 | %s |' % compact(dim, 220),
          '| 基础平台线索 | %s |' % infer_platform(hint_blob),
          '| 规模线索 | %s |' % infer_scale(hint_blob),
          '| 执行环境线索 | %s |' % infer_execution(hint_blob)]
    if audit:
        source_label = '%s（%s）' % (audit.get('source_title'), audit.get('kind'))
        L += ['| 来源审计 | 已核验：[%s](%s) |' % (compact(source_label, 180), audit.get('source_link') or ''),
              '| 来源核验依据 | %s |' % compact(audit.get('source_basis') or '已核对论文元数据与摘要。', 220)]
    if full:
        L += ['| 全文状态 | 已核查本地全文：`docs/_fulltext/%s` |' % full['source']]
    L += ['']

    L += ['## 1. 测什么问题（内容与所测环节）', '']
    if d:
        L += ['**核心问题**：%s' % d['problem'], '']
    else:
        L += ['**核心问题**：%s。' % desc, '',
              '**摘要级问题描述**：%s' % summary, '']
        L += ['信息取自表内论文 *%s*%s。' % (
            primary_row.get('title') or primary['title'],
            '（该基准的提出者）' if self_paper else
            '（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）'), '']
    if primary_row.get('dim'):
        L += ['**主要测量维度**：%s。' % compact(primary_row['dim']), '']

    L += ['## 2. 怎么构建的', '']
    L += ['### 2.1 构建要素', '',
          '| 要素 | 摘要级记录 |', '|---|---|',
          '| 基础平台 | %s |' % infer_platform(hint_blob),
          '| 任务/场景规模 | %s |' % infer_scale(hint_blob),
          '| 扰动、风险或约束 | %s |' % compact(dim, 220),
          '| 对照/配对方式 | %s |' % ('摘要提到配对、孪生或受控对照。' if re.search(r'配对|孪生|对照|paired|twin|controlled|same-scene', blob, re.I) else '摘要未明确配对设计。'),
          '| 指标与判分线索 | %s |' % compact(dim, 220),
          '| 执行设置 | %s |' % infer_execution(hint_blob), '']
    L += ['### 2.2 详细说明', '', build_text, '']
    if not d:
        L += ['> 本节依据当前调研表的摘要和结构化字段整理；任务划分、阈值、采样方式和完整指标公式仍需回到原文核对。', '']

    L += ['## 3. 用这个基准测了什么', '']
    L += ['**被测对象**：%s' % compact(target, 220), '',
          '**结果应如何读取**：先按“评测维度/指标”字段区分主指标、辅助指标和对照条件；若论文同时报告任务成功与安全/鲁棒性结果，应将二者分开阅读。', '',
          '下表按论文列出；“摘要级发现”保留调研表中的概要，不等同于全文实验结论。', '',
          '| 论文 | 年份 / 来源 | 角色 | 被测对象 | 使用方式 / 指标 | 摘要级发现 |',
          '|---|---|---|---|---|---|']
    for p in papers:
        row = ROWBY.get(p['title'], {})
        role = '**提出**' if p['self'] else '使用'
        use = row.get('dim') or row.get('cat') or '表内未记录使用方式。'
        finding = row.get('summ') or '表内未记录摘要级发现。'
        link = row.get('link') or p.get('link') or ''
        L.append('| [%s](%s) | %s / %s | %s | %s | %s | %s |' % (
            compact(row.get('zh') or p['title'], 42), link, compact(p.get('year') or '—'),
            compact(p.get('venue') or '—', 28), role, compact(row.get('obj') or target, 100),
            compact(use, 150), excerpt(finding, 150)))
    L.append('')

    L += ['## 4. 关键结论、改进方向与可复用性', '']
    if d:
        L += ['**关键结论**：%s' % d['finding'], '',
              '**论文提到的改进方向**：%s' % d['improve'], '']
    else:
        L += ['**摘要级发现（按关联论文整理）**：', '']
        for p in papers:
            r2 = ROWBY.get(p['title'], {})
            L.append('- **%s**（%s，%s）：%s' % (
                compact(r2.get('zh') or p['title'], 52), p.get('year') or '—',
                '提出' if p['self'] else '使用', excerpt(r2.get('summ'), 260)))
        L += ['', '**基于当前字段的改进提示（不是原文逐字结论）**：', '']
        for prompt in suggested_followups(tier, tags, bool(others)):
            L.append('- %s' % prompt)
        L.append('')
    if others and self_paper:
        reuse_status = '已有至少一篇后续论文使用，具备初步跨论文证据。'
    elif others and not self_paper:
        reuse_status = '本表含使用论文，但原始提出论文未单列，暂不能确认是否形成复用链。'
    else:
        reuse_status = '当前只看到提出论文，尚无跨论文复用证据。'
    L += ['**复用状态**：%s' % reuse_status, '']

    L += ['## 5. 相关论文（均来自本调研表）', '']
    for p in papers:
        link = ROWBY.get(p['title'], {}).get('link') or p.get('link') or ''
        L.append('- [%s](%s)（%s，%s）%s' % (p['title'], link, p['year'], (p['venue'] or '—')[:40],
                                      '  ← **提出**' if p['self'] else ''))
    L += ['', '## 6. 证据边界与复核建议', '']
    if full:
        L += ['### 6.1 全文核查补录（核心论文）', '',
              '> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。', '',
              '**来源文件**：`docs/_fulltext/%s`。' % full['source'], '',
              '**评测协议**：%s' % full['protocol'], '',
              '**定量证据**：%s' % full['quantitative'], '',
              '**全文结论**：%s' % full['findings'], '',
              '**适用边界**：%s' % full['limits'], '',
              '### 6.2 证据边界与复核建议', '']
    L += ['- **证据级别**：%s（%s）。' % (evidence_code, evidence_text),
          '- **主要来源**：[%s](%s)。' % (compact(primary_row.get('title') or primary['title'], 120), source_link),
          '- **当前限制**：本文档基于调研表、论文摘要和少量人工整理；核心条目另有本地全文核查补录，但仍未替代对全文实验表格、附录、代码仓库和数据下载说明的逐项复核。',
          '- **建议复核**：优先确认任务/场景划分、样本规模、指标公式、判分阈值、模型清单，以及仿真与真机设置是否一致。', '',
          '---', '', '*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成。'
          ' A 级文档含人工扩写字段；核心条目附本地全文核查补录；B/C 级文档主要依赖摘要级结构化记录。*', '']

    fn = '%s__%s.md' % (ORDER.index(tier) + 1 if tier in ORDER else 9, slug(name))
    open(os.path.join(outdir, fn), 'w', encoding='utf-8').write('\n'.join(L))
    index[tier].append((name, fn, len(papers), len(others), evidence_code))
    paper_cards = []
    for p in papers:
        row = ROWBY.get(p['title'], {})
        paper_cards.append({
            'title': p['title'],
            'display_title': row.get('zh') or p['title'],
            'year': p.get('year'),
            'venue': p.get('venue'),
            'role': '提出' if p.get('self') else '使用',
            'link': row.get('link') or p.get('link') or '',
            'dimension': row.get('dim') or row.get('cat') or '',
            'summary': row.get('summ') or '',
        })
    role = ESB2_ROLE.get(name)
    card = {
        'name': name,
        'document': fn,
        'tier': tier,
        'stage_label': d['stage'] if d else desc,
        'problem': d['problem'] if d else summary,
        'build': build_text,
        'finding': d['finding'] if d else summary,
        'improve': d['improve'] if d else None,
        'tags': tags,
        'platform_hint': infer_platform(hint_blob),
        'scale_hint': infer_scale(hint_blob),
        'execution_hint': infer_execution(hint_blob),
        'dimension': dim,
        'years': years,
        'sources': sources,
        'source_link': source_link,
        'primary_paper': primary['title'],
        'paper_count': len(papers),
        'user_count': len(others),
        'reuser_count': len(others) if self_paper else 0,
        'has_self_paper': bool(self_paper),
        'evidence': {'code': evidence_code, 'description': evidence_text},
        'fulltext': ({
            'status': True,
            'source': full['source'],
            'protocol': full['protocol'],
            'quantitative': full['quantitative'],
            'findings': full['findings'],
            'limits': full['limits'],
        } if full else {
            'status': False,
            'source': None,
            'protocol': None,
            'quantitative': None,
            'findings': None,
            'limits': None,
        }),
        'esb2_role': ({'label': role[0], 'use': role[1]} if role else None),
        'coverage': {'stages': coverage_stages, 'axes': coverage_axes},
        'papers': paper_cards,
    }
    if audit:
        card['source_audit'] = audit
    cards.append(card)

# 索引
L = ['# 基准文档索引', '',
     '本目录为每个基准一份独立文档，共 **%d** 份，对应调研表中的 %d 篇论文。' % (
         sum(len(v) for v in index.values()), len(ROWBY)), '',
     '文档结构：①评测卡片 ②测什么问题 ③怎么构建 ④逐篇论文证据 ⑤关键结论与改进方向 ⑥相关论文 ⑦证据边界；10 个核心条目另含全文核查补录。', '',
     '证据级别：A=人工扩写字段 + 摘要；B=提出论文摘要；C=使用论文转述。核心条目在此基础上补充 `docs/_fulltext` 的本地全文核查，仍保留原始证据边界。', '']
for tier in ORDER:
    if tier not in index:
        continue
    L += ['## %s（%d 个）' % (tier, len(index[tier])), '',
          '| 基准 | 表内论文数 | 其中使用者 | 证据级别 | 全文补录 | 文档 |', '|---|---|---|---|---|---|']
    for name, fn, n, o, evidence_code in sorted(index[tier], key=lambda x: (-x[2], x[0])):
        L.append('| %s | %d | %d | %s | %s | [%s](%s) |' % (
            name, n, o, evidence_code, '是' if name in FULLTEXT_DETAILS else '—',
            fn.replace('.md', ''), fn))
    L.append('')
open(os.path.join(outdir, 'README.md'), 'w', encoding='utf-8').write('\n'.join(L))

# ── 补充：未被任何基准文档覆盖的论文（多为评测方法 / 攻防 / 综述，未提出可复用基准）──
covered = ''.join(open(os.path.join(outdir, f), encoding='utf-8').read()
                  for f in os.listdir(outdir)
                  if f.endswith('.md') and not f.startswith('0__'))
left = [r for r in ROWBY.values() if r['title'] not in covered]
if left:
    left.sort(key=lambda r: (r['cat'], str(r['year'])))
    M = ['# 评测方法与协议汇总（未绑定单一基准）', '',
         '本表中以下 **%d 篇**论文，其贡献是**评测协议、度量方法、诊断分析或综述**，'
         '而不是一个可被反复复用的独立基准（或该基准即为本文自身的一次性评测集）。'
         '因此没有为它们单独建基准文档，集中在此说明。' % len(left), '',
         '| 论文（英文原名） | 中文题名 | 年 | 类别 | 评测设计 / 度量 |', '|---|---|---|---|---|']
    for r in left:
        M.append('| [%s](%s) | %s | %s | %s | %s |' % (
            r['title'], r['link'], (r['zh'] or '')[:36], r['year'], r['cat'],
            (r.get('dim') or '').replace('|', '／')[:76]))
    M += ['', '## 为什么这些不单独成文', '',
          '- **评测方法/度量**：提出的是评价方式（如干预式协议、形式化验证、行为级指标），'
          '本身不附带任务集，无法作为「基准」被他人直接复用。',
          '- **攻防工作**：主体是攻击或防御方法，评测协议虽可复用但服务于单一方法，覆盖面有限。',
          '- **综述**：不含实验基准。', '',
          '> 若需要把其中某个协议提升为独立基准文档，在 `scripts/bench_registry.py` 里加一条正则即可。', '']
    open(os.path.join(outdir, '0__评测方法与协议汇总.md'), 'w', encoding='utf-8').write('\n'.join(M))
    print('catch-all doc covers:', len(left))

write_comparison_outputs(cards)

print('docs written:', sum(len(v) for v in index.values()))
for t in ORDER:
    if t in index:
        print(' ', t, len(index[t]))
