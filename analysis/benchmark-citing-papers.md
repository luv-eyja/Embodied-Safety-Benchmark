# 引用了这些 Benchmark 的论文：清单与口径

> 观测日期 2026-11-04。结构化清单：[benchmark_citing_works.json](../data/benchmark_citing_works.json)；计数来源：[引用快照](../data/benchmark_citation_snapshot.json)。

范围为主目录 **62 个已分类条目**，每条只取一个选定论文记录（预印本与正式版不合并、不相加）。本文件由 `scripts/build_benchmark_citing_report.py` 从上述 JSON 渲染，正文数字与清单同源。

## 1. 三个不同的口径

| 口径 | 怎么得到 | 能说 | 不能说 |
|---|---|---|---|
| `cited_by_count` | OpenAlex 在该 Work 记录上统计的被引次数 | 该记录的被引量级 | 其他数据库同值；benchmark 被采用 |
| `cites` 清单 | OpenAlex `filter=cites:<work>` 返回的论文 | 论文参考文献里有这篇原论文 | 它真的跑过这个 benchmark |
| `arxiv` 命中 | arXiv `cat:cs.RO 或 cs.CV` 且 `abs:"名称"`，再逐条字面核对标题／摘要 | 摘要里出现了这个名称，且保留上下文片段 | 引用或使用了该 benchmark |

三个口径互不替代，本文件也不把它们相加。**未查到不等于没人引用**：0 只是该记录在查询时的计数，新论文的收录与参考文献解析都有延迟。引用数也不等于独立采用——作者自用、只做背景引用、和真在这个 benchmark 上跑实验是三种强度不同的证据。

两个细节需要先说明：

- 同一条目的 `cited_by_count` 与引文清单长度会差几条（例如 nuScenes 7179 对 7151）。前者是 OpenAlex 维护的计数，后者由参考文献解析重新汇总，两者更新节奏不同；本文件两者都照原样展示，不取平均、不补齐。
- 引文清单里个别记录年份早于来源论文，这是 OpenAlex 的元数据错误；概览的年份跨度只统计不早于来源论文的年份，逐条清单仍保留原始记录。
- 引文由 OpenAlex 的参考文献解析生成，可能把同名或元数据相近的条目误记成引用；同一论文的预印本与正式版也可能各占一条。清单适合用来找入口，具体到某篇论文是否真的引用／使用了该 benchmark，仍须打开原文核对。

## 2. 总览

