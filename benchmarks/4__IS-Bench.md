# IS-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：显式风险及安全动作顺序，是安全规划基准。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：交互安全（过程导向）  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/AI45Lab/IS-Bench](https://github.com/AI45Lab/IS-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 交互过程中的安全规划 |
| 历史关键词标签（未重新统计） | 物理/接触安全、任务能力 |
| 评测维度/指标 | 161 个场景 / 388 个安全风险；过程导向评测（风险感知与缓解步骤顺序） |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 161 个场景、388 个独特风险，采用多视角视觉交互；18 种原子技能，涵盖操作前防范和操作后处置。 |
| 执行环境线索 | 交互过程中的安全规划 |
| OpenAlex 引用快照 | [2](https://openalex.org/W7138977141)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 3 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：代理能否看到行动引入的新危险，并在正确的先后顺序执行防范和补救？

**评测层级**：交互过程中的安全规划。

## 2. 怎么构建的

**核心场景与条目**：161 个场景、388 个独特风险，采用多视角视觉交互；18 种原子技能，涵盖操作前防范和操作后处置。

**实现与判分**：逐步执行动作并更新图像及历史，按风险相关步骤的前后关系核验安全行为；提供不同级别提醒和安全思维链，分开报告任务 SR、安全 SSR 与风险处置召回。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402) | 2025 | 提出 | 161 个场景 / 388 个安全风险；过程导向评测（风险感知与缓解步骤顺序） | 指出静态、非交互的评测范式无法评估交互环境中的风险：它无法模拟由智能体自身动作引发的动态风险，且依赖忽略中间步骤的事后评判。该基准提出「交互安全」——智能体感知涌现风险并按正确程序顺序执行缓解步骤的能力——含 161 个场景、388 个具体安全风险，并采用过程导向的评测核查中间步骤，发表于 AAAI（会议／期刊） 2026。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：L1 条件下 GPT-4o（LLM 模型） 的任务 SR 为 81.3%，SSR 只有 33.8%；增强安全思维链能改善风险处置，但可能牺牲任务完成。

**适用边界**：提醒等级与输入场景表示不同会显著改变结果；不能拿有具体安全提示的设置与无提示设置直接排名。终点无事故不代表过程满足顺序要求。

## 5. 相关论文（均来自本调研表）

- [IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks](https://arxiv.org/abs/2506.16402)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

提醒等级与输入场景表示不同会显著改变结果；不能拿有具体安全提示的设置与无提示设置直接排名。终点无事故不代表过程满足顺序要求。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Xiaoya Lu, Zeren Chen, Xuhao Hu, et al., ‘IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks,’ arXiv preprint, 2025, arXiv:2506.16402v3. [论文](https://arxiv.org/abs/2506.16402)；[核查正文](https://arxiv.org/html/2506.16402v3)。

**重点核查位置（章节主题）**：Data Generation Pipeline；Evaluation Framework；Main Results；Visual-Centric Ablations。

OpenAlex 被引次数：**[2](https://openalex.org/W7138977141)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/AI45Lab/IS-Bench](https://github.com/AI45Lab/IS-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **2** 篇引文论文（清单保留被引最高的 2 篇）；arXiv 摘要检索因名称歧义不作计数。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/AI45Lab/IS-Bench](https://github.com/AI45Lab/IS-Bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/AI45Lab/IS-Bench) | https://raw.githubusercontent.com/AI45Lab/IS-Bench/HEAD/README.md | stars 56，最后推送 2025-11-24，保留文本 4184 字符（截断） |

**项目页显示**：GitHub https://github.com/AI45Lab/IS-Bench（56 stars，2025-11-24 推送）README 记录 AAAI 2025 接收、2025-07 代码与数据集发布，并声明“代码整理中”。

**涉及领域**：VLM 驱动具身代理在日常家庭任务中的“交互安全”；强调动作会改变风险状态。

**测试目的与构建方法**：逐步执行动作并更新图像与历史，按风险相关步骤的前后关系核验安全行为；提供不同级别提醒与安全思维链，分开报告任务 SR、安全 SSR 与风险处置召回。

**测试缺陷**：提醒等级与场景表示不同会显著改变结果，有提示与无提示设置不可直接排名；终点无事故不代表过程满足顺序要求；依赖 VLM 作被测评与裁判，存在闭环偏置。

**与具身智能安全的相关性**：直接测交互安全：危险是否由代理自己的动作引发、能否被及时处置。它是“动态风险”而非静态图文安全，但仍在图像—技能层，不涉及力。

**用这个 benchmark 测了什么**：L1 条件下 GPT-4o 的任务 SR 81.3% 而 SSR 仅 33.8%；加安全思维链能改善风险处置但可能牺牲任务完成——即安全与能力存在权衡。下游有 HomeGuard 与一篇跨层安全综述引用。

**本轮核查边界**：README 自述代码仍在整理，实际可运行性未验证。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮取得引文 2 篇、arXiv 摘要命中 0 篇，但摘要里没有出现能判读用法的句子（可能只有题名提及或无摘要）。详见第 7 节的记录。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 6 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **SSR** | Safe Success Rate | 安全成功率 | 既完成任务又没违规的 episode ÷ 全部 episode。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **L0** | difficulty level L0–L3 | L0–L3 难度档 | 基准自定义的难度阶梯：常见是 L0 干净、L1 加扰动、L2 更强扰动或结构变化，L3 更难。 |
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| IS-Bench | 基准 | VLM 代理交互安全基准 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 AAAI（会议／期刊）、GPT-4o（LLM 模型）），不再重复解释。

<!-- glossary:end -->
