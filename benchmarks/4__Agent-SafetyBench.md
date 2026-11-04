# Agent-SafetyBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；软件代理邻接研究；目标：安全。
> **分类依据**：通用代理安全任务集；物理风险类别不代表实际机器人测试。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：LLM 智能体安全  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/thu-coai/Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Agent-SafetyBench: Evaluating the Safety of LLM Agents |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Self-Evolving |
| 应用领域 | 未标注 |
| 被测对象 | 通用工具代理安全；邻接参考 |
| 历史关键词标签（未重新统计） | 失败恢复 |
| 评测维度/指标 | 349 个交互环境、2000 个测试用例；8 类风险、10 种失败模式 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 349 个交互环境、2,000 测试用例、8 类风险、10 种失败模式，包含信息泄漏、财产损失、物理后果及工具可用性等。 |
| 执行环境线索 | 通用工具代理安全；邻接参考 |
| OpenAlex 引用快照 | [6](https://openalex.org/W4405627542)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 3 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：LLM 使用工具与外部环境交互时，会出现哪些超出文本回答的安全失误？

**评测层级**：通用工具代理安全；邻接参考。

## 2. 怎么构建的

**核心场景与条目**：349 个交互环境、2,000 测试用例、8 类风险、10 种失败模式，包含信息泄漏、财产损失、物理后果及工具可用性等。

**实现与判分**：整合已有测试、去重和增补，统一环境格式并人工质检；用评分器评价多步工具交互，同时考察有用性与安全提示的效果。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470) | 2024 | 提出 | 349 个交互环境、2000 个测试用例；8 类风险、10 种失败模式 | 面向 LLM 作为智能体被部署后的新型安全挑战（工具使用、环境交互），构建 349 个交互环境与 2000 个测试用例，覆盖 8 类安全风险与 10 种常见失败模式。对 16 个流行 LLM 智能体的评测给出一个警示性结果：没有任何智能体安全分超过 60%。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：16 个被测代理均未达到 60% 安全分数；论文将问题归纳为鲁棒性和风险意识不足，提示单靠防御提示不够。

**适用边界**：其环境多数是软件／工具层，列入物理后果类别不代表运行了机器人动力学。适合借鉴 taxonomy 和安全／有用性双评价，不能直接当 VLA 物理安全分数。

## 5. 相关论文（均来自本调研表）

- [Agent-SafetyBench: Evaluating the Safety of LLM Agents](https://arxiv.org/abs/2412.14470)（2024；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

其环境多数是软件／工具层，列入物理后果类别不代表运行了机器人动力学。适合借鉴 taxonomy 和安全／有用性双评价，不能直接当 VLA 物理安全分数。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Zhexin Zhang, Shiyao Cui, Yida Lu, et al., ‘Agent-SafetyBench: Evaluating the Safety of LLM Agents,’ arXiv preprint, 2024, arXiv:2412.14470v2. [论文](https://arxiv.org/abs/2412.14470)；[核查正文](https://arxiv.org/html/2412.14470v2)。

**重点核查位置（章节主题）**：3.1 Risk Categories；3.2 Data Collection；3.3 Scorer；4 Experiments。

OpenAlex 被引次数：**[6](https://openalex.org/W4405627542)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/thu-coai/Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **6** 篇引文论文（清单保留被引最高的 6 篇）；arXiv 摘要命中 1 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/thu-coai/Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/thu-coai/Agent-SafetyBench) | https://raw.githubusercontent.com/thu-coai/Agent-SafetyBench/HEAD/README.md | stars 167，license MIT（开源许可证），最后推送 2025-08-11，保留文本 1811 字符（截断） |

**项目页显示**：GitHub repo（167 stars，MIT，2025-08-11 最后推送）：提供数据集、环境与代码，数据同时发布在 HuggingFace，README 给出 Quick Start 与 News 时间线。

**涉及领域**：软件代理（LLM agent）的多步工具交互；风险类别覆盖软件、数据、内容与文本化的物理后果，不含机器人动力学。

**测试目的与构建方法**：汇总并去重既有代理安全测试，统一为 16 类风险、8 类失败模式的环境集合，人工质检后用脚本化评分器同时判安全性与有用性。

**测试缺陷**：环境停在工具调用层，物理后果只是文本标签；评分器与任务模板强绑定，新工具难复用；安全／有用性权衡只在少量提示策略上验证。

**与具身智能安全的相关性**：直接测智能体安全（风险类别 × 失败模式），可作为具身代理“上层决策与工具使用”的邻接证据；不能替代关节级／接触级的物理安全评测。

**用这个 benchmark 测了什么**：论文测 16 个 LLM 代理，均未达到 60% 安全分数，问题归为鲁棒性与风险意识不足；SHE（2026）在此基准上做安全 harness 演化并报告提升；多篇 LLM 代理安全综述引用其分类法。

**本轮核查边界**：本轮只读 README 与仓库元数据，未运行任何环境。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **1 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| SHE: Trajectory-driven Safety Harness Evolution for LLM Agents（2026） | SHE（在多种 LLM 代理上做安全 harness 演化），对照静态 SafeHarness | 评测（安全 harness 演化前后对比） | Agent-SafetyBench 的风险达成率（ASR）与正常效用 | ASR 相比静态 SafeHarness 降低到 1/3.1（3.1× 降幅），同时正常效用提升 |

**原文片段（摘要）**：

- SHE: Trajectory-driven Safety Harness Evolution for LLM Agen…（2026，arXiv）：> achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 3 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **ASR** | Attack Success Rate | 攻击成功率 | 攻击达成目标的比例；与语音领域的“自动语音识别”缩写相同，看语境。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |

**本文最容易读错的地方**：
- **ASR**：把攻击成功率当成语音识别，或反过来。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| Agent-SafetyBench | 基准 | 通用工具代理安全；邻接参考 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）），不再重复解释。

<!-- glossary:end -->
