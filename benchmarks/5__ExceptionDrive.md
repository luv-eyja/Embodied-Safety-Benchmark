# ExceptionDrive

> **所属环节**：反事实边角案例  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

反事实边角案例。

该基准由 *ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving* 提出，其定位为：**ExceptionDrive：面向规划的反事实边角案例基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：21 个任务 / 6 个安全族；无参考评测协议（UR/HCC/HPR）。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [ExceptionDrive：面向规划的反事实边角案例基准](https://arxiv.org/abs/2609.37871) | 2026 | arXiv 预印本 (arXiv:2609.37 | **提出** | 21 个任务 / 6 个安全族；无参考评测协议（UR/HCC/HPR） |

## 4. 关键结论与改进方向

**要点**：指出在常规驾驶基准上的平均表现无法证明规划器在稀有且安全攸关的危险情形下可靠。基准用 VLM 辅助筛选、局部多视角编辑与质量审计，把危险插入真实 nuScenes 场景并保留其上下文；21 个任务跨六个安全族，定义危险/冲突区域、局部安全约束与可接受响应。由于插入危险会使记录的人类轨迹失效，采用无参考协议，用不安全率（UR）、危险避让合规（HCC）、危险接近响应（HPR）等指标评估编辑后的预测。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving（2026，arXiv 预印本 (arXiv:2609.37871)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
