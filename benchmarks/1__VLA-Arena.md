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
| OpenAlex 引用快照 | [0](https://openalex.org/W7117763818)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 8 个缩写／技术词，并标出 6 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Borong Zhang, Jiahao Li, Jiachen Shen, et al., ‘VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models,’ arXiv preprint, 2025, arXiv:2512.22539v4. [论文](https://arxiv.org/abs/2512.22539)；[核查正文](https://arxiv.org/html/2512.22539v4)。

**重点核查位置（章节主题）**：2 Benchmark Design；3 Dataset；4 Experiments；5 Real-world Evaluation。

OpenAlex 被引次数：**[0](https://openalex.org/W7117763818)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://vla-arena.github.io](https://vla-arena.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 6 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://vla-arena.github.io](https://vla-arena.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://vla-arena.github.io) | https://vla-arena.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://vla-arena.github.io 含模型排行榜、任务商店与开源框架入口，作者为北大 AI 研究院团队。

**涉及领域**：VLA 的分难度基准；170 个任务、L0–L2 三档，覆盖 Safety、Distractor、Extrapolation、Long Horizon 四类。

**测试目的与构建方法**：扩展约束式 BDDL，提供不同规模示范集；仅在 L0 训练、向 L1／L2 评估，并对任务结构、语言与视觉变化分别计分；同时报告完成与安全代价。

**测试缺陷**：难度、扰动与训练预算必须分开报告；较高 SR 不自动意味着约束代价更低；局部真机结果不能覆盖全部 170 个任务；Safety 只是四类之一。

**与具身智能安全的相关性**：直接（部分）：Safety 类任务显式包含约束违反，是本库中“能力 + 安全”同表报告的少数基准；其余三类是能力／鲁棒性。

**用这个 benchmark 测了什么**：不同诊断维度会改变模型相对排序；下游 FreqFM、LoopVLA、ActionPiece 等在 VLA-Arena 上报告结果（如 FreqFM 在 VLA-Arena L0–L2 达 51.5%）；ICML（会议／期刊） 2026。

**本轮核查边界**：只读项目页与排行榜入口，未进入任务商店。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **4 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| ActionPiece: Rethinking Action Tokenization for Autoregressive Vision-…（2026） | ActionPiece + Qwen3-VL（VLM 模型）-4B 策略 | 训练后评测（同一训练设置下对比） | VLA-Arena L0–L2 平均，另报 LIBERO／LIBERO-Plus／SimplerEnv | VLA-Arena L0–L2 51.5%；LIBERO 94.8%、未见 LIBERO-Plus 68.8%、SimplerEnv 71.9% |
| StellaVLA: In-Context Structured Demonstration for Generalizable Visio…（2026） | StellaVLA，对照 π0.5 与 LingBot-VLA | 评测（官方 leaderboard 提交） | VLA-Arena leaderboard（2026-08-01），总分 | 总分 0.63 排名第一，π0.5 为 0.44、LingBot-VLA 为 0.22；LIBERO 上 98.8% |
| Learning from Runtime Feedback through Failure-Bank Self-Evolution（2026） | FailBank（运行期失败库自进化），在两种 VLA 主干上 | 评测（跨两种难度、两种主干） | VLA-Arena 两个难度层级 × 两个 VLA backbone | 摘要只说明评测设置，未给数值 |
| Frequency-Conditioned Flow Matching for Vision-Language-Action Models（2026） | FreqFM（频域条件流匹配，插入既有 Flow Matching 动作专家） | 训练后评测（与 LIBERO／LIBERO-Plus 并列报告） | VLA-Arena、LIBERO、LIBERO-Plus 三套 | 三套上一致提升，其中 LIBERO-Plus +9.3 个点；另在六个真机任务验证 |

**原文片段（摘要）**：

- ActionPiece: Rethinking Action Tokenization for Autoregressi…（2026，arXiv）：> additional evaluations reaching 71.9% on SimplerEnv and 51.5% across VLA-Arena L0-L2
- StellaVLA: In-Context Structured Demonstration for Generaliz…（2026，arXiv）：> On the VLA-Arena leaderboard, StellaVLA ranks first with an overall score of 0.63
- Learning from Runtime Feedback through Failure-Bank Self-Evo…（2026，arXiv）：> We evaluate FailBank on the VLA-Arena benchmark across two difficulty levels and two VLA backbones
- Frequency-Conditioned Flow Matching for Vision-Language-Acti…（2026，arXiv）：> Across LIBERO, LIBERO-Plus, and VLA-Arena, FreqFM consistently improves performance

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 8 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 基准自定义的难度阶梯：常见是 L0 干净、L1 加扰动、L2 更强扰动或结构变化，L3 更难。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **leaderboard** | leaderboard | 排行榜 | 公开提交与排名的榜单，反映社区参与度，不等于论文引用。 |
| **BDDL** | Behavior Domain Definition Language | 行为域定义语言 | 用符号逻辑描述任务初态、目标与物体关系的任务定义语言。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| VLA-Arena | 基准 | 分难度的 VLA 基准与榜单 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| LIBERO-Plus | 基准 | LIBERO 的扰动扩展 |
| SimplerEnv | 基准 | 真实策略的仿真代理评测 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 ICML（会议／期刊）、Qwen3-VL（VLM 模型）），不再重复解释。

<!-- glossary:end -->
