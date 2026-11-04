# HygieneRoboBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：污染传播及受限资源安全规划测试集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：卫生感知规划  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://euron-zc.github.io/HygieneRoboBench](https://euron-zc.github.io/HygieneRoboBench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Task Planning |
| 应用领域 | 家务规划 |
| 被测对象 | 接触历史驱动的卫生规划 |
| 历史关键词标签（未重新统计） | 物理/接触安全、任务能力 |
| 评测维度/指标 | 624 个实例 / 134 个任务族；接触史传播、处理代价、用户优先级 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 134 任务族、624 实例；双夹爪、工具和共用表面间的污染传播，配置不同历史、用户偏好和新接触事件。 |
| 执行环境线索 | 接触历史驱动的卫生规划 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221007195)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：接触历史造成污染传播后，机器人如何安全继续任务，同时满足资源、时间和用户成本优先级？

**评测层级**：接触历史驱动的卫生规划。

## 2. 怎么构建的

**核心场景与条目**：134 任务族、624 实例；双夹爪、工具和共用表面间的污染传播，配置不同历史、用户偏好和新接触事件。

**实现与判分**：规划器读取公开规则、结构化状态和历史；独立 evaluator 完整重放计划，隐藏 reference 给出可行性与最优成本。Hygiene-NSP 结合语言接地、历史重建和 CP-SAT。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots](https://arxiv.org/abs/2610.08642) | 2026 | 提出 | 624 个实例 / 134 个任务族；接触史传播、处理代价、用户优先级 | 指出与污染物接触会通过机器人的夹爪、工具与共用表面传播危害，而新的接触可能让已有计划变得不安全；现有基准不能同时评估「规划器如何根据接触史识别卫生风险」与「新接触事件后如何规划安全的后续动作」。基准含 624 个实例、134 个任务族，要求规划器在时间与资源限制下、尊重用户优先级地求解。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：Hygiene-NSP 总体安全解决率 SR 为 94.4%、最优安全解决率 OSR 为 90.4%；安全完成与按用户优先级最省成本并非同一能力。

**适用边界**：这里的 SR 包括正确拒绝不可行续接，不能当纯执行成功率。参考最优性只在声明的动作、时间界内成立，也不等于真实微生物传播验证。

## 5. 相关论文（均来自本调研表）

- [HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots](https://arxiv.org/abs/2610.08642)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这里的 SR 包括正确拒绝不可行续接，不能当纯执行成功率。参考最优性只在声明的动作、时间界内成立，也不等于真实微生物传播验证。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Yurun Chen, Josh Qixuan Sun, Jason Qin, et al., ‘HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots,’ arXiv preprint, 2026, arXiv:2610.08642v1. [论文](https://arxiv.org/abs/2610.08642)；[核查正文](https://arxiv.org/html/2610.08642v1)。

**重点核查位置（章节主题）**：III-A Task Formulation；III-C Protocol and Metrics；IV Hygiene-NSP；V-B；V-C。

OpenAlex 被引次数：**[0](https://openalex.org/W7221007195)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://euron-zc.github.io/HygieneRoboBench](https://euron-zc.github.io/HygieneRoboBench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://euron-zc.github.io/HygieneRoboBench](https://euron-zc.github.io/HygieneRoboBench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://euron-zc.github.io/HygieneRoboBench) | https://euron-zc.github.io/HygieneRoboBench | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://euron-zc.github.io/HygieneRoboBench 是完整叙事页（问题／基准／发现／方法／真机案例），并链向 Paper、arXiv、Video 与 GitHub。

**涉及领域**：家庭机器人的“卫生感知”长时程规划；涉及接触传播与清洁顺序。

**测试目的与构建方法**：规划器读取公开规则、结构化状态与历史；独立 evaluator 完整重放计划，用隐藏 reference 给出可行性与最优成本；配套 Hygiene-NSP 方法结合语言接地、历史重建与 CP-SAT 求解。

**测试缺陷**：SR 包括“正确拒绝不可行续接”，不能当纯执行成功率；最优性只在声明的动作与时间界内成立；不验证真实微生物传播，卫生规则是人工设定。

**与具身智能安全的相关性**：直接测一类被忽视的安全：交叉污染与卫生顺序。它把“接触历史”变成可验证约束，对家庭／医疗场景有意义，但仍是规则层而非生物实验。

**用这个 benchmark 测了什么**：Hygiene-NSP 总体安全解决率 SR 94.4%、最优安全解决率 OSR 90.4%，显示“安全完成”与“按用户优先级最省成本”是两种能力；项目页同时展示真机案例与仿真。

**本轮核查边界**：只读项目页叙事，未进入评测器实现。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 4 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **OSR** | Optimal Safe Resolution | 最优安全解决率 | 在安全完成的前提下，还达到参考最优成本的比例。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| HygieneRoboBench | 基准 | 接触历史驱动的卫生规划 |

<!-- glossary:end -->
