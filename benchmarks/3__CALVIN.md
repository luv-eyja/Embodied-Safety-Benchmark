# CALVIN

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：核心是语言条件组合及环境划分协议。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：认知 + 规划（长时程语言遵循）  
> **分类**：VLA 能力  
> **关联论文**：本表 4 篇（提出 1、使用 3；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://calvin-robot.github.io/](https://calvin-robot.github.io/)；[https://github.com/mees/calvin](https://github.com/mees/calvin)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks |
| 年份 | 2021（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 语言条件长时程操作 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | 34 个任务、1000+ 条长时程指令链；连续指令平均完成长度 |
| 基础平台线索 | CALVIN |
| 规模线索 | 4 个桌面环境、34 类操作，涉及抽屉、滑门、按钮、灯和积木；核心评估是连续完成指令链。 |
| 执行环境线索 | 语言条件长时程操作 |
| OpenAlex 引用快照 | [189](https://openalex.org/W4226073959)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 8 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：从非结构化 play 数据学习后，机器人能否按自然语言连续完成多步组合任务并迁移环境？

**评测层级**：语言条件长时程操作。

## 2. 怎么构建的

**核心场景与条目**：4 个桌面环境、34 类操作，涉及抽屉、滑门、按钮、灯和积木；核心评估是连续完成指令链。

**实现与判分**：收集多模态 play 与语言标注，用状态变化判定单任务完成；区分单环境、多环境和训练三环境／测试第四环境，报告链长各级成功率与平均完成长度。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models](https://arxiv.org/abs/2609.39971) | 2026 | 使用 | 反事实指令下的行为切换；指令-动作绑定（instruction-action binding） | 指出聚合鲁棒性分数会掩盖一种特定失败：策略同时响应语言与视觉，却不把两者结合来选择任务需要的动作——指令只是唤起熟悉的轨迹族，视觉反馈只调整其执行。行为分析显示失败回合常保留原任务行为或切换到另一已示范任务（说明语言并未被简单忽略），并通过读出与干预把这种选择关联到任务条件的内部状态。 |
| [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2609.18084) | 2026 | 使用 | 区域隔离微调的归一化参数位移（适配代价谱） | 检验「每个网络区域都需要同等适配」这一隐含假设：用区域隔离微调下的归一化参数位移度量各区适配代价，在 5 个架构各异的 VLA 上发现一致的适配谱——外观偏移的代价集中在视觉编码器、指令偏移在语言主干、新物体偏移同时落在视觉编码器与动作头。据此提出「观察—诊断—分配—适配」流水线，把有限适配容量分配到真正需要的区域。 |
| [Retrieval-triggered Action Projection Adjustment for Frozen VLA Policies: An Empirical Study and Failure Analysis](https://arxiv.org/abs/2610.24573) | 2026 | 使用 | 近碰撞/停滞代理事件率、任务成功数；独立复现队列 | 为无法从历史失败中学习的冻结 VLA 设计「检索触发投影修正」（RTPC）：检索压力采集的局部深度记录，只施加平移投影修正、保持旋转与夹爪指令不变，形成可审计的外部记忆包装器。结果值得注意：主实验中代理事件率下降但任务成功数不变，且该下降在独立复现队列中未能重现，检索到的修正方向与随机基线不可区分——一个带有方法学价值的负结果。 |
| [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227) | 2022 | 提出 | 34 个任务、1000+ 条长时程指令链；连续指令平均完成长度 | 语言条件长时程操作的代表性基准：在仿真桌面环境中定义 34 个操作任务，并把它们串联成上千条由语言指令逐步给出的长时程序列，度量策略在连续指令下平均能正确完成多少步。其「指令链」设计使长时程语言遵循成为可量化指标，是 VLA 通用能力评测的经典基线之一。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：原论文以 MCIL 等基线表明，训练场景中的单任务表现不能代表未见环境和连续指令组合表现。主要成果是长期指令协议、多传感器数据和环境划分。

**适用边界**：现代论文的 ABC→D 协议、数据量、历史窗口和模型与原始基线不同，引用原论文不能据此报告当前榜首；该基准主要测能力而非显式危险约束。

## 5. 相关论文（均来自本调研表）

- [When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models](https://arxiv.org/abs/2609.39971)（2026；使用）
- [Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models](https://arxiv.org/abs/2609.18084)（2026；使用）
- [Retrieval-triggered Action Projection Adjustment for Frozen VLA Policies: An Empirical Study and Failure Analysis](https://arxiv.org/abs/2610.24573)（2026；使用）
- [CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)（2022；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

现代论文的 ABC→D 协议、数据量、历史窗口和模型与原始基线不同，引用原论文不能据此报告当前榜首；该基准主要测能力而非显式危险约束。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Oier Mees, Lukas Hermann, Erick Rosete-Beas, et al., ‘CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks,’ arXiv preprint, 2021, arXiv:2112.03227v4. [论文](https://arxiv.org/abs/2112.03227)；[核查正文](https://arxiv.org/html/2112.03227v4)。

**重点核查位置（章节主题）**：III-A Environment；III-C The CALVIN Challenge；V Experiments。

OpenAlex 被引次数：**[189](https://openalex.org/W4226073959)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://calvin-robot.github.io/](https://calvin-robot.github.io/)；[https://github.com/mees/calvin](https://github.com/mees/calvin)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 3 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **188** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 49 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://calvin-robot.github.io/](https://calvin-robot.github.io/)；[https://github.com/mees/calvin](https://github.com/mees/calvin)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://calvin-robot.github.io/) | https://calvin-robot.github.io/ | 保留文本 263 字符（截断） |
| [repo](https://github.com/mees/calvin) | https://raw.githubusercontent.com/mees/calvin/HEAD/README.md | stars 1002，license MIT（开源许可证），最后推送 2025-09-08，保留文本 4200 字符（截断） |

**项目页显示**：官网 https://calvin-robot.github.io/ 已 404（GitHub Pages Site not found）；代码在 https://github.com/mees/calvin（1,002 stars，MIT，2025-09-08 最后推送），README 指向原论文并说明获得 2022 RA-L（会议／期刊） 最佳论文。

**涉及领域**：语言条件的长时程机械臂操作；桌面仿真环境，含多模态 play 数据与人类语言标注。

**测试目的与构建方法**：采集多模态示教与语言标注，按状态变化判定单任务完成；区分单环境、多环境、以及“训练三环境／测试第四环境”的 ABC→D 协议，报告不同指令链长的成功率与平均完成长度。

**测试缺陷**：现代论文的 ABC→D 协议、数据量、历史窗口与模型均与原始基线不同，引用原论文不能据此报告当前榜首；任务与场景高度固定，容易过拟合；只测能力不测显式危险约束（有 2026 年工作专门审计其奖励／数据依赖）。

**与具身智能安全的相关性**：较弱：它是能力与长期指令跟随基准；可作为安全策略的前置能力门槛，但分数本身不反映风险。

**用这个 benchmark 测了什么**：原论文用 MCIL 等基线说明单任务表现不能代表未见环境与连续指令组合；其后 188 篇引文包括 Code as Policies、Visual Language Maps、Text2Motion 等；2026 年有审计工作以 CALVIN 为案例研究“并行策略评测的基准路径保真度”。

**本轮核查边界**：官网失效，只能以代码仓库为准；未核验数据集下载。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| What Matters in Language Conditioned Robotic Imitation Learning Over U…（2022） | MCIL 系列改进（该文自己的模型） | 训练后评测（SOTA 对比） | CALVIN 的语言条件长时程任务 | 论文称显著优于当时 SOTA（摘要无具体数值） |
| Grounding Language with Visual Affordances over Unstructured Data（2023） | 该文的视觉可供性接地方法 | 训练后评测（仿真 + 真机） | CALVIN（仿真）+ 真实机器人，另学 25+ 种视觉运动技能 | 称在 CALVIN 上达到 SOTA |
| Diffusion Transformer Policy（2024） | Diffusion Transformer Policy，真机为 Franka | 训练后评测（多基准并列） | ManiSkill2、LIBERO、CALVIN、SimplerEnv 四套仿真 + 真机 | 称在四处一致优于基线（摘要无逐项数值） |
| Multi-Teacher On-Policy Distillation for Flow-Based Vision-Language-Ac…（2026） | Velocity Loss OPD（多教师在线策略蒸馏），从联合 SFT 初始化 | 训练后评测（按指令链长报告） | CALVIN 五指令序列的成功率，另报 LIBERO-40 与 Meta-World MT5 | CALVIN 五指令序列绝对提升 33.4 个百分点；LIBERO-40 +22.55%、Meta-World MT5 +22.6% |
| What Are We Actually Benchmarking in Robot Manipulation?（2026） | —（基准审计，不测模型） | 审计（把 CALVIN 当被审计对象） | 对 LIBERO、CALVIN、SimplerEnv、RoboCasa、RoboTwin 2.0 做诊断 | 指出奖励／数据来源依赖等问题，并为每种失效模式提一个诊断指标 |

**原文片段（摘要）**：

- What Matters in Language Conditioned Robotic Imitation Learn…（2022，OpenAlex 引文）：> significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation benchmark
- Grounding Language with Visual Affordances over Unstructured…（2023，OpenAlex 引文）：> achieving state-of-the-art performance on the challenging CALVIN benchmark
- Diffusion Transformer Policy（2024，arXiv）：> Extensive experiments … on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm
- Multi-Teacher On-Policy Distillation for Flow-Based Vision-L…（2026，arXiv）：> yields absolute success-rate gains of 22.55% on LIBERO-40, 33.4% on CALVIN five-instruction sequences
- What Are We Actually Benchmarking in Robot Manipulation?（2026，arXiv）：> We audit LIBERO, CALVIN, SimplerEnv, RoboCasa, and RoboTwin 2.0 under these diagnostics

**口径提示**：arXiv 摘要检索还命中《Style Transfer to Calvin and Hobbes comics》——因为出现 “Calvin” 这个名字，与基准无关，已剔除。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 6 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **SFT** | Supervised Fine-Tuning | 监督微调 | 用示范数据做有监督训练，把通用模型变成任务模型。 |
| **ABC→D** | train on A/B/C, test on D | 三环境训练、第四环境测试 | CALVIN 的经典协议：用三个环境训练，在没见过的第四个环境评测。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| CALVIN | 基准 | 语言条件长时程操作基准 |
| ManiSkill2 | 基准 | ManiSkill 的第二代 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| SimplerEnv | 基准 | 真实策略的仿真代理评测 |
| RoboCasa | 基准 | 家庭场景大规模仿真基准 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）、RA-L（会议／期刊）），不再重复解释。

<!-- glossary:end -->
