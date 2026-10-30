# nuScenes

> **所属环节**：真实驾驶数据集（开环）  
> **分类**：具身安全  
> **关联论文**：本表 3 篇（提出者 0 篇，使用者 3 篇）

## 1. 测什么问题（内容与所测环节）

真实驾驶数据集（开环）。

## 2. 怎么构建的

本表未记录该基准的详细构建方式，需查原文。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [超越排行榜：域偏移下驾驶策略的反事实诊断](https://arxiv.org/abs/2609.22582) | 2026 | arXiv 预印本 (arXiv:2609.22 | 使用 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 |
| [DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准](https://arxiv.org/abs/2608.29005) | 2026 | arXiv 预印本 (arXiv:2608.29 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 |
| [ExceptionDrive：面向规划的反事实边角案例基准](https://arxiv.org/abs/2609.37871) | 2026 | arXiv 预印本 (arXiv:2609.37 | 使用 | 21 个任务 / 6 个安全族；无参考评测协议（UR/HCC/HPR） |

## 4. 关键结论与改进方向

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift（2026，arXiv 预印本 (arXiv:2609.22582)）
- A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving（2026，arXiv 预印本 (arXiv:2608.29005)）
- ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving（2026，arXiv 预印本 (arXiv:2609.37871)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
