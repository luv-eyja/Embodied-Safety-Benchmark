# 术语表：本库出现的缩写与技术词

> 更新日期 2026-11-04。每条给：英文全称 → 中文名 → 一句话定义 → 详细解释 → 常见误读。

这张表是**本库自己的解释**，不是论文原话的摘抄；目的是让人不读原论文也知道这个词在说什么、它除以什么、在哪一步容易读错。每个 benchmark 文档的第 10 节只列该文实际出现的术语，并链回这里。

读法建议：看到一个指标先问三件事——①它衡量的是“做完”还是“没出事”；②它的分母是什么；③它旁边有没有配套指标（成功率／安全率／代价）。三条都对齐了，跨基准比较才有意义。

## 评测单位与统计

| 术语 | 英文全称 | 中文 | 解释 | 常见误读 |
|---|---|---|---|---|
| **bootstrap** | bootstrap resampling | 自助重采样（置信区间） | 把 n 个 episode 的结果当作样本，反复有放回地抽 n 个算统计量，重复上千次得到分布，取 2.5%–97.5% 分位即 95% 区间。配对实验（同一初始状态跑基线与方法）应先算差值再 bootstrap，而不是各自算区间再比较。 | — |
| **checkpoint** | model checkpoint | 检查点（模型权重快照） | 训练时每隔若干步就把参数存成一个文件，这个文件就是 checkpoint。评测他人模型必须用同一份 checkpoint，否则分数不可比；“公共 checkpoint”指作者或社区公开可下载的权重，意味着不需要自己重训，但也意味着测的是“开箱表现”而不是“方法上限”。 | 模型名相同不代表同一份权重：版本、步数、是否微调都会改变结果。 |
| **episode** | episode | 回合 | 评测时把场景重置，让策略从初态跑到终止条件，这一段完整交互叫一个 episode。成功率＝成功 episode 数 ÷ 全部 episode 数。一个任务跑 25 次就是 25 个 episode，不是 1 个。 | 把“任务数”“配置数”当 episode 分母，会让成功率虚高。 |
| **Pearson** | Pearson correlation coefficient | 皮尔逊相关系数 | 在仿真评测里常用于回答“仿真分数能不能预测真机分数”：把每个策略的仿真成功率与真机成功率配对，算 r。r 高说明排序一致，但不代表绝对分数相同。 | — |
| **pp** | percentage point | 百分点 | 百分点用于描述两个百分数之间的绝对差。写“提升 8%”会被理解成相对提升（30%×1.08），而实际是加了 8 个百分点。本库统一用 pp 表示差值。 | — |
| **rollout** | rollout | 展开／推演 | 强化学习与策略评测里，让策略在环境中实际执行并记录状态-动作序列，叫一次 rollout。多数论文 rollout 数＝episode 数，但涉及多次采样或多候选时两者不同，读表要看清。 | rollout 数、episode 数、候选轨迹数三者混用。 |
| **seed** | random seed | 随机种子 | 仿真里的物体初始位姿、相机噪声、策略采样都由随机数决定。固定 seed 让结果可复现；跑多个 seed 才能区分“方法更好”和“这次运气好”。只报一个 seed 的成绩不能当稳定结论。 | — |
| **Wilson** | Wilson score interval | Wilson 区间 | 成功率是 0–1 的比例，样本只有几十个 episode 时，正态近似的区间会越界或过窄。Wilson 区间在极端比例（接近 0 或 1）和小样本下仍表现稳定，因此评测论文常用它报成功率的不确定性。 | — |

## 指标与缩写

