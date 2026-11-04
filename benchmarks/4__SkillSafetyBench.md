# SkillSafetyBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；软件代理邻接研究；目标：能力、安全。
> **分类依据**：软件技能包的安全任务集，不是机器人技能控制。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：技能攻击面  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/AI45Lab/skill-safety-bench](https://github.com/AI45Lab/skill-safety-bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Tool Use and Skill |
| 应用领域 | 技能攻击面 |
| 被测对象 | 技能型软件代理安全；邻接参考 |
| 历史关键词标签（未重新统计） | 对抗/后门安全 |
| 评测维度/指标 | 155 个对抗案例 / 47 个任务 / 6 个风险域 / 30 个安全类别 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 47 个任务、155 个风险案例、六域和 30 个安全类别；使用多种命令行代理和模型组合。 |
| 执行环境线索 | 技能型软件代理安全；邻接参考 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7161027243)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 2 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：用户任务正常时，代理是否会过度信任技能说明及本地工作流材料，从而做出越界行为？

**评测层级**：技能型软件代理安全；邻接参考。

## 2. 怎么构建的

**核心场景与条目**：47 个任务、155 个风险案例、六域和 30 个安全类别；使用多种命令行代理和模型组合。

**实现与判分**：每个案例附可执行任务环境及独立规则验证器，把正常任务完成与风险行为分开评分；比较的是代理框架和模型的组合，而不仅底座模型。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces](https://arxiv.org/abs/2605.12015) | 2026 | 提出 | 155 个对抗案例 / 47 个任务 / 6 个风险域 / 30 个安全类别 | 指出可复用技能正成为扩展 LLM 智能体的常见接口，把过程性指引与文件、工具、记忆和执行环境的访问打包在一起；这种模块化引入了既有安全评测大量遗漏的攻击面——即便用户请求完全良性，不安全影响也可能藏在技能指引、本地工件或执行环境文件中，把智能体导向不安全动作。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：主表同一 GLM-5.1 在两种代理框架下的风险达成率分别为 50.3% 和 33.5%，显示框架上下文有影响，但该对照不足以孤立解释具体机制。

**适用边界**：这里的 skill 是软件代理技能包，不是机器人运动技能。风险达成与任务成功可同时发生，安全与效用不能用一个数字替代。

## 5. 相关论文（均来自本调研表）

- [SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces](https://arxiv.org/abs/2605.12015)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这里的 skill 是软件代理技能包，不是机器人运动技能。风险达成与任务成功可同时发生，安全与效用不能用一个数字替代。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Chang Jin, An Wang, Zeming Wei, et al., ‘SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces,’ arXiv preprint, 2026, arXiv:2605.12015v3. [论文](https://arxiv.org/abs/2605.12015)；[核查正文](https://arxiv.org/html/2605.12015v3)。

**重点核查位置（章节主题）**：3 Benchmark Overview；4 Benchmark Construction；5.3 Metrics；5.4 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7161027243)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/AI45Lab/skill-safety-bench](https://github.com/AI45Lab/skill-safety-bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/AI45Lab/skill-safety-bench](https://github.com/AI45Lab/skill-safety-bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/AI45Lab/skill-safety-bench) | https://raw.githubusercontent.com/AI45Lab/skill-safety-bench/HEAD/README.md | stars 33，license Apache-2.0（开源许可证），最后推送 2026-05-14，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/AI45Lab/skill-safety-bench（33 stars，Apache-2.0，2026-05-14 推送）自称“fully materialized benchmark”，并把案例浏览器、排行榜与实验分析放在独立网站。

**涉及领域**：软件代理的“技能面”攻击安全；把攻击放在技能包、脚本、模板与工作区文件中。

**测试目的与构建方法**：每个案例保持用户任务普通，把攻击置于代理执行时会查阅的本地技能／辅助文件；每个案例附可执行任务环境与独立规则验证器，把正常任务完成与风险行为分开评分。

**测试缺陷**：这里的 skill 是软件代理技能包，不是机器人运动技能；风险达成与任务成功可同时发生，安全与效用不能用一个数字替代；比较的是“框架 + 模型”组合，难以孤立机制。

**与具身智能安全的相关性**：邻接：具身代理同样依赖技能库与工具链，这条攻击面会传导到物理动作；但基准不含机器人执行。

**用这个 benchmark 测了什么**：同一 GLM-5.1 在两种代理框架下的风险达成率分别为 50.3% 与 33.5%——框架上下文显著影响结果，但该对照不足以解释具体机制。

**本轮核查边界**：只读 README，未进入案例浏览器。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| SkillSafetyBench | 基准 | 技能型软件代理安全；邻接参考 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 Apache-2.0（开源许可证）），不再重复解释。

<!-- glossary:end -->
