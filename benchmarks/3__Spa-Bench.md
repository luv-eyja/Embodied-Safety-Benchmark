# Spa-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：真机空间理解和执行混淆的受控诊断。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：空间接地真机基准  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://justintiensmith.github.io/Spa-Bench](https://justintiensmith.github.io/Spa-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › World Model |
| 应用领域 | 未标注 |
| 被测对象 | 真实机器人空间接地 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 六类空间描述（物体状态、相对大小、指代、关系放置、序数、计数）；ID/OOD 对比 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | SO-101 上六类桌面任务：物体状态、相对大小、指代描述、关系摆放、序数位置、计数；1,200 示范与 2,892 真实评测轨迹。 |
| 执行环境线索 | 真实机器人空间接地 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221577967)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：模型失败究竟因为不理解空间描述，还是因为不会执行所需机械动作？

**评测层级**：真实机器人空间接地。

## 2. 怎么构建的

**核心场景与条目**：SO-101 上六类桌面任务：物体状态、相对大小、指代描述、关系摆放、序数位置、计数；1,200 示范与 2,892 真实评测轨迹。

**实现与判分**：保留对象、概念和动作的训练支持，仅留出空间配置；在相同场景比较空间指令与直接操作指令，另测改写、跨任务对象和无需动作条件。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696) | 2026 | 提出 | 六类空间描述（物体状态、相对大小、指代、关系放置、序数、计数）；ID/OOD 对比 | 多数 VLA 评测只看物体、指令或环境变化下的总体操作成功率，难以判断策略能否把空间描述可靠地落到物理场景中。该真机基准覆盖物体状态、相对大小、指代描述、关系放置、序数位置与计数六类桌面任务，主要对比分布内与分布外表现，直接考察空间描述到行为的接地能力。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：三个完整评测策略的 ID 成功率为 67.5–73.3%，OOD 为 40.7–52.0%；匹配场景中直接指令比空间指令高 28.3–40.0 个百分点，支持接地错误并非纯运动问题。

**适用边界**：五个模型并非全部完成同样评测，主要比较限于三个完整策略。小型桌面机器人和有限物体不代表开放世界空间推理。

## 5. 相关论文（均来自本调研表）

- [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

五个模型并非全部完成同样评测，主要比较限于三个完整策略。小型桌面机器人和有限物体不代表开放世界空间推理。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Justin Tien-Smith, Matthew Pidden, Rolandos Alexandros Potamias, ‘Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2610.12696v1. [论文](https://arxiv.org/abs/2610.12696)；[核查正文](https://arxiv.org/html/2610.12696v1)。

**重点核查位置（章节主题）**：III-A Task Suite；III-C Controlled ID and OOD；V-A；V-B Matched-Scene Diagnostics。

OpenAlex 被引次数：**[0](https://openalex.org/W7221577967)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://justintiensmith.github.io/Spa-Bench](https://justintiensmith.github.io/Spa-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 2 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://justintiensmith.github.io/Spa-Bench](https://justintiensmith.github.io/Spa-Bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://justintiensmith.github.io/Spa-Bench) | https://justintiensmith.github.io/Spa-Bench | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://justintiensmith.github.io/Spa-Bench 为 Imperial College London 的真机基准页，含摘要与视频；本轮未取到独立代码仓库。

**涉及领域**：VLA 的空间接地（spatial grounding）；真机桌面机器人，仅留出空间配置。

**测试目的与构建方法**：保留对象、概念与动作的训练支持，只留出空间配置；在相同场景下比较空间指令与直接操作指令，另测改写、跨任务对象与“无需动作”条件。

**测试缺陷**：五个模型并非全部完成同样评测，主要比较限于三个完整策略；小型桌面机器人与有限物体不代表开放世界空间推理；空间配置的留出方式影响难度。

**与具身智能安全的相关性**：中等：空间接地错误会导致“够错位置／撞到旁边的物体”，是物理安全的上游原因；基准本身评成功率。

**用这个 benchmark 测了什么**：三个完整评测策略 ID 成功率 67.5–73.3%、OOD 40.7–52.0%；匹配场景中直接指令比空间指令高 28.3–40.0 个百分点，说明接地错误不是纯运动问题。

**本轮核查边界**：只读项目页，代码入口未确认。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **2 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Benchmarking LLM Judges for Mobile Agent Evaluation（2026） | 6 种 judge 方法（5 种改编自 SPA-Bench／A3／AndroidArena／AgentRewardBen… | 借用评测方法（把 SPA-Bench 的评分做法搬来做 judge 对比） | 6 个移动代理基准、4 个代理模型、68 个 App | 产出的是 judge 方法比较，不是 SPA-Bench 上的模型分数 |
| OpenMobile-2: Building Versatile Mobile Agents with Scalable Environme…（2026） | OpenMobile-2 | 评测（迁移测试） | AndroidWorld 79.9、MobileWorld 50.4，另报 SPA-Bench 上的迁移表现 | 在 SPA-Bench 上表现“接近翻倍”（摘要未给绝对值） |

**原文片段（摘要）**：

- Benchmarking LLM Judges for Mobile Agent Evaluation（2026，arXiv）：> We evaluate 6 judge methods (five adapted from SPA-Bench, A3 …) across multiple LLM backends
- OpenMobile-2: Building Versatile Mobile Agents with Scalable…（2026，arXiv）：> nearly doubling SPA-Bench performance

**口径提示**：SPA-Bench 是手机 GUI 代理基准（Spa-Bench）与机器人空间接地基准（Spa-Bench: Real-Robot Spatial Grounding）重名：上面两条 Arduino／手机代理的引用属于前者，不是本条真机空间接地基准。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 6 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **ID** | In-Distribution | 分布内 | 测试与训练同分布，通常作为上限参照。 |
| **OOD** | Out-of-Distribution | 分布外 | 测试数据与训练分布不同，用来检验泛化。 |
| **GUI** | Graphical User Interface | 图形界面（软件代理） | 手机／桌面应用的图形界面，软件代理基准的操作对象。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| Spa-Bench | 基准 | 真实机器人空间接地 |

<!-- glossary:end -->
