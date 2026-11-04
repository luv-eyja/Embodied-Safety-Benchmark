# BiDex-100

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：统一双手任务与能力轴评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：双手灵巧操作 106 任务  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://robbyant-research.github.io/BiDex-100](https://robbyant-research.github.io/BiDex-100)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 双手灵巧操作仿真 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 5 条能力轴：泛化、指令遵循、少示范、长时程、记忆；每任务配域外变体 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 名称虽为 100，正文包含 106 任务；两种本体、8,080 条成功核验示范、约 625 万帧，按五条能力轴组织。 |
| 执行环境线索 | 双手灵巧操作仿真 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7223068191)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：通用 VLA 在高自由度双手操作中，泛化、指令遵循、少样本、长时程和记忆能力分别如何？

**评测层级**：双手灵巧操作仿真。

## 2. 怎么构建的

**核心场景与条目**：名称虽为 100，正文包含 106 任务；两种本体、8,080 条成功核验示范、约 625 万帧，按五条能力轴组织。

**实现与判分**：声明式配置对象、区域、关节和目标，使用逻辑完成条件与阶段进度；用匹配的随机种子构造 ID/OOD，每任务两种种子各 25 episode。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459) | 2026 | 提出 | 5 条能力轴：泛化、指令遵循、少示范、长时程、记忆；每任务配域外变体 | 现有工作很少有针对灵巧操作专门设计的基准，导致模型的灵巧操作能力刻画不足。BiDex-100 是双手灵巧操作的仿真基准，兼顾任务覆盖广度、多维评测与高自由度手部本体：含 106 个任务，沿泛化、指令遵循、少示范、长时程、记忆五条能力轴组织；每个任务配一个含受控视觉与空间变化的域外变体，用于系统评估分布外表现。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：LingBot-VLA-v2 的 ID 总成功率为 52.21%，OOD 为 1.68%；GR00T-N1.7 的 OOD 总成功率为 5.45%。多任务成功与域外泛化差距巨大。

**适用边界**：结果对应文中本体、训练设置及组合变化；进度分数和全部完成率不同。不可把模型家族结论推广至未测 checkpoint。

## 5. 相关论文（均来自本调研表）

- [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

结果对应文中本体、训练设置及组合变化；进度分数和全部完成率不同。不可把模型家族结论推广至未测 checkpoint。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Yong Wang, Kecheng Zheng, Xing Zhu, et al., ‘BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks,’ arXiv preprint, 2026, arXiv:2610.25459v2. [论文](https://arxiv.org/abs/2610.25459)；[核查正文](https://arxiv.org/html/2610.25459v2)。

**重点核查位置（章节主题）**：Benchmark Design；Evaluation Protocol；V-C Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7223068191)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://robbyant-research.github.io/BiDex-100](https://robbyant-research.github.io/BiDex-100)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://robbyant-research.github.io/BiDex-100](https://robbyant-research.github.io/BiDex-100)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://robbyant-research.github.io/BiDex-100) | https://robbyant-research.github.io/BiDex-100 | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://robbyant-research.github.io/BiDex-100 提供 Overview、Document、Setup、Domain Randomization、Tasks、Leaderboard 与 News，作者匿名（投稿中）。

**涉及领域**：双臂灵巧操作，100+ 仿真任务，按“能力边界”组织。

**测试目的与构建方法**：声明式配置对象、区域、关节与目标，用逻辑完成条件和阶段进度判分；用匹配随机种子构造 ID/OOD 划分，每任务两种种子各 25 episode。

**测试缺陷**：结果绑定特定本体与训练设置；进度分数与全部完成率不可互换；域外泛化只用种子匹配的 OOD 划分，未必覆盖真实分布偏移；纯仿真。

**与具身智能安全的相关性**：间接：多任务灵巧操作的能力边界可用来定位“哪些动作类别还没做稳”，但基准本身不定义风险或伤害。

**用这个 benchmark 测了什么**：LingBot-VLA-v2 的 ID 总成功率 52.21%、OOD 仅 1.68%；GR00T-N1.7 的 OOD 总成功率 5.45%，显示多任务成功与域外泛化差距巨大。

**本轮核查边界**：只读项目页，未核对任务清单与评分实现。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 6 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **GR00T** | NVIDIA GR00T N1 / N1.5 | GR00T 机器人基础模型 | NVIDIA 的类人／通用操作基础模型家族，常作为强基线或微调起点。 |
| **ID** | In-Distribution | 分布内 | 测试与训练同分布，通常作为上限参照。 |
| **OOD** | Out-of-Distribution | 分布外 | 测试数据与训练分布不同，用来检验泛化。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| BiDex-100 | 基准 | 双手灵巧操作仿真 |

<!-- glossary:end -->
