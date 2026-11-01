# 基准卡片与跨基准比较

> 本文件由 `scripts/build_benchmark_docs.py` 自动生成；用于从单篇 benchmark 文档进入横向选型。
> 关键词分类是发现性下界，全文补录只覆盖 10 个核心基准，不能替代逐篇协议核查。

## 1. 数据范围与用途

- 基准：**122** 个；关联论文：**193** 篇。
- 全文核查补录：**10** 个；至少有一篇后续使用论文：**11** 个。
- “后续使用”只计同时有提出论文和非提出论文的条目；若本表只有使用论文，则保留为“原始提出论文未单列”。
- `data/benchmark_cards.json` 是机器可读入口；`data/benchmark_source_audit.json` 记录提出来源核验；本文件保留分类口径、核心对照和选型建议。

## 2. 按分类汇总

| 分类 | 基准数 | 全文补录 | 有后续使用 | 覆盖至少 2 类安全属性 |
|---|---:|---:|---:|---:|
| VLA 安全 | 12 | 6 | 1 | 8 |
| VLA 鲁棒性 | 16 | 3 | 2 | 11 |
| VLA 能力 | 31 | 0 | 6 | 18 |
| 具身智能体安全 | 46 | 1 | 0 | 18 |
| 具身安全 | 17 | 0 | 2 | 6 |

## 3. 环节 × 安全属性比较

下表按每个基准的提出论文摘要和定位描述做关键词分类；一个基准可以命中多个环节和属性。

| 环节 | 语义/指令安全 | 物理/接触安全 | 对抗/后门安全 | 分布偏移鲁棒性 | 失败恢复 | 实时/治理 | 基准数 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 感知层 | 21 | 21 | 4 | 23 | 14 | 4 | 54 |
| 认知/语义层 | 37 | 24 | 6 | 14 | 8 | 5 | 47 |
| 规划层 | 12 | 13 | 7 | 11 | 11 | 3 | 35 |
| 动作控制层 | 28 | 37 | 9 | 28 | 19 | 11 | 83 |
| 终态/后果层 | 0 | 6 | 0 | 0 | 1 | 1 | 6 |

**属性覆盖（去重计数）**：语义/指令安全 37；物理/接触安全 57；对抗/后门安全 17；分布偏移鲁棒性 42；失败恢复 25；实时/治理 13。

## 4. 核心全文基准对照

