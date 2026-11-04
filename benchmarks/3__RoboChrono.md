# RoboChrono

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：对已采集机器人视频进行理解测试，无策略动作执行。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：流式任务理解  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://continuity3.github.io/robochrono](https://continuity3.github.io/robochrono)；[https://github.com/mfan-res/ROBOCHRONO](https://github.com/mfan-res/ROBOCHRONO)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboChrono: A Real Robot Benchmark for Streaming Task Understanding |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 机器人流式视频理解 |
| 历史关键词标签（未重新统计） | 语义/指令安全、任务能力 |
| 评测维度/指标 | 39 个场景 / 34,713 个评测实例；7 类任务（识别、对齐、时序接地） |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 39 种操作场景、1,816 个成功视频、约 25 小时；包括夹爪、灵巧手及人手，七项任务覆盖当前／下一动作、跨视角匹配、顺序和时间定位。 |
| 执行环境线索 | 机器人流式视频理解 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214955540)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：只看到当前时刻以前的画面，模型能否理解动作进度、预测下一步并定位事件？

**评测层级**：机器人流式视频理解。

## 2. 怎么构建的

**核心场景与条目**：39 种操作场景、1,816 个成功视频、约 25 小时；包括夹爪、灵巧手及人手，七项任务覆盖当前／下一动作、跨视角匹配、顺序和时间定位。

**实现与判分**：人工时间标注后生成问题，输入严格截断为观察前缀；六项选择题报告正确率，动作时间定位独立报告 R@1、tIoU≥0.5，未来信息仅用于标签。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboChrono: A Real Robot Benchmark for Streaming Task Understanding](https://arxiv.org/abs/2609.36605) | 2026 | 提出 | 39 个场景 / 34,713 个评测实例；7 类任务（识别、对齐、时序接地） | 理解正在进行的机器人操作，要求模型把视觉观测与交互历史、任务进度联系起来。RoboChrono 是流式任务理解基准，由真机执行数据与互补的裸手人类录制构成，含 39 个场景、34,713 个评测实例；评测 7 类任务、归为识别、对齐与时序接地三组，覆盖动作理解与预判、视觉对应、时序排序与动作定位。18 个视觉语言模型的零样本评测显示任务间差异巨大。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：18 个多模态模型的结果显示跨帧识别、下一步预测和时间定位难度不同；论文最佳选择题聚合为 0.805，时间定位为 0.721，二者不是同一种指标。

**适用边界**：这是视频理解而非机器人控制成功率。成功示范视频不能代表失败恢复过程；人手与机器人视频、不同任务指标不宜无条件求平均。

## 5. 相关论文（均来自本调研表）

- [RoboChrono: A Real Robot Benchmark for Streaming Task Understanding](https://arxiv.org/abs/2609.36605)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这是视频理解而非机器人控制成功率。成功示范视频不能代表失败恢复过程；人手与机器人视频、不同任务指标不宜无条件求平均。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Yuzhou Wu, Longteng Fan, Zimeng Li, et al., ‘RoboChrono: A Real Robot Benchmark for Streaming Task Understanding,’ arXiv preprint, 2026, arXiv:2609.36605v1. [论文](https://arxiv.org/abs/2609.36605)；[核查正文](https://arxiv.org/html/2609.36605v1)。

**重点核查位置（章节主题）**：3.1 Benchmark Overview；3.2 Data Collection and Temporal Annotation；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214955540)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://continuity3.github.io/robochrono](https://continuity3.github.io/robochrono)；[https://github.com/mfan-res/ROBOCHRONO](https://github.com/mfan-res/ROBOCHRONO)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://continuity3.github.io/robochrono](https://continuity3.github.io/robochrono)；[https://github.com/mfan-res/ROBOCHRONO](https://github.com/mfan-res/ROBOCHRONO)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://continuity3.github.io/robochrono) | https://continuity3.github.io/robochrono | 保留文本 4200 字符（截断） |
| [repo](https://github.com/mfan-res/ROBOCHRONO) | https://raw.githubusercontent.com/mfan-res/ROBOCHRONO/HEAD/README.md | stars 14，license Apache-2.0（开源许可证），最后推送 2026-09-28，保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://continuity3.github.io/robochrono（含 Tianji／GIM 两个数据集与在线预览）与 GitHub https://github.com/mfan-res/ROBOCHRONO（14 stars，Apache-2.0，2026-09-28 推送）并存，README 注明“独立排行榜即将发布”。

**涉及领域**：真实机器人的流式任务理解（视频时序推理）；含人类示教与两种真实机械臂数据。

**测试目的与构建方法**：人工时间标注后生成问题，输入严格截断为“观察前缀”（不给未来帧）；六项选择题报告正确率，动作时间定位独立报告 R@1 与 tIoU≥0.5，未来信息只用于标签。

**测试缺陷**：这是视频理解而非控制成功率；成功示范视频不能代表失败与恢复过程；人手视频与机器人视频、不同任务指标不宜无条件平均；题目由标注生成，风格集中。

**与具身智能安全的相关性**：间接：实时场景理解是“及时识别危险”的前提，但基准不含风险标注，也没有动作输出。

**用这个 benchmark 测了什么**：18 个多模态模型的结果显示跨帧识别、下一步预测与时间定位难度不同；论文最佳选择题聚合 0.805、时间定位 0.721，二者不是同一指标。

**本轮核查边界**：只读项目页与 README，未下载数据集。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **R@1** | Recall at 1 | 首位命中率 | 检索或定位时，第一名即为正确的比例。 |
| **tIoU** | temporal Intersection over Union | 时间交并比 | 时间区间预测与真值的时间重叠比，用于动作定位。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **zero-shot** | zero-shot evaluation | 零样本评测 | 不针对该基准做任何训练或微调，直接拿现成模型跑。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboChrono | 基准 | 机器人流式视频理解 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 Apache-2.0（开源许可证）），不再重复解释。

<!-- glossary:end -->
