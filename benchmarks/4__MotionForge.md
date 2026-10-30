# MotionForge

> **所属环节**：动态物体长时程操作  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

动态物体长时程操作。

该基准由 *MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts* 提出，其定位为：**MotionForge：动态物体长时程操作的数据生成与基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：域偏移 + 动态场景；模型无关的实时执行协议。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [MotionForge：动态物体长时程操作的数据生成与基准](https://arxiv.org/abs/2609.25689) | 2026 | arXiv 预印本 (arXiv:2609.25 | **提出** | 域偏移 + 动态场景；模型无关的实时执行协议 |

## 4. 关键结论与改进方向

**要点**：指出学习型机器人策略虽进展显著，但几乎都在静态或准静态环境中评测；动态操作中物体与场景在机器人感知、推理与行动的同时持续演化。现有动态仿真基准多聚焦短时程反应式交互与简单运动模式，对系统性的域偏移评测与模型无关的实时执行协议支持有限。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts（2026，arXiv 预印本 (arXiv:2609.25689)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
