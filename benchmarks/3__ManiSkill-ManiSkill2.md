# ManiSkill / ManiSkill2

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：评测任务集与统一接口，保留版本合并条目的边界。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（可泛化技能）  
> **分类**：VLA 能力  
> **关联论文**：本表 2 篇（提出 1、使用 1；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://maniskill2.github.io/](https://maniskill2.github.io/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills |
| 年份 | 2023（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 可泛化操作仿真平台 |
| 历史关键词标签（未重新统计） | 语义/指令安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 物体级拓扑与几何变化、完全动态仿真、多类型操作任务原生支持 |
| 基础平台线索 | LIBERO、RoboTwin、ManiSkill、SAPIEN |
| 规模线索 | 本次以 ManiSkill2 论文为准：20 个任务族、2,000 余对象模型、400 万余示范帧，覆盖固定／移动、单臂／双臂和刚体／软体。 |
| 执行环境线索 | 可泛化操作仿真平台 |
| OpenAlex 引用快照 | [24](https://openalex.org/W4320165654)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 6 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：能否在统一、高效的环境中比较不同视觉表示、学习算法和机器人控制方式？

**评测层级**：可泛化操作仿真平台。

## 2. 怎么构建的

**核心场景与条目**：本次以 ManiSkill2 论文为准：20 个任务族、2,000 余对象模型、400 万余示范帧，覆盖固定／移动、单臂／双臂和刚体／软体。

**实现与判分**：基于 SAPIEN，提供 RGB-D、点云、状态观察，多种动作控制与示范转换；分训练对象与未见对象，支持规划、模仿和强化学习。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401) | 2026 | 使用 | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） | 训练数据变化（仿真中的域随机化方案、模仿学习中的示范筛选）是提升操作策略鲁棒性的主要手段，但其机制不清楚，实践中只能靠昂贵的试错调随机化参数。作者以物体尺寸、颜色、类型以及场景光照与语言提示为变量，跨 ManiSkill 与 LIBERO/RoboTwin 做系列案例研究，同时考察模型行为与内部表示，并以经验神经正切核（NTK）为主要分析工具。 |
| [ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659) | 2023 | 提出 | 物体级拓扑与几何变化、完全动态仿真、多类型操作任务原生支持 | 指出既有操作基准多是一组可仿真环境，因缺乏物体级拓扑与几何变化、非完全动态仿真、或缺少对多类操作任务的原生支持，已不足以推动前沿研究。ManiSkill2 是 SAPIEN ManiSkill 基准的下一代版本，针对这些痛点构建统一的、面向可泛化操作技能的评测平台。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文的 Contact-GraspNet＋规划基线在 PickSingleYCB 的 74 个训练对象、各 5 次测试中成功率 43.24%，并提供模仿／强化学习及迁移案例。成果主要是环境、数据和统一接口。

**适用边界**：ManiSkill 与 ManiSkill2 属不同版本，此处引用量仅对应后者。控制空间、观察模态和对象划分不同的结果不能直接合并；训练对象分数不是泛化分数。

## 5. 相关论文（均来自本调研表）

