# SimplerEnv

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：主要为真机策略设计可验证的仿真代理评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（评测基础设施）  
> **分类**：VLA 能力  
> **关联论文**：本表 3 篇（提出 1、使用 2；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://simpler-env.github.io/](https://simpler-env.github.io/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Evaluating Real-World Robot Manipulation Policies in Simulation |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 真机策略的仿真代理评测 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 仿真-真机对齐；控制与视觉差异消解；与真机成功率的相关性 |
| 基础平台线索 | LIBERO、SimplerEnv |
| 规模线索 | Google Robot 与 WidowX BridgeV2 设置下的罐子、移动物体、抽屉等刚体操作；重点是模拟与真实的配对测试。 |
| 执行环境线索 | 真机策略的仿真代理评测 |
| OpenAlex 引用快照 | [4](https://openalex.org/W4396822572)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 9 个缩写／技术词，并标出 7 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：不反复占用真实机器人，能否用模拟可靠预测实机策略的相对表现？

**评测层级**：真机策略的仿真代理评测。

## 2. 怎么构建的

**核心场景与条目**：Google Robot 与 WidowX BridgeV2 设置下的罐子、移动物体、抽屉等刚体操作；重点是模拟与真实的配对测试。

**实现与判分**：以 SAPIEN 搭建环境，缩小控制与视觉差距；Visual Matching 匹配真实画面，Variant Aggregation 汇总环境变体，报告排序违背 MMRV 和 Pearson 相关。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802) | 2026 | 使用 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 | 指出刚体基准中的任务成功并不能说明模型是否保全了物体。ManiPhysicsZoo 汇总文献支撑的材质属性、3D 网格与参考文献形成可复用物体资产，再由基于求解器的评估依据几何、材质与抓取条件计算损伤阈值并与实测接触力比较，从而在 LIBERO 与 SimplerEnv 上区分「完成任务」与「安全完成任务」，公开 VLA 检查点在两者间存在显著差距。 |
| [Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)](https://arxiv.org/abs/2405.05941) | 2024 | 提出 | 仿真-真机对齐；控制与视觉差异消解；与真机成功率的相关性 | 直面「真机评测不可扩展且难复现」的问题：指出控制差异与视觉差异是仿真评测不可靠的两个关键来源，并提出无需构建全保真数字孪生的缓解手段，使仿真评测结果与真机表现对齐。该工作为 VLA 提供了一条低成本、可复现的能力评测路径，也是后续大量 VLA 论文采用的仿真评测协议来源。 |
| [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245) | 2026 | 使用 | 时空关系与人类意图推理；社会合规导航 | 指出机器人在动态、以人为中心的环境中导航需要基于稳健场景理解的社会合规决策；近期 VLM 展现出物体识别、常识推理与情境理解等能力，看似契合社会导航的需求，但 VLM 能否准确理解复杂的社会导航场景（例如推断智能体之间的时空关系与人的意图）仍不清楚——而这正是安全且社会合规导航的前提。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：Google Robot 六个 checkpoint 的任务平均 Pearson r：验证 MSE 为 0.308，VarAgg 为 0.778，VisMatch 为 0.924；VisMatch 的 MMRV 为 0.056。

**适用边界**：相关性证明的是所测任务／策略上的相对预测价值，不是任意物体动力学或绝对成功率的等价性。原论文以刚体、已知真实设置为主。

## 5. 相关论文（均来自本调研表）

- [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)（2026；使用）
- [Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)](https://arxiv.org/abs/2405.05941)（2024；提出）
- [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

相关性证明的是所测任务／策略上的相对预测价值，不是任意物体动力学或绝对成功率的等价性。原论文以刚体、已知真实设置为主。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Xuanlin Li, Kyle Hsu, Jiayuan Gu, et al., ‘Evaluating Real-World Robot Manipulation Policies in Simulation,’ arXiv preprint, 2024, arXiv:2405.05941v1. [论文](https://arxiv.org/abs/2405.05941)；[核查正文](https://arxiv.org/html/2405.05941v1)。

**重点核查位置（章节主题）**：III-B Metrics；IV Control and Visual Gaps；V SIMPLER；VI-B Correlations。

OpenAlex 被引次数：**[4](https://openalex.org/W4396822572)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://simpler-env.github.io/](https://simpler-env.github.io/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 2 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **4** 篇引文论文（清单保留被引最高的 4 篇）；arXiv 摘要命中 50 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://simpler-env.github.io/](https://simpler-env.github.io/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://simpler-env.github.io/) | https://simpler-env.github.io/ | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://simpler-env.github.io/ 给 Paper／Video／Code／CoLab 入口，作者来自 UCSD、Stanford、Berkeley、Google DeepMind（机构）。

**涉及领域**：真实机器人策略的仿真评测；SAPIEN 中复现 WidowX 与 Google Robot 的真实设置。

**测试目的与构建方法**：以 SAPIEN 搭建环境、缩小控制与视觉差距；用 Visual Matching 匹配真实画面、Variant Aggregation 汇总环境变体，报告排序违背 MMRV 与 Pearson 相关。

**测试缺陷**：相关性证明的是“所测任务／策略上的相对预测价值”，不是任意物体动力学或绝对成功率的等价性；原论文以刚体、已知真实设置为主；视觉匹配依赖人工调参。

**与具身智能安全的相关性**：弱：本身是能力评测，价值在于提供“廉价代理指标”；若用于安全评测，须先证明相关性在风险场景下仍成立。

**用这个 benchmark 测了什么**：Google Robot 六个 checkpoint 的任务平均 Pearson r：验证 MSE 0.308、VarAgg 0.778、VisMatch 0.924（MMRV 0.056）——说明评测协议设计本身决定相关性；下游 PhysBrain、CronusVLA 等报告在 SimplerEnv-WidowX 上的结果。

**本轮核查边界**：只读项目页，未运行仿真。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding（2025） | Discrete Diffusion VLA | 评测（分 SimplerEnv 的两个子集报告） | SimplerEnv-Fractal 的 visual matching 与 SimplerEnv-Bridge 总体 | SimplerEnv-Fractal 71.2%、SimplerEnv-Bridge 54.2%；LIBERO 平均 96.4% |
| DeFI: Disentangled Robot Learning via Separate Forward and Inverse Dyn…（2026） | DeFI | 评测（CALVIN + SimplerEnv 并列） | CALVIN ABC-D 平均任务长度；SimplerEnv-Fractal 成功率 | CALVIN 平均长度 4.51；SimplerEnv-Fractal 51.2% |
| CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame（2025） | CronusVLA | 派生扰动基准（SimplerEnv-OR）+ 评测 | 24 类观察扰动 × 120 个严重度等级 | 产出新扰动基准 SimplerEnv-OR；用于测时间与空间扰动下的鲁棒性 |
| PhysBrain 1.0 Technical Report（2026） | PhysBrain 1.0 | 评测（多基准 SOTA 对比） | ERQA、PhysBench、SimplerEnv-WidowX、LIBERO、RoboCasa | 称在多模态问答与具身控制基准上取得 SOTA，域外表现尤其强 |
| TTF-VLA: Temporal Token Fusion via Pixel-Attention Integration（2025） | TTF-VLA | 评测（逐基准报告均值） | LIBERO 与 SimplerEnv，另加真机任务 | LIBERO 平均 +4.0 个百分点（72.4% vs 基线 68.4%），SimplerEnv 做跨环境验证 |

**原文片段（摘要）**：

- Discrete Diffusion VLA: Bringing Discrete Diffusion to Actio…（2025，arXiv）：> 71.2% visual matching on SimplerEnv-Fractal, and 54.2% overall on SimplerEnv-Bridge
- DeFI: Disentangled Robot Learning via Separate Forward and I…（2026，arXiv）：> DeFI achieving an average task length of 4.51 for CALVIN, 51.2% success rate on SimplerEnv-Fractal
- CronusVLA: Towards Efficient and Robust Manipulation via Mul…（2025，arXiv）：> we introduce SimplerEnv-OR, a novel benchmark featuring 24 types of observational disturbances and 120 severity levels
- PhysBrain 1.0 Technical Report（2026，arXiv）：> including ERQA, PhysBench, SimplerEnv-WidowX, LIBERO, and RoboCasa, PhysBrain 1.0 achieves SOTA results
- TTF-VLA: Temporal Token Fusion via Pixel-Attention Integrati…（2025，arXiv）：> 4.0 percentage points average on LIBERO (72.4% vs 68.4% baseline), cross-environment validation on SimplerEnv

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 9 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **Pearson** | Pearson correlation coefficient | 皮尔逊相关系数 | 衡量两组数线性相关强度的指标，取值 −1 到 1。 |
| **MMRV** | Mean Maximum Rank Violation | 平均最大排名违背 | 衡量仿真分数与真机分数的排序不一致程度，越低越好。 |
| **MSE** | Mean Squared Error | 均方误差 | 预测值与真值差的平方的平均，用于回归与世界模型预测。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **digital twin** | digital twin | 数字孪生 | 按真实场景生成的可交互三维副本，用于批量造数据与评测。 |
| **ABC→D** | train on A/B/C, test on D | 三环境训练、第四环境测试 | CALVIN 的经典协议：用三个环境训练，在没见过的第四个环境评测。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **SAPIEN** | SAPIEN | SAPIEN 仿真引擎 | 面向铰接物体操作的物理仿真引擎，ManiSkill、SimplerEnv 的底座。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| SimplerEnv | 基准 | 真实策略的仿真代理评测 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| ManiPhysicsBench | 基准 | 物体保全物理评估基准 |
| STARS | 基准 | 表征学习方法；并非新 benchmark |
| CALVIN | 基准 | 语言条件长时程操作基准 |
| RoboCasa | 基准 | 家庭场景大规模仿真基准 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 Google DeepMind（机构）），不再重复解释。

<!-- glossary:end -->
