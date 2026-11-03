# ORBIT

<!-- survey-classification:start -->
> **统一调研分类**：评测框架；软件代理邻接研究；目标：能力、安全。
> **分类依据**：主要贡献是多代理安全的可组合执行和评分框架。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：多智能体安全评测框架  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/wlanderson0/orbit](https://github.com/wlanderson0/orbit)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | ORBIT: A Framework for Multi-Agent Safety and Security Evaluations |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Cascading Risks |
| 应用领域 | 多智能体 |
| 被测对象 | 多代理安全评测框架；邻接参考 |
| 历史关键词标签（未重新统计） | 对抗/后门安全、任务能力 |
| 评测维度/指标 | 联合变化攻击、防御与架构；共享评测基础设施 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 完整框架支持五类场景；论文实证切片主要是浏览器、编码、桌面、协作分配四类，结合不同威胁与防护配置。 |
| 执行环境线索 | 多代理安全评测框架；邻接参考 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214782110)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：通信结构、记忆共享和安全机制如何共同影响多代理系统的风险与正常效用？

**评测层级**：多代理安全评测框架；邻接参考。

## 2. 怎么构建的

**核心场景与条目**：完整框架支持五类场景；论文实证切片主要是浏览器、编码、桌面、协作分配四类，结合不同威胁与防护配置。

**实现与判分**：基于 UK AISI Inspect，以配置分离角色、拓扑、调度、记忆、风险和防护；在隔离环境中将风险运行与正常运行配对，报告 Wilson／bootstrap 区间。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [ORBIT: A Framework for Multi-Agent Safety and Security Evaluations](https://arxiv.org/abs/2609.33102) | 2026 | 提出 | 联合变化攻击、防御与架构；共享评测基础设施 | 指出多智能体 LLM 系统越来越多地用于复杂长时程任务，也带来显著的安全与安保风险：让任务泛化成为可能的灵活协议同时暴露了从级联提示注入到智能体间串通的新型威胁。防御进展缓慢的原因是缺乏共享的经验基础设施，每做一个新防御都要定制环境，无法标准化比较；现有评测只覆盖孤立威胁模型或单智能体设置。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：约 90 种实验条件形成可控比较矩阵；贡献在于统一架构／安全因素的对照基础设施，而非一个可概括所有系统的总安全分。

**适用边界**：论文只测试了完整配置空间的一个切片，支持某场景不等于已全面实测；多数任务不是机器人环境，应作为多代理评测设计参考。

## 5. 相关论文（均来自本调研表）

- [ORBIT: A Framework for Multi-Agent Safety and Security Evaluations](https://arxiv.org/abs/2609.33102)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

论文只测试了完整配置空间的一个切片，支持某场景不等于已全面实测；多数任务不是机器人环境，应作为多代理评测设计参考。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Ben Hagag, William L. Anderson, Srija Chakraborty, et al., ‘ORBIT: A Framework for Multi-Agent Safety and Security Evaluations,’ arXiv preprint, 2026, arXiv:2609.33102v1. [论文](https://arxiv.org/abs/2609.33102)；[核查正文](https://arxiv.org/html/2609.33102v1)。

**重点核查位置（章节主题）**：3.1 Design Principles；3.2 Experiment Layers；3.4 Metrics；4 Task Suite；5 Experiment Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214782110)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/wlanderson0/orbit](https://github.com/wlanderson0/orbit)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
