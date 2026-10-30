# NAVSIM

> **所属环节**：数据驱动非反应式仿真  
> **分类**：具身安全  
> **关联论文**：本表 3 篇（提出者 1 篇，使用者 2 篇）

## 1. 测什么问题（内容与所测环节）

数据驱动非反应式仿真。

该基准由 *NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking* 提出，其定位为：**NAVSIM：数据驱动的非反应式自动驾驶仿真与基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：基于真实数据的非反应式仿真与统一指标。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [超越排行榜：域偏移下驾驶策略的反事实诊断](https://arxiv.org/abs/2609.22582) | 2026 | arXiv 预印本 (arXiv:2609.22 | 使用 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 |
| [DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准](https://arxiv.org/abs/2608.29005) | 2026 | arXiv 预印本 (arXiv:2608.29 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 |
| [NAVSIM：数据驱动的非反应式自动驾驶仿真与基准](https://scholar.google.com/scholar?q=NavSim%3A+Data-Driven+Non-Reactive+Autonomous+Vehicle+Simulation+and+Benchmarking) | 2024 | NeurIPS 2024（神经信息处理系统大会） | **提出** | 基于真实数据的非反应式仿真与统一指标 |

## 4. 关键结论与改进方向

**要点**：提出数据驱动的非反应式仿真基准：用真实驾驶日志构建可复现的仿真评测，避免反应式仿真的域差与不稳定，为端到端规划器提供统一、低成本的比较平台（NeurIPS 2024）。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift（2026，arXiv 预印本 (arXiv:2609.22582)）
- A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving（2026，arXiv 预印本 (arXiv:2608.29005)）
- NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking（2024，NeurIPS 2024（神经信息处理系统大会））  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
