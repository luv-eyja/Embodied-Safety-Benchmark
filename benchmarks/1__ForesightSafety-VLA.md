# ForesightSafety-VLA

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性、安全。
> **分类依据**：有明确安全任务集、扰动轴和过程评分。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：感知 + 指令理解 + 动作控制（三侧安全）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/tuotuoLyu/ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 仿真 VLA 安全控制 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 13 类安全 taxonomy；累计安全代价 CC、风险暴露时间 RET、四象限分解 |
| 基础平台线索 | RoboTwin |
| 规模线索 | 基于 RoboTwin 的 66 个场景、5 种本体、13 类风险；Safe-Core、Safe-Lang、Safe-Vis 分别诊断核心风险、语言变化和视觉变化。 |
| 执行环境线索 | 仿真 VLA 安全控制 |
| 全文状态 | 已核查本地全文：`docs/_fulltext/ForesightSafety-VLA.txt` |
| OpenAlex 引用快照 | [0](https://openalex.org/W7166132482)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 12 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：VLA 能否在行动前预见后果，处理危险物、动作约束和时序前置条件，而不只完成任务？

**评测层级**：仿真 VLA 安全控制。

## 2. 怎么构建的

**核心场景与条目**：基于 RoboTwin 的 66 个场景、5 种本体、13 类风险；Safe-Core、Safe-Lang、Safe-Vis 分别诊断核心风险、语言变化和视觉变化。

**实现与判分**：用层级任务难度及语言／视觉扰动构造可控测试，结合任务完成与约束违反信号，报告 SR、CC、RET 及安全／不安全成功和失败的四象限。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079) | 2026 | 提出 | 13 类安全 taxonomy；累计安全代价 CC、风险暴露时间 RET、四象限分解 | 把安全作为首要评测目标的诊断型基准：定义覆盖物理交互安全（Safe-Core）、指令侧安全（Safe-Lang）、感知侧安全（Safe-Vis）的 13 类安全 taxonomy，并在场景结构、语言指令、视觉观测三个受控变化维度下评测，使失败来源可被诊断而非被单一总分掩盖。除二元成功率外还度量过程级风险——累计安全代价与风险暴露时间——并给出安全/不安全成功与失败的四象限分解；在 RoboTwin 上实例化 66 个安全增强基础场景。结果表明即使最强策略也有不可忽视的安全代价与非安全的名义成功，且结构与视觉变化造成的安全退化远强于普通语言变化。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：原文示例中 OpenVLA-oft 的 SR 为 0.48、不安全成功为 0.06，即成功轨迹中 12.5% 不安全；常规措辞变化与结构性风险的影响不同。成果包括场景、风险 taxonomy 和统一评分协议。

**适用边界**：四象限的分母是全部 episode，不能把不安全成功率直接当成成功中的违规比例。仿真中的风险触发与真实损伤之间仍有距离。

## 5. 相关论文（均来自本调研表）

- [ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2606.27079)（2026；提出）

## 6. 证据边界与复核建议

### 6.1 全文核查补录（核心论文）

> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。

**来源文件**：`docs/_fulltext/ForesightSafety-VLA.txt`。

**评测协议**：RoboTwin 中从已有资产与原语人工构造 66 个基础场景，覆盖 Safe-Core、Safe-Lang、Safe-Vis 三侧 13 类风险；通过 hazard injection、constraint tightening、temporal precondition insertion 三类算子增强。结构/布局 L0–L2、语言 W0–W4、视觉 V0–V4 三个变化维度分别控制难度，W3–W4 的语言由前沿 LLM 生成后人工核验；视觉扰动在推理时累积且不改变物理动力学。

**定量证据**：实验覆盖 5 种本体；每个模型-任务-设置共 50 个 evaluation episodes，分布于 3 个随机种子，另对 10 个代表场景做诊断子集。四个完整基线的累计安全代价 CC 为 OpenVLA-oft 0.18、RDT 0.29、DP 0.34、ACT 0.39；unsafe-success 比例为 0.06、0.10、0.10、0.12。OpenVLA-oft 总成功率 0.48，成功回合中 12.5% 不安全；RDT、DP、ACT 的总成功率分别为 25.0%、29.4%、37.5%。

