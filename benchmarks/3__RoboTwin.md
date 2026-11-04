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
| 规模线索 | 本次阅读 CVPR（会议／期刊） 2025 对应版本的 14 项任务，包含交接、双物体抓取、摆放、开柜和挂杯；在 COBOT Magic 平台验证。 |
| 执行环境线索 | 双臂生成式数字孪生 |
| OpenAlex 引用快照 | [31](https://openalex.org/W4413144615)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 8 个缩写／技术词，并标出 9 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Yao Mu, Tianxing Chen, Zanxin Chen, et al., ‘RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins,’ arXiv preprint, 2025, arXiv:2504.13059v1. [论文](https://doi.org/10.1109/CVPR52734.2025.02575)；[核查正文](https://arxiv.org/html/2504.13059v1)。

**重点核查位置（章节主题）**：3 Digital Twin Generation；4 Benchmark；5.1 Setup；5.2 Results；5.3 Real World。

OpenAlex 被引次数：**[31](https://openalex.org/W4413144615)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://robotwin-platform.github.io/](https://robotwin-platform.github.io/)；[https://github.com/robotwin-Platform/robotwin](https://github.com/robotwin-Platform/robotwin)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 7 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **30** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 49 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://robotwin-platform.github.io/](https://robotwin-platform.github.io/)；[https://github.com/robotwin-Platform/robotwin](https://github.com/robotwin-Platform/robotwin)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://robotwin-platform.github.io/) | https://robotwin-platform.github.io/ | 保留文本 4200 字符（截断） |
| [repo](https://github.com/robotwin-Platform/robotwin) | https://raw.githubusercontent.com/robotwin-Platform/robotwin/HEAD/README.md | stars 3033，license MIT（开源许可证），最后推送 2026-09-24，保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://robotwin-platform.github.io/ 为 2.0 版本；GitHub https://github.com/robotwin-Platform/robotwin（3,033 stars，MIT，2026-09-24 推送）README 汇总 Webpage／Doc／Paper／Talk／Leaderboard。

**涉及领域**：双臂操作的数据生成与基准；单图生成数字孪生，强域随机化（RoboTwin 2.0）。

**测试目的与构建方法**：由单图生成物体孪生，为资产补充空间关系标注，再分解任务并生成专家运动；用 20／50／100 示范训练 2D Diffusion Policy 与不同点云输入的 DP3。

**测试缺陷**：成功要求终点姿态达标且全程无碰撞；本卡对应 1.0，不能与 2.0 的任务规模或后来的 VLA 结果混用；单项示例不是全基准平均。

**与具身智能安全的相关性**：中等：成功判据含“全程无碰撞”，因此比纯成功率高一点安全含义；但没有损伤、力或违规类别。

**用这个 benchmark 测了什么**：同一任务随输入与示范量差异很大（100 示范的 Block Hammer Beat 上 DP3 XYZ+RGB 82.0%、2D DP 0%）；下游 PointVLA 等引用，RoboTwin 2.0（ICML（会议／期刊） 2026）成为主要基线。

**本轮核查边界**：站内信息以 2.0 为主，1.0 与 2.0 的差异未逐条拆分。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| RecastVLA: From Past Interaction to Future Control with Adaptive Test-…（2026） | RecastVLA（测试时训练） | 评测（与“不做测试时训练”的匹配策略对比） | LIBERO、RoboTwin、RoboDojo 与 12 个真机任务；RoboTwin Clean-to-Clean | RoboTwin Clean-to-Clean 提升 10.68 个百分点 |
| Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robot Ma…（2026） | Qwen-RobotManip | 评测（OOD 设置族） | RoboTwin-Clean2Rand、RoboTwin-IF、RoboTwin-XE 等 OOD 子集 | 把 RoboTwin 的多个变体当 OOD 测试场；未给单一分数 |
| Seeing Realism from Simulation: Efficient Video Transfer for Visual Ro…（2026） | 该文的视频迁移方法 | 训练后评测（跨基准 + 真机） | RoboTwin 2.0、LIBERO、LIBERO-Plus 与真实机器人平台 | 称四处一致提升（摘要无具体数值） |
| RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Doma…（2025） | —（该文即 2.0 版本） | 自更新（数据生成器 + 统一评测协议） | 双臂操作，强域随机化 | 产出 2.0 与统一协议；原论文的 1.0 版本是本条目的来源 |
| Benchmarking Generalizable Bimanual Manipulation: RoboTwin Dual-Arm Co…（2025） | 挑战赛参赛策略 | 派生挑战赛（CVPR 2025 MEIS Workshop） | 双臂协作任务赛道 | 产出赛题与成绩榜，不是原基准分数 |

**原文片段（摘要）**：

- RecastVLA: From Past Interaction to Future Control with Adap…（2026，arXiv）：> including 10.68 percentage points on RoboTwin Clean-to-Clean
- Qwen-RobotManip Technical Report: Alignment Unlocks Scale fo…（2026，arXiv）：> adopt OOD settings including … RoboTwin-Clean2Rand, RoboTwin-IF, and RoboTwin-XE
- Seeing Realism from Simulation: Efficient Video Transfer for…（2026，arXiv）：> Extensive experiments on Robotwin 2.0, LIBERO, LIBERO-Plus, and a real robotic platform demonstrate consistent improvements
- RoboTwin 2.0: A Scalable Data Generator and Benchmark with S…（2025，arXiv）：> We present RoboTwin 2.0, a scalable framework … together with unified evaluation protocols for dual-arm manipulation
- Benchmarking Generalizable Bimanual Manipulation: RoboTwin D…（2025，arXiv）：> we launched the RoboTwin Dual-Arm Collaboration Challenge at the 2nd MEIS Workshop, CVPR 2025

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 8 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **DP3** | 3D Diffusion Policy | 三维扩散策略 | 用点云输入的扩散策略基线，与 2D 版本对照说明三维表示的价值。 |
| **WAM** | World-Action Model | 世界—动作模型 | 同时预测未来画面与动作的模型，用于规划或作为策略主干。 |
| **DP** | Diffusion Policy | 扩散策略 | 用扩散模型生成动作序列的模仿学习基线，安全论文里常作“普通策略”对照。 |
| **digital twin** | digital twin | 数字孪生 | 按真实场景生成的可交互三维副本，用于批量造数据与评测。 |
| **domain randomization** | domain randomization | 域随机化 | 训练时随机化纹理、光照、相机位姿、物理参数，逼策略学不变特征。 |
| **OOD** | Out-of-Distribution | 分布外 | 测试数据与训练分布不同，用来检验泛化。 |
| **RGB** | RGB image observation | 彩色图像观测 | 只用普通彩色相机画面作为输入，不含深度、触觉或本体状态。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboTwin | 基准 | 双臂操作数据生成与评测 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| ManiSkill | 基准 | 通用操作技能基准（SAPIEN） |
| TrapVLA | 基准 | VLA 后门／失效注入方法与其基准 |
| ForesightSafety-VLA | 基准 | VLA 安全诊断基准 |
| LIBERO-Plus | 基准 | LIBERO 的扰动扩展 |

另有 3 个专有名称已在正文首次出现处加括号标注类别（例如 CVPR（会议／期刊）、MIT（开源许可证）、ICML（会议／期刊）），不再重复解释。

<!-- glossary:end -->
