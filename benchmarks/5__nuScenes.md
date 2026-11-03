# nuScenes

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：虽提供训练数据，也明确定义独立感知测试任务与指标，主归评测任务集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：真实驾驶数据集（开环）  
> **分类**：具身安全  
> **关联论文**：本表 3 篇（提出 0、使用 3；方法参考另标）
> **证据级别**：原表 C；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://www.nuscenes.org/](https://www.nuscenes.org/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | nuScenes: A multimodal dataset for autonomous driving |
| 年份 | 2019（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | Planning › Trajectory Planning |
| 应用领域 | 未标注 |
| 被测对象 | 真实驾驶感知数据与评测 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 |
| 基础平台线索 | CARLA、nuScenes、NAVSIM |
| 规模线索 | 1,000 个各 20 秒场景，六相机、五雷达、一个激光雷达，360° 感知；原始标注含 23 类物体与八种属性。 |
| 执行环境线索 | 真实驾驶感知数据与评测 |
| 来源审计 | [nuScenes: A multimodal dataset for autonomous driving](https://arxiv.org/abs/1903.11027)；external_original_paper |
| 来源核验依据 | nuScenes 是当前 DriveDegrade、ExceptionDrive 等条目的底层数据集；原始数据集论文不在当前 192 条本库记录中。 |
| OpenAlex 引用快照 | [7152](https://openalex.org/W2925148167)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何以完整车载多传感器数据标准化三维检测和跟踪，而不只依靠单目图像？

**评测层级**：真实驾驶感知数据与评测。

## 2. 怎么构建的

**核心场景与条目**：1,000 个各 20 秒场景，六相机、五雷达、一个激光雷达，360° 感知；原始标注含 23 类物体与八种属性。

**实现与判分**：同步传感器、定位和地图，人工标注三维框；定义检测与跟踪的时间信息边界，提供 NDS、误差分量及 AMOTA／AMOTP 等，而不只计算框重叠。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift](https://arxiv.org/abs/2609.22582) | 2026 | 使用 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 | 指出排行榜名次只报告结果、不报告行为，因而难以预测策略在新地点的表现：nuScenes 开环误差或 NAVSIM 排名并不迁移到「新地点且行人位于自车走廊附近」的场景。提出反事实体检——数百帧真实画面各做两种编辑（移除行人、夜间重打光）并由独立检测器验证，把规划轨迹的变化当作诊断量而非分数，并从中读出两个因果轴、构造五项「考试」以分离被单一分数合并的行为差异。 |
| [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005) | 2026 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 | 指出纯视觉端到端驾驶模型正接近部署，而部署中相机流会被模糊、噪声、低照度、天气、丢帧与内存故障破坏，但策略在驾驶能力崩溃前能容忍多少尚不清楚；已有的损坏鲁棒性基准针对检测或鸟瞰图感知，而非真正驱动车辆的计划输出。基准把 16 类退化在 5 个严重度下于图像加载器内即时注入，单一算子即可触达 15 个策略。 |
| [ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving](https://arxiv.org/abs/2609.37871) | 2026 | 使用 | 21 个任务 / 6 个安全族；无参考评测协议（UR/HCC/HPR） | 指出在常规驾驶基准上的平均表现无法证明规划器在稀有且安全攸关的危险情形下可靠。基准用 VLM 辅助筛选、局部多视角编辑与质量审计，把危险插入真实 nuScenes 场景并保留其上下文；21 个任务跨六个安全族，定义危险/冲突区域、局部安全约束与可接受响应。由于插入危险会使记录的人类轨迹失效，采用无参考协议，用不安全率（UR）、危险避让合规（HCC）、危险接近响应（HPR）等指标评估编辑后的预测。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：成果是多模态真实驾驶数据、开发工具和检测／跟踪基线，成为后续多任务驾驶研究的重要数据底座。原论文自身主要评价感知。

**适用边界**：23 类标注不等于检测榜单全部评价 23 类。后来的预测／规划扩展不应倒推为原论文已完成；检测高分不是闭环驾驶安全保证。

## 5. 相关论文（均来自本调研表）

- [Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift](https://arxiv.org/abs/2609.22582)（2026；使用）
- [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005)（2026；使用）
- [ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving](https://arxiv.org/abs/2609.37871)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

23 类标注不等于检测榜单全部评价 23 类。后来的预测／规划扩展不应倒推为原论文已完成；检测高分不是闭环驾驶安全保证。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Holger Caesar, Varun Bankiti, Alex H. Lang, et al., ‘nuScenes: A multimodal dataset for autonomous driving,’ arXiv preprint, 2019, arXiv:1903.11027v5. [论文](https://arxiv.org/abs/1903.11027)；[核查正文](https://arxiv.org/html/1903.11027v5)。

**重点核查位置（章节主题）**：2 The nuScenes Dataset；3.1 Detection；3.2 Tracking；4 Experiments。

OpenAlex 被引次数：**[7152](https://openalex.org/W2925148167)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://www.nuscenes.org/](https://www.nuscenes.org/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 3 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
