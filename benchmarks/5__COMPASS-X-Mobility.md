# COMPASS / X-Mobility

> **所属环节**：学习型导航 sim-to-real  
> **分类**：具身安全  
> **关联论文**：本表 6 篇（提出者 1 篇，使用者 5 篇）

## 1. 测什么问题（内容与所测环节）

学习型导航 sim-to-real。

该基准由 *Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots* 提出，其定位为：**工业内部物流的 Physical AI sim-to-real 基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：两种本体扩展 + 数字孪生；sim-to-real 变体。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LIBERO-Pro2.0：具身基础模型鲁棒性基准](https://arxiv.org/abs/2610.24587) | 2026 | arXiv 预印本 (arXiv:2610.24 | 使用 | 6 维度 22 种静态扰动 + 20 种运行时干预，1648 个偏移任务实例 |
| [SafePlan-Bench / Safe-Align：任务规划安全的测量与对齐](https://arxiv.org/abs/2504.14650) | 2025 | arXiv 预印本 (arXiv:2504.14 | 使用 | 2027 个日常任务、8 类危险（如火灾）；规划安全性 |
| [Agent-SafetyBench：LLM 智能体安全基准](https://arxiv.org/abs/2412.14470) | 2024 | arXiv 预印本 (arXiv:2412.14 | 使用 | 349 个交互环境、2000 个测试用例；8 类风险、10 种失败模式 |
| [LABIT：工业长时程装配基准](https://arxiv.org/abs/2610.16398) | 2026 | arXiv 预印本 (arXiv:2610.16 | 使用 | 多装配与子装配步骤；长时程工业流程 |
| [工业内部物流的 Physical AI sim-to-real 基准](https://arxiv.org/abs/2610.28432) | 2026 | arXiv 预印本 (arXiv:2610.28 | **提出** | 两种本体扩展 + 数字孪生；sim-to-real 变体 |
| [具身智能体安全：从安全基准到输入审核](https://arxiv.org/abs/2504.15699) | 2025 | IJCAI 2025（国际人工智能联合会议） | 使用 | 从分类学、数据集、审核器架构、训练到评测的完整流水线 |

## 4. 关键结论与改进方向

**要点**：指出经典导航栈可靠但每换一种机器人或场地就要重新工程化，学习型导航把工作从手调参数转移到数据生成与训练（在新本体或场地通过仿真微调适配策略），但这种适配后的策略在真实工业机器人上是否仍可靠缺乏系统测试。该工作在 NVIDIA X-Mobility 与 COMPASS 流程上，用仿真扩展基准并做真机验证。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models（2026，arXiv 预印本 (arXiv:2610.24587)）
- A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents（2025，arXiv 预印本 (arXiv:2504.14650)）
- Agent-SafetyBench: Evaluating the Safety of LLM Agents（2024，arXiv 预印本 (arXiv:2412.14470)）
- LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks（2026，arXiv 预印本 (arXiv:2610.16398)）
- Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots（2026，arXiv 预印本 (arXiv:2610.28432)）  ← **提出**
- Advancing Embodied Agent Security: From Safety Benchmarks to Input Moderation（2025，IJCAI 2025（国际人工智能联合会议））

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