**全文结论**：结构与视觉变化造成的安全退化明显强于普通语言变化；对抗性语言 W3–W4 会造成额外风险。代表性 lift_pot 场景中热风险暴露约 40%、空间边界约 60%、力风险低于 10%，但任一风险激活的 episode 占 62%；Thermal/Energy 最难，Temporal Sequence 相对容易。

**适用边界**：部分扩展模型和逐类结果只在全文表格中给出；CC、RET 与四象限结果需要保持其原始阈值和 episode 聚合方式，不能与普通 success rate 直接混合。

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

四象限的分母是全部 episode，不能把不安全成功率直接当成成功中的违规比例。仿真中的风险触发与真实损伤之间仍有距离。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Mingyang Lyu, Yinqian Sun, Yiyang Jia, et al., ‘ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2606.27079v2. [论文](https://arxiv.org/abs/2606.27079)；[核查正文](https://arxiv.org/html/2606.27079v2)。

**重点核查位置（章节主题）**：III Benchmark；IV Evaluation；V Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7166132482)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/tuotuoLyu/ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/tuotuoLyu/ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/tuotuoLyu/ForesightSafety-VLA) | https://raw.githubusercontent.com/tuotuoLyu/ForesightSafety-VLA/HEAD/README.md | stars 87，license NOASSERTION，最后推送 2026-10-29，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/tuotuoLyu/ForesightSafety-VLA（87 stars，2026-10-29 推送，许可标记 NOASSERTION），README 为论文首页信息与作者单位。

**涉及领域**：VLA 模型的物理与语义安全诊断；仿真操作场景，含任务难度分级与语言／视觉扰动。

**测试目的与构建方法**：用层级任务难度与语言／视觉扰动构造可控测试，结合任务完成与约束违反信号，报告 SR、约束违反 CC、风险暴露 RET，并把 episode 分成安全成功／不安全成功／安全失败／不安全失败四象限。

**测试缺陷**：四象限分母是全部 episode，不能把“不安全成功”当成成功中的违规比；仿真风险触发与真实损伤仍有距离；扰动强度与任务难度耦合。

**与具身智能安全的相关性**：直接测执行层安全：动作是否违反约束，以及“成功”里有多少是危险的。四象限正好把能力与安全解耦，是本库中最贴近物理安全的评测之一。

**用这个 benchmark 测了什么**：原文示例 OpenVLA-oft 的 SR 0.48、不安全成功 0.06（即成功轨迹中约 12.5% 不安全）；常规措辞变化与结构性风险影响不同，说明“换个说法”不足以暴露风险。

**本轮核查边界**：只读 README 头部，未核对代码与数据集。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 12 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **CC** | Cumulative safety Cost | 累计安全代价 | 一次 episode 内违规代价的累加，衡量“踩线有多重”而非“有没有踩线”。 |
| **RET** | Risk Exposure Time | 风险暴露时间 | 处于风险状态（如贴着人或物体）的时长。 |
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **OpenVLA** | OpenVLA（含 OpenVLA-oft 变体） | OpenVLA 开源策略 | 开源的 7B VLA 基线，安全基准里最常被拿来测“干净能力 vs 安全”的模型之一。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **RDT** | Robotics Diffusion Transformer | 机器人扩散 Transformer | 基于扩散 Transformer 的机器人策略，常见对照模型之一。 |
| **DP** | Diffusion Policy | 扩散策略 | 用扩散模型生成动作序列的模仿学习基线，安全论文里常作“普通策略”对照。 |
| **ACT** | Action Chunking with Transformers | 动作分块 Transformer 策略 | 把连续多步动作一次性预测的模仿学习基线，常作为对照。 |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 基准自定义的难度阶梯：常见是 L0 干净、L1 加扰动、L2 更强扰动或结构变化，L3 更难。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| ForesightSafety-VLA | 基准 | VLA 安全诊断基准 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |

<!-- glossary:end -->
