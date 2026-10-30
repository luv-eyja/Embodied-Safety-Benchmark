# EmbodiedGovBench

> **所属环节**：治理与演进安全  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

治理与演进安全。

该基准由 *EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems* 提出，其定位为：**EmbodiedGovBench：具身系统的治理与演进安全基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：7 个治理维度：未授权能力调用、运行时漂移、可恢复性、可审计性、演进安全等。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [EmbodiedGovBench：具身系统的治理与演进安全基准](https://arxiv.org/abs/2604.11174) | 2026 | arXiv 预印本 (arXiv:2604.11 | **提出** | 7 个治理维度：未授权能力调用、运行时漂移、可恢复性、可审计性、演进安全等 |

## 4. 关键结论与改进方向

**要点**：指出现有评测被任务成功率（完成率、操作精度）主导，无法回答具身系统是否「可治理」——是否尊重能力边界、执行策略约束、安全恢复、保留审计轨迹并响应人类监督。基准不再只问机器人能否完成任务，而是在真实扰动下考察系统是否保持可控、受策略约束、可恢复、可审计与演进安全，覆盖七个治理维度。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems（2026，arXiv 预印本 (arXiv:2604.11174)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
