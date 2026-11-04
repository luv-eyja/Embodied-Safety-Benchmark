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
| OpenAlex 引用快照 | [0](https://openalex.org/W7206171071)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 1 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Yosel Delgado, José G. Buenaventura-Carreón, Floris Erich, et al., ‘Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion,’ arXiv preprint, 2026, arXiv:2609.00906v1. [论文](https://arxiv.org/abs/2609.00906)；[核查正文](https://arxiv.org/html/2609.00906v1)。

**重点核查位置（章节主题）**：III Benchmark Design；IV-A Shape Generalization；IV-B Tolerance-dependent Insertion；V Scenario Generator。

OpenAlex 被引次数：**[0](https://openalex.org/W7206171071)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/aistairc/peg-in-bench](https://github.com/aistairc/peg-in-bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/aistairc/peg-in-bench](https://github.com/aistairc/peg-in-bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/aistairc/peg-in-bench) | https://raw.githubusercontent.com/aistairc/peg-in-bench/HEAD/README.md | stars 0，最后推送 2026-08-31，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/aistairc/peg-in-bench（0 stars，2026-08-31 推送）为“Scenario Generator”，README 说明由 NEDO（机构） JPNP25015 项目支持，生成随机但可复现的装配场景。

**涉及领域**：高精度轴孔装配（peg-in-hole）；模块化实体件 + 场景生成器，面向机器人与人类装配能力对比。

**测试目的与构建方法**：提供 STL 文件与场景生成器，输出标准化配置与机器可读任务描述，在固定物理条件下控制几何、公差与方位因素。

**测试缺陷**：材料、打印精度、公差测量与机器人接触控制都会影响复现；提供场景生成器不等于已用所有几何／公差组合验证；本轮未发现可作为统一排行榜的大规模成功率对照。

**与具身智能安全的相关性**：间接：装配接触是力相关风险场景，但基准关注装配成功与可靠性，没有损伤或过载判罚；实体件反而便于做真实接触测试。

**用这个 benchmark 测了什么**：成果是低门槛的模块化实体件与任务规范；未发现可引用的统一模型排行榜，因此不对代表分数作猜测。

**本轮核查边界**：仓库只有场景生成器，评测结果需回到论文；未打印实体件。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 1 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| Peg-in-Bench | 基准 | 可打印物理插接基准设计 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 NEDO（机构）），不再重复解释。

<!-- glossary:end -->
