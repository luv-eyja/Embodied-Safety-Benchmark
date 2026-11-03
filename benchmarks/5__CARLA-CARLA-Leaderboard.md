# CARLA / CARLA Leaderboard

<!-- survey-classification:start -->
> **统一调研分类**：仿真平台；具身研究底座；目标：能力、鲁棒性。
> **分类依据**：本条当前来源是模拟器论文；与 Leaderboard 合并命名不代表同一协议。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：城市驾驶仿真与排行榜  
> **分类**：具身安全  
> **关联论文**：本表 4 篇（提出 0、使用 4；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://carla.org/](https://carla.org/)；[https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | CARLA: An Open Urban Driving Simulator |
| 年份 | 2017（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | Agentic › Cascading Risks |
| 应用领域 | 自动驾驶 |
| 被测对象 | 驾驶仿真平台；原论文与榜单需区分 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | 对抗补丁实时注入；针对智能体而非孤立 ML 模型 |
| 基础平台线索 | CARLA、SUMO、nuScenes、NAVSIM |
| 规模线索 | 2017 原论文使用两个城镇、六种天气，四类任务从直行、转弯到导航及带动态障碍导航；训练和未见城镇／天气分开。 |
| 执行环境线索 | 驾驶仿真平台；原论文与榜单需区分 |
| OpenAlex 引用快照 | 未核验（查询失败／未匹配）；2026-11-03 |
| 来源审计 | [CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938)；external_original_paper |
| 来源核验依据 | 2026-11-03 复核原始论文标题与方法章节：CARLA 模拟器原论文；Leaderboard 是后续评测平台，引用量不代表 Leaderboard 本身 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何在可控城市环境、天气与动态交通下比较自动驾驶方法及其泛化？

**评测层级**：驾驶仿真平台；原论文与榜单需区分。

## 2. 怎么构建的

**核心场景与条目**：2017 原论文使用两个城镇、六种天气，四类任务从直行、转弯到导航及带动态障碍导航；训练和未见城镇／天气分开。

**实现与判分**：开放城市资产、传感器和交互仿真，比较模块化、模仿学习与强化学习方法；按到达目标、距离及违规等评价。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?](https://arxiv.org/abs/2610.16634) | 2026 | 使用 | 配对反事实单元（固定场景只改指令）；四类指令遵循范围 | 现有闭环驾驶基准主要度量路线完成度、安全性与规则符合度，却未回答「语言是否真正决定了车辆执行哪一种可行行为」。该基准以配对反事实单元为评测单位：固定初始驾驶场景、只改指令，从而把孤立的指令成功与配对反事实成功区分开，覆盖四种指令遵循范围，并可检验该区分是否在不同评测区间持续成立。 |
| [Attacking Autonomous Driving Agents with Adversarial Machine Learning: A Holistic Evaluation with the CARLA Leaderboard](https://arxiv.org/abs/2511.14876) | 2025 | 使用 | 对抗补丁实时注入；针对智能体而非孤立 ML 模型 | 指出自动驾驶智能体依赖多个 ML 模型、控制逻辑与自定义模块的组合输出，虽然大量先前工作已证明对抗样本能误导单个 ML 模型，但这些攻击能否对不同智能体、环境与场景产生有害驾驶动作仍不清楚。作者主张针对智能体整体而非孤立模型评估，用 CARLA 城市驾驶仿真器在运行时把对抗补丁注入并针对 CARLA Leaderboard 上的多个智能体评测。 |
| [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005) | 2026 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 | 指出纯视觉端到端驾驶模型正接近部署，而部署中相机流会被模糊、噪声、低照度、天气、丢帧与内存故障破坏，但策略在驾驶能力崩溃前能容忍多少尚不清楚；已有的损坏鲁棒性基准针对检测或鸟瞰图感知，而非真正驱动车辆的计划输出。基准把 16 类退化在 5 个严重度下于图像加载器内即时注入，单一算子即可触达 15 个策略。 |
| [SIREN-Bench: Behavior-Driven Generation and Evaluation of Emergency-Vehicle Interactions](https://arxiv.org/abs/2608.24094) | 2026 | 使用 | SUMO–CARLA 联合仿真；行为级控制特权与响应 | 指出紧急车辆（EMV）会重组周边交通——民用车辆刹车、变道或让出救援通道——评测这些安全攸关交互需要对 EMV 特权与民用车辆响应同时具备行为级控制能力，并保持一致感知与真值，而现有数据集与仿真基准并不直接提供这一组合。SIREN 把 SUMO 的网络级交通演化与行为逻辑同 CARLA 的连续车辆控制与同步车载感知耦合起来。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：成果是 CARLA 平台与早期受控驾驶协议，展示方法在未见天气／城镇上的不同泛化特点。本卡被引数对应原始模拟器论文。

**适用边界**：原实验允许忽略限速与信号灯，不能视为现代 Leaderboard 的规则。Leaderboard 是后续独立协议与版本，模拟器论文引用量不等于排行榜引用量。

## 5. 相关论文（均来自本调研表）

- [Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?](https://arxiv.org/abs/2610.16634)（2026；使用）
- [Attacking Autonomous Driving Agents with Adversarial Machine Learning: A Holistic Evaluation with the CARLA Leaderboard](https://arxiv.org/abs/2511.14876)（2025；使用）
- [A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving](https://arxiv.org/abs/2608.29005)（2026；使用）
- [SIREN-Bench: Behavior-Driven Generation and Evaluation of Emergency-Vehicle Interactions](https://arxiv.org/abs/2608.24094)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

原实验允许忽略限速与信号灯，不能视为现代 Leaderboard 的规则。Leaderboard 是后续独立协议与版本，模拟器论文引用量不等于排行榜引用量。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Alexey Dosovitskiy, German Ros, Felipe Codevilla, et al., ‘CARLA: An Open Urban Driving Simulator,’ arXiv preprint, 2017, arXiv:1711.03938v1. [论文](https://arxiv.org/abs/1711.03938)；[核查正文](https://arxiv.org/html/1711.03938v1)。

**重点核查位置（章节主题）**：2 Simulation Engine；3 Autonomous Driving；4 Experiments；5 Results；S.3 Experimental Setup。

OpenAlex 被引次数：**未核验（查询失败／未匹配）**；观测日期：2026-11-03。本次未取得可核验计数，不按 0 处理。

**项目与成果入口**：[https://carla.org/](https://carla.org/)；[https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 4 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
