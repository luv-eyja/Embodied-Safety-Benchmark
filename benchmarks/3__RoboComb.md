# RoboComb

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：RoboCombine 的技能组合与交接评测；仓库保留 RoboComb 短名。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：技能组合泛化  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/AutoLab-SAI-SJTU/RoboCombine](https://github.com/AutoLab-SAI-SJTU/RoboCombine)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Exploring the Limits of Combinatorial Generalization in Embodied Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Task Planning |
| 应用领域 | 未标注 |
| 被测对象 | 原子技能组合泛化 |
| 历史关键词标签（未重新统计） | 语义/指令安全、失败恢复、任务能力 |
| 评测维度/指标 | 有序成功率（覆盖组合 vs 重组组合）；HSE 诊断框架 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 以原子技能重组长任务，区分训练可见组合与未见重组；特别关注上一个技能留下的状态与下一个技能训练起点的不一致。 |
| 执行环境线索 | 原子技能组合泛化 |
| 来源审计 | [Exploring the Limits of Combinatorial Generalization in Embodied Manipulation](https://arxiv.org/abs/2610.15425)；same_paper_in_registry |
| 来源核验依据 | 摘要实际使用名称 RoboCombine；本库正则将其收录为 RoboComb，属于名称缩写/变体。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221756428)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：已经学会的原子技能，能否在未见过的组合中可靠衔接？

**评测层级**：原子技能组合泛化。

## 2. 怎么构建的

**核心场景与条目**：以原子技能重组长任务，区分训练可见组合与未见重组；特别关注上一个技能留下的状态与下一个技能训练起点的不一致。

**实现与判分**：RoboCombine 框架比较 Oracle-HSE、Ordered-HSE 和整段指令执行，将高层调度与低层技能、交接状态分开诊断；用 PRTI 扩展原子技能的初始状态覆盖。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Exploring the Limits of Combinatorial Generalization in Embodied Manipulation](https://arxiv.org/abs/2610.15425) | 2026 | 提出 | 有序成功率（覆盖组合 vs 重组组合）；HSE 诊断框架 | 在受控研究中，让完整指令训练只在有限的技能组合序列上进行，结果覆盖组合的有序成功率为 40.0%，而重组组合仅 7.7%——说明模型记忆了序列模板而非真正重组技能。作者提出分层子任务执行（HSE）诊断框架，通过规划器、触发器与策略共享的模块化接口暴露技能重组问题，把长时程失败分解为可分离的失败模式，并构建 RoboComb 基准。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：有限组合任务微调在已见组合上达到 40%，未见重组仅 7.7%；提示主要瓶颈不只是任务规划，还包括交接状态分布。

**适用边界**：仓库短名 RoboComb 对应正文 RoboCombine。组合微调与只用原子示范是不同训练设定；使用 oracle 交接的成绩不是端到端自主能力。

## 5. 相关论文（均来自本调研表）

- [Exploring the Limits of Combinatorial Generalization in Embodied Manipulation](https://arxiv.org/abs/2610.15425)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

仓库短名 RoboComb 对应正文 RoboCombine。组合微调与只用原子示范是不同训练设定；使用 oracle 交接的成绩不是端到端自主能力。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Xupeng Zhang, Yantai Yang, Chang Guo, et al., ‘Exploring the Limits of Combinatorial Generalization in Embodied Manipulation,’ arXiv preprint, 2026, arXiv:2610.15425v1. [论文](https://arxiv.org/abs/2610.15425)；[核查正文](https://arxiv.org/html/2610.15425v1)。

**重点核查位置（章节主题）**：3.1 Benchmark；3.2 Hierarchical Evaluation；4.1；4.2；5 Analysis。

OpenAlex 被引次数：**[0](https://openalex.org/W7221756428)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/AutoLab-SAI-SJTU/RoboCombine](https://github.com/AutoLab-SAI-SJTU/RoboCombine)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
