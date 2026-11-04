# INFUSE

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；软件代理邻接研究；目标：安全。
> **分类依据**：软件长工作流安全测试；不计物理机器人场景。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：间接提示注入全生命周期  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/judydnguyen/infuse](https://github.com/judydnguyen/infuse)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › Instruction Understanding |
| 应用领域 | 间接提示注入 |
| 被测对象 | 软件代理工作流安全；邻接参考 |
| 历史关键词标签（未重新统计） | 语义/指令安全、对抗/后门安全 |
| 评测维度/指标 | 40 个真实任务 × 56 类攻击面的结构化分类；全生命周期 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 40 个真实风格软件任务、56 种风险情形、五类威胁；测试对象涉及工具、文件和外部服务，非机器人动作环境。 |
| 执行环境线索 | 软件代理工作流安全；邻接参考 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7222558873)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 1 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：长时程代理在持续读取外部材料时，安全边界能否贯穿整个工作流程？

**评测层级**：软件代理工作流安全；邻接参考。

## 2. 怎么构建的

**核心场景与条目**：40 个真实风格软件任务、56 种风险情形、五类威胁；测试对象涉及工具、文件和外部服务，非机器人动作环境。

**实现与判分**：用隔离环境、统一任务约定和确定性任务验证保持可比性；将正常效用、行为风险的规则核验和模型判分分别记录，比较不同代理及防护条件。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776) | 2026 | 提出 | 40 个真实任务 × 56 类攻击面的结构化分类；全生命周期 | 指出 LLM 智能体越来越多地执行长时程端到端工作流（shell 命令、代码修改、依赖安装、与远程服务交互），自主性扩大使其暴露于间接提示注入——嵌入外部内容的对抗指令被当作合法任务指令执行。现有评测多聚焦孤立的恶意字符串、单步工具调用或狭窄的智能体配置，未能覆盖真实工作流全生命周期。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：19 个模型形成 41,824 条风险测试轨迹与 720 条正常参考运行；平均风险目标达成率在模型判分下为 19.6%、规则核验下为 15.4%，说明裁判方式影响报告值。

**适用边界**：并非所有任务都兼容所有风险情形，不能把 40×56×19 当实际样本数。适合借鉴长链评测与独立验证，不能用作具身碰撞或损伤结论。

## 5. 相关论文（均来自本调研表）

- [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

并非所有任务都兼容所有风险情形，不能把 40×56×19 当实际样本数。适合借鉴长链评测与独立验证，不能用作具身碰撞或损伤结论。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas, et al., ‘INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems,’ arXiv preprint, 2026, arXiv:2610.20776v1. [论文](https://arxiv.org/abs/2610.20776)；[核查正文](https://arxiv.org/html/2610.20776v1)。

**重点核查位置（章节主题）**：3.1 Test Suite Construction；3.2 Evaluation Pipeline；4.1 Setup；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7222558873)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/judydnguyen/infuse](https://github.com/judydnguyen/infuse)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要检索因名称歧义不作计数。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/judydnguyen/infuse](https://github.com/judydnguyen/infuse)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/judydnguyen/infuse) | https://raw.githubusercontent.com/judydnguyen/infuse/HEAD/README.md | stars 0，license MIT（开源许可证），最后推送 2026-10-21，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/judydnguyen/infuse（0 stars，MIT，2026-10-21 推送）含 tasks／attacks 目录、DEFENSES 文档与 tests。

**涉及领域**：代理系统的间接提示注入（间接 prompt injection）安全；文件、工具与记忆表面的统一测试面。

**测试目的与构建方法**：在隔离环境中用统一任务约定与确定性任务验证保持可比，把“正常效用”“行为风险（规则核验）”与“模型判分”分别记录，比较不同代理与防护条件。

**测试缺陷**：并非所有任务都兼容所有风险情形，40×56×19 是配置空间而非实际样本数；裁判方式（规则 vs 模型）显著改变报告值；软件环境，不能推出机器人碰撞或损伤结论。

**与具身智能安全的相关性**：邻接：测的是“读到的内容能否劫持代理行为”。具身代理同样依赖记忆与工具，这一层风险会传导到物理动作，但基准本身没有物理执行。

**用这个 benchmark 测了什么**：19 个模型形成 41,824 条风险轨迹与 720 条正常参考运行；平均风险目标达成率在模型判分下 19.6%、规则核验下 15.4%，说明“谁当裁判”会改变结论。

**本轮核查边界**：只读 README 结构，未执行任何攻击任务。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

名称是常用动词／多个项目的缩写（VCC-INFUSE、INFUSE 后门攻击、INFUSE 幻觉缓解、网络入侵检测 INFUSE 等），无法区分所指。本轮不给使用明细。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 1 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| INFUSE | 基准 | 软件代理工作流安全；邻接参考 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 MIT（开源许可证）），不再重复解释。

<!-- glossary:end -->
