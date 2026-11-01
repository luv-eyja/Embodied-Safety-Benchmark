# RoboTwin

> **所属环节**：动作控制（双臂协同）  
> **分类**：VLA 能力  
> **关联论文**：本表 8 篇（提出者 1 篇，使用者 7 篇）
> **证据级别**：A（人工扩写字段 + 表内摘要；未逐篇精读全文）

> **项目地址审计**：`platform_only`；[https://robotwin-platform.github.io/](https://robotwin-platform.github.io/)；[https://github.com/robotwin-Platform/robotwin](https://github.com/robotwin-Platform/robotwin)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins |
| 年份 | 2025、2026 |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 双臂机器人操作策略（含 VLA）。 |
| 关注属性 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、任务能力 |
| 评测维度/指标 | 生成式数字孪生；双臂协同任务与真机迁移 |
| 基础平台线索 | LIBERO、RoboTwin、ManiSkill |
| 规模线索 | 表内摘要未明确规模。 |
| 执行环境线索 | 摘要同时提到仿真与真机/实体机器人。 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：单臂基准无法覆盖双臂/高自由度协同操作；而双臂任务的场景与物体多样性极难靠手工搭建。

**主要测量维度**：生成式数字孪生；双臂协同任务与真机迁移。

## 2. 怎么构建的

### 2.1 构建要素

| 要素 | 摘要级记录 |
|---|---|
| 基础平台 | LIBERO、RoboTwin、ManiSkill |
| 任务/场景规模 | 表内摘要未明确规模。 |
| 扰动、风险或约束 | 生成式数字孪生；双臂协同任务与真机迁移 |
| 对照/配对方式 | 摘要提到配对、孪生或受控对照。 |
| 指标与判分线索 | 生成式数字孪生；双臂协同任务与真机迁移 |
| 执行设置 | 摘要同时提到仿真与真机/实体机器人。 |

### 2.2 详细说明

用**生成式数字孪生**批量生成多样化物体与场景，从而在仿真中大规模构造双臂协同操作任务，并支持向真机迁移的评测。

## 3. 用这个基准测了什么

**被测对象**：双臂机器人操作策略（含 VLA）。

**结果应如何读取**：先按“评测维度/指标”字段区分主指标、辅助指标和对照条件；若论文同时报告任务成功与安全/鲁棒性结果，应将二者分开阅读。

下表按论文列出；“摘要级发现”保留调研表中的概要，不等同于全文实验结论。

| 论文 | 年份 / 来源 | 角色 | 被测对象 | 使用方式 / 指标 | 摘要级发现 |
|---|---|---|---|---|---|
| [Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准](https://arxiv.org/abs/2608.26578) | 2026 / arXiv 预印本 (arXiv:2608.26578) | 使用 | VLA 模型 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 | 提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。 |
| [动作 tokenizer 究竟该按什么评：重建之外的可预测性与鲁棒性](https://arxiv.org/abs/2610.09170) | 2026 / arXiv 预印本 (arXiv:2610.09170) | 使用 | 自回归动作 token 策略（含 VLA）与其动作 tokenizer | token 可预测性、未见 token 的解码合理性、下游策略成功率 | 通过大量分析指出：动作重建足够精确只是下游策略成功的必要条件——策略还必须能为新观测预测出正确的 token，且未见过的 token 预测仍要解码成合理动作；这些性质位于 tokenizer 训练的下游，不被重建目标直接激励。 |
| [Memorize / Adapt / Ignore：训练数据变化如何生效的机制诊断](https://arxiv.org/abs/2609.38401) | 2026 / arXiv 预印本 (arXiv:2609.38401) | 使用 | ManiSkill 拾放 RL 策略与 LIBERO / RoboTwin 上微调的 VLA | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） | 训练数据变化（仿真中的域随机化方案、模仿学习中的示范筛选）是提升操作策略鲁棒性的主要手段，但其机制不清楚，实践中只能靠昂贵的试错调随机化参数。 |
| [世界动作模型需要什么样的视觉表示](https://arxiv.org/abs/2610.13024) | 2026 / arXiv 预印本 (arXiv:2610.13024) | 使用 | 世界动作模型（WAM）；5 种集成机制 | 视觉表示 × 集成机制 × 特征组合的受控对比；鲁棒性 | WAM 从预训练视频生成模型继承强先验，但其 VAE 表示是为视觉重建而非操作优化；外部视觉表示能提升操作，但既有方法把表示选择与集成机制绑在一起，掩盖了各自的作用。 |
| [JailWAM：世界动作模型的越狱攻击与评测框架](https://arxiv.org/abs/2604.05498) | 2026 / arXiv 预印本 (arXiv:2604.05498) | 使用 | 世界动作模型（WAM）控制的机械臂 | 三级安全分类框架；越狱攻击成功率与物理危害 | 指出世界动作模型能联合预测未来状态与动作、物理操作能力更强，但这也使其安全风险更大，而既有研究对 WAM 的越狱脆弱性关注极少。作者先定义「三级安全分类框架」以系统量化机械臂动作的安全性，再提出首个面向 WAM 的越狱攻击与评测框架 JailWAM（含视觉-轨迹映射等三个核心组件）。 |
| [TAPDreamer：面向世界动作模型的可迁移对抗补丁](https://arxiv.org/abs/2610.06814) | 2026 / arXiv 预印本 (arXiv:2610.06814) | 使用 | 世界动作模型（WAM） | 仅用公开编码器、无需查询目标策略；跨任务与跨动作架构迁移 | 世界动作模型依赖相机输入，而相机输入被操纵会污染跨任务、跨动作策略共享的视觉表示。既有攻击需要访问目标模型的输出或预测未来，TAPDreamer 只用公开编码器构造一个固定的局部扰动即可跨任务与动作架构迁移、且无需任何目标策略查询； |
| [RoboTwin：生成式数字孪生的双臂机器人基准](https://doi.org/10.1109/CVPR52734.2025.02575) | 2025 / CVPR 2025（IEEE/CVF 计算机视觉与模式… | **提出** | 双臂机器人操作策略 | 生成式数字孪生；双臂协同任务与真机迁移 | 用生成式数字孪生构建双臂机器人基准：借助生成模型批量生成多样化物体与场景的数字孪生，从而在仿真中大规模构造双臂协同操作任务，并支持向真机迁移的评测。 |
| [dWorldEval：离散扩散世界模型驱动的可扩展策略评测](https://arxiv.org/abs/2604.22152) | 2026 / arXiv 预印本 (arXiv:2604.22152) | 使用 | 机器人策略（大规模跨环境跨任务） | 离散扩散世界模型；视觉/语言/动作统一 token 空间 | 指出在数千个环境、数千个任务上评测机器人策略用现有方法不可行，因此需要新的可扩展评测方法论。 |

## 4. 关键结论、改进方向与可复用性

**关键结论**：生成式资产是解决场景多样性瓶颈的可行路径；双臂任务对协调性的要求暴露了单臂基准看不到的失败模式。

**论文提到的改进方向**：①把双臂协调性作为独立指标；②生成的数字孪生需做真机一致性校验；③已被多篇安全基准复用为场景底座（Trap-RoboTwin、ForesightSafety-VLA）。

**复用状态**：已有至少一篇后续论文使用，具备初步跨论文证据。

## 5. 相关论文（均来自本调研表）

- [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2026，arXiv 预印本 (arXiv:2608.26578)）
- [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170)（2026，arXiv 预印本 (arXiv:2610.09170)）
- [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)（2026，arXiv 预印本 (arXiv:2609.38401)）
- [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024)（2026，arXiv 预印本 (arXiv:2610.13024)）
- [JailWAM: Jailbreaking World Action Models in Robot Control](https://arxiv.org/abs/2604.05498)（2026，arXiv 预印本 (arXiv:2604.05498)）
- [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)（2026，arXiv 预印本 (arXiv:2610.06814)）
- [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://doi.org/10.1109/CVPR52734.2025.02575)（2025，CVPR 2025（IEEE/CVF 计算机视觉与模式识别会议））  ← **提出**
- [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152)（2026，arXiv 预印本 (arXiv:2604.22152)）

## 6. 证据边界与复核建议

- **证据级别**：A（人工扩写字段 + 表内摘要；未逐篇精读全文）。
- **主要来源**：[RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://doi.org/10.1109/CVPR52734.2025.02575)。
- **当前限制**：本文档基于调研表、论文摘要和少量人工整理；核心条目另有本地全文核查补录，但仍未替代对全文实验表格、附录、代码仓库和数据下载说明的逐项复核。
- **建议复核**：优先确认任务/场景划分、样本规模、指标公式、判分阈值、模型清单，以及仿真与真机设置是否一致。

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成。 A 级文档含人工扩写字段；核心条目附本地全文核查补录；B/C 级文档主要依赖摘要级结构化记录。*
