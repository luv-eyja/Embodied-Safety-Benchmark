# TrafficSignBench

> **所属环节**：交通标志合规闭环  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

交通标志合规闭环。

该基准由 *TrafficSignBench: Rule-Centric Closed-Loop Evaluation of Traffic-Sign Compliance in Autonomous Driving* 提出，其定位为：**TrafficSignBench：以交通标志为中心的闭环合规评测**。

## 2. 怎么构建的

构建要点（据原文摘要）：真实地图仿真 + 规则定向的程序化场景生成；规则合规率。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [TrafficSignBench：以交通标志为中心的闭环合规评测](https://arxiv.org/abs/2609.38463) | 2026 | arXiv 预印本 (arXiv:2609.38 | **提出** | 真实地图仿真 + 规则定向的程序化场景生成；规则合规率 |

## 4. 关键结论与改进方向

**要点**：指出自动驾驶规划器通常用驾驶分数、到达率与碰撞率等聚合指标评测，这些指标并不直接测量对交通规则的遵守程度，导致规划器可以在基准上取得高分却仍表现出不安全或违规行为，限制其真实部署适用性。基准以交通标志为中心，把真实地图仿真与规则定向的程序化场景生成结合，实现系统且可解释的规则合规评测。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- TrafficSignBench: Rule-Centric Closed-Loop Evaluation of Traffic-Sign Compliance in Autonomous Driving（2026，arXiv 预印本 (arXiv:2609.38463)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
