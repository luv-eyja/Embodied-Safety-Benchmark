# BiDex-100

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：统一双手任务与能力轴评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：双手灵巧操作 106 任务  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://robbyant-research.github.io/BiDex-100](https://robbyant-research.github.io/BiDex-100)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 双手灵巧操作仿真 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 5 条能力轴：泛化、指令遵循、少示范、长时程、记忆；每任务配域外变体 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 名称虽为 100，正文包含 106 任务；两种本体、8,080 条成功核验示范、约 625 万帧，按五条能力轴组织。 |
| 执行环境线索 | 双手灵巧操作仿真 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7223068191)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：通用 VLA 在高自由度双手操作中，泛化、指令遵循、少样本、长时程和记忆能力分别如何？

**评测层级**：双手灵巧操作仿真。

## 2. 怎么构建的

**核心场景与条目**：名称虽为 100，正文包含 106 任务；两种本体、8,080 条成功核验示范、约 625 万帧，按五条能力轴组织。

**实现与判分**：声明式配置对象、区域、关节和目标，使用逻辑完成条件与阶段进度；用匹配的随机种子构造 ID/OOD，每任务两种种子各 25 episode。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459) | 2026 | 提出 | 5 条能力轴：泛化、指令遵循、少示范、长时程、记忆；每任务配域外变体 | 现有工作很少有针对灵巧操作专门设计的基准，导致模型的灵巧操作能力刻画不足。BiDex-100 是双手灵巧操作的仿真基准，兼顾任务覆盖广度、多维评测与高自由度手部本体：含 106 个任务，沿泛化、指令遵循、少示范、长时程、记忆五条能力轴组织；每个任务配一个含受控视觉与空间变化的域外变体，用于系统评估分布外表现。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：LingBot-VLA-v2 的 ID 总成功率为 52.21%，OOD 为 1.68%；GR00T-N1.7 的 OOD 总成功率为 5.45%。多任务成功与域外泛化差距巨大。

**适用边界**：结果对应文中本体、训练设置及组合变化；进度分数和全部完成率不同。不可把模型家族结论推广至未测 checkpoint。

## 5. 相关论文（均来自本调研表）

- [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

结果对应文中本体、训练设置及组合变化；进度分数和全部完成率不同。不可把模型家族结论推广至未测 checkpoint。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Yong Wang, Kecheng Zheng, Xing Zhu, et al., ‘BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks,’ arXiv preprint, 2026, arXiv:2610.25459v2. [论文](https://arxiv.org/abs/2610.25459)；[核查正文](https://arxiv.org/html/2610.25459v2)。

**重点核查位置（章节主题）**：Benchmark Design；Evaluation Protocol；V-C Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7223068191)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://robbyant-research.github.io/BiDex-100](https://robbyant-research.github.io/BiDex-100)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
