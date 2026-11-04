# RoboCasa365

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：在平台上建立扩展任务数据和多任务／持续学习协议。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：大规模日常任务训练与评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 0、使用 1；方法参考另标）
> **证据级别**：原表 C；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robocasa.ai/](https://robocasa.ai/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 大规模日常操作与持续学习 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 |
| 基础平台线索 | RoboCasa、RoboCasa365 |
| 规模线索 | 365 任务、2,500 厨房，约 600 小时人类数据与 1,600 小时合成数据；65 原子任务、300 复合任务。目标评测分原子、已见复合和未见复合。 |
| 执行环境线索 | 大规模日常操作与持续学习 |
| 来源审计 | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)；external_original_paper |
| 来源核验依据 | RoboCasa-Shift 论文明确说明其 benchmark built on RoboCasa365；原始 RoboCasa365 论文不在当前 192 条本库记录中。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7133954504)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 8 个缩写／技术词，并标出 9 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：扩大任务、场景和示范后，策略能否掌握复合任务、迁移未见组合并持续学习？

**评测层级**：大规模日常操作与持续学习。

## 2. 怎么构建的

**核心场景与条目**：365 任务、2,500 厨房，约 600 小时人类数据与 1,600 小时合成数据；65 原子任务、300 复合任务。目标评测分原子、已见复合和未见复合。

**实现与判分**：分别设置多任务训练、预训练后微调、四阶段终身学习；严格区分预训练与目标示范，按示范量、任务组合和场景划分比较。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026 | 使用 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 | 针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：终身学习实验中，原子任务成功率从第一阶段 41.5% 降至第四阶段 10.6%，展示持续学习中的明显遗忘；提供开放模型和不同数据量协议。

**适用边界**：365 个任务不全都属于同一个测试拆分；上述退化来自指定训练流程，不代表所有持续学习算法。大规模合成训练收益也不能直接当安全改进。

## 5. 相关论文（均来自本调研表）

