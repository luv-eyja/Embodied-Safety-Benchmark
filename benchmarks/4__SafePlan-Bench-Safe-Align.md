# SafePlan-Bench / Safe-Align

> **所属环节**：任务规划安全测量与对齐  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 0 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：任务规划安全测量与对齐。

提出测量与对齐一体的框架 Safe-BeAl：SafePlan-Bench 建立任务规划安全的综合基准，覆盖 2027 个日常任务及其对应环境，分布于 8 类危险之中；实证分析表明即便没有对抗输入或恶意意图，LLM 智能体也会表现出不安全行为。随后提出 Safe-Align，把物理世界安全知识注入智能体以缓解这些危险。

信息取自表内论文 *A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：2027 个日常任务、8 类危险（如火灾）；规划安全性。

## 3. 用这个基准测了什么

**被测对象**：LLM 驱动的具身智能体。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [SafePlan-Bench / Safe-Align：任务规划安全的测量与对齐](https://arxiv.org/abs/2504.14650) | 2025 | arXiv 预印本 (arXiv:2504.14 | 使用 | 2027 个日常任务、8 类危险（如火灾）；规划安全性 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **SafePlan-Bench / Safe-Align：任务规划安全的测量与**（2025）：随后提出 Safe-Align，把物理世界安全知识注入智能体以缓解这些危险。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents（2025，arXiv 预印本 (arXiv:2504.14650)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
