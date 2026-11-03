# LIBERO（基础套件）

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：主要贡献是终身学习任务与迁移评价。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：认知 + 动作控制（终身学习）  
> **分类**：VLA 能力  
> **关联论文**：本表 30 篇（提出 1、使用 29；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://libero-project.github.io/main.html](https://libero-project.github.io/main.html)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning |
| 年份 | 2023（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 终身机器人学习基础基准 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | 从活动语言提取任务模板，以 BDDL 表达对象、初态和目标，在 robosuite／MuJoCo 中执行；比较不同任务顺序、预训练、架构和终身学习方法。 |
| 基础平台线索 | LIBERO、RoboTwin、SimplerEnv、ManiSkill |
| 规模线索 | 原版 130 任务：Spatial 10、Object 10、Goal 10 与 LIBERO-100；后者可拆为 90 个预训练和 10 个长任务。空间、物体和目标变化分别控制。 |
| 执行环境线索 | 终身机器人学习基础基准 |
| OpenAlex 引用快照 | [136](https://openalex.org/W7133220882)；2026-11-03 |
| 来源审计 | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)；same_paper_in_registry |
| 来源核验依据 | 2026-11-03 复核原始论文标题与方法章节：§3–4；原始论文，不以 MINERVA 代替 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：机器人能否跨任务迁移知识，在学习新技能时减少旧技能遗忘？

**评测层级**：终身机器人学习基础基准。

## 2. 怎么构建的

**核心场景与条目**：原版 130 任务：Spatial 10、Object 10、Goal 10 与 LIBERO-100；后者可拆为 90 个预训练和 10 个长任务。空间、物体和目标变化分别控制。

