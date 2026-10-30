# VLA-Arena

> **所属环节**：四维任务结构的难度梯度（含 Safety 套件）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

四维任务结构的难度梯度（含 Safety 套件）。

该基准由 *VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models* 提出，其定位为：**VLA-Arena：开源 VLA 基准框架**。

## 2. 怎么构建的

构建要点（据原文摘要）：三轴结构化难度（任务结构 / 语言指令 W0–W4 / 视觉观测 V0–V4）；11 个任务套件、170 个任务。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [VLA-Arena：开源 VLA 基准框架](https://arxiv.org/abs/2512.22539) | 2025 | arXiv 预印本 (arXiv:2512.22 | **提出** | 三轴结构化难度（任务结构 / 语言指令 W0–W4 / 视觉观测 V0–V4）；11 个任务套件、170 个任务 |

## 4. 关键结论与改进方向

**要点**：以结构化任务设计框架量化难度：任务结构维度含 Safety、Distractor、Extrapolation、Long Horizon 四个维度共 11 个套件 170 个任务，每个套件分 L0–L2 三级而微调只允许用 L0，以严格测泛化；语言与视觉扰动可作为任意任务上的诊断探针，区分稳健接地与表层模式匹配。评测主流 VLA 后发现记忆优于泛化、视觉感知流于表面、忽视安全约束，且 L0–L2 间出现模型排名反转，说明各难度级提供非冗余信息。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2512.22539)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