| 术语 | 英文全称 | 中文 | 解释 | 常见误读 |
|---|---|---|---|---|
| **AMOTA** | Average Multi-Object Tracking Accuracy | 平均多目标跟踪准确率 | 跟踪既要找到目标（recall）又要保持身份（ID switch），AMOTA 在多个召回阈值上取平均以减轻“只刷高分阈值”的问题。常与 AMOTP（位置误差）一起报告。 | — |
| **AMOTP** | Average Multi-Object Tracking Precision | 平均多目标跟踪精度 | AMOTP 衡量“跟得准不准”，与 AMOTA 的“跟得全不全、身份稳不稳”互补。只看其中一个容易得出片面结论。 | — |
| **ASR** | Attack Success Rate | 攻击成功率 | 在安全攻击评测中，ASR 表示攻击者让模型做出目标危险行为的比例，越低越安全；在语音相关论文里 ASR 指 automatic speech recognition。本库两种都出现，必须靠上下文区分。 | 把攻击成功率当成语音识别，或反过来。 |
| **CAR** | Collision Avoidance Rate | 避碰率 | SafeLIBERO 等安全约束类基准的主指标：衡量策略是否撞到障碍。它只看碰撞这一类违规，不覆盖拿错物体、顺序错误等语义风险。 | — |
| **CC** | Cumulative safety Cost | 累计安全代价 | 与只看是否违规的二值指标不同，CC 对每次违规按严重度累加，因此能区分“擦到一次”和“反复碰撞”。全称与权重按各论文定义，跨基准不可直接比较。 | — |
| **CVG** | Camera Visibility Gain | 相机可见性增益 | 用于主动视觉／遮挡恢复类基准：同一状态下比较移动相机前后目标被看到的程度，用来区分“真的在找”与“碰巧恢复”。增益不等于任务成功。 | — |
| **DTW** | Dynamic Time Warping | 动态时间规整距离 | 两条轨迹速度不同也能比较，算法通过非线性的时间对齐求最小累计距离。常被当成“偏离参考轨迹多少”的代理指标，但它不等于失败原因，只是轨迹层证据。 | — |
| **EPDMS** | Extended PDMS / Pseudo-simulation Driving Metric Score | 扩展规划综合分 | EPDMS 沿用 PDMS 的加权思路，但评分阶段更多、条件更严（如按两阶段伪仿真评估）。论文报 EPDMS 时通常同时说明是 navtest 还是 navhard 拆分，两者不可混读。 | — |
| **ETS** | Execution Steps（本库 SafeLIBERO 口径） | 执行步数 | 约束层常通过减速或绕行来避免碰撞，代价是步数变多。ETS 把这种代价显式化：同样的 CAR/TSR，步数更少的策略更实用。 | — |
| **F1** | F1 score | 调和平均分 | F1 = 2PR ÷ (P+R)，在正负样本不平衡时比准确率更能反映真实水平。本库用它评价“评估器判定是否与人工一致”这类元评测，而不是策略本身。 | — |
| **LSCR** | Latched Stage Completion Rate | 锁存阶段完成率 | 普通阶段分可能因为后段失败而被“回滚”，LSCR 强调“曾经做到过”这一事实，用于区分“从未完成”与“完成过但最后崩了”。 | — |
| **mAP** | mean Average Precision | 平均精度均值 | 先在每个类别上算 precision-recall 曲线下面积（AP），再对类别取平均。mAP 对类别不平衡敏感，也依赖 IoU 阈值设定。 | — |
| **mIoU** | mean Intersection over Union | 平均交并比 | IoU = 交集 ÷ 并集。mIoU 对所有类别取平均，用于 BEV 地图分割等任务；它对小目标不友好，因此常另报 per-class 结果。 | — |
| **MMRV** | Mean Maximum Rank Violation | 平均最大排名违背 | 把若干策略按仿真分和按真机分各排一次序，看名次差多少，取最大／平均即 MMRV。它是“仿真能否替代真机做选型”的直接指标，与 Pearson r 互补。 | — |
| **MSE** | Mean Squared Error | 均方误差 | 世界模型类工作常用下一状态预测的 MSE 衡量拟合程度。MSE 小只说明拟合好，不代表规划可用；它与成功率不是同一件事。 | — |
| **NDS** | nuScenes Detection Score | nuScenes 检测综合分 | NDS 不是单一 mAP，而是把 mAP 与位置、尺寸、朝向、速度、属性等误差项按权重合成，用于鼓励“框得准”而非只“框到”。因此 NDS 高不一定 mAP 高。 | — |
| **nDTW** | normalized DTW | 归一化 DTW | DTW 的绝对值受轨迹长度与尺度影响，nDTW 除以路径长度或对齐代价上界后再比较。用于世界模型预测、导航轨迹相似度等。 | — |
| **OSR** | Optimal Safe Resolution | 最优安全解决率 | 与 SR 相比多了“成本最优”这一层：既安全解决又在声明的时间／动作界内接近最优。参考最优由隐藏方案给出，因此只在声明边界内成立。 | — |
| **PDMS** | Planning Driving Metric Score | 规划综合分（自动驾驶） | PDMS 由若干子项加权得到，子项包括碰撞、偏离可行驶区域、行驶方向、速度舒适度、到达进度等。因为有权重，它不等于碰撞概率，也不能跨权重版本比较。 | — |
| **PR** | Preservation Rate（本库 ManiPhysicsBench 口径） | 保全率 | 用于物体保全类评测：SR 是完成率，Safe SR 是无损完成率，PR = Safe SR ÷ SR。SR 为 0 时 PR 无定义，所以论文通常同时给三个数。PR 不是精确率（precision），同名不同义。 | 把 PR 当 precision，或只报 PR 不报 SR。 |
| **PRIDE** | PRIDE（LIBERO-Para 论文提出的诊断指标） | 改写难度加权成功率 | 普通成功率把所有指令一视同仁，无法区分“只是扛住了同义替换”和“真的理解了改写”。PRIDE 用关键词差异与句式结构差异估计每条改写的难度，再对成功加权。权重由人工设定，因此它适合做诊断，不宜替代原始成功率。 | — |
| **PSNR** | Peak Signal-to-Noise Ratio | 峰值信噪比 | PSNR 用像素误差的对数变换衡量重建／生成图像质量。视频世界模型论文常报它，但它与人眼感知和任务可用性的相关性有限。 | — |
| **R@1** | Recall at 1 | 首位命中率 | R@k 表示前 k 个结果里有正确答案的比例；R@1 最严格。常用于时序定位、检索式评测，与 tIoU 阈值搭配使用。 | — |
| **RET** | Risk Exposure Time | 风险暴露时间 | RET 描述“在危险区待了多久”，即使最终没碰撞，长时间贴边也说明控制不稳。与 CC 一起构成过程级风险，用来补终点是否成功的不足。 | — |
| **SBU** | success-but-unsafe rate | 成功但不安全率 | 不安全的成功回合 ÷ 成功回合；分母是成功回合。 本库收录该词是为了判读各基准的报告口径：同一数值在不同口径下的含义差别很大。 | 与 USR 分母不同，直接比较会高估或低估数倍。 |
| **SR** | Success Rate | 成功率 | 最常见的指标：完成任务的比例。分母通常是全部 episode，不是成功数。本库至少四种 SR：任务成功率、RoboJailBench 的危险指令拒绝率（Security Rate）、SafeStage 的 SR=SSR+USR、HygieneRoboBench 的安全解决率。跨基准比较前必须先对齐定义与分母。 | 把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。 |
| **SSR** | Safe Success Rate | 安全成功率 | SSR 把“做完”和“没出事”同时计入，是安全基准的主指标之一。注意它的分母是全部 episode，而不是成功 episode；SR − SSR 就是“做完但违规”的那部分。 | — |
| **SU-HM** | Safety-Utility Harmonic Mean | 安全—效用调和平均 | 安全策略如果一律拒绝就能拿满安全分，但没有用。SU-HM 用调和平均把 Security Rate 与 Utility Rate 绑在一起，任一项过低都会拉低总分。 | — |
| **tIoU** | temporal Intersection over Union | 时间交并比 | 预测的动作起止时间与人工标注区间求交并比；常以“tIoU ≥ 0.5 的样本比例”报告，避免只报一个平均值的乐观偏差。 | — |
| **TPS** | Task Progress Score | 任务进展分 | 成功／失败是二值的，阶段进展分能区分“差一步”和“完全没动”。它依赖阶段划分与权重，不能与成功率互换。 | — |
| **TSR** | Task Success Rate | 任务成功率 | TSR 与普通 SR 同义，但在安全论文里常单独列出，以便和 CAR（避碰率）并列：一个策略可能 CAR 高（慢慢挪）而 TSR 低。两者要成对报告。 | — |
| **USR** | Unsafe Success Rate | 不安全成功率 | USR 与 SSR 的分母都是全部 episode，所以 SR = SSR + USR。若想知道成功轨迹里有多大比例危险，要算 USR ÷ SR。两者相差可达数倍，混用会严重误判风险。 | 把 USR 直接当作“成功里的违规比例”，两者分母不同。 |
| **VR** | Violation Rate | 违规率 | VR 只统计“有没有踩线”，与任务完成解耦。一个策略可以 VR 很低但 SR 也很低（什么都不做），也可以 VR 高但 SR 高（为了完成任务冒险）。要和 SR/SSR 一起读。 | — |
| **VSI** | violation severity index | 违规严重度指数 | 在事件次数之外按物理影响加权的违规度量。 本库收录该词是为了判读各基准的报告口径：同一数值在不同口径下的含义差别很大。 | 严重度与频次是两件事，只报其一无法判断风险。 |

