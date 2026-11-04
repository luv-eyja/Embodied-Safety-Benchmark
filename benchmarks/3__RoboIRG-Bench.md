# RoboIRG-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：指代接地和记忆使用能力测试。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：隐式指代接地  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://aernar.github.io/RoboIRGBench](https://aernar.github.io/RoboIRGBench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › Instruction Understanding |
| 应用领域 | 未标注 |
| 被测对象 | 隐式指代与具身记忆 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、失败恢复、任务能力 |
| 评测维度/指标 | 直接 / 推理中介 / 空间 / 语境四类隐式指代 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 基于 RoboMME 的 11 个任务、40 个变体，覆盖直接、推理、空间和上下文指代，并配置显式指令对照。 |
| 执行环境线索 | 隐式指代与具身记忆 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214772858)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：指令没有直接命名目标，而依赖空间关系、先前事件或推理时，机器人能否找到正确对象？

**评测层级**：隐式指代与具身记忆。

## 2. 怎么构建的

**核心场景与条目**：基于 RoboMME 的 11 个任务、40 个变体，覆盖直接、推理、空间和上下文指代，并配置显式指令对照。

**实现与判分**：保持任务、状态和模型底座可比，比较五种基于 π0.5 的记忆／接地配置；每条件三个种子各 50 episode，使用显式与隐式表现差定位问题。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2609.34384) | 2026 | 提出 | 直接 / 推理中介 / 空间 / 语境四类隐式指代 | 既有基准通常假设任务相关信息在指令中被明确给出，而人类常以隐含方式指代物体、数量与关系。该基准把这一能力定义为隐式指代接地（IRG），基于 RoboMME 构建 40 个变体、覆盖 11 个任务与四类挑战，并评测采用不同记忆机制的代表性 VLA 在从语言与感知上下文恢复目标上的表现。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：FrameS 的显式、直接隐式和推理指代成功率分别为 45.82%、29.76%、16.85%；有记忆不等于会利用记忆完成指代推理。

**适用边界**：成绩同时受底层操作能力约束；比较的是特定 π0.5 配置，不是全部模型家族。显式指令对照很重要，不能把所有失败归因于记忆不足。

## 5. 相关论文（均来自本调研表）

- [RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2609.34384)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

成绩同时受底层操作能力约束；比较的是特定 π0.5 配置，不是全部模型家族。显式指令对照很重要，不能把所有失败归因于记忆不足。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Aernaer Akelijiang, Jiannan Li, Zhineng Chen, et al., ‘RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2609.34384v1. [论文](https://arxiv.org/abs/2609.34384)；[核查正文](https://arxiv.org/html/2609.34384v1)。

**重点核查位置（章节主题）**：Benchmark Design；Experimental Setup；Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214772858)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://aernar.github.io/RoboIRGBench](https://aernar.github.io/RoboIRGBench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://aernar.github.io/RoboIRGBench](https://aernar.github.io/RoboIRGBench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://aernar.github.io/RoboIRGBench) | https://aernar.github.io/RoboIRGBench | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://aernar.github.io/RoboIRGBench 给 arXiv 与 Code 入口，并展示“显式接地 + 四种隐式设置”的平均成功对比图。

**涉及领域**：VLA 的隐式指代接地（implicit referential grounding）；目标在指令中被隐去，需要记忆与推理补全。

**测试目的与构建方法**：保持任务、状态与模型底座可比，比较五种基于 π0.5 的记忆／接地配置；每条件三个种子各 50 episode，用“显式 vs 隐式”表现差定位问题。

**测试缺陷**：成绩同时受底层操作能力约束；只比较特定 π0.5 配置，不代表全部模型家族；必须用显式指令对照，否则会把操作失败误判为指代失败。

**与具身智能安全的相关性**：间接：指代错误会直接导致“对错的物体动手”，是语义安全的上游原因；基准不评风险。

**用这个 benchmark 测了什么**：FrameS 的显式、直接隐式与推理指代成功率分别为 45.82%、29.76%、16.85%——有记忆不等于会用记忆做指代推理。

**本轮核查边界**：只读项目页，未进入代码。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 5 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboIRG-Bench | 基准 | 隐式指代与具身记忆 |

<!-- glossary:end -->
