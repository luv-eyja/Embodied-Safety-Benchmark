# RoboChrono 之外：AeroIntent

> **所属环节**：UAV 任务意图识别  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

UAV 任务意图识别。

该基准由 *AeroIntent: A Synchronized Multimodal Benchmark for UAV Mission Intent Recognition* 提出，其定位为：**AeroIntent：UAV 任务意图识别的同步多模态基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：990 条同步多模态序列、22 个轨迹程序、5 类任务意图；雷达/RGB/红外/深度。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [AeroIntent：UAV 任务意图识别的同步多模态基准](https://arxiv.org/abs/2610.25869) | 2026 | arXiv 预印本 (arXiv:2610.25 | **提出** | 990 条同步多模态序列、22 个轨迹程序、5 类任务意图；雷达/RGB/红外/深度 |

## 4. 关键结论与改进方向

**要点**：指出从多模态观测可靠识别任务级 UAV 意图对低空空域监视与安全至关重要，而现有 UAV 多模态数据集主要支持检测、跟踪与定位，对跨留出轨迹程序与不完整雷达历史的意图识别支持有限。基准含 990 条同步多模态序列，并提供程序不相交、雷达缺失与观测前缀三类评测协议。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- AeroIntent: A Synchronized Multimodal Benchmark for UAV Mission Intent Recognition（2026，arXiv 预印本 (arXiv:2610.25869)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
