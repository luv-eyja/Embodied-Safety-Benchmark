# MotionForge

> **所属环节**：动态物体长时程操作  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：动态物体长时程操作。

指出学习型机器人策略虽进展显著，但几乎都在静态或准静态环境中评测；动态操作中物体与场景在机器人感知、推理与行动的同时持续演化。现有动态仿真基准多聚焦短时程反应式交互与简单运动模式，对系统性的域偏移评测与模型无关的实时执行协议支持有限。

信息取自表内论文 *MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：域偏移 + 动态场景；模型无关的实时执行协议。

## 3. 用这个基准测了什么

**被测对象**：操作策略（含 VLA）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [MotionForge：动态物体长时程操作的数据生成与基准](https://arxiv.org/abs/2609.25689) | 2026 | arXiv 预印本 (arXiv:2609.25 | **提出** | 域偏移 + 动态场景；模型无关的实时执行协议 |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts（2026，arXiv 预印本 (arXiv:2609.25689)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
