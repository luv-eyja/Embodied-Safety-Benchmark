# Bench2Dex

> **所属环节**：跨灵巧手视触觉  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

跨灵巧手视触觉。

该基准由 *Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands* 提出，其定位为：**Bench2Dex：跨灵巧手的视触觉双臂操作基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：12 种灵巧手；共享的仿真触觉接口。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [Bench2Dex：跨灵巧手的视触觉双臂操作基准](https://arxiv.org/abs/2609.15726) | 2026 | arXiv 预印本 (arXiv:2609.15 | **提出** | 12 种灵巧手；共享的仿真触觉接口 |

## 4. 关键结论与改进方向

**要点**：指出触觉能提供视觉难以推断的接触信息，但灵巧手的触觉硬件尚未收敛到统一设计——不同手的指结构、接触面与传感器布局各异，仿真触觉信号又与真实传感器测量不同，因而难以在一致实验条件下研究跨手视触觉操作。Bench2Dex 为 12 种灵巧手构建统一仿真触觉接口并据此评测。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- Bench2Dex: Benchmarking Visuo-Tactile Bimanual Dexterous Manipulation Across Dexterous Hands（2026，arXiv 预印本 (arXiv:2609.15726)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