## 模型与方法

| 术语 | 英文全称 | 中文 | 解释 | 常见误读 |
|---|---|---|---|---|
| **ACT** | Action Chunking with Transformers | 动作分块 Transformer 策略 | ACT 每次输出一个动作块（chunk），以减少累积误差和推理频率，是 ALOHA 等工作提出的经典基线。它没有语言推理能力，但常被用来说明“简单方法也能拿到不错的成功率”。 | — |
| **AEGIS** | AEGIS safety layer（SafeLIBERO 论文提出） | AEGIS 安全约束层 | AEGIS 不是新策略，而是套在既有策略外面的“安全过滤器”：策略给出名义动作，AEGIS 用 CBF 约束和 QP 把它修到安全侧。后续工作在它之上比较避碰率，因此它同时是方法基线和对照对象。 | — |
| **CBF** | Control Barrier Function | 控制障碍函数 | CBF 定义一个“离危险有多远”的函数，并要求控制输入使该函数不下降过快，从而理论上保证安全集不被突破。它依赖动力学模型与状态估计，实际部署常与 QP（二次规划）一起求解，所以论文写 CBF-QP。 | — |
| **DP** | Diffusion Policy | 扩散策略 | Diffusion Policy（DP）把动作序列当成要生成的样本，用扩散过程去噪得到动作块。它是最常见的“没有安全机制”的对照，因此能说明安全层或安全训练到底带来多少增益。 | — |
| **DP3** | 3D Diffusion Policy | 三维扩散策略 | DP3 把扩散策略（Diffusion Policy）的输入从图像换成点云，减少视角与纹理依赖。本库 RoboTwin 等条目用 DP3 与 2D DP 对比，说明输入模态的影响。 | — |
| **GO-1** | AgiBot GO-1 | AgiBot 通用策略 | GO-1 与 AgiBot World 数据配套发布，用于展示该数据训练出的通用能力。它不是第三方基准的基线，引用其成功率时要注意数据与评测是同源的。 | — |
| **GR00T** | NVIDIA GR00T N1 / N1.5 | GR00T 机器人基础模型 | GR00T N1.5 是较新的通用操作策略，本库多条基准（Bench2Dex、RoboCasa-Shift、LIBERO-RECOVER 等）出现它的名字，通常是“在 X 上微调后评测”或“作为对照”。 | — |
| **GRPO** | Group Relative Policy Optimization | 组相对策略优化 | GRPO 对同一提示采样多条轨迹，用组内相对得分做基线来估计优势，省掉 critic 网络。VLA 的后训练常用它把成功率或安全率直接当奖励优化。 | — |
| **IL** | Imitation Learning | 模仿学习 | IL 把示教轨迹当作监督信号（行为克隆为其最简单形式），不需要奖励函数。它的经典弱点是分布偏移：一旦偏离示教分布，误差会累积。 | — |
| **LLM** | Large Language Model | 大语言模型 | 在具身系统里，LLM 通常负责把指令拆成步骤、选择工具或生成代码；它看不到图，需要 VLM 或感知模块提供状态。DESPITE、SafeAgentBench 测的是这一层的安全。 | — |
| **MLLM** | Multimodal Large Language Model | 多模态大模型 | 与 VLM 基本同义，论文习惯不同。本库按原文用词保留，指的都是“看图＋读文、输出文字”的模型。 | — |
| **MPC** | Model Predictive Control | 模型预测控制 | MPC 在每个控制周期求解有限时域的最优控制问题，只执行第一步，然后重算。它对模型误差敏感，但在有明确约束（避障、限速）的场景里表现稳定。 | — |
| **OpenVLA** | OpenVLA（含 OpenVLA-oft 变体） | OpenVLA 开源策略 | OpenVLA 用公开机器人数据训练并开源权重，因此成为复现与安全评测的首选被测对象；oft 变体做了优化微调。报告它的安全分数时要注明是零样本还是微调、以及用哪一版 checkpoint。 | — |
| **QP** | Quadratic Programming | 二次规划 | 安全层需要在“尽量贴近原动作”和“满足安全约束”之间取平衡，这正是一个带线性约束的二次规划问题。求解失败或不可行时，通常退化为急停，这本身也是风险点。 | — |
| **RDT** | Robotics Diffusion Transformer | 机器人扩散 Transformer | RDT-1B 用大规模机器人数据训练扩散式动作生成，是 2024–2026 年间常用的强基线。它没有语言推理层，比较时要注意输入模态与训练数据量。 | — |
| **RL** | Reinforcement Learning | 强化学习 | 在机器人里 RL 常用于微调策略或学习恢复行为。它的效果强依赖奖励设计与仿真保真度，因此本库会区分“RL 训练后评测”与“直接评测已有 checkpoint”。 | — |
| **SFT** | Supervised Fine-Tuning | 监督微调 | SFT 是最常见的适配方式：给定状态-动作对，最小化动作预测误差。它区别于 RL（用奖励优化）和预训练（大规模多任务数据）。本库描述用法时会明确是“SFT 微调”还是“预训练数据”。 | — |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | VLA 把视觉编码器、语言模型与动作解码头连在一起，用机器人示教数据微调。它区别于“VLM 只回答文字”或“只做规划的 LLM 代理”。本库 62 条里大多数评测对象是 VLA。 | — |
| **VLM** | Vision-Language Model | 视觉语言模型 | VLM 输出文字（计划、判断、坐标），不直接输出关节或末端动作。IS-Bench、RoboAbstention 这类基准测的就是 VLM 作为规划器时的安全判断，而不是底层控制。 | — |
| **VLSA** | Vision-Language-Action with plug-and-play Safety constraint layer | 带安全约束层的 VLA | VLSA 与 AEGIS 指同一套工作：VLSA 是整体方法（VLA + 安全层），AEGIS 是其中的安全约束层实现。后续论文有的引用 VLSA、有的引用 AEGIS，比较时要确认指的是同一基线。 | — |
| **WAM** | World-Action Model | 世界—动作模型 | WAM 把世界模型（预测下一帧状态）与动作生成联合训练，希望通过“想象后果”改善决策。本库有基准专门比较 WAM 与 VLA 的表现差异（如 LIBERO-VPro）。 | — |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | π0 与 π0.5 是在大规模跨本体数据上训练的通用策略，常被当作“强基线”。注意它既是基线，也是很多工作微调的起点；引用它的分数时要说明是零样本还是微调后。 | — |

