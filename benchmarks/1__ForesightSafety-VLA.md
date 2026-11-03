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
| OpenAlex 引用快照 | [0](https://openalex.org/W7166132482)；2026-11-03 |

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
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Mingyang Lyu, Yinqian Sun, Yiyang Jia, et al., ‘ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2606.27079v2. [论文](https://arxiv.org/abs/2606.27079)；[核查正文](https://arxiv.org/html/2606.27079v2)。

**重点核查位置（章节主题）**：III Benchmark；IV Evaluation；V Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7166132482)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/tuotuoLyu/ForesightSafety-VLA](https://github.com/tuotuoLyu/ForesightSafety-VLA)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