| 条目 | 被引 | 引文年份 | 引文清单 | arXiv 摘要命中 | 状态 |
|---|---:|---|---:|---:|---|
| [nuScenes](../benchmarks/5__nuScenes.md) | 7179 | 2020–2026 | 25/7151 | ≥49 | 有引文（仅列前 25 条） |
| [CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md) | 3759 | 2017–2026 | 25/3758 | ≥49 | 有引文（仅列前 25 条） |
| [CALVIN](../benchmarks/3__CALVIN.md) | 189 | 2022–2026 | 25/188 | ≥49 | 有引文（仅列前 25 条） |
| [LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md) | 136 | 2024–2026 | 25/136 | ≥50 | 有引文（仅列前 25 条） |
| [Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md) | 113 | 2023–2026 | 25/113 | 25 | 有引文（仅列前 25 条） |
| [NAVSIM](../benchmarks/5__NAVSIM.md) | 63 | 2025–2026 | 25/63 | ≥49 | 有引文（仅列前 25 条） |
| [SafeBench](../benchmarks/5__SafeBench.md) | 48 | 2022–2026 | 25/48 | 歧义，不作计数 | 有引文（仅列前 25 条） |
| [RoboTwin](../benchmarks/3__RoboTwin.md) | 31 | 2025–2026 | 25/30 | ≥49 | 有引文（仅列前 25 条） |
| [COLOSSEUM](../benchmarks/3__COLOSSEUM.md) | 29 | 2024–2026 | 25/29 | 10 | 有引文（仅列前 25 条） |
| [ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md) | 24 | 2023–2026 | 24/24 | ≥50 | 有引文 |
| [RoboMIND](../benchmarks/3__RoboMIND.md) | 23 | 2025–2026 | 23/23 | 2 | 有引文 |
| [VLABench](../benchmarks/3__VLABench.md) | 16 | 2025–2026 | 16/16 | 17 | 有引文 |
| [AgiBot World](../benchmarks/3__AgiBot-World.md) | 13 | 2025–2026 | 13/13 | 2 | 有引文 |
| [BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md) | 7 | 2024–2025 | 7/7 | 25 | 有引文 |
| [Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md) | 6 | 2025–2026 | 6/6 | 1 | 有引文 |
| [RoboCasa](../benchmarks/3__RoboCasa.md) | 4 | 2025 | 4/4 | ≥49 | 有引文 |
| [SimplerEnv](../benchmarks/3__SimplerEnv.md) | 4 | 2024–2026 | 4/4 | ≥50 | 有引文 |
| [IS-Bench](../benchmarks/4__IS-Bench.md) | 2 | 2026 | 2/2 | 歧义，不作计数 | 有引文 |
| [SafeAgentBench](../benchmarks/4__SafeAgentBench.md) | 2 | 2025 | 2/2 | 3 | 有引文 |
| [EmbodiedBench](../benchmarks/4__EmbodiedBench.md) | 1 | 2025 | 1/1 | 6 | 有引文 |
| [ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md) | 0 | — | 0/0 | 1 | 无引文、有摘要命中 |
| [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) | 0 | — | 0/0 | 0 | 无引文 |
| [HazardArena](../benchmarks/1__HazardArena.md) | 0 | — | 0/0 | 0 | 无引文 |
| [LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md) | 0 | — | 0/0 | 2 | 无引文、有摘要命中 |
| [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboHarm](../benchmarks/1__RoboHarm.md) | 0 | — | 0/0 | 0 | 无引文 |
| [SafeLIBERO](../benchmarks/1__SafeLIBERO.md) | 0 | — | 0/0 | 7 | 无引文、有摘要命中 |
| [SafeStage](../benchmarks/1__SafeStage.md) | 0 | — | 0/0 | 0 | 无引文 |
| [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) | 0 | — | 0/0 | 0 | 无引文 |
| [VLA-Arena](../benchmarks/1__VLA-Arena.md) | 0 | — | 0/0 | 6 | 无引文、有摘要命中 |
| [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) | 0 | — | 0/0 | 0 | 无引文 |
| [LIBERO-Para](../benchmarks/2__LIBERO-Para.md) | 0 | — | 0/0 | 3 | 无引文、有摘要命中 |
| [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) | 0 | — | 0/0 | 0 | 无引文 |
| [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) | 0 | — | 0/0 | 0 | 无引文 |
| [BiDex-100](../benchmarks/3__BiDex-100.md) | 0 | — | 0/0 | 0 | 无引文 |
| [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboCasa365](../benchmarks/3__RoboCasa365.md) | 0 | — | 0/0 | 32 | 无引文、有摘要命中 |
| [RoboChrono](../benchmarks/3__RoboChrono.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboComb](../benchmarks/3__RoboComb.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboFollow](../benchmarks/3__RoboFollow.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboReel](../benchmarks/3__RoboReel.md) | 0 | — | 0/0 | 0 | 无引文 |
| [Spa-Bench](../benchmarks/3__Spa-Bench.md) | 0 | — | 0/0 | 2 | 无引文、有摘要命中 |
| [Bench2Dex](../benchmarks/4__Bench2Dex.md) | 0 | — | 0/0 | 0 | 无引文 |
| [DESPITE](../benchmarks/4__DESPITE.md) | 0 | — | 0/0 | 歧义，不作计数 | 无引文、名称歧义命中（不计） |
| [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [INFUSE](../benchmarks/4__INFUSE.md) | 0 | — | 0/0 | 歧义，不作计数 | 无引文、名称歧义命中（不计） |
| [LABIT](../benchmarks/4__LABIT.md) | 0 | — | 0/0 | 0 | 无引文 |
| [MSK-Bench](../benchmarks/4__MSK-Bench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [MemForm](../benchmarks/4__MemForm.md) | 0 | — | 0/0 | 0 | 无引文 |
| [MineAmongUs](../benchmarks/4__MineAmongUs.md) | 0 | — | 0/0 | 0 | 无引文 |
| [ORBIT](../benchmarks/4__ORBIT.md) | 0 | — | 0/0 | 歧义，不作计数 | 无引文、名称歧义命中（不计） |
| [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboAbstention](../benchmarks/4__RoboAbstention.md) | 0 | — | 0/0 | 0 | 无引文 |
| [RoboJailBench](../benchmarks/4__RoboJailBench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [STARS](../benchmarks/4__STARS.md) | 0 | — | 0/0 | 歧义，不作计数 | 无引文、名称歧义命中（不计） |
| [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) | 0 | — | 0/0 | 0 | 无引文 |
| [VIPS](../benchmarks/5__VIPS.md) | 0 | — | 0/0 | 歧义，不作计数 | 无引文、名称歧义命中（不计） |

四类互斥，合计 62 = **20** 条有可列出的引文论文（原始计数合计 11618，同一论文可引多个条目，故不可当独立论文数）+ **7** 条只有 arXiv 摘要命中、引文图中暂无引文 + **5** 条名称歧义、命中不能当计数 + **30** 条两种口径都没有。

## 3. 有引文的条目：谁在引用

按被引数从高到低。每条列出被引最高的引文（至多 8 篇），完整列表见 JSON；“类型”是 OpenAlex 的 `type` 字段，不是对论文内容的判断。

### nuScenes（被引 7151）

来源论文：[nuScenes: A multimodal dataset for autonomous driving](https://arxiv.org/abs/1903.11027)；OpenAlex 记录：[W2925148167](https://openalex.org/W2925148167)。引文年份分布：2026 年 1100、2025 年 1648、2024 年 1582、2023 年 1139、2022 年 715、2021 年 584、2020 年 325（另有 57 条记录年份早于来源论文，未计入）。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2020 | [Scalability in Perception for Autonomous Driving: Waymo Open Dataset](https://doi.org/10.1109/cvpr42600.2020.00252) | conference-paper | 3437 |
| 2020 | [Deep Learning for 3D Point Clouds: A Survey](https://doi.org/10.1109/tpami.2020.3005434) | article | 2429 |
| 2021 | [Center-based 3D Object Detection and Tracking](https://doi.org/10.1109/cvpr46437.2021.01161) | conference-paper | 2182 |
| 2020 | [A Survey of Autonomous Driving: Common Practices and Emerging Technologies](https://doi.org/10.1109/access.2020.2983149) | article | 1893 |
| 2019 | [A survey of deep learning techniques for autonomous driving](https://doi.org/10.1002/rob.21918) | article | 1809 |
| 2019 | [Argoverse: 3D Tracking and Forecasting With Rich Maps](https://doi.org/10.1109/cvpr.2019.00895) | conference-paper | 1483 |
| 2020 | [Tracking Objects as Points](https://doi.org/10.1007/978-3-030-58548-8_28) | conference-paper | 1434 |
| 2020 | [Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges](https://doi.org/10.1109/tits.2020.2972974) | article | 1425 |

> 该记录共 7151 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### CARLA / CARLA Leaderboard（被引 3758）

来源论文：[CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938)；OpenAlex 记录：[W2767621168](https://openalex.org/W2767621168)。引文年份分布：2026 年 10、2025 年 381、2024 年 814、2023 年 785、2022 年 630、2021 年 519、2020 年 339、2019 年 206、2018 年 72、2017 年 1（另有 1 条记录年份早于来源论文，未计入）。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2020 | [nuScenes: A Multimodal Dataset for Autonomous Driving](https://doi.org/10.1109/cvpr42600.2020.01164) | conference-paper | 7179 |
| 2021 | [Deep Reinforcement Learning for Autonomous Driving: A Survey](https://doi.org/10.1109/tits.2021.3054625) | article | 2351 |
| 2020 | [Shortcut learning in deep neural networks](https://doi.org/10.1038/s42256-020-00257-z) | article | 2261 |
| 2020 | [Self-Supervised Visual Feature Learning With Deep Neural Networks: A Survey](https://doi.org/10.1109/tpami.2020.2992393) | article | 2050 |
| 2020 | [A Survey of Autonomous Driving: Common Practices and Emerging Technologies](https://doi.org/10.1109/access.2020.2983149) | article | 1893 |
| 2019 | [ADVENT: Adversarial Entropy Minimization for Domain Adaptation in Semantic Segmentation](https://doi.org/10.1109/cvpr.2019.00262) | conference-paper | 1536 |
| 2019 | [Argoverse: 3D Tracking and Forecasting With Rich Maps](https://doi.org/10.1109/cvpr.2019.00895) | conference-paper | 1483 |
| 2020 | [Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges](https://doi.org/10.1109/tits.2020.2972974) | article | 1425 |

> 该记录共 3758 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### CALVIN（被引 188）

来源论文：[CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)；OpenAlex 记录：[W4226073959](https://openalex.org/W4226073959)。引文年份分布：2026 年 75、2025 年 63、2024 年 33、2023 年 14、2022 年 3。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2023 | [Code as Policies: Language Model Programs for Embodied Control](https://doi.org/10.1109/icra48891.2023.10160591) | conference-paper | 773 |
| 2023 | [Visual Language Maps for Robot Navigation](https://doi.org/10.1109/icra48891.2023.10160969) | conference-paper | 376 |
| 2023 | [Text2Motion: from natural language instructions to feasible plans](https://doi.org/10.1007/s10514-023-10131-7) | article | 219 |
| 2024 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration 0](https://doi.org/10.1109/icra57147.2024.10611477) | conference-paper | 198 |
| 2024 | [Transformer in reinforcement learning for decision-making: a survey](https://doi.org/10.1631/fitee.2300548) | article | 101 |
| 2023 | [Goal-Conditioned Imitation Learning using Score-based Diffusion Policies](https://doi.org/10.15607/rss.2023.xix.028) | conference-paper | 84 |
| 2025 | [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://doi.org/10.1109/access.2025.3609980) | article | 83 |
| 2022 | [What Matters in Language Conditioned Robotic Imitation Learning Over Unstructured Data](https://doi.org/10.1109/lra.2022.3196123) | article | 77 |

> 该记录共 188 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### LIBERO（基础套件）（被引 136）

来源论文：[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)；OpenAlex 记录：[W7133220882](https://openalex.org/W7133220882)。引文年份分布：2026 年 115、2025 年 18、2024 年 3。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Diffusion models for robotic manipulation: a survey](https://doi.org/10.3389/frobt.2025.1606247) | review | 33 |
| 2025 | [Exploring Embodied Multimodal Large Models: Development, datasets, and future directions](https://doi.org/10.1016/j.inffus.2025.103198) | article | 26 |
| 2025 | [Embodied AI: A Survey on the Evolution from Perceptive to Behavioral Intelligence](https://doi.org/10.1002/smb2.70003) | article | 22 |
| 2024 | [LOTUS: Continual Imitation Learning for Robot Manipulation Through Unsupervised Skill Discovery](https://doi.org/10.1109/icra57147.2024.10611129) | conference-paper | 21 |
| 2026 | [Bridging language and action: A survey of language-conditioned robot manipulation](https://doi.org/10.1177/02783649261468360) | article | 9 |
| 2026 | [Understanding Agentic AI: Algorithms and Infrastructure](https://doi.org/10.1109/jas.2026.125993) | article | 9 |
| 2025 | [CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance](https://doi.org/10.1109/iccv51701.2025.00910) | conference-paper | 9 |
| 2025 | [IRASim: A Fine-Grained World Model for Robot Manipulation](https://doi.org/10.1109/iccv51701.2025.00917) | conference-paper | 6 |

> 该记录共 136 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### Open X-Embodiment（被引 113）

来源论文：[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)；OpenAlex 记录：[W4387764390](https://openalex.org/W4387764390)。引文年份分布：2026 年 4、2025 年 40、2024 年 65、2023 年 2（另有 2 条记录年份早于来源论文，未计入）。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2024 | [Foundation models in robotics: Applications, challenges, and the future](https://doi.org/10.1177/02783649241281508) | article | 230 |
| 2024 | [Large language models for robotics: Opportunities, challenges, and perspectives](https://doi.org/10.1016/j.jai.2024.12.003) | article | 169 |
| 2024 | [Enhancing Autonomous System Security and Resilience With Generative AI: A Comprehensive Survey](https://doi.org/10.1109/access.2024.3439363) | article | 106 |
| 2024 | [Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action](https://doi.org/10.1109/cvpr52733.2024.02497) | conference-paper | 88 |
| 2025 | [Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning](https://doi.org/10.1126/scirobotics.ads5033) | article | 79 |
| 2024 | [RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot](https://doi.org/10.1109/icra57147.2024.10611615) | conference-paper | 78 |
| 2025 | [AIGC-empowered smart manufacturing: Prospects and challenges](https://doi.org/10.1016/j.rcim.2025.103076) | article | 67 |
| 2024 | [CoPa: General Robotic Manipulation through Spatial Constraints of Parts with Foundation Models](https://doi.org/10.1109/iros58592.2024.10801352) | conference-paper | 61 |

> 该记录共 113 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### NAVSIM（被引 63）

来源论文：[NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://doi.org/10.52202/079017-0902)；OpenAlex 记录：[W4415798424](https://openalex.org/W4415798424)。引文年份分布：2026 年 56、2025 年 7。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Combining Camera–LiDAR Fusion and Motion Planning Using Bird’s-Eye View Representation for End-to-End Autonomous Driving](https://doi.org/10.3390/drones9040281) | article | 12 |
| 2026 | [LLM4AD: Large Language Models for Autonomous Driving—Concept, Review, Benchmark, Experiments, and Future Trends](https://doi.org/10.1109/jproc.2026.3678829) | article | 8 |
| 2025 | [Research Challenges and Progress in the End-to-End V2X Cooperative Autonomous Driving Competition](https://doi.org/10.1109/iccvw69036.2025.00195) | conference-paper | 6 |
| 2026 | [DriveVA: Video Action Models are Zero-Shot Drivers](https://doi.org/10.1007/978-3-032-37718-0_19) | conference-paper | 5 |
| 2026 | [A Survey on Interaction-Aware Decision-Making for Autonomous Driving: Challenges, Solutions, and Perspectives](https://doi.org/10.1109/tits.2026.3678531) | article | 4 |
| 2025 | [SparseAD: Sparse Query-Centric Paradigm for Efficient End-to-End Autonomous Driving](https://doi.org/10.1109/tai.2025.3639457) | article | 4 |
| 2025 | [ConsistencyDrive: Efficient End-to-End Autonomous Driving with Consistency Models](https://doi.org/10.1109/crc67523.2025.11288252) | conference-paper | 3 |
| 2026 | [DIVER: Reinforced Diffusion Breaks Imitation Bottlenecks in End-to-End Autonomous Driving](https://doi.org/10.1109/tpami.2026.3708096) | article | 2 |

> 该记录共 63 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### SafeBench（被引 48）

来源论文：[SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682)；OpenAlex 记录：[W7133222348](https://openalex.org/W7133222348)。引文年份分布：2026 年 18、2025 年 12、2024 年 9、2023 年 8、2022 年 1。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2023 | [A Survey on Safety-Critical Driving Scenario Generation—A Methodological Perspective](https://doi.org/10.1109/tits.2023.3259322) | article | 269 |
| 2023 | [Synthetic Datasets for Autonomous Driving: A Survey](https://doi.org/10.1109/tiv.2023.3331024) | article | 102 |
| 2024 | [ChatScene: Knowledge-Enabled Safety-Critical Scenario Generation for Autonomous Vehicles](https://doi.org/10.1109/cvpr52733.2024.01464) | conference-paper | 92 |
| 2024 | [Reliability Engineering in a Time of Rapidly Converging Technologies](https://doi.org/10.1109/tr.2024.3355905) | article | 15 |
| 2024 | [OpenSBT: A Modular Framework for Search-based Testing of Automated Driving Systems](https://doi.org/10.1145/3639478.3640027) | conference-paper | 14 |
| 2024 | [Exploring the Potential of Multi-Modal AI for Driving Hazard Prediction](https://doi.org/10.1109/tiv.2024.3417353) | article | 10 |
| 2023 | [(Re) 2 H2O: Autonomous Driving Scenario Generation via Reversely Regularized Hybrid Offline-and-Online Reinforcement Learning](https://doi.org/10.1109/iv55152.2023.10186559) | conference-paper | 10 |
| 2026 | [A Survey on the Application of Large Language Models in Scenario-Based Testing of Automated Driving Systems](https://doi.org/10.1109/tits.2026.3651004) | article | 9 |

> 该记录共 48 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### RoboTwin（被引 30）

来源论文：[RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://doi.org/10.1109/CVPR52734.2025.02575)；OpenAlex 记录：[W4413144615](https://openalex.org/W4413144615)。引文年份分布：2026 年 23、2025 年 7。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://doi.org/10.1109/access.2025.3609980) | article | 83 |
| 2025 | [Embodied AI: A Survey on the Evolution from Perceptive to Behavioral Intelligence](https://doi.org/10.1002/smb2.70003) | article | 22 |
| 2026 | [PointVLA: Injecting the 3D World Into Vision-Language-Action Models](https://doi.org/10.1109/lra.2026.3653303) | article | 19 |
| 2026 | [From Data Mirror to Smart Copilot: A Survey on NextG Semantic Communication for Propelling Digital Twin World Into Cognitive Stage](https://doi.org/10.1109/comst.2026.3665395) | article | 17 |
| 2025 | [Physical AI: bridging the sim-to-real divide toward embodied, ethical, and autonomous intelligence](https://doi.org/10.1007/s44379-025-00050-y) | article | 13 |
| 2025 | [Design and Development of Cost-Effective Humanoid Robots for Enhanced Human–Robot Interaction](https://doi.org/10.3390/automation6030041) | article | 9 |
| 2025 | [GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://doi.org/10.1109/iccv51701.2025.00865) | conference-paper | 7 |
| 2026 | [Cooperative Control Framework for Dual-Arm Robot Enhanced by Vision Language Model and Reinforcement Learning](https://doi.org/10.1109/tase.2026.3660080) | article | 4 |

> 该记录共 30 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### COLOSSEUM（被引 29）

来源论文：[THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191)；OpenAlex 记录：[W4402354166](https://openalex.org/W4402354166)。引文年份分布：2026 年 8、2025 年 17、2024 年 4。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://doi.org/10.1109/access.2025.3609980) | article | 83 |
| 2025 | [Multimodal fusion and vision–language models: A survey for robot vision](https://doi.org/10.1016/j.inffus.2025.103652) | article | 52 |
| 2024 | [Unfolding the Literature: A Review of Robotic Cloth Manipulation](https://doi.org/10.1146/annurev-control-022723-033252) | review | 33 |
| 2025 | [Towards Generalizable Vision-Language Robotic Manipulation: A Benchmark and LLM-Guided 3D Policy](https://doi.org/10.1109/icra55743.2025.11127315) | conference-paper | 14 |
| 2025 | [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/iros60139.2025.11247088) | conference-paper | 13 |
| 2024 | [ViSaRL: Visual Reinforcement Learning Guided by Human Saliency](https://doi.org/10.1109/iros58592.2024.10801388) | conference-paper | 9 |
| 2025 | [Embodied intelligence for robot manipulation: development and challenges](https://doi.org/10.1007/s44336-025-00020-1) | article | 6 |
| 2025 | [Learning 4D Embodied World Models](https://doi.org/10.1109/iccv51701.2025.00507) | conference-paper | 6 |

> 该记录共 29 篇引文，这里只列被引最高的 25 篇，其余见结构化清单。

### ManiSkill / ManiSkill2（被引 24）

来源论文：[ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659)；OpenAlex 记录：[W4320165654](https://openalex.org/W4320165654)。引文年份分布：2026 年 2、2025 年 8、2024 年 13、2023 年 1。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2023 | [Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments](https://doi.org/10.1109/lra.2023.3270034) | article | 270 |
| 2025 | [Surgical embodied intelligence for generalized task autonomy in laparoscopic robot-assisted surgery](https://doi.org/10.1126/scirobotics.adt3093) | article | 55 |
| 2024 | [PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI](https://doi.org/10.1109/cvpr52733.2024.01539) | conference-paper | 54 |
| 2025 | [Empowering natural human–robot collaboration through multimodal language models and spatial intelligence: Pathways and perspectives](https://doi.org/10.1016/j.rcim.2025.103064) | article | 32 |
| 2024 | [The RL/LLM Taxonomy Tree: Reviewing Synergies Between Reinforcement Learning and Large Language Models](https://doi.org/10.1613/jair.1.15960) | article | 32 |
| 2025 | [A Survey of Embodied Learning for Object-centric Robotic Manipulation](https://doi.org/10.1007/s11633-025-1542-8) | article | 25 |
| 2024 | [Kinematic-aware Prompting for Generalizable Articulated Object Manipulation with LLMs](https://doi.org/10.1109/icra57147.2024.10610744) | conference-paper | 23 |
| 2024 | [RGBManip: Monocular Image-based Robotic Manipulation through Active Object Pose Estimation](https://doi.org/10.1109/icra57147.2024.10610690) | conference-paper | 17 |

> 共 24 篇，文档内只列 8 篇；结构化清单中为全部 24 篇。

### RoboMIND（被引 23）

来源论文：[RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](https://arxiv.org/abs/2412.13877)；OpenAlex 记录：[W4414050913](https://openalex.org/W4414050913)。引文年份分布：2026 年 11、2025 年 12。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://doi.org/10.1109/access.2025.3609980) | article | 83 |
| 2025 | [From screens to scenes: A survey of embodied AI in healthcare](https://doi.org/10.1016/j.inffus.2025.103033) | article | 51 |
| 2025 | [Embodied AI: A Survey on the Evolution from Perceptive to Behavioral Intelligence](https://doi.org/10.1002/smb2.70003) | article | 22 |
| 2025 | [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/iros60139.2025.11247088) | conference-paper | 13 |
| 2025 | [Embodied intelligence for robot manipulation: development and challenges](https://doi.org/10.1007/s44336-025-00020-1) | article | 6 |
| 2026 | [The trusted evolution framework: governing cognitive stability in self-evolving foundation models](https://doi.org/10.1007/s10044-026-01615-0) | article | 2 |
| 2026 | [Towards Generalizable Robotic Manipulation in Dynamic Environments](https://doi.org/10.1007/978-3-032-37592-6_18) | conference-paper | 2 |
| 2025 | [4D Visual Pre-Training for Robot Learning](https://doi.org/10.1109/iccv51701.2025.00791) | conference-paper | 2 |

> 共 23 篇，文档内只列 8 篇；结构化清单中为全部 23 篇。

### VLABench（被引 16）

来源论文：[VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://doi.org/10.1109/ICCV51701.2025.01037)；OpenAlex 记录：[W4405783861](https://openalex.org/W4405783861)。引文年份分布：2026 年 15、2025 年 1。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Diffusion models for robotic manipulation: a survey](https://doi.org/10.3389/frobt.2025.1606247) | review | 33 |
| 2026 | [Sensing the Action: Rethinking Sensor Modalities and Multi-Modal Fusion in Vision–Language–Action Models for Robotic Manipulation](https://doi.org/10.3390/s26113541) | review | 2 |
| 2026 | [Towards Generalizable Robotic Manipulation in Dynamic Environments](https://doi.org/10.1007/978-3-032-37592-6_18) | conference-paper | 2 |
| 2026 | [REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation](https://doi.org/10.1109/lra.2026.3692088) | article | 1 |
| 2026 | [Benchmark-path fidelity in parallel robot-policy evaluation: a CALVIN case study](https://doi.org/10.1007/s11227-026-08965-w) | article | 0 |
| 2026 | [Separating Execution and Target Selection in Vision–Language–Action Evaluation: A VLABench Case Study](https://doi.org/10.3390/robotics15100201) | article | 0 |
| 2026 | [VTP: A Task-Aware Transmission Protocol for Edge Vision-Language-Action Robotic Systems](https://doi.org/10.1109/iccc70295.2026.11680263) | conference-paper | 0 |
| 2026 | [Humanized-VLA: A Joint-Control VLA Fine-Tuning and Evaluation Framework Without Real Human Motion Demonstrations](https://doi.org/10.1109/aris70457.2026.11734530) | conference-paper | 0 |

> 共 16 篇，文档内只列 8 篇；结构化清单中为全部 16 篇。

### AgiBot World（被引 13）

来源论文：[AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088)；OpenAlex 记录：[W4416748905](https://openalex.org/W4416748905)。引文年份分布：2026 年 11、2025 年 2。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2026 | [PointVLA: Injecting the 3D World Into Vision-Language-Action Models](https://doi.org/10.1109/lra.2026.3653303) | article | 19 |
| 2026 | [X-Distill: Cross-Architecture Vision Distillation for Visuomotor Learning](https://doi.org/10.1109/lra.2026.3711479) | article | 0 |
| 2026 | [Proprioception Enhances Vision Language Model in Generating Captions and Subtask Segmentations for Robot Task](https://doi.org/10.1109/aim65483.2026.11658182) | conference-paper | 0 |
| 2026 | [Breaking the Resource Barrier: Parameter-Efficient Hierarchical VLA Fine-Tuning via Single-View Semantic Reasoning](https://doi.org/10.1109/ur69537.2026.11626770) | conference-paper | 0 |
| 2026 | [RoboTransfer: Controllable Geometry-Consistent Video Diffusion for Manipulation Policy Transfer](https://doi.org/10.1109/cvprf71909.2026.00140) | conference-paper | 0 |
| 2026 | [Learning Multi-Task Robot Trajectory Segmentation from Visual and Kinematic Streams](https://doi.org/10.1109/cvprf71909.2026.00144) | conference-paper | 0 |
| 2026 | [$A_{1}$: Adaptive Truncated Vision-Language-Action Model From Affordance to Action](https://doi.org/10.1109/cvprf71909.2026.00149) | conference-paper | 0 |
| 2026 | [OT-Curation: Sub-Trajectory Quality Estimation via State-Action Optimal Transport](https://doi.org/10.1109/ijcnn69854.2026.11730071) | conference-paper | 0 |

> 共 13 篇，文档内只列 8 篇；结构化清单中为全部 13 篇。

### BEHAVIOR-1K（被引 7）

来源论文：[BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation](https://arxiv.org/abs/2403.09227)；OpenAlex 记录：[W4392872989](https://openalex.org/W4392872989)。引文年份分布：2025 年 3、2024 年 4。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2024 | [Self-Driving Laboratories for Chemistry and Materials Science](https://doi.org/10.1021/acs.chemrev.4c00055) | review | 707 |
| 2024 | [YOLOv10 to Its Genesis: A Decadal and Comprehensive Review of The You Only Look Once Series](https://doi.org/10.20944/preprints202406.1366.v1) | preprint | 43 |
| 2025 | [A Survey of Embodied Learning for Object-centric Robotic Manipulation](https://doi.org/10.1007/s11633-025-1542-8) | article | 25 |
| 2025 | [Will multimodal large language models ever achieve deep understanding of the world?](https://doi.org/10.3389/fnsys.2025.1683133) | article | 6 |
| 2024 | [Designing AI to Think with Us, Not for Us](https://doi.org/10.1111/epic.12198) | conference-paper | 3 |
| 2024 | [YOLOv10 to Its Genesis: A Decadal and Comprehensive Review of The You Only Look Once Series](https://doi.org/10.20944/preprints202406.1366.v2) | preprint | 2 |
| 2025 | [WorldAPIs: The World Is Worth How Many APIs? A Thought Experiment](https://doi.org/10.1609/aaai.v39i23.34683) | conference-paper | 0 |

### Agent-SafetyBench（被引 6）

来源论文：[Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470)；OpenAlex 记录：[W4405627542](https://openalex.org/W4405627542)。引文年份分布：2026 年 4、2025 年 2。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies](https://doi.org/10.1145/3773080) | article | 62 |
| 2026 | [A Holistic Review of Agentic AI Frameworks, Applications, and Research Trajectories](https://doi.org/10.1007/s11831-026-10675-8) | article | 3 |
| 2026 | [Application and progress of artificial intelligence agents in drug development](https://doi.org/10.3724/zdxbyxb-2025-0697) | review | 1 |
| 2026 | [The rise of agentic AI in drug discovery from static tools to autonomous virtual scientists](https://doi.org/10.1038/s44386-026-00075-0) | review | 0 |
| 2026 | [Safeguarding LLM Agents from Misalignment through Provenance Analysis](https://doi.org/10.1145/3832783.3837535) | conference-paper | 0 |
| 2025 | [SafeServe: Scalable Tooling for Release Safety and Push Testing in Multi-App Monetization Platforms](https://doi.org/10.1109/ngdn66208.2025.11182150) | conference-paper | 0 |

### RoboCasa（被引 4）

来源论文：[RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)；OpenAlex 记录：[W4399424845](https://openalex.org/W4399424845)。引文年份分布：2025 年 4。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Empowering natural human–robot collaboration through multimodal language models and spatial intelligence: Pathways and perspectives](https://doi.org/10.1016/j.rcim.2025.103064) | article | 32 |
| 2025 | [BOSS: Benchmark for Observation Space Shift in Long-Horizon Task](https://doi.org/10.1109/lra.2025.3585390) | article | 3 |
| 2025 | [WorldAPIs: The World Is Worth How Many APIs? A Thought Experiment](https://doi.org/10.1609/aaai.v39i23.34683) | conference-paper | 0 |
| 2025 | [scene_synthesizer: A Python Library for Procedural Scene Generation in Robot Manipulation](https://doi.org/10.21105/joss.07561) | article | 0 |

### SimplerEnv（被引 4）

来源论文：[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)；OpenAlex 记录：[W4396822572](https://openalex.org/W4396822572)。引文年份分布：2026 年 1、2025 年 2、2024 年 1。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2024 | [Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes](https://doi.org/10.1146/annurev-control-030323-022510) | review | 188 |
| 2026 | [SimNav-XR: an extended reality platform for mobile robot simulation using ROS2 and Unity3D](https://doi.org/10.3389/frobt.2026.1708161) | article | 2 |
| 2025 | [Beyond performance: Explaining generalisation failures of Robotic Foundation Models in industrial simulation](https://doi.org/10.1016/j.birob.2025.100249) | article | 1 |
| 2025 | [Data-Driven Robotics in Practice](https://doi.org/10.1007/979-8-8688-0989-7_11) | book-chapter | 0 |

### IS-Bench（被引 2）

来源论文：[IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402)；OpenAlex 记录：[W7138977141](https://openalex.org/W7138977141)。引文年份分布：2026 年 2。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2026 | [HomeGuard: VLM-Based Embodied Safeguard for Identifying Contextual Risk in Household Task](https://doi.org/10.1007/978-3-032-37577-3_26) | conference-paper | 0 |
| 2026 | [From bits to atoms: A survey of cross-layer safety in Embodied AI](https://doi.org/10.59717/ipj.aiplus.2026.100013) | article | 0 |

### SafeAgentBench（被引 2）

来源论文：[SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)；OpenAlex 记录：[W4405562840](https://openalex.org/W4405562840)。引文年份分布：2025 年 2。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies](https://doi.org/10.1145/3773080) | article | 62 |
| 2025 | [Bridging Today and the Future of Humanity: AI Safety in 2024 and Beyond](https://doi.org/10.32388/zhm9uq) | preprint | 1 |

### EmbodiedBench（被引 1）

来源论文：[EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560)；OpenAlex 记录：[W4407590542](https://openalex.org/W4407590542)。引文年份分布：2025 年 1。

| 年份 | 论文 | 类型 | 被引 |
|---|---|---|---:|
| 2025 | [Robocskbench: Benchmarking Embodied Commonsense Capabilities of Large Language Models](https://doi.org/10.1109/ur65550.2025.11078036) | conference-paper | 0 |

## 4. 引文图中暂无引文、但 arXiv 摘要提到该 benchmark 的论文

这些论文的标题或摘要里出现 benchmark 名称，但 OpenAlex 的引文图还没有把原论文记为其参考文献。可能是新论文的参考文献解析延迟，也可能只是提到名字。**这是候选列表，不是引用证据**；每条附命中的上下文片段，便于逐条判断它在说“我们用了它”还是别的。名称本身有歧义的条目不在此列，见第 6 节。命中数只统计**已取回的一页**（最多 50 条）：检索池大于 50 时标成 `≥N`，是下界而不是全量。名称按整词匹配，但派生名也会算命中（例如 `LIBERO` 会命中 `LIBERO-Safety`、`LIBERO-Para` 这类行文），因此这一列的误差偏向“宽”，不能当作精确引用数。

“题名”列标 ✔ 表示该名称出现在论文标题里，而不是正文摘要。

### RoboCasa365（摘要命中 32 篇）

来源论文：[RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"RoboCasa365"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2026 | [MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinating and Imagining](https://arxiv.org/abs/2609.35652) |  | cs.RO |
| 2026 | [Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents](https://arxiv.org/abs/2609.39304) |  | cs.RO |
| 2026 | [Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies](https://arxiv.org/abs/2610.14155) |  | cs.RO |
| 2026 | [MOST: Memory of Object States and Task Progress for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2611.00734) |  | cs.RO |
| 2026 | [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939) |  | cs.CV |
| 2026 | [REKI: Registering Knowledge in VLAs](https://arxiv.org/abs/2610.22178) |  | cs.RO |
| 2026 | [StructRL: Online Structured Reinforcement Learning for Long-Horizon Vision-Language-Action Tasks](https://arxiv.org/abs/2609.36352) |  | cs.CV |
| 2026 | [Can World and Action Modeling Benefit Each Other under Unified Causal Training?](https://arxiv.org/abs/2610.21095) |  | cs.CV |

命中上下文：

- 2609.35652v1：…iction. In controlled ablations, replacing clean-action prediction with velocity prediction lowers success on RoboCasa365 composite-seen tasks from 32.8% to 29.2%, and removing future supervision or multilevel conditioning causes l…
- 2609.39304v4：…ination back into the policy with multi-teacher on-policy distillation yields a standalone policy at 62.2% on RoboCasa365 under the official protocol, 4.8 points above its starting point with no harness at inference; the evolved ha…
- 2610.14155v1：…int optimization of the supervised VLM layers, VAIR, and the action generator connects the two components. On RoboCasa365, Axiom-0 achieves 62.32% overall success in our evaluation, exceeding the highest published leaderboard score…
- 2611.00734v1：…e further introduce RoboCasa-Long, a benchmark of multi-minute, multi-stage mobile manipulation tasks. Across RoboCasa365, RoboCasa-Long, and real-world robot experiments, MOST consistently outperforms Xiaomi-Robotics-1 (XR-1), the…
- 2610.01939v2：…nly the images and state they request. Across 700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365, it raises success from 63.1% to 71.7% over tool calling with the same GPT-6 Astra planner and primitives, us…
- 2610.22178v1：…a that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) follo…

> 命中 32 篇，此处列被引／相关性最高的 8 篇，其余见结构化清单。

### SafeLIBERO（摘要命中 7 篇）

来源论文：[VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"SafeLIBERO"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2026 | [Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models](https://arxiv.org/abs/2611.01713) |  | cs.AI |
| 2026 | [SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Model](https://arxiv.org/abs/2606.20698) |  | cs.RO |
| 2026 | [DetAug: Obstacle-Blind Trajectory Augmentation for Zero-shot Obstacle Avoidance](https://arxiv.org/abs/2609.18395) |  | cs.RO |
| 2026 | [VLPSA: Vision-Language-Poisson-Safe Actions for Full-Body Safety of Learned Policies](https://arxiv.org/abs/2609.22462) |  | cs.RO |
| 2026 | [WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation](https://arxiv.org/abs/2610.01083) |  | cs.RO |
| 2026 | [Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching](https://arxiv.org/abs/2607.01378) |  | cs.RO |
| 2026 | [Your Model Already Knows: Attention-Guided Safety Filter for Vision-Language-Action Models](https://arxiv.org/abs/2606.09749) |  | cs.RO |

命中上下文：

- 2611.01713v1：…te is added to the CBF-QP objective as a soft guidance term, while the CBF safety constraint remains hard. On SafeLIBERO, our method improves collision avoidance, task success, and SafeSuccess compared with AEGIS. Our project page…
- 2606.20698v2：…execution and trajectory safety. These decoupled signals are balanced through Lagrangian-constrained GRPO. On SafeLIBERO Level I, SafeDojo improves average safe-success rate by 8.25 percentage points over the strongest baseline; o…
- 2609.18395v1：…At inference it samples a batch of labels and executes the trajectory with the lowest collision cost. On the SafeLIBERO benchmark DetAug achieves a collision-free success rate more than 20pp above the next best method, and select…
- 2609.22462v1：…ask regions, VLPSA combines dual resolutions of this PSF using Boolean CBF compositions. We evaluate VLPSA on SafeLIBERO against safety-filtering baselines, where it achieves the highest collision avoidance rate among the evaluate…
- 2610.01083v2：…mensional operational-space action for collision avoidance across robot, scene, and attached geometry. On the SafeLIBERO benchmark, a variant of LIBERO augmented with obstacles for safety evaluation, WBAG achieves the best overall…
- 2607.01378v1：…neural trajectory generation enables predictive collision avoidance rather than reactive intervention. On the SafeLIBERO benchmark, our method achieves 82.8% collision avoidance and 81.6% task success, a 6.3% and 19.8% improvement…

### VLA-Arena（摘要命中 6 篇）

来源论文：[VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"VLA-Arena"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2026 | [Frequency-Conditioned Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2609.10405) |  | cs.RO |
| 2026 | [LoopVLA: Learning Sufficiency in Recurrent Refinement for Vision-Language-Action Models](https://arxiv.org/abs/2605.09948) |  | cs.AI |
| 2026 | [ActionPiece: Rethinking Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2609.18487) |  | cs.RO |
| 2026 | [Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models](https://arxiv.org/abs/2609.39820) |  | cs.RO |
| 2026 | [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671) |  | cs.RO |
| 2026 | [Triggering Generalist Reasoning via Predictive Uncertainty for Dual-System VLA](https://arxiv.org/abs/2610.05025) |  | cs.CV |

命中上下文：

- 2609.10405v1：…into existing Flow Matching action experts without changing the VLA backbone. Across LIBERO, LIBERO-Plus, and VLA-Arena, FreqFM consistently improves performance, including a 9.3-point gain on LIBERO-Plus, and further demonstrate…
- 2605.09948v2：…thereby linking sufficiency learning to policy optimization signals. Experiments on LIBERO, LIBERO-Plus, and VLA-Arena show that LoopVLA pushes the efficiency-performance frontier of VLA policies, reducing parameters by 45% and…
- 2609.18487v1：…RO and 68.8% on unseen LIBERO-Plus, with additional evaluations reaching 71.9% on SimplerEnv and 51.5% across VLA-Arena L0-L2. Component ablations show that the two objectives jointly improve PRC and policy success, demonstrating…
- 2609.39820v1：…retains successful uncorrected actions as quiet anchors for guarded LoRA updates. We evaluate FailBank on the VLA-Arena benchmark across two difficulty levels and two VLA backbones. Compared with the base policies, FailBank impro…
- 2608.11671v1：…ence uses the action expert alone, preserving real-time, high-frequency control with no added latency. On the VLA-Arena leaderboard(Aug 1, 2026), StellaVLA ranks first with an overall score of 0.63, versus 0.44 and 0.22 for the s…
- 2610.05025v2：…s the architecture already runs, requiring neither manual phase labels nor an auxiliary uncertainty model. On VLA-Arena, it achieves a higher success rate at matched call budgets than alternative uncertainty baselines while maint…

### LIBERO-Para（摘要命中 3 篇）

来源论文：[LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"LIBERO-Para"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2026 | [WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction](https://arxiv.org/abs/2610.18568) |  | cs.RO |
| 2026 | [Grounded Semantic Re-Binding for Robust Instruction Generalization in Vision-Language-Action Models](https://arxiv.org/abs/2608.02497) |  | cs.RO |
| 2026 | [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562) |  | cs.RO |

命中上下文：

- 2610.18568v1：…1.47% on RoboTwin 2.0 and 98.7% on LIBERO, along with 88.0%, 61.4%, and 75.0% on LIBERO-Plus, LIBERO-Pro, and LIBERO-Para, respectively. On real-world tasks, it improves the success rate of $π_{0.5}$ from 38.3% to 73.3%. These resu…
- 2608.02497v1：…rgeted intervention dramatically restores paraphrastic invariance using only canonical demonstrations. On the LIBERO-Para benchmark, GSR improves success rates by up to 44.6 percent. It enables lightweight models to rival massively…
- 2609.25562v2：…tely evaluates clean capability on LIBERO, non-language robustness on LIBERO-Plus, instruction sensitivity on LIBERO-Para, and observed execution cost. Reported task scores aggregate three complete evaluations with distinct random…

### LIBERO-Safety（摘要命中 2 篇）

来源论文：[LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"LIBERO-Safety"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2026 | [FabriVLA: A Lightweight Vision-Language-Action Model with Conformal Action Chunk Uncertainty](https://arxiv.org/abs/2607.08575) |  | cs.RO |
| 2026 | [VLA-ULAP: Interleaving Cloud VLA Calls with Ultra-Lightweight Local Action Prediction at the Edge](https://arxiv.org/abs/2609.18663) |  | cs.RO |

命中上下文：

- 2607.08575v3：…at a user chosen confidence level, 3.3$\times$ tighter in mean radius than an unconditional conformal set. On LIBERO-Safety, these bounds rank rollouts by risk before execution, supporting risk ranked review. Together, FabriVLA and J…
- 2609.18663v2：…LA-ULAP exceed $π_{0.5}$'s success rate by 11.0 and 15.5 percentage points (pp) on two tasks in latency-aware LIBERO-Safety simulation while approximately halving VLA calls.

### Spa-Bench（摘要命中 2 篇）

来源论文：[Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"Spa-Bench"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2026 | [Benchmarking LLM Judges for Mobile Agent Evaluation](https://arxiv.org/abs/2608.11434) |  | cs.AI |
| 2026 | [OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools](https://arxiv.org/abs/2610.14157) |  | cs.SE |

命中上下文：

- 2608.11434v1：…anning 6 mobile agent benchmarks, 4 agent models, and 68 apps. We evaluate 6 judge methods (five adapted from SPA-Bench, A3 with two modes, AndroidArena, and AgentRewardBench, plus a simple baseline we design) across multiple LLM…
- 2610.14157v1：…ld (79.9) and MobileWorld (50.4), while showing promising transfer to real-device mobile use, nearly doubling SPA-Bench performance from 31.9 to 59.6. All resources are available at https://os-copilot.github.io/OpenMobile2-Home/.

### ASIMOV Benchmark（摘要命中 1 篇）

来源论文：[Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)；检索式 `(cat:cs.RO OR cat:cs.CV) AND abs:"ASIMOV Benchmark"`。

| 年份 | 论文 | 题名 | 分类 |
|---|---|---|---|
| 2025 | [SciFi-Benchmark: Leveraging Science Fiction To Improve Robot Behavior](https://arxiv.org/abs/2503.10706) |  | cs.CL |

命中上下文：

- 2503.10706v2：…setting (23.3% to 92.3%). Additionally, we find that those constitutions are among the top performers on the ASIMOV Benchmark which is derived from real-world images and hospital injury reports. Sci-Fi-inspired constitutions are thus h…

## 5. 两种口径下都没有线索的条目

既无 OpenAlex 引文，arXiv 摘要检索也没有命中。多数是 2026 年的新条目，收录与引用都有延迟；这只是“本轮没查到”，不是“无人使用”。

| 条目 | 来源论文 | 观测 |
|---|---|---|
| [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) | ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models | 被引 0，摘要无命中 |
| [HazardArena](../benchmarks/1__HazardArena.md) | HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models | 被引 0，摘要无命中 |
| [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) | ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation | 被引 0，摘要无命中 |
| [RoboHarm](../benchmarks/1__RoboHarm.md) | Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control | 被引 0，摘要无命中 |
| [SafeStage](../benchmarks/1__SafeStage.md) | SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation | 被引 0，摘要无命中 |
| [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) | TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes | 被引 0，摘要无命中 |
| [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) | Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation | 被引 0，摘要无命中 |
| [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) | LIBERO-MAX: Do Robot Policies Adapt When the World Changes? | 被引 0，摘要无命中 |
| [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) | LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models | 被引 0，摘要无命中 |
| [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) | LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models | 被引 0，摘要无命中 |
| [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) | RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation | 被引 0，摘要无命中 |
| [BiDex-100](../benchmarks/3__BiDex-100.md) | BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks | 被引 0，摘要无命中 |
| [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) | IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models | 被引 0，摘要无命中 |
| [RoboChrono](../benchmarks/3__RoboChrono.md) | RoboChrono: A Real Robot Benchmark for Streaming Task Understanding | 被引 0，摘要无命中 |
| [RoboComb](../benchmarks/3__RoboComb.md) | Exploring the Limits of Combinatorial Generalization in Embodied Manipulation | 被引 0，摘要无命中 |
| [RoboFollow](../benchmarks/3__RoboFollow.md) | RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents | 被引 0，摘要无命中 |
| [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) | RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models | 被引 0，摘要无命中 |
| [RoboReel](../benchmarks/3__RoboReel.md) | Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation | 被引 0，摘要无命中 |
| [Bench2Dex](../benchmarks/4__Bench2Dex.md) | Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands | 被引 0，摘要无命中 |
| [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) | EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems | 被引 0，摘要无命中 |
| [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) | HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots | 被引 0，摘要无命中 |
| [LABIT](../benchmarks/4__LABIT.md) | LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks | 被引 0，摘要无命中 |
| [MSK-Bench](../benchmarks/4__MSK-Bench.md) | MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics | 被引 0，摘要无命中 |
| [MemForm](../benchmarks/4__MemForm.md) | MemForm: Benchmarking Memory Formation Poisoning in LLM Agents | 被引 0，摘要无命中 |
| [MineAmongUs](../benchmarks/4__MineAmongUs.md) | Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions | 被引 0，摘要无命中 |
| [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) | Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion | 被引 0，摘要无命中 |
| [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) | PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI | 被引 0，摘要无命中 |
| [RoboAbstention](../benchmarks/4__RoboAbstention.md) | The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents | 被引 0，摘要无命中 |
| [RoboJailBench](../benchmarks/4__RoboJailBench.md) | RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents | 被引 0，摘要无命中 |
| [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) | SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces | 被引 0，摘要无命中 |

## 6. 名称歧义：这些条目的 arXiv 命中不能当计数

以下名称是常用词、常用动词或与别的项目重名，arXiv 检索会返回大量无关论文，因此本报告不给这些条目报“命中数”，只保留检索记录和少量示例，用来说明为什么不用它计数。要判断谁用了它，应回到引文图或人工核对。

| 条目 | 原因 | 检索式 | 示例命中（不作证据） |
|---|---|---|---|
| DESPITE | despite 是常用英文词，命中的绝大多数与该论文无关 | `(cat:cs.RO OR cat:cs.CV) AND abs:"DESPITE"` | DeSPITE: Exploring Contrastive Deep Skeleton-Pointcloud-IMU-Text Embeddings for  |
| INFUSE | infuse 是常用动词，命中含大量无关工作 | `(cat:cs.RO OR cat:cs.CV) AND abs:"INFUSE"` | VCC-INFUSE: Towards Accurate and Efficient Selection of Unlabeled Examples in Se |
| IS-Bench | 检索器把 IS-Bench 拆成 IS／Bench 两个泛词，命中与本题无关 | `(cat:cs.RO OR cat:cs.CV) AND abs:"IS-Bench"` | — |
| ORBIT | orbit 是常用名词，命中的多数与 ORBIT 框架无关 | `(cat:cs.RO OR cat:cs.CV) AND abs:"ORBIT"` | Orbit-Planner: Towards Latent World Models for On-Orbit Obstacle Avoidance of Sa |
| STARS | stars 是常用名词，命中的多数与 STARS 方法无关 | `(cat:cs.RO OR cat:cs.CV) AND abs:"STARS"` | STARS: Self-supervised Tuning for 3D Action Recognition in Skeleton Sequences |
| SafeBench | SafeBench 同时被自动驾驶与多模态 LLM 安全两类工作使用，需按正文区分 | `(cat:cs.RO OR cat:cs.CV) AND abs:"SafeBench"` | Jailbreak Large Vision-Language Models Through Multi-Modal Linkage |
| VIPS | VIPS 同时是图像处理库名与多个项目的缩写 | `(cat:cs.RO OR cat:cs.CV) AND abs:"VIPS"` | Beyond Single Expert: Harmonizing Diverse Visual Priors in MLLMs for Spatial Und |

## 7. 查询记录与后续

查询接口、参数与失败原因见 JSON 的 `queries`／`errors` 字段；每个计数都是单条记录的一次观测，跨日期比较时须带上观测日期。

把它升级为“采用审计”需要逐篇打开引文论文，记录实验章节／表格、所用任务版本、作者与原团队的关系，以及是运行了该 benchmark 还是只引用。当前清单只提供入口，不提供这个结论。
