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
| OpenAlex 引用快照 | [0](https://openalex.org/W7222558873)；2026-11-03 |

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
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas, et al., ‘INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems,’ arXiv preprint, 2026, arXiv:2610.20776v1. [论文](https://arxiv.org/abs/2610.20776)；[核查正文](https://arxiv.org/html/2610.20776v1)。

**重点核查位置（章节主题）**：3.1 Test Suite Construction；3.2 Evaluation Pipeline；4.1 Setup；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7222558873)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/judydnguyen/infuse](https://github.com/judydnguyen/infuse)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
