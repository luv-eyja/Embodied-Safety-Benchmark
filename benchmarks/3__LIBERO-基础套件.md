# LIBERO（基础套件）

> **所属环节**：认知 + 动作控制（终身学习）  
> **分类**：VLA 能力  
> **关联论文**：本表 30 篇（提出者 2 篇，使用者 28 篇）
> **证据级别**：A（人工扩写字段 + 表内摘要；未逐篇精读全文）

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO? |
| 年份 | 2023、2025、2026 |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | VLA 领域事实标准：π0/π0.5、OpenVLA、OpenVLA-OFT、GR00T N1/N1.5、Octo、SmolVLA、DTP、RoboMamba 等，几乎所有论文都以 LIBERO 平均成功率作为主指标。 |
| 关注属性 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | 参数规模—成功率曲线；架构/训练/推理因素消融 |
| 基础平台线索 | LIBERO、RoboTwin、SimplerEnv、ManiSkill |
| 规模线索 | 130 任务；1648 个偏移任务实例；1648 个经六轮校验的偏移任务实例；39390 条轨迹；11 条硬件扰动轴 × 5 个严重度 = 210 种条件；500 回合；7 的动作生成模块残差流做受控机制可解释性研究：系统性破坏输入样本；4 个任务套件、3 个 VLA、7 种扰动条件 |
| 执行环境线索 | 摘要同时提到仿真与真机/实体机器人。 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：测「知识迁移」与「终身学习」：同一策略在任务序列上顺序学习后，能否保持旧技能并迁移到新任务。

**主要测量维度**：参数规模—成功率曲线；架构/训练/推理因素消融。

## 2. 怎么构建的

### 2.1 构建要素

| 要素 | 摘要级记录 |
|---|---|
| 基础平台 | LIBERO、RoboTwin、SimplerEnv、ManiSkill |
| 任务/场景规模 | 130 任务；1648 个偏移任务实例；1648 个经六轮校验的偏移任务实例；39390 条轨迹；11 条硬件扰动轴 × 5 个严重度 = 210 种条件；500 回合；7 的动作生成模块残差流做受控机制可解释性研究：系统性破坏输入样本；4 个任务套件、3 个 VLA、7 种扰动条件 |
| 扰动、风险或约束 | 参数规模—成功率曲线；架构/训练/推理因素消融 |
| 对照/配对方式 | 摘要提到配对、孪生或受控对照。 |
| 指标与判分线索 | 参数规模—成功率曲线；架构/训练/推理因素消融 |
| 执行设置 | 摘要同时提到仿真与真机/实体机器人。 |

### 2.2 详细说明

4 个任务套件共 **130 个语言条件操作任务**：LIBERO-Spatial（空间关系）、LIBERO-Object（物体）、LIBERO-Goal（目标）、LIBERO-Long（长时程）。每套件配 50 条人类遥操作示范，并有预训练/顺序微调的标准协议。

## 3. 用这个基准测了什么

**被测对象**：VLA 领域事实标准：π0/π0.5、OpenVLA、OpenVLA-OFT、GR00T N1/N1.5、Octo、SmolVLA、DTP、RoboMamba 等，几乎所有论文都以 LIBERO 平均成功率作为主指标。

**结果应如何读取**：先按“评测维度/指标”字段区分主指标、辅助指标和对照条件；若论文同时报告任务成功与安全/鲁棒性结果，应将二者分开阅读。

下表按论文列出；“摘要级发现”保留调研表中的概要，不等同于全文实验结论。

