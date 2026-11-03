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
| OpenAlex 引用快照 | [0](https://openalex.org/W7212081197)；2026-11-03 |

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
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Weiwei Gu, Anmol Gupta, Anant Sah, et al., ‘Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation,’ arXiv preprint, 2026, arXiv:2609.08209v4. [论文](https://arxiv.org/abs/2609.08209)；[核查正文](https://arxiv.org/html/2609.08209v4)。

**重点核查位置（章节主题）**：3.2 Dataset；3.3 Tasks；3.4 Evaluation；4.2 Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7212081197)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://roboreel.github.io](https://roboreel.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
