# ISO-based Humanoid Orchestrator Benchmark

> **所属环节**：人形协作 LLM 编排器  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：人形协作 LLM 编排器。

指出 LLM 越来越多地通过自然语言接口编排机器人行为，但其作为人机协作中安全感知决策者的可靠性没有任何基准可测；与执行二值允许/拒绝的确定性安全系统不同，LLM 编排器表现出从「过度合规」（拒绝安全动作）到完全安全违规的连续谱。该工作是首个面向人形协作 LLM 编排器的安全评测环境。

信息取自表内论文 *How Long Until Your Robot Ignores You? A Safety Benchmark for LLM Orchestrators in Human-Humanoid Collaboration*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：基于 MCP 的架构；ISO 10218-2:2025 防护措施安全不变式。

## 3. 用这个基准测了什么

**被测对象**：作为机器人编排器的 LLM。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [人形协作中 LLM 编排器的安全基准](https://arxiv.org/abs/2609.07288) | 2026 | arXiv 预印本 (arXiv:2609.07 | **提出** | 基于 MCP 的架构；ISO 10218-2:2025 防护措施安全不变式 |

## 4. 关键结论与改进方向

**关键结论**：见上文第 1 节的概要。

**改进方向**：该基准目前仅在其提出论文中出现，提出者给出的改进方向可参考原文的讨论与未来工作；若要形成方向性结论，需等待后续论文复用该基准。

## 5. 相关论文（均来自本调研表）

- How Long Until Your Robot Ignores You? A Safety Benchmark for LLM Orchestrators in Human-Humanoid Collaboration（2026，arXiv 预印本 (arXiv:2609.07288)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