- [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

365 个任务不全都属于同一个测试拆分；上述退化来自指定训练流程，不代表所有持续学习算法。大规模合成训练收益也不能直接当安全改进。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, et al., ‘RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots,’ arXiv preprint, 2026, arXiv:2603.04356v1. [论文](https://arxiv.org/abs/2603.04356)；[核查正文](https://arxiv.org/html/2603.04356v1)。

**重点核查位置（章节主题）**：3.3 Tasks；3.4 Datasets；4.1 Multi-task training；4.2 Foundation model training；4.3 Lifelong learning。

OpenAlex 被引次数：**[0](https://openalex.org/W7133954504)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://robocasa.ai/](https://robocasa.ai/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 32 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://robocasa.ai/](https://robocasa.ai/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://robocasa.ai/) | https://robocasa.ai/ | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://robocasa.ai/ 同时承载 RoboCasa 与 RoboCasa365；2026-10 更新说明 leaderboard 接受 agentic 提交，10-14 发布覆盖 300 个复合任务的子任务标注流水线。

**涉及领域**：大规模家庭操作训练／基准；365 个任务、多阶段终身学习协议。

**测试目的与构建方法**：分别设置多任务训练、预训练后微调、四阶段终身学习；严格区分预训练数据与目标示范，按示范量、任务组合与场景划分比较。

**测试缺陷**：365 个任务不都属于同一个测试拆分；遗忘结论来自指定训练流程，不代表所有持续学习算法；大规模合成训练的收益不能直接当安全改进。

**与具身智能安全的相关性**：弱：它是能力与规模基准；其“持续学习遗忘”结果对安全有间接含义（旧技能退化可能带来风险），但基准不测风险。

**用这个 benchmark 测了什么**：终身学习实验中原子任务成功率从第一阶段 41.5% 降至第四阶段 10.6%，显示明显遗忘；arXiv 摘要命中 ≥32 篇，多篇报告在 RoboCasa365 官方协议下的成功率（如 62.2%、62.32%）。

**本轮核查边界**：两版共用站点，未单独下载 365 数据。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **7 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Polic…（2026） | Axiom-0，对照 Paimon-0（VLA 模型） 与 Xiaomi-Robotics-1（XR-1（VLA 模型）） | 训练后评测（对照官方 leaderboard） | RoboCasa365 总体成功率（官方协议） | 62.32%，比最高公开榜单分（Paimon-0 的 58.1%）高 4.22pp，比 XR-1 高 4.92pp |
| Scale and Selection: What Makes Automatic Harness Evolution Work for V…（2026） | 把多智能体 harness 的 rollout 蒸馏回策略后的 standalone 策略 | 训练（多教师在线策略蒸馏）后评测 | RoboCasa365 官方协议 | 62.2%，比自身起点高 4.8 个百分点 |
| Fewer Tokens, Better Action: GPT-6 Astra Robot Agents（2026） | GPT-6 Astra 规划器 + 原语（tool calling） | 评测（与同一规划器的工具调用方式对比） | LIBERO-PRO、RoboTwin 2.0 与 RoboCasa365 共 700 个仿真任务实例 | 成功率 63.1% → 71.7%，LLM 调用减少 49% |
| MOST: Memory of Object States and Task Progress for Long-Horizon Mobil…（2026） | MOST，对照 Xiaomi-Robotics-1（XR-1，前 SOTA） | 训练后评测（跨基准 + 真机） | RoboCasa365、RoboCasa-Long 与真机 | 三处均优于 XR-1；摘要未给数值 |
| MM-ABC: Towards Generalist Mobile Manipulation via Seeing, Coordinatin…（2026） | MM-ABC | 评测 + 消融（在基准上做控制变量实验） | RoboCasa365 composite-seen 任务 | 把干净动作预测换成速度预测，成功率由 32.8% 降到 29.2% |
| REKI: Registering Knowledge in VLAs（2026） | REKI（2.4B VLA，只用公开数据预训练） | 预训练后评测（效率—性能前沿对比） | LIBERO-Plus、RoboTwin Clean2Rand 与 RoboCasa365 等 | 称在性能与模型规模之间建立新 Pareto 前沿；摘要未给逐项数值 |
| Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robot Ma…（2026） | Qwen-RobotManip（以 Qwen 为底座） | 评测（明确指出标准基准不够，改用 OOD 设置） | 把 RoboCasa365、LIBERO-Plus、EBench、RoboTwin-Clean2Rand／IF／XE 作为 OOD 组 | 结论是“标准基准无法反映预训练质量”，故采用 OOD 组；未给单一分数 |

**原文片段（摘要）**：

- Axiom-0: Hierarchical Self-Refinement for Vision-Language-Ac…（2026，arXiv）：> Axiom-0 achieves 62.32% overall success … exceeding the highest published leaderboard score (Paimon-0, 58.1%)
- Scale and Selection: What Makes Automatic Harness Evolution…（2026，arXiv）：> yields a standalone policy at 62.2% on RoboCasa365 under the official protocol, 4.8 points above its starting point
- Fewer Tokens, Better Action: GPT-6 Astra Robot Agents（2026，arXiv）：> Across 700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365, it raises success from 63.1% to 71.7%
- MOST: Memory of Object States and Task Progress for Long-Hor…（2026，arXiv）：> Across RoboCasa365, RoboCasa-Long, and real-world robot experiments, MOST consistently outperforms XR-1
- MM-ABC: Towards Generalist Mobile Manipulation via Seeing, C…（2026，arXiv）：> replacing clean-action prediction with velocity prediction lowers success on RoboCasa365 composite-seen tasks from 32.8% to 29.2%
- REKI: Registering Knowledge in VLAs（2026，arXiv）：> sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365…
- Qwen-RobotManip Technical Report: Alignment Unlocks Scale fo…（2026，arXiv）：> standard benchmarks fail to capture pretraining quality and instead adopt OOD settings including RoboCasa365

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 8 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **rollout** | rollout | 展开／推演 | 用当前策略跑一次得到的完整轨迹，常与 episode 混用。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **leaderboard** | leaderboard | 排行榜 | 公开提交与排名的榜单，反映社区参与度，不等于论文引用。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **ABC→D** | train on A/B/C, test on D | 三环境训练、第四环境测试 | CALVIN 的经典协议：用三个环境训练，在没见过的第四个环境评测。 |
| **ablation** | ablation study | 消融实验 | 逐个去掉或替换模块，看性能变化，用来归因。 |
| **OOD** | Out-of-Distribution | 分布外 | 测试数据与训练分布不同，用来检验泛化。 |

**本文最容易读错的地方**：
- **rollout**：rollout 数、episode 数、候选轨迹数三者混用。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboCasa365 | 基准 | RoboCasa 的 365 任务版本 |
| RoboCasa | 基准 | 家庭场景大规模仿真基准 |
| RoboCasa-Shift | 基准 | 长时程操作阶段鲁棒性 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |
| LIBERO-Plus | 基准 | LIBERO 的扰动扩展 |

另有 3 个专有名称已在正文首次出现处加括号标注类别（例如 Paimon-0（VLA 模型）、XR-1（VLA 模型）、GPT-6（LLM 模型）），不再重复解释。

<!-- glossary:end -->
