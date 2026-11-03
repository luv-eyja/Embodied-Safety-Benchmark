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
| OpenAlex 引用快照 | [23](https://openalex.org/W4320165654)；2026-11-03 |

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
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Jiayuan Gu, Fanbo Xiang, Xuanlin Li, et al., ‘ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills,’ arXiv preprint, 2023, arXiv:2302.04659v1. [论文](https://arxiv.org/abs/2302.04659)；[核查正文](https://arxiv.org/html/2302.04659v1)。

**重点核查位置（章节主题）**：Benchmark Design；Demonstrations；5 Applications；5.1 Sense-plan-act。

OpenAlex 被引次数：**[23](https://openalex.org/W4320165654)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://maniskill2.github.io/](https://maniskill2.github.io/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
