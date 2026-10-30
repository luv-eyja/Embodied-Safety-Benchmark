# COMPASS / X-Mobility

> **所属环节**：学习型导航 sim-to-real  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：学习型导航 sim-to-real。

指出经典导航栈可靠但每换一种机器人或场地就要重新工程化，学习型导航把工作从手调参数转移到数据生成与训练（在新本体或场地通过仿真微调适配策略），但这种适配后的策略在真实工业机器人上是否仍可靠缺乏系统测试。该工作在 NVIDIA X-Mobility 与 COMPASS 流程上，用仿真扩展基准并做真机验证。

信息取自表内论文 *Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：两种本体扩展 + 数字孪生；sim-to-real 变体。

## 3. 用这个基准测了什么

**被测对象**：学习型导航策略（NVIDIA X-Mobility / COMPASS）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [工业内部物流的 Physical AI sim-to-real 基准](https://arxiv.org/abs/2610.28432) | 2026 | arXiv 预印本 (arXiv:2610.28 | **提出** | 两种本体扩展 + 数字孪生；sim-to-real 变体 |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- Physical AI for Intralogistics: Benchmarking the NVIDIA Sim-to-Real Ecosystem for Cosmos-Enhanced COMPASS Navigation on Industrial Mobile Robots（2026，arXiv 预印本 (arXiv:2610.28432)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
