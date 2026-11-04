# RoboCasa

<!-- survey-classification:start -->
> **统一调研分类**：仿真平台；具身研究底座；目标：能力。
> **分类依据**：主要提供大规模交互厨房、资产和数据生成；同时有配套任务评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（日常场景规模化）  
> **分类**：VLA 能力  
> **关联论文**：本表 4 篇（提出 1、使用 3；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robocasa.ai/](https://robocasa.ai/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 日常操作仿真平台 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 以 robosuite／MuJoCo 和大量厨房、物体资产构建交互场景，结合人类示范与自动数据生成，系统变化场景、对象和任务组合。 |
| 基础平台线索 | RoboCasa、RoboCasa365 |
| 规模线索 | 原版 100 个厨房任务，包括 25 个原子、75 个复合任务；八类基本技能覆盖抓放、开关门／抽屉、操纵开关、插入和导航等。 |
| 执行环境线索 | 日常操作仿真平台 |
| OpenAlex 引用快照 | [4](https://openalex.org/W4399424845)；2026-11-04 |
| 来源审计 | [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)；same_paper_in_registry |
| 来源核验依据 | 2026-11-03 复核原始论文标题与方法章节：§3–4；与 RoboCasa-Shift / RoboCasa365 分开 |
| 术语说明 | 第 10 节解释本文出现的 12 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何用多样厨房场景和复合任务训练、评估通用机器人？

**评测层级**：日常操作仿真平台。

## 2. 怎么构建的

**核心场景与条目**：原版 100 个厨房任务，包括 25 个原子、75 个复合任务；八类基本技能覆盖抓放、开关门／抽屉、操纵开关、插入和导航等。

**实现与判分**：以 robosuite／MuJoCo 和大量厨房、物体资产构建交互场景，结合人类示范与自动数据生成，系统变化场景、对象和任务组合。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026 | 使用 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 | 针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。 |
| [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024) | 2026 | 使用 | 视觉表示 × 集成机制 × 特征组合的受控对比；鲁棒性 | WAM 从预训练视频生成模型继承强先验，但其 VAE 表示是为视觉重建而非操作优化；外部视觉表示能提升操作，但既有方法把表示选择与集成机制绑在一起，掩盖了各自的作用。作者在受控设置下系统比较视觉表示、五种集成机制与特征组合，结论包括：强通用视觉表示带来更广的鲁棒性收益，能匹配甚至超过为特定视觉能力预训练的表示；通道级联合预测效果最好。 |
| [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523) | 2024 | 提出 | 大规模日常场景（以厨房为主）、数千场景与大量演示数据 | 主张用高保真物理仿真来扩展机器人的环境、任务与数据规模，提供以厨房为主的大量日常场景与数千条演示，用于训练与评测通用操作策略。它把评测从「少数桌面任务」推向「日常环境中的大规模任务」，是长时程、多任务 VLA 评测的重要底座（RoboCasa365、RoboCasa-Shift 等即建立在其上）。 |
| [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773) | 2026 | 使用 | 信号时序逻辑（STL）不变式 + 定量鲁棒性；安全率、成功但不安全率 | 指出二元成功率会掩盖轨迹上的安全违规：策略可能到达目标，却施加过度接触、扰动旁观物体、使手中物体失稳或进入机器人自碰撞。SafeVLA-Bench 是一个「事后」安全评估框架，可直接套在现有基于仿真的 VLA 基准上，把任务相关的安全要求编码为信号时序逻辑（STL）不变式并给出定量鲁棒性语义；除原生成功率外，还报告安全率与「成功但不安全」率。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文比较场景／任务多样性及合成示范的训练作用，并给出向真机迁移的实验。核心贡献是统一日常环境、复合任务和可扩展数据生成。

**适用边界**：原论文为 arXiv:2406.02523；不能用后续 RoboCasa-Shift 或 RoboCasa365 取代其来源，也不能把 365 版的任务和厨房规模写成原始版本。

## 5. 相关论文（均来自本调研表）

- [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2026；使用）
- [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024)（2026；使用）
- [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)（2024；提出）
- [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

原论文为 arXiv:2406.02523；不能用后续 RoboCasa-Shift 或 RoboCasa365 取代其来源，也不能把 365 版的任务和厨房规模写成原始版本。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, et al., ‘RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots,’ arXiv preprint, 2024, arXiv:2406.02523v1. [论文](https://arxiv.org/abs/2406.02523)；[核查正文](https://arxiv.org/html/2406.02523v1)。

**重点核查位置（章节主题）**：III Environment；IV Tasks and Datasets；V Experiments。

OpenAlex 被引次数：**[4](https://openalex.org/W4399424845)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://robocasa.ai/](https://robocasa.ai/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 3 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **4** 篇引文论文（清单保留被引最高的 4 篇）；arXiv 摘要命中 49 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://robocasa.ai/](https://robocasa.ai/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://robocasa.ai/) | https://robocasa.ai/ | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://robocasa.ai/ 汇总 Paper（RoboCasa 与 RoboCasa365）、Code、Documentation、Leaderboard 与 Updates，近期更新包括 leaderboard 接受 agentic 提交、发布 300 个复合任务的逐帧子任务标注。

**涉及领域**：大规模家庭场景仿真与日常任务训练／评测；robosuite／MuJoCo 厨房环境。

**测试目的与构建方法**：以 robosuite／MuJoCo 与大量厨房、物体资产构建交互场景，结合人类示范与自动数据生成，系统变化场景、对象与任务组合；发布复合任务与示范数据集。

**测试缺陷**：原论文为 arXiv:2406.02523，不能用后续 RoboCasa-Shift 或 RoboCasa365 取代其来源，也不能把 365 版的厨房与任务规模写成原始版本；仿真资产与真实厨房仍有差距。

**与具身智能安全的相关性**：弱到中等：厨房是典型危险场景（火、刀、热表面），但基准指标是任务成功；其价值是提供可控场景，便于叠加安全约束。

**用这个 benchmark 测了什么**：论文比较场景／任务多样性与合成示范的训练作用，并给出向真机迁移的实验；下游 BOSS 用它研究长时程观察空间偏移，SeeTraceAct 用它做可见性感知规划，另发布 RoboCasa-DC 跨本体示范扩展。

**本轮核查边界**：项目页为 RoboCasa／RoboCasa365 共用，未逐项区分两版资源。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Z-1: Efficient Reinforcement Learning for Vision-Language-Action（2026） | Z-1（基于 π0.5，先 SFT 再逐任务 GRPO） | 微调（用公开示范做 SFT）+ 强化学习后评测 | 只用 RoboCasa 公开示范做 SFT，然后在 24 个标准 RoboCasa 任务上做 task-wise GRPO | 摘要强调效率与 24 任务覆盖，未给具体成功率 |
| LY-GWM-RoboCasa-Human300: Prediction-Guided Action Selection（2026） | GR00T-N1.5（在 Human300 上微调）+ 图动力学模型 + 状态奖励打分器 | 微调（Human300 示范）+ 推理期选择 | RoboCasa 环境中的动作生成与候选选择 | 摘要只说明组件与流程，未给数值 |
| SeeTraceAct: Visibility-Aware Latent Planning from Cross-Embodiment De…（2026） | SeeTraceAct（可见性感知隐规划） | 扩展基准（发布 RoboCasa-DC）+ 评测 | 把机器人轨迹与新增人类示教配对，形成 demo-conditioned 扩展 RoboCasa-DC | 产出 RoboCasa-DC 数据扩展，不是基准分数 |
| AffordanceWAM: Affordance-Aware Joint World-Action Modeling（2026） | AffordanceWAM（可供性感知联合世界—动作模型） | 训练后评测（跨基准 + 真机） | RoboCasa、CALVIN ABC→D 与真实操作 | 称相比只用 RGB 或只用机器人数据的基线一致更优 |
| MOST: Memory of Object States and Task Progress for Long-Horizon Mobil…（2026） | MOST（物体状态与任务进度记忆） | 扩展基准（提出 RoboCasa-Long）+ 评测 | 多分钟、多阶段的移动操作任务 | 产出 RoboCasa-Long 基准，不是原基准分数 |

**原文片段（摘要）**：

- Z-1: Efficient Reinforcement Learning for Vision-Language-Ac…（2026，arXiv）：> Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise GRPO strategy across 24 standard RoboCasa tasks
- LY-GWM-RoboCasa-Human300: Prediction-Guided Action Selection（2026，arXiv）：> a Human300-fine-tuned GR00T-N1.5 action generator, an action-conditioned graph dynamics model, and a learned binary state-reward scorer
- SeeTraceAct: Visibility-Aware Latent Planning from Cross-Emb…（2026，arXiv）：> we introduce and release RoboCasa-DC, a demo-conditioned extension of RoboCasa
- AffordanceWAM: Affordance-Aware Joint World-Action Modeling（2026，arXiv）：> Experiments on RoboCasa, CALVIN ABC→D, and real-world manipulation demonstrate consistent gains
- MOST: Memory of Object States and Task Progress for Long-Hor…（2026，arXiv）：> We further introduce RoboCasa-Long, a benchmark of multi-minute, multi-stage mobile manipulation tasks

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 12 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **rollout** | rollout | 展开／推演 | 用当前策略跑一次得到的完整轨迹，常与 episode 混用。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **WAM** | World-Action Model | 世界—动作模型 | 同时预测未来画面与动作的模型，用于规划或作为策略主干。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **SFT** | Supervised Fine-Tuning | 监督微调 | 用示范数据做有监督训练，把通用模型变成任务模型。 |
| **GRPO** | Group Relative Policy Optimization | 组相对策略优化 | 一种不需要价值网络的强化学习算法，按组内相对优势更新策略。 |
| **GR00T** | NVIDIA GR00T N1 / N1.5 | GR00T 机器人基础模型 | NVIDIA 的类人／通用操作基础模型家族，常作为强基线或微调起点。 |
| **leaderboard** | leaderboard | 排行榜 | 公开提交与排名的榜单，反映社区参与度，不等于论文引用。 |
| **ABC→D** | train on A/B/C, test on D | 三环境训练、第四环境测试 | CALVIN 的经典协议：用三个环境训练，在没见过的第四个环境评测。 |
| **robosuite** | robosuite | robosuite 操作仿真库 | 基于 MuJoCo 的机械臂操作环境库，LIBERO、RoboCasa 都建在上面。 |
| **MuJoCo** | MuJoCo | MuJoCo 物理引擎 | 经典的高效刚体物理引擎，robosuite、LIBERO 的底层。 |
| **RGB** | RGB image observation | 彩色图像观测 | 只用普通彩色相机画面作为输入，不含深度、触觉或本体状态。 |

**本文最容易读错的地方**：
- **rollout**：rollout 数、episode 数、候选轨迹数三者混用。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboCasa | 基准 | 家庭场景大规模仿真基准 |
| RoboCasa365 | 基准 | RoboCasa 的 365 任务版本 |
| RoboCasa-Shift | 基准 | 长时程操作阶段鲁棒性 |
| CALVIN | 基准 | 语言条件长时程操作基准 |

<!-- glossary:end -->
