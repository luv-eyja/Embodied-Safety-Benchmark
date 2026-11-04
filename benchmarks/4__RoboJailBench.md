# RoboJailBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：安全。
> **分类依据**：安全—有用性评测数据和接口，非物理控制成功率。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：越狱攻防（安全-有用性权衡）  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://purseclab.github.io/benchmark-for-robotics-security](https://purseclab.github.io/benchmark-for-robotics-security)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Task Planning |
| 应用领域 | 未标注 |
| 被测对象 | 具身规划的安全与有用性评测 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、对抗/后门安全、任务能力 |
| 评测维度/指标 | 越狱攻击成功率 + 良性指令遵循；安全-有用性权衡 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 18 类风险后果的 taxonomy，以六种数据来源构造正常／危险意图对照，强调场景接地和安全—有用性平衡。 |
| 执行环境线索 | 具身规划的安全与有用性评测 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7161775162)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：增强拒绝危险目标后，模型是否仍能接受语义相近的正常目标？

**评测层级**：具身规划的安全与有用性评测。

## 2. 怎么构建的

**核心场景与条目**：18 类风险后果的 taxonomy，以六种数据来源构造正常／危险意图对照，强调场景接地和安全—有用性平衡。

**实现与判分**：统一评测接口，分别报告危险目标拒绝的 Security Rate、正常目标接受的 Utility Rate 和调和均值 SU-HM；将无风险干预基线与压力测试分开。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](https://arxiv.org/abs/2605.19328) | 2026 | 提出 | 越狱攻击成功率 + 良性指令遵循；安全-有用性权衡 | 指出既有具身越狱研究依赖临时数据集、指标有限，且只看攻击成功率而忽视对良性指令的遵循能力；现有基准要么面向聊天模型，要么只做非对抗的安全评测，都无法刻画具身越狱所需的风险、输入、后果与评价标准。该基准填补这一空白，统一衡量攻击有效性与良性任务能力之间的权衡。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：无额外干预的基线中 Claude Haiku 4.5 的危险拒绝率为 98.28%，GPT 5.4 Nano 正常接受率为 99.49%、SU-HM 为 97.84%；这些不是受压力条件下的最终安全率。

**适用边界**：本论文 SR 指 Security Rate，其他机器人论文常指 Success Rate。接受／拒绝计划不等于物理动作成功或安全，不可将不同条件表格混读。

## 5. 相关论文（均来自本调研表）

- [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](https://arxiv.org/abs/2605.19328)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

本论文 SR 指 Security Rate，其他机器人论文常指 Success Rate。接受／拒绝计划不等于物理动作成功或安全，不可将不同条件表格混读。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Doguhuan Yeke, Yanming Zhou, Leo Y. Lin, et al., ‘RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents,’ arXiv preprint, 2026, arXiv:2605.19328v1. [论文](https://arxiv.org/abs/2605.19328)；[核查正文](https://arxiv.org/html/2605.19328v1)。

**重点核查位置（章节主题）**：3.2 Security Taxonomy；3.3 Intent Contrast Dataset；3.4 Evaluation Framework；4.1 Baseline Performance。

OpenAlex 被引次数：**[0](https://openalex.org/W7161775162)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://purseclab.github.io/benchmark-for-robotics-security](https://purseclab.github.io/benchmark-for-robotics-security)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://purseclab.github.io/benchmark-for-robotics-security](https://purseclab.github.io/benchmark-for-robotics-security)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://purseclab.github.io/benchmark-for-robotics-security) | https://purseclab.github.io/benchmark-for-robotics-security | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://purseclab.github.io/benchmark-for-robotics-security 提供 Metadata、Code、arXiv、View Examples、Leaderboard、BibTeX，标注 11 子集／18 类别／990 配对指令／1,408 场景图／428MB 数据。

**涉及领域**：具身机器人的对抗攻击与防御；11 个子集、18 个安全类别。

**测试目的与构建方法**：统一评测接口，分别报告危险目标拒绝的 Security Rate、正常目标接受的 Utility Rate 与调和均值 SU-HM；把“无风险干预基线”与“压力测试”分开。

**测试缺陷**：本论文的 SR 指 Security Rate，与其他机器人论文的 Success Rate 同名异义，极易误读；接受／拒绝计划不等于物理动作成功；990 对指令与 1,408 张场景图仍是有限覆盖。

**与具身智能安全的相关性**：直接：测攻击条件下的拒绝能力，是安全评测里少见的“攻防”视角；但仍停在计划层，未测执行后的物理后果。

**用这个 benchmark 测了什么**：无额外干预的基线中 Claude Haiku 4.5 危险拒绝率 98.28%，GPT 5.4 Nano 正常接受率 99.49%、SU-HM 97.84%——这些是干净条件下的数字，不是受压力后的最终安全率。

**本轮核查边界**：只读项目页统计，未下载 428MB 数据。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **SU-HM** | Safety-Utility Harmonic Mean | 安全—效用调和平均 | 把危险拒绝率与正常接受率合成为一个分，防止只靠“全拒绝”刷安全。 |
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboJailBench | 基准 | 具身对抗攻击与防御基准 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 Claude（LLM 模型）），不再重复解释。

<!-- glossary:end -->
