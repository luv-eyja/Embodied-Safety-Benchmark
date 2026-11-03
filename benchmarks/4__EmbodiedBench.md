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
| OpenAlex 引用快照 | [1](https://openalex.org/W4407590542)；2026-11-03 |

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

**原论文结果与成果**：24 个模型中，原论文最佳 GPT-4o 平均仅 28.9%；模型在高层任务较强，低层操作明显困难。成果是跨执行层级的标准化环境与能力诊断。

**适用边界**：它主要测能力，不是专门的安全约束基准；四种环境动作抽象不同，整体均值不能解释为真实机械臂安全成功率。模型结果是论文当时版本。

## 5. 相关论文（均来自本调研表）

- [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

它主要测能力，不是专门的安全约束基准；四种环境动作抽象不同，整体均值不能解释为真实机械臂安全成功率。模型结果是论文当时版本。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Rui Yang, Hanyang Chen, Junyu Zhang, et al., ‘EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents,’ arXiv preprint, 2025, arXiv:2502.09560v3. [论文](https://arxiv.org/abs/2502.09560)；[核查正文](https://arxiv.org/html/2502.09560v3)。

**重点核查位置（章节主题）**：4.1 High-level and Low-level Tasks；4.2 Data Collection；4.3 Agent Design；5.2 Benchmark Results。

OpenAlex 被引次数：**[1](https://openalex.org/W4407590542)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://embodiedbench.github.io](https://embodiedbench.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
