# ASIMOV Benchmark

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：安全。
> **分类依据**：主要为情境安全测试与准则生成配套数据，未以连续控制为主。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：语义安全与机器人宪法  
> **分类**：VLA 安全  
> **关联论文**：本表 2 篇（提出 1、使用 1；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Generating Robot Constitutions & Benchmarks for Semantic Safety |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › World Model |
| 应用领域 | 未标注 |
| 被测对象 | 机器人语义安全判断／数据与方法 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、对抗/后门安全、失败恢复、任务能力 |
| 评测维度/指标 | 语义安全；大规模情景化安全判断数据集 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 多模态场景、伤害事件描述和伦理困境三个子集；既包含明显危险，也包含依赖人、物和情境的灰区。表 1 合计约 294 万动作／指令、51 万上下文，不是同等数量的人类标注。 |
| 执行环境线索 | 机器人语义安全判断／数据与方法 |
| 来源审计 | [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明发布 ASIMOV Benchmark；AGENTSAFE 是本库中的使用论文。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W4414578652)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 3 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：机器人能否判断某个动作在具体情境下是否合宜，并将这种判断落实为可修订的安全准则？

**评测层级**：机器人语义安全判断／数据与方法。

## 2. 怎么构建的

**核心场景与条目**：多模态场景、伤害事件描述和伦理困境三个子集；既包含明显危险，也包含依赖人、物和情境的灰区。表 1 合计约 294 万动作／指令、51 万上下文，不是同等数量的人类标注。

**实现与判分**：将情境与候选动作转成可判别的问答，用模型生成和增补机器人 constitution，再与人类判断比较；验证集包括 2,273 个问题，其中 1,140 个有人类标签。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697) | 2025 | 使用 | 感知-规划-执行全过程；危险指令下的违规与失败模式 | 指出既有安全基准危险范围窄、只看最终结果，忽略智能体完整的感知-规划-执行过程，从而掩盖关键失败模式。SAFE 含三部分：可扩展的对抗仿真沙箱 SAFE-THOR（通用适配器把 VLM 高层输出映射为底层具身控制，支持多种智能体工作流接入）、风险感知的 SAFE-VERSE 等，用于系统评估具身 VLM 智能体执行危险指令时的安全性。 |
| [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663) | 2025 | 提出 | 语义安全；大规模情景化安全判断数据集 | 指出机器人安全研究长期聚焦碰撞回避与近身危害，而视觉语言模型使机器人具备高层语义理解与自然语言交互能力，其幻觉与被越狱等已知脆弱性一旦被交予可产生物理接触的机器人即形成直接危险。工作有两点贡献：给出可规模化生成「机器人宪法」的数据配方，并发布 ASIMOV Benchmark——用于评测与提升机器人基础模型语义安全的大规模数据集集合。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文报告自动生成准则可达到 84.3% 的人类判断一致率，并给出有限机器人场景的防护验证。主要成果是语义安全数据与准则生成流程。

**适用边界**：一致率不等于闭环动作安全率；自动扩增规模不代表人工审查覆盖率。机器人案例数量小，不能据此声称对所有物理危险有保证。

## 5. 相关论文（均来自本调研表）

- [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697)（2025；使用）
- [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

一致率不等于闭环动作安全率；自动扩增规模不代表人工审查覆盖率。机器人案例数量小，不能据此声称对所有物理危险有保证。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Pierre Sermanet, Anirudha Majumdar, Alex Irpan, et al., ‘Generating Robot Constitutions & Benchmarks for Semantic Safety,’ arXiv preprint, 2025, arXiv:2503.08663v1. [论文](https://arxiv.org/abs/2503.08663)；[核查正文](https://arxiv.org/html/2503.08663v1)。

**重点核查位置（章节主题）**：3 ASIMOV Datasets；4 Generating Constitutions；6 Empirical Evaluation。

OpenAlex 被引次数：**[0](https://openalex.org/W4414578652)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 1 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://asimov-benchmark.github.io/](https://asimov-benchmark.github.io/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://asimov-benchmark.github.io/) | https://asimov-benchmark.github.io/ | 保留文本 98 字符（截断） |

**项目页显示**：项目地址为 https://asimov-benchmark.github.io/，抓取时只返回跳转提示（Redirecting to ASIMOV Benchmark v1），未取到数据或代码说明。

**涉及领域**：图像—动作的语义安全问答；数据来自真实图像与医院伤害报告，面向机器人在家庭／医疗场景的常识性伤害判断。

**测试目的与构建方法**：把情境与候选动作转成可判别的问答对，用模型生成并增补“机器人 constitution”，再与人类判断比对；验证集 2,273 题，其中 1,140 题有人类标签。

**测试缺陷**：一致率不等于闭环动作安全率；自动扩增的规模不代表人工审查覆盖；机器人案例数量少，不能据此声称对所有物理危险有保证；项目页已重定向到 v1，未提供可运行的评测脚本入口。

**与具身智能安全的相关性**：直接测“伤害常识”这一层安全：模型能否识别会伤人的动作。它覆盖语义与后果判断，但不是执行层约束，不能回答碰撞、力控或轨迹越界问题。

**用这个 benchmark 测了什么**：论文报告自动生成的准则与人类判断达到 84.3% 一致率，并给出少量机器人场景的防护验证；SciFi-Benchmark（2026）在同一基准上比较科幻作品衍生的 constitution，报告一致率提升。本轮未从项目页取得完整被测模型清单。

**本轮核查边界**：项目页为纯跳转页，代码／数据可用性未在本轮核实。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **1 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| SciFi-Benchmark: Leveraging Science Fiction To Improve Robot Behavior（2025） | 由科幻作品生成的 constitution（准则）驱动的模型 | 评测（安全准则比较） | ASIMOV 验证集（题目由真实图像与医院伤害报告派生），比较不同 constitution 的人类判断一致率 | 该文的 constitution 进入 ASIMOV 上的最优一组；摘要未给出具体数值 |

**原文片段（摘要）**：

- SciFi-Benchmark: Leveraging Science Fiction To Improve Robot…（2025，arXiv）：> 那些 constitution 在 ASIMOV Benchmark 上属于 top performers

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 3 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| ASIMOV Benchmark | 基准 | 机器人语义安全判断／数据与方法 |

<!-- glossary:end -->
