# NAVSIM

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：数据驱动评测协议，有明确危险后果指标但闭环交互受限。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：数据驱动非反应式仿真  
> **分类**：具身安全  
> **关联论文**：本表 3 篇（提出 1、使用 2；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/autonomousvision/navsim](https://github.com/autonomousvision/navsim)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Trajectory Planning |
| 应用领域 | 自动驾驶 |
| 被测对象 | 非反应式驾驶仿真评测 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、任务能力 |
| 评测维度/指标 | 基于真实数据的非反应式仿真与统一指标 |
| 基础平台线索 | CARLA、nuScenes、NAVSIM |
| 规模线索 | 从真实驾驶数据挑选有挑战场景，短时展开鸟瞰状态；背景交通按记录运行，不因被测策略而改变。 |
| 执行环境线索 | 非反应式驾驶仿真评测 |
| OpenAlex 引用快照 | [63](https://openalex.org/W4415798424)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 8 个缩写／技术词，并标出 6 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：能否保留真实观测和大规模数据，同时让离线驾驶评测比轨迹距离误差更接近闭环表现？

**评测层级**：非反应式驾驶仿真评测。

## 2. 怎么构建的

**核心场景与条目**：从真实驾驶数据挑选有挑战场景，短时展开鸟瞰状态；背景交通按记录运行，不因被测策略而改变。

**实现与判分**：将候选轨迹在非反应式环境中展开，以碰撞、行驶区域、进度、碰撞时间等组成 PDMS，并对照不同闭环设置检查相关性。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift](https://arxiv.org/abs/2609.22582) | 2026 | 使用 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 | 指出排行榜名次只报告结果、不报告行为，因而难以预测策略在新地点的表现：nuScenes 开环误差或 NAVSIM 排名并不迁移到「新地点且行人位于自车走廊附近」的场景。提出反事实体检——数百帧真实画面各做两种编辑（移除行人、夜间重打光）并由独立检测器验证，把规划轨迹的变化当作诊断量而非分数，并从中读出两个因果轴、构造五项「考试」以分离被单一分数合并的行为差异。 |
| [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005) | 2026 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 | 指出纯视觉端到端驾驶模型正接近部署，而部署中相机流会被模糊、噪声、低照度、天气、丢帧与内存故障破坏，但策略在驾驶能力崩溃前能容忍多少尚不清楚；已有的损坏鲁棒性基准针对检测或鸟瞰图感知，而非真正驱动车辆的计划输出。基准把 16 类退化在 5 个严重度下于图像加载器内即时注入，单一算子即可触达 15 个策略。 |
| [NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://doi.org/10.52202/079017-0902) | 2024 | 提出 | 基于真实数据的非反应式仿真与统一指标 | 提出数据驱动的非反应式仿真基准：用真实驾驶日志构建可复现的仿真评测，避免反应式仿真的域差与不稳定，为端到端规划器提供统一、低成本的比较平台（NeurIPS（会议／期刊） 2024）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：CVPR（会议／期刊） 2024 挑战赛有 143 队、463 次提交；论文发现中等算力的 TransFuser 可与部分更复杂驾驶架构竞争。主要成果是数据驱动的可扩展评测协议。

**适用边界**：非反应式模拟不包含他车对自车行为的真实反应，不能替代长期交互安全评估。比赛提交数是社区参与证据，不是论文被引数。

## 5. 相关论文（均来自本调研表）

- [Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift](https://arxiv.org/abs/2609.22582)（2026；使用）
- [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005)（2026；使用）
- [NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://doi.org/10.52202/079017-0902)（2024；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

非反应式模拟不包含他车对自车行为的真实反应，不能替代长期交互安全评估。比赛提交数是社区参与证据，不是论文被引数。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Daniel Dauner, Marcel Hallgarten, Tianyu Li, et al., ‘NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking,’ arXiv preprint, 2024, arXiv:2406.15349v2. [论文](https://doi.org/10.52202/079017-0902)；[核查正文](https://arxiv.org/html/2406.15349v2)。

**重点核查位置（章节主题）**：3 NAVSIM；3.1 Train and Test Splits；4.1 Closed-Loop Alignment；4.2 Analysis。

OpenAlex 被引次数：**[63](https://openalex.org/W4415798424)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/autonomousvision/navsim](https://github.com/autonomousvision/navsim)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 2 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **63** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 49 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/autonomousvision/navsim](https://github.com/autonomousvision/navsim)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/autonomousvision/navsim) | https://raw.githubusercontent.com/autonomousvision/navsim/HEAD/README.md | stars 1140，license Apache-2.0（开源许可证），最后推送 2025-10-27，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/autonomousvision/navsim（1,140 stars，Apache-2.0，2025-10-27 推送）README 给 Paper／Supplementary／Leaderboard v1、v2 入口与安装说明。

**涉及领域**：自动驾驶的非反应式伪仿真评测；传感器数据驱动的规划与闭环相关性。

**测试目的与构建方法**：把候选轨迹在非反应式环境中展开，用碰撞、可行驶区域、进度、碰撞时间等组成 PDMS 分数，并对照不同闭环设置检查相关性；公开 leaderboard 分 navtest 与 navhard。

**测试缺陷**：非反应式模拟不含他车对自车行为的真实反应，不能替代长期交互安全评估；PDMS 权重影响排序；比赛提交数是社区参与证据，不是被引数。

**与具身智能安全的相关性**：中等偏强：碰撞与可行驶区域直接进入指标，所以它比纯开环规划基准更接近安全；但缺少交互反应，无法评估“逼他车避让”这类风险行为。

**用这个 benchmark 测了什么**：CVPR 2024 挑战赛 143 队、463 次提交，公开 LB 持续更新；论文发现中等算力的 TransFuser 可与部分更复杂架构竞争；下游 DriveFuture 报告 NAVSIM-v2 上 55.5 EPDMS。

**本轮核查边界**：只读 README 与入口，未下载数据或跑评测。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Gaze-Flow: Human-Like and Interpretable End-to-End Planning via Gaze（2026） | Gaze-Flow（端到端规划） | 评测（v1 与 v2 分别报告） | NAVSIM v1 的 PDMS 与 v2 的 EPDMS | PDMS 91.5（v1）、EPDMS 86.7（v2）；摘要称在安全、舒适、规则遵守与类人度上都有竞争力 |
| DriveFuture: Future-Aware Latent World Models for Autonomous Driving（2026） | DriveFuture（未来感知隐世界模型） | 评测（官方榜单拆分） | NAVSIM-v2 的 navhard 与 navtest 两个拆分，EPDMS | navhard 55.5 EPDMS、navtest 89.9 EPDMS，称达到公开榜单 SOTA |
| DIVER: Reinforced Diffusion Breaks Imitation Bottlenecks in End-to-End…（2026） | DIVER（强化扩散） | 评测（闭环 + 开环并列） | 闭环 NAVSIM 与 Bench2Drive，另在开环 nuScenes 上评测 | 称显著提升轨迹多样性并缓解模仿瓶颈；摘要未给 NAVSIM 分数 |
| Driving on manifolds: A stochastic manifold mapping paradigm（2026） | DOM（流形映射） | 评测（基准 + 真车闭环） | NAVSIM、大规模真实数据集与真实闭环实验 | 称达到 SOTA 并有良好 scaling 性质；未给数值 |
| Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark St…（2026） | —（指标研究，不测单一模型） | 审计（检验开环指标能否预测闭环） | NAVSIM v2 引入的“安全感知开环指标”与闭环表现的相关性 | 提出并检验相关性；结论按论文，不在此复述数值 |

**原文片段（摘要）**：

- Gaze-Flow: Human-Like and Interpretable End-to-End Planning…（2026，OpenAlex 引文）：> Gaze-Flow achieves a PDMS of 91.5 on NAVSIM v1 and an EPDMS of 86.7 on NAVSIM v2
- DriveFuture: Future-Aware Latent World Models for Autonomous…（2026，arXiv）：> reaching 55.5 EPDMS on NAVSIM-v2 navhard, 89.9 EPDMS on NAVSIM-v2 navtest
- DIVER: Reinforced Diffusion Breaks Imitation Bottlenecks in…（2026，OpenAlex 引文）：> Extensive experiments on the closed-loop NAVSIM and Bench2Drive benchmarks
- Driving on manifolds: A stochastic manifold mapping paradigm（2026，OpenAlex 引文）：> Validated on the NAVSIM benchmark, large-scale real-world datasets, and closed-loop real-world experiments
- Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Be…（2026，arXiv）：> we ask whether the more recent, safety-aware open-loop metrics introduced by NAVSIM v2 can bridge this gap

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 8 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **PDMS** | Planning Driving Metric Score | 规划综合分（自动驾驶） | NAVSIM 的综合驾驶分：把碰撞、可行驶区域、舒适、进度按权重合成。 |
| **EPDMS** | Extended PDMS / Pseudo-simulation Driving Metric Score | 扩展规划综合分 | NAVSIM v2 在 PDMS 基础上加入更严格子项（含伪仿真两阶段）的分数。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |
| **open-loop** | open-loop evaluation | 开环评测 | 按记录好的输入序列评估，不考虑模型输出对后续状态的影响。 |
| **leaderboard** | leaderboard | 排行榜 | 公开提交与排名的榜单，反映社区参与度，不等于论文引用。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **CARLA** | CARLA | CARLA 自动驾驶仿真器 | 开放源码的城市驾驶仿真器，自动驾驶安全测试的事实底座。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| NAVSIM | 基准 | 非反应式自动驾驶伪仿真评测 |
| CARLA | 仿真平台 | 开源城市驾驶仿真器 |
| nuScenes | 数据集 | 多模态自动驾驶数据集 |

另有 3 个专有名称已在正文首次出现处加括号标注类别（例如 NeurIPS（会议／期刊）、CVPR（会议／期刊）、Apache-2.0（开源许可证）），不再重复解释。

<!-- glossary:end -->
