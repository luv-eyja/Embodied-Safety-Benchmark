# Balanced Multi-Robot Task Allocation Benchmark

> **所属环节**：通信退化下 MRTA  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：通信退化下 MRTA。

指出为嵌入式部署选择去中心化多机器人任务分配方法时，不能只看路径性能。基准在 Collaborative Visit 场景下对比六种分配器（CBAA、ACBBA、PI、HIPC、DMCHBA、DGA），覆盖 MinMax/MinSum 旅行代价、通信鲁棒性与需求、分配可靠性、计算负担与规模敏感性，核心研究使用 500 组配对十目标任务、25 种理想与退化通信条件（伯努利丢包、Gilbert–Elliott 丢包与瑞利衰落）。

信息取自表内论文 *Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：500 组配对实例 × 25 种通信条件；旅行代价、通信鲁棒性、分配可靠性、算力与规模敏感性。

## 3. 用这个基准测了什么

**被测对象**：6 种去中心化 MRTA 分配器。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [通信退化下的去中心化多机器人任务分配基准](https://arxiv.org/abs/2609.13711) | 2026 | arXiv 预印本 (arXiv:2609.13 | **提出** | 500 组配对实例 × 25 种通信条件；旅行代价、通信鲁棒性、分配可靠性、算力与规模敏感性 |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation（2026，arXiv 预印本 (arXiv:2609.13711)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
