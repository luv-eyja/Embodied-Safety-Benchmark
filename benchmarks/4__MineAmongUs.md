# MineAmongUs

> **所属环节**：具身社交欺骗  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 0 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：具身社交欺骗。

指出 LLM/VLM 智能体的策略性欺骗已成为 AI 对齐与安全的核心议题，社交推理游戏是典型试验台；但现有试验台是纯文本的、且只跑单一固定智能体配置，漏掉了欺骗分类学视为核心的非言语感觉运动通道，也让人无法判断观察到的行为到底反映底层模型还是外围执行框架。该基准是一个 3D 多模态 Among Us 沙盒。

信息取自表内论文 *Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：3D 多模态 Among Us 沙盒；言语 + 非言语感觉运动通道。

## 3. 用这个基准测了什么

**被测对象**：多模态 VLM 智能体。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [MineAmongUs：具身社交中的言语与非言语联合欺骗](https://arxiv.org/abs/2608.30428) | 2026 | arXiv 预印本 (arXiv:2608.30 | 使用 | 3D 多模态 Among Us 沙盒；言语 + 非言语感觉运动通道 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **MineAmongUs：具身社交中的言语与非言语联合欺骗**（2026）：该基准是一个 3D 多模态 Among Us 沙盒。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions（2026，arXiv 预印本 (arXiv:2608.30428)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
