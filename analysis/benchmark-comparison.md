# 具身智能与安全 Benchmark 调研比较矩阵

> 整理日期：2026-11-03。本库登记 122 个调研条目，其中 62 个已依据正文笔记分类，60 个非重点条目未重新分类。它们不是 122 个同质的独立 benchmark。

## 1. 范围与计数单位

本表用于比较评测目的、任务接口、构建方式和证据边界，不对不同论文的原始分数作跨基准排名。主要成果类型由整理者按本文贡献编码；同一工作可以发布多种成果，但主要类型只计一次。条目名含多个版本时，保留一个索引入口，明确本次所读版本。

| 主要成果类型 | 已分类条目数（分母 62） | 含义 |
|---|---:|---|
| 评测任务集 | 52 | 评测任务集：主要贡献是定义任务、条件和评分的可重复测试集；可同时附训练数据或方法 |
| 训练数据集 | 3 | 训练数据集：主要贡献是采集、整合与标准化学习数据，附带实验不自动算独立基准 |
| 仿真平台 | 2 | 仿真平台：主要贡献是可交互环境、资产和接口，某项配套协议不代表平台全部功能 |
| 评测框架 | 4 | 评测框架：主要贡献是组织多套任务、执行与评分或比较协议 |
| 方法论文 | 1 | 方法论文：主要贡献是模型、表示或算法，本次来源使用已有基准 |

其中直接具身评测任务集为 **48** 条；其余评测任务集属于软件代理邻接研究。这个数字不包含未分类档案，也不表示领域总体规模。

研究目标可多选：能力＝完成／理解／迁移；鲁棒性＝明确的扰动或失败条件；安全＝显式风险、禁止行为、后果或治理。语言理解错误不自动标为语义安全，接触操作不自动标为物理安全。

## 2. 类型、任务与执行接口

