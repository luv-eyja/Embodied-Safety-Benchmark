# RoboAbstention

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：安全。
> **分类依据**：安全弃权测试，非真实执行后果判定。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：弃权能力评测  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://purseclab.github.io/RoboAbstention](https://purseclab.github.io/RoboAbstention)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Cascading Risks |
| 应用领域 | 未标注 |
| 被测对象 | 具身图像条件下的弃权判断 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、实时/治理、任务能力 |
| 评测维度/指标 | 弃权分类法；歧义、物理不可行、错误前提、传感器不足四类情形 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 从 DROID、Robo2VLM、RoboVQA、BridgeV2、EgoThink 各取 250 图，共 1,250 图、6,069 指令，覆盖不同弃权原因。 |
| 执行环境线索 | 具身图像条件下的弃权判断 |
| 来源审计 | [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce RoboAbstention。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7162010380)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：当对象不存在、指代含糊、能力不足或任务不可行时，规划模型是否知道应当停止或请求澄清？

**评测层级**：具身图像条件下的弃权判断。

## 2. 怎么构建的

**核心场景与条目**：从 DROID、Robo2VLM、RoboVQA、BridgeV2、EgoThink 各取 250 图，共 1,250 图、6,069 指令，覆盖不同弃权原因。

**实现与判分**：三阶段生成：结构化视觉接地、确定性约束推导、按类别生成指令；每图每类别抽取单条，减少模板重复，并分析错误继续执行的类型。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544) | 2026 | 提出 | 弃权分类法；歧义、物理不可行、错误前提、传感器不足四类情形 | 指出已有弃权研究多针对纯文本 LLM，无法刻画具身机器人环境固有的感知接地与物理约束。工作在具身语境下给出弃权分类法，并构建可扩展、可审计的 RoboAbstention 框架，用来自五个机器人数据集的图像生成弃权指令，要求智能体识别指令歧义、物理上不可行、基于错误前提或受限于可用传感模态与上下文而无法解决的情形。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文最佳模型 Gemini 2.5 Flash 的弃权率仅 39.0%，显示前沿视觉模型仍常在信息不足时给出计划；成果是可审计的弃权 taxonomy 与图像指令集。

**适用边界**：主要是静态图像／计划回答，不验证真实物理不可行性或实际执行结果。数据集中该弃权样本的识别率不能代表正常请求上的低误拒绝率。

## 5. 相关论文（均来自本调研表）

- [The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents](https://arxiv.org/abs/2605.20544)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

主要是静态图像／计划回答，不验证真实物理不可行性或实际执行结果。数据集中该弃权样本的识别率不能代表正常请求上的低误拒绝率。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Doguhan Yeke, Elif Su Temirel, Ananth Shreekumar, et al., ‘The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents,’ arXiv preprint, 2026, arXiv:2605.20544v1. [论文](https://arxiv.org/abs/2605.20544)；[核查正文](https://arxiv.org/html/2605.20544v1)。

**重点核查位置（章节主题）**：3.1 Sources；3.2 Taxonomy；3.3 Creation；3.4 Statistics；4.2 Benchmarking。

OpenAlex 被引次数：**[0](https://openalex.org/W7162010380)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://purseclab.github.io/RoboAbstention](https://purseclab.github.io/RoboAbstention)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
