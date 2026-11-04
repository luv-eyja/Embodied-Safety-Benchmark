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
| OpenAlex 引用快照 | [3759](https://openalex.org/W2767621168)；2026-11-04 |
| 来源审计 | [CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938)；external_original_paper |
| 来源核验依据 | 2026-11-03 复核原始论文标题与方法章节：CARLA 模拟器原论文；Leaderboard 是后续评测平台，引用量不代表 Leaderboard 本身 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 5 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Alexey Dosovitskiy, German Ros, Felipe Codevilla, et al., ‘CARLA: An Open Urban Driving Simulator,’ arXiv preprint, 2017, arXiv:1711.03938v1. [论文](https://arxiv.org/abs/1711.03938)；[核查正文](https://arxiv.org/html/1711.03938v1)。

**重点核查位置（章节主题）**：2 Simulation Engine；3 Autonomous Driving；4 Experiments；5 Results；S.3 Experimental Setup。

OpenAlex 被引次数：**[3759](https://openalex.org/W2767621168)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://carla.org/](https://carla.org/)；[https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 4 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **3758** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 49 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://carla.org/](https://carla.org/)；[https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://carla.org/) | https://carla.org/ | 保留文本 4179 字符（截断） |
| [repo](https://github.com/carla-simulator/carla) | https://raw.githubusercontent.com/carla-simulator/carla/HEAD/README.md | stars 14566，license MIT（开源许可证），最后推送 2026-11-03，保留文本 4200 字符（截断） |

**项目页显示**：官网 https://carla.org/ 与 GitHub https://github.com/carla-simulator/carla（14,566 stars，MIT，2026-11-03 推送）均活跃，README 指向 UE5 文档与发布页。

**涉及领域**：自动驾驶城市仿真平台与排行榜协议；开放城市资产、传感器与交通参与者。

**测试目的与构建方法**：提供开放源码的城市驾驶仿真、数字资产与可控传感器／天气／交通配置，早期论文用固定路线比较模块化、模仿学习与强化学习方法，按到达目标、距离与违规评价；Leaderboard 是后续独立协议与版本。

**测试缺陷**：原模拟器论文的实验允许忽略限速与信号灯，不能视为现代 Leaderboard 规则；仿真器引用量不等于排行榜引用量；渲染与物理开销大，结果受版本影响明显。

**与具身智能安全的相关性**：强：可编程构造危险场景（行人、恶劣天气、传感器失效），是自动驾驶安全测试的事实底座；但安全性取决于测试场景如何设计，平台本身不保证覆盖。

**用这个 benchmark 测了什么**：成果是 CARLA 平台与早期受控驾驶协议，展示方法在未见天气／城镇上的不同泛化；3,758 篇引文含 nuScenes、Argoverse 等数据集与大量安全测试框架，例如 ANTI-CARLA 用其做对抗测试。

**本轮核查边界**：只读官网与仓库首页，未安装仿真器或运行 Leaderboard。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| ANTI-CARLA: An Adversarial Testing Framework for Autonomous Vehicles（2022） | 被测自动驾驶栈（框架侧生成对抗场景） | 安全测试框架（在 CARLA 中生成对抗场景） | CARLA 场景与传感器配置 | 产出对抗测试框架，不是模型分数 |
| PCLA: A Framework for Testing Autonomous Agents in the CARLA Simulator（2025） | CARLA Leaderboard 参赛代理 | 测试框架（在 CARLA 上搭测试流水线） | 以 Leaderboard 代理为被测对象 | 产出测试框架；摘要称 Leaderboard 代理是该环境下表现最好的一批 |
| vEDGAR — Can CARLA Do HiL?（2025） | 自动驾驶算法（含硬件在环） | 方法／基础设施（把 CARLA 用于 HiL 测试） | CARLA 用于训练、评测与软件在环测试 | 研究 CARLA 能否支撑硬件在环；摘要未给模型分数 |
| Multi-Modal Fusion Transformer for End-to-End Autonomous Driving（2021） | 多模态融合 Transformer（端到端驾驶） | 评测（端到端驾驶） | CARLA 城市环境与复杂场景 | 称在复杂城市场景上验证有效，未给驾驶分数 |
| Paris-CARLA-3D: A Real and Synthetic Outdoor Point Cloud Dataset（2021） | —（数据集） | 数据生成（用 CARLA 扩增真实点云） | 车载 LiDAR + 相机采集的真实点云，与 CARLA 合成数据配对 | 产出 Paris-CARLA-3D 数据集 |

**原文片段（摘要）**：

- ANTI-CARLA: An Adversarial Testing Framework for Autonomous…（2022，arXiv）：> These challenges can be addressed by using driving simulators such as CARLA instead
- PCLA: A Framework for Testing Autonomous Agents in the CARLA…（2025，arXiv）：> the autonomous agents from the CARLA Leaderboard challenge are regarded as the best-performing agents within this environment
- vEDGAR — Can CARLA Do HiL?（2025，arXiv）：> Common open-source simulators like CARLA are extensively used in training, evaluation, and software-in-the-loop testing
- Multi-Modal Fusion Transformer for End-to-End Autonomous Dri…（2021，OpenAlex 引文）：> We experimentally validate the efficacy of our approach in urban settings involving complex scenarios using the CARLA urban driving simulator
- Paris-CARLA-3D: A Real and Synthetic Outdoor Point Cloud Dat…（2021，arXiv）：> Paris-CARLA-3D is a dataset of several dense colored point clouds of outdoor environments built by a mobile LiDAR and camera system

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 4 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |
| **open-loop** | open-loop evaluation | 开环评测 | 按记录好的输入序列评估，不考虑模型输出对后续状态的影响。 |
| **HiL** | Hardware-in-the-Loop | 硬件在环 | 把真实控制器接入仿真环境测试，介于纯仿真与实车之间。 |
| **CARLA** | CARLA | CARLA 自动驾驶仿真器 | 开放源码的城市驾驶仿真器，自动驾驶安全测试的事实底座。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| CARLA | 仿真平台 | 开源城市驾驶仿真器 |
| CARLA / CARLA Leaderboard | 基准 | 驾驶仿真平台；原论文与榜单需区分 |
| nuScenes | 数据集 | 多模态自动驾驶数据集 |
| NAVSIM | 基准 | 非反应式自动驾驶伪仿真评测 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）），不再重复解释。

<!-- glossary:end -->
