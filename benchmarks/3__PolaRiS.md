# PolaRiS

> **所属环节**：real-to-sim 可扩展评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

real-to-sim 可扩展评测。

该基准由 *PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies* 提出，其定位为：**PolaRiS：通用策略的可扩展 real-to-sim 评测**。

## 2. 怎么构建的

构建要点（据原文摘要）：real-to-sim 构建；仿真评测与真机表现的一致性。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [PolaRiS：通用策略的可扩展 real-to-sim 评测](https://doi.org/10.15607/RSS.2026.XXII.062) | 2026 | RSS 2026（Robotics: Scien | **提出** | real-to-sim 构建；仿真评测与真机表现的一致性 |

## 4. 关键结论与改进方向

**要点**：直指机器人评测的老问题——真机 rollout 随机、难复现且耗时，而通用策略需要跨大量场景与任务评测，这一问题被进一步放大。仿真提供了可扩展的补充，但现有仿真基准与真机之间的视觉与物理域差异使其成为不可靠的改进信号，而构建真实多样的仿真场景本身又极其昂贵。PolaRiS 用 real-to-sim 的方式构建可扩展评测，使仿真结果能可靠反映真机表现。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies（2026，RSS 2026（Robotics: Science and Systems））  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
