# PhysAI-Bench

> **所属环节**：UAV 智能体决策  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

UAV 智能体决策。

该基准由 *PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI* 提出，其定位为：**PhysAI-Bench：UAV 自主智能体决策基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：10,178 条标准化决策实例；任务上下文、时序依赖与物理约束。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [PhysAI-Bench：UAV 自主智能体决策基准](https://arxiv.org/abs/2609.23695) | 2026 | arXiv 预印本 (arXiv:2609.23 | **提出** | 10,178 条标准化决策实例；任务上下文、时序依赖与物理约束 |

## 4. 关键结论与改进方向

**要点**：指出现有基准评估物理感知、直觉物理、具身导航与协作推理，却很少评估可靠自主所需的智能体式决策。基准含 10,178 条从自主 UAV 任务对话轨迹中自动抽取的标准化决策实例，每条保留任务上下文、时序依赖与物理约束。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- PhysAI-Bench: A Benchmark for LLM-Based Agentic Decision-Making in Autonomous UAV-Centric Physical AI（2026，arXiv 预印本 (arXiv:2609.23695)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
