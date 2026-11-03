# MemForm

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；软件代理邻接研究；目标：安全。
> **分类依据**：控制记忆接口的安全诊断集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：记忆形成投毒  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/opanhw/memform-code](https://github.com/opanhw/memform-code)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | MemForm: Benchmarking Memory Formation Poisoning in LLM Agents |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Memory |
| 应用领域 | 记忆投毒 |
| 被测对象 | 代理记忆可靠性诊断；邻接参考 |
| 历史关键词标签（未重新统计） | 对抗/后门安全 |
| 评测维度/指标 | 五类形成接口：内容、证据、范围、选择、路径投毒 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | Content、Evidence、Scope、Selection、Path 五个记忆接口；六种 LLM、两种回答格式，在正常／受影响条件下对照。 |
| 执行环境线索 | 代理记忆可靠性诊断；邻接参考 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221777130)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：长期记忆形成过程中，经验内容、证据、适用范围、保留选择和整合次序会怎样影响后续行为？

**评测层级**：代理记忆可靠性诊断；邻接参考。

## 2. 怎么构建的

**核心场景与条目**：Content、Evidence、Scope、Selection、Path 五个记忆接口；六种 LLM、两种回答格式，在正常／受影响条件下对照。

**实现与判分**：对同一语义任务家族构造受控配对，分开检查形成的记忆与后续行为；只在满足正常条件要求的 eligible query 上统计风险目标达成率。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [MemForm: Benchmarking Memory Formation Poisoning in LLM Agents](https://arxiv.org/abs/2610.14431) | 2026 | 提出 | 五类形成接口：内容、证据、范围、选择、路径投毒 | 指出长期记忆让 LLM 智能体能从过去交互中学习，但也使「记忆形成」暴露于对抗影响之下；既有研究多按攻击通道、破坏模式或生命周期阶段组织记忆投毒，对形成接口刻画不足。MemForm 把记忆形成投毒形式化为对持久记忆产出与提交接口的对抗操纵，并引入「选择投毒」与「路径投毒」作为隔离保持与巩固环节的受控干预类别。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：主实现中，选择题格式的描述性宏平均风险达成率范围为 35.2–84.0%，自由回答为 49.0–87.1%；即使保留经历相同，整合次序仍可能改变行为。

**适用边界**：各模型 eligible 子集不同，因此这些范围不是相同测试分布上的直接安全排名；这是记忆机制诊断，不是物理机器人执行评测。

## 5. 相关论文（均来自本调研表）

- [MemForm: Benchmarking Memory Formation Poisoning in LLM Agents](https://arxiv.org/abs/2610.14431)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

各模型 eligible 子集不同，因此这些范围不是相同测试分布上的直接安全排名；这是记忆机制诊断，不是物理机器人执行评测。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Haowen Pan, Pengyang Shao, Yunshan Ma, et al., ‘MemForm: Benchmarking Memory Formation Poisoning in LLM Agents,’ arXiv preprint, 2026, arXiv:2610.14431v1. [论文](https://arxiv.org/abs/2610.14431)；[核查正文](https://arxiv.org/html/2610.14431v1)。

**重点核查位置（章节主题）**：3.1 Definition and Scope；4.1 Construction；4.3 Protocol；5.2 Overall Results；5.5 Limitations。

OpenAlex 被引次数：**[0](https://openalex.org/W7221777130)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/opanhw/memform-code](https://github.com/opanhw/memform-code)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