**实现与判分**：从活动语言提取任务模板，以 BDDL 表达对象、初态和目标，在 robosuite／MuJoCo 中执行；比较不同任务顺序、预训练、架构和终身学习方法。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models](https://arxiv.org/abs/2610.24587) | 2026 | 使用 | 6 维度 22 种静态扰动 + 20 种运行时干预，1648 个偏移任务实例 | 针对「LIBERO 高分不等于鲁棒」的问题，按条件、环境、观测、执行、机器人状态配置、语言六个维度构建 22 种静态扰动与 20 种运行时干预，生成 1648 个经六轮校验的偏移任务实例，并采集 39390 条轨迹支持面向鲁棒性的训练与评测。 |
| [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843) | 2026 | 使用 | 11 条硬件扰动轴 × 5 个严重度 = 210 种条件；每条件 500 回合 | 只扰动机器人自身硬件与部署配置（相机安装与光学、相机-机械臂标定、驱动增益、控制频率、本体感觉噪声、基座位姿、桌面高度、夹爪垫磨损等），完全固定 LIBERO 任务本身，从而把「任务分布偏移」与「硬件配置偏移」解耦。9 个 VLA 的汇总成功率在中等严重度降至 0.767、最高严重度降至 0.509，并配有统计检验。 |
| [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178) | 2026 | 使用 | 失败识别与恢复成功率（相对纯任务成功率） | 指出 LIBERO 上已接近 100% 的成功率具有误导性：真实交互中必然出现抓取失败、碰撞与物体意外移动，机器人不仅要完成任务还要能识别并从中恢复，而这一能力此前基本未被度量。该基准在既有成功率之外补充失败恢复能力的评测，弥合基准成绩与真实可靠性之间的差距。 |
| [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578) | 2026 | 使用 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 | 提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。 |
| [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802) | 2026 | 使用 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 | 指出刚体基准中的任务成功并不能说明模型是否保全了物体。ManiPhysicsZoo 汇总文献支撑的材质属性、3D 网格与参考文献形成可复用物体资产，再由基于求解器的评估依据几何、材质与抓取条件计算损伤阈值并与实测接触力比较，从而在 LIBERO 与 SimplerEnv 上区分「完成任务」与「安全完成任务」，公开 VLA 检查点在两者间存在显著差距。 |
| [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562) | 2026 | 使用 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 | VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。该基准在统一上报口径下对 6 个已发布系统分轴评测：LIBERO 上的干净能力、LIBERO-Plus 上的非语言鲁棒性、LIBERO-Para 上的指令敏感度以及实测执行代价，并聚合三个不同随机种子的完整评测。 |
| [Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies](https://arxiv.org/abs/2610.19438) | 2026 | 使用 | 指令改写下的成功率；错误指令探针；复述共识与置信度选择 | 揭示 LIBERO 微调与评测使用同十条指令串所带来的评测偏差：改写指令会使基座 OpenVLA 成功率下降 38.0 个点，测试期 prompt 集成无法恢复；取 K 条复述中位动作的「复述共识」在训练指令属于其中之一时反而再降 16.8 点，说明聚合只降低方差、去不掉复述共享的偏差。并提出错误指令探针度量策略对指令的依赖程度。 |
| [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](https://arxiv.org/abs/2610.10178) | 2026 | 使用 | 激活/归因修补（activation & attribution patching）；残差流干预 | 在 VLA 缺乏显式接地模块、依赖视觉-语言主干固有能力的背景下，对 π0.5 与 GR00T N1.7 的动作生成模块残差流做受控机制可解释性研究：系统性破坏输入样本的任务指令，用激活与归因修补判断动作生成在多大程度上真正依赖语言，而非仅依赖视觉线索与表层相关性。 |
| [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351) | 2026 | 使用 | 行为指标：运动平滑度、效率、夹爪行为及其变异性 | 指出鲁棒性仍主要用任务成功率（TSR）衡量。该工作提出与基准无关的行为鲁棒性评测框架，刻画成功轨迹在扰动下「如何被执行」，包括运动平滑度、效率与夹爪行为等指标；在 LIBERO/LIBERO-Plus 的 4 个任务套件、3 个 VLA、7 种扰动条件下评测，发现扰动会改变成功行为的典型模式与其变异性。 |
| [VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2609.21246) | 2026 | 使用 | OOD 检测 + 偏移类别分类 + 执行进度；失败风险预测 | 指出 VLA 在分布外条件下仍可能成功，因此单靠 OOD 检测不足以预测执行失败。框架分两阶段：先用图像与语言的池化表示检测 OOD 输入并判定偏移类别，再对被标记为 OOD 的输入结合偏移类别、动作前缀特征与执行进度，用跨偏移共享的逻辑回归随执行过程更新失败风险。 |
| [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715) | 2026 | 使用 | 参数规模—成功率曲线；架构/训练/推理因素消融 | 用一个刻意精简的策略族测量 LIBERO 实际需要的模型容量：0.54M 参数策略在 4 个标准套件、2000 次 rollout 上取得 95.1% 平均成功率，仅比报告中的 LeRobot π0.5 低 2.4 个点（参数少 7700 倍），性能约在 1M 参数处饱和、低于 0.25M 崩溃。这一结果对「LIBERO 是否仍是有效的能力基准」提出了直接质疑。 |
| [Does Continual Imitation Learning Remain Grounded? A Language-Perturbed Benchmark for Robotic Task Retention](https://arxiv.org/abs/2610.00542) | 2026 | 使用 | 保义/变义指令变体；任务能力与语言敏感性分离 | 指出持续模仿学习通常只考察「不遗忘」，但保持任务表现并不保证行为仍受语言接地——策略可能依赖场景线索、物体关联或记忆中的任务结构。该基准为 LIBERO 的 Goal、Spatial、Object、Long 套件构造保义与变义指令变体，在每一持续学习阶段后用 Original 与 Paraphrase 指令评测，把任务胜任度与语言敏感性分开，作为标准学习指标的补充诊断。 |
| [SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323) | 2026 | 使用 | 攻击隐蔽性（运动学连续性）、攻击成功率 | 指出现代 VLA 中「动作分块 + 增量位姿表示」共同造成块内视觉开环：机器人必须执行 K 步动作序列，逐步扰动可随积分累积。据此提出黑盒隐蔽后门攻击 SilentDrift，用 Smootherstep 构造具备 C² 连续性的扰动，保证轨迹边界处速度与加速度为零以满足严格运动学一致性约束；并通过关键帧攻击策略只污染关键的接近阶段以提升隐蔽性。 |
| [DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932) | 2025 | 使用 | 指定动作原语的触发成功率；名义任务性能保持 | 指出现有 VLA 后门研究主要关注无目标攻击或任务级劫持，对单个动作的细粒度控制尚属空白。方法在「流水线黑盒、仅有限数据投毒」的现实设定下，用窗口一致的重标注方案做分块微调，强制某个可复用动作原语（如开夹爪）在攻击者指定的决策点执行；在 OpenVLA-7B 与 LIBERO 上，仅视觉投毒即达到 98.67%–99.83% 的攻击成功率。 |
| [Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237) | 2025 | 使用 | 补丁攻击成功率；跨模型/跨机械臂迁移性 | 提出嵌入破坏补丁攻击 EDPA：无需知道模型架构或被控机械臂即可生成可直接置于相机视野中的对抗补丁，其构造依据是破坏视觉-文本潜表示之间的语义对齐、并最大化潜表示的差异；同时给出相应的防御策略。该工作为「VLA 攻击的可迁移性与可复现评测」提供了基线。 |
| [Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation](https://arxiv.org/abs/2603.12717) | 2026 | 使用 | 7 类文本腐蚀 × 3 个攻击者层级；仅改推理轨迹、输入不动 | 指出推理型 VLA 在动作解码前会生成一段自然语言计划，这条「推理模块→动作解码器」的内部文本通道此前从未被对抗审视。作者设计 7 类文本腐蚀（盲噪声、机械语义、LLM 自适应三个攻击者层级），在 40 个 LIBERO 任务上检验「只污染推理轨迹、所有输入保持不变」能否降低物理任务成功率，并揭示出显著的不对称性（替换物体名等改动的影响远大于其他腐蚀）。 |
| [An Empirical Study and Open Testbed for Federated Fine-Tuning of Vision-Language-Action Models](https://arxiv.org/abs/2609.22973) | 2026 | 使用 | LIBERO 40 个仿真任务 + 两处真机 6 个任务；2/3 站点分布式示范 | 把预训练 VLA 适配到新机器人、新环境或新任务需要本地采集示范，而这些数据常被丢弃。作者系统研究三个现代预训练 VLA 的联邦微调（LIBERO 40 个仿真任务，以及两处真机实验共 6 个任务，示范分别来自 2 个与 3 个站点），并针对「缺乏可复现基准与可复用训练框架、结果难以比较」的问题开放测试床。 |
| [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170) | 2026 | 使用 | token 可预测性、未见 token 的解码合理性、下游策略成功率 | 通过大量分析指出：动作重建足够精确只是下游策略成功的必要条件——策略还必须能为新观测预测出正确的 token，且未见过的 token 预测仍要解码成合理动作；这些性质位于 tokenizer 训练的下游，不被重建目标直接激励。作者据此提出同时衡量可预测性与鲁棒解码的动作 tokenizer 设计（PACT）。 |
| [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401) | 2026 | 使用 | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） | 训练数据变化（仿真中的域随机化方案、模仿学习中的示范筛选）是提升操作策略鲁棒性的主要手段，但其机制不清楚，实践中只能靠昂贵的试错调随机化参数。作者以物体尺寸、颜色、类型以及场景光照与语言提示为变量，跨 ManiSkill 与 LIBERO/RoboTwin 做系列案例研究，同时考察模型行为与内部表示，并以经验神经正切核（NTK）为主要分析工具。 |
| [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2609.18084) | 2026 | 使用 | 区域隔离微调的归一化参数位移（适配代价谱） | 检验「每个网络区域都需要同等适配」这一隐含假设：用区域隔离微调下的归一化参数位移度量各区适配代价，在 5 个架构各异的 VLA 上发现一致的适配谱——外观偏移的代价集中在视觉编码器、指令偏移在语言主干、新物体偏移同时落在视觉编码器与动作头。据此提出「观察—诊断—分配—适配」流水线，把有限适配容量分配到真正需要的区域。 |
| [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2610.10526) | 2026 | 使用 | 单次编辑引起的成功率波动、oracle 短语搜索、ID/OOD 差距归因 | 刻画 VLA 对指令措辞的惊人敏感性：π0.5 对 "switch on the stove" 有 100% 成功率、换成 "switch on the hot plate" 只有 2%；即使用改写增广微调过的 π0 检查点，波动仍可达 61 个点。作者用经统计检验的单次编辑波动与 oracle 短语搜索量化该敏感性，发现仅靠措辞就几乎能填平 ID 与 OOD 之间 21 点的差距；因为敏感性是系统性的，可被表述为显式改写规则，从而在不修改策略的前提下缓解。 |
| [What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency](https://arxiv.org/abs/2609.13984) | 2026 | 使用 | 动作头设计 × 模块规模，每种配置配实测端侧延迟 | 在固定主干与训练流水线、并把每种配置与实测端侧延迟配对的前提下扫描动作头设计与模块规模，得到三点结论：动作头性能主要由初始化决定（把语言主干最后几层 transformer 复制进头部是收益最大的单一杠杆，且不增加延迟），而非解码器架构、损失函数或推理预算；对齐假设还能解释其余各轴（如流匹配的作用）。 |
| [Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?](https://arxiv.org/abs/2610.06078) | 2026 | 使用 | 线性探针 + 表示相似性分析（RSA）；物理 vs 非物理属性可解码性 | 追问 VLA 的泛化到底源于对物体物理属性的整体理解（从而能适应未见布局），还是仅仅重放恰好奏效的已学动作——前者是真泛化，后者是偶然鲁棒。对 7 个 VLA 的激活做线性探针与表示相似性分析，发现质量、易碎性、可变形性、摩擦、尺寸等物理属性在几乎每个模态流中都比语义类别、材质、声音、价格等非物理属性更难解码，且相对基座 VLM，机器人预训练反而削弱了这种可解码性。 |
| [Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269) | 2025 | 使用 | 触发器为真实物体；目标导向动作执行率、干净性能保持 | 揭示一种更现实的威胁：攻击者只需把物理物体作为触发器注入训练数据。GoBA 让 VLA 在无触发器时表现正常、在触发器出现时执行预设的目标导向动作（而不只是让任务失败），比既有假设白盒访问、仅导致任务失败的后门更接近真实攻击面。 |
| [When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203) | 2025 | 使用 | 文本/视觉/跨模态三层攻击；跨模态对齐破坏 | 指出 VLA 的对抗鲁棒性在真实的多模态与黑盒条件下仍未被充分研究，既有工作只看单模态扰动，忽略了从根本上影响具身推理与决策的跨模态失配。VLA-Fool 统一了三个层次的多模态对抗攻击（文本扰动等），在白盒与黑盒设定下系统评测，构成一份较完整的 VLA 多模态鲁棒性评估。 |
| [Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](https://arxiv.org/abs/2610.03498) | 2026 | 使用 | SAE 特征与补丁的相关性；条件抑制后的成功率 | 针对「对抗补丁通过操纵视觉观测导致 VLA 控制失败，但其内部机制与可干预点不清楚」的问题，用稀疏自编码器（SAE）机制性分析 VLA 表示，找到一个激活与对抗补丁存在强相关的特征；在线性探针检测到攻击时，仅在推理期抑制该特征。该干预无需微调即提升鲁棒性，在 LIBERO-10 上对补丁攻击的评测中提升了成功率。 |
| [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814) | 2026 | 使用 | 仅用公开编码器、无需查询目标策略；跨任务与跨动作架构迁移 | 世界动作模型依赖相机输入，而相机输入被操纵会污染跨任务、跨动作策略共享的视觉表示。既有攻击需要访问目标模型的输出或预测未来，TAPDreamer 只用公开编码器构造一个固定的局部扰动即可跨任务与动作架构迁移、且无需任何目标策略查询；其洞见是补丁引起的注意力权重与 value 向量交互会把影响广播到全局表示。 |
| [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | 2023 | 提出 | 4 个任务套件（130 个任务）；知识迁移与终身学习指标 | VLA 领域使用最广的能力评测平台：把语言条件操作任务分为 LIBERO-Spatial、Object、Goal、Long 四个套件共 130 个任务，重点是「知识迁移」与「终身学习」——同一策略在任务序列上顺序学习后能否保持并迁移。几乎所有 VLA 论文都以 LIBERO 平均成功率作为主指标，也因此成为后续大量鲁棒性/安全性基准（LIBERO-Plus、LIBERO-Pro、LIBERO-X、LIBERO-MAX 等）的底座。 |
| [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773) | 2026 | 使用 | 信号时序逻辑（STL）不变式 + 定量鲁棒性；安全率、成功但不安全率 | 指出二元成功率会掩盖轨迹上的安全违规：策略可能到达目标，却施加过度接触、扰动旁观物体、使手中物体失稳或进入机器人自碰撞。SafeVLA-Bench 是一个「事后」安全评估框架，可直接套在现有基于仿真的 VLA 基准上，把任务相关的安全要求编码为信号时序逻辑（STL）不变式并给出定量鲁棒性语义；除原生成功率外，还报告安全率与「成功但不安全」率。 |
| [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152) | 2026 | 使用 | 离散扩散世界模型；视觉/语言/动作统一 token 空间 | 指出在数千个环境、数千个任务上评测机器人策略用现有方法不可行，因此需要新的可扩展评测方法论。dWorldEval 用离散扩散世界模型作为可扩展的评测代理：把视觉、语言与机器人动作等所有模态映射到统一 token 空间，用单个基于 transformer 的去噪网络建模，从而以生成方式预测策略执行结果。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：原论文的关键指标是前向迁移 FWT、负向后向迁移 NBT 和成功曲线 AUC，展示新任务学习、旧任务保留之间的权衡；它后来成为大量 VLA 工作的基础环境。

**适用边界**：后来常见的 40 任务成功率评测只覆盖特定组合，不能替代原始 130 任务的终身学习目的。原始来源应为 2306.03310，不应引用 MINERVA 作为提出者。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models](https://arxiv.org/abs/2610.24587)（2026；使用）
- [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843)（2026；使用）
- [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178)（2026；使用）
- [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2026；使用）
- [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)（2026；使用）
- [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)（2026；使用）
- [Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies](https://arxiv.org/abs/2610.19438)（2026；使用）
- [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](https://arxiv.org/abs/2610.10178)（2026；使用）
- [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351)（2026；使用）
- [VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2609.21246)（2026；使用）
- [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715)（2026；使用）
- [Does Continual Imitation Learning Remain Grounded? A Language-Perturbed Benchmark for Robotic Task Retention](https://arxiv.org/abs/2610.00542)（2026；使用）
- [SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323)（2026；使用）
- [DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932)（2025；使用）
- [Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237)（2025；使用）
- [Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation](https://arxiv.org/abs/2603.12717)（2026；使用）
- [An Empirical Study and Open Testbed for Federated Fine-Tuning of Vision-Language-Action Models](https://arxiv.org/abs/2609.22973)（2026；使用）
- [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170)（2026；使用）
- [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)（2026；使用）
- [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2609.18084)（2026；使用）
- [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2610.10526)（2026；使用）
- [What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency](https://arxiv.org/abs/2609.13984)（2026；使用）
- [Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?](https://arxiv.org/abs/2610.06078)（2026；使用）
- [Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269)（2025；使用）
- [When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203)（2025；使用）
- [Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](https://arxiv.org/abs/2610.03498)（2026；使用）
- [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)（2026；使用）
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)（2023；提出）
- [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773)（2026；使用）
- [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

后来常见的 40 任务成功率评测只覆盖特定组合，不能替代原始 130 任务的终身学习目的。原始来源应为 2306.03310，不应引用 MINERVA 作为提出者。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Bo Liu, Yifeng Zhu, Chongkai Gao, et al., ‘LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning,’ arXiv preprint, 2023, arXiv:2306.03310v2. [论文](https://arxiv.org/abs/2306.03310)；[核查正文](https://arxiv.org/html/2306.03310v2)。

**重点核查位置（章节主题）**：Benchmark Construction；Task Suites；5.1 Evaluation Metrics；5 Experiments。

OpenAlex 被引次数：**[136](https://openalex.org/W7133220882)**；观测日期：2026-11-03。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://libero-project.github.io/main.html](https://libero-project.github.io/main.html)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 29 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
