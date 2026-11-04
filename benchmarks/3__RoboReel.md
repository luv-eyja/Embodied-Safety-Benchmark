# RoboReel

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：以视频观察到机器人执行的测试协议为主，附配对数据。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：从观察学习（LfO）  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://roboreel.github.io](https://roboreel.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 从观察学习的操作基准 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 10 个操作任务；真机人类示范视频 + 仿真轨迹 + 评测环境 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 10 项任务包括推块、关抽屉、清空篮子、按按钮、开盖、抓放、收玩具和叠杯；提供人类视频、配对机器人仿真轨迹与多种测试条件。 |
| 执行环境线索 | 从观察学习的操作基准 |
| 来源审计 | [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](https://arxiv.org/abs/2609.08209)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce RoboReel unified benchmark。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7212081197)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：机器人从人类视频学习时，视觉外观、动作对应与精细操作分别构成什么障碍？

**评测层级**：从观察学习的操作基准。

## 2. 怎么构建的

**核心场景与条目**：10 项任务包括推块、关抽屉、清空篮子、按按钮、开盖、抓放、收玩具和叠杯；提供人类视频、配对机器人仿真轨迹与多种测试条件。

**实现与判分**：将人类观察和机器人动作数据对齐，比较视频条件策略与从人体运动提取关键点的策略，并用模拟／实机相对表现检查基准有效性。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](https://arxiv.org/abs/2609.08209) | 2026 | 提出 | 10 个操作任务；真机人类示范视频 + 仿真轨迹 + 评测环境 | 从观察学习是机器人数据规模化的重要途径，但既有方法在假设、硬件与环境设置上差异很大，难以比较。该基准捆绑真机人类示范视频、仿真机器人轨迹与统一评测环境，覆盖 10 个操作任务，为「从人类视频学习操作技能」提供可比的评测底座。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：视频条件 π0.5 在部分长时程条件下更强；Point Policy 可较好完成推块、关抽屉，却更难处理精细抓取。方法差异随技能类型而改变。

**适用边界**：包含配对机器人训练数据的设置不是纯粹从公开视频零样本学会操作；不同数据访问条件必须说明。相对趋势一致不等于模拟绝对成功率等于真机。

## 5. 相关论文（均来自本调研表）

- [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](https://arxiv.org/abs/2609.08209)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

包含配对机器人训练数据的设置不是纯粹从公开视频零样本学会操作；不同数据访问条件必须说明。相对趋势一致不等于模拟绝对成功率等于真机。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Weiwei Gu, Anmol Gupta, Anant Sah, et al., ‘Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation,’ arXiv preprint, 2026, arXiv:2609.08209v4. [论文](https://arxiv.org/abs/2609.08209)；[核查正文](https://arxiv.org/html/2609.08209v4)。

**重点核查位置（章节主题）**：3.2 Dataset；3.3 Tasks；3.4 Evaluation；4.2 Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7212081197)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://roboreel.github.io](https://roboreel.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://roboreel.github.io](https://roboreel.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://roboreel.github.io) | https://roboreel.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://roboreel.github.io 标注 CoRL（会议／期刊） 2026，代码与数据均为“Soon”，并说明“为什么还要另一个基准”。

**涉及领域**：从观察中学习（Learning from Observation）；配对真人视频与仿真机器人轨迹，十个操作任务。

**测试目的与构建方法**：把人类观察与机器人动作数据对齐，比较“视频条件策略”与“从人体运动提取关键点的策略”，并用模拟／实机的相对表现检验基准有效性。

**测试缺陷**：包含配对机器人训练数据的设置不是“从公开视频零样本学会”；不同数据访问条件必须说明；相对趋势一致不代表模拟绝对成功率等于真机；论文被 CoRL 2026 接收，代码与数据标注“Soon”。

**与具身智能安全的相关性**：弱：属能力基准；但“模仿人类视频”本身是安全风险来源（学会了不该学的动作），这一维度未被评测。

**用这个 benchmark 测了什么**：视频条件 π0.5 在部分长时程条件下更强；Point Policy 能较好完成推块、关抽屉，却更难处理精细抓取——方法优劣随技能类型改变。

**本轮核查边界**：代码／数据尚未发布，无法核实实现。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **zero-shot** | zero-shot evaluation | 零样本评测 | 不针对该基准做任何训练或微调，直接拿现成模型跑。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboReel | 基准 | 从观察学习的操作基准 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 CoRL（会议／期刊）），不再重复解释。

<!-- glossary:end -->
