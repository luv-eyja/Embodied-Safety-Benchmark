# RoboCasa-Shift

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：鲁棒性。
> **分类依据**：已有平台上的阶段鲁棒性测试协议。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：感知 + 长时程控制（阶段感知诊断）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/HaochengWang23/RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 长时程操作阶段鲁棒性 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 |
| 基础平台线索 | RoboCasa、RoboCasa365 |
| 规模线索 | 从 16 个候选任务筛出 4 个干净条件至少成功 12/20 的任务；4 种视觉扰动、3 档强度加干净条件，4×20×13=1,040 rollout。 |
| 执行环境线索 | 长时程操作阶段鲁棒性 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7223122581)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：同样的总成功率下降，是否来自长任务中完全不同阶段的失误？

**评测层级**：长时程操作阶段鲁棒性。

## 2. 怎么构建的

**核心场景与条目**：从 16 个候选任务筛出 4 个干净条件至少成功 12/20 的任务；4 种视觉扰动、3 档强度加干净条件，4×20×13=1,040 rollout。

**实现与判分**：固定初始状态、指令和策略种子作配对，记录子目标及首次失败阶段。另做零变化相机控制，用于量化运行中的非确定性。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026 | 提出 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 | 针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：相机 L2 与模糊 L1 的成功下降同为 0.188，首次阶段失败比例却为 19% 与 36.4%；零变化相机控制仍有 8/80 次结果翻转。

**适用边界**：仅分析 GR00T-N1.5 和干净条件可完成的四个任务，存在明确的筛选边界。零扰动的非确定性必须从扰动效应中区分。

## 5. 相关论文（均来自本调研表）

- [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

仅分析 GR00T-N1.5 和干净条件可完成的四个任务，存在明确的筛选边界。零扰动的非确定性必须从扰动效应中区分。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Haocheng Wang, Youquan Liu, Weiyu Guo, et al., ‘RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation,’ arXiv preprint, 2026, arXiv:2610.27861v1. [论文](https://arxiv.org/abs/2610.27861)；[核查正文](https://arxiv.org/html/2610.27861v1)。

**重点核查位置（章节主题）**：III-A Task Selection；III-C Evaluation；IV-A；IV-B；IV-D。

OpenAlex 被引次数：**[0](https://openalex.org/W7223122581)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/HaochengWang23/RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/HaochengWang23/RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/HaochengWang23/RoboCasa-Shift) | https://raw.githubusercontent.com/HaochengWang23/RoboCasa-Shift/HEAD/README.md | stars 2，license MIT（开源许可证），最后推送 2026-10-22，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/HaochengWang23/RoboCasa-Shift（2 stars，MIT，2026-10-22 推送）README 给 arXiv、代码与 formal evaluation 记录，并说明使用 RoboCasa 官方成功判据与仿真状态里程碑。

**涉及领域**：长时程家庭操作的阶段感知鲁棒性；在 RoboCasa 上施加受控分布偏移。

**测试目的与构建方法**：固定初始状态、指令与策略种子做配对，记录子目标与首次失败阶段；另做“零变化相机”控制实验以量化运行中的非确定性。

**测试缺陷**：只分析 GR00T-N1.5 与“干净条件下可完成”的四个任务，筛选边界明确；零扰动下也有结果翻转，必须从扰动效应中扣除；任务与偏移类型有限。

**与具身智能安全的相关性**：间接：阶段级失效定位对安全诊断有用，但基准评成功与进度，不评违规；可作为安全失效分析的框架。

**用这个 benchmark 测了什么**：相机 L2 与模糊 L1 的成功下降同为 0.188，而首次阶段失败比例分别为 19% 与 36.4%；零变化相机控制仍有 8/80 次结果翻转——说明“同样的分数”背后失效机制不同。

**本轮核查边界**：只读 README，未跑配对评测。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **rollout** | rollout | 展开／推演 | 用当前策略跑一次得到的完整轨迹，常与 episode 混用。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **GR00T** | NVIDIA GR00T N1 / N1.5 | GR00T 机器人基础模型 | NVIDIA 的类人／通用操作基础模型家族，常作为强基线或微调起点。 |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 基准自定义的难度阶梯：常见是 L0 干净、L1 加扰动、L2 更强扰动或结构变化，L3 更难。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **rollout**：rollout 数、episode 数、候选轨迹数三者混用。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboCasa | 基准 | 家庭场景大规模仿真基准 |
| RoboCasa-Shift | 基准 | 长时程操作阶段鲁棒性 |
| RoboCasa365 | 基准 | RoboCasa 的 365 任务版本 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）），不再重复解释。

<!-- glossary:end -->
