# SafeAgentBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：具身交互环境下的安全任务规划测试。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：安全任务规划  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/shengyin1224/SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Cascading Risks |
| 应用领域 | 未标注 |
| 被测对象 | 交互仿真中的安全任务规划 |
| 历史关键词标签（未重新统计） | 任务能力 |
| 评测维度/指标 | 安全任务规划；危险场景下的计划合规率 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 750 个任务、10 类危险、三种任务类型；SafeAgentEnv 提供 17 个高层动作和低层执行器，支持九种代理基线。 |
| 执行环境线索 | 交互仿真中的安全任务规划 |
| OpenAlex 引用快照 | [2](https://openalex.org/W4405562840)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 3 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：代理对明确危险与正常长任务中的隐含风险，是否有足够的主动拒绝和安全规划能力？

**评测层级**：交互仿真中的安全任务规划。

## 2. 怎么构建的

**核心场景与条目**：750 个任务、10 类危险、三种任务类型；SafeAgentEnv 提供 17 个高层动作和低层执行器，支持九种代理基线。

**实现与判分**：任务生成后筛选标注，在交互环境执行高层计划；从执行结果与语义两方面评价，分别比较详细、抽象及长时程任务。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178) | 2024 | 提出 | 安全任务规划；危险场景下的计划合规率 | 面向具身 LLM 智能体的安全任务规划评测：在危险场景中检验智能体生成的执行计划是否满足安全要求，是「规划层安全」评测的代表性工作之一，常与 AGENTSAFE、IS-Bench 等一起作为具身智能体安全评测的基线集合。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：对详细危险任务，最有安全意识的基线拒绝率也只有 10%；仅替换底座 LLM 没有稳定解决安全意识不足。成果是可执行危险任务集与统一环境。

**适用边界**：高层动作接口和控制器可能承担部分运动能力，不能与端到端关节 VLA 同分比较；拒绝率低不等于所有任务都成功造成物理后果。

## 5. 相关论文（均来自本调研表）

- [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)（2024；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

高层动作接口和控制器可能承担部分运动能力，不能与端到端关节 VLA 同分比较；拒绝率低不等于所有任务都成功造成物理后果。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Sheng Yin, Xianghe Pang, Yuanzhuo Ding, et al., ‘SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents,’ arXiv preprint, 2024, arXiv:2412.13178v5. [论文](https://arxiv.org/abs/2412.13178)；[核查正文](https://arxiv.org/html/2412.13178v5)。

**重点核查位置（章节主题）**：3 Dataset；4.1 Embodied Environment；4.2 Evaluation Methods；5.1；5.3；5.4。

OpenAlex 被引次数：**[2](https://openalex.org/W4405562840)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/shengyin1224/SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **2** 篇引文论文（清单保留被引最高的 2 篇）；arXiv 摘要命中 3 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/shengyin1224/SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/shengyin1224/SafeAgentBench) | https://raw.githubusercontent.com/shengyin1224/SafeAgentBench/HEAD/README.md | stars 79，最后推送 2025-02-25，保留文本 4036 字符（截断） |

**项目页显示**：GitHub https://github.com/shengyin1224/SafeAgentBench（79 stars，2025-02-25 推送）README 明确 750 个任务、可执行的危险任务集与统一环境，并说明动机是“代理能完美执行危险任务”。

**涉及领域**：具身 LLM 代理的安全任务规划；750 个危险任务、语义与执行两层评价。

**测试目的与构建方法**：任务生成后筛选标注，在交互环境中执行高层计划；从执行结果与语义两方面评价，分别比较详细、抽象与长时程任务。

**测试缺陷**：高层动作接口与控制器可能承担部分运动能力，不能与端到端关节 VLA 同分比较；拒绝率低不等于所有任务都真造成物理后果；底座 LLM 换模型并不能稳定改善安全意识。

**与具身智能安全的相关性**：直接测“会不会规划危险任务”，属规划层安全；对家庭服务机器人有意义，但不覆盖执行时的碰撞与力。

**用这个 benchmark 测了什么**：对详细危险任务，最有安全意识的基线拒绝率也只有 10%；仅替换底座 LLM 没有稳定解决安全意识不足。下游有语音误听（ASR 错误）研究把它与其他安全基准组合评测。

**本轮核查边界**：只读 README 的组成说明，未运行环境。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **3 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| ConceptBot: Enhancing Robot's Autonomy through Task Decomposition（2025） | ConceptBot（任务分解） | 评测（与次优基线对比） | SafeAgentBench 总体分数 | 总分 80%，次优基线 46% |
| NEXUS: Learning Safety Constraints and Action Models for Safe Embodied…（2026） | NEXUS（安全约束 + 动作模型） | 评测（安全—完成权衡 + 越狱压力测试） | SafeAgentBench 评测集：安全任务完成、危险任务拒绝、越狱下违规率 | 称取得最佳整体权衡，并在越狱攻击下维持低违规率；摘要未给数值 |
| When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled E…（2026） | EAI 模型（受 ASR 错误影响） | 输入扰动注入（把语音识别错误叠到基准上） | 模拟 ASR 错误 + SafeAgentBench 与 POEX 的危险任务 | 测出 ASR 错误如何降低安全性；摘要未给数值 |

**原文片段（摘要）**：

- ConceptBot: Enhancing Robot's Autonomy through Task Decompos…（2025，arXiv）：> On SafeAgentBench, ConceptBot achieved an overall score of 80% (versus 46% for the next-best baseline)
- NEXUS: Learning Safety Constraints and Action Models for Saf…（2026，arXiv）：> NEXUS achieves the best overall trade-off between safetask completion and unsafe-task refusal
- When Robots Mishear Us: Mapping the Safety Risks of Voice-Co…（2026，arXiv）：> We simulate ASR errors and combine them with existing safety benchmarks (SafeAgentBench and POEX)

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
| SafeAgentBench | 基准 | 交互仿真中的安全任务规划 |
| IS-Bench | 基准 | VLM 代理交互安全基准 |

<!-- glossary:end -->
