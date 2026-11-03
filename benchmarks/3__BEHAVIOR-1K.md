# BEHAVIOR-1K

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：活动需求、任务定义和评测为主，OmniGibson 是配套平台。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：家务长时程活动  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 0、使用 1；方法参考另标）
> **证据级别**：原表 C；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://behavior.stanford.edu/](https://behavior.stanford.edu/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 家庭活动仿真平台与任务集 |
| 历史关键词标签（未重新统计） | 语义/指令安全、失败恢复、任务能力 |
| 评测维度/指标 | 21 类技能 / 417 子任务 / 137,899 片段；技能级诊断 |
| 基础平台线索 | BEHAVIOR-1K |
| 规模线索 | 1,000 种活动、50 个场景、9,000 余对象；任务取自人类需求调查，包含整理、清洁、烹饪等，超越单次抓放。 |
| 执行环境线索 | 家庭活动仿真平台与任务集 |
| 来源审计 | [BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation](https://arxiv.org/abs/2403.09227)；external_original_paper |
| 来源核验依据 | ManiUnit 论文明确说明其数据与 benchmark built from 50 BEHAVIOR-1K activities；BEHAVIOR-1K 原始论文不在当前 192 条本库记录中。 |
| OpenAlex 引用快照 | [6](https://openalex.org/W4392872989)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：机器人能否完成对人有实际价值、涉及复杂状态变化的长时程家庭活动？

**评测层级**：家庭活动仿真平台与任务集。

## 2. 怎么构建的

**核心场景与条目**：1,000 种活动、50 个场景、9,000 余对象；任务取自人类需求调查，包含整理、清洁、烹饪等，超越单次抓放。

**实现与判分**：BDDL 用逻辑关系描述初态与目标；OmniGibson 支持刚体、软体、液体及热／烹饪状态等，结合技能式执行器和活动完成检查。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks](https://arxiv.org/abs/2610.12089) | 2026 | 使用 | 21 类技能 / 417 子任务 / 137,899 片段；技能级诊断 | 长时程移动操作要求机器人按单条自然语言指令跨房间导航并连续执行多个操作技能，评测上有三个难点：同一指令下相似观测使技能选择歧义；前序技能虽成功，但继承的机器人状态可能偏离下一技能的示范起点；任务级指标无法做技能级诊断，且早期失败会让后续技能根本没被测到。ManiUnit 基于 BEHAVIOR-1K 的 50 个活动构建数据集（21 类技能、417 个子任务、137,899 个片段）与相应基准。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文给出多种仿真解法，并在 CollectTrash 的真实 Tiago 与公寓孪生中分析迁移；真实抓取和感知误差是重要落差来源。成果是需求驱动的活动库、资产和仿真器。

**适用边界**：本次读的是 arXiv:2403.09227 的扩展论文；后续 ManiUnit 等使用的任务子集不能当成原始全集。某些基线使用抽象抓取，不能与全低层控制直接比较。

## 5. 相关论文（均来自本调研表）

- [ManiUnit: A Manipulation Skill Dataset and Benchmark for Long-Horizon Tasks](https://arxiv.org/abs/2610.12089)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

本次读的是 arXiv:2403.09227 的扩展论文；后续 ManiUnit 等使用的任务子集不能当成原始全集。某些基线使用抽象抓取，不能与全低层控制直接比较。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Chengshu Li, Ruohan Zhang, Josiah Wong, et al., ‘BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation,’ arXiv preprint, 2024, arXiv:2403.09227v1. [论文](https://arxiv.org/abs/2403.09227)；[核查正文](https://arxiv.org/html/2403.09227v1)。

**重点核查位置（章节主题）**：4 Dataset；5 OmniGibson；6.1 Evaluating Solutions；6.2 Real Robot。

OpenAlex 被引次数：**[6](https://openalex.org/W4392872989)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://behavior.stanford.edu/](https://behavior.stanford.edu/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
