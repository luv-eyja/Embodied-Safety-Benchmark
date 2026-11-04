# Bench2Dex

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：多本体双手测试集，统一模拟触觉不等于真触觉验证。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：跨灵巧手视触觉  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://bench2dex.github.io](https://bench2dex.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 灵巧操作 |
| 被测对象 | 双手视触觉仿真与数据平台 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 12 种灵巧手；共享的仿真触觉接口 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 12 种灵巧手、26 个双手任务、约 1,300 条遥操作示范；工具、关节物体和多阶段操作，七种扰动分不变性与等变性两轴。 |
| 执行环境线索 | 双手视触觉仿真与数据平台 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7213308421)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 8 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：灵巧手结构和触觉硬件不同，能否在统一格式下研究双手操作与泛化？

**评测层级**：双手视触觉仿真与数据平台。

## 2. 怎么构建的

**核心场景与条目**：12 种灵巧手、26 个双手任务、约 1,300 条遥操作示范；工具、关节物体和多阶段操作，七种扰动分不变性与等变性两轴。

**实现与判分**：Isaac Lab（仿真平台） 中记录手套／腕部遥操作，离线重放成同步 RGB-D、触觉、关节、动作和物体状态；局部接触几何转换为统一图像式触觉，采用稳定成功 SR 和锁存阶段完成 LSCR。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](https://arxiv.org/abs/2609.15726) | 2026 | 提出 | 12 种灵巧手；共享的仿真触觉接口 | 指出触觉能提供视觉难以推断的接触信息，但灵巧手的触觉硬件尚未收敛到统一设计——不同手的指结构、接触面与传感器布局各异，仿真触觉信号又与真实传感器测量不同，因而难以在一致实验条件下研究跨手视触觉操作。Bench2Dex 为 12 种灵巧手构建统一仿真触觉接口并据此评测。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：四种策略在不同任务和扰动通道表现差异明显；例如 Gaming Desk Setup 的 GR00T-N1.5 四通道平均稳定成功率为 59.5%，ACT 为 31.0%。

**适用边界**：统一触觉是模拟接触表征，不是特定真实传感器的数字复制；主实验部分策略仅用 RGB 与关节，不能将所有成绩解释为触觉带来的收益。

## 5. 相关论文（均来自本调研表）

- [Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands](https://arxiv.org/abs/2609.15726)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

统一触觉是模拟接触表征，不是特定真实传感器的数字复制；主实验部分策略仅用 RGB 与关节，不能将所有成绩解释为触觉带来的收益。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Zhenjie Yang, Yideng Zhang, Dongjie Zhang, et al., ‘Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands,’ arXiv preprint, 2026, arXiv:2609.15726v1. [论文](https://arxiv.org/abs/2609.15726)；[核查正文](https://arxiv.org/html/2609.15726v1)。

**重点核查位置（章节主题）**：3.1 Teleoperation；3.3 Visuo-Tactile Acquisition；3.4 Datasets and Policy；3.5 Metrics；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7213308421)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://bench2dex.github.io](https://bench2dex.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://bench2dex.github.io](https://bench2dex.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://bench2dex.github.io) | https://bench2dex.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://bench2dex.github.io 提供 Overview、Compare Embodiments、Teleop & Data、Tasks、Evaluation、Generalization、Leaderboard 与 Docs 入口，属完整发布页。

**涉及领域**：双臂灵巧手操作，带仿真指尖视触觉；桌面装配类任务。

**测试目的与构建方法**：在 Isaac Lab 中录制手套／腕部遥操作，离线重放成同步 RGB-D、触觉、关节、动作与物体状态，把局部接触几何转成统一图像式触觉，用稳定成功率 SR 与锁存阶段完成 LSCR 判分。

**测试缺陷**：统一触觉是模拟接触表征，不是特定真实传感器的数字复刻；主实验部分策略只用 RGB 与关节，不能把成绩解释为触觉收益；全部在仿真中完成。

**与具身智能安全的相关性**：间接：接触表征与力相关，但指标是成功与阶段完成，不含损伤、滑移或过载判罚；可作为触觉安全研究的前置平台。

**用这个 benchmark 测了什么**：四种策略在不同任务与扰动通道差异明显，例如 Gaming Desk Setup 上 GR00T-N1.5 四通道平均稳定成功率 59.5%、ACT 为 31.0%。

**本轮核查边界**：只读项目页导航与摘要，未进入 Leaderboard 或评测脚本。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **LSCR** | Latched Stage Completion Rate | 锁存阶段完成率 | 阶段一旦完成就锁定、不因后续失败撤销的完成率。 |
| **GR00T** | NVIDIA GR00T N1 / N1.5 | GR00T 机器人基础模型 | NVIDIA 的类人／通用操作基础模型家族，常作为强基线或微调起点。 |
| **ACT** | Action Chunking with Transformers | 动作分块 Transformer 策略 | 把连续多步动作一次性预测的模仿学习基线，常作为对照。 |
| **teleoperation** | teleoperation | 遥操作 | 人通过手柄、外骨骼或手套远程操控机器人采集数据。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |
| **Isaac** | Isaac Sim / Isaac Lab | Isaac 仿真与训练框架 | NVIDIA 的 GPU 加速仿真与并行训练框架，适合大规模域随机化。 |
| **RGB** | RGB image observation | 彩色图像观测 | 只用普通彩色相机画面作为输入，不含深度、触觉或本体状态。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| Bench2Dex | 基准 | 双手视触觉仿真与数据平台 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 Isaac Lab（仿真平台）），不再重复解释。

<!-- glossary:end -->
