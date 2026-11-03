# LABIT

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：工业长装配能力测试，安全低速不等于安全评测目标。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：工业长时程装配  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://irp-hka.github.io/robotic-assembly-benchmark](https://irp-hka.github.io/robotic-assembly-benchmark)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 工业装配 |
| 被测对象 | 真实工业长时程装配 |
| 历史关键词标签（未重新统计） | 物理/接触安全、任务能力 |
| 评测维度/指标 | 多装配与子装配步骤；长时程工业流程 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | DIN 标准零件，包含拧紧、放置、插入、卡扣及不同公差；零件供给分定位送料、无序平放、箱内杂乱三级，壳体固定夹具位置。 |
| 执行环境线索 | 真实工业长时程装配 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221815075)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：装配中的早期误差会怎样影响后续步骤，如何跨多种装配原语报告可靠性？

**评测层级**：真实工业长时程装配。

## 2. 怎么构建的

**核心场景与条目**：DIN 标准零件，包含拧紧、放置、插入、卡扣及不同公差；零件供给分定位送料、无序平放、箱内杂乱三级，壳体固定夹具位置。

**实现与判分**：按装配原语的难度维度预先计分，并报告每类原语、子装配和整体可靠性；提供零件、模拟及真实基线的位置和力矩记录。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks](https://arxiv.org/abs/2610.16398) | 2026 | 提出 | 多装配与子装配步骤；长时程工业流程 | 指出传统基准多聚焦单一任务（抓取、插入），已无法应对现代制造流程的复杂性与步骤间耦合：新方法的能力已从离散任务扩展到整个装配体的构建。LABIT 因此把评测范围扩展到更广的装配与子装配步骤序列。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：真实基线重复五次，平均完整装配用时约 32 分钟；抓取可靠性 100%、插入平均 82.3%，但部分重定向步骤为 0%，总分会掩盖局部瓶颈。

**适用边界**：五次重复规模小，抓取满分来自定位送料条件，不能外推到杂乱箱。低速真实运行影响时间，不应把用时直接视作算法效率上限。

## 5. 相关论文（均来自本调研表）

- [LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks](https://arxiv.org/abs/2610.16398)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

五次重复规模小，抓取满分来自定位送料条件，不能外推到杂乱箱。低速真实运行影响时间，不应把用时直接视作算法效率上限。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Constantin Schempp, Christian Friedrich, Luca Kofler, et al., ‘LABIT: Long-Horizon Robotic Assembly Benchmark for Industrial Tasks,’ arXiv preprint, 2026, arXiv:2610.16398v1. [论文](https://arxiv.org/abs/2610.16398)；[核查正文](https://arxiv.org/html/2610.16398v1)。

**重点核查位置（章节主题）**：3.2 Tasks；3.3 Performance Metrics；3.3.2 Evaluation Protocol；4.2 Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7221815075)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://irp-hka.github.io/robotic-assembly-benchmark](https://irp-hka.github.io/robotic-assembly-benchmark)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