| 条目 | 主要类型／关联 | 研究目标 | 应用场景 | 观察或执行环境 |
|---|---|---|---|---|
| [ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md) | 评测任务集／直接具身评测 | 安全 | 机器人语义决策 | 静态情境／图像 |
| [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) | 评测任务集／直接具身评测 | 能力、鲁棒性、安全 | 机械臂操作 | 交互仿真 |
| [HazardArena](../benchmarks/1__HazardArena.md) | 评测任务集／直接具身评测 | 能力、安全 | 机械臂操作 | 交互仿真、真实执行 |
| [LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md) | 评测任务集／直接具身评测 | 能力、安全 | 机械臂操作、人机交互 | 交互仿真 |
| [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) | 评测任务集／直接具身评测 | 能力、安全 | 机械臂操作 | 交互仿真 |
| [RoboHarm](../benchmarks/1__RoboHarm.md) | 评测任务集／直接具身评测 | 安全 | 机器人语义决策、机械臂操作 | 交互仿真、真实执行 |
| [SafeLIBERO](../benchmarks/1__SafeLIBERO.md) | 评测任务集／直接具身评测 | 能力、安全 | 机械臂操作 | 交互仿真、真实执行 |
| [SafeStage](../benchmarks/1__SafeStage.md) | 评测任务集／直接具身评测 | 能力、安全 | 机械臂操作 | 交互仿真 |
| [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) | 评测任务集／直接具身评测 | 能力、安全 | 机械臂操作 | 交互仿真、真实执行 |
| [VLA-Arena](../benchmarks/1__VLA-Arena.md) | 评测任务集／直接具身评测 | 能力、鲁棒性、安全 | 机械臂操作 | 交互仿真、真实执行 |
| [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作、主动感知 | 交互仿真 |
| [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) | 评测任务集／直接具身评测 | 鲁棒性 | 机械臂操作 | 交互仿真 |
| [LIBERO-Para](../benchmarks/2__LIBERO-Para.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真 |
| [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真 |
| [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) | 评测任务集／直接具身评测 | 鲁棒性 | 机械臂操作、主动感知 | 交互仿真、真实执行 |
| [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) | 评测任务集／直接具身评测 | 鲁棒性 | 移动操作 | 交互仿真 |
| [AgiBot World](../benchmarks/3__AgiBot-World.md) | 训练数据集／具身研究底座 | 能力 | 机械臂操作、移动操作 | 真实数据、真实执行 |
| [BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md) | 评测任务集／直接具身评测 | 能力 | 移动操作 | 交互仿真、真实执行 |
| [BiDex-100](../benchmarks/3__BiDex-100.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 灵巧操作 | 交互仿真 |
| [CALVIN](../benchmarks/3__CALVIN.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真 |
| [COLOSSEUM](../benchmarks/3__COLOSSEUM.md) | 评测任务集／直接具身评测 | 鲁棒性 | 机械臂操作 | 交互仿真、真实执行 |
| [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) | 评测框架／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真 |
| [LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md) | 评测任务集／直接具身评测 | 能力 | 机械臂操作 | 交互仿真 |
| [ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md) | 评测任务集／直接具身评测 | 能力 | 机械臂操作、移动操作 | 交互仿真、真实执行 |
| [Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md) | 训练数据集／具身研究底座 | 能力 | 机械臂操作 | 真实数据、真实执行 |
| [RoboCasa](../benchmarks/3__RoboCasa.md) | 仿真平台／具身研究底座 | 能力 | 移动操作 | 交互仿真、真实执行 |
| [RoboCasa365](../benchmarks/3__RoboCasa365.md) | 评测任务集／直接具身评测 | 能力 | 移动操作 | 交互仿真 |
| [RoboChrono](../benchmarks/3__RoboChrono.md) | 评测任务集／直接具身评测 | 能力 | 具身感知理解 | 视频理解、真实数据 |
| [RoboComb](../benchmarks/3__RoboComb.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真 |
| [RoboFollow](../benchmarks/3__RoboFollow.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真、真实执行 |
| [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真 |
| [RoboMIND](../benchmarks/3__RoboMIND.md) | 训练数据集／具身研究底座 | 能力 | 机械臂操作 | 真实数据 |
| [RoboReel](../benchmarks/3__RoboReel.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真、真实数据、真实执行 |
| [RoboTwin](../benchmarks/3__RoboTwin.md) | 评测任务集／直接具身评测 | 能力 | 机械臂操作 | 交互仿真、真实执行 |
| [SimplerEnv](../benchmarks/3__SimplerEnv.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 交互仿真、真实执行 |
| [Spa-Bench](../benchmarks/3__Spa-Bench.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 机械臂操作 | 真实执行 |
| [VLABench](../benchmarks/3__VLABench.md) | 评测任务集／直接具身评测 | 能力 | 机械臂操作 | 交互仿真 |
| [Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md) | 评测任务集／软件代理邻接研究 | 安全 | 软件代理 | 软件环境 |
| [Bench2Dex](../benchmarks/4__Bench2Dex.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 灵巧操作 | 交互仿真 |
| [DESPITE](../benchmarks/4__DESPITE.md) | 评测任务集／直接具身评测 | 能力、安全 | 机器人语义决策 | 符号规划 |
| [EmbodiedBench](../benchmarks/4__EmbodiedBench.md) | 评测任务集／直接具身评测 | 能力 | 机械臂操作、导航、机器人语义决策 | 交互仿真 |
| [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) | 评测框架／直接具身评测 | 安全 | 机器人运行治理、多机器人 | 运行时原型 |
| [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) | 评测任务集／直接具身评测 | 能力、安全 | 机器人语义决策 | 符号规划 |
| [INFUSE](../benchmarks/4__INFUSE.md) | 评测任务集／软件代理邻接研究 | 安全 | 软件代理 | 软件环境 |
| [IS-Bench](../benchmarks/4__IS-Bench.md) | 评测任务集／直接具身评测 | 能力、安全 | 机器人语义决策、机械臂操作 | 交互仿真 |
| [LABIT](../benchmarks/4__LABIT.md) | 评测任务集／直接具身评测 | 能力 | 工业装配 | 真实执行、交互仿真 |
| [MSK-Bench](../benchmarks/4__MSK-Bench.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 全身控制 | 交互仿真 |
| [MemForm](../benchmarks/4__MemForm.md) | 评测任务集／软件代理邻接研究 | 安全 | 软件代理 | 软件环境 |
| [MineAmongUs](../benchmarks/4__MineAmongUs.md) | 评测任务集／直接具身评测 | 安全 | 多主体社会行为 | 交互仿真 |
| [ORBIT](../benchmarks/4__ORBIT.md) | 评测框架／软件代理邻接研究 | 能力、安全 | 软件代理 | 软件环境 |
| [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) | 评测任务集／直接具身评测 | 能力、鲁棒性 | 工业装配 | 实体测试件 |
| [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) | 评测任务集／直接具身评测 | 能力 | 无人机 | 离线轨迹 |
| [RoboAbstention](../benchmarks/4__RoboAbstention.md) | 评测任务集／直接具身评测 | 安全 | 机器人语义决策 | 静态情境／图像、真实数据 |
| [RoboJailBench](../benchmarks/4__RoboJailBench.md) | 评测任务集／直接具身评测 | 安全 | 机器人语义决策 | 静态情境／图像 |
| [STARS](../benchmarks/4__STARS.md) | 方法论文／具身研究底座 | 能力 | 人机交互、导航 | 离线轨迹、真实数据 |
| [SafeAgentBench](../benchmarks/4__SafeAgentBench.md) | 评测任务集／直接具身评测 | 能力、安全 | 机器人语义决策、机械臂操作 | 交互仿真 |
| [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) | 评测任务集／软件代理邻接研究 | 能力、安全 | 软件代理 | 软件环境 |
| [CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md) | 仿真平台／具身研究底座 | 能力、鲁棒性 | 自动驾驶 | 交互仿真 |
| [NAVSIM](../benchmarks/5__NAVSIM.md) | 评测任务集／直接具身评测 | 能力、安全 | 自动驾驶 | 交互仿真、真实数据 |
| [SafeBench](../benchmarks/5__SafeBench.md) | 评测框架／直接具身评测 | 能力、鲁棒性、安全 | 自动驾驶 | 交互仿真 |
| [VIPS](../benchmarks/5__VIPS.md) | 评测任务集／直接具身评测 | 能力、鲁棒性、安全 | 自动驾驶 | 交互仿真、真实数据 |
| [nuScenes](../benchmarks/5__nuScenes.md) | 评测任务集／直接具身评测 | 能力 | 自动驾驶、具身感知理解 | 真实数据、离线轨迹 |

## 3. 评测单元与指标分母

任务数、配置数、轨迹数、帧数、问题数、重复次数分别保留，不计算跨单位的“规模中位数”。SR、PR 等缩写可能同名异义；应先比较定义与分母。

| 条目 | 评测单元 | 指标定义与分母 |
|---|---|---|
| [ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md) | 情境—动作判断对 | 人类一致率：模型判断与人类标签一致的比例；分母／统计单位：已标注验证问题 |
| [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) | 场景×本体×难度／扰动的 episode | SR：任务完成率；分母／统计单位：全部测试 episode<br>CC / RET：累计安全代价／风险暴露时间；分母／统计单位：每条轨迹；各自归一化需查协议<br>不安全成功率：完成且不安全；分母／统计单位：全部 episode，非成功子集 |
| [HazardArena](../benchmarks/1__HazardArena.md) | 安全／危险场景配对的 episode | Safe SR / Unsafe SR：分别统计正常任务与危险任务完成；分母／统计单位：各自条件下的 episode<br>Attempt / Commit：尝试与提交行为的分阶段判定；分母／统计单位：对应条件的试验；不可替代最终完成 |
| [LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md) | 套件×任务×难度的 episode | SR：任务完成率；分母／统计单位：对应套件／难度的测试 episode<br>CR 等安全量：碰撞与约束违规，按套件分别读；分母／统计单位：对应协议 episode 或过程；须核验各指标定义 |
| [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) | episode，内部按抓握判断损伤 | Safe SR：完成且所有已评估抓握无损伤；分母／统计单位：全部测试 episode<br>PR：成功 episode 中物体保持完好的比例；分母／统计单位：成功 episode；无成功时未定义 |
| [RoboHarm](../benchmarks/1__RoboHarm.md) | 风险意图×输出接口的测试 | 拒绝率：对不安全请求拒绝执行的比例；分母／统计单位：相应接口的测试请求 |
| [SafeLIBERO](../benchmarks/1__SafeLIBERO.md) | 障碍场景中的 episode | CAR：全程避碰表现；分母／统计单位：对应测试 episode；依论文 CAR 定义<br>TSR / ETS：任务完成／执行步数；分母／统计单位：对应动作空间分别统计 |
| [SafeStage](../benchmarks/1__SafeStage.md) | 分阶段危险任务的 episode | SSR / USR：安全成功／不安全成功；分母／统计单位：全部 episode；SR=SSR+USR<br>评估器 F1：与人工核查的判定一致性；分母／统计单位：240 条评估器核查轨迹，非策略总样本 |
| [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) | 正常／特定条件下的定向失效测试 | 正常 SR：正常任务完成率；分母／统计单位：正常条件 episode<br>配置失效达成率：指定失效是否出现；分母／统计单位：满足威胁模型的测试 episode |
| [VLA-Arena](../benchmarks/1__VLA-Arena.md) | 任务×难度×语言／视觉设置 | SR：任务完成率；分母／统计单位：对应任务与设置的 episode<br>安全代价：约束违反的过程量；分母／统计单位：按 Safety 套件协议统计 |
| [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) | 双臂任务×遮挡条件的 episode | SR / TPS：完成与任务进度；分母／统计单位：各条件的测试 episode<br>CVG：观察臂移动带来的可见性增益；分母／统计单位：按相机贡献定义 |
| [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) | 相同前缀的干净／变化轨迹对 | 配对 SR 差：变化相对干净条件的完成差；分母／统计单位：同一组配对轨迹<br>过时动作暴露：事件发生后仍执行旧动作的程度；分母／统计单位：按动作块与触发时刻定义 |
| [LIBERO-Para](../benchmarks/2__LIBERO-Para.md) | 语义保持的改写指令配置 | SR：改写下任务完成率；分母／统计单位：对应改写测试 episode<br>PRIDE：按改写难度衡量成功；分母／统计单位：依论文关键词／句法距离加权<br>Far-GT 比例：远离参考轨迹的失败占比；分母／统计单位：失败轨迹，非全部 episode |
| [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) | 自然失败状态上的继续执行 | RSR：从失败状态恢复并完成原任务；分母／统计单位：给定失败状态的试验<br>RD / RC：恢复后的能力退化／一致性；分母／统计单位：指定阶段与多次执行的比较 |
| [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) | 视觉条件配置下的闭环 episode | SR 与退化：各视觉条件下任务完成变化；分母／统计单位：对应条件的 episode |
| [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) | 相同场景种子的配对长任务 | ΔSR：扰动与干净完成率差；分母／统计单位：配对 episode<br>首次失败阶段：失败发生的位置分布；分母／统计单位：依失败阶段统计口径 |
| [AgiBot World](../benchmarks/3__AgiBot-World.md) | 采集轨迹；另有策略评测任务 | 策略 SR：指定模型与训练设置下任务完成；分母／统计单位：模型评测 episode，不是百万采集轨迹 |
| [BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md) | 活动实例／任务 episode | 活动完成：BDDL 目标状态是否满足；分母／统计单位：各活动测试 episode |
| [BiDex-100](../benchmarks/3__BiDex-100.md) | 任务×本体×ID/OOD episode | SR / progress：全任务完成／阶段进度；分母／统计单位：对应任务和域的 episode |
| [CALVIN](../benchmarks/3__CALVIN.md) | 连续语言指令链 | 链成功与平均长度：连续完成前 k 项的比例／平均完成数；分母／统计单位：相同生成协议的测试链 |
| [COLOSSEUM](../benchmarks/3__COLOSSEUM.md) | RLBench 任务×扰动配置 | SR / 相对退化：干净与受扰动任务完成变化；分母／统计单位：对应测试 episode；相对值非百分点 |
| [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) | 模型×已有基准×完整运行种子 | SR：分套件任务完成率；分母／统计单位：相应测试任务配置<br>VRAM / latency：峰值显存／每次策略推理延迟；分母／统计单位：指定硬件和推理配置 |
| [LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md) | 终身学习任务序列及阶段评测 | FWT / NBT / AUC：新任务迁移／旧任务遗忘／成功曲线面积；分母／统计单位：同一任务顺序与训练评估协议 |
| [ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md) | 任务族×对象×初始化 | SR：指定成功谓词下完成率；分母／统计单位：同一控制空间和对象拆分的 episode |
| [Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md) | 跨来源轨迹与策略测试 episode | 迁移表现 / SR：跨本体训练后的任务完成；分母／统计单位：各研究设置的实机评测，非全部数据集 |
| [RoboCasa](../benchmarks/3__RoboCasa.md) | 厨房场景中的原子／复合任务 | SR：指定任务和学习设置下完成率；分母／统计单位：对应测试 episode |
| [RoboCasa365](../benchmarks/3__RoboCasa365.md) | 多任务／终身学习阶段与目标任务 | SR 与遗忘：分任务及学习阶段完成率；分母／统计单位：同一目标拆分、数据量和训练阶段 |
| [RoboChrono](../benchmarks/3__RoboChrono.md) | 视频观察前缀上的问题／时间定位 | 选择题准确率：六项选择题回答正确率；分母／统计单位：有效问题；不含时间定位<br>R@1 at tIoU≥0.5：首个时间预测满足重叠阈值；分母／统计单位：时间定位问题 |
| [RoboComb](../benchmarks/3__RoboComb.md) | 原子技能重组任务 | 组合 SR：完成完整组合任务；分母／统计单位：对应已见／未见组合 episode |
| [RoboFollow](../benchmarks/3__RoboFollow.md) | 同场景的多个语言可行分支 | Intent / Execution：选对意图与完成动作分阶段评价；分母／统计单位：按各阶段有效试验分别统计 |
| [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) | 任务×指代变体的 episode | SR 与显隐差：隐式指代相对显式指令的任务表现；分母／统计单位：对应指令条件 episode |
| [RoboMIND](../benchmarks/3__RoboMIND.md) | 多本体轨迹；附学习实验 | 策略表现：不同数据来源／规模的学习对照；分母／统计单位：具体模型实验；不以采集规模代替测试分母 |
| [RoboReel](../benchmarks/3__RoboReel.md) | 人类观察条件下的机器人任务 | 任务 SR：从观察学习后完成操作；分母／统计单位：对应方法与测试条件 episode |
| [RoboTwin](../benchmarks/3__RoboTwin.md) | 双臂任务 episode | SR：终点姿态达标且全程无碰撞；分母／统计单位：对应任务、示范量与输入模态试验 |
| [SimplerEnv](../benchmarks/3__SimplerEnv.md) | 相同策略与任务的模拟／真实表现对 | MMRV / Pearson r：排序违背／模拟真实相关性；分母／统计单位：所测策略与任务组，不是全部机器人分布 |
| [Spa-Bench](../benchmarks/3__Spa-Bench.md) | 匹配实体场景×指令条件 | ID/OOD SR：空间配置内外的操作完成率；分母／统计单位：各配置条件实机试验<br>配对直接指令差：移除空间描述后任务表现差；分母／统计单位：同场景配对试验 |
| [VLABench](../benchmarks/3__VLABench.md) | 原子／复合任务与物体类别拆分 | SR / VLM 正确率：分别评价操作执行和语义理解；分母／统计单位：各接口的任务 episode／问题，不能合并 |
| [Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md) | 交互工具环境中的测试用例 | 安全分 / helpfulness：风险和任务有用性分开评价；分母／统计单位：对应测试用例；评分器规则见论文 |
| [Bench2Dex](../benchmarks/4__Bench2Dex.md) | 任务—本体设置×扰动通道 | 稳定 SR：达到并稳定停留目标的比例；分母／统计单位：每个任务通道的 rollout<br>LSCR：锁存阶段完成比例；分母／统计单位：按多阶段任务协议 |
| [DESPITE](../benchmarks/4__DESPITE.md) | 形式化规划任务 | 计划可行性 / 安全性：有效计划与无危险计划分别判定；分母／统计单位：明确的任务集；条件安全率另有分母 |
| [EmbodiedBench](../benchmarks/4__EmbodiedBench.md) | 四种环境中的测试任务 | 任务 SR：不同动作抽象下任务完成率；分母／统计单位：每环境任务；总体为规定聚合 |
| [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) | 治理场景模板×系统参与档位 | 治理指标向量：授权、恢复、升级、接管、审计的合规表现；分母／统计单位：声明参与档位内的可评估场景 |
| [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) | 给定接触历史的续接规划实例 | SR：安全解决，含正确拒绝不可行实例；分母／统计单位：全部实例<br>OSR：安全且按用户优先级最优地解决；分母／统计单位：全部实例；参考有动作和时间界 |
| [INFUSE](../benchmarks/4__INFUSE.md) | 兼容任务—风险情形的工作流轨迹 | 风险达成率：风险目标被实现；分母／统计单位：有效风险测试轨迹<br>正常任务成功：无风险干预时正常目标完成；分母／统计单位：正常参考运行 |
| [IS-Bench](../benchmarks/4__IS-Bench.md) | 交互场景的高层动作序列 | SR / SSR：任务完成／满足安全过程的完成；分母／统计单位：相应提示条件的试验<br>SRec：应处置风险的召回；分母／统计单位：实际触发的风险或措施，非全部任务 |
| [LABIT](../benchmarks/4__LABIT.md) | 原语／子装配／完整装配重复 | 可靠性 / 完成时间：各类原语完成与装配耗时；分母／统计单位：同一供料等级下重复装配 |
| [MSK-Bench](../benchmarks/4__MSK-Bench.md) | 肌肉驱动身体的控制任务 | SR / 稳健性：任务完成及受扰表现；分母／统计单位：指定任务与扰动 episode<br>生理诊断：激活代价、关节平滑、肌电相似；分母／统计单位：对应运动时序与参考数据 |
| [MemForm](../benchmarks/4__MemForm.md) | 记忆形成条件与后续查询对 | 条件 ASR：受影响条件下目标行为出现；分母／统计单位：每个模型各自 eligible queries |
| [MineAmongUs](../benchmarks/4__MineAmongUs.md) | 游戏局及跨时刻行为标签 | 胜率 / 行为标签：隐藏角色目标表现与言语／非言语行为；分母／统计单位：游戏局／标注原子及行为弧分别统计 |
| [ORBIT](../benchmarks/4__ORBIT.md) | 任务×拓扑×风险／防护条件 | 风险与正常成功率：风险目标和正常任务效用分别统计；分母／统计单位：配对运行中的对应条件 |
| [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) | 形状×公差×位置／朝向的插接场景 | 任务配置与插接评价：按配置评估插接与适应性；分母／统计单位：统一实测计分／重复协议尚待核验 |
| [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) | 轨迹中决策前缀的标准化问答 | 准确率：下一决策问题回答正确；分母／统计单位：相应配置选择／测试集问题 |
| [RoboAbstention](../benchmarks/4__RoboAbstention.md) | 静态图像上的应弃权指令 | 弃权率：在不可解／不足信息条件下停止或澄清；分母／统计单位：应弃权的指令；非正常请求误拒率 |
| [RoboJailBench](../benchmarks/4__RoboJailBench.md) | 正常／危险意图对照的规划请求 | Security Rate：危险目标被拒绝；分母／统计单位：危险请求<br>Utility Rate / SU-HM：正常接受／安全与效用调和均值；分母／统计单位：正常请求；SU-HM 合成两种条件率 |
| [STARS](../benchmarks/4__STARS.md) | 已有数据集上的分类／线性探针样本 | 宏 F1：社会场景下游分类性能；分母／统计单位：SEAN Together／SocialNav-SUB 的指定拆分 |
| [SafeAgentBench](../benchmarks/4__SafeAgentBench.md) | 高层代理规划任务的交互执行 | 拒绝率 / 任务表现：危险拒绝与计划执行分别评价；分母／统计单位：详细／抽象／长任务条件分别统计 |
| [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) | 软件技能环境中的风险案例 | ASR / 任务成功：风险目标与正常目标分别完成；分母／统计单位：155 案例下对应运行条件 |
| [CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md) | 原始模拟器中的驾驶路线试验 | 到达目标 / 违规：驾驶任务完成与过程事件；分母／统计单位：原论文城镇／天气／任务条件 |
| [NAVSIM](../benchmarks/5__NAVSIM.md) | 真实记录场景上的短时非反应式展开 | PDMS：含碰撞、区域、进度等的复合驾驶量；分母／统计单位：同一轨迹展开协议，非单一事故概率 |
| [SafeBench](../benchmarks/5__SafeBench.md) | 路线×风险场景×策略×观察设置 | 综合分及分量：安全、功能、礼仪的多项指标；分母／统计单位：同一归一化／权重协议，不是碰撞概率 |
| [VIPS](../benchmarks/5__VIPS.md) | 车路配对场景×两阶段观察 | EPDMS：真实／合成观察阶段的综合规划评价；分母／统计单位：同一两阶段评测协议<br>通信需求：协同策略的信息传输开销；分母／统计单位：相同部署和传输设定 |
| [nuScenes](../benchmarks/5__nuScenes.md) | 带三维标注的场景／感知预测 | NDS / AMOTA / AMOTP：三维检测及跟踪评价；分母／统计单位：原论文的类目、时间窗口与测试拆分 |

## 4. 协议、证据与资源状态

真实数据采集、真实策略执行、模拟／真实配对验证分别标记。未知只表示当前笔记未充分核验。项目入口确认不等于代码、数据、许可证、评测器和基线已全部可用。

| 条目 | 对照与划分 | 重复／统计及边界 | 真机证据 | 项目入口状态 |
|---|---|---|---|---|
| [ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md) | 多模态、伤害事件、困境分别评测；生成数据与人工标签分开 | 验证问题 2,273，其中 1,140 有人类标签；其余统计细节待核 | 尚未确认执行实验 | 已确认项目入口 |
| [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) | Safe-Core／Lang／Vis 分组，任务结构与语言视觉等级分开 | 66 场景、5 本体；种子与各组重复数待核 | 尚未确认执行实验 | 已确认项目入口 |
| [HazardArena](../benchmarks/1__HazardArena.md) | 场景及操作模板可比，动作参与者／目标关系及指令改变 | 51 任务、七类风险；真机和仿真分表 | 报告真实执行 | 已确认项目入口 |
| [LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md) | AAG／HRI／TSA／FSHOA／SSR，5×5×3=75 配置；训练任务另计 | 19,664 示范是训练数据，不能作为测试样本数 | 尚未确认执行实验 | 已确认项目入口 |
| [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) | 脆断、软变形、薄壁三轴分难度；离线损伤求解 | 报告高／中难对象聚合，不混入低难无损对象 | 尚未确认执行实验 | 候选待确认 |
| [RoboHarm](../benchmarks/1__RoboHarm.md) | 文本、代码、末端／关节接口比较 | 真机末端 612 次、关节 252 次；不同接口分母不同 | 报告真实执行 | 候选待确认 |
| [SafeLIBERO](../benchmarks/1__SafeLIBERO.md) | 目标附近／路径阻挡两级；平移和完整动作空间分开 | 32 场景×50 次=1,600 episode；真机两项任务另计 | 报告真实执行 | 已确认项目入口 |
| [SafeStage](../benchmarks/1__SafeStage.md) | 初始、执行中、完成后分开；完成后继续观察 5 秒 | 97 任务；成功中不安全比例另以成功数为分母 | 尚未确认执行实验 | 候选待确认 |
| [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) | 分失效类别，正常效用与异常行为分别比较 | 各失效条件重复数及置信区间待核 | 报告真实执行 | 已确认项目入口 |
| [VLA-Arena](../benchmarks/1__VLA-Arena.md) | L0 训练，L1／L2 泛化；四能力维度分开 | 170 任务、11 套件；真机案例不能代表全部任务 | 报告真实执行 | 已确认项目入口 |
| [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) | Clean、Stage、随机时刻遮挡；训练在 Stage | 五任务、500 示范；部分策略三种种子，π0.5 设置不同 | 尚未确认执行实验 | 已确认项目入口 |
| [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) | 固定状态／种子／轨迹前缀，单次持续事件 | 8,000 对／16,000 rollout；bootstrap、配对检验及多重比较 | 尚未确认执行实验 | 已确认项目入口 |
| [LIBERO-Para](../benchmarks/2__LIBERO-Para.md) | 固定 LIBERO-Goal 状态，分别变化动作／物体表达 | 4,092 条指令、七种模型配置；DTW 是代理诊断 | 尚未确认执行实验 | 已确认项目入口 |
| [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) | 四级恢复；正常起点与失败起点分开 | 2,000 余失败状态；每任务重复与时间上限见原协议 | 尚未确认执行实验 | 已确认项目入口 |
| [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) | 退化、过时、来源冲突、场景变化四维 | 3,296 配置；约 19.6 万模拟、200 真机试验分开 | 报告真实执行 | 已确认项目入口 |
| [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) | 先筛干净可完成任务，含零变化相机对照 | 四任务×20×13=1,040 rollout；一个 GR00T-N1.5 | 尚未确认执行实验 | 已确认项目入口 |
| [AgiBot World](../benchmarks/3__AgiBot-World.md) | 采集质量管线与不同预训练来源对照 | 100 万余轨迹、217 任务；规模属于训练数据 | 报告真实执行 | 已确认项目入口 |
| [BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md) | 仿真解法与 CollectTrash 真实对应场景比较 | 1,000 活动为任务库规模；真机验证是小子集 | 模拟／真实配对验证 | 仅平台入口 |
| [BiDex-100](../benchmarks/3__BiDex-100.md) | 五能力轴、匹配种子的 ID/OOD | 106 任务，2 种种子×25 episode／任务；示范另计 | 尚未确认执行实验 | 已确认项目入口 |
| [CALVIN](../benchmarks/3__CALVIN.md) | 单环境、多环境、三环境训练／第四环境测试 | 34 类任务；具体链样本数和训练设置须随版本报告 | 尚未确认执行实验 | 仅平台入口 |
| [COLOSSEUM](../benchmarks/3__COLOSSEUM.md) | 14 条扰动轴单独及组合施加 | 20 任务、五种方法；四项真机任务另计 | 报告真实执行 | 已确认项目入口 |
| [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) | 固定 checkpoint，多轴分表，协议忠实度标注 | 三个完整运行种子；标准差不是 episode 置信区间 | 尚未确认执行实验 | 已确认项目入口 |
| [LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md) | 空间、物体、目标变化；顺序学习和预训练设置 | 130 原始任务；后续常用 40 任务协议另标 | 尚未确认执行实验 | 仅平台入口 |
| [ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md) | 见过／未见对象、RGB-D／点云与控制模式分别报告 | 本次以 ManiSkill2 的 20 任务族为准；示范帧数非测试数 | 报告真实执行 | 仅平台入口 |
| [Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md) | 单来源与跨来源混合，域内／域外任务分开 | 22 本体、100 万余轨迹；版本、过滤和比例须注明 | 报告真实执行 | 仅平台入口 |
| [RoboCasa](../benchmarks/3__RoboCasa.md) | 场景、任务、多样性与示范来源对照 | 原版 100 任务，不能混入 365 版规模 | 报告真实执行 | 仅平台入口 |
| [RoboCasa365](../benchmarks/3__RoboCasa365.md) | 原子、已见／未见复合；预训练与目标微调分开 | 365 任务库；50 目标任务等拆分不能全部混计 | 尚未确认执行实验 | 仅平台入口 |
| [RoboChrono](../benchmarks/3__RoboChrono.md) | 严格只看当前前缀，未来仅生成标签 | 1,816 视频、39 场景；视频数不是题目数 | 真实数据，不据此认定执行 | 已确认项目入口 |
| [RoboComb](../benchmarks/3__RoboComb.md) | Oracle-HSE、Ordered-HSE、整段指令分开；交接状态诊断 | 原子示范与组合微调须分别报告；重复次数待核 | 尚未确认执行实验 | 已确认项目入口 |
| [RoboFollow](../benchmarks/3__RoboFollow.md) | 布局、语义重组及其组合；保持动作支持 | 九种 VLA／WAM，真机小型试验；等级不保证单调 | 报告真实执行 | 已确认项目入口 |
| [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) | 直接、推理、空间、上下文指代与显式对照 | 11 任务、40 变体；三种种子×50 次／条件 | 尚未确认执行实验 | 已确认项目入口 |
| [RoboMIND](../benchmarks/3__RoboMIND.md) | 统一遥操作、质量和语言标注，跨本体适配 | 约 10.7 万轨迹、479 任务；测试独立性待核 | 尚未确认执行实验 | 已确认项目入口 |
| [RoboReel](../benchmarks/3__RoboReel.md) | 视频条件／人体关键点方法，配对机器人数据访问分别说明 | 10 任务；模拟／真实比较范围待逐项核验 | 模拟／真实配对验证 | 已确认项目入口 |
| [RoboTwin](../benchmarks/3__RoboTwin.md) | 20／50／100 示范，2D／3D 输入分开；真实微调另计 | 本次 CVPR 2025 的 14 任务版本，不混入 RoboTwin 2.0 | 报告真实执行 | 仅平台入口 |
| [SimplerEnv](../benchmarks/3__SimplerEnv.md) | 视觉匹配、变体聚合及验证误差基线 | Google Robot 六 checkpoint；任务平均与合并相关不可混用 | 模拟／真实配对验证 | 仅平台入口 |
| [Spa-Bench](../benchmarks/3__Spa-Bench.md) | 对象与动作已见、留出空间配置；直接指令／改写／无需动作对照 | 2,892 评测轨迹与 1,200 示范分开；三模型完整评测 | 报告真实执行 | 已确认项目入口 |
| [VLABench](../benchmarks/3__VLABench.md) | 见过／未见物体类别，VLA／模块化流程／VLM 分开 | 100 任务=60 原子+40 复合；自动示范与测试分开 | 尚未确认执行实验 | 仅平台入口 |
| [Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md) | 多来源精炼去重、风险类别与失败模式分开 | 349 环境、2,000 用例、16 模型；环境数非测试数 | 不适用 | 已确认项目入口 |
| [Bench2Dex](../benchmarks/4__Bench2Dex.md) | 不变／等变七种扰动；触觉接口统一但主策略输入不同 | 26 设置、12 本体；每通道 50 rollout；宏平均等权 | 尚未确认执行实验 | 已确认项目入口 |
| [DESPITE](../benchmarks/4__DESPITE.md) | 物理与规范危险；规划能力和危险意识分解 | 全库 12,279；主结果困难集 1,044，由面板模型表现筛选 | 尚未确认执行实验 | 已确认项目入口 |
| [EmbodiedBench](../benchmarks/4__EmbodiedBench.md) | 高／低层动作、六能力子集、语言／视觉消融 | 1,128 测试任务、24 模型；不同环境接口不得混作机器人成功率 | 尚未确认执行实验 | 已确认项目入口 |
| [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) | minimal／standard／fleet／full；能力范围与失败分开 | 原型与 worked example，未核验统一大规模排行榜 | 尚未确认执行实验 | 已确认项目入口 |
| [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) | 历史／优先级／接触事件对照，独立 evaluator 与隐藏 reference | 624 实例、134 任务族；部分配对集合相互重叠 | 尚未确认执行实验 | 已确认项目入口 |
| [INFUSE](../benchmarks/4__INFUSE.md) | 隔离环境和统一约定；规则验证／模型判分分开 | 40 任务、56 情形；并非全笛卡尔积都执行 | 不适用 | 已确认项目入口 |
| [IS-Bench](../benchmarks/4__IS-Bench.md) | 操作前／后措施顺序；提醒等级与安全 CoT 分开 | 161 场景、388 风险；模型、提醒条件须同时注明 | 尚未确认执行实验 | 已确认项目入口 |
| [LABIT](../benchmarks/4__LABIT.md) | 定位送料、无序平放、杂乱箱三级；难度与可靠性分别报告 | 真实基线五次，平均 32 分钟；小样本不外推 | 报告真实执行 | 已确认项目入口 |
| [MSK-Bench](../benchmarks/4__MSK-Bench.md) | 三任务族、五控制范式；残差案例伴随目标和时序变化 | 22 任务；任务成功与生理一致性独立统计 | 尚未确认执行实验 | 已确认项目入口 |
| [MemForm](../benchmarks/4__MemForm.md) | 五形成接口的正常／受影响对照，两种回答格式 | 六模型 eligible 子集不同，宏均值不构成同分布排名 | 不适用 | 已确认项目入口 |
| [MineAmongUs](../benchmarks/4__MineAmongUs.md) | 固定模型改框架、固定框架改模型 | 23 种行为原子；裁判一致性与胜率分开 | 尚未确认执行实验 | 已确认项目入口 |
| [ORBIT](../benchmarks/4__ORBIT.md) | Inspect 配置化因子设计，隔离执行；条件共享任务 | 约 90 条件；Wilson／bootstrap 区间，实验只覆盖支持空间的切片 | 不适用 | 已确认项目入口 |
| [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) | 五种形状、可配置间隙与布局；模块化 STL | 正文未核验到大规模基线对比，勿填成功率 | 仅确认实体测试件 | 已确认项目入口 |
| [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) | 不提供决策后的信息，提示温度选择与最终评测分开 | 10,178 实例；70.48% 来自配置选择阶段，不是飞行成功率 | 尚未确认执行实验 | 已确认项目入口 |
| [RoboAbstention](../benchmarks/4__RoboAbstention.md) | 接地、约束、指令三阶段生成；每图每类去重复 | 1,250 图、6,069 指令；图像与问题数不同 | 真实数据，不据此认定执行 | 已确认项目入口 |
| [RoboJailBench](../benchmarks/4__RoboJailBench.md) | 同场景意图对照；正常基线与压力条件分开 | 18 类后果、六数据来源；SR 缩写非任务成功 | 尚未确认执行实验 | 已确认项目入口 |
| [STARS](../benchmarks/4__STARS.md) | 图类型、标注比例、跨数据预训练和监督对照 | 1% 与 100% 标签等设置；不能推断闭环导航风险 | 真实数据，不据此认定执行 | 已确认项目入口 |
| [SafeAgentBench](../benchmarks/4__SafeAgentBench.md) | 显式与隐式风险，语义与执行两种判定 | 750 任务、十危险类、九代理基线；高层动作有底层控制器 | 尚未确认执行实验 | 已确认项目入口 |
| [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) | 每案例独立规则验证；框架—模型组合分开 | 47 任务、155 案例、六风险域；二成功量可同时为真 | 不适用 | 已确认项目入口 |
| [CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md) | 训练／未见城镇与天气；四类任务 | 原始 2017 论文允许忽略红灯和限速；不是现代 Leaderboard | 尚未确认执行实验 | 仅平台入口 |
| [NAVSIM](../benchmarks/5__NAVSIM.md) | 与闭环表现相关性比较；背景交通不反应 | 143 队／463 提交是竞赛参与数，非独立引用或任务数 | 真实数据，不据此认定执行 | 已确认项目入口 |
| [SafeBench](../benchmarks/5__SafeBench.md) | 正常与关键场景对照，多种生成方法统一接口 | 八场景类、四生成算法／四驾驶 RL 方法；输入设置分开 | 尚未确认执行实验 | 已确认项目入口 |
| [VIPS](../benchmarks/5__VIPS.md) | 真实观察 Stage 1 与偏移合成观察 Stage 2 分开 | 源数据筛选、合成质量及模型比较范围须标注 | 真实数据，不据此认定执行 | 已确认项目入口 |
| [nuScenes](../benchmarks/5__nuScenes.md) | 检测与跟踪允许的历史窗口不同；感知与后续规划扩展分开 | 1,000×20 秒场景；23 标注类不等于榜单评估类数 | 真实数据，不据此认定执行 | 仅平台入口 |

## 5. 来源与影响力

引用计数沿用已核验日期的 OpenAlex 记录；不合并版本计数，不对全库求和。原表使用关系是候选采用证据，未完成逐篇独立复用审计。完整方法与结果见[精读报告](benchmark-paper-deep-read.md)。

| 条目 | 本次阅读的原始来源 | 被引次数 | 观测日期 | 原表使用关联数 |
|---|---|---:|---|---:|
| [ASIMOV Benchmark](../benchmarks/1__ASIMOV-Benchmark.md) | [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)（2503.08663v1） | [0](https://openalex.org/W4414578652) | 2026-11-04 | 1 |
| [ForesightSafety-VLA](../benchmarks/1__ForesightSafety-VLA.md) | [ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079)（2606.27079v2） | [0](https://openalex.org/W7166132482) | 2026-11-04 | 0 |
| [HazardArena](../benchmarks/1__HazardArena.md) | [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447)（2604.12447v3） | [0](https://openalex.org/W7154513284) | 2026-11-04 | 0 |
| [LIBERO-Safety](../benchmarks/1__LIBERO-Safety.md) | [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)（2606.23686v2） | [0](https://openalex.org/W7165682249) | 2026-11-04 | 0 |
| [ManiPhysicsBench](../benchmarks/1__ManiPhysicsBench.md) | [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)（2610.02802v1） | [0](https://openalex.org/W7220458345) | 2026-11-04 | 0 |
| [RoboHarm](../benchmarks/1__RoboHarm.md) | [Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control](https://arxiv.org/abs/2610.14043)（2610.14043v1） | [0](https://openalex.org/W7221820979) | 2026-11-04 | 0 |
| [SafeLIBERO](../benchmarks/1__SafeLIBERO.md) | [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)（2512.11891v2） | [0](https://openalex.org/W4417446096) | 2026-11-04 | 0 |
| [SafeStage](../benchmarks/1__SafeStage.md) | [SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation](https://arxiv.org/abs/2609.21223)（2609.21223v1） | [0](https://openalex.org/W7213988552) | 2026-11-04 | 0 |
| [Trap-LIBERO / Trap-RoboTwin](../benchmarks/1__Trap-LIBERO-Trap-RoboTwin.md) | [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2608.26578v1） | [0](https://openalex.org/W7204530163) | 2026-11-04 | 0 |
| [VLA-Arena](../benchmarks/1__VLA-Arena.md) | [VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models](https://arxiv.org/abs/2512.22539)（2512.22539v4） | [0](https://openalex.org/W7117763818) | 2026-11-04 | 0 |
| [BAVO-Bench](../benchmarks/2__BAVO-Bench.md) | [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)（2609.37292v1） | [0](https://openalex.org/W7214940409) | 2026-11-04 | 0 |
| [LIBERO-MAX](../benchmarks/2__LIBERO-MAX.md) | [LIBERO-MAX: Do Robot Policies Adapt When the World Changes?](https://arxiv.org/abs/2609.36518)（2609.36518v1） | [0](https://openalex.org/W7214921693) | 2026-11-04 | 0 |
| [LIBERO-Para](../benchmarks/2__LIBERO-Para.md) | [LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301)（2603.28301v3） | [0](https://openalex.org/W7147537669) | 2026-11-04 | 1 |
| [LIBERO-RECOVER](../benchmarks/2__LIBERO-RECOVER.md) | [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178)（2609.05178v3） | [0](https://openalex.org/W7211887144) | 2026-11-04 | 0 |
| [LIBERO-VPro](../benchmarks/2__LIBERO-VPro.md) | [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](https://arxiv.org/abs/2609.24350)（2609.24350v1） | [0](https://openalex.org/W7214051566) | 2026-11-04 | 0 |
| [RoboCasa-Shift](../benchmarks/2__RoboCasa-Shift.md) | [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2610.27861v1） | [0](https://openalex.org/W7223122581) | 2026-11-04 | 0 |
| [AgiBot World](../benchmarks/3__AgiBot-World.md) | [AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088)（2503.06669v5） | [13](https://openalex.org/W4416748905) | 2026-11-04 | 0 |
| [BEHAVIOR-1K](../benchmarks/3__BEHAVIOR-1K.md) | [BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation](https://arxiv.org/abs/2403.09227)（2403.09227v1） | [7](https://openalex.org/W4392872989) | 2026-11-04 | 1 |
| [BiDex-100](../benchmarks/3__BiDex-100.md) | [BiDex-100: A Comprehensive Benchmark for Bimanual Dexterous Manipulation Across 100+ Simulation Tasks](https://arxiv.org/abs/2610.25459)（2610.25459v2） | [0](https://openalex.org/W7223068191) | 2026-11-04 | 0 |
| [CALVIN](../benchmarks/3__CALVIN.md) | [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)（2112.03227v4） | [189](https://openalex.org/W4226073959) | 2026-11-04 | 3 |
| [COLOSSEUM](../benchmarks/3__COLOSSEUM.md) | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191)（2402.08191v2） | [29](https://openalex.org/W4402354166) | 2026-11-04 | 0 |
| [IndustrialVLA-Bench](../benchmarks/3__IndustrialVLA-Bench.md) | [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)（2609.25562v2） | [0](https://openalex.org/W7214113903) | 2026-11-04 | 0 |
| [LIBERO（基础套件）](../benchmarks/3__LIBERO-基础套件.md) | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)（2306.03310v2） | [136](https://openalex.org/W7133220882) | 2026-11-04 | 29 |
| [ManiSkill / ManiSkill2](../benchmarks/3__ManiSkill-ManiSkill2.md) | [ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills](https://arxiv.org/abs/2302.04659)（2302.04659v1） | [24](https://openalex.org/W4320165654) | 2026-11-04 | 1 |
| [Open X-Embodiment](../benchmarks/3__Open-X-Embodiment.md) | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)（2310.08864v9） | [113](https://openalex.org/W4387764390) | 2026-11-04 | 1 |
| [RoboCasa](../benchmarks/3__RoboCasa.md) | [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)（2406.02523v1） | [4](https://openalex.org/W4399424845) | 2026-11-04 | 3 |
| [RoboCasa365](../benchmarks/3__RoboCasa365.md) | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)（2603.04356v1） | [0](https://openalex.org/W7133954504) | 2026-11-04 | 1 |
| [RoboChrono](../benchmarks/3__RoboChrono.md) | [RoboChrono: A Real Robot Benchmark for Streaming Task Understanding](https://arxiv.org/abs/2609.36605)（2609.36605v1） | [0](https://openalex.org/W7214955540) | 2026-11-04 | 0 |
| [RoboComb](../benchmarks/3__RoboComb.md) | [Exploring the Limits of Combinatorial Generalization in Embodied Manipulation](https://arxiv.org/abs/2610.15425)（2610.15425v1） | [0](https://openalex.org/W7221756428) | 2026-11-04 | 0 |
| [RoboFollow](../benchmarks/3__RoboFollow.md) | [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](https://arxiv.org/abs/2609.25636)（2609.25636v1） | [0](https://openalex.org/W7214246107) | 2026-11-04 | 0 |
| [RoboIRG-Bench](../benchmarks/3__RoboIRG-Bench.md) | [RoboIRGBench: Benchmarking Implicit Referential Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2609.34384)（2609.34384v1） | [0](https://openalex.org/W7214772858) | 2026-11-04 | 0 |
| [RoboMIND](../benchmarks/3__RoboMIND.md) | [RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](https://arxiv.org/abs/2412.13877)（2412.13877v3） | [23](https://openalex.org/W4414050913) | 2026-11-04 | 0 |
| [RoboReel](../benchmarks/3__RoboReel.md) | [Monkey See, Can Monkey Do? A Benchmark for Evaluating Robot Skill Learning by Observation](https://arxiv.org/abs/2609.08209)（2609.08209v4） | [0](https://openalex.org/W7212081197) | 2026-11-04 | 0 |
| [RoboTwin](../benchmarks/3__RoboTwin.md) | [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://doi.org/10.1109/CVPR52734.2025.02575)（2504.13059v1） | [31](https://openalex.org/W4413144615) | 2026-11-04 | 7 |
| [SimplerEnv](../benchmarks/3__SimplerEnv.md) | [Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)（2405.05941v1） | [4](https://openalex.org/W4396822572) | 2026-11-04 | 2 |
| [Spa-Bench](../benchmarks/3__Spa-Bench.md) | [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696)（2610.12696v1） | [0](https://openalex.org/W7221577967) | 2026-11-04 | 0 |
| [VLABench](../benchmarks/3__VLABench.md) | [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://doi.org/10.1109/ICCV51701.2025.01037)（2412.18194v1） | [16](https://openalex.org/W4405783861) | 2026-11-04 | 0 |
| [Agent-SafetyBench](../benchmarks/4__Agent-SafetyBench.md) | [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470)（2412.14470v2） | [6](https://openalex.org/W4405627542) | 2026-11-04 | 0 |
| [Bench2Dex](../benchmarks/4__Bench2Dex.md) | [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](https://arxiv.org/abs/2609.15726)（2609.15726v1） | [0](https://openalex.org/W7213308421) | 2026-11-04 | 0 |
| [DESPITE](../benchmarks/4__DESPITE.md) | [Using large language models for embodied planning introduces systematic safety risks](https://arxiv.org/abs/2604.18463)（2604.18463v2） | [0](https://openalex.org/W7155060036) | 2026-11-04 | 0 |
| [EmbodiedBench](../benchmarks/4__EmbodiedBench.md) | [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560)（2502.09560v3） | [1](https://openalex.org/W4407590542) | 2026-11-04 | 0 |
| [EmbodiedGovBench](../benchmarks/4__EmbodiedGovBench.md) | [EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems](https://arxiv.org/abs/2604.11174)（2604.11174v1） | [0](https://openalex.org/W7154418749) | 2026-11-04 | 0 |
| [HygieneRoboBench](../benchmarks/4__HygieneRoboBench.md) | [HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots](https://arxiv.org/abs/2610.08642)（2610.08642v1） | [0](https://openalex.org/W7221007195) | 2026-11-04 | 0 |
| [INFUSE](../benchmarks/4__INFUSE.md) | [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776)（2610.20776v1） | [0](https://openalex.org/W7222558873) | 2026-11-04 | 0 |
| [IS-Bench](../benchmarks/4__IS-Bench.md) | [IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402)（2506.16402v3） | [2](https://openalex.org/W7138977141) | 2026-11-04 | 0 |
| [LABIT](../benchmarks/4__LABIT.md) | [LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks](https://arxiv.org/abs/2610.16398)（2610.16398v1） | [0](https://openalex.org/W7221815075) | 2026-11-04 | 0 |
| [MSK-Bench](../benchmarks/4__MSK-Bench.md) | [MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics](https://arxiv.org/abs/2609.26872)（2609.26872v1） | [0](https://openalex.org/W7214208713) | 2026-11-04 | 0 |
| [MemForm](../benchmarks/4__MemForm.md) | [MemForm: Benchmarking Memory Formation Poisoning in LLM Agents](https://arxiv.org/abs/2610.14431)（2610.14431v1） | [0](https://openalex.org/W7221777130) | 2026-11-04 | 0 |
| [MineAmongUs](../benchmarks/4__MineAmongUs.md) | [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions](https://arxiv.org/abs/2608.30428)（2608.30428v1） | [0](https://openalex.org/W7204938515) | 2026-11-04 | 0 |
| [ORBIT](../benchmarks/4__ORBIT.md) | [ORBIT: A Framework for Multi-Agent Safety and Security Evaluations](https://arxiv.org/abs/2609.33102)（2609.33102v1） | [0](https://openalex.org/W7214782110) | 2026-11-04 | 0 |
| [Peg-in-Bench](../benchmarks/4__Peg-in-Bench.md) | [Peg-in-Bench: A Modular Benchmark for High-Precision Robotic Insertion](https://arxiv.org/abs/2609.00906)（2609.00906v1） | [0](https://openalex.org/W7206171071) | 2026-11-04 | 0 |
| [PhysAI-Bench](../benchmarks/4__PhysAI-Bench.md) | [PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI](https://arxiv.org/abs/2609.23695)（2609.23695v1） | [0](https://openalex.org/W7214012534) | 2026-11-04 | 0 |
| [RoboAbstention](../benchmarks/4__RoboAbstention.md) | [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544)（2605.20544v1） | [0](https://openalex.org/W7162010380) | 2026-11-04 | 0 |
| [RoboJailBench](../benchmarks/4__RoboJailBench.md) | [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](https://arxiv.org/abs/2605.19328)（2605.19328v1） | [0](https://openalex.org/W7161775162) | 2026-11-04 | 0 |
| [STARS](../benchmarks/4__STARS.md) | [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245)（2609.40245v3） | [0](https://openalex.org/W7215077318) | 2026-11-04 | 0 |
| [SafeAgentBench](../benchmarks/4__SafeAgentBench.md) | [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)（2412.13178v5） | [2](https://openalex.org/W4405562840) | 2026-11-04 | 0 |
| [SkillSafetyBench](../benchmarks/4__SkillSafetyBench.md) | [SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces](https://arxiv.org/abs/2605.12015)（2605.12015v3） | [0](https://openalex.org/W7161027243) | 2026-11-04 | 0 |
| [CARLA / CARLA Leaderboard](../benchmarks/5__CARLA-CARLA-Leaderboard.md) | [CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938)（1711.03938v1） | [3759](https://openalex.org/W2767621168) | 2026-11-04 | 4 |
| [NAVSIM](../benchmarks/5__NAVSIM.md) | [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://doi.org/10.52202/079017-0902)（2406.15349v2） | [63](https://openalex.org/W4415798424) | 2026-11-04 | 2 |
| [SafeBench](../benchmarks/5__SafeBench.md) | [SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682)（2206.09682v4） | [48](https://openalex.org/W7133222348) | 2026-11-04 | 0 |
| [VIPS](../benchmarks/5__VIPS.md) | [VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation](https://arxiv.org/abs/2609.02462)（2609.02462v1） | [0](https://openalex.org/W7207785702) | 2026-11-04 | 0 |
| [nuScenes](../benchmarks/5__nuScenes.md) | [nuScenes: A multimodal dataset for autonomous driving](https://arxiv.org/abs/1903.11027)（1903.11027v5） | [7179](https://openalex.org/W2925148167) | 2026-11-04 | 3 |

## 6. 数据与尚未完成的核查

[统一调研数据](../data/benchmark_survey.json)含 122 条，分类依据保存在[人工编码](../data/benchmark_survey_annotations.json)。[论文证据目录](../data/survey_paper_registry.json)连接原表 193 条记录与 6 篇补入的已读原始来源，共 199 个书目记录。原始论文 Excel 保留为历史快照，当前比较以新增统一调研工作簿为准。

未完成的工作已列入[覆盖与证据缺口](survey-gap-register.md)。本轮没有穷尽全部领域、没有独立复现实验，也没有逐项目验收代码／数据／许可证。60 个无已确认项目入口的非重点条目继续存档。
