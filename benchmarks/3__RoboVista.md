# RoboVista

> **所属环节**：VLM 空间理解 VQA  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：VLM 空间理解 VQA。

面向未来机器人应用，为视觉语言模型提供细粒度空间理解与具身决策的挑战。RoboVista 是专家标注的视觉问答（VQA）数据集，扎根于 6 个机器人应用域与 39 个多样任务，重点覆盖可变机器人本体、与可变形物体的交互、复杂杂乱场景，以及长时程上下文理解。

信息取自表内论文 *RoboVista: Evaluating Vision Language Models for Diverse Robot Applications*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：6 个机器人应用域 / 39 个任务；专家标注 VQA。

## 3. 用这个基准测了什么

**被测对象**：视觉语言模型（VLM）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [RoboVista：面向多样机器人应用的 VLM 评测](https://doi.org/10.15607/RSS.2026.XXII.095) | 2026 | RSS 2026（Robotics: Scien | **提出** | 6 个机器人应用域 / 39 个任务；专家标注 VQA |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- RoboVista: Evaluating Vision Language Models for Diverse Robot Applications（2026，RSS 2026（Robotics: Science and Systems））  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
