# RoboChrono

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：对已采集机器人视频进行理解测试，无策略动作执行。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：流式任务理解  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://continuity3.github.io/robochrono](https://continuity3.github.io/robochrono)；[https://github.com/mfan-res/ROBOCHRONO](https://github.com/mfan-res/ROBOCHRONO)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboChrono: A Real Robot Benchmark for Streaming Task Understanding |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 机器人流式视频理解 |
| 历史关键词标签（未重新统计） | 语义/指令安全、任务能力 |
| 评测维度/指标 | 39 个场景 / 34,713 个评测实例；7 类任务（识别、对齐、时序接地） |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 39 种操作场景、1,816 个成功视频、约 25 小时；包括夹爪、灵巧手及人手，七项任务覆盖当前／下一动作、跨视角匹配、顺序和时间定位。 |
| 执行环境线索 | 机器人流式视频理解 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214955540)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：只看到当前时刻以前的画面，模型能否理解动作进度、预测下一步并定位事件？

**评测层级**：机器人流式视频理解。

## 2. 怎么构建的

**核心场景与条目**：39 种操作场景、1,816 个成功视频、约 25 小时；包括夹爪、灵巧手及人手，七项任务覆盖当前／下一动作、跨视角匹配、顺序和时间定位。

**实现与判分**：人工时间标注后生成问题，输入严格截断为观察前缀；六项选择题报告正确率，动作时间定位独立报告 R@1、tIoU≥0.5，未来信息仅用于标签。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboChrono: A Real Robot Benchmark for Streaming Task Understanding](https://arxiv.org/abs/2609.36605) | 2026 | 提出 | 39 个场景 / 34,713 个评测实例；7 类任务（识别、对齐、时序接地） | 理解正在进行的机器人操作，要求模型把视觉观测与交互历史、任务进度联系起来。RoboChrono 是流式任务理解基准，由真机执行数据与互补的裸手人类录制构成，含 39 个场景、34,713 个评测实例；评测 7 类任务、归为识别、对齐与时序接地三组，覆盖动作理解与预判、视觉对应、时序排序与动作定位。18 个视觉语言模型的零样本评测显示任务间差异巨大。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：18 个多模态模型的结果显示跨帧识别、下一步预测和时间定位难度不同；论文最佳选择题聚合为 0.805，时间定位为 0.721，二者不是同一种指标。

**适用边界**：这是视频理解而非机器人控制成功率。成功示范视频不能代表失败恢复过程；人手与机器人视频、不同任务指标不宜无条件求平均。

## 5. 相关论文（均来自本调研表）

- [RoboChrono: A Real Robot Benchmark for Streaming Task Understanding](https://arxiv.org/abs/2609.36605)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这是视频理解而非机器人控制成功率。成功示范视频不能代表失败恢复过程；人手与机器人视频、不同任务指标不宜无条件求平均。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Yuzhou Wu, Longteng Fan, Zimeng Li, et al., ‘RoboChrono: A Real Robot Benchmark for Streaming Task Understanding,’ arXiv preprint, 2026, arXiv:2609.36605v1. [论文](https://arxiv.org/abs/2609.36605)；[核查正文](https://arxiv.org/html/2609.36605v1)。

**重点核查位置（章节主题）**：3.1 Benchmark Overview；3.2 Data Collection and Temporal Annotation；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214955540)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://continuity3.github.io/robochrono](https://continuity3.github.io/robochrono)；[https://github.com/mfan-res/ROBOCHRONO](https://github.com/mfan-res/ROBOCHRONO)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
