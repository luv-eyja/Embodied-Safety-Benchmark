# Embodied Agent Interface

> **所属环节**：具身决策模块化接口  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

具身决策模块化接口。

该基准由 *Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making* 提出，其定位为：**Embodied Agent Interface：具身决策的模块化评测接口**。

## 2. 怎么构建的

构建要点（据原文摘要）：目标解释、子目标分解、动作序列化、状态跟踪等环节的统一接口。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [Embodied Agent Interface：具身决策的模块化评测接口](https://scholar.google.com/scholar?q=Embodied+Agent+Interface%3A+Benchmarking+LLMs+for+Embodied+Decision+Making) | 2024 | NeurIPS 2024（神经信息处理系统大会） | **提出** | 目标解释、子目标分解、动作序列化、状态跟踪等环节的统一接口 |

## 4. 关键结论与改进方向

**要点**：把 LLM 具身决策拆成若干可单独评测的环节，用统一接口连接不同仿真环境与模型，从而定位失败究竟出在目标解释、子任务分解、动作接地还是状态跟踪上，而不是只报告端到端成功率（NeurIPS 2024）。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making（2024，NeurIPS 2024（神经信息处理系统大会））  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
