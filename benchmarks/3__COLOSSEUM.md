# COLOSSEUM

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：鲁棒性。
> **分类依据**：受控环境变化下的操作泛化基准。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：感知（泛化边界）  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://robot-colosseum.github.io](https://robot-colosseum.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 仿真环境泛化与鲁棒性 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 20 个任务、14 条扰动轴；单轴和组合扰动成功率 |
| 基础平台线索 | RLBench / CoppeliaSim |
| 规模线索 | 基于 RLBench／CoppeliaSim 的 20 个任务、14 条扰动轴，包含目标与容器颜色／纹理／大小、背景、照明、干扰物、物理和相机变化。 |
| 执行环境线索 | 仿真环境泛化与鲁棒性 |
| OpenAlex 引用快照 | [29](https://openalex.org/W4402354166)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：操作策略对训练环境以外的外观、几何与物理变化究竟有多脆弱？

**评测层级**：仿真环境泛化与鲁棒性。

## 2. 怎么构建的

**核心场景与条目**：基于 RLBench／CoppeliaSim 的 20 个任务、14 条扰动轴，包含目标与容器颜色／纹理／大小、背景、照明、干扰物、物理和相机变化。

**实现与判分**：分别施加单轴与组合扰动，以相同任务目标评价策略；比较五种操作方法，并在四项真实桌面任务检查模拟趋势。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191) | 2024 | 提出 | 20 个任务、14 条扰动轴；单轴和组合扰动成功率 | 基于 RLBench／CoppeliaSim 的 20 个任务、14 条扰动轴，包含目标与容器颜色／纹理／大小、背景、照明、干扰物、物理和相机变化。论文报告常见变化造成约 30–50% 性能退化，组合变化可达至少 75% 的相对退化。成果是系统扰动集与跨策略诊断。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文报告常见变化造成约 30–50% 性能退化，组合变化可达至少 75% 的相对退化。成果是系统扰动集与跨策略诊断。

**适用边界**：原底座不是 LIBERO。相对退化不能改写成成功率下降同等百分点；模拟／实机和不同扰动组合应分别报告。

## 5. 相关论文（均来自本调研表）

- [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191)（2024；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

原底座不是 LIBERO。相对退化不能改写成成功率下降同等百分点；模拟／实机和不同扰动组合应分别报告。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Wilbert Pumacay, Ishika Singh, Jiafei Duan, et al., ‘THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation,’ arXiv preprint, 2024, arXiv:2402.08191v2. [论文](https://arxiv.org/abs/2402.08191)；[核查正文](https://arxiv.org/html/2402.08191v2)。

**重点核查位置（章节主题）**：III-A Benchmark；III-B Perturbations；III-C Evaluation；IV Experiments。

OpenAlex 被引次数：**[29](https://openalex.org/W4402354166)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://robot-colosseum.github.io](https://robot-colosseum.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **29** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 10 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://robot-colosseum.github.io](https://robot-colosseum.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://robot-colosseum.github.io) | https://robot-colosseum.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://robot-colosseum.github.io 提供 ArXiv、Code、Real World Setup、Leaderboard 与 Dataset 入口（RSS（会议／期刊） 2024）。

**涉及领域**：机械臂操作的泛化评测；在 RLBench／CoppeliaSim 上施加系统扰动。

**测试目的与构建方法**：分别施加单轴与组合扰动（纹理、光照、相机位姿、桌面颜色、干扰物等），用相同任务目标评价策略；比较五种操作方法，并在四项真实桌面任务检查模拟趋势。

**测试缺陷**：原底座不是 LIBERO；相对退化不能改写成成功率下降同等百分点；模拟与实机、不同扰动组合须分别报告；扰动轴之间可能交互，单轴结果不能线性外推。

**与具身智能安全的相关性**：中等：扰动鲁棒性是安全的前置条件（分布变化下的失效常导致事故），但基准评的是成功率退化，不含风险约束或伤害度量。

**用这个 benchmark 测了什么**：论文报告常见变化造成约 30–50% 性能退化，组合变化可达至少 75% 相对退化；2026 年 Colosseum V2 扩展到 VLA 泛化评测；引文含多篇 VLA 与多模态综述。

**本轮核查边界**：只读项目页导航，未核对 Leaderboard 数值或数据集许可。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robot M…（2025） | DynaRend（3D 动态表征学习） | 训练后评测（跨基准 + 真机） | RLBench 与 Colosseum 两套泛化基准，另做真实机器人实验 | 称在策略成功率与对环境的泛化上有显著提升 |
| Hyperbolic Multiview Pretraining for Robotic Manipulation（2026） | HyperMVP（双曲空间多视角预训练） | 预训练后评测（含扰动设置） | COLOSSEUM（多扰动）、RLBench 与真实场景 | 称在不同任务与扰动设置下一致优于强基线 |
| FOCI Policy: Focus on Object-Centric Interactions for Relational Manip…（2026） | FOCI Policy（物体中心交互） | 训练后评测（数据效率对比） | RLBench、COLOSSEUM 与真实任务，比较训练数据量 | 以明显更少的训练数据达到强性能（摘要无具体数值） |
| Robust Industrial Manipulation Under Test-Time Perturbations（2026） | 固定相机的 Franka Panda 工作单元策略 | 评测（工业场景扰动测试） | 在 RLBench 与 Colosseum 上做测试时扰动评估 | 研究测试时扰动下的鲁棒性，摘要未给数值 |
| Colosseum V2: Benchmarking Generalization for Vision-Language-Action（2026） | VLA（作为被测对象） | 派生新版本基准（不是使用者，而是升级者） | 面向 VLA 泛化的大规模仿真基准 | 产出的是 V2 基准；原 COLOSSEUM 是其前身 |

**原文片段（摘要）**：

- DynaRend: Learning 3D Dynamics via Masked Future Rendering f…（2025，arXiv）：> We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum
- Hyperbolic Multiview Pretraining for Robotic Manipulation（2026，arXiv）：> We evaluate HyperMVP on COLOSSEUM, RLBench, and real-world scenarios
- FOCI Policy: Focus on Object-Centric Interactions for Relati…（2026，arXiv）：> Experiments on RLBench, COLOSSEUM, and real-world tasks show … with substantially less training data
- Robust Industrial Manipulation Under Test-Time Perturbations（2026，OpenAlex 引文）：> This paper studies this problem in a fixedcamera Franka Panda workcell using RLBench and Colosseum
- Colosseum V2: Benchmarking Generalization for Vision-Languag…（2026，arXiv）：> we introduce Colosseum V2, a large-scale simulation benchmark for evaluating VLA generalization

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 4 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **RLBench** | RLBench | RLBench 操作基准环境 | CoppeliaSim 上的机械臂任务集，常作泛化评测的底座。 |
| **CoppeliaSim** | CoppeliaSim (V-REP) | CoppeliaSim 仿真器 | 通用机器人仿真器，RLBench 的物理后端。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| COLOSSEUM | 基准 | 系统扰动的操作泛化基准 |
| RLBench | 基准 | CoppeliaSim 上的机械臂任务集 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 RSS（会议／期刊）），不再重复解释。

<!-- glossary:end -->
