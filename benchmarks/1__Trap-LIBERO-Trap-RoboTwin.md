# Trap-LIBERO / Trap-RoboTwin

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：安全方法附带两套具名受控诊断任务；不概括为普通鲁棒性。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：配置化失败后门  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://john-liua.github.io/TrapVLA](https://john-liua.github.io/TrapVLA)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | VLA 定向失效诊断／安全研究 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、对抗/后门安全、失败恢复 |
| 评测维度/指标 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 |
| 基础平台线索 | LIBERO、RoboTwin |
| 规模线索 | 在 LIBERO 与 RoboTwin 中分别考察过早闭合、抓取偏移、过早释放及释放偏移等失效类别，并提供模拟及有限真机分析。 |
| 执行环境线索 | VLA 定向失效诊断／安全研究 |
| 来源审计 | [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明构建 Trap-LIBERO 与 Trap-RoboTwin。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7204530163)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 2 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：干净任务分数较高时，是否仍可能隐藏只在特定条件下出现的定向操作失败？

**评测层级**：VLA 定向失效诊断／安全研究。

## 2. 怎么构建的

**核心场景与条目**：在 LIBERO 与 RoboTwin 中分别考察过早闭合、抓取偏移、过早释放及释放偏移等失效类别，并提供模拟及有限真机分析。

**实现与判分**：论文将正常任务效用与特定失效目标的达成程度分开统计，结合轨迹和动作层信号检查失效是否符合指定类型；本条仅记录评测层设计。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578) | 2026 | 提出 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 | 提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文展示干净成功率保持较高时仍可出现定向失效，说明标准成功率不足以筛查策略完整性；提供两套受控安全评测任务。

**适用边界**：论文结果依赖特定威胁假设、模型与任务；不能推断任意部署模型都存在此类问题。正常成功和配置失效指标不是同一分母或同一目标。

## 5. 相关论文（均来自本调研表）

- [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

论文结果依赖特定威胁假设、模型与任务；不能推断任意部署模型都存在此类问题。正常成功和配置失效指标不是同一分母或同一目标。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, et al., ‘TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes,’ arXiv preprint, 2026, arXiv:2608.26578v1. [论文](https://arxiv.org/abs/2608.26578)；[核查正文](https://arxiv.org/html/2608.26578v1)。

**重点核查位置（章节主题）**：Task Definition；Evaluation Metrics；Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7204530163)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://john-liua.github.io/TrapVLA](https://john-liua.github.io/TrapVLA)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://john-liua.github.io/TrapVLA](https://john-liua.github.io/TrapVLA)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://john-liua.github.io/TrapVLA) | https://john-liua.github.io/TrapVLA | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://john-liua.github.io/TrapVLA 标注 Code & Dataset “Coming soon”，页面主题为“Stealthy textual triggers / Configured robot failures”。

**涉及领域**：VLA 的后门攻击与失效注入；在 LIBERO 与 RoboTwin 上构造文本触发器与指定失效模式。

**测试目的与构建方法**：把“正常任务效用”与“特定失效目标的达成程度”分开统计，结合轨迹与动作层信号检查失效是否符合指定类型；提供两套受控评测任务与攻击方法 TrapVLA。

**测试缺陷**：结果依赖特定威胁假设、模型与任务，不能推断任意部署模型都有此问题；正常成功与配置失效指标不是同一分母；代码与数据标注“Coming soon”。

**与具身智能安全的相关性**：直接：这是“策略完整性”问题——干净成功率很高仍可能被触发器操纵，标准成功率筛查不出来；属安全评测中少见的攻防视角。

**用这个 benchmark 测了什么**：论文展示干净成功率保持较高时仍可出现定向失效，说明标准成功率不足以筛查完整性；两套任务分别建立在 LIBERO 与 RoboTwin 上。

**本轮核查边界**：代码／数据未发布，无法核实攻击实现与复现条件。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| Trap-LIBERO / Trap-RoboTwin | 基准 | VLA 定向失效诊断／安全研究 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |
| TrapVLA | 基准 | VLA 后门／失效注入方法与其基准 |

<!-- glossary:end -->
