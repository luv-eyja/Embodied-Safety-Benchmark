# Spa-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：真机空间理解和执行混淆的受控诊断。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：空间接地真机基准  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://justintiensmith.github.io/Spa-Bench](https://justintiensmith.github.io/Spa-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › World Model |
| 应用领域 | 未标注 |
| 被测对象 | 真实机器人空间接地 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 六类空间描述（物体状态、相对大小、指代、关系放置、序数、计数）；ID/OOD 对比 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | SO-101 上六类桌面任务：物体状态、相对大小、指代描述、关系摆放、序数位置、计数；1,200 示范与 2,892 真实评测轨迹。 |
| 执行环境线索 | 真实机器人空间接地 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221577967)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：模型失败究竟因为不理解空间描述，还是因为不会执行所需机械动作？

**评测层级**：真实机器人空间接地。

## 2. 怎么构建的

**核心场景与条目**：SO-101 上六类桌面任务：物体状态、相对大小、指代描述、关系摆放、序数位置、计数；1,200 示范与 2,892 真实评测轨迹。

**实现与判分**：保留对象、概念和动作的训练支持，仅留出空间配置；在相同场景比较空间指令与直接操作指令，另测改写、跨任务对象和无需动作条件。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696) | 2026 | 提出 | 六类空间描述（物体状态、相对大小、指代、关系放置、序数、计数）；ID/OOD 对比 | 多数 VLA 评测只看物体、指令或环境变化下的总体操作成功率，难以判断策略能否把空间描述可靠地落到物理场景中。该真机基准覆盖物体状态、相对大小、指代描述、关系放置、序数位置与计数六类桌面任务，主要对比分布内与分布外表现，直接考察空间描述到行为的接地能力。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：三个完整评测策略的 ID 成功率为 67.5–73.3%，OOD 为 40.7–52.0%；匹配场景中直接指令比空间指令高 28.3–40.0 个百分点，支持接地错误并非纯运动问题。

**适用边界**：五个模型并非全部完成同样评测，主要比较限于三个完整策略。小型桌面机器人和有限物体不代表开放世界空间推理。

## 5. 相关论文（均来自本调研表）

- [Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2610.12696)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

五个模型并非全部完成同样评测，主要比较限于三个完整策略。小型桌面机器人和有限物体不代表开放世界空间推理。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Justin Tien-Smith, Matthew Pidden, Rolandos Alexandros Potamias, ‘Spa-Bench: A Real-Robot Benchmark for Spatial Grounding in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2610.12696v1. [论文](https://arxiv.org/abs/2610.12696)；[核查正文](https://arxiv.org/html/2610.12696v1)。

**重点核查位置（章节主题）**：III-A Task Suite；III-C Controlled ID and OOD；V-A；V-B Matched-Scene Diagnostics。

OpenAlex 被引次数：**[0](https://openalex.org/W7221577967)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://justintiensmith.github.io/Spa-Bench](https://justintiensmith.github.io/Spa-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
