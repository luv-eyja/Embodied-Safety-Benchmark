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
| OpenAlex 引用快照 | [63](https://openalex.org/W4415798424)；2026-11-03 |

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
| [NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://doi.org/10.52202/079017-0902) | 2024 | 提出 | 基于真实数据的非反应式仿真与统一指标 | 提出数据驱动的非反应式仿真基准：用真实驾驶日志构建可复现的仿真评测，避免反应式仿真的域差与不稳定，为端到端规划器提供统一、低成本的比较平台（NeurIPS 2024）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：CVPR 2024 挑战赛有 143 队、463 次提交；论文发现中等算力的 TransFuser 可与部分更复杂驾驶架构竞争。主要成果是数据驱动的可扩展评测协议。

**适用边界**：非反应式模拟不包含他车对自车行为的真实反应，不能替代长期交互安全评估。比赛提交数是社区参与证据，不是论文被引数。

## 5. 相关论文（均来自本调研表）

- [Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift](https://arxiv.org/abs/2609.22582)（2026；使用）
- [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005)（2026；使用）
- [NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://doi.org/10.52202/079017-0902)（2024；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

非反应式模拟不包含他车对自车行为的真实反应，不能替代长期交互安全评估。比赛提交数是社区参与证据，不是论文被引数。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Daniel Dauner, Marcel Hallgarten, Tianyu Li, et al., ‘NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking,’ arXiv preprint, 2024, arXiv:2406.15349v2. [论文](https://doi.org/10.52202/079017-0902)；[核查正文](https://arxiv.org/html/2406.15349v2)。

**重点核查位置（章节主题）**：3 NAVSIM；3.1 Train and Test Splits；4.1 Closed-Loop Alignment；4.2 Analysis。

OpenAlex 被引次数：**[63](https://openalex.org/W4415798424)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/autonomousvision/navsim](https://github.com/autonomousvision/navsim)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 2 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
