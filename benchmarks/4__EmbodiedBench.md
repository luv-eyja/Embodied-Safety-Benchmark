# EmbodiedBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：原分类曾置于安全组，正文主要评估通用具身能力。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：MLLM 具身智能体六能力  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://embodiedbench.github.io](https://embodiedbench.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › Instruction Understanding |
| 应用领域 | 未标注 |
| 被测对象 | 视觉具身代理能力评测 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 1128 个任务 / 4 个环境；6 个能力子集 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 1,128 测试任务，EB-ALFRED、EB-Habitat、EB-Navigation、EB-Manipulation 四类环境；六个能力子集覆盖常识、复杂指令、空间、视觉和长时程等。 |
| 执行环境线索 | 视觉具身代理能力评测 |
| OpenAlex 引用快照 | [1](https://openalex.org/W4407590542)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 5 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：多模态模型能否将看到的场景转化成可执行行动，低层空间操作与高层语义规划有何差距？

**评测层级**：视觉具身代理能力评测。

## 2. 怎么构建的

**核心场景与条目**：1,128 测试任务，EB-ALFRED、EB-Habitat、EB-Navigation、EB-Manipulation 四类环境；六个能力子集覆盖常识、复杂指令、空间、视觉和长时程等。

**实现与判分**：统一视觉代理输入、历史和结构化动作输出；高层环境使用离散技能，导航和操作采用更细粒度动作，并提供执行有效性反馈及语言／视觉消融。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560) | 2025 | 提出 | 1128 个任务 / 4 个环境；6 个能力子集 | 针对 MLLM 具身智能体缺乏综合评测框架的问题，构建覆盖 4 个环境、1128 个测试任务的基准：从家务等高层语义任务到导航与操作等原子动作级任务，并设 6 个精选子集分别考察常识推理、复杂指令理解、空间意识、视觉感知与长期规划等核心能力。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：24 个模型中，原论文最佳 GPT-4o（LLM 模型） 平均仅 28.9%；模型在高层任务较强，低层操作明显困难。成果是跨执行层级的标准化环境与能力诊断。

**适用边界**：它主要测能力，不是专门的安全约束基准；四种环境动作抽象不同，整体均值不能解释为真实机械臂安全成功率。模型结果是论文当时版本。

## 5. 相关论文（均来自本调研表）

