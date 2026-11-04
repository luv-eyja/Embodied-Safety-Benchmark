# RoboAbstention

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：安全。
> **分类依据**：安全弃权测试，非真实执行后果判定。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：弃权能力评测  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://purseclab.github.io/RoboAbstention](https://purseclab.github.io/RoboAbstention)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Cascading Risks |
| 应用领域 | 未标注 |
| 被测对象 | 具身图像条件下的弃权判断 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、实时/治理、任务能力 |
| 评测维度/指标 | 弃权分类法；歧义、物理不可行、错误前提、传感器不足四类情形 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 从 DROID、Robo2VLM、RoboVQA、BridgeV2、EgoThink 各取 250 图，共 1,250 图、6,069 指令，覆盖不同弃权原因。 |
| 执行环境线索 | 具身图像条件下的弃权判断 |
| 来源审计 | [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce RoboAbstention。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7162010380)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：当对象不存在、指代含糊、能力不足或任务不可行时，规划模型是否知道应当停止或请求澄清？

**评测层级**：具身图像条件下的弃权判断。

## 2. 怎么构建的

**核心场景与条目**：从 DROID、Robo2VLM、RoboVQA、BridgeV2、EgoThink 各取 250 图，共 1,250 图、6,069 指令，覆盖不同弃权原因。

**实现与判分**：三阶段生成：结构化视觉接地、确定性约束推导、按类别生成指令；每图每类别抽取单条，减少模板重复，并分析错误继续执行的类型。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544) | 2026 | 提出 | 弃权分类法；歧义、物理不可行、错误前提、传感器不足四类情形 | 指出已有弃权研究多针对纯文本 LLM，无法刻画具身机器人环境固有的感知接地与物理约束。工作在具身语境下给出弃权分类法，并构建可扩展、可审计的 RoboAbstention 框架，用来自五个机器人数据集的图像生成弃权指令，要求智能体识别指令歧义、物理上不可行、基于错误前提或受限于可用传感模态与上下文而无法解决的情形。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文最佳模型 Gemini（VLM 模型） 2.5 Flash 的弃权率仅 39.0%，显示前沿视觉模型仍常在信息不足时给出计划；成果是可审计的弃权 taxonomy 与图像指令集。

**适用边界**：主要是静态图像／计划回答，不验证真实物理不可行性或实际执行结果。数据集中该弃权样本的识别率不能代表正常请求上的低误拒绝率。

## 5. 相关论文（均来自本调研表）

- [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

主要是静态图像／计划回答，不验证真实物理不可行性或实际执行结果。数据集中该弃权样本的识别率不能代表正常请求上的低误拒绝率。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Doguhan Yeke, Elif Su Temirel, Ananth Shreekumar, et al., ‘The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents,’ arXiv preprint, 2026, arXiv:2605.20544v1. [论文](https://arxiv.org/abs/2605.20544)；[核查正文](https://arxiv.org/html/2605.20544v1)。

**重点核查位置（章节主题）**：3.1 Sources；3.2 Taxonomy；3.3 Creation；3.4 Statistics；4.2 Benchmarking。

OpenAlex 被引次数：**[0](https://openalex.org/W7162010380)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://purseclab.github.io/RoboAbstention](https://purseclab.github.io/RoboAbstention)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://purseclab.github.io/RoboAbstention](https://purseclab.github.io/RoboAbstention)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://purseclab.github.io/RoboAbstention) | https://purseclab.github.io/RoboAbstention | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://purseclab.github.io/RoboAbstention 提供 arXiv、Dataset、Code、View Examples、View Results 与 BibTeX，并列出 6,069 图像、1,250 弃权类别、8 个源数据集、5 类抽象。

**涉及领域**：具身代理的“该不该拒绝”判断；静态图像 × 弃权类别，面向 VLM 规划器。

**测试目的与构建方法**：三阶段生成：结构化视觉接地 → 确定性约束推导 → 按类别生成指令；每图每类别抽单条以减少模板重复，并分析“错误却继续执行”的类型。

**测试缺陷**：主要是静态图像与计划回答，不验证真实物理不可行性；该弃权样本上的识别率不能代表正常请求上的低误拒率；类别由规则生成，覆盖有限。

**与具身智能安全的相关性**：直接相关于安全的一个重要侧面：知道何时不该做。弃权机制是风险规避的最后一环，但基准不测执行后的后果。

**用这个 benchmark 测了什么**：论文中最佳模型 Gemini 2.5 Flash 的弃权率仅 39.0%，说明前沿 VLM 仍常在信息不足时给出计划；成果是可审计的弃权 taxonomy 与 6,069 图像／1,250 弃权类别的指令集。

**本轮核查边界**：只读项目页统计与摘要，未下载数据。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboAbstention | 基准 | 具身图像条件下的弃权判断 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 Gemini（VLM 模型）），不再重复解释。

<!-- glossary:end -->
