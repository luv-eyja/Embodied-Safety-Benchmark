# 已分类条目的场景与研究目标共现

> 本轮覆盖矩阵仅统计 62 个已分类条目；60 个档案未知。每个格子按条目名去重，格子的成员列表保存在 data/benchmark_survey.json。

## 统计口径

- 主要成果类型、具身关联和研究目标由正文笔记人工编码；不是关键词扫描。
- 同一条目可属于多个应用场景和目标，因此行列之间不可直接相加当独立条目总数。
- 单元格只表示条目同时具有两类标签；尚未逐任务验证该目标在每一种场景上的实验，不作为联合任务覆盖证明。
- 这里的空格或零代表本轮样本没有编码到相应条目，不代表领域不存在工作。
- 原有“环节×安全属性”把独立标签作笛卡尔积，无法证明某属性在该环节被实际评测；本轮撤回这种缺口推断。

## 场景标签 × 目标标签（62 个已分类条目的共现）

| 应用场景 | 能力 | 鲁棒性 | 安全 | 本场景去重条目数 |
|---|---:|---:|---:|---:|
| 主动感知 | 1 | 2 | 0 | 2 |
| 人机交互 | 2 | 0 | 1 | 2 |
| 全身控制 | 1 | 1 | 0 | 1 |
| 具身感知理解 | 2 | 0 | 0 | 2 |
| 多主体社会行为 | 0 | 0 | 1 | 1 |
| 多机器人 | 0 | 0 | 1 | 1 |
| 导航 | 2 | 0 | 0 | 2 |
| 工业装配 | 2 | 1 | 0 | 2 |
| 无人机 | 1 | 0 | 0 | 1 |
| 机器人语义决策 | 5 | 0 | 8 | 9 |
| 机器人运行治理 | 0 | 0 | 1 | 1 |
| 机械臂操作 | 29 | 16 | 11 | 33 |
| 灵巧操作 | 2 | 2 | 0 | 2 |
| 移动操作 | 5 | 1 | 0 | 6 |
| 自动驾驶 | 5 | 3 | 3 | 5 |
| 软件代理 | 2 | 0 | 5 | 5 |

## 成员与证据

- **主动感知**：[BAVO-Bench](../benchmarks/2__BAVO-Bench.md)、[LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md)。
- **人机交互**：[LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md)、[STARS](../benchmarks/4__STARS.md)。
- **全身控制**：[MSK-Bench](../benchmarks/4__MSK-Bench.md)。
- **具身感知理解**：[RoboChrono](../benchmarks/3__RoboChrono.md)、[nuScenes](../benchmarks/5__nuScenes.md)。
- **多主体社会行为**：[MineAmongUs](../benchmarks/4__MineAmongUs.md)。
- **多机器人**：[EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md)。
- **导航**：[EmbodiedBench](../benchmarks/4__EmbodiedBench.md)、[STARS](../benchmarks/4__STARS.md)。
- **工业装配**：[LABIT](../benchmarks/4__LABIT.md)、[Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md)。
- **无人机**：[PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md)。
- **机器人语义决策**：[ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md)、[RoboHarm](../benchmarks/1__RoboHarm.md)、[DESPITE](../benchmarks/4__DESPITE.md)、[EmbodiedBench](../benchmarks/4__EmbodiedBench.md)、[HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md)、[IS-Bench](../benchmarks/4__IS-Bench.md)、[RoboAbstention](../benchmarks/4__RoboAbstention.md)、[RoboJailBench](../benchmarks/4__RoboJailBench.md)、[SafeAgentBench](../benchmarks/4__SafeAgentBench.md)。
- **机器人运行治理**：[EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md)。
- **机械臂操作**：[ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md)、[HazardArena](../benchmarks/1__HazardArena.md)、[LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md)、[ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md)、[RoboHarm](../benchmarks/1__RoboHarm.md)、[SafeLIBERO](../benchmarks/1__SafeLIBERO.md)、[SafeStage](../benchmarks/1__SafeStage.md)、[Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md)、[VLA-Arena](../benchmarks/1__VLA-Arena.md)、[BAVO-Bench](../benchmarks/2__BAVO-Bench.md)、[LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md)、[LIBERO-Para](../benchmarks/2__LIBERO-Para.md)、[LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md)、[LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md)、[AgiBot World](../benchmarks/3__AgiBot-World.md)、[CALVIN](../benchmarks/3__CALVIN.md)、[COLOSSEUM](../benchmarks/3__COLOSSEUM.md)、[IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md)、[LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md)、[ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md)、[Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md)、[RoboComb](../benchmarks/3__RoboComb.md)、[RoboFollow](../benchmarks/3__RoboFollow.md)、[RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md)、[RoboMIND](../benchmarks/3__RoboMIND.md)、[RoboReel](../benchmarks/3__RoboReel.md)、[RoboTwin](../benchmarks/3__RoboTwin.md)、[SimplerEnv](../benchmarks/3__SimplerEnv.md)、[Spa-Bench](../benchmarks/3__Spa-Bench.md)、[VLABench](../benchmarks/3__VLABench.md)、[EmbodiedBench](../benchmarks/4__EmbodiedBench.md)、[IS-Bench](../benchmarks/4__IS-Bench.md)、[SafeAgentBench](../benchmarks/4__SafeAgentBench.md)。
- **灵巧操作**：[BiDex-100](../benchmarks/3__BiDex-100.md)、[Bench2Dex](../benchmarks/4__Bench2Dex.md)。
- **移动操作**：[RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md)、[AgiBot World](../benchmarks/3__AgiBot-World.md)、[BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md)、[ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md)、[RoboCasa](../benchmarks/3__RoboCasa.md)、[RoboCasa365](../benchmarks/3__RoboCasa365.md)。
- **自动驾驶**：[CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md)、[NAVSIM](../benchmarks/5__NAVSIM.md)、[SafeBench](../benchmarks/5__SafeBench.md)、[VIPS](../benchmarks/5__VIPS.md)、[nuScenes](../benchmarks/5__nuScenes.md)。
- **软件代理**：[Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md)、[INFUSE](../benchmarks/4__INFUSE.md)、[MemForm](../benchmarks/4__MemForm.md)、[ORBIT](../benchmarks/4__ORBIT.md)、[SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md)。

## 解释边界

多机器人治理原型与多机器人实体控制不同；UAV 离线决策题也不同于飞行闭环。导航包含在综合基准中，不证明存在足够独立导航评测覆盖。选型时还应按比较矩阵的执行环境和主要类型筛选。

ESB-2 是可选设计提案；本矩阵不证明其创新性、必要性或“唯一覆盖空白”。参见[统计修正记录](../analysis/statistical-corrections.md)。
