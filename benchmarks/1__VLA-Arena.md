# VLA-Arena

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性、安全。
> **分类依据**：多维统一任务集，安全仅是其中明确的一维。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：四维任务结构的难度梯度（含 Safety 套件）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://vla-arena.github.io](https://vla-arena.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 仿真多维 VLA 诊断 |
| 历史关键词标签（未重新统计） | 语义/指令安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 三轴结构化难度（任务结构 / 语言指令 W0–W4 / 视觉观测 V0–V4）；11 个任务套件、170 个任务 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 170 个任务、11 套件、Safety／Distractor／Extrapolation／Long-Horizon 四维；任务难度 L0–L2，另设语言和视觉扰动等级。 |
| 执行环境线索 | 仿真多维 VLA 诊断 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7117763818)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何同时区分安全、干扰、外推和长时程能力，而不让一个平均成功率掩盖短板？

**评测层级**：仿真多维 VLA 诊断。

## 2. 怎么构建的

**核心场景与条目**：170 个任务、11 套件、Safety／Distractor／Extrapolation／Long-Horizon 四维；任务难度 L0–L2，另设语言和视觉扰动等级。

**实现与判分**：扩展约束式 BDDL，提供不同规模示范集；仅在 L0 训练，向 L1／L2 评估，并对任务结构、语言、视觉变化分别计分。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539) | 2025 | 提出 | 三轴结构化难度（任务结构 / 语言指令 W0–W4 / 视觉观测 V0–V4）；11 个任务套件、170 个任务 | 以结构化任务设计框架量化难度：任务结构维度含 Safety、Distractor、Extrapolation、Long Horizon 四个维度共 11 个套件 170 个任务，每个套件分 L0–L2 三级而微调只允许用 L0，以严格测泛化；语言与视觉扰动可作为任意任务上的诊断探针，区分稳健接地与表层模式匹配。评测主流 VLA 后发现记忆优于泛化、视觉感知流于表面、忽视安全约束，且 L0–L2 间出现模型排名反转，说明各难度级提供非冗余信息。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：不同诊断维度会改变模型相对排序；基准同时报告完成和安全代价，并配有真机案例检查。成果是共享任务表示、难度体系和数据。

**适用边界**：难度、扰动和训练预算应分开报告；较高 SR 不自动意味着约束代价更低，局部真机结果也不能覆盖全部 170 个任务。

## 5. 相关论文（均来自本调研表）

- [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

难度、扰动和训练预算应分开报告；较高 SR 不自动意味着约束代价更低，局部真机结果也不能覆盖全部 170 个任务。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Borong Zhang, Jiahao Li, Jiachen Shen, et al., ‘VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models,’ arXiv preprint, 2025, arXiv:2512.22539v4. [论文](https://arxiv.org/abs/2512.22539)；[核查正文](https://arxiv.org/html/2512.22539v4)。

**重点核查位置（章节主题）**：2 Benchmark Design；3 Dataset；4 Experiments；5 Real-world Evaluation。

OpenAlex 被引次数：**[0](https://openalex.org/W7117763818)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://vla-arena.github.io](https://vla-arena.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
