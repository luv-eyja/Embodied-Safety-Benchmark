# VLABench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：长任务和语言推理评测，不因语言接地自动算安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：认知 + 规划（长时程推理）  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://vlabench.github.io/](https://vlabench.github.io/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 长时程语言与操作推理 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 大规模任务集；长时程推理与组合泛化 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 60 个原子任务、40 个复合任务，覆盖抓放、开门／抽屉、挂物、工具、按钮、插入、倾倒、旋转和探索。 |
| 执行环境线索 | 长时程语言与操作推理 |
| OpenAlex 引用快照 | [16](https://openalex.org/W4405783861)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：语言条件操作能否泛化到新物体类别、隐含语义和需要常识／规划的任务？

**评测层级**：长时程语言与操作推理。

## 2. 怎么构建的

**核心场景与条目**：60 个原子任务、40 个复合任务，覆盖抓放、开门／抽屉、挂物、工具、按钮、插入、倾倒、旋转和探索。

**实现与判分**：任务技能库结合运动规划自动生成轨迹，语言扩增描述对象与意图；分别评估 VLA、基础模型工作流和 VLM，未见物体按不同类别而非仅换纹理划分。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning](https://doi.org/10.1109/ICCV51701.2025.01037) | 2025 | 提出 | 大规模任务集；长时程推理与组合泛化 | 大规模语言条件操作基准，强调「长时程推理」与组合泛化：任务需要多步推理与常识知识才能完成，而不只是把一条指令映射为一次抓取。它把评测重心从单步操作成功率推向「推理—规划—执行」的整链能力，是 VLA 能力评测中较有代表性的高难度基准。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：成果是 100 任务、多维语言语义和更严格的对象类别泛化协议；评测显示低层技能获取、目标语义解析和长任务推理需要分开分析。

**适用边界**：VLM 问答正确率、模块化流程成功率和端到端 VLA 成功率属于不同接口。未见类别设置比同类新实例更严格，跨论文比较必须统一。

## 5. 相关论文（均来自本调研表）

- [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning](https://doi.org/10.1109/ICCV51701.2025.01037)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

VLM 问答正确率、模块化流程成功率和端到端 VLA 成功率属于不同接口。未见类别设置比同类新实例更严格，跨论文比较必须统一。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Shiduo Zhang, Zhe Xu, Peiju Liu, et al., ‘VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks,’ arXiv preprint, 2024, arXiv:2412.18194v1. [论文](https://doi.org/10.1109/ICCV51701.2025.01037)；[核查正文](https://arxiv.org/html/2412.18194v1)。

**重点核查位置（章节主题）**：3.1 Task Description；3.2 Benchmark Evaluation；3.3 Data Generation；Experiments。

OpenAlex 被引次数：**[16](https://openalex.org/W4405783861)**；观测日期：2026-11-03。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://vlabench.github.io/](https://vlabench.github.io/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
