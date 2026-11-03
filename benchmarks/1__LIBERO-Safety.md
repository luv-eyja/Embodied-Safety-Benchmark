# LIBERO-Safety

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：安全约束和分套件任务定义是主要产出。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：物理与语义安全；五类套件 × L0-L2 难度  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://libero-safety.github.io](https://libero-safety.github.io)
>
> 具体的任务条目、UBDDL 参数、CuRobo 轨迹生成和运行接口见：[LIBERO-Safety：实现拆解与任务条目](../analysis/LIBERO-Safety-实现拆解.md)。

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 仿真 VLA 物理与语义安全 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 |
| 基础平台线索 | LIBERO |
| 规模线索 | AAG、HRI、TSA、FSHOA、SSR 五套任务，每套 5 个任务、3 档难度，共 75 个测试配置；另有 40 个训练任务和 19,664 条无碰撞示范。 |
| 执行环境线索 | 仿真 VLA 物理与语义安全 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7165682249)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：传统 LIBERO 成功标准遗漏哪些物理与语义风险，如何将风险变成逐步可检查的任务约束？

**评测层级**：仿真 VLA 物理与语义安全。

## 2. 怎么构建的

**核心场景与条目**：AAG、HRI、TSA、FSHOA、SSR 五套任务，每套 5 个任务、3 档难度，共 75 个测试配置；另有 40 个训练任务和 19,664 条无碰撞示范。

**实现与判分**：用 UBDDL 扩展 BDDL 的随机化、动态交互和逐步安全检查；关键姿态与 CuRobo 用于示范生成。除终点成功，还记录碰撞和场景风险。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686) | 2026 | 提出 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 | 提出 LIBERO-Safety，面向 VLA 的物理与语义安全进行统一评测。基准包含 affordance-aware grasping、human-robot interaction、tabletop spatial avoidance、free-space hand-object avoidance 与 semantic safety reasoning 五类套件，每类含 L0–L2 三档难度；通过 keypose-driven pipeline 生成 19,664 条严格无碰撞示范，并同时报告物理安全、语义安全和环境随机性下的鲁棒性。官方项目页注明已被 ECCV 2026 接收。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：表 3 中 OpenVLA-OFT 在 AAG 的 L0／L1／L2 成功率为 50.0%／79.3%／1.3%，说明训练分布和风险形态会造成非单调表现。成果为可复用的安全任务描述与评测扩展。

**适用边界**：不能把 L1 的高成功率解释为安全性全面更好；须同时看安全指标。部分数据生成组件的公开状态仍以仓库实现审计为准，论文描述不等于全部代码已可运行。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

不能把 L1 的高成功率解释为安全性全面更好；须同时看安全指标。部分数据生成组件的公开状态仍以仓库实现审计为准，论文描述不等于全部代码已可运行。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Rongxu Cui, Zongzheng Zhang, Jingrui Pang, et al., ‘LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2606.23686v2. [论文](https://arxiv.org/abs/2606.23686)；[核查正文](https://arxiv.org/html/2606.23686v2)。

**重点核查位置（章节主题）**：3.1 Benchmark Design；3.2 Data Generation；4.2 Main Results；4.3 Analysis。

OpenAlex 被引次数：**[0](https://openalex.org/W7165682249)**；观测日期：2026-11-03。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://libero-safety.github.io](https://libero-safety.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。

本仓库另有[LIBERO-Safety 实现拆解](../analysis/LIBERO-Safety-实现拆解.md)。
<!-- paper-review:end -->
