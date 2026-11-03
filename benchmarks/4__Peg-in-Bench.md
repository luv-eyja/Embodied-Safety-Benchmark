# Peg-in-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：实体评测件与场景定义，而非已完成所有条件的实证榜单。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：高精度插入  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/aistairc/peg-in-bench](https://github.com/aistairc/peg-in-bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 精密装配 |
| 被测对象 | 可打印物理插接基准设计 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 可 3D 打印模块；多轴几何、多公差等级；可配置基座 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 五种插销形状、不同配合间隙、模块化底座和孔件；从单插销到多步装配，独立变化目标位置、方向与任务组合。 |
| 执行环境线索 | 可打印物理插接基准设计 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7206171071)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何用可复用的实体零件，系统测量高精度插入对几何、公差和布局变化的泛化？

**评测层级**：可打印物理插接基准设计。

## 2. 怎么构建的

**核心场景与条目**：五种插销形状、不同配合间隙、模块化底座和孔件；从单插销到多步装配，独立变化目标位置、方向与任务组合。

**实现与判分**：提供 STL 文件与场景生成器，输出标准化配置及机器可读任务描述；在固定物理条件下控制几何和空间因素。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion](https://arxiv.org/abs/2609.00906) | 2026 | 提出 | 可 3D 打印模块；多轴几何、多公差等级；可配置基座 | 指出高精度插入因严格对中要求与接触密集交互而困难，虽然 peg-in-hole 被广泛用于评测，但现有基准多依赖固定任务配置，无法评估跨插入场景的鲁棒性与泛化。该基准由完全可 3D 打印的模块化组件构成，含多种轴几何、公差等级与可配置基座结构，可组合出不同难度的插入场景。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：主要成果是低门槛的模块化实体件与任务规范。本次正文核查未发现可作为统一模型排行榜的大规模成功率对照，因此不填造一个代表分数。

**适用边界**：材料、打印精度、公差测量和机器人接触控制都会影响复现。提供场景生成器并不等于论文已验证所有几何／公差组合。

## 5. 相关论文（均来自本调研表）

- [Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion](https://arxiv.org/abs/2609.00906)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

材料、打印精度、公差测量和机器人接触控制都会影响复现。提供场景生成器并不等于论文已验证所有几何／公差组合。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Yosel Delgado, José G. Buenaventura-Carreón, Floris Erich, et al., ‘Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion,’ arXiv preprint, 2026, arXiv:2609.00906v1. [论文](https://arxiv.org/abs/2609.00906)；[核查正文](https://arxiv.org/html/2609.00906v1)。

**重点核查位置（章节主题）**：III Benchmark Design；IV-A Shape Generalization；IV-B Tolerance-dependent Insertion；V Scenario Generator。

OpenAlex 被引次数：**[0](https://openalex.org/W7206171071)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/aistairc/peg-in-bench](https://github.com/aistairc/peg-in-bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
