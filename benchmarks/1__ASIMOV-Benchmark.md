# ASIMOV Benchmark

> **所属环节**：语义安全与机器人宪法  
> **分类**：VLA 安全  
> **关联论文**：本表 2 篇（提出者 0 篇，使用者 2 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：语义安全与机器人宪法。

指出既有安全基准危险范围窄、只看最终结果，忽略智能体完整的感知-规划-执行过程，从而掩盖关键失败模式。SAFE 含三部分：可扩展的对抗仿真沙箱 SAFE-THOR（通用适配器把 VLM 高层输出映射为底层具身控制，支持多种智能体工作流接入）、风险感知的 SAFE-VERSE 等，用于系统评估具身 VLM 智能体执行危险指令时的安全性。

信息取自表内论文 *AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：感知-规划-执行全过程；危险指令下的违规与失败模式。

## 3. 用这个基准测了什么

**被测对象**：VLM 驱动的具身智能体。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [AGENTSAFE / SAFE：危险指令下的具身智能体安全](https://arxiv.org/abs/2506.14697) | 2025 | arXiv 预印本 (arXiv:2506.14 | 使用 | 感知-规划-执行全过程；危险指令下的违规与失败模式 |
| [ASIMOV Benchmark：语义安全基准与机器人宪法](https://arxiv.org/abs/2503.08663) | 2025 | arXiv 预印本 (arXiv:2503.08 | 使用 | 语义安全；大规模情景化安全判断数据集 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **AGENTSAFE / SAFE：危险指令下的具身智能体安全**（2025）：SAFE 含三部分：可扩展的对抗仿真沙箱 SAFE-THOR（通用适配器把 VLM 高层输出映射为底层具身控制，支持多种智能体工作流接入）、风险感知的 SAFE-VERSE 等，用于系统评估具身 VLM 智能体执行危险指令时的安全性。
- **ASIMOV Benchmark：语义安全基准与机器人宪法**（2025）：工作有两点贡献：给出可规模化生成「机器人宪法」的数据配方，并发布 ASIMOV Benchmark——用于评测与提升机器人基础模型语义安全的大规模数据集集合。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions（2025，arXiv 预印本 (arXiv:2506.14697)）
- Generating Robot Constitutions & Benchmarks for Semantic Safety（2025，arXiv 预印本 (arXiv:2503.08663)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
