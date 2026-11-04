# MSK-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：生理控制与鲁棒性测试，不因身体接触直接标安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：全身肌肉骨骼控制  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://zzongzheng0918.github.io/MSK-Bench](https://zzongzheng0918.github.io/MSK-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 全身控制 |
| 被测对象 | 肌肉驱动全身控制 |
| 历史关键词标签（未重新统计） | 物理/接触安全、实时/治理 |
| 评测维度/指标 | 22 个全身任务、3 个递进难度类；任务/范式/生理指标 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 22 个任务分六项姿态稳定、六项移动、十项环境交互：站立、平衡、行走、跑跳、楼梯、跨障、开门、接物等。 |
| 执行环境线索 | 肌肉驱动全身控制 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214208713)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 2 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：控制器能否在高维、延迟且冗余的肌肉系统中完成任务，并产生合理的生理活动？

**评测层级**：肌肉驱动全身控制。

## 2. 怎么构建的

**核心场景与条目**：22 个任务分六项姿态稳定、六项移动、十项环境交互：站立、平衡、行走、跑跳、楼梯、跨障、开门、接物等。

**实现与判分**：统一任务和扰动，比较奖励式 RL、代理奖励调优、潜动作、模仿先验与残差适配；除成功率还报告激活代价、关节平滑及肌电包络相似度。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics](https://arxiv.org/abs/2609.26872) | 2026 | 提出 | 22 个全身任务、3 个递进难度类；任务/范式/生理指标 | 指出肌肉骨骼（MSK）人形提供了生理上更真实的全身运动控制载体，但高维肌肉驱动、延迟激活动力学与冗余肌腱结构使学习远难于力矩驱动的人形；现有 MSK 基准分散在步态、假肢、灵巧手或特定挑战赛道，全身肌肉驱动控制缺乏标准化任务、方法与指标的评估。基准含 22 个全身运动控制任务，分为姿态稳定、常见运动等三个递进难度类别。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文用从诊断到残差适配的案例展示，任务完成改善和肌电一致性必须分别验证；生理指标能揭示仅看奖励／成功看不到的问题。

**适用边界**：残差案例同时调整目标与参考运动时序，收益不能单独归因于残差模块。肌肉仿真不是人类临床实验，也不是普通关节力矩控制的同条件榜单。

## 5. 相关论文（均来自本调研表）

- [MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics](https://arxiv.org/abs/2609.26872)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

残差案例同时调整目标与参考运动时序，收益不能单独归因于残差模块。肌肉仿真不是人类临床实验，也不是普通关节力矩控制的同条件榜单。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Mengtao Ou, Zongzheng Zhang, Zhenghao Xiao, et al., ‘MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics,’ arXiv preprint, 2026, arXiv:2609.26872v1. [论文](https://arxiv.org/abs/2609.26872)；[核查正文](https://arxiv.org/html/2609.26872v1)。

**重点核查位置（章节主题）**：III MSK-Bench；IV Residual Adaptation Case Study；Appendix A-B Evaluation Details。

OpenAlex 被引次数：**[0](https://openalex.org/W7214208713)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://zzongzheng0918.github.io/MSK-Bench](https://zzongzheng0918.github.io/MSK-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://zzongzheng0918.github.io/MSK-Bench](https://zzongzheng0918.github.io/MSK-Bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://zzongzheng0918.github.io/MSK-Bench) | https://zzongzheng0918.github.io/MSK-Bench | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://zzongzheng0918.github.io/MSK-Bench 定位为“全身肌肉驱动类人控制基准”，作者来自清华 AIR、港大等。

**涉及领域**：全身肌肉骨骼驱动的类人控制；跨任务、控制范式与生理指标。

**测试目的与构建方法**：统一任务与扰动，比较奖励式 RL、代理奖励调优、潜动作、模仿先验与残差适配；除成功率外，报告激活代价、关节平滑度与肌电包络相似度。

**测试缺陷**：残差案例同时调整目标与参考运动时序，收益不能单独归因于残差模块；肌肉仿真不是临床实验，也不能与关节力矩控制同条件比较；生理指标的定义依赖所选肌骨模型。

**与具身智能安全的相关性**：间接但独特：肌肉激活、关节平滑与能耗是“生理代价”类安全指标，可用于评估动作是否对硬件／人体友好；基准不设碰撞或损伤判罚。

**用这个 benchmark 测了什么**：论文以“诊断→残差适配”的案例展示：任务完成改善与肌电一致性必须分别验证，生理指标能揭示只看奖励／成功看不到的问题。

**本轮核查边界**：只读项目页标题与摘要，未取到代码或数据入口。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **RL** | Reinforcement Learning | 强化学习 | 用奖励信号优化策略，区别于用示范做监督学习。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| MSK-Bench | 基准 | 肌肉驱动全身控制 |

<!-- glossary:end -->