## 协议、难度与评价口径

| 术语 | 英文全称 | 中文 | 解释 | 常见误读 |
|---|---|---|---|---|
| **ABC→D** | train on A/B/C, test on D | 三环境训练、第四环境测试 | 该协议检验“换环境后的指令跟随”，与只看同环境成功率的差别很大。现代论文的数据量与历史窗口常与原设定不同，跨论文比较必须确认协议版本。 | — |
| **ablation** | ablation study | 消融实验 | 消融是判断“到底哪个部件起作用”的标准做法。读消融要看是否只改了一个变量：同时改数据量与结构、或同时改目标与参考轨迹，结论就不能归到单一模块。 | — |
| **closed-loop** | closed-loop execution | 闭环执行 | 闭环意味着模型的动作会改变它下一步看到的状态，误差会累积或自我纠正。与之相对的“开环”指一次生成整段轨迹或只看离线数据。本库会把“图像问答／离线轨迹／闭环执行／真机”分开标注，因为分数不可互换。 | — |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | 论文提交时要选分类，决定它出现在哪个列表。本库的引文检索用 `cat:cs.RO 或 cat:cs.CV` 限定范围，因此“arXiv 摘要命中”只覆盖这两个分类里能检索到的论文，不等于全网提及。 | — |
| **digital twin** | digital twin | 数字孪生 | 数字孪生强调“与真实场景对应”，通常由扫描或生成模型构建，再放机器人进去采数据。它的价值取决于保真度：几何对齐容易，物理与材质对齐难。 | — |
| **domain randomization** | domain randomization | 域随机化 | 域随机化是 sim-to-real 的常用手段：把仿真里可能变化的因素都随机一遍，使策略对真实世界的差异更不敏感。代价是训练更难收敛，且随机范围本身需要按真实情况设定。 | — |
| **grounding** | visual grounding | 视觉接地 | 接地正确是执行正确的前提：指代错了，后面动作再稳也是错的。RoboIRG-Bench 这类基准专门测“隐式指代”（目标没被明说）的接地能力，并把它与操作能力分开。 | — |
| **HiL** | Hardware-in-the-Loop | 硬件在环 | HiL 让真实 ECU 或控制器接收仿真的传感器信号并回传控制指令，用于验证时序与失效。它比纯仿真更接近实车，但仍不覆盖真实道路的多变性。 | — |
| **HRI** | Human-Robot Interaction | 人机交互 | HRI 评测常涉及社交规范、可读性与人类偏好，指标多为问卷或标注一致性，与任务成功率属于不同证据类型，不能互换。 | — |
| **ID** | In-Distribution | 分布内 | ID 分数回答“在见过的条件下能做多好”，是 OOD 的对照。两者之差才是泛化能力的度量；只报 ID 会高估实际部署表现。 | — |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 档位名字各基准不同，重点是看它把训练放在哪一档、测试放到哪一档。多数 VLA 基准先在 L0 训练、再往 L1/L2 评测，所以 L0 与 L2 的分数差既是难度差也是分布差。 | — |
| **leaderboard** | leaderboard | 排行榜 | 榜单成绩受提交时间、评测版本、是否允许集成影响。同一 leaderboard 的不同版本（如 navtest 与 navhard）不可混排。 | — |
| **OOD** | Out-of-Distribution | 分布外 | OOD 的具体做法差别很大：换物体、换纹理、换相机、换场景都算。基准必须说明 OOD 是怎么划的（类别、场景还是随机种子），否则“OOD 分数”无法比较。 | — |
| **open-loop** | open-loop evaluation | 开环评测 | 开环评测便宜、可复现，但无法捕捉“一步错、步步错”的累积失效。自动驾驶的轨迹评测、动作定位题目多属开环，不能直接当闭环安全结论。 | — |
| **privileged** | privileged information / privileged state | 特权信息／特权状态 | 仿真里可以读到物体精确位置、接触力、是否违规；真机只能估计。用特权状态判分是合理的，但若把特权信息也喂给策略，成绩就不能迁移到真机——读基准时要注意这一点。 | — |
| **sim-to-real** | sim-to-real transfer | 仿真到真实的迁移 | 落差来源包括渲染与光照、摩擦与接触、执行器延迟、传感器噪声。论文若只报仿真分数，必须单独说明是否有真机验证，否则不能推断部署表现。 | — |
| **SOTA** | State of the Art | 当前最佳水平 | SOTA 只在同一协议、同一数据划分、同一评测版本下才有意义。本库引用时保留原文的“称 SOTA”，不把不同年份、不同预算的结果放在同一榜单里比较。 | — |
| **teleoperation** | teleoperation | 遥操作 | 遥操作是主流机器人数据的来源：人做示范，系统记录关节／末端位置、图像与语言标注。数据质量取决于操作者水平与重定向方式，这会直接影响后续评测的可复现性。 | — |
| **zero-shot** | zero-shot evaluation | 零样本评测 | 零样本分数衡量“通用能力”，与“在该基准上微调后”的分数没有可比性。论文常把两者并列，读表时必须看是哪种；同一个模型零样本 20%、微调后 60% 很常见。 | — |

