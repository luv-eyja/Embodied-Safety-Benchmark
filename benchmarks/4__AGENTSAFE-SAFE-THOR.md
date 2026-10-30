# AGENTSAFE / SAFE-THOR

> **所属环节**：危险指令下的智能体安全  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

危险指令下的智能体安全。

该基准由 *AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions* 提出，其定位为：**AGENTSAFE / SAFE：危险指令下的具身智能体安全**。

## 2. 怎么构建的

构建要点（据原文摘要）：感知-规划-执行全过程；危险指令下的违规与失败模式。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [AGENTSAFE / SAFE：危险指令下的具身智能体安全](https://arxiv.org/abs/2506.14697) | 2025 | arXiv 预印本 (arXiv:2506.14 | **提出** | 感知-规划-执行全过程；危险指令下的违规与失败模式 |

## 4. 关键结论与改进方向

**要点**：指出既有安全基准危险范围窄、只看最终结果，忽略智能体完整的感知-规划-执行过程，从而掩盖关键失败模式。SAFE 含三部分：可扩展的对抗仿真沙箱 SAFE-THOR（通用适配器把 VLM 高层输出映射为底层具身控制，支持多种智能体工作流接入）、风险感知的 SAFE-VERSE 等，用于系统评估具身 VLM 智能体执行危险指令时的安全性。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions（2025，arXiv 预印本 (arXiv:2506.14697)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
