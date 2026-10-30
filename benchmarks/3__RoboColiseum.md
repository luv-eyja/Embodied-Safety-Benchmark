# RoboColiseum

> **所属环节**：前沿模型四条赛道评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

前沿模型四条赛道评测。

该基准由 *Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum* 提出，其定位为：**RoboColiseum：前沿 LLM 控制机器人的跨模型评测**。

## 2. 怎么构建的

构建要点（据原文摘要）：四条赛道：指令遵循、空间推理、通用操作、鲁棒性。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [RoboColiseum：前沿 LLM 控制机器人的跨模型评测](https://arxiv.org/abs/2610.27865) | 2026 | arXiv 预印本 (arXiv:2610.27 | **提出** | 四条赛道：指令遵循、空间推理、通用操作、鲁棒性 |

## 4. 关键结论与改进方向

**要点**：在 RoboColiseum 上做多维对比评测，并实现 Agent2Act 控制框架，把四个前沿模型通过共享的观测、动作执行与反馈接口接入评测环境。统一任务设置与评分标准下，四个模型呈现一致的能力画像：指令遵循得分很高（其中三个接近满分）、空间推理较强，而通用操作得分明显低于其余三条赛道。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum（2026，arXiv 预印本 (arXiv:2610.27865)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
