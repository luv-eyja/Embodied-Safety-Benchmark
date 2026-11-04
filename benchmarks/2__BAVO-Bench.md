# BAVO-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：评估主动观察和遮挡鲁棒性，没有据遮挡推断安全约束。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：遮挡下的主动视觉恢复  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 主动视觉 |
| 被测对象 | 仿真双臂主动视觉 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 5 个双臂任务，一臂操作、一臂携带相机；Clean、Stage 和随机时刻遮挡三种条件，每任务 100 条 VR 示范，共 500 条。 |
| 执行环境线索 | 仿真双臂主动视觉 |
| 来源审计 | [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce BAVO-Bench。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214940409)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 8 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：遮挡发生后，机器人能否主动移动观察相机，再继续操作？

**评测层级**：仿真双臂主动视觉。

## 2. 怎么构建的

**核心场景与条目**：5 个双臂任务，一臂操作、一臂携带相机；Clean、Stage 和随机时刻遮挡三种条件，每任务 100 条 VR 示范，共 500 条。

**实现与判分**：用阶段相关遮挡数据训练，评估 SR、任务进展 TPS 和相机运动带来的可见性增益 CVG，区分真实主动观察与单纯视觉恢复。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292) | 2026 | 提出 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 | 指出物理主动视觉允许机器人在任务相关观测不可靠时改变视角，但现有操作基准对「策略如何在执行中从遮挡恢复」支持有限。BAVO-Bench 通过 Clean、Stage Occlusion 与 Random-time Occlusion 三种条件系统控制外部可见性，同时评测操作性能与主动视觉恢复能力；作者据此提出联合视角与操作控制的 A-FAR 策略。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：A-FAR 的 Clean／Stage／随机遮挡 SR 为 51.3%／63.7%／18.7%。训练匹配的 Stage 可能比 Clean 更高，不能假定难度单调；随机遮挡明显更难。

**适用边界**：ACT、ManiFlow、A-FAR 使用三种种子，π0.5 的训练设置不同，不能将所有行当等预算比较；可见性增益也不能替代任务成功。

## 5. 相关论文（均来自本调研表）

- [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

ACT、ManiFlow、A-FAR 使用三种种子，π0.5 的训练设置不同，不能将所有行当等预算比较；可见性增益也不能替代任务成功。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Kaijun Luo, Yudi Huang, Qijun Zhong, et al., ‘Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation,’ arXiv preprint, 2026, arXiv:2609.37292v1. [论文](https://arxiv.org/abs/2609.37292)；[核查正文](https://arxiv.org/html/2609.37292v1)。

**重点核查位置（章节主题）**：3.2 Benchmark；5.1 Experimental Setup；5.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214940409)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://hcplab-sysu.github.io/BAVO-Bench) | https://hcplab-sysu.github.io/BAVO-Bench | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://hcplab-sysu.github.io/BAVO-Bench 提供动机图、benchmark 与方法的整体示意及作者单位，未见独立代码仓库链接。

**涉及领域**：机械臂操作中的主动视觉与遮挡恢复（物理主动观察）；桌面操作场景。

**测试目的与构建方法**：构造阶段相关的遮挡数据，训练并评测策略在外部遮挡下主动移动相机恢复可见性；指标为成功率 SR、任务进展 TPS 与相机运动带来的可见性增益 CVG。

**测试缺陷**：可见性增益不能替代任务成功；ACT、ManiFlow、A-FAR 使用三种种子而 π0.5 训练设置不同，各行不是等预算比较；遮挡只在仿真中程序化生成。

**与具身智能安全的相关性**：间接但重要：遮挡导致的“看不见仍在动”是典型事故来源，该基准把“主动确认视野”作为可测能力；它不直接给碰撞或伤害指标。

**用这个 benchmark 测了什么**：A-FAR 在 Clean／Stage／随机遮挡下的 SR 为 51.3%／63.7%／18.7%，说明训练匹配的 Stage 可能比 Clean 更高、难度并不单调；被测策略含 ACT、ManiFlow、π0.5 与 A-FAR。

**本轮核查边界**：项目页是静态介绍页，代码与数据可获取性未核实。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 8 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VR** | Violation Rate | 违规率 | 发生约束违反的 episode ÷ 全部 episode，不看任务是否完成。 |
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **TPS** | Task Progress Score | 任务进展分 | 把任务拆成阶段后，按完成到第几个阶段给的部分分。 |
| **CVG** | Camera Visibility Gain | 相机可见性增益 | 主动移动相机后，目标可见性提升多少。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **ACT** | Action Chunking with Transformers | 动作分块 Transformer 策略 | 把连续多步动作一次性预测的模仿学习基线，常作为对照。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| BAVO-Bench | 基准 | 仿真双臂主动视觉 |

<!-- glossary:end -->