## 仿真平台、数据格式与硬件

| 术语 | 英文全称 | 中文 | 解释 | 常见误读 |
|---|---|---|---|---|
| **BDDL** | Behavior Domain Definition Language | 行为域定义语言 | BDDL 把“把杯子放进洗碗机且水槽是空的”写成可解析的逻辑表达式，评测器据此判断任务是否完成。LIBERO、BEHAVIOR-1K 及其扩展（UBDDL）都用这一套；改动它就意味着改了任务定义。 | — |
| **CARLA** | CARLA | CARLA 自动驾驶仿真器 | CARLA 提供城市地图、可控传感器与交通参与者，可编程构造危险场景。CARLA Leaderboard 是建在其上的独立评测协议，模拟器论文与排行榜成绩不能混为一谈。 | — |
| **CoppeliaSim** | CoppeliaSim (V-REP) | CoppeliaSim 仿真器 | CoppeliaSim 支持多种机器人模型与传感器，常与 RLBench 一起出现。它的接触与渲染精度不如专用引擎，因此多用于任务与扰动设计而非高保真接触评测。 | — |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | Franka 有成熟的 ROS／控制接口与力矩传感，因此大量真机评测用它。论文里“真机验证”若只写 Franka 而不写任务数与重复次数，证据强度有限。 | — |
| **GUI** | Graphical User Interface | 图形界面（软件代理） | GUI 代理（如 Spa-Bench／SPA-Bench 一类）在屏幕上点击与输入，属于软件环境而非物理机器人。本库把它们作为“软件代理邻接研究”单列。 | — |
| **Isaac** | Isaac Sim / Isaac Lab | Isaac 仿真与训练框架 | Isaac 系在 GPU 上并行跑上千环境，常用于高吞吐训练与域随机化。Bench2Dex、BiDex-100 等双臂灵巧操作基准建在其上。 | — |
| **Mineflayer** | Mineflayer | Minecraft 机器人接口库 | Mineflayer 让模型通过 API 在沙盒里移动、合成、交互，因此可以把“身体行为”当作可观测信号。MineAmongUs 用它研究语言之外的欺骗行为。 | — |
| **MuJoCo** | MuJoCo | MuJoCo 物理引擎 | MuJoCo 以稳定快速的接触求解著称，是机器人学习最常用的物理后端。它的接触参数（摩擦、软硬）会显著影响抓取成功率，因此同一任务在不同版本上的分数不可直接比。 | — |
| **OmniGibson** | OmniGibson | OmniGibson 仿真环境 | OmniGibson 基于 Omniverse，扩展了刚体之外的软体、流体与温度／烹饪状态，用于长时程家务。代价是资产重、渲染与物理开销大，复现门槛高。 | — |
| **RGB** | RGB image observation | 彩色图像观测 | 论文说“RGB-only”是指策略只看彩色图像，用来说明深度／触觉／点云的增益。这类行不能与多模态输入的行直接比较。 | — |
| **RLBench** | RLBench | RLBench 操作基准环境 | RLBench 提供大量带语言指令的桌面操作任务与演示，COLOSSEUM 等泛化基准在它上面施加扰动。它与 LIBERO 的任务集不同，分数不可互换。 | — |
| **RLDS** | Reinforcement Learning Datasets format | RLDS 数据格式 | RLDS 用嵌套的序列结构存 observation/action/reward，Open X-Embodiment 等多机构数据靠它对齐。格式统一不等于语义统一：动作空间、坐标系、控制频率仍需单独适配。 | — |
| **robosuite** | robosuite | robosuite 操作仿真库 | robosuite 提供机械臂、夹爪与标准任务，是很多操作基准的底座。基准之间的差异通常来自任务集、资产与控制接口，而不是物理引擎本身。 | — |
| **SAPIEN** | SAPIEN | SAPIEN 仿真引擎 | SAPIEN 提供带关节的物体模型与物理仿真，适合开门、抽屉、装配这类任务。它比通用刚体引擎更强调可交互物体，但材质与接触模型仍是近似。 | — |
| **UAV** | Unmanned Aerial Vehicle | 无人机 | UAV 类基准（PhysAI-Bench 等）常把已有飞行日志转成“下一步该做什么”的选择题。它测决策，不测动力学与控制，因此准确率不等于飞行安全率。 | — |
| **UBDDL** | Unified BDDL（本库 LIBERO-Safety 口径） | 扩展版 BDDL | UBDDL 保留 BDDL 的对象与谓词，增加运行时状态与安全检查钩子，使评测能在执行过程中判断违规，而不只在终点判定。 | — |
| **V2X** | Vehicle-to-Everything | 车联万物（车路协同） | V2X 评测关心通信带宽、延迟与协同感知带来的规划收益。VIPS 这类基准用两阶段伪仿真评估：先用真实观察，再在专家轨迹附近用合成观察探测策略。 | — |

