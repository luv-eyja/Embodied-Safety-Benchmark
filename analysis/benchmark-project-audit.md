# Benchmark 项目地址审计

审计范围：`data/benchmark_cards.json` 中的 122 个 benchmark；审计日期：2026-11-01。
本表区分 benchmark 自己的项目地址和它依托的平台地址，避免把 LIBERO、CARLA、nuScenes 等基础平台误当成每个派生 benchmark 的独立项目。

| 状态 | 含义 | 数量 |
|---|---|---:|
| `found` | 已确认论文项目链接或官方项目/代码页 | 47 |
| `platform_only` | 只有依托平台地址 | 12 |
| `candidate` | 名称匹配但官方归属待确认 | 3 |
| `not_found` | 本轮未确认项目地址 | 60 |

## 全量清单

| Benchmark | 状态 | 项目地址 | 论文来源 | 发现方式 / 备注 |
|---|---|---|---|---|
| AGENTSAFE / SAFE-THOR | `not_found` | — | [论文](https://arxiv.org/abs/2506.14697) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| ASIMOV Benchmark | `found` | [https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/) | [论文](https://arxiv.org/abs/2503.08663) | manual_official_or_platform_check；Official ASIMOV Benchmark project page. |
| AeroIntent | `not_found` | — | [论文](https://arxiv.org/abs/2610.25869) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Agent-SafetyBench | `found` | [https://github.com/thu-coai/Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) | [论文](https://arxiv.org/abs/2412.14470) | arxiv_abs；Project/code links extracted from arXiv abs page 2412.14470. |
| AgiBot World | `found` | [https://agibot-world.com/](https://agibot-world.com/)、[https://github.com/OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World) | [论文](https://doi.org/10.1109/IROS60139.2025.11247088) | manual_official_or_platform_check；Official project site and code repository. |
| BAVO-Bench | `found` | [https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench) | [论文](https://arxiv.org/abs/2609.37292) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.37292. |
| BEHAVIOR-1K | `platform_only` | [https://behavior.stanford.edu/](https://behavior.stanford.edu/) | [论文](https://arxiv.org/abs/2610.12089) | manual_official_or_platform_check；Canonical BEHAVIOR platform page; no separate project page for the registry entry was confirmed. |
| BLINDSPOT | `not_found` | — | [论文](https://arxiv.org/abs/2609.16305) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Balanced Multi-Robot Task Allocation Benchmark | `not_found` | — | [论文](https://arxiv.org/abs/2609.13711) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Bench2Dex | `found` | [https://bench2dex.github.io](https://bench2dex.github.io) | [论文](https://arxiv.org/abs/2609.15726) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.15726. |
| Bench2Drive | `not_found` | — | [论文](https://doi.org/10.52202/079017-0025) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| BiDex-100 | `found` | [https://robbyant-research.github.io/BiDex-100](https://robbyant-research.github.io/BiDex-100) | [论文](https://arxiv.org/abs/2610.25459) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.25459. |
| CALVIN | `platform_only` | [https://calvin-robot.github.io/](https://calvin-robot.github.io/)、[https://github.com/mees/calvin](https://github.com/mees/calvin) | [论文](https://arxiv.org/abs/2112.03227) | manual_official_or_platform_check；Canonical CALVIN project/code page. |
| CAPSafe | `not_found` | — | [论文](https://arxiv.org/abs/2610.28381) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| CARLA / CARLA Leaderboard | `platform_only` | [https://carla.org/](https://carla.org/)、[https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla) | [论文](https://arxiv.org/abs/2511.14876) | manual_official_or_platform_check；Canonical CARLA simulator pages; leaderboard-specific project page not confirmed. |
| COLOSSEUM | `found` | [https://robot-colosseum.github.io](https://robot-colosseum.github.io) | [论文](https://arxiv.org/abs/2402.08191) | arxiv_abs；Project/code links extracted from arXiv abs page 2402.08191. |
| COMPASS / X-Mobility | `not_found` | — | [论文](https://arxiv.org/abs/2610.28432) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| DESPITE | `found` | [https://despite-safety.github.io](https://despite-safety.github.io) | [论文](https://arxiv.org/abs/2604.18463) | arxiv_abs；Project/code links extracted from arXiv abs page 2604.18463. |
| DPed-VLN | `not_found` | — | [论文](https://arxiv.org/abs/2609.21504) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| DUMA-Bench | `not_found` | — | [论文](https://arxiv.org/abs/2609.24662) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| DriveDegrade | `not_found` | — | [论文](https://arxiv.org/abs/2608.29005) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Embodied Agent Interface | `not_found` | — | [论文](https://doi.org/10.52202/079017-3188) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| EmbodiedBench | `found` | [https://embodiedbench.github.io](https://embodiedbench.github.io) | [论文](https://arxiv.org/abs/2502.09560) | arxiv_abs；Project/code links extracted from arXiv abs page 2502.09560. |
| EmbodiedGovBench | `found` | [https://github.com/s20sc/embodied-gov-bench](https://github.com/s20sc/embodied-gov-bench) | [论文](https://arxiv.org/abs/2604.11174) | arxiv_abs；Project/code links extracted from arXiv abs page 2604.11174. |
| Everyday-Environment Robot Benchmarking | `not_found` | — | [论文](https://arxiv.org/abs/2609.26490) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| ExceptionDrive | `not_found` | — | [论文](https://arxiv.org/abs/2609.37871) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| ForesightSafety-VLA | `found` | [https://github.com/tuotuoLyu/ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA) | [论文](https://arxiv.org/abs/2606.27079) | manual_official_or_platform_check；GitHub repository found by exact benchmark-title search. |
| GaugeBench | `not_found` | — | [论文](https://arxiv.org/abs/2610.07597) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| GuardianBench | `not_found` | — | [论文](https://arxiv.org/abs/2608.21928) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| HASARD | `not_found` | — | [论文](https://arxiv.org/abs/2503.08241) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| HUGE-Bench | `not_found` | — | [论文](https://doi.org/10.1007/978-3-032-37167-6_21) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| HazardArena | `found` | [https://github.com/HazardArena-Team/HazardArena](https://github.com/HazardArena-Team/HazardArena) | [论文](https://arxiv.org/abs/2604.12447) | arxiv_abs；Project/code links extracted from arXiv abs page 2604.12447. |
| HygieneRoboBench | `found` | [https://euron-zc.github.io/HygieneRoboBench](https://euron-zc.github.io/HygieneRoboBench) | [论文](https://arxiv.org/abs/2610.08642) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.08642. |
| INFUSE | `found` | [https://github.com/judydnguyen/infuse](https://github.com/judydnguyen/infuse) | [论文](https://arxiv.org/abs/2610.20776) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.20776. |
| IS-Bench | `found` | [https://github.com/AI45Lab/IS-Bench](https://github.com/AI45Lab/IS-Bench) | [论文](https://arxiv.org/abs/2506.16402) | arxiv_abs；Project/code links extracted from arXiv abs page 2506.16402. |
| ISO-based Humanoid Orchestrator Benchmark | `not_found` | — | [论文](https://arxiv.org/abs/2609.07288) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| IndustrialVLA-Bench | `found` | [https://github.com/xiaoqi-7/IndustrialVLA-Bench](https://github.com/xiaoqi-7/IndustrialVLA-Bench) | [论文](https://arxiv.org/abs/2609.25562) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.25562. |
| Inspect Robots | `not_found` | — | [论文](https://arxiv.org/abs/2610.06306) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| LABIT | `found` | [https://irp-hka.github.io/robotic-assembly-benchmark](https://irp-hka.github.io/robotic-assembly-benchmark) | [论文](https://arxiv.org/abs/2610.16398) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.16398. |
| LIBERO-CTRL | `not_found` | — | [论文](https://arxiv.org/abs/2609.15940) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| LIBERO-MAX | `found` | [https://liberomax.github.io](https://liberomax.github.io) | [论文](https://arxiv.org/abs/2609.36518) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.36518. |
| LIBERO-Para | `found` | [https://github.com/xiaoqi-7/IndustrialVLA-Bench](https://github.com/xiaoqi-7/IndustrialVLA-Bench) | [论文](https://arxiv.org/abs/2609.25562) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.25562. |
| LIBERO-Plus | `not_found` | — | [论文](https://arxiv.org/abs/2510.13626) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| LIBERO-Pro2.0 | `not_found` | — | [论文](https://arxiv.org/abs/2610.24587) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| LIBERO-RECOVER | `found` | [https://liulin815.github.io/LIBERO-Recovery](https://liulin815.github.io/LIBERO-Recovery) | [论文](https://arxiv.org/abs/2609.05178) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.05178. |
| LIBERO-RIG | `not_found` | — | [论文](https://arxiv.org/abs/2610.18843) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| LIBERO-Safety | `found` | [https://libero-safety.github.io](https://libero-safety.github.io) | [论文](https://arxiv.org/abs/2606.23686) | arxiv_abs；Project/code links extracted from arXiv abs page 2606.23686. |
| LIBERO-VPro | `found` | [https://huiqiongli.github.io/LIBERO-VPro](https://huiqiongli.github.io/LIBERO-VPro) | [论文](https://arxiv.org/abs/2609.24350) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.24350. |
| LIBERO-X | `not_found` | — | [论文](https://arxiv.org/abs/2602.06556) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| LIBERO（基础套件） | `platform_only` | [https://libero-project.github.io/main.html](https://libero-project.github.io/main.html) | [论文](https://arxiv.org/abs/2609.03715) | manual_official_or_platform_check；Canonical LIBERO project page. |
| LongBench | `not_found` | — | [论文](https://arxiv.org/abs/2604.16788) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| MAGMA-Bench | `not_found` | — | [论文](https://arxiv.org/abs/2610.13534) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| MMA-SafetyBench | `not_found` | — | [论文](https://arxiv.org/abs/2610.19384) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| MSK-Bench | `found` | [https://zzongzheng0918.github.io/MSK-Bench](https://zzongzheng0918.github.io/MSK-Bench) | [论文](https://arxiv.org/abs/2609.26872) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.26872. |
| ManiGuard-Bench | `not_found` | — | [论文](https://arxiv.org/abs/2608.17386) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| ManiPhysicsBench | `candidate` | [https://github.com/sangwu99/ManiPhysicsBench_Arxiv](https://github.com/sangwu99/ManiPhysicsBench_Arxiv) | [论文](https://arxiv.org/abs/2610.02802) | manual_official_or_platform_check；Repository matches the benchmark title, but the paper page does not link it explicitly. |
| ManiSkill / ManiSkill2 | `platform_only` | [https://maniskill2.github.io/](https://maniskill2.github.io/) | [论文](https://arxiv.org/abs/2302.04659) | manual_official_or_platform_check；Canonical ManiSkill2 project page. |
| ManiUnit | `not_found` | — | [论文](https://arxiv.org/abs/2610.12089) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| MemForm | `found` | [https://github.com/opanhw/memform-code](https://github.com/opanhw/memform-code) | [论文](https://arxiv.org/abs/2610.14431) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.14431. |
| MemTransfer | `not_found` | — | [论文](https://arxiv.org/abs/2609.32313) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| MineAmongUs | `found` | [https://junseokim0103.github.io/Lies-We-Can-See](https://junseokim0103.github.io/Lies-We-Can-See) | [论文](https://arxiv.org/abs/2608.30428) | arxiv_abs；Project/code links extracted from arXiv abs page 2608.30428. |
| MotionForge | `not_found` | — | [论文](https://arxiv.org/abs/2609.25689) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| NAVSIM | `found` | [https://github.com/autonomousvision/navsim](https://github.com/autonomousvision/navsim) | [论文](https://doi.org/10.52202/079017-0902) | manual_official_or_platform_check；Official NAVSIM repository. |
| ORBIT | `found` | [https://github.com/wlanderson0/orbit](https://github.com/wlanderson0/orbit) | [论文](https://arxiv.org/abs/2609.33102) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.33102. |
| ORDER | `not_found` | — | [论文](https://arxiv.org/abs/2609.22285) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Open X-Embodiment | `platform_only` | [https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)、[https://github.com/google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment) | [论文](https://doi.org/10.1109/IROS60139.2025.11247088) | manual_official_or_platform_check；Canonical OXE project/code pages. |
| PASTABench | `not_found` | — | [论文](https://arxiv.org/abs/2609.28197) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| PLCBENCH | `not_found` | — | [论文](https://arxiv.org/abs/2608.26882) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Peg-in-Bench | `found` | [https://github.com/aistairc/peg-in-bench](https://github.com/aistairc/peg-in-bench) | [论文](https://arxiv.org/abs/2609.00906) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.00906. |
| PhysAI-Bench | `found` | [https://github.com/maferrag/physai-bench](https://github.com/maferrag/physai-bench) | [论文](https://arxiv.org/abs/2609.23695) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.23695. |
| Physics-Consistent HRI Benchmark | `not_found` | — | [论文](https://arxiv.org/abs/2609.02402) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| PolaRiS | `not_found` | — | [论文](https://doi.org/10.15607/RSS.2026.XXII.062) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| R2R-CE | `not_found` | — | [论文](https://arxiv.org/abs/2610.14682) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| REVERSAL-BENCH | `not_found` | — | [论文](https://arxiv.org/abs/2609.17745) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RT-Safe | `not_found` | — | [论文](https://arxiv.org/abs/2610.09294) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Radar2Plan | `not_found` | — | [论文](https://arxiv.org/abs/2610.06121) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Robo2Process | `not_found` | — | [论文](https://arxiv.org/abs/2606.13040) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RoboAbstention | `found` | [https://purseclab.github.io/RoboAbstention](https://purseclab.github.io/RoboAbstention) | [论文](https://arxiv.org/abs/2605.20544) | arxiv_abs；Project/code links extracted from arXiv abs page 2605.20544. |
| RoboCasa | `platform_only` | [https://robocasa.ai/](https://robocasa.ai/) | [论文](https://arxiv.org/abs/2610.27861) | manual_official_or_platform_check；Canonical RoboCasa project page. |
| RoboCasa-Shift | `found` | [https://github.com/HaochengWang23/RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift) | [论文](https://arxiv.org/abs/2610.27861) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.27861. |
| RoboCasa365 | `platform_only` | [https://robocasa.ai/](https://robocasa.ai/) | [论文](https://arxiv.org/abs/2610.27861) | manual_official_or_platform_check；Canonical RoboCasa project page hosts RoboCasa365. |
| RoboChrono | `found` | [https://continuity3.github.io/robochrono](https://continuity3.github.io/robochrono)、[https://github.com/mfan-res/ROBOCHRONO](https://github.com/mfan-res/ROBOCHRONO) | [论文](https://arxiv.org/abs/2609.36605) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.36605. |
| RoboColiseum | `not_found` | — | [论文](https://arxiv.org/abs/2610.27865) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RoboComb | `found` | [https://github.com/AutoLab-SAI-SJTU/RoboCombine](https://github.com/AutoLab-SAI-SJTU/RoboCombine) | [论文](https://arxiv.org/abs/2610.15425) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.15425. |
| RoboDojo | `not_found` | — | [论文](https://arxiv.org/abs/2609.24170) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RoboEval | `not_found` | — | [论文](https://doi.org/10.1109/ICRA57385.2026.11697082) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RoboFollow | `found` | [https://github.com/AutoLab-SAI-SJTU/RoboFollow](https://github.com/AutoLab-SAI-SJTU/RoboFollow) | [论文](https://arxiv.org/abs/2609.25636) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.25636. |
| RoboHarm | `candidate` | [https://github.com/robocurve/roboharm](https://github.com/robocurve/roboharm) | [论文](https://arxiv.org/abs/2610.14043) | manual_official_or_platform_check；Repository matches the benchmark title, but authorship/official status needs confirmation. |
| RoboIRG-Bench | `found` | [https://aernar.github.io/RoboIRGBench](https://aernar.github.io/RoboIRGBench) | [论文](https://arxiv.org/abs/2609.34384) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.34384. |
| RoboJailBench | `found` | [https://purseclab.github.io/benchmark-for-robotics-security](https://purseclab.github.io/benchmark-for-robotics-security) | [论文](https://arxiv.org/abs/2605.19328) | arxiv_abs；Project/code links extracted from arXiv abs page 2605.19328. |
| RoboMIND | `found` | [https://x-humanoid-robomind.github.io](https://x-humanoid-robomind.github.io) | [论文](https://arxiv.org/abs/2412.13877) | arxiv_abs；Project/code links extracted from arXiv abs page 2412.13877. |
| RoboReel | `found` | [https://roboreel.github.io](https://roboreel.github.io) | [论文](https://arxiv.org/abs/2609.08209) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.08209. |
| RoboStress | `not_found` | — | [论文](https://arxiv.org/abs/2609.37334) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RoboTwin | `platform_only` | [https://robotwin-platform.github.io/](https://robotwin-platform.github.io/)、[https://github.com/robotwin-Platform/robotwin](https://github.com/robotwin-Platform/robotwin) | [论文](https://doi.org/10.1109/CVPR52734.2025.02575) | manual_official_or_platform_check；Canonical RoboTwin Platform pages. |
| RoboVAD | `not_found` | — | [论文](https://arxiv.org/abs/2609.17843) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| RoboVista | `not_found` | — | [论文](https://doi.org/10.15607/RSS.2026.XXII.095) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| SIREN-Bench | `not_found` | — | [论文](https://arxiv.org/abs/2608.24094) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| STARS | `found` | [https://larg.github.io/stars](https://larg.github.io/stars) | [论文](https://arxiv.org/abs/2609.40245) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.40245. |
| SafeAgentBench | `found` | [https://github.com/shengyin1224/SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench) | [论文](https://arxiv.org/abs/2412.13178) | arxiv_abs；Project/code links extracted from arXiv abs page 2412.13178. |
| SafeBench | `found` | [https://safebench.github.io](https://safebench.github.io) | [论文](https://arxiv.org/abs/2206.09682) | arxiv_abs；Project/code links extracted from arXiv abs page 2206.09682. |
| SafeLIBERO | `found` | [https://vlsa-aegis.github.io](https://vlsa-aegis.github.io) | [论文](https://arxiv.org/abs/2512.11891) | arxiv_abs；Project/code links extracted from arXiv abs page 2512.11891. |
| SafeMindBench | `not_found` | — | [论文](https://arxiv.org/abs/2509.25885) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| SafePlan-Bench / Safe-Align | `not_found` | — | [论文](https://arxiv.org/abs/2504.14650) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| SafeStage | `candidate` | [https://github.com/reeta-042/safestage](https://github.com/reeta-042/safestage) | [论文](https://arxiv.org/abs/2609.21223) | manual_official_or_platform_check；Repository matches the title but is not confirmed as an official author repository. |
| SafeVLA-Bench | `not_found` | — | [论文](https://arxiv.org/abs/2606.00773) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| SimplerEnv | `platform_only` | [https://simpler-env.github.io/](https://simpler-env.github.io/) | [论文](https://arxiv.org/abs/2405.05941) | manual_official_or_platform_check；Canonical SimplerEnv project page. |
| SkillSafetyBench | `found` | [https://github.com/AI45Lab/skill-safety-bench](https://github.com/AI45Lab/skill-safety-bench) | [论文](https://arxiv.org/abs/2605.12015) | arxiv_abs；Project/code links extracted from arXiv abs page 2605.12015. |
| Spa-Bench | `found` | [https://justintiensmith.github.io/Spa-Bench](https://justintiensmith.github.io/Spa-Bench) | [论文](https://arxiv.org/abs/2610.12696) | arxiv_abs；Project/code links extracted from arXiv abs page 2610.12696. |
| TALK-Dem | `not_found` | — | [论文](https://arxiv.org/abs/2609.38371) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| TSHA | `not_found` | — | [论文](https://arxiv.org/abs/2603.29759) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| TrafficSignBench | `not_found` | — | [论文](https://arxiv.org/abs/2609.38463) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Trap-LIBERO / Trap-RoboTwin | `found` | [https://john-liua.github.io/TrapVLA](https://john-liua.github.io/TrapVLA) | [论文](https://arxiv.org/abs/2608.26578) | arxiv_abs；Project/code links extracted from arXiv abs page 2608.26578. |
| VIPS | `found` | [https://vips2026.github.io](https://vips2026.github.io) | [论文](https://arxiv.org/abs/2609.02462) | arxiv_abs；Project/code links extracted from arXiv abs page 2609.02462. |
| VLA-Arena | `found` | [https://vla-arena.github.io](https://vla-arena.github.io) | [论文](https://arxiv.org/abs/2512.22539) | arxiv_abs；Project/code links extracted from arXiv abs page 2512.22539. |
| VLA-GAUGE | `not_found` | — | [论文](https://arxiv.org/abs/2610.16567) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| VLA-Retain | `not_found` | — | [论文](https://arxiv.org/abs/2610.27698) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| VLABench | `platform_only` | [https://vlabench.github.io/](https://vlabench.github.io/) | [论文](https://doi.org/10.1109/ICCV51701.2025.01037) | manual_official_or_platform_check；Canonical VLABench project page. |
| VLN-Safe | `not_found` | — | [论文](https://arxiv.org/abs/2610.14682) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| VestaBench | `not_found` | — | [论文](https://doi.org/10.18653/v1/2025.emnlp-industry.149) | not_arxiv；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| Words to World | `not_found` | — | [论文](https://arxiv.org/abs/2610.15228) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| X2Real | `not_found` | — | [论文](https://arxiv.org/abs/2609.27449) | arxiv_abs；截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。 |
| nuScenes | `platform_only` | [https://www.nuscenes.org/](https://www.nuscenes.org/) | [论文](https://arxiv.org/abs/2609.22582) | manual_official_or_platform_check；Canonical nuScenes dataset/evaluation page. |

## 判定边界

- `found` 只表示地址已找到，不表示已逐项验证代码、数据和论文版本完全一致。
- `platform_only` 可以作为复现入口，但不能证明该 benchmark 有独立维护的项目仓库。
- `candidate` 不纳入正式来源统计；需要作者主页、论文项目页或仓库 README 的明确关联后再升级为 `found`。
- `not_found` 表示本轮没有确认到地址，并不证明项目绝对不存在；论文只有 DOI、项目未公开或搜索引擎未收录时都可能出现这种结果。
