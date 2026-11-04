# MemForm

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；软件代理邻接研究；目标：安全。
> **分类依据**：控制记忆接口的安全诊断集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：记忆形成投毒  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/opanhw/memform-code](https://github.com/opanhw/memform-code)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | MemForm: Benchmarking Memory Formation Poisoning in LLM Agents |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Memory |
| 应用领域 | 记忆投毒 |
| 被测对象 | 代理记忆可靠性诊断；邻接参考 |
| 历史关键词标签（未重新统计） | 对抗/后门安全 |
| 评测维度/指标 | 五类形成接口：内容、证据、范围、选择、路径投毒 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | Content、Evidence、Scope、Selection、Path 五个记忆接口；六种 LLM、两种回答格式，在正常／受影响条件下对照。 |
| 执行环境线索 | 代理记忆可靠性诊断；邻接参考 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221777130)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 2 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：长期记忆形成过程中，经验内容、证据、适用范围、保留选择和整合次序会怎样影响后续行为？

**评测层级**：代理记忆可靠性诊断；邻接参考。

## 2. 怎么构建的

**核心场景与条目**：Content、Evidence、Scope、Selection、Path 五个记忆接口；六种 LLM、两种回答格式，在正常／受影响条件下对照。

**实现与判分**：对同一语义任务家族构造受控配对，分开检查形成的记忆与后续行为；只在满足正常条件要求的 eligible query 上统计风险目标达成率。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [MemForm: Benchmarking Memory Formation Poisoning in LLM Agents](https://arxiv.org/abs/2610.14431) | 2026 | 提出 | 五类形成接口：内容、证据、范围、选择、路径投毒 | 指出长期记忆让 LLM 智能体能从过去交互中学习，但也使「记忆形成」暴露于对抗影响之下；既有研究多按攻击通道、破坏模式或生命周期阶段组织记忆投毒，对形成接口刻画不足。MemForm 把记忆形成投毒形式化为对持久记忆产出与提交接口的对抗操纵，并引入「选择投毒」与「路径投毒」作为隔离保持与巩固环节的受控干预类别。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：主实现中，选择题格式的描述性宏平均风险达成率范围为 35.2–84.0%，自由回答为 49.0–87.1%；即使保留经历相同，整合次序仍可能改变行为。

**适用边界**：各模型 eligible 子集不同，因此这些范围不是相同测试分布上的直接安全排名；这是记忆机制诊断，不是物理机器人执行评测。

## 5. 相关论文（均来自本调研表）

- [MemForm: Benchmarking Memory Formation Poisoning in LLM Agents](https://arxiv.org/abs/2610.14431)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

各模型 eligible 子集不同，因此这些范围不是相同测试分布上的直接安全排名；这是记忆机制诊断，不是物理机器人执行评测。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Haowen Pan, Pengyang Shao, Yunshan Ma, et al., ‘MemForm: Benchmarking Memory Formation Poisoning in LLM Agents,’ arXiv preprint, 2026, arXiv:2610.14431v1. [论文](https://arxiv.org/abs/2610.14431)；[核查正文](https://arxiv.org/html/2610.14431v1)。

**重点核查位置（章节主题）**：3.1 Definition and Scope；4.1 Construction；4.3 Protocol；5.2 Overall Results；5.5 Limitations。

OpenAlex 被引次数：**[0](https://openalex.org/W7221777130)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/opanhw/memform-code](https://github.com/opanhw/memform-code)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/opanhw/memform-code](https://github.com/opanhw/memform-code)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/opanhw/memform-code) | https://raw.githubusercontent.com/opanhw/memform-code/HEAD/README.md | stars 1，license MIT（开源许可证），最后推送 2026-09-22，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/opanhw/memform-code（1 star，MIT，2026-09-22 推送）自述为 evaluation release，强调“Every item is a paired intervention”。

**涉及领域**：LLM 代理的持久记忆投毒；配对干预下的记忆形成与下游行为。

**测试目的与构建方法**：对同一语义任务家族构造受控配对，只改变记忆构建环节，固定下游触发、动作空间与家族语义；分开检查形成的记忆与后续行为，只在满足正常条件的 eligible query 上统计风险目标达成率。

**测试缺陷**：各模型的 eligible 子集不同，不是同一测试分布上的安全排名；这是记忆机制诊断，不是物理机器人执行；配对项由人工构造，覆盖的记忆表面有限。

**与具身智能安全的相关性**：邻接：具身代理的长期记忆一旦被污染，会在后续任务中持续产生错误决策。它测的是“记忆这一层的完整性”，可为具身代理的平台安全提供接口级证据。

**用这个 benchmark 测了什么**：主实现中，选择题格式的描述性宏平均风险达成率 35.2–84.0%，自由回答 49.0–87.1%；即使经历相同，整合次序仍可能改变行为。

**本轮核查边界**：只读 README 的定位与方法说明，未跑配对实验。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 2 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| MemForm | 基准 | 代理记忆可靠性诊断；邻接参考 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）），不再重复解释。

<!-- glossary:end -->
