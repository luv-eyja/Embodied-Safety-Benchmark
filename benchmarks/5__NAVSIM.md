# NAVSIM

> **所属环节**：数据驱动非反应式仿真  
> **分类**：具身安全  
> **关联论文**：本表 3 篇（提出者 1 篇，使用者 2 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：数据驱动非反应式仿真。

提出数据驱动的非反应式仿真基准：用真实驾驶日志构建可复现的仿真评测，避免反应式仿真的域差与不稳定，为端到端规划器提供统一、低成本的比较平台（NeurIPS 2024）。

信息取自表内论文 *NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：基于真实数据的非反应式仿真与统一指标。

## 3. 用这个基准测了什么

**被测对象**：端到端驾驶规划器。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [超越排行榜：域偏移下驾驶策略的反事实诊断](https://arxiv.org/abs/2609.22582) | 2026 | arXiv 预印本 (arXiv:2609.22 | 使用 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 |
| [DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准](https://arxiv.org/abs/2608.29005) | 2026 | arXiv 预印本 (arXiv:2608.29 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 |
| [NAVSIM：数据驱动的非反应式自动驾驶仿真与基准](https://scholar.google.com/scholar?q=NavSim%3A+Data-Driven+Non-Reactive+Autonomous+Vehicle+Simulation+and+Benchmarking) | 2024 | NeurIPS 2024（神经信息处理系统大会） | **提出** | 基于真实数据的非反应式仿真与统一指标 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **超越排行榜：域偏移下驾驶策略的反事实诊断**（2026）：提出反事实体检——数百帧真实画面各做两种编辑（移除行人、夜间重打光）并由独立检测器验证，把规划轨迹的变化当作诊断量而非分数，并从中读出两个因果轴、构造五项「考试」以分离被单一分数合并的行为差异。
- **DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准**（2026）：基准把 16 类退化在 5 个严重度下于图像加载器内即时注入，单一算子即可触达 15 个策略。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift（2026，arXiv 预印本 (arXiv:2609.22582)）
- A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving（2026，arXiv 预印本 (arXiv:2608.29005)）
- NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking（2024，NeurIPS 2024（神经信息处理系统大会））  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
