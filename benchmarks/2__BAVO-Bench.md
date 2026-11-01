# BAVO-Bench

> **所属环节**：遮挡下的主动视觉恢复  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）
> **证据级别**：B（提出论文的结构化摘要记录；未逐篇精读全文）

> **项目地址审计**：`found`；[https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation |
| 年份 | 2026 |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 主动视觉 |
| 被测对象 | 双臂操作策略（含主动视觉策略） |
| 关注属性 | 物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 表内摘要未明确规模。 |
| 执行环境线索 | 表内摘要未明确执行环境。 |
| 来源审计 | 已核验：[Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation（same_paper_in_registry）](https://arxiv.org/abs/2609.37292) |
| 来源核验依据 | 摘要明确写明 introduce BAVO-Bench。 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：遮挡下的主动视觉恢复。

**摘要级问题描述**：指出物理主动视觉允许机器人在任务相关观测不可靠时改变视角，但现有操作基准对「策略如何在执行中从遮挡恢复」支持有限。BAVO-Bench 通过 Clean、Stage Occlusion 与 Random-time Occlusion 三种条件系统控制外部可见性，同时评测操作性能与主动视觉恢复能力；作者据此提出联合视角与操作控制的 A-FAR 策略。

信息取自表内论文 *Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation*（该基准的提出者）。

**主要测量维度**：Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复。

## 2. 怎么构建的

### 2.1 构建要素

| 要素 | 摘要级记录 |
|---|---|
| 基础平台 | 表内摘要未明确基础平台。 |
| 任务/场景规模 | 表内摘要未明确规模。 |
| 扰动、风险或约束 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 |
| 对照/配对方式 | 摘要未明确配对设计。 |
| 指标与判分线索 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 |
| 执行设置 | 表内摘要未明确执行环境。 |

### 2.2 详细说明

本仓库当前保存的是摘要级构建信息：Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复

> 本节依据当前调研表的摘要和结构化字段整理；任务划分、阈值、采样方式和完整指标公式仍需回到原文核对。

## 3. 用这个基准测了什么

**被测对象**：双臂操作策略（含主动视觉策略）

**结果应如何读取**：先按“评测维度/指标”字段区分主指标、辅助指标和对照条件；若论文同时报告任务成功与安全/鲁棒性结果，应将二者分开阅读。

下表按论文列出；“摘要级发现”保留调研表中的概要，不等同于全文实验结论。

| 论文 | 年份 / 来源 | 角色 | 被测对象 | 使用方式 / 指标 | 摘要级发现 |
|---|---|---|---|---|---|
| [BAVO-Bench：遮挡恢复的双臂主动视觉基准](https://arxiv.org/abs/2609.37292) | 2026 / arXiv 预印本 (arXiv:2609.37292) | **提出** | 双臂操作策略（含主动视觉策略） | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 | 指出物理主动视觉允许机器人在任务相关观测不可靠时改变视角，但现有操作基准对「策略如何在执行中从遮挡恢复」支持有限。BAVO-Bench 通过 Clean、Stage Occlusion 与 Random-time Occlusion 三种条件系统控制外部可见性，同时评测操作性能与主动视觉恢复能力； |

## 4. 关键结论、改进方向与可复用性

**摘要级发现（按关联论文整理）**：

- **BAVO-Bench：遮挡恢复的双臂主动视觉基准**（2026，提出）：指出物理主动视觉允许机器人在任务相关观测不可靠时改变视角，但现有操作基准对「策略如何在执行中从遮挡恢复」支持有限。BAVO-Bench 通过 Clean、Stage Occlusion 与 Random-time Occlusion 三种条件系统控制外部可见性，同时评测操作性能与主动视觉恢复能力；作者据此提出联合视角与操作控制的 A-FAR 策略。

**基于当前字段的改进提示（不是原文逐字结论）**：

- 按扰动轴、严重度和 clean/OOD 对照分别报告结果，避免只保留聚合成功率。
- 补充约束定义、违规阈值和过程/终态指标，确认安全成功与任务成功是否分开统计。
- 明确失败注入时刻、失败识别标准和恢复成功判据。
- 当前尚无跨论文复用证据，需由独立工作复测后再形成稳定的横向结论。

**复用状态**：当前只看到提出论文，尚无跨论文复用证据。

## 5. 相关论文（均来自本调研表）

- [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)（2026，arXiv 预印本 (arXiv:2609.37292)）  ← **提出**

## 6. 证据边界与复核建议

- **证据级别**：B（提出论文的结构化摘要记录；未逐篇精读全文）。
- **主要来源**：[Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)。
- **当前限制**：本文档基于调研表、论文摘要和少量人工整理；核心条目另有本地全文核查补录，但仍未替代对全文实验表格、附录、代码仓库和数据下载说明的逐项复核。
- **建议复核**：优先确认任务/场景划分、样本规模、指标公式、判分阈值、模型清单，以及仿真与真机设置是否一致。

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成。 A 级文档含人工扩写字段；核心条目附本地全文核查补录；B/C 级文档主要依赖摘要级结构化记录。*
