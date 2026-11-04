# LIBERO-Safety

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：安全约束和分套件任务定义是主要产出。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：物理与语义安全；五类套件 × L0-L2 难度  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://libero-safety.github.io](https://libero-safety.github.io)
>
> 具体的任务条目、UBDDL 参数、CuRobo 轨迹生成和运行接口见：[LIBERO-Safety：实现拆解与任务条目](../analysis/LIBERO-Safety-实现拆解.md)。

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 仿真 VLA 物理与语义安全 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 |
| 基础平台线索 | LIBERO |
| 规模线索 | AAG、HRI、TSA、FSHOA、SSR 五套任务，每套 5 个任务、3 档难度，共 75 个测试配置；另有 40 个训练任务和 19,664 条无碰撞示范。 |
| 执行环境线索 | 仿真 VLA 物理与语义安全 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7165682249)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 10 个缩写／技术词，并标出 3 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：传统 LIBERO 成功标准遗漏哪些物理与语义风险，如何将风险变成逐步可检查的任务约束？

**评测层级**：仿真 VLA 物理与语义安全。

## 2. 怎么构建的

**核心场景与条目**：AAG、HRI、TSA、FSHOA、SSR 五套任务，每套 5 个任务、3 档难度，共 75 个测试配置；另有 40 个训练任务和 19,664 条无碰撞示范。

**实现与判分**：用 UBDDL 扩展 BDDL 的随机化、动态交互和逐步安全检查；关键姿态与 CuRobo 用于示范生成。除终点成功，还记录碰撞和场景风险。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686) | 2026 | 提出 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 | 提出 LIBERO-Safety，面向 VLA 的物理与语义安全进行统一评测。基准包含 affordance-aware grasping、human-robot interaction、tabletop spatial avoidance、free-space hand-object avoidance 与 semantic safety reasoning 五类套件，每类含 L0–L2 三档难度；通过 keypose-driven pipeline 生成 19,664 条严格无碰撞示范，并同时报告物理安全、语义安全和环境随机性下的鲁棒性。官方项目页注明已被 ECCV（会议／期刊） 2026 接收。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：表 3 中 OpenVLA-OFT 在 AAG 的 L0／L1／L2 成功率为 50.0%／79.3%／1.3%，说明训练分布和风险形态会造成非单调表现。成果为可复用的安全任务描述与评测扩展。

**适用边界**：不能把 L1 的高成功率解释为安全性全面更好；须同时看安全指标。部分数据生成组件的公开状态仍以仓库实现审计为准，论文描述不等于全部代码已可运行。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

不能把 L1 的高成功率解释为安全性全面更好；须同时看安全指标。部分数据生成组件的公开状态仍以仓库实现审计为准，论文描述不等于全部代码已可运行。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Rongxu Cui, Zongzheng Zhang, Jingrui Pang, et al., ‘LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2606.23686v2. [论文](https://arxiv.org/abs/2606.23686)；[核查正文](https://arxiv.org/html/2606.23686v2)。

**重点核查位置（章节主题）**：3.1 Benchmark Design；3.2 Data Generation；4.2 Main Results；4.3 Analysis。

OpenAlex 被引次数：**[0](https://openalex.org/W7165682249)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://libero-safety.github.io](https://libero-safety.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 2 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。

本仓库另有[LIBERO-Safety 实现拆解](../analysis/LIBERO-Safety-实现拆解.md)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://libero-safety.github.io](https://libero-safety.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://libero-safety.github.io) | https://libero-safety.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://libero-safety.github.io 给出完整作者单位（清华 AIR、BAAI 等）与论文信息；实现细节见本库另一份拆解笔记。

**涉及领域**：VLA 的物理与语义安全；基于 LIBERO 生态的家庭操作任务，带渐进安全检查。

**测试目的与构建方法**：用 UBDDL 扩展 BDDL 的随机化、动态交互与逐步安全检查，关键姿态与 CuRobo 用于示范生成；除终点成功外还记录碰撞与场景风险，分 L0／L1／L2 风险形态。

**测试缺陷**：不能把 L1 高成功率解释为“更安全”，必须同时看安全指标；部分数据生成组件的公开状态需以仓库实现审计为准；风险定义仍由人工规则给出。

**与具身智能安全的相关性**：直接：把安全检查嵌进 LIBERO 的执行流程，能量化“成功但违规”。它是本库中最容易与现有 VLA 生态复用的安全评测之一。

**用这个 benchmark 测了什么**：表 3 中 OpenVLA-OFT 在 AAG 的 L0／L1／L2 成功率为 50.0%／79.3%／1.3%，显示训练分布与风险形态造成非单调表现；下游 FabriVLA 用它按风险给 rollout 排序，VLA-ULAP 在 latency-aware 版本上报告 +11.0／+15.5pp。

**本轮核查边界**：项目页为介绍页，代码与数据仓库未在本轮直接核实。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **2 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| FabriVLA: A Lightweight Vision-Language-Action Model with Conformal Ac…（2026） | FabriVLA（轻量 VLA + 保形预测） | 评测并叠加方法（用基准做风险排序） | LIBERO-Safety rollout，用保形区间在执行前给轨迹排风险 | 摘要只说明“可按风险排序 rollout、支持风险排序复核”，未给成功率数值 |
| VLA-ULAP: Interleaving Cloud VLA Calls with Ultra-Lightweight Local Ac…（2026） | VLA-ULAP（云端 VLA + 本地轻量动作预测），对照 π0.5 | 评测（时延感知场景） | latency-aware LIBERO-Safety 仿真中的两个任务 | 成功率比 π0.5 高 11.0 与 15.5 个百分点，同时把 VLA 调用次数减半 |

**原文片段（摘要）**：

- FabriVLA: A Lightweight Vision-Language-Action Model with Co…（2026，arXiv）：> On LIBERO-Safety, these bounds rank rollouts by risk before execution
- VLA-ULAP: Interleaving Cloud VLA Calls with Ultra-Lightweigh…（2026，arXiv）：> exceed π0.5's success rate by 11.0 and 15.5 pp on two tasks in latency-aware LIBERO-Safety simulation

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 10 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **rollout** | rollout | 展开／推演 | 用当前策略跑一次得到的完整轨迹，常与 episode 混用。 |
| **pp** | percentage point | 百分点 | 两个百分比相减的单位；30%→38% 是 +8pp，不是 +8%。 |
| **SSR** | Safe Success Rate | 安全成功率 | 既完成任务又没违规的 episode ÷ 全部 episode。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **OpenVLA** | OpenVLA（含 OpenVLA-oft 变体） | OpenVLA 开源策略 | 开源的 7B VLA 基线，安全基准里最常被拿来测“干净能力 vs 安全”的模型之一。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 基准自定义的难度阶梯：常见是 L0 干净、L1 加扰动、L2 更强扰动或结构变化，L3 更难。 |
| **HRI** | Human-Robot Interaction | 人机交互 | 研究人与机器人如何协作、沟通与共处的方向。 |
| **UBDDL** | Unified BDDL（本库 LIBERO-Safety 口径） | 扩展版 BDDL | 在 BDDL 上加入随机化、动态交互与逐步安全检查的扩展。 |
| **BDDL** | Behavior Domain Definition Language | 行为域定义语言 | 用符号逻辑描述任务初态、目标与物体关系的任务定义语言。 |

**本文最容易读错的地方**：
- **rollout**：rollout 数、episode 数、候选轨迹数三者混用。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| LIBERO-Safety | 基准 | LIBERO 的安全扩展 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 ECCV（会议／期刊）），不再重复解释。

<!-- glossary:end -->