- [Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation](https://arxiv.org/abs/2609.38401)（2026；使用）
- [ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659)（2023；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

ManiSkill 与 ManiSkill2 属不同版本，此处引用量仅对应后者。控制空间、观察模态和对象划分不同的结果不能直接合并；训练对象分数不是泛化分数。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Jiayuan Gu, Fanbo Xiang, Xuanlin Li, et al., ‘ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills,’ arXiv preprint, 2023, arXiv:2302.04659v1. [论文](https://arxiv.org/abs/2302.04659)；[核查正文](https://arxiv.org/html/2302.04659v1)。

**重点核查位置（章节主题）**：Benchmark Design；Demonstrations；5 Applications；5.1 Sense-plan-act。

OpenAlex 被引次数：**[24](https://openalex.org/W4320165654)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://maniskill2.github.io/](https://maniskill2.github.io/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **24** 篇引文论文（清单保留被引最高的 24 篇）；arXiv 摘要命中 50 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://maniskill2.github.io/](https://maniskill2.github.io/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://maniskill2.github.io/) | https://maniskill2.github.io/ | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://maniskill2.github.io/ 提供 Get Started、Video、Paper、Code、Doc、Colab 与 Discord，并公告 ManiSkill 3 Beta 已开源。

**涉及领域**：通用操作技能仿真与基准；基于 SAPIEN，覆盖抓取、装配、移动等多类任务与多种机器人。

**测试目的与构建方法**：提供 RGB-D、点云与状态观察，多种动作控制接口与示范转换；区分训练对象与未见对象，支持规划、模仿学习与强化学习；pip 可装、可跑 Colab。

**测试缺陷**：ManiSkill 与 ManiSkill2 属不同版本，引用量仅对应后者；控制空间、观察模态与对象划分不同的结果不能直接合并；训练对象上的分数不是泛化分数。

**与具身智能安全的相关性**：弱：这是能力与仿真基础设施，本身不测安全；但它是接触丰富任务的主要试验台，可承载力／接触类安全扩展。

**用这个 benchmark 测了什么**：论文的 Contact-GraspNet＋规划基线在 PickSingleYCB 的 74 个训练对象、各 5 次测试中成功率 43.24%，并提供模仿／强化学习与迁移案例；下游有 Orbit、PhyScene 等，2025 年 ManiSkill-ViTac 挑战赛把它扩展成触觉赛道。

**本轮核查边界**：只读官网首页，ManiSkill 3 与 ManiSkill2 的差异未逐项核对。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **4 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| NestedVLA: Learning to Consolidate and Generate Skills for Vision-Lang…（2026） | NestedVLA（技能整合），三个用 RL 微调的策略 | 训练后评测（跨基准技能整合） | 分别用 MetaWorld、ManiSkill、CALVIN 上 RL 微调的策略做整合 | 摘要只说明整合方式，未给数值 |
| RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learnin…（2025） | RLinf-VLA（VLA 强化学习框架） | 训练加速评测（在基准上测吞吐） | ManiSkill 上的混合细粒度流水线分配 | 训练加速 1.61×–1.88× |
| ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Ta…（2024） | 参赛策略（触觉 + 视觉） | 派生挑战赛（以 ManiSkill 为底座） | 接触丰富任务，要求同时用触觉与视觉 | 产出的是赛题与协议，不是原基准分数 |
| Let's Handle It: Generalizable Manipulation of Articulated Objects（2022） | 该文的抓取／操作框架 | 挑战赛提交（SAPIEN ManiSkill Challenge 2021 赛道… | 四个操作技能，日常铰接物体 | 摘要称四项技能均可演示，未给榜单名次 |

**原文片段（摘要）**：

- NestedVLA: Learning to Consolidate and Generate Skills for V…（2026，arXiv）：> We evaluate NestedVLA by consolidating three policies fine-tuned with reinforcement learning on MetaWorld, ManiSkill, and CALVIN
- RLinf-VLA: A Unified and Efficient Framework for Reinforceme…（2025，arXiv）：> achieves a 1.61×-1.88× training speedup on ManiSkill
- ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learni…（2024，arXiv）：> This article introduces the ManiSkill-ViTac Challenge 2025
- Let's Handle It: Generalizable Manipulation of Articulated O…（2022，arXiv）：> We demonstrate our framework on four manipulation skills … that comprise the SAPIEN ManiSkill Manipulation challenge

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 5 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **RL** | Reinforcement Learning | 强化学习 | 用奖励信号优化策略，区别于用示范做监督学习。 |
| **domain randomization** | domain randomization | 域随机化 | 训练时随机化纹理、光照、相机位姿、物理参数，逼策略学不变特征。 |
| **SAPIEN** | SAPIEN | SAPIEN 仿真引擎 | 面向铰接物体操作的物理仿真引擎，ManiSkill、SimplerEnv 的底座。 |
| **RGB** | RGB image observation | 彩色图像观测 | 只用普通彩色相机画面作为输入，不含深度、触觉或本体状态。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| ManiSkill | 基准 | 通用操作技能基准（SAPIEN） |
| ManiSkill / ManiSkill2 | 基准 | 可泛化操作仿真平台 |
| ManiSkill2 | 基准 | ManiSkill 的第二代 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |
| CALVIN | 基准 | 语言条件长时程操作基准 |

<!-- glossary:end -->
