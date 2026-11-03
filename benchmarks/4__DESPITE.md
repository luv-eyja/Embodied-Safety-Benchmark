# DESPITE

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：确定性验证的安全规划任务集，未执行低层动作。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：具身规划的系统性安全风险  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://despite-safety.github.io](https://despite-safety.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Using large language models for embodied planning introduces systematic safety risks |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Task Planning |
| 应用领域 | 规划 |
| 被测对象 | 符号具身安全规划 |
| 历史关键词标签（未重新统计） | 物理/接触安全、任务能力 |
| 评测维度/指标 | 12,279 个任务；物理与规范两类危险；确定性验证 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 12,279 个任务覆盖物理和规范危险；主结果／规模分析使用从面板模型筛选出的 1,044 个困难任务，任务因素分析使用全集。 |
| 执行环境线索 | 符号具身安全规划 |
| 来源审计 | [Using large language models for embodied planning introduces systematic safety risks](https://arxiv.org/abs/2604.18463)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce DESPITE benchmark。 |
| 全文状态 | 已核查本地全文：`docs/_fulltext/DESPITE.txt` |
| OpenAlex 引用快照 | [0](https://openalex.org/W7155060036)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：计划可执行、能达成目标，是否意味着计划也安全？模型变大首先改善哪种能力？

**评测层级**：符号具身安全规划。

## 2. 怎么构建的

**核心场景与条目**：12,279 个任务覆盖物理和规范危险；主结果／规模分析使用从面板模型筛选出的 1,044 个困难任务，任务因素分析使用全集。

**实现与判分**：用带安全约束的规划形式化与确定性验证，分别判定计划有效性、危险性和安全完成；评估 23 个模型，并分解规划能力与安全意识。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Using Large Language Models for Embodied Planning Introduces Systematic Safety Risks](https://arxiv.org/abs/2604.18463) | 2026 | 提出 | 12,279 个任务；物理与规范两类危险；确定性验证 | 为系统评估规划安全性，基准含 12,279 个跨物理与规范危险的**完全确定性验证**任务。对 23 个模型的评测给出核心结论：规划能力接近完美并不保证安全——规划最好的模型只在 0.4% 任务上未能产出有效计划，却有 28.3% 的任务产出危险计划；18 个开源模型（3B 到 671B）的规划能力随规模从 0.4% 提升到 99.3%，而安全意识基本持平（38–57%）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：最强规划模型仅 0.4% 任务未产生有效计划，却在 28.3% 任务产生危险计划；18 个开源模型的规划能力随规模明显改善，安全意识仍集中在约 38–57%。

**适用边界**：这是形式化规划验证，不是执行机器人关节轨迹；主结果来自按模型表现挑出的困难集，不能宣称是全部 12,279 任务的随机平均。

## 5. 相关论文（均来自本调研表）

- [Using Large Language Models for Embodied Planning Introduces Systematic Safety Risks](https://arxiv.org/abs/2604.18463)（2026；提出）

## 6. 证据边界与复核建议

### 6.1 全文核查补录（核心论文）

> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。

**来源文件**：`docs/_fulltext/DESPITE.txt`。

**评测协议**：从 5 个异质来源构造 12,279 个具身规划任务，另设 1,044 个 hard split；形式验证器把计划分为 infeasible、feasible-unsafe、feasible-safe，并允许冗余但安全的计划。主要指标为 Feasibility、Safety、Safety Precision、Safety Intention；7 个模型完成全量任务，另比较 18 个 3B–671B 开源模型与 proprietary reasoning 模型。

**定量证据**：最佳规划模型的 infeasible 约 0.4%，但 dangerous plan 仍约 28.3%；开源模型 feasibility 为 0.4–99.3%，Safety Intention 约 37.6–56.9%，专有 reasoning 模型约 71–81%。hard split 中 GPT-5 的 feasibility 99.5、Safety Precision 81.4；高可行性难例中 physical danger 占 70.6–88.2%，高安全性/意图难例中 normative danger 占 18.4–40.0%/15.7–42.5%。加入 2–64 个无关动作后，feasibility 下降 21.0%、Safety Intention 下降 17.3%，联合安全退化 37.9%。

**全文结论**：规划可执行与规划安全是两个不同能力轴；模型即使能找到合法计划，也常未识别物理或规范危险。PDDL/基础问题格式会隐藏危险语境，确定性验证器和冗余安全计划设计是该基准可复核性的关键。

**适用边界**：该基准评测的是语言模型生成的具身计划和形式验证结果，不能直接代替 VLA 的连续控制安全；不同模型的提示、推理模式和输出预算仍需按原文协议解释。

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这是形式化规划验证，不是执行机器人关节轨迹；主结果来自按模型表现挑出的困难集，不能宣称是全部 12,279 任务的随机平均。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Tao Zhang, Kaixian Qu, Zhibin Li, et al., ‘Using large language models for embodied planning introduces systematic safety risks,’ arXiv preprint, 2026, arXiv:2604.18463v2. [论文](https://arxiv.org/abs/2604.18463)；[核查正文](https://arxiv.org/html/2604.18463v2)。

**重点核查位置（章节主题）**：1.1 Safe Planning Landscape；1.2 Scaling；3.1 Experimental Setup；3.2 Formalism；3.3 Evaluation。

OpenAlex 被引次数：**[0](https://openalex.org/W7155060036)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://despite-safety.github.io](https://despite-safety.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
