# EmbodiedGovBench

<!-- survey-classification:start -->
> **统一调研分类**：评测框架；直接具身评测；目标：安全。
> **分类依据**：主要是治理维度、协议和适配评测原型，不能把示例当实证覆盖。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：治理与演进安全  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/s20sc/embodied-gov-bench](https://github.com/s20sc/embodied-gov-bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Self-Evolving |
| 应用领域 | 未标注 |
| 被测对象 | 治理评测协议与原型框架 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | 7 个治理维度：未授权能力调用、运行时漂移、可恢复性、可审计性、演进安全等 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 七个治理维度：未授权能力调用、运行漂移、恢复、策略可移植性、版本升级、人工覆盖与审计；同时考虑单机器人和多主体机群。 |
| 执行环境线索 | 治理评测协议与原型框架 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7154418749)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：机器人能完成任务之外，是否还能受权限约束、接受人工接管、恢复故障并留下可审计记录？

**评测层级**：治理评测协议与原型框架。

## 2. 怎么构建的

**核心场景与条目**：七个治理维度：未授权能力调用、运行漂移、恢复、策略可移植性、版本升级、人工覆盖与审计；同时考虑单机器人和多主体机群。

**实现与判分**：参数化场景和扰动经 adapter 注入系统，收集轨迹后由 governance judge 对照合法动作与权限边界；按 minimal／standard／fleet／full 档报告覆盖，不以任务完成代替合规。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems](https://arxiv.org/abs/2604.11174) | 2026 | 提出 | 7 个治理维度：未授权能力调用、运行时漂移、可恢复性、可审计性、演进安全等 | 指出现有评测被任务成功率（完成率、操作精度）主导，无法回答具身系统是否「可治理」——是否尊重能力边界、执行策略约束、安全恢复、保留审计轨迹并响应人类监督。基准不再只问机器人能否完成任务，而是在真实扰动下考察系统是否保持可控、受策略约束、可恢复、可审计与演进安全，覆盖七个治理维度。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文成果以指标体系、参与档位、两类原型目标及 worked example 为主；本次核查没有发现可当作大规模实证排行榜的统一比较结果。

**适用边界**：示例分数不能写成多模型实验成果。可解释运行轨迹是评测前提；不支持某一治理接口与实际治理失败应分别标注。

## 5. 相关论文（均来自本调研表）

- [EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems](https://arxiv.org/abs/2604.11174)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

示例分数不能写成多模型实验成果。可解释运行轨迹是评测前提；不支持某一治理接口与实际治理失败应分别标注。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Xue Qin, Simin Luan, John See, et al., ‘EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems,’ arXiv preprint, 2026, arXiv:2604.11174v1. [论文](https://arxiv.org/abs/2604.11174)；[核查正文](https://arxiv.org/html/2604.11174v1)。

**重点核查位置（章节主题）**：3 Governance Dimensions；5 Scoring；6.4 Execution Protocol；6.5 Participation Profiles；7 Prototype Instantiation。

OpenAlex 被引次数：**[0](https://openalex.org/W7154418749)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/s20sc/embodied-gov-bench](https://github.com/s20sc/embodied-gov-bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
