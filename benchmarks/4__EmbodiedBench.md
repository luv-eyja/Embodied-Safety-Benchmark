# EmbodiedBench

> **所属环节**：MLLM 具身智能体六能力  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：MLLM 具身智能体六能力。

针对 MLLM 具身智能体缺乏综合评测框架的问题，构建覆盖 4 个环境、1128 个测试任务的基准：从家务等高层语义任务到导航与操作等原子动作级任务，并设 6 个精选子集分别考察常识推理、复杂指令理解、空间意识、视觉感知与长期规划等核心能力。

信息取自表内论文 *EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：1128 个任务 / 4 个环境；6 个能力子集。

## 3. 用这个基准测了什么

**被测对象**：多模态大模型（MLLM）驱动的具身智能体。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [EmbodiedBench：视觉驱动具身智能体综合基准](https://arxiv.org/abs/2502.09560) | 2025 | arXiv 预印本 (arXiv:2502.09 | **提出** | 1128 个任务 / 4 个环境；6 个能力子集 |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents（2025，arXiv 预印本 (arXiv:2502.09560)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
