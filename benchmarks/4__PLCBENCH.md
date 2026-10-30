# PLCBENCH

> **所属环节**：PLC 到物理影响（HIL）  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

PLC 到物理影响（HIL）。

该基准由 *PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?* 提出，其定位为：**PLCBENCH：LLM 智能体将 PLC 访问转化为持续物理影响的评测**。

## 2. 怎么构建的

构建要点（据原文摘要）：真实 PLC 硬件在环（HIL）；从网络访问到持续物理影响的完整链路。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [PLCBENCH：LLM 智能体将 PLC 访问转化为持续物理影响的评测](https://arxiv.org/abs/2608.26882) | 2026 | arXiv 预印本 (arXiv:2608.26 | **提出** | 真实 PLC 硬件在环（HIL）；从网络访问到持续物理影响的完整链路 |

## 4. 关键结论与改进方向

**要点**：指出工业控制系统依赖 PLC 连接网络化计算与物理控制，而工具使用型 LLM 智能体构成新兴攻击威胁：自主智能体能否把网络可达的 PLC 转化为持续的负面物理影响？现有评测多聚焦数字任务或 PLC 测试的单个阶段，停留在「软件漏洞利用成功」「写入被接受」或「获得工具访问」就下结论，会错误刻画物理风险。该基准是首个真实 PLC 硬件在环框架。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?（2026，arXiv 预印本 (arXiv:2608.26882)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
