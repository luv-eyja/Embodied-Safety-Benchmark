# RoboDojo

> **所属环节**：42 任务真机评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：42 任务真机评测。

追问「不做任务微调，LLM 能否直接充当机器人操作策略」。在 RoboDojo 全部 42 个任务、总计 2100 次试验上，GPT-6 Astra 取得 22.48% 平均成功率与 28.97 Score，超过所有公开条目；而同样后处理下 GPT-5.5 与 DeepSeek-Flash 仅 0.88% 与 1.92%。作者进一步指出 Astra 呈现高度两极化的能力分布。

信息取自表内论文 *An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：RoboDojo 全部 42 个任务；成功率与 Score（每任务 50 回合协议）。

## 3. 用这个基准测了什么

**被测对象**：3 个 LLM 作为策略（无任务微调）；40 个公开策略作对照。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LLM 作为策略：GPT-6 Astra 在 RoboDojo 的早期评测](https://arxiv.org/abs/2609.24170) | 2026 | arXiv 预印本 (arXiv:2609.24 | **提出** | RoboDojo 全部 42 个任务；成功率与 Score（每任务 50 回合协议） |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond（2026，arXiv 预印本 (arXiv:2609.24170)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
