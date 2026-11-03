# PhysAI-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：物理约束背景下的决策能力测试，未把物理约束词直接算安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：UAV 智能体决策  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/maferrag/physai-bench](https://github.com/maferrag/physai-bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Tool Use and Skill |
| 应用领域 | UAV 决策 |
| 被测对象 | UAV 任务轨迹中的离线决策问答 |
| 历史关键词标签（未重新统计） | 物理/接触安全 |
| 评测维度/指标 | 10,178 条标准化决策实例；任务上下文、时序依赖与物理约束 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 从自主 UAV 任务对话轨迹提取 10,178 个决策实例，保留任务、传感信息、MCP 工具、A2A 交互及延迟／丢包／边缘负载等网络条件。 |
| 执行环境线索 | UAV 任务轨迹中的离线决策问答 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214012534)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：无人机代理在物理约束、通信和多代理信息同时存在时，能否选择合适的下一步决策？

**评测层级**：UAV 任务轨迹中的离线决策问答。

## 2. 怎么构建的

**核心场景与条目**：从自主 UAV 任务对话轨迹提取 10,178 个决策实例，保留任务、传感信息、MCP 工具、A2A 交互及延迟／丢包／边缘负载等网络条件。

**实现与判分**：仅暴露决策前上下文，构造标准化问题；先选择模型提示／温度配置，再按论文两阶段协议评估，分析少样本与零样本差异。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI](https://arxiv.org/abs/2609.23695) | 2026 | 提出 | 10,178 条标准化决策实例；任务上下文、时序依赖与物理约束 | 指出现有基准评估物理感知、直觉物理、具身导航与协作推理，却很少评估可靠自主所需的智能体式决策。基准含 10,178 条从自主 UAV 任务对话轨迹中自动抽取的标准化决策实例，每条保留任务上下文、时序依赖与物理约束。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：模型专属配置选择阶段的最佳准确率为 70.48%；这一数值来自该阶段配置比较，不应直接宣传为全部 10,178 实例的闭环飞行成功率。

**适用边界**：它评估轨迹派生决策，不执行完整飞行闭环；标签与数据生成链影响有效性。配置选择集和最终测试集必须分清，准确率也不是碰撞率。

## 5. 相关论文（均来自本调研表）

- [PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI](https://arxiv.org/abs/2609.23695)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

它评估轨迹派生决策，不执行完整飞行闭环；标签与数据生成链影响有效性。配置选择集和最终测试集必须分清，准确率也不是碰撞率。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Mohamed Amine Ferrag, Merouane Debbah, Abderrahmane Lakas, et al., ‘PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI,’ arXiv preprint, 2026, arXiv:2609.23695v1. [论文](https://arxiv.org/abs/2609.23695)；[核查正文](https://arxiv.org/html/2609.23695v1)。

**重点核查位置（章节主题）**：III-B Benchmark Overview；III-C Composition；IV-D Two-Stage Protocol；V-A Configuration Selection。

OpenAlex 被引次数：**[0](https://openalex.org/W7214012534)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/maferrag/physai-bench](https://github.com/maferrag/physai-bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
