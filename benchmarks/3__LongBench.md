# LongBench

> **所属环节**：真机长时程操作  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

真机长时程操作。

该基准由 *LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks* 提出，其定位为：**LongBench：真机长时程操作基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：1000+ 真机回合；Context-Independent / Context-Dependent 两个区间。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LongBench：真机长时程操作基准](https://arxiv.org/abs/2604.16788) | 2026 | arXiv 预印本 (arXiv:2604.16 | **提出** | 1000+ 真机回合；Context-Independent / Context-Dependent 两个区间 |

## 4. 关键结论与改进方向

**要点**：真机长时程操作基准，含 1000 余个真实回合，分两个互补区间：完全可观测的 Context-Independent 与由歧义驱动的 Context-Dependent。任务被组织为能力子集与歧义子集，从而支持对执行鲁棒性、时间一致性与上下文依赖推理做机制感知的评测。评测 6 个 SOTA 策略显示长时程性能并非由单一因素决定：完全可观测设定下的表现与执行鲁棒性关联更强，而上下文难度因任务而异，且记忆类方法并未带来一致提升。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks（2026，arXiv 预印本 (arXiv:2604.16788)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
