# MSK-Bench

> **所属环节**：全身肌肉骨骼控制  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

全身肌肉骨骼控制。

该基准由 *MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics* 提出，其定位为：**MSK-Bench：全身肌肉骨骼运动控制基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：22 个全身任务、3 个递进难度类；任务/范式/生理指标。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [MSK-Bench：全身肌肉骨骼运动控制基准](https://arxiv.org/abs/2609.26872) | 2026 | arXiv 预印本 (arXiv:2609.26 | **提出** | 22 个全身任务、3 个递进难度类；任务/范式/生理指标 |

## 4. 关键结论与改进方向

**要点**：指出肌肉骨骼（MSK）人形提供了生理上更真实的全身运动控制载体，但高维肌肉驱动、延迟激活动力学与冗余肌腱结构使学习远难于力矩驱动的人形；现有 MSK 基准分散在步态、假肢、灵巧手或特定挑战赛道，全身肌肉驱动控制缺乏标准化任务、方法与指标的评估。基准含 22 个全身运动控制任务，分为姿态稳定、常见运动等三个递进难度类别。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- MSK-Bench: Benchmarking Full-Body Musculoskeletal Motor Control Across Tasks, Control Paradigms, and Physiological Metrics（2026，arXiv 预印本 (arXiv:2609.26872)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
