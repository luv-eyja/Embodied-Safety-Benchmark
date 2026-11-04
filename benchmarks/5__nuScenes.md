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
| OpenAlex 引用快照 | [7179](https://openalex.org/W2925148167)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 11 个缩写／技术词，并标出 3 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Holger Caesar, Varun Bankiti, Alex H. Lang, et al., ‘nuScenes: A multimodal dataset for autonomous driving,’ arXiv preprint, 2019, arXiv:1903.11027v5. [论文](https://arxiv.org/abs/1903.11027)；[核查正文](https://arxiv.org/html/1903.11027v5)。

**重点核查位置（章节主题）**：2 The nuScenes Dataset；3.1 Detection；3.2 Tracking；4 Experiments。

OpenAlex 被引次数：**[7179](https://openalex.org/W2925148167)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://www.nuscenes.org/](https://www.nuscenes.org/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 3 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **7151** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 49 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://www.nuscenes.org/](https://www.nuscenes.org/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://www.nuscenes.org/) | https://www.nuscenes.org/ | 保留文本 46 字符（截断） |

**项目页显示**：官网 https://www.nuscenes.org/ 需启用 JavaScript 才能渲染，抓取只得到提示文本；数据与工具通过该站发布。

**涉及领域**：自动驾驶多模态数据集与感知基准；同步相机、激光雷达、毫米波雷达、定位与地图。

**测试目的与构建方法**：同步传感器、定位与地图，人工标注三维框；定义检测与跟踪的时间信息边界，提供 NDS、误差分量与 AMOTA／AMOTP 等指标，而不只算框重叠。

**测试缺陷**：23 类标注不等于榜单全部评价 23 类；后来的预测／规划扩展不应倒推为原论文已完成；检测高分不是闭环驾驶安全保证；站点依赖 JS，静态抓取无内容。

**与具身智能安全的相关性**：弱到中等：感知是安全的前置，但数据集本身不含风险标注或违规定义；安全性取决于下游如何用它构造场景。

**用这个 benchmark 测了什么**：成果是多模态真实驾驶数据、开发工具与检测／跟踪基线，成为多任务驾驶研究的数据底座；7,151 篇引文覆盖 Waymo Open Dataset、3D 点云综述等；2026 年有工作专门“重访 nuScenes”总结其进展与挑战。

**本轮核查边界**：站点为前端渲染，未取到数据下载与许可证细节。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Center-based 3D Object Detection and Tracking（CenterPoint）（2021） | CenterPoint | 训练后评测（检测 + 跟踪 SOTA） | nuScenes 3D 检测与跟踪，指标 NDS 与 AMOTA | 单模型 65.5 NDS、63.8 AMOTA |
| BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View（2023） | BEVFusion（多传感器融合） | 训练后评测（检测 + BEV 分割） | nuScenes 3D 检测 mAP／NDS 与 BEV map segmentation mIoU | mAP 与 NDS 各高 1.3%，分割 mIoU 高 13.6%，算力低 1.9 倍 |
| TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection（2022） | TransFusion | 训练后评测（检测 + 跟踪榜单） | nuScenes 3D 检测，另扩展到跟踪任务 | 在 nuScenes 跟踪榜单拿到第 1 名 |
| PointPainting: Sequential Fusion for 3D Object Detection（2020） | PointPainting（叠加到 Point-RCNN／VoxelNet／PointPillars） | 训练后评测（作为通用增强模块） | KITTI 与 nuScenes 两个数据集 | 在三个 SOTA 检测器上均有大幅提升 |
| Planning-oriented Autonomous Driving（UniAD）（2023） | UniAD（规划导向的端到端框架） | 训练后评测（把规划与感知任务串起来） | nuScenes 上的检测、跟踪、建图、运动预测与规划 | 在 nuScenes 上实例化并报告各任务成绩；摘要未给单一数值 |

**原文片段（摘要）**：

- Center-based 3D Object Detection and Tracking（CenterPoint）（2021，OpenAlex 引文）：> CenterPoint achieved state-of-the-art performance on the nuScenes benchmark … with 65.5 NDS and 63.8 AMOTA
- BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird'…（2023，OpenAlex 引文）：> achieving 1.3% higher mAP and NDS on 3D object detection and 13.6% higher mIoU on BEV map segmentation
- TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detect…（2022，OpenAlex 引文）：> achieve the 1st place in the leader-board of nuScenes tracking
- PointPainting: Sequential Fusion for 3D Object Detection（2020，OpenAlex 引文）：> large improvements on three different state-of-the art methods … on the KITTI and nuScenes datasets
- Planning-oriented Autonomous Driving（UniAD）（2023，OpenAlex 引文）：> We instantiate UniAD on the challenging nuScenes benchmark

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 11 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **NDS** | nuScenes Detection Score | nuScenes 检测综合分 | nuScenes 检测榜的综合分，由 mAP 与多项误差指标加权得到。 |
| **AMOTA** | Average Multi-Object Tracking Accuracy | 平均多目标跟踪准确率 | nuScenes 跟踪主指标，跨召回阈值对 MOTA 取平均。 |
| **AMOTP** | Average Multi-Object Tracking Precision | 平均多目标跟踪精度 | 跟踪框与真值的位置误差，越小越好。 |
| **mAP** | mean Average Precision | 平均精度均值 | 检测类任务的综合精度：各类别 AP 的平均。 |
| **mIoU** | mean Intersection over Union | 平均交并比 | 分割任务的准确度：预测区域与真值区域的重叠比，按类别平均。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **open-loop** | open-loop evaluation | 开环评测 | 按记录好的输入序列评估，不考虑模型输出对后续状态的影响。 |
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **CARLA** | CARLA | CARLA 自动驾驶仿真器 | 开放源码的城市驾驶仿真器，自动驾驶安全测试的事实底座。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| nuScenes | 数据集 | 多模态自动驾驶数据集 |
| NAVSIM | 基准 | 非反应式自动驾驶伪仿真评测 |
| CARLA | 仿真平台 | 开源城市驾驶仿真器 |

<!-- glossary:end -->
