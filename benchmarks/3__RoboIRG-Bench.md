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
| OpenAlex 引用快照 | [0](https://openalex.org/W7214772858)；2026-11-03 |

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
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Aernaer Akelijiang, Jiannan Li, Zhineng Chen, et al., ‘RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2609.34384v1. [论文](https://arxiv.org/abs/2609.34384)；[核查正文](https://arxiv.org/html/2609.34384v1)。

**重点核查位置（章节主题）**：Benchmark Design；Experimental Setup；Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214772858)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://aernar.github.io/RoboIRGBench](https://aernar.github.io/RoboIRGBench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
