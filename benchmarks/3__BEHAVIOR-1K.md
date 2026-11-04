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
| OpenAlex 引用快照 | [7](https://openalex.org/W4392872989)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 7 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Chengshu Li, Ruohan Zhang, Josiah Wong, et al., ‘BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation,’ arXiv preprint, 2024, arXiv:2403.09227v1. [论文](https://arxiv.org/abs/2403.09227)；[核查正文](https://arxiv.org/html/2403.09227v1)。

**重点核查位置（章节主题）**：4 Dataset；5 OmniGibson；6.1 Evaluating Solutions；6.2 Real Robot。

OpenAlex 被引次数：**[7](https://openalex.org/W4392872989)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://behavior.stanford.edu/](https://behavior.stanford.edu/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **7** 篇引文论文（清单保留被引最高的 7 篇）；arXiv 摘要命中 25 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://behavior.stanford.edu/](https://behavior.stanford.edu/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://behavior.stanford.edu/) | https://behavior.stanford.edu/ | 保留文本 2197 字符（截断） |

**项目页显示**：项目页 https://behavior.stanford.edu/ 为文档站：给 Getting Started、源码入口（StanfordVL/BEHAVIOR-1K）与 2026 Challenge 信息，强调“第一个基于真实人类需求的仿真基准”。

**涉及领域**：家庭长时程移动操作；1,000 项基于人类需求调查的日常活动，仿真 + OmniGibson。

**测试目的与构建方法**：先用问卷确定“人真正希望机器人代劳”的活动，再用 BDDL 逻辑描述初态与目标，在 OmniGibson 中支持刚体、软体、液体与热／烹饪状态，按活动完成检查评分。

**测试缺陷**：部分基线使用抽象抓取，不能与全低层控制直接比较；任务极长导致失败归因困难；资产与仿真开销大，复现门槛高；后续工作使用的任务子集不等于原始全集。

**与具身智能安全的相关性**：间接：长时程家务是事故高发场景，但基准评的是完成度而非风险；可用其状态谓词扩展出安全约束，原始协议不含违规判罚。

**用这个 benchmark 测了什么**：论文给出多种仿真解法，并在 CollectTrash 上用真实 Tiago 与公寓孪生分析 sim-to-real 落差；2026 年有工作在此基准上研究“语义交接失败”（skill 交接状态不可用）；25 篇 arXiv 摘要命中含多篇长时程编排研究。

**本轮核查边界**：只读文档站首页，未核对资产下载与许可证条款。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **6 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge（2025） | openpi（π 系列开源实现）竞赛方案 | 评测（竞赛提交） | 2025 BEHAVIOR Challenge 的长时程家务移动操作任务 | 摘要只交代任务性质与方案背景，未给分数 |
| Foresight: Failure Detection for Long-Horizon Robotic Manipulation（2026） | Foresight（失败检测器），配多种 SOTA VLA 策略 | 评测（失败检测任务，与 SOTA 检测方法对比） | 仿真中的 LIBERO-Long、ManiSkill-Long 与 BEHAVIOR-1K，另做真机验证 | 摘要称与 SOTA 失败检测方法对比并有真机验证，未给具体数值 |
| MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizo…（2026） | MobiAgent（双环递归自改进） | 训练后评测（含真机） | RoboCasa 与 BEHAVIOR-1K，另加真实任务 | 摘要称三处均验证有效，未给具体数值 |
| BEHAVIOR-Spatial Benchmark: Evaluating Spatial Understanding for Embod…（2026） | VLM 与 VLA（作为被测对象） | 派生子基准（建立在 BEHAVIOR-1K 之上） | 新增空间问答、点目标接地与机器人动作三类任务，检验 VLM 空间理解与 VLA 行为的关系 | 产出的是新基准，不是 BEHAVIOR-1K 上的分数 |
| Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Lang…（2026） | agent-orchestrated VLA 执行框架 | 诊断（在基准上做失效分析） | BEHAVIOR-1K 的技能交接状态（semantic handoff） | 提出并诊断“上一个技能结束时状态不可用于下一个技能”的失败模式 |
| SSC: A Verifiable Structured Representation for Bimanual Manipulation（2026） | —（方法论文，把它的标注格式当参照） | 仅批评／参照其数据格式 | BEHAVIOR-1K 的 skill_annotation 模板 | 认为该模板“语言上过度切分”，影响可读性与标注一致性 |

**原文片段（摘要）**：

- Openpi Comet: Competition Solution For 2025 BEHAVIOR Challen…（2025，arXiv）：> BEHAVIOR-1K focuses on everyday household tasks … long-horizon mobile manipulation challenges
- Foresight: Failure Detection for Long-Horizon Robotic Manipu…（2026，arXiv）：> We evaluate Foresight … in simulation on LIBERO-Long, ManiSkill-Long, and BEHAVIOR-1K
- MobiAgent: Dual-Loop Recursive Policy Self-Improvement for L…（2026，arXiv）：> Evaluations on RoboCasa, BEHAVIOR-1K, and real-world tasks demonstrate the effectiveness of MobiAgent
- BEHAVIOR-Spatial Benchmark: Evaluating Spatial Understanding…（2026，arXiv）：> We present BEHAVIOR-Spatial, a benchmark built on BEHAVIOR-1K that measures spatial question answering
- Diagnosing Semantic Handoff Failures in Agent-Orchestrated V…（2026，arXiv）：> We study this semantic handoff problem in BEHAVIOR-1K through an agent-orchestrated VLA execution harness
- SSC: A Verifiable Structured Representation for Bimanual Man…（2026，arXiv）：> Rigid template formats, such as BEHAVIOR-1K's skill_annotation, are linguistically over-segmented

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 7 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **sim-to-real** | sim-to-real transfer | 仿真到真实的迁移 | 把仿真里训好的策略用到真机时出现的性能落差问题。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **OmniGibson** | OmniGibson | OmniGibson 仿真环境 | BEHAVIOR-1K 的仿真环境，支持软体、液体与烹饪等状态。 |
| **BDDL** | Behavior Domain Definition Language | 行为域定义语言 | 用符号逻辑描述任务初态、目标与物体关系的任务定义语言。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| BEHAVIOR-1K | 基准 | 1000 项家务活动的长时程基准 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| ManiSkill | 基准 | 通用操作技能基准（SAPIEN） |
| RoboCasa | 基准 | 家庭场景大规模仿真基准 |

<!-- glossary:end -->
