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
| OpenAlex 引用快照 | [0](https://openalex.org/W7221756428)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 2 个缩写／技术词，并标出 3 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Xupeng Zhang, Yantai Yang, Chang Guo, et al., ‘Exploring the Limits of Combinatorial Generalization in Embodied Manipulation,’ arXiv preprint, 2026, arXiv:2610.15425v1. [论文](https://arxiv.org/abs/2610.15425)；[核查正文](https://arxiv.org/html/2610.15425v1)。

**重点核查位置（章节主题）**：3.1 Benchmark；3.2 Hierarchical Evaluation；4.1；4.2；5 Analysis。

OpenAlex 被引次数：**[0](https://openalex.org/W7221756428)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/AutoLab-SAI-SJTU/RoboCombine](https://github.com/AutoLab-SAI-SJTU/RoboCombine)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/AutoLab-SAI-SJTU/RoboCombine](https://github.com/AutoLab-SAI-SJTU/RoboCombine)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/AutoLab-SAI-SJTU/RoboCombine) | https://raw.githubusercontent.com/AutoLab-SAI-SJTU/RoboCombine/HEAD/README.md | stars 10，license MIT（开源许可证），最后推送 2026-10-15，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/AutoLab-SAI-SJTU/RoboCombine（10 stars，MIT，2026-10-15 推送）README 明确公开范围：19 个组合任务、3 条轨道、2 个策略适配器，2026-10 发布评测代码。

**涉及领域**：具身操作的组合泛化；19 个组合任务、3 条轨道（full_inst、oracle_hse、ordered_hse）。

**测试目的与构建方法**：用 RoboCombine 框架比较 Oracle-HSE、Ordered-HSE 与整段指令执行，把高层调度、低层技能与交接状态分开诊断；用 PRTI 扩展原子技能的初始状态覆盖。

**测试缺陷**：仓库短名 RoboComb 对应正文 RoboCombine；组合微调与只用原子示范是不同的训练设定；oracle 交接下的成绩不是端到端自主能力；只支持 Motus、pi05 两种适配器。

**与具身智能安全的相关性**：间接：组合任务的失败集中在“交接状态”，这类失败在真实流水线里往往表现为碰撞或掉落，但基准只记成功。

**用这个 benchmark 测了什么**：有限组合任务微调在已见组合达 40%，未见重组仅 7.7%；瓶颈不只是任务规划，还包括交接状态分布；NeurIPS（会议／期刊） 2026 接收。

**本轮核查边界**：只读 README 的能力表，未跑评测代码。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 2 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboComb | 基准 | 原子技能组合泛化 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）、NeurIPS（会议／期刊）），不再重复解释。

<!-- glossary:end -->
