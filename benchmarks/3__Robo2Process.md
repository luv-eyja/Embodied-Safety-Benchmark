# Robo2Process

> **所属环节**：过程感知理解  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

过程感知理解。

该基准由 *Robo2Process: Benchmarking and Learning Process-Aware Understanding in Vision-Language Robotic Manipulation* 提出，其定位为：**Robo2Process：过程感知理解的基准与学习**。

## 2. 怎么构建的

构建要点（据原文摘要）：局部过程单元（LPU）；过程感知 QA 监督与诊断。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [Robo2Process：过程感知理解的基准与学习](https://arxiv.org/abs/2606.13040) | 2026 | arXiv 预印本 (arXiv:2606.13 | **提出** | 局部过程单元（LPU）；过程感知 QA 监督与诊断 |

## 4. 关键结论与改进方向

**要点**：指出被用作机器人评审、奖励生成器与失败检测器的视觉语言模型，必须理解操作「如何展开」而不只是「是否成功」，但细粒度的过程监督没有统一形式，现有评测也无法系统诊断这类能力。Robo2Process 是轨迹接地的框架：把视觉观测与来源原生的信号和标注对齐，抽取局部过程单元（LPU），再经任务特定采样、确定性标签构造与歧义处理生成结构化的 QA 监督。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- Robo2Process: Benchmarking and Learning Process-Aware Understanding in Vision-Language Robotic Manipulation（2026，arXiv 预印本 (arXiv:2606.13040)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
