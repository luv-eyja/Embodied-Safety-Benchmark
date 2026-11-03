# RoboTwin

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：任务、数字孪生与生成专家数据共同支持双臂评测；未因成功谓词含避碰单列安全目标。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（双臂协同）  
> **分类**：VLA 能力  
> **关联论文**：本表 8 篇（提出 1、使用 7；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robotwin-platform.github.io/](https://robotwin-platform.github.io/)；[https://github.com/robotwin-Platform/robotwin](https://github.com/robotwin-Platform/robotwin)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 双臂生成式数字孪生 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、任务能力 |
| 评测维度/指标 | 生成式数字孪生；双臂协同任务与真机迁移 |
| 基础平台线索 | LIBERO、RoboTwin、ManiSkill |
| 规模线索 | 本次阅读 CVPR 2025 对应版本的 14 项任务，包含交接、双物体抓取、摆放、开柜和挂杯；在 COBOT Magic 平台验证。 |
| 执行环境线索 | 双臂生成式数字孪生 |
| OpenAlex 引用快照 | [31](https://openalex.org/W4413144615)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：双臂示范稀缺时，如何自动产生多样资产和可执行专家轨迹，并缩小真实评测差距？

**评测层级**：双臂生成式数字孪生。

## 2. 怎么构建的

**核心场景与条目**：本次阅读 CVPR 2025 对应版本的 14 项任务，包含交接、双物体抓取、摆放、开柜和挂杯；在 COBOT Magic 平台验证。

**实现与判分**：由单图生成物体孪生，为资产补充空间关系标注，再分解任务与生成专家运动；以 20／50／100 示范训练 2D Diffusion Policy 与不同点云输入的 DP3。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578) | 2026 | 使用 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 | 提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。 |
| [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170) | 2026 | 使用 | token 可预测性、未见 token 的解码合理性、下游策略成功率 | 通过大量分析指出：动作重建足够精确只是下游策略成功的必要条件——策略还必须能为新观测预测出正确的 token，且未见过的 token 预测仍要解码成合理动作；这些性质位于 tokenizer 训练的下游，不被重建目标直接激励。作者据此提出同时衡量可预测性与鲁棒解码的动作 tokenizer 设计（PACT）。 |
| [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401) | 2026 | 使用 | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） | 训练数据变化（仿真中的域随机化方案、模仿学习中的示范筛选）是提升操作策略鲁棒性的主要手段，但其机制不清楚，实践中只能靠昂贵的试错调随机化参数。作者以物体尺寸、颜色、类型以及场景光照与语言提示为变量，跨 ManiSkill 与 LIBERO/RoboTwin 做系列案例研究，同时考察模型行为与内部表示，并以经验神经正切核（NTK）为主要分析工具。 |
| [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024) | 2026 | 使用 | 视觉表示 × 集成机制 × 特征组合的受控对比；鲁棒性 | WAM 从预训练视频生成模型继承强先验，但其 VAE 表示是为视觉重建而非操作优化；外部视觉表示能提升操作，但既有方法把表示选择与集成机制绑在一起，掩盖了各自的作用。作者在受控设置下系统比较视觉表示、五种集成机制与特征组合，结论包括：强通用视觉表示带来更广的鲁棒性收益，能匹配甚至超过为特定视觉能力预训练的表示；通道级联合预测效果最好。 |
| [JailWAM: Jailbreaking World Action Models in Robot Control](https://arxiv.org/abs/2604.05498) | 2026 | 使用 | 三级安全分类框架；越狱攻击成功率与物理危害 | 指出世界动作模型能联合预测未来状态与动作、物理操作能力更强，但这也使其安全风险更大，而既有研究对 WAM 的越狱脆弱性关注极少。作者先定义「三级安全分类框架」以系统量化机械臂动作的安全性，再提出首个面向 WAM 的越狱攻击与评测框架 JailWAM（含视觉-轨迹映射等三个核心组件）。 |
| [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814) | 2026 | 使用 | 仅用公开编码器、无需查询目标策略；跨任务与跨动作架构迁移 | 世界动作模型依赖相机输入，而相机输入被操纵会污染跨任务、跨动作策略共享的视觉表示。既有攻击需要访问目标模型的输出或预测未来，TAPDreamer 只用公开编码器构造一个固定的局部扰动即可跨任务与动作架构迁移、且无需任何目标策略查询；其洞见是补丁引起的注意力权重与 value 向量交互会把影响广播到全局表示。 |
| [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://doi.org/10.1109/CVPR52734.2025.02575) | 2025 | 提出 | 生成式数字孪生；双臂协同任务与真机迁移 | 用生成式数字孪生构建双臂机器人基准：借助生成模型批量生成多样化物体与场景的数字孪生，从而在仿真中大规模构造双臂协同操作任务，并支持向真机迁移的评测。它填补了单臂基准之外的「双臂/高自由度协同」评测空白，也被多篇 VLA 安全基准（如 Trap-RoboTwin、ForesightSafety-VLA）复用为场景底座。 |
| [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152) | 2026 | 使用 | 离散扩散世界模型；视觉/语言/动作统一 token 空间 | 指出在数千个环境、数千个任务上评测机器人策略用现有方法不可行，因此需要新的可扩展评测方法论。dWorldEval 用离散扩散世界模型作为可扩展的评测代理：把视觉、语言与机器人动作等所有模态映射到统一 token 空间，用单个基于 transformer 的去噪网络建模，从而以生成方式预测策略执行结果。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：同一任务随输入和示范量表现差异很大，例如 100 示范的 Block Hammer Beat 上 DP3 XYZ+RGB 为 82.0%，2D DP 为 0%；有限真机微调实验支持仿真预训练的帮助。

**适用边界**：这里的成功要求终点姿态达标且全程无碰撞。该版本不能与 RoboTwin 2.0 的任务规模或后来的 VLA 结果混用；单项示例不是全基准平均。

## 5. 相关论文（均来自本调研表）

- [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2026；使用）
- [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170)（2026；使用）
- [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)（2026；使用）
- [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024)（2026；使用）
- [JailWAM: Jailbreaking World Action Models in Robot Control](https://arxiv.org/abs/2604.05498)（2026；使用）
- [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)（2026；使用）
- [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://doi.org/10.1109/CVPR52734.2025.02575)（2025；提出）
- [dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model](https://arxiv.org/abs/2604.22152)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这里的成功要求终点姿态达标且全程无碰撞。该版本不能与 RoboTwin 2.0 的任务规模或后来的 VLA 结果混用；单项示例不是全基准平均。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Yao Mu, Tianxing Chen, Zanxin Chen, et al., ‘RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins,’ arXiv preprint, 2025, arXiv:2504.13059v1. [论文](https://doi.org/10.1109/CVPR52734.2025.02575)；[核查正文](https://arxiv.org/html/2504.13059v1)。

**重点核查位置（章节主题）**：3 Digital Twin Generation；4 Benchmark；5.1 Setup；5.2 Results；5.3 Real World。

OpenAlex 被引次数：**[31](https://openalex.org/W4413144615)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://robotwin-platform.github.io/](https://robotwin-platform.github.io/)；[https://github.com/robotwin-Platform/robotwin](https://github.com/robotwin-Platform/robotwin)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 7 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