| 基准 | 可复用评测角色 | 主要平台 | 规模线索 | 覆盖环节 | 覆盖属性 | 关键定量证据 | 文档 |
|---|---|---|---|---|---|---|---|
| ForesightSafety-VLA | 过程级风险与四象限 | RoboTwin | 5 种本体、66 个安全增强场景；66 个安全增强基础场景；66 个基础场景；50 个 evaluation episodes；10 个代表场景 | 感知层、认知/语义层 | 语义/指令安全、分布偏移鲁棒性、失败恢复 | 实验覆盖 5 种本体；每个模型-任务-设置共 50 个 evaluation episodes，分布于 3 个随机种子，另对 10 个代表场景做诊断子集。四个完整基线的累计安全代价 CC 为 OpenVLA-oft 0.18、RDT 0.29、DP 0.34、ACT 0.39；unsafe-success 比例为 0.06、0.10、0.10、0.12。OpenVLA-oft 总成功率 0.48，成功回合中 12.5% 不安全；RDT、DP、ACT 的总… | [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) |
| HazardArena | 语义孪生与 Commit 事件 | Franka | 2,000+ 物体资产和 75 个新建语境关键资产中组织 51 个任务；5 个任务族、每族 2 条安全和 1 条不安全指令、每条件 | 感知层、认知/语义层、动作控制层 | 语义/指令安全 | 四个 VLA 在仿真主实验使用跨类别安全/不安全配对；VLA-Adapter 安全微调前 Safe SR/Unsafe SR/Unsafe Commit 为 0.25/0.22/0.44，加拒答数据后为 0.26/0.01/0.03；另一代表性模型由 0.36/0.33/0.61 变为 0.36/0.04/0.06。真机 Franka Panda 使用腕部和场景 RGB 相机，5 个任务族、每族 2 条安全和 1 条不安全指令、每条件 100 trial… | [HazardArena](../benchmarks/1__HazardArena.md) |
| ManiGuard-Bench | 形式化规约与运行时监控 | Franka | 200 基础任务 × 5 扰动 = 1000 锁定场景；6 类接触密集家务任务组织为 200 个锁定基础任务；23000 次 rollout 的结果显示：6–… | 动作控制层 | 物理/接触安全、分布偏移鲁棒性、实时/治理 | 全文将零样本与微调策略放在超过 23,000 次 rollout 上比较。6–21% 的成功 rollout 违反安全规约；在该基准上微调后，安全任务完成率由接近 0 提升到 7.5–29.8%，参与且安全的比例由 16–40% 提升到 51–72%，但参与型 rollout 仍有 21–42% 违规。 | [ManiGuard-Bench](../benchmarks/1__ManiGuard-Bench.md) |
| RoboHarm | 接口迁移与具身拒答 | MuJoCo、YAM | 5 个不安全任务 | 感知层、认知/语义层、动作控制层 | 语义/指令安全 | 文本拒答率为 user-framed 73%、robot-framed 84%，切换到 CaP/EEF/EEF-N/joint 后降至 25%/19%/18%/19%。真机 6 个模型完成 612 次 EEF 和 252 次 joint trials；真实 EEF 拒答 18%，joint 拒答 41%，与仿真 EEF 19%、joint 31% 同方向。burner/brick 在真机仅 8/254 拒答，toaster 为 0/120；doll 为… | [RoboHarm](../benchmarks/1__RoboHarm.md) |
| SafeStage | 生命周期阶段诊断 | Franka、RoboLab、PhysX | 97 个专门设计的风险场景；97 个专门设计任务；3 个环境种子、每种子 10 次 rollout；240 条人工核验 rollout | 动作控制层、终态/后果层 | 物理/接触安全 | 评估器使用位姿、接触、支撑、包含关系、区域、位移、朝向和速度等 privileged 信号；接触阈值为 >0.1 N 且需跨多帧持续。FSH 在任务完成后保持机器人姿态并继续观察 5 秒。对 240 条人工核验 rollout 的自动判分精度为 95.81%、召回率 98.77%、F1 97.26%；分阶段 F1 为 ISH 98.65、ETS 96.43、FSH 95.65。默认提示汇总 SR 33.74%、SSR 9.84%，成功但不安全的 roll… | [SafeStage](../benchmarks/1__SafeStage.md) |
| SafeVLA-Bench | 通用安全测量层 | LIBERO、RoboCasa | 200 episodes（10 个任务；50 episodes | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | LIBERO 代表性结果：OpenVLA-7B SR/Safety/SBU/VSI 为 69.4/77.4/10.8/0.174；Octo 为 93.9/77.5/19.2/0.140；GR00T-N1.7 为 94.2/72.0/24.0/0.169；UniVLA 为 94.8/79.5/17.1/0.127；InternVLA-M1 为 96.4/81.5/16.8/0.118；VLA-Adapter 为 97.6/82.0/17.0/0.104；O… | [SafeVLA-Bench](../benchmarks/1__SafeVLA-Bench.md) |
| LIBERO-CTRL | 复合扰动配对 | LIBERO | 10 个任务、每任务；40×10=400 个匹配 task；2,000 个 nominal rollout | 未标注 | 分布偏移鲁棒性、失败恢复 | 每个 checkpoint 先在四套件的 2,000 个 nominal rollouts 上复现；六个主策略包括 OpenVLA-OFT、UniVLA、SmolVLA、VLA-JEPA、PredVLA 和一项匿名公式模型。全文摘要给出：即使聚合差异无法显著区分，最多 29.0% 的匹配初始状态仍改变结果；最受影响的 policy-severity 条件变化率达 34.5%。统计用按任务聚类的 bootstrap，并对三种随机策略做独立随机种子复评。 | [LIBERO-CTRL](../benchmarks/2__LIBERO-CTRL.md) |
| LIBERO-RIG | latent 硬件偏移 | LIBERO | 11 条硬件扰动轴 × 5 个严重度 = 210 种条件；500 回合；210 种条件；0.767 跌到最高严重度的 0.509**（干净条件；11 条轴、5… | 感知层、动作控制层 | 分布偏移鲁棒性 | 汇总成功率由 nominal 0.932 降至中等严重度 0.767，再降至最高严重度 0.509。严重度 3 的跨轴均值约为：camera position 0.448、camera orientation 0.596、robot base 0.692、frame rotation 0.752、FOV 0.777、control frequency 0.786、table height/pad 0.846、wrist 0.890、gain 0.908、… | [LIBERO-RIG](../benchmarks/2__LIBERO-RIG.md) |
| LIBERO-VPro | 视觉证据时序 | LIBERO、Franka | 12 类挑战 96 种设置；12 类挑战、96 种设置、3296 个任务-条件案例；19.6 万仿真回合；200 次 Franka Research 3 真机… | 感知层、动作控制层 | 分布偏移鲁棒性 | 视觉证据退化包含目标/容器遮挡比例 25/50/75/100% 与四种时序、交互线索遮挡、短时 blackout/noise 和视角不可用；相机陈旧包含 3 档固定延迟、冻结和历史回放；一致性包含跨视角矛盾和预测-现实分歧；场景变化包含 distractor、前置条件变化、视觉歧义以及 Taper/Multipeak/Twist/Asymmetric 几何。LingBot 的递归自预测总体成功率由 97.0 降至 53.8，Long 套件由 98 降至… | [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) |
| DESPITE | 规划能力与安全双轴 | 表内摘要未明确基础平台。 | 12,279 个任务；12,279 个跨物理与规范危险的**完全确定性验证**任务；0.4% 任务；28.3% 的任务；12,279 个具身规划任务；7 个模… | 规划层 | 物理/接触安全 | 最佳规划模型的 infeasible 约 0.4%，但 dangerous plan 仍约 28.3%；开源模型 feasibility 为 0.4–99.3%，Safety Intention 约 37.6–56.9%，专有 reasoning 模型约 71–81%。hard split 中 GPT-5 的 feasibility 99.5、Safety Precision 81.4；高可行性难例中 physical danger 占 70.6–88.… | [DESPITE](../benchmarks/4__DESPITE.md) |

