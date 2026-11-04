# LIBERO-RECOVER

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：恢复能力测试；恢复成功不自动表示全过程安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：控制（失败恢复）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://liulin815.github.io/LIBERO-Recovery](https://liulin815.github.io/LIBERO-Recovery)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真自然失败状态恢复 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、任务能力 |
| 评测维度/指标 | 失败识别与恢复成功率（相对纯任务成功率） |
| 基础平台线索 | LIBERO |
| 规模线索 | 收集 2,000 余真实策略运行产生的失败状态；四级恢复从动作重试、动作适配到物体状态与环境恢复，并按空间、物体结构、交互和拓扑能力标注。 |
| 执行环境线索 | 仿真自然失败状态恢复 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7211887144)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：模型在自己的执行错误之后能否恢复，正常起点的高分是否能预测恢复能力？

**评测层级**：仿真自然失败状态恢复。

## 2. 怎么构建的

**核心场景与条目**：收集 2,000 余真实策略运行产生的失败状态；四级恢复从动作重试、动作适配到物体状态与环境恢复，并按空间、物体结构、交互和拓扑能力标注。

**实现与判分**：从存档失败状态继续执行原任务，报告 Recovery Success Rate、Recovery Degradation 和一致性；分级、分能力比较，而不是只加随机初始扰动。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178) | 2026 | 提出 | 失败识别与恢复成功率（相对纯任务成功率） | 指出 LIBERO 上已接近 100% 的成功率具有误导性：真实交互中必然出现抓取失败、碰撞与物体意外移动，机器人不仅要完成任务还要能识别并从中恢复，而这一能力此前基本未被度量。该基准在既有成功率之外补充失败恢复能力的评测，弥合基准成绩与真实可靠性之间的差距。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：表 2 中 GR00T-N1.5 在 LIBERO-Spatial 恢复集的 RSR 从 0.057 提升至混合恢复数据训练后的 0.116；论文同时发现这种收益未稳定转化为正常起点分数。更长动作块通常更难恢复。

**适用边界**：这里的自然失败发生在仿真策略 rollout，并非真实世界事故。失败状态来源策略与筛选流程影响分布，恢复集提升不等于所有失败都可自行纠正。

## 5. 相关论文（均来自本调研表）

- [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这里的自然失败发生在仿真策略 rollout，并非真实世界事故。失败状态来源策略与筛选流程影响分布，恢复集提升不等于所有失败都可自行纠正。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Lin Liu, Zhicheng Bao, Lu Zhang, et al., ‘LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models,’ arXiv preprint, 2026, arXiv:2609.05178v3. [论文](https://arxiv.org/abs/2609.05178)；[核查正文](https://arxiv.org/html/2609.05178v3)。

**重点核查位置（章节主题）**：2 Failure Collection；3.2 Evaluation Metrics；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7211887144)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://liulin815.github.io/LIBERO-Recovery](https://liulin815.github.io/LIBERO-Recovery)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://liulin815.github.io/LIBERO-Recovery](https://liulin815.github.io/LIBERO-Recovery)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://liulin815.github.io/LIBERO-Recovery) | https://liulin815.github.io/LIBERO-Recovery | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://liulin815.github.io/LIBERO-Recovery 明确 2,178 场景、4 个恢复等级、16 个评测维度、3,184 条人类示教（4 名遥操作者、625,731 帧 @20Hz，第三人称 + 腕部视角），并标注双盲评审中、代码将发布。

**涉及领域**：机械臂操作的失败恢复；从存档失败状态继续执行原任务。

**测试目的与构建方法**：从真实策略 rollout 中的失败状态续跑，报告 Recovery Success Rate、Recovery Degradation 与一致性，并按 L1–L4 恢复等级与能力分组比较，而不是只加随机初始扰动。

**测试缺陷**：自然失败来自仿真策略 rollout，不是真实事故；失败状态由特定策略与筛选流程产生，分布随之变化；恢复集上的提升不等于所有失败都能自行纠正。

**与具身智能安全的相关性**：直接相关：事故后能否“止损并恢复”是安全工程的核心指标之一；它把安全从“不出事”扩展到“出事后的可控性”，但仍是仿真。

**用这个 benchmark 测了什么**：2,178 个恢复场景、130 个子任务、4 个 LIBERO 套件与 3,184 条人类恢复示教；表 2 中 GR00T-N1.5 在 LIBERO-Spatial 恢复集 RSR 由 0.057 升到 0.116（混合恢复数据训练），但收益未稳定转化为正常起点分数；更长动作块通常更难恢复。

**本轮核查边界**：代码标注“soon／将发布”，本轮无法核实可运行性。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 6 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **rollout** | rollout | 展开／推演 | 用当前策略跑一次得到的完整轨迹，常与 episode 混用。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **GR00T** | NVIDIA GR00T N1 / N1.5 | GR00T 机器人基础模型 | NVIDIA 的类人／通用操作基础模型家族，常作为强基线或微调起点。 |
| **teleoperation** | teleoperation | 遥操作 | 人通过手柄、外骨骼或手套远程操控机器人采集数据。 |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 基准自定义的难度阶梯：常见是 L0 干净、L1 加扰动、L2 更强扰动或结构变化，L3 更难。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **rollout**：rollout 数、episode 数、候选轨迹数三者混用。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| LIBERO-RECOVER | 基准 | 仿真自然失败状态恢复 |

<!-- glossary:end -->