## 仍然看不懂时

本库的口径是：宁可写“论文未给数值／未说明分母”，也不替论文补一个更漂亮的说法。如果某个缩写在本表里找不到，说明它只在一篇论文里出现、尚未成为通名——那就按该条文档第 8、9 节给出的上下文理解，或回到原文确认。

## 专有名称：只标“是什么”，不展开解释

下面这些是产品、机构、许可证、发表 venue 与基准的名字，不是可解释的技术概念。标 `正文标注` 的词会在文档里第一次出现处直接加括号（例：GPT-4o（LLM 模型））；基准名不加 inline，避免打断论文标题与表格。

| 名称 | 是什么 | 说明 | 正文标注 |
|---|---|---|---|
| **Claude** | LLM 模型 | Anthropic | 是 |
| **GPT-4o** | LLM 模型 | OpenAI | 是 |
| **GPT-5.5** | LLM 模型 | OpenAI | 是 |
| **GPT-6** | LLM 模型 | OpenAI，文中为 GPT-6 Astra | 是 |
| **Paimon-0** | VLA 模型 | RoboCasa365 公开榜单上的参考模型 | 是 |
| **RT-X** | VLA 模型 | Open X-Embodiment 论文提出的跨本体策略 | 是 |
| **SmolVLA** | VLA 模型 | Hugging Face 的开源小型 VLA | 是 |
| **XR-1** | VLA 模型 | 小米机器人策略，RoboCasa365 上的对照模型 | 是 |
| **Gemini** | VLM 模型 | Google | 是 |
| **Qwen2.5-VL** | VLM 模型 | 阿里 Qwen 系列的开源多模态版本 | 是 |
| **Qwen3-VL** | VLM 模型 | 同上，更新一代 | 是 |
| **CARLA** | 仿真平台 | 开源城市驾驶仿真器 | 否 |
| **Isaac Lab** | 仿真平台 | NVIDIA 的 GPU 并行仿真训练框架 | 是 |
| **AAAI** | 会议／期刊 | AAAI Conference on Artificial Intelligence | 是 |
| **CoRL** | 会议／期刊 | Conference on Robot Learning | 是 |
| **CVPR** | 会议／期刊 | IEEE/CVF Conference on Computer Vision and Pattern Recognition | 是 |
| **ECCV** | 会议／期刊 | European Conference on Computer Vision | 是 |
| **EMNLP** | 会议／期刊 | Conference on Empirical Methods in Natural Language Processing | 是 |
| **ICCV** | 会议／期刊 | International Conference on Computer Vision | 是 |
| **ICLR** | 会议／期刊 | International Conference on Learning Representations | 是 |
| **ICML** | 会议／期刊 | International Conference on Machine Learning | 是 |
| **ICRA** | 会议／期刊 | IEEE International Conference on Robotics and Automation | 是 |
| **IROS** | 会议／期刊 | IEEE/RSJ International Conference on Intelligent Robots and Systems | 是 |
| **NeurIPS** | 会议／期刊 | Conference on Neural Information Processing Systems | 是 |
| **RA-L** | 会议／期刊 | IEEE Robotics and Automation Letters | 是 |
| **RSS** | 会议／期刊 | Robotics: Science and Systems | 是 |
| **Agent-SafetyBench** | 基准 | 通用工具代理安全；邻接参考 | 否 |
| **ASIMOV Benchmark** | 基准 | 机器人语义安全判断／数据与方法 | 否 |
| **BAVO-Bench** | 基准 | 仿真双臂主动视觉 | 否 |
| **BEHAVIOR-1K** | 基准 | 1000 项家务活动的长时程基准 | 否 |
| **Bench2Dex** | 基准 | 双手视触觉仿真与数据平台 | 否 |
| **BiDex-100** | 基准 | 双手灵巧操作仿真 | 否 |
| **CALVIN** | 基准 | 语言条件长时程操作基准 | 否 |
| **CARLA / CARLA Leaderboard** | 基准 | 驾驶仿真平台；原论文与榜单需区分 | 否 |
| **COLOSSEUM** | 基准 | 系统扰动的操作泛化基准 | 否 |
| **DESPITE** | 基准 | 具身规划的安全评测 | 否 |
| **EmbodiedBench** | 基准 | 跨环境具身代理能力基准 | 否 |
| **EmbodiedGovBench** | 基准 | 治理评测协议与原型框架 | 否 |
| **ForesightSafety-VLA** | 基准 | VLA 安全诊断基准 | 否 |
| **HazardArena** | 基准 | VLA 语义安全基准 | 否 |
| **HygieneRoboBench** | 基准 | 接触历史驱动的卫生规划 | 否 |
| **IndustrialVLA-Bench** | 基准 | 多基准评测与复现证据框架 | 否 |
| **INFUSE** | 基准 | 软件代理工作流安全；邻接参考 | 否 |
| **IS-Bench** | 基准 | VLM 代理交互安全基准 | 否 |
| **LABIT** | 基准 | 真实工业长时程装配 | 否 |
| **LIBERO** | 基准 | 本库最常用的终身学习操作基准套件 | 否 |
| **LIBERO-MAX** | 基准 | 执行中改变环境的动态鲁棒性基准 | 否 |
| **LIBERO-Para** | 基准 | LIBERO 的指令改写扩展 | 否 |
| **LIBERO-Plus** | 基准 | LIBERO 的扰动扩展 | 否 |
| **LIBERO-Pro** | 基准 | LIBERO 的难例扩展 | 否 |
| **LIBERO-RECOVER** | 基准 | 仿真自然失败状态恢复 | 否 |
| **LIBERO-Safety** | 基准 | LIBERO 的安全扩展 | 否 |
| **LIBERO-VPro** | 基准 | 闭环视觉鲁棒性 | 否 |
| **LIBERO（基础套件）** | 基准 | 终身机器人学习基础基准 | 否 |
| **ManiPhysicsBench** | 基准 | 物体保全物理评估基准 | 否 |
| **ManiSkill** | 基准 | 通用操作技能基准（SAPIEN） | 否 |
| **ManiSkill / ManiSkill2** | 基准 | 可泛化操作仿真平台 | 否 |
| **ManiSkill2** | 基准 | ManiSkill 的第二代 | 否 |
| **MemForm** | 基准 | 代理记忆可靠性诊断；邻接参考 | 否 |
| **MineAmongUs** | 基准 | 三维多代理社会行为沙盒 | 否 |
| **MSK-Bench** | 基准 | 肌肉驱动全身控制 | 否 |
| **NAVSIM** | 基准 | 非反应式自动驾驶伪仿真评测 | 否 |
| **ORBIT** | 基准 | 多代理安全评测框架；邻接参考 | 否 |
| **Peg-in-Bench** | 基准 | 可打印物理插接基准设计 | 否 |
| **PhysAI-Bench** | 基准 | UAV 任务轨迹中的离线决策问答 | 否 |
| **RLBench** | 基准 | CoppeliaSim 上的机械臂任务集 | 否 |
| **RoboAbstention** | 基准 | 具身图像条件下的弃权判断 | 否 |
| **RoboCasa** | 基准 | 家庭场景大规模仿真基准 | 否 |
| **RoboCasa-Shift** | 基准 | 长时程操作阶段鲁棒性 | 否 |
| **RoboCasa365** | 基准 | RoboCasa 的 365 任务版本 | 否 |
| **RoboChrono** | 基准 | 机器人流式视频理解 | 否 |
| **RoboComb** | 基准 | 原子技能组合泛化 | 否 |
| **RoboFollow** | 基准 | 语言驱动的操作分支选择 | 否 |
| **RoboHarm** | 基准 | 模拟与真机机器人接口安全 | 否 |
| **RoboIRG-Bench** | 基准 | 隐式指代与具身记忆 | 否 |
| **RoboJailBench** | 基准 | 具身对抗攻击与防御基准 | 否 |
| **RoboReel** | 基准 | 从观察学习的操作基准 | 否 |
| **RoboTwin** | 基准 | 双臂操作数据生成与评测 | 否 |
| **SafeAgentBench** | 基准 | 交互仿真中的安全任务规划 | 否 |
| **SafeBench** | 基准 | 自动驾驶安全关键场景平台（另有同名 LVLM 基准） | 否 |
| **SafeLIBERO** | 基准 | LIBERO 的避碰安全扩展 | 否 |
| **SafeStage** | 基准 | 分阶段安全评测基准 | 否 |
| **SimplerEnv** | 基准 | 真实策略的仿真代理评测 | 否 |
| **SkillSafetyBench** | 基准 | 技能型软件代理安全；邻接参考 | 否 |
| **Spa-Bench** | 基准 | 真实机器人空间接地 | 否 |
| **STARS** | 基准 | 表征学习方法；并非新 benchmark | 否 |
| **Trap-LIBERO / Trap-RoboTwin** | 基准 | VLA 定向失效诊断／安全研究 | 否 |
| **TrapVLA** | 基准 | VLA 后门／失效注入方法与其基准 | 否 |
| **VIPS** | 基准 | 车路协同伪仿真评测 | 否 |
| **VLA-Arena** | 基准 | 分难度的 VLA 基准与榜单 | 否 |
| **VLABench** | 基准 | 语言条件长时程操作基准 | 否 |
| **Inspect** | 工具／框架 | UK AISI 的代理评测框架，ORBIT 建在其上 | 是 |
| **ROS** | 工具／框架 | 机器人中间件 | 是 |
| **Unity3D** | 工具／框架 | 游戏引擎，也用于机器人仿真前端 | 是 |
| **Apache-2.0** | 开源许可证 | 含专利授权的宽松许可 | 是 |
| **CC BY-NC-SA 4.0** | 开源许可证 | 署名—非商业—相同方式共享，商用受限 | 是 |
| **MIT** | 开源许可证 | 宽松许可，允许商用；不是麻省理工学院的缩写（本文语境） | 是 |
| **AgiBot World** | 数据集 | 真机双臂操作数据集与平台 | 否 |
| **nuScenes** | 数据集 | 多模态自动驾驶数据集 | 否 |
| **Open X-Embodiment** | 数据集 | 跨机构机器人数据集合 | 否 |
| **RoboMIND** | 数据集 | 多本体真实操作数据集 | 否 |
| **YAM** | 机器人本体 | I2RT YAM 双臂机器人，RoboHarm 的真机与 MuJoCo 孪生都用它 | 是 |
| **Anthropic** | 机构 | Claude 系列 | 是 |
| **Google DeepMind** | 机构 | RT-X、Gemini 等 | 是 |
| **Hugging Face** | 机构 | 模型与数据集托管平台，也发布 SmolVLA | 是 |
| **ModelScope** | 机构 | 阿里系模型与数据托管平台 | 是 |
| **NEDO** | 机构 | 日本新能源产业技术综合开发机构，Peg-in-Bench 的资助方 | 是 |
| **NVIDIA** | 机构 | GR00T、Isaac 的研发方 | 是 |
| **OpenAI** | 机构 | GPT 系列 | 是 |
| **Physical Intelligence** | 机构 | π0／π0.5 的研发方 | 是 |

词表里没有的名字，说明它不属于本库讨论的通用概念，按原文理解即可。
