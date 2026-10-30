# RoboDojo

> **所属环节**：42 任务真机评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

42 任务真机评测。

该基准由 *An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond* 提出，其定位为：**LLM 作为策略：GPT-6 Astra 在 RoboDojo 的早期评测**。

## 2. 怎么构建的

构建要点（据原文摘要）：RoboDojo 全部 42 个任务；成功率与 Score（每任务 50 回合协议）。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LLM 作为策略：GPT-6 Astra 在 RoboDojo 的早期评测](https://arxiv.org/abs/2609.24170) | 2026 | arXiv 预印本 (arXiv:2609.24 | **提出** | RoboDojo 全部 42 个任务；成功率与 Score（每任务 50 回合协议） |

## 4. 关键结论与改进方向

**要点**：追问「不做任务微调，LLM 能否直接充当机器人操作策略」。在 RoboDojo 全部 42 个任务、总计 2100 次试验上，GPT-6 Astra 取得 22.48% 平均成功率与 28.97 Score，超过所有公开条目；而同样后处理下 GPT-5.5 与 DeepSeek-Flash 仅 0.88% 与 1.92%。作者进一步指出 Astra 呈现高度两极化的能力分布。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond（2026，arXiv 预印本 (arXiv:2609.24170)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