## 5. ESB-2 复用建议

核心基准可以按“评测层”组合，而不是把它们当作互斥任务集：

| 设计层 | 优先参考 | 应保留的协议思想 |
|---|---|---|
| 阶段定位 | SafeStage；ForesightSafety-VLA | 初始态、执行期、终态分开报告，并保留过程级风险。 |
| 统一判分 | ManiGuard-Bench；SafeVLA-Bench | 公开物理谓词、形式化规约和可审计的安全/能力双轴。 |
| 配对归因 | HazardArena；LIBERO-CTRL；LIBERO-RIG；LIBERO-VPro | 固定 task/seed/policy，只改变语境、组合扰动、硬件或视觉证据。 |
| 规划与接口 | DESPITE；RoboHarm | 分离计划安全与动作安全，观察文本对齐向具身接口迁移时的损失。 |

下一步实施时，优先把 SafeVLA-Bench 的规约层与 SafeStage 的阶段层组合，再用 HazardArena/LIBERO-CTRL 的配对协议做归因；LIBERO-RIG、LIBERO-VPro 和 RoboHarm 可作为部署侧扩展。

## 6. 全量卡片索引

| 基准 | 分类 | 环节 | 安全属性 | 平台 | 规模线索 | 全文 | 后续使用 | 文档 |
|---|---|---|---|---|---|---|---:|---|
| ASIMOV Benchmark | VLA 安全 | 感知层、认知/语义层 | 语义/指令安全、物理/接触安全、对抗/后门安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 1 | [ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md) |
| ForesightSafety-VLA | VLA 安全 | 感知层、认知/语义层 | 语义/指令安全、分布偏移鲁棒性、失败恢复 | RoboTwin | 5 种本体、66 个安全增强场景；66 个安全增强基础场景；66 个基础场景；50 个 evaluation episodes；10 个代… | 是 | 0 | [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) |
| HazardArena | VLA 安全 | 感知层、认知/语义层、动作控制层 | 语义/指令安全 | Franka | 2,000+ 物体资产和 75 个新建语境关键资产中组织 51 个任务；5 个任务族、每族 2 条安全和 1 条不安全指令、每条件 | 是 | 0 | [HazardArena](../benchmarks/1__HazardArena.md) |
| LIBERO-Safety | VLA 安全 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | LIBERO | 19,664 条严格无碰撞示范 | — | 0 | [LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md) |
| ManiGuard-Bench | VLA 安全 | 动作控制层 | 物理/接触安全、分布偏移鲁棒性、实时/治理 | Franka | 200 基础任务 × 5 扰动 = 1000 锁定场景；6 类接触密集家务任务组织为 200 个锁定基础任务；23000 次 rollou… | 是 | 0 | [ManiGuard-Bench](../benchmarks/1__ManiGuard-Bench.md) |
| ManiPhysicsBench | VLA 安全 | 终态/后果层 | 物理/接触安全 | LIBERO、SimplerEnv | 表内摘要未明确规模。 | — | 0 | [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) |
| RoboHarm | VLA 安全 | 感知层、认知/语义层、动作控制层 | 语义/指令安全 | MuJoCo、YAM | 5 个不安全任务 | 是 | 0 | [RoboHarm](../benchmarks/1__RoboHarm.md) |
| SafeLIBERO | VLA 安全 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全 | LIBERO | 表内摘要未明确规模。 | — | 0 | [SafeLIBERO](../benchmarks/1__SafeLIBERO.md) |
| SafeStage | VLA 安全 | 动作控制层、终态/后果层 | 物理/接触安全 | Franka、RoboLab、PhysX | 97 个专门设计的风险场景；97 个专门设计任务；3 个环境种子、每种子 10 次 rollout；240 条人工核验 rollout | 是 | 0 | [SafeStage](../benchmarks/1__SafeStage.md) |
| SafeVLA-Bench | VLA 安全 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | LIBERO、RoboCasa | 200 episodes（10 个任务；50 episodes | 是 | 0 | [SafeVLA-Bench](../benchmarks/1__SafeVLA-Bench.md) |
| Trap-LIBERO / Trap-RoboTwin | VLA 安全 | 动作控制层 | 对抗/后门安全、分布偏移鲁棒性、失败恢复 | LIBERO、RoboTwin | 表内摘要未明确规模。 | — | 0 | [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) |
| VLA-Arena | VLA 安全 | 感知层、认知/语义层 | 语义/指令安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 11 个任务套件、170 个任务 以结构化任务设计框架量化难度：任务；11 个套件 170 个任务 | — | 0 | [VLA-Arena](../benchmarks/1__VLA-Arena.md) |
| BAVO-Bench | VLA 鲁棒性 | 感知层、动作控制层 | 物理/接触安全、分布偏移鲁棒性、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) |
| DriveDegrade | VLA 鲁棒性 | 感知层、规划层 | 物理/接触安全、对抗/后门安全、分布偏移鲁棒性 | CARLA、nuScenes、NAVSIM | 表内摘要未明确规模。 | — | 0 | [DriveDegrade](../benchmarks/2__DriveDegrade.md) |
| LIBERO-CTRL | VLA 鲁棒性 | 未标注 | 分布偏移鲁棒性、失败恢复 | LIBERO | 10 个任务、每任务；40×10=400 个匹配 task；2,000 个 nominal rollout | 是 | 0 | [LIBERO-CTRL](../benchmarks/2__LIBERO-CTRL.md) |
| LIBERO-MAX | VLA 鲁棒性 | 感知层、动作控制层 | 分布偏移鲁棒性、失败恢复 | LIBERO | 8000 对配对案例；8,000 对配对案例 | — | 0 | [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) |
| LIBERO-Para | VLA 鲁棒性 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | LIBERO | 表内摘要未明确规模。 | — | 0 | [LIBERO-Para](../benchmarks/2__LIBERO-Para.md) |
| LIBERO-Plus | VLA 鲁棒性 | 感知层、认知/语义层 | 语义/指令安全、分布偏移鲁棒性 | LIBERO | 6 个能力套件的 ID/OOD 配对任务；6 个能力套件的分布内/分布外配对任务；4 个任务套件、3 个 VLA、7 种扰动条件；0.54… | — | 9 | [LIBERO-Plus](../benchmarks/2__LIBERO-Plus.md) |
| LIBERO-Pro2.0 | VLA 鲁棒性 | 感知层、动作控制层 | 分布偏移鲁棒性 | LIBERO | 1648 个偏移任务实例；1648 个经六轮校验的偏移任务实例；39390 条轨迹；1,648 个经验证的偏移任务实例；39,390 条轨迹 | — | 1 | [LIBERO-Pro2.0](../benchmarks/2__LIBERO-Pro2-0.md) |
| LIBERO-RECOVER | VLA 鲁棒性 | 未标注 | 物理/接触安全、失败恢复 | LIBERO | 表内摘要未明确规模。 | — | 0 | [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) |
| LIBERO-RIG | VLA 鲁棒性 | 感知层、动作控制层 | 分布偏移鲁棒性 | LIBERO | 11 条硬件扰动轴 × 5 个严重度 = 210 种条件；500 回合；210 种条件；0.767 跌到最高严重度的 0.509**（干净… | 是 | 0 | [LIBERO-RIG](../benchmarks/2__LIBERO-RIG.md) |
| LIBERO-VPro | VLA 鲁棒性 | 感知层、动作控制层 | 分布偏移鲁棒性 | LIBERO、Franka | 12 类挑战 96 种设置；12 类挑战、96 种设置、3296 个任务-条件案例；19.6 万仿真回合；200 次 Franka Res… | 是 | 0 | [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) |
| LIBERO-X | VLA 鲁棒性 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | LIBERO | 表内摘要未明确规模。 | — | 0 | [LIBERO-X](../benchmarks/2__LIBERO-X.md) |
| RoboCasa-Shift | VLA 鲁棒性 | 感知层、规划层、动作控制层 | 分布偏移鲁棒性、失败恢复 | RoboCasa、RoboCasa365 | 5 等 VLA 策略 单因子受控偏移 + 干净/扰动配对 rollout；4 个通过干净性能门槛的长时程任务；4 个通过预设干净性能门槛的… | — | 0 | [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) |
| RoboStress | VLA 鲁棒性 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 7 种部署场景 | — | 0 | [RoboStress](../benchmarks/2__RoboStress.md) |
| VLA-GAUGE | VLA 鲁棒性 | 动作控制层 | 物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 6 个能力套件的 ID/OOD 配对任务；6 个能力套件的分布内/分布外配对任务 | — | 0 | [VLA-GAUGE](../benchmarks/2__VLA-GAUGE.md) |
| VLA-Retain | VLA 鲁棒性 | 感知层 | 分布偏移鲁棒性 | LIBERO | 表内摘要未明确规模。 | — | 0 | [VLA-Retain](../benchmarks/2__VLA-Retain.md) |
| VLN-Safe | VLA 鲁棒性 | 动作控制层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 38.5–56.8% 的成功回合 | — | 0 | [VLN-Safe](../benchmarks/2__VLN-Safe.md) |
| AgiBot World | VLA 能力 | 动作控制层 |  | 表内摘要未明确基础平台。 | 1 等） 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；100 万余条轨迹、217 个任务、5 类部署场景 | — | 0 | [AgiBot World](../benchmarks/3__AgiBot-World.md) |
| BEHAVIOR-1K | VLA 能力 | 感知层、认知/语义层、规划层、动作控制层 | 语义/指令安全、失败恢复 | BEHAVIOR-1K | 21 类技能 / 417 子任务；1K 的 50 个活动构建数据集（21 类技能、417 个子任务 | — | 0 | [BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md) |
| BiDex-100 | VLA 能力 | 感知层、认知/语义层、规划层、动作控制层 | 语义/指令安全、物理/接触安全 | 表内摘要未明确基础平台。 | 100 双手灵巧操作 106 任务；5 条能力轴：泛化、指令遵循、少示范；106 个任务 | — | 0 | [BiDex-100](../benchmarks/3__BiDex-100.md) |
| CALVIN | VLA 能力 | 认知/语义层、规划层、动作控制层 | 语义/指令安全、物理/接触安全 | CALVIN | 34 个任务；34 个操作任务 | — | 3 | [CALVIN](../benchmarks/3__CALVIN.md) |
| COLOSSEUM | VLA 能力 | 感知层 | 物理/接触安全、分布偏移鲁棒性 | LIBERO | 表内摘要未明确规模。 | — | 0 | [COLOSSEUM](../benchmarks/3__COLOSSEUM.md) |
| HUGE-Bench | VLA 能力 | 感知层、认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [HUGE-Bench](../benchmarks/3__HUGE-Bench.md) |
| IndustrialVLA-Bench | VLA 能力 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | LIBERO | 表内摘要未明确规模。 | — | 0 | [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) |
| LIBERO（基础套件） | VLA 能力 | 认知/语义层 | 物理/接触安全 | LIBERO、RoboTwin、SimplerEnv、ManiSkill | 130 任务；1648 个偏移任务实例；1648 个经六轮校验的偏移任务实例；39390 条轨迹；11 条硬件扰动轴 × 5 个严重度 =… | — | 28 | [LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md) |
| LongBench | VLA 能力 | 感知层、认知/语义层、规划层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 6 个 SOTA 操作策略（真机） 1000+ 真机回合；1000 余个真实回合 | — | 0 | [LongBench](../benchmarks/3__LongBench.md) |
| ManiSkill / ManiSkill2 | VLA 能力 | 动作控制层 |  | LIBERO、RoboTwin、ManiSkill、SAPIEN | 表内摘要未明确规模。 | — | 1 | [ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md) |
| ManiUnit | VLA 能力 | 感知层、认知/语义层、规划层、动作控制层 | 语义/指令安全、失败恢复 | BEHAVIOR-1K | 21 类技能 / 417 子任务；1K 的 50 个活动构建数据集（21 类技能、417 个子任务 | — | 0 | [ManiUnit](../benchmarks/3__ManiUnit.md) |
| Open X-Embodiment | VLA 能力 | 动作控制层 |  | 表内摘要未明确基础平台。 | 1 等） 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；100 万余条轨迹、217 个任务、5 类部署场景 | — | 0 | [Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md) |
| PolaRiS | VLA 能力 | 感知层 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [PolaRiS](../benchmarks/3__PolaRiS.md) |
| Robo2Process | VLA 能力 | 感知层、认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Robo2Process](../benchmarks/3__Robo2Process.md) |
| RoboCasa | VLA 能力 | 感知层、规划层、动作控制层 | 分布偏移鲁棒性、失败恢复 | RoboCasa、RoboCasa365 | 5 等 VLA 策略 单因子受控偏移 + 干净/扰动配对 rollout；4 个通过干净性能门槛的长时程任务 | — | 2 | [RoboCasa](../benchmarks/3__RoboCasa.md) |
| RoboCasa365 | VLA 能力 | 感知层、规划层、动作控制层 | 分布偏移鲁棒性、失败恢复 | RoboCasa、RoboCasa365 | 5 等 VLA 策略 单因子受控偏移 + 干净/扰动配对 rollout；4 个通过干净性能门槛的长时程任务 | — | 0 | [RoboCasa365](../benchmarks/3__RoboCasa365.md) |
| RoboChrono | VLA 能力 | 感知层、动作控制层 |  | 表内摘要未明确基础平台。 | 39 个场景；34,713 个评测实例；7 类任务；18 个视觉语言模型的零样本评测显示任务 | — | 0 | [RoboChrono](../benchmarks/3__RoboChrono.md) |
| RoboColiseum | VLA 能力 | 感知层、认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboColiseum](../benchmarks/3__RoboColiseum.md) |
| RoboComb | VLA 能力 | 认知/语义层、规划层、动作控制层 | 语义/指令安全、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboComb](../benchmarks/3__RoboComb.md) |
| RoboDojo | VLA 能力 | 动作控制层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 42 任务；3 个 LLM 作为策略（无任务；40 个公开策略作对照 RoboDojo 全部 42 个任务；50 回合协议） 追问「不做任… | — | 0 | [RoboDojo](../benchmarks/3__RoboDojo.md) |
| RoboEval | VLA 能力 | 动作控制层、终态/后果层 | 物理/接触安全、失败恢复 | 表内摘要未明确基础平台。 | 8 个双臂任务 + 3000+ 专家示范；8 个系统控制变化条件的双臂任务、3000 余条专家示范 | — | 0 | [RoboEval](../benchmarks/3__RoboEval.md) |
| RoboFollow | VLA 能力 | 感知层、认知/语义层 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboFollow](../benchmarks/3__RoboFollow.md) |
| RoboIRG-Bench | VLA 能力 | 感知层、认知/语义层 | 语义/指令安全、物理/接触安全、失败恢复 | 表内摘要未明确基础平台。 | 40 个变体、覆盖 11 个任务 | — | 0 | [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) |
| RoboMIND | VLA 能力 | 动作控制层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboMIND](../benchmarks/3__RoboMIND.md) |
| RoboReel | VLA 能力 | 动作控制层 | 分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 10 个操作任务 | — | 0 | [RoboReel](../benchmarks/3__RoboReel.md) |
| RoboTwin | VLA 能力 | 动作控制层 |  | LIBERO、RoboTwin、ManiSkill | 表内摘要未明确规模。 | — | 7 | [RoboTwin](../benchmarks/3__RoboTwin.md) |
| RoboVista | VLA 能力 | 感知层、规划层 |  | 表内摘要未明确基础平台。 | 6 个机器人应用域 / 39 个任务；6 个机器人应用域与 39 个多样任务 | — | 0 | [RoboVista](../benchmarks/3__RoboVista.md) |
| SimplerEnv | VLA 能力 | 感知层、动作控制层 | 物理/接触安全 | LIBERO、SimplerEnv | 表内摘要未明确规模。 | — | 2 | [SimplerEnv](../benchmarks/3__SimplerEnv.md) |
| Spa-Bench | VLA 能力 | 认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Spa-Bench](../benchmarks/3__Spa-Bench.md) |
| VLABench | VLA 能力 | 认知/语义层、规划层、动作控制层 | 语义/指令安全、物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [VLABench](../benchmarks/3__VLABench.md) |
| X2Real | VLA 能力 | 感知层 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [X2Real](../benchmarks/3__X2Real.md) |
| AGENTSAFE / SAFE-THOR | 具身智能体安全 | 感知层、认知/语义层、规划层、动作控制层 | 语义/指令安全、对抗/后门安全、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [AGENTSAFE / SAFE-THOR](../benchmarks/4__AGENTSAFE-SAFE-THOR.md) |
| AeroIntent | 具身智能体安全 | 感知层、动作控制层 |  | 表内摘要未明确基础平台。 | 990 条同步多模态序列、22 个轨迹程序、5 类任务 | — | 0 | [AeroIntent](../benchmarks/4__AeroIntent.md) |
| Agent-SafetyBench | 具身智能体安全 | 未标注 | 失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md) |
| BLINDSPOT | 具身智能体安全 | 规划层、动作控制层 | 对抗/后门安全、失败恢复、实时/治理 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [BLINDSPOT](../benchmarks/4__BLINDSPOT.md) |
| Bench2Dex | 具身智能体安全 | 感知层、动作控制层 | 物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Bench2Dex](../benchmarks/4__Bench2Dex.md) |
| CAPSafe | 具身智能体安全 | 认知/语义层、规划层、动作控制层 | 语义/指令安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [CAPSafe](../benchmarks/4__CAPSafe.md) |
| DESPITE | 具身智能体安全 | 规划层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 12,279 个任务；12,279 个跨物理与规范危险的**完全确定性验证**任务；0.4% 任务；28.3% 的任务；12,279 个具… | 是 | 0 | [DESPITE](../benchmarks/4__DESPITE.md) |
| DUMA-Bench | 具身智能体安全 | 动作控制层 | 对抗/后门安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [DUMA-Bench](../benchmarks/4__DUMA-Bench.md) |
| Embodied Agent Interface | 具身智能体安全 | 规划层、动作控制层 | 失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Embodied Agent Interface](../benchmarks/4__Embodied-Agent-Interface.md) |
| EmbodiedBench | 具身智能体安全 | 感知层、认知/语义层、规划层、动作控制层 | 语义/指令安全、物理/接触安全 | 表内摘要未明确基础平台。 | 1128 个任务；4 个环境、1128 个测试任务的基准：从家务等高层语义任务 | — | 0 | [EmbodiedBench](../benchmarks/4__EmbodiedBench.md) |
| EmbodiedGovBench | 具身智能体安全 | 动作控制层 | 物理/接触安全、分布偏移鲁棒性、失败恢复、实时/治理 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) |
| GaugeBench | 具身智能体安全 | 感知层 | 分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [GaugeBench](../benchmarks/4__GaugeBench.md) |
| GuardianBench | 具身智能体安全 | 感知层、认知/语义层、动作控制层 | 语义/指令安全 | 表内摘要未明确基础平台。 | 3024 个「同场景安全/不安全」配对样本；3024 组同场景安全/不安全对比样本 | — | 0 | [GuardianBench](../benchmarks/4__GuardianBench.md) |
| HASARD | 具身智能体安全 | 感知层、动作控制层 |  | 表内摘要未明确基础平台。 | 3D 基准只考虑简单导航任务 | — | 0 | [HASARD](../benchmarks/4__HASARD.md) |
| HygieneRoboBench | 具身智能体安全 | 感知层、规划层、动作控制层、终态/后果层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 624 个实例 / 134 个任务；624 个实例、134 个任务 | — | 0 | [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) |
| INFUSE | 具身智能体安全 | 认知/语义层、规划层、动作控制层 | 语义/指令安全、对抗/后门安全 | 表内摘要未明确基础平台。 | 40 个真实任务 | — | 0 | [INFUSE](../benchmarks/4__INFUSE.md) |
| IS-Bench | 具身智能体安全 | 感知层、动作控制层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 161 个场景 | — | 0 | [IS-Bench](../benchmarks/4__IS-Bench.md) |
| Inspect Robots | 具身智能体安全 | 动作控制层 | 物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Inspect Robots](../benchmarks/4__Inspect-Robots.md) |
| LABIT | 具身智能体安全 | 规划层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [LABIT](../benchmarks/4__LABIT.md) |
| MAGMA-Bench | 具身智能体安全 | 感知层、认知/语义层、规划层、动作控制层 | 分布偏移鲁棒性、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [MAGMA-Bench](../benchmarks/4__MAGMA-Bench.md) |
| MMA-SafetyBench | 具身智能体安全 | 感知层、认知/语义层、动作控制层 | 语义/指令安全、对抗/后门安全、实时/治理 | 表内摘要未明确基础平台。 | 1083 条对抗轨迹 | — | 0 | [MMA-SafetyBench](../benchmarks/4__MMA-SafetyBench.md) |
| MSK-Bench | 具身智能体安全 | 动作控制层、终态/后果层 | 物理/接触安全、实时/治理 | 表内摘要未明确基础平台。 | 22 个全身任务；22 个全身运动控制任务 | — | 0 | [MSK-Bench](../benchmarks/4__MSK-Bench.md) |
| MemForm | 具身智能体安全 | 未标注 | 对抗/后门安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [MemForm](../benchmarks/4__MemForm.md) |
| MemTransfer | 具身智能体安全 | 感知层 |  | 表内摘要未明确基础平台。 | 10 类任务的 100 个导航案例 | — | 0 | [MemTransfer](../benchmarks/4__MemTransfer.md) |
| MineAmongUs | 具身智能体安全 | 认知/语义层、动作控制层 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [MineAmongUs](../benchmarks/4__MineAmongUs.md) |
| MotionForge | 具身智能体安全 | 感知层、认知/语义层、规划层、动作控制层 | 分布偏移鲁棒性、实时/治理 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [MotionForge](../benchmarks/4__MotionForge.md) |
| ORBIT | 具身智能体安全 | 规划层 | 对抗/后门安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [ORBIT](../benchmarks/4__ORBIT.md) |
| ORDER | 具身智能体安全 | 认知/语义层 | 实时/治理 | 表内摘要未明确基础平台。 | 500 题知识测试 + 更难组合任务 | — | 0 | [ORDER](../benchmarks/4__ORDER.md) |
| PASTABench | 具身智能体安全 | 动作控制层 | 实时/治理 | 表内摘要未明确基础平台。 | 1139 个多轮轨迹 | — | 0 | [PASTABench](../benchmarks/4__PASTABench.md) |
| PLCBENCH | 具身智能体安全 | 动作控制层 | 对抗/后门安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [PLCBENCH](../benchmarks/4__PLCBENCH.md) |
| Peg-in-Bench | 具身智能体安全 | 未标注 | 物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) |
| PhysAI-Bench | 具身智能体安全 | 感知层、认知/语义层、动作控制层 |  | 表内摘要未明确基础平台。 | 10,178 条标准化决策实例；10,178 条从自主 UAV 任务对话轨迹中自动抽取的标准化决策实例 | — | 0 | [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) |
| REVERSAL-BENCH | 具身智能体安全 | 动作控制层 | 失败恢复 | 表内摘要未明确基础平台。 | 8 种操作设置 | — | 0 | [REVERSAL-BENCH](../benchmarks/4__REVERSAL-BENCH.md) |
| RT-Safe | 具身智能体安全 | 感知层、认知/语义层、动作控制层 | 实时/治理 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RT-Safe](../benchmarks/4__RT-Safe.md) |
| RoboAbstention | 具身智能体安全 | 感知层、认知/语义层 | 语义/指令安全、物理/接触安全、实时/治理 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboAbstention](../benchmarks/4__RoboAbstention.md) |
| RoboJailBench | 具身智能体安全 | 认知/语义层 | 语义/指令安全、物理/接触安全、对抗/后门安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboJailBench](../benchmarks/4__RoboJailBench.md) |
| RoboVAD | 具身智能体安全 | 动作控制层 | 物理/接触安全、失败恢复、实时/治理 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [RoboVAD](../benchmarks/4__RoboVAD.md) |
| STARS | 具身智能体安全 | 认知/语义层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [STARS](../benchmarks/4__STARS.md) |
| SafeAgentBench | 具身智能体安全 | 规划层、动作控制层 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [SafeAgentBench](../benchmarks/4__SafeAgentBench.md) |
| SafeMindBench | 具身智能体安全 | 感知层、认知/语义层、规划层、动作控制层 |  | 表内摘要未明确基础平台。 | 5558 个样本 | — | 0 | [SafeMindBench](../benchmarks/4__SafeMindBench.md) |
| SafePlan-Bench / Safe-Align | 具身智能体安全 | 认知/语义层、规划层 | 对抗/后门安全 | 表内摘要未明确基础平台。 | 2027 个日常任务 | — | 0 | [SafePlan-Bench / Safe-Align](../benchmarks/4__SafePlan-Bench-Safe-Align.md) |
| SkillSafetyBench | 具身智能体安全 | 动作控制层 | 对抗/后门安全 | 表内摘要未明确基础平台。 | 155 个对抗案例 / 47 个任务 | — | 0 | [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) |
| TALK-Dem | 具身智能体安全 | 认知/语义层、规划层 | 语义/指令安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [TALK-Dem](../benchmarks/4__TALK-Dem.md) |
| TSHA | 具身智能体安全 | 未标注 | 物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [TSHA](../benchmarks/4__TSHA.md) |
| VestaBench | 具身智能体安全 | 规划层 | 物理/接触安全、对抗/后门安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [VestaBench](../benchmarks/4__VestaBench.md) |
| Words to World | 具身智能体安全 | 感知层、认知/语义层、动作控制层 | 语义/指令安全、物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Words to World](../benchmarks/4__Words-to-World.md) |
| Balanced Multi-Robot Task Allocation Benc… | 具身安全 | 未标注 | 物理/接触安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 6 种去中心化 MRTA 分配器 500 组配对实例；25 种通信条件；500 组配对十目标任务、25 种理想与退化通信条件 | — | 0 | [Balanced Multi-Robot Task Allocation Benc…](../benchmarks/5__Balanced-Multi-Robot-Task-Allocation-Benchmark.md) |
| Bench2Drive | 具身安全 | 动作控制层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Bench2Drive](../benchmarks/5__Bench2Drive.md) |
| CARLA / CARLA Leaderboard | 具身安全 | 动作控制层 | 对抗/后门安全、实时/治理 | CARLA、SUMO、nuScenes、NAVSIM | 表内摘要未明确规模。 | — | 3 | [CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md) |
| COMPASS / X-Mobility | 具身安全 | 未标注 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [COMPASS / X-Mobility](../benchmarks/5__COMPASS-X-Mobility.md) |
| DPed-VLN | 具身安全 | 认知/语义层、动作控制层 | 语义/指令安全 | Habitat | 33,093 个导航回合 | — | 0 | [DPed-VLN](../benchmarks/5__DPed-VLN.md) |
| Everyday-Environment Robot Benchmarking | 具身安全 | 未标注 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Everyday-Environment Robot Benchmarking](../benchmarks/5__Everyday-Environment-Robot-Benchmarking.md) |
| ExceptionDrive | 具身安全 | 规划层、动作控制层 | 分布偏移鲁棒性、实时/治理 | nuScenes | 21 个任务 | — | 0 | [ExceptionDrive](../benchmarks/5__ExceptionDrive.md) |
| ISO-based Humanoid Orchestrator Benchmark | 具身安全 | 感知层、动作控制层 |  | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [ISO-based Humanoid Orchestrator Benchmark](../benchmarks/5__ISO-based-Humanoid-Orchestrator-Benchmark.md) |
| NAVSIM | 具身安全 | 规划层、终态/后果层 | 物理/接触安全 | CARLA、nuScenes、NAVSIM | 表内摘要未明确规模。 | — | 2 | [NAVSIM](../benchmarks/5__NAVSIM.md) |
| Physics-Consistent HRI Benchmark | 具身安全 | 感知层、动作控制层 | 物理/接触安全、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [Physics-Consistent HRI Benchmark](../benchmarks/5__Physics-Consistent-HRI-Benchmark.md) |
| R2R-CE | 具身安全 | 动作控制层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 38.5–56.8% 的成功回合 | — | 0 | [R2R-CE](../benchmarks/5__R2R-CE.md) |
| Radar2Plan | 具身安全 | 感知层、规划层、动作控制层 | 分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 4D 雷达开环轨迹；4D 雷达在恶劣条件；4D 雷达基准主要关注感知而非轨迹；4D 雷达数据做开环自车轨迹 | — | 0 | [Radar2Plan](../benchmarks/5__Radar2Plan.md) |
| SIREN-Bench | 具身安全 | 感知层、动作控制层 | 物理/接触安全 | CARLA、SUMO | 表内摘要未明确规模。 | — | 0 | [SIREN-Bench](../benchmarks/5__SIREN-Bench.md) |
| SafeBench | 具身安全 | 未标注 | 对抗/后门安全、分布偏移鲁棒性 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [SafeBench](../benchmarks/5__SafeBench.md) |
| TrafficSignBench | 具身安全 | 规划层 | 物理/接触安全 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [TrafficSignBench](../benchmarks/5__TrafficSignBench.md) |
| VIPS | 具身安全 | 感知层、规划层 | 物理/接触安全、分布偏移鲁棒性、失败恢复 | 表内摘要未明确基础平台。 | 表内摘要未明确规模。 | — | 0 | [VIPS](../benchmarks/5__VIPS.md) |
| nuScenes | 具身安全 | 规划层、动作控制层 |  | CARLA、nuScenes、NAVSIM | 21 个任务 | — | 0 | [nuScenes](../benchmarks/5__nuScenes.md) |