- [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

它主要测能力，不是专门的安全约束基准；四种环境动作抽象不同，整体均值不能解释为真实机械臂安全成功率。模型结果是论文当时版本。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Rui Yang, Hanyang Chen, Junyu Zhang, et al., ‘EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents,’ arXiv preprint, 2025, arXiv:2502.09560v3. [论文](https://arxiv.org/abs/2502.09560)；[核查正文](https://arxiv.org/html/2502.09560v3)。

**重点核查位置（章节主题）**：4.1 High-level and Low-level Tasks；4.2 Data Collection；4.3 Agent Design；5.2 Benchmark Results。

OpenAlex 被引次数：**[1](https://openalex.org/W4407590542)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://embodiedbench.github.io](https://embodiedbench.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **1** 篇引文论文（清单保留被引最高的 1 篇）；arXiv 摘要命中 6 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://embodiedbench.github.io](https://embodiedbench.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://embodiedbench.github.io) | https://embodiedbench.github.io | — |

**项目页显示**：项目页 https://embodiedbench.github.io 抓取后无有效文本（依赖前端渲染），本轮只能以论文与卡片记录为准。

**涉及领域**：视觉驱动具身代理的综合能力评测，跨 4 类环境（高层家务、导航、操作等），面向多模态大模型。

**测试目的与构建方法**：统一视觉代理输入、历史与结构化动作输出；高层环境用离散技能，导航与操作采用更细粒度动作，并提供执行有效性反馈与语言／视觉消融。

**测试缺陷**：主要测能力而非安全约束；四类环境的动作抽象不同，整体均值不能解释为真实机械臂安全成功率；模型结果对应当年版本；项目页无静态文本，复现入口需 JS 渲染。

**与具身智能安全的相关性**：较弱：它的价值是给出“能力门槛”与失败模式（低层操作明显弱于高层），为安全评测提供对照；本身不含风险约束或违规判罚。

**用这个 benchmark 测了什么**：24 个模型中，原论文最佳 GPT-4o 平均仅 28.9%，高层任务较强、低层操作明显困难；后续有 MemCompiler 等在此基准上评测记忆机制，Robocskbench 引用其能力划分。

**本轮核查边界**：项目页未取到内容，代码／数据可用性未核实。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **6 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| RoboMemory: A Brain-inspired Multi-memory Agentic Framework（2025） | RoboMemory，实例化为 Qwen2.5-VL（VLM 模型）-72B-Ins | 评测（加记忆框架后的增益） | EmbodiedBench 全部子集，与强基线及闭源 SOTA 比较 | 平均成功率比强基线高 26.5%，并超过闭源 SOTA（Claude（LLM 模型） 系列） |
| RoboGPT-R1: Enhancing Robot Task Planning with Reinforcement Learning（2025） | RoboGPT-R1，在 Qwen2.5-VL-3B 上训练 | 强化学习训练后评测（小模型 vs 大模型） | EmbodiedBench 上的任务规划成功率 | 比 GPT-4o-mini 高 21.33%，比基于 Qwen2.5-VL-7B 的其他工作高 20.33% |
| RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Age…（2026） | RoboFoundry，基线为 GPT-5.5（LLM 模型） | 评测（系统级演化前后对比） | EmbodiedBench 总体表现 | 相对 GPT-5.5 提升 27.8%，称达到 SOTA |
| MemCompiler: Compile, Don't Inject — State-Conditioned Memory（2026） | MemCompiler，在多种开源主干上 | 评测（有／无记忆对照） | AlfWorld、EmbodiedBench、ScienceWorld | 相比无记忆一致提升（最高 +129%），并接近前沿闭源系统 |
| MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents（2026） | 两个表现较弱的 MLLM + MemCtrl 记忆控制器 | 评测（增强前后对比，多子集） | EmbodiedBench 多个子集 | 平均提升约 16%，部分子集超过 20% |
| Look Before You Move: Agent-Interface-Aligned Supervision（2026） | AIDA 监督流程 | 评测（导航子集） | EmbodiedBench 的导航子集 | 摘要称验证了该流程对导航任务的可用性，未给数值 |

**原文片段（摘要）**：

- RoboMemory: A Brain-inspired Multi-memory Agentic Framework（2025，arXiv）：> instantiated with Qwen2.5-VL-72B-Ins, improves the average success rate by 26.5% over its strong baseline
- RoboGPT-R1: Enhancing Robot Task Planning with Reinforcement…（2025，arXiv）：> significantly outperforms the larger-scale model, GPT-4o-mini, by 21.33% … on the EmbodiedBench benchmark
- RoboFoundry: System-as-Policy Evolution for Self-Learning Em…（2026，arXiv）：> On EmbodiedBench, RoboFoundry achieves state-of-the-art performance, notably improving GPT-5.5 by 27.8%
- MemCompiler: Compile, Don't Inject — State-Conditioned Memor…（2026，arXiv）：> Across Alf World, EmbodiedBench, and ScienceWorld, MemCompiler consistently improves over no-memory … (up to +129%)
- MemCtrl: Using MLLMs as Active Memory Controllers on Embodie…（2026，arXiv）：> μ-augmented MLLMs show an improvement of around 16% on average, with over 20% on…
- Look Before You Move: Agent-Interface-Aligned Supervision（2026，arXiv）：> Applying AIDA to a navigation subset of EmbodiedBench further demonstrates the pipeline's utility

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 5 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **MLLM** | Multimodal Large Language Model | 多模态大模型 | VLM 的另一种叫法，强调多模态输入。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **ablation** | ablation study | 消融实验 | 逐个去掉或替换模块，看性能变化，用来归因。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| EmbodiedBench | 基准 | 跨环境具身代理能力基准 |

另有 4 个专有名称已在正文首次出现处加括号标注类别（例如 GPT-4o（LLM 模型）、Qwen2.5-VL（VLM 模型）、Claude（LLM 模型）、GPT-5.5（LLM 模型）），不再重复解释。

<!-- glossary:end -->