| 论文 | 年份 / 来源 | 角色 | 被测对象 | 使用方式 / 指标 | 摘要级发现 |
|---|---|---|---|---|---|
| [LIBERO-Pro2.0：具身基础模型鲁棒性基准](https://arxiv.org/abs/2610.24587) | 2026 / arXiv 预印本 (arXiv:2610.24587) | 使用 | 具身基础模型 / VLA | 6 维度 22 种静态扰动 + 20 种运行时干预，1648 个偏移任务实例 | 针对「LIBERO 高分不等于鲁棒」的问题，按条件、环境、观测、执行、机器人状态配置、语言六个维度构建 22 种静态扰动与 20 种运行时干预，生成 1648 个经六轮校验的偏移任务实例，并采集 39390 条轨迹支持面向鲁棒性的训练与评测。 |
| [LIBERO-RIG：硬件部署配置鲁棒性基准](https://arxiv.org/abs/2610.18843) | 2026 / arXiv 预印本 (arXiv:2610.18843) | 使用 | VLA 模型（9 个近期模型） | 11 条硬件扰动轴 × 5 个严重度 = 210 种条件；每条件 500 回合 | 只扰动机器人自身硬件与部署配置（相机安装与光学、相机-机械臂标定、驱动增益、控制频率、本体感觉噪声、基座位姿、桌面高度、夹爪垫磨损等），完全固定 LIBERO 任务本身，从而把「任务分布偏移」与「硬件配置偏移」解耦。9 个 VLA 的汇总成功率在中等严重度降至 0.767、最高严重度降至 0. |
| [LIBERO-RECOVER：失败恢复能力基准](https://arxiv.org/abs/2609.05178) | 2026 / arXiv 预印本 (arXiv:2609.05178) | 使用 | VLA 与世界动作模型 | 失败识别与恢复成功率（相对纯任务成功率） | 指出 LIBERO 上已接近 100% 的成功率具有误导性：真实交互中必然出现抓取失败、碰撞与物体意外移动，机器人不仅要完成任务还要能识别并从中恢复，而这一能力此前基本未被度量。该基准在既有成功率之外补充失败恢复能力的评测，弥合基准成绩与真实可靠性之间的差距。 |
| [Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准](https://arxiv.org/abs/2608.26578) | 2026 / arXiv 预印本 (arXiv:2608.26578) | 使用 | VLA 模型 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 | 提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。 |
| [ManiPhysicsBench：物体保全的物理评测](https://arxiv.org/abs/2610.02802) | 2026 / arXiv 预印本 (arXiv:2610.02802) | 使用 | 公开 VLA 检查点 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 | 指出刚体基准中的任务成功并不能说明模型是否保全了物体。 |
| [IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测](https://arxiv.org/abs/2609.25562) | 2026 / arXiv 预印本 (arXiv:2609.25562) | 使用 | 6 个已发布的 VLA 与世界动作模型（WAM） | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 | VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。 |
| [复述共识不等于自一致性：VLA 的指令依赖与鲁棒性](https://arxiv.org/abs/2610.19438) | 2026 / arXiv 预印本 (arXiv:2610.19438) | 使用 | OpenVLA 等 VLA 策略 | 指令改写下的成功率；错误指令探针；复述共识与置信度选择 | 揭示 LIBERO 微调与评测使用同十条指令串所带来的评测偏差：改写指令会使基座 OpenVLA 成功率下降 38.0 个点，测试期 prompt 集成无法恢复；取 K 条复述中位动作的「复述共识」在训练指令属于其中之一时反而再降 16.8 点，说明聚合只降低方差、去不掉复述共享的偏差。 |
| [VLA 真的理解指令吗：语言接地的机制可解释性研究](https://arxiv.org/abs/2610.10178) | 2026 / arXiv 预印本 (arXiv:2610.10178) | 使用 | π0.5、GR00T N1.7 | 激活/归因修补（activation & attribution patching）；残差流干预 | 在 VLA 缺乏显式接地模块、依赖视觉-语言主干固有能力的背景下，对 π0.5 与 GR00T N1.7 的动作生成模块残差流做受控机制可解释性研究：系统性破坏输入样本的任务指令，用激活与归因修补判断动作生成在多大程度上真正依赖语言，而非仅依赖视觉线索与表层相关性。 |
| [只有成功率够吗：扰动下 VLA 的行为鲁棒性度量](https://arxiv.org/abs/2610.01351) | 2026 / arXiv 预印本 (arXiv:2610.01351) | 使用 | 3 个 SOTA VLA；LIBERO / LIBERO-Plus | 行为指标：运动平滑度、效率、夹爪行为及其变异性 | 指出鲁棒性仍主要用任务成功率（TSR）衡量。该工作提出与基准无关的行为鲁棒性评测框架，刻画成功轨迹在扰动下「如何被执行」，包括运动平滑度、效率与夹爪行为等指标； |
| [VLA-Scope：偏移感知的失败预测](https://arxiv.org/abs/2609.21246) | 2026 / arXiv 预印本 (arXiv:2609.21246) | 使用 | OpenVLA（10 个 LIBERO 设置） | OOD 检测 + 偏移类别分类 + 执行进度；失败风险预测 | 指出 VLA 在分布外条件下仍可能成功，因此单靠 OOD 检测不足以预测执行失败。框架分两阶段：先用图像与语言的池化表示检测 OOD 输入并判定偏移类别，再对被标记为 OOD 的输入结合偏移类别、动作前缀特征与执行进度，用跨偏移共享的逻辑回归随执行过程更新失败风险。 |
| [MINERVA：LIBERO 的任务容量下限](https://arxiv.org/abs/2609.03715) | 2026 / arXiv 预印本 (arXiv:2609.03715) | **提出** | 刻意精简的视觉运动策略 vs 十亿参数 VLA | 参数规模—成功率曲线；架构/训练/推理因素消融 | 用一个刻意精简的策略族测量 LIBERO 实际需要的模型容量：0.54M 参数策略在 4 个标准套件、2000 次 rollout 上取得 95.1% 平均成功率，仅比报告中的 LeRobot π0.5 低 2.4 个点（参数少 7700 倍），性能约在 1M 参数处饱和、低于 0.25M 崩溃。 |
| [语言扰动下的持续模仿学习任务保持基准](https://arxiv.org/abs/2610.00542) | 2026 / arXiv 预印本 (arXiv:2610.00542) | 使用 | 持续模仿学习策略（LIBERO-Goal） | 保义/变义指令变体；任务能力与语言敏感性分离 | 指出持续模仿学习通常只考察「不遗忘」，但保持任务表现并不保证行为仍受语言接地——策略可能依赖场景线索、物体关联或记忆中的任务结构。 |
| [SilentDrift：利用动作分块的隐蔽后门攻击](https://arxiv.org/abs/2601.14323) | 2026 / arXiv 预印本 (arXiv:2601.14323) | 使用 | VLA 模型（黑盒后门） | 攻击隐蔽性（运动学连续性）、攻击成功率 | 指出现代 VLA 中「动作分块 + 增量位姿表示」共同造成块内视觉开环：机器人必须执行 K 步动作序列，逐步扰动可随积分累积。据此提出黑盒隐蔽后门攻击 SilentDrift，用 Smootherstep 构造具备 C² 连续性的扰动，保证轨迹边界处速度与加速度为零以满足严格运动学一致性约束； |
| [DropVLA：动作级后门攻击](https://arxiv.org/abs/2510.10932) | 2025 / arXiv 预印本 (arXiv:2510.10932) | 使用 | OpenVLA-7B（LIBERO 评测） | 指定动作原语的触发成功率；名义任务性能保持 | 指出现有 VLA 后门研究主要关注无目标攻击或任务级劫持，对单个动作的细粒度控制尚属空白。方法在「流水线黑盒、仅有限数据投毒」的现实设定下，用窗口一致的重标注方案做分块微调，强制某个可复用动作原语（如开夹爪）在攻击者指定的决策点执行； |
| [EDPA：模型无关的 VLA 对抗补丁攻击与防御](https://arxiv.org/abs/2510.13237) | 2025 / arXiv 预印本 (arXiv:2510.13237) | 使用 | 多种 VLA 模型（无需架构先验） | 补丁攻击成功率；跨模型/跨机械臂迁移性 | 提出嵌入破坏补丁攻击 EDPA：无需知道模型架构或被控机械臂即可生成可直接置于相机视野中的对抗补丁，其构造依据是破坏视觉-文本潜表示之间的语义对齐、并最大化潜表示的差异；同时给出相应的防御策略。该工作为「VLA 攻击的可迁移性与可复现评测」提供了基线。 |
| [Altered Thoughts：推理型 VLA 的思维链脆弱性探针](https://arxiv.org/abs/2603.12717) | 2026 / arXiv 预印本 (arXiv:2603.12717) | 使用 | 采用思维链（CoT）推理的 SOTA VLA；40 个 LIBERO 桌面任务 | 7 类文本腐蚀 × 3 个攻击者层级；仅改推理轨迹、输入不动 | 指出推理型 VLA 在动作解码前会生成一段自然语言计划，这条「推理模块→动作解码器」的内部文本通道此前从未被对抗审视。 |
| [预训练 VLA 联邦微调的实证研究与开放测试床](https://arxiv.org/abs/2609.22973) | 2026 / arXiv 预印本 (arXiv:2609.22973) | 使用 | 3 个现代预训练 VLA 策略 | LIBERO 40 个仿真任务 + 两处真机 6 个任务；2/3 站点分布式示范 | 把预训练 VLA 适配到新机器人、新环境或新任务需要本地采集示范，而这些数据常被丢弃。 |
| [动作 tokenizer 究竟该按什么评：重建之外的可预测性与鲁棒性](https://arxiv.org/abs/2610.09170) | 2026 / arXiv 预印本 (arXiv:2610.09170) | 使用 | 自回归动作 token 策略（含 VLA）与其动作 tokenizer | token 可预测性、未见 token 的解码合理性、下游策略成功率 | 通过大量分析指出：动作重建足够精确只是下游策略成功的必要条件——策略还必须能为新观测预测出正确的 token，且未见过的 token 预测仍要解码成合理动作；这些性质位于 tokenizer 训练的下游，不被重建目标直接激励。 |
| [Memorize / Adapt / Ignore：训练数据变化如何生效的机制诊断](https://arxiv.org/abs/2609.38401) | 2026 / arXiv 预印本 (arXiv:2609.38401) | 使用 | ManiSkill 拾放 RL 策略与 LIBERO / RoboTwin 上微调的 VLA | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） | 训练数据变化（仿真中的域随机化方案、模仿学习中的示范筛选）是提升操作策略鲁棒性的主要手段，但其机制不清楚，实践中只能靠昂贵的试错调随机化参数。 |
| [不是所有层都要调：VLA 适配的区域诊断](https://arxiv.org/abs/2609.18084) | 2026 / arXiv 预印本 (arXiv:2609.18084) | 使用 | 5 个架构各异的 VLA（OpenVLA-OFT、π0、SmolVLA、DTP、Octo；93M–7B） | 区域隔离微调的归一化参数位移（适配代价谱） | 检验「每个网络区域都需要同等适配」这一隐含假设：用区域隔离微调下的归一化参数位移度量各区适配代价，在 5 个架构各异的 VLA 上发现一致的适配谱——外观偏移的代价集中在视觉编码器、指令偏移在语言主干、新物体偏移同时落在视觉编码器与动作头。 |
| [Rephrase Before You Act：VLA 的语言敏感性刻画与缓解](https://arxiv.org/abs/2610.10526) | 2026 / arXiv 预印本 (arXiv:2610.10526) | 使用 | π0.5、π0 等 VLA | 单次编辑引起的成功率波动、oracle 短语搜索、ID/OOD 差距归因 | 刻画 VLA 对指令措辞的惊人敏感性：π0.5 对 "switch on the stove" 有 100% 成功率、换成 "switch on the hot plate" 只有 2%；即使用改写增广微调过的 π0 检查点，波动仍可达 61 个点。 |
| [什么让 VLA 更高效：动作头、规模与延迟的受控评测](https://arxiv.org/abs/2609.13984) | 2026 / arXiv 预印本 (arXiv:2609.13984) | 使用 | 固定主干（SigLIP2 / Qwen2.5）下的 VLA 配置网格 | 动作头设计 × 模块规模，每种配置配实测端侧延迟 | 在固定主干与训练流水线、并把每种配置与实测端侧延迟配对的前提下扫描动作头设计与模块规模，得到三点结论：动作头性能主要由初始化决定（把语言主干最后几层 transformer 复制进头部是收益最大的单一杠杆，且不增加延迟），而非解码器架构、损失函数或推理预算； |
| [VLA 是理解物体还是重放动作：物理属性的表示探针](https://arxiv.org/abs/2610.06078) | 2026 / arXiv 预印本 (arXiv:2610.06078) | 使用 | 7 个 VLA 及其基座 VLM | 线性探针 + 表示相似性分析（RSA）；物理 vs 非物理属性可解码性 | 追问 VLA 的泛化到底源于对物体物理属性的整体理解（从而能适应未见布局），还是仅仅重放恰好奏效的已学动作——前者是真泛化，后者是偶然鲁棒。 |
| [GoBA：以物理物体为触发器的目标导向后门](https://arxiv.org/abs/2510.09269) | 2025 / arXiv 预印本 (arXiv:2510.09269) | 使用 | VLA 模型（基于主流 VLA 基准） | 触发器为真实物体；目标导向动作执行率、干净性能保持 | 揭示一种更现实的威胁：攻击者只需把物理物体作为触发器注入训练数据。GoBA 让 VLA 在无触发器时表现正常、在触发器出现时执行预设的目标导向动作（而不只是让任务失败），比既有假设白盒访问、仅导致任务失败的后门更接近真实攻击面。 |
| [VLA-Fool：跨模态失配下的多模态对抗攻击](https://arxiv.org/abs/2511.16203) | 2025 / arXiv 预印本 (arXiv:2511.16203) | 使用 | VLA 模型（白盒与黑盒） | 文本/视觉/跨模态三层攻击；跨模态对齐破坏 | 指出 VLA 的对抗鲁棒性在真实的多模态与黑盒条件下仍未被充分研究，既有工作只看单模态扰动，忽略了从根本上影响具身推理与决策的跨模态失配。VLA-Fool 统一了三个层次的多模态对抗攻击（文本扰动等），在白盒与黑盒设定下系统评测，构成一份较完整的 VLA 多模态鲁棒性评估。 |
| [Detect and Suppress：对抗补丁的机制性防御](https://arxiv.org/abs/2610.03498) | 2026 / arXiv 预印本 (arXiv:2610.03498) | 使用 | VLA 模型（LIBERO-10 评测） | SAE 特征与补丁的相关性；条件抑制后的成功率 | 针对「对抗补丁通过操纵视觉观测导致 VLA 控制失败，但其内部机制与可干预点不清楚」的问题，用稀疏自编码器（SAE）机制性分析 VLA 表示，找到一个激活与对抗补丁存在强相关的特征；在线性探针检测到攻击时，仅在推理期抑制该特征。 |
| [TAPDreamer：面向世界动作模型的可迁移对抗补丁](https://arxiv.org/abs/2610.06814) | 2026 / arXiv 预印本 (arXiv:2610.06814) | 使用 | 世界动作模型（WAM） | 仅用公开编码器、无需查询目标策略；跨任务与跨动作架构迁移 | 世界动作模型依赖相机输入，而相机输入被操纵会污染跨任务、跨动作策略共享的视觉表示。既有攻击需要访问目标模型的输出或预测未来，TAPDreamer 只用公开编码器构造一个固定的局部扰动即可跨任务与动作架构迁移、且无需任何目标策略查询； |
| [LIBERO：终身机器人学习与知识迁移基准](https://arxiv.org/abs/2306.03310) | 2023 / NeurIPS 2023（神经信息处理系统大会，Dat… | **提出** | 语言条件操作策略 / 终身学习智能体 | 4 个任务套件（130 个任务）；知识迁移与终身学习指标 | VLA 领域使用最广的能力评测平台：把语言条件操作任务分为 LIBERO-Spatial、Object、Goal、Long 四个套件共 130 个任务，重点是「知识迁移」与「终身学习」——同一策略在任务序列上顺序学习后能否保持并迁移。 |
| [SafeVLA-Bench：VLA 的「成功-安全」落差基准](https://arxiv.org/abs/2606.00773) | 2026 / arXiv 预印本 (arXiv:2606.00773) | 使用 | 现有仿真 VLA 基准（事后安全评估） | 信号时序逻辑（STL）不变式 + 定量鲁棒性；安全率、成功但不安全率 | 指出二元成功率会掩盖轨迹上的安全违规：策略可能到达目标，却施加过度接触、扰动旁观物体、使手中物体失稳或进入机器人自碰撞。SafeVLA-Bench 是一个「事后」安全评估框架，可直接套在现有基于仿真的 VLA 基准上，把任务相关的安全要求编码为信号时序逻辑（STL）不变式并给出定量鲁棒性语义； |
| [dWorldEval：离散扩散世界模型驱动的可扩展策略评测](https://arxiv.org/abs/2604.22152) | 2026 / arXiv 预印本 (arXiv:2604.22152) | 使用 | 机器人策略（大规模跨环境跨任务） | 离散扩散世界模型；视觉/语言/动作统一 token 空间 | 指出在数千个环境、数千个任务上评测机器人策略用现有方法不可行，因此需要新的可扩展评测方法论。 |

## 4. 关键结论、改进方向与可复用性

**关键结论**：作为**能力底座**极其成功（任务干净、协议统一、复现性好），但也因此成为**饱和基准**：SOTA 已接近 100%，区分度下降；且它只测「做得成」，不测鲁棒性、安全性或失败恢复——本调研中的大量工作正是围绕这些缺口展开（LIBERO-Plus/Pro2.0/RIG/VPro/MAX/RECOVER/CTRL/X/Para、SafeLIBERO、Trap-LIBERO）。

**论文提到的改进方向**：①在 LIBERO 之上补充分布偏移、硬件扰动、过程安全与失败恢复维度；②报告需说明微调与评测是否共用同一指令集（否则虚高）；③容量下限研究（MINERVA）提示该基准的任务容量已接近饱和，需更难的任务集。

**复用状态**：已有至少一篇后续论文使用，具备初步跨论文证据。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models](https://arxiv.org/abs/2610.24587)（2026，arXiv 预印本 (arXiv:2610.24587)）
- [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843)（2026，arXiv 预印本 (arXiv:2610.18843)）
- [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178)（2026，arXiv 预印本 (arXiv:2609.05178)）
- [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2026，arXiv 预印本 (arXiv:2608.26578)）
- [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)（2026，arXiv 预印本 (arXiv:2610.02802)）
- [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)（2026，arXiv 预印本 (arXiv:2609.25562)）
- [Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies](https://arxiv.org/abs/2610.19438)（2026，arXiv 预印本 (arXiv:2610.19438)）
- [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](https://arxiv.org/abs/2610.10178)（2026，arXiv 预印本 (arXiv:2610.10178)）
- [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351)（2026，arXiv 预印本 (arXiv:2610.01351)）
- [VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models](https://arxiv.org/abs/2609.21246)（2026，arXiv 预印本 (arXiv:2609.21246)）
- [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715)（2026，arXiv 预印本 (arXiv:2609.03715)）  ← **提出**
- [Does Continual Imitation Learning Remain Grounded? A Language-Perturbed Benchmark for Robotic Task Retention](https://arxiv.org/abs/2610.00542)（2026，arXiv 预印本 (arXiv:2610.00542)）
- [SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2601.14323)（2026，arXiv 预印本 (arXiv:2601.14323)）
- [DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models](https://arxiv.org/abs/2510.10932)（2025，arXiv 预印本 (arXiv:2510.10932)）
- [Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models](https://arxiv.org/abs/2510.13237)（2025，arXiv 预印本 (arXiv:2510.13237)）
- [Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation](https://arxiv.org/abs/2603.12717)（2026，arXiv 预印本 (arXiv:2603.12717)）
- [An Empirical Study and Open Testbed for Federated Fine-Tuning of Vision-Language-Action Models](https://arxiv.org/abs/2609.22973)（2026，arXiv 预印本 (arXiv:2609.22973)）
- [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170)（2026，arXiv 预印本 (arXiv:2610.09170)）
- [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)（2026，arXiv 预印本 (arXiv:2609.38401)）
- [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2609.18084)（2026，arXiv 预印本 (arXiv:2609.18084)）
- [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2610.10526)（2026，arXiv 预印本 (arXiv:2610.10526)）
- [What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency](https://arxiv.org/abs/2609.13984)（2026，arXiv 预印本 (arXiv:2609.13984)）
- [Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?](https://arxiv.org/abs/2610.06078)（2026，arXiv 预印本 (arXiv:2610.06078)）
- [Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects](https://arxiv.org/abs/2510.09269)（2025，arXiv 预印本 (arXiv:2510.09269)）
- [When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2511.16203)（2025，arXiv 预印本 (arXiv:2511.16203)）
- [Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models](https://arxiv.org/abs/2610.03498)（2026，arXiv 预印本 (arXiv:2610.03498)）
- [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)（2026，arXiv 预印本 (arXiv:2610.06814)）
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)（2023，NeurIPS 2023（神经信息处理系统大会，Datasets & Bench）  ← **提出**
- [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773)（2026，arXiv 预印本 (arXiv:2606.00773)）
- [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152)（2026，arXiv 预印本 (arXiv:2604.22152)）

## 6. 证据边界与复核建议

- **证据级别**：A（人工扩写字段 + 表内摘要；未逐篇精读全文）。
- **主要来源**：[MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715)。
- **当前限制**：本文档基于调研表、论文摘要和少量人工整理；核心条目另有本地全文核查补录，但仍未替代对全文实验表格、附录、代码仓库和数据下载说明的逐项复核。
- **建议复核**：优先确认任务/场景划分、样本规模、指标公式、判分阈值、模型清单，以及仿真与真机设置是否一致。

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成。 A 级文档含人工扩写字段；核心条目附本地全文核查补录；B/C 级文档主要依赖摘要级结构化记录。*
