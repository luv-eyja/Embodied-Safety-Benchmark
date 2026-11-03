# RoboMIND

<!-- survey-classification:start -->
> **统一调研分类**：训练数据集；具身研究底座；目标：能力。
> **分类依据**：主要提供规范化多本体操作数据，名称中 Benchmark 不决定成果类型。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：多本体操作  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://x-humanoid-robomind.github.io](https://x-humanoid-robomind.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 多本体真机操作数据 |
| 历史关键词标签（未重新统计） | 物理/接触安全、任务能力 |
| 评测维度/指标 | 跨本体大规模真机数据与统一评测 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 约 10.7 万轨迹，四种本体 Franka、Tien Kung、AgileX Cobot、UR5e；479 任务、96 类物体和 38 种技能。 |
| 执行环境线索 | 多本体真机操作数据 |
| OpenAlex 引用快照 | [23](https://openalex.org/W4414050913)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何用统一采集与质量控制支持跨形态的模仿学习和 VLA 训练？

**评测层级**：多本体真机操作数据。

## 2. 怎么构建的

**核心场景与条目**：约 10.7 万轨迹，四种本体 Franka、Tien Kung、AgileX Cobot、UR5e；479 任务、96 类物体和 38 种技能。

**实现与判分**：统一遥操作、传感记录、质量筛选和语言标注，提供不同机器人动作格式的适配；论文分别评估模仿学习、基础模型及数据迁移。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](https://arxiv.org/abs/2412.13877) | 2025 | 提出 | 跨本体大规模真机数据与统一评测 | 面向「多本体」的操作基准与数据集：汇集多种机器人本体的大规模真机示范，并在统一协议下评测策略跨本体的迁移与泛化能力。它把 VLA 评测从单一本体推向跨本体一致性，是判断「策略学到的是任务还是本体特性」的重要工具。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：成果是多本体、带任务语义与失败信息的真实数据平台，以及不同数据规模和来源下的训练对照；用以研究数据覆盖和迁移，不只有单一榜单分数。

**适用边界**：训练数据规模不是安全场景覆盖率。跨本体评测须注明保留／见过的任务和机器人，不可将全部轨迹既算训练又算独立测试。

## 5. 相关论文（均来自本调研表）

- [RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation](https://arxiv.org/abs/2412.13877)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

训练数据规模不是安全场景覆盖率。跨本体评测须注明保留／见过的任务和机器人，不可将全部轨迹既算训练又算独立测试。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Kun Wu, Chengkai Hou, Jiaming Liu, et al., ‘RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation,’ Robotics: Science and Systems XXI (RSS 2025), 2024, arXiv:2412.13877v3. [论文](https://arxiv.org/abs/2412.13877)；[核查正文](https://arxiv.org/html/2412.13877v3)。

**重点核查位置（章节主题）**：III Data Collection；IV Dataset；V Experiments。

OpenAlex 被引次数：**[23](https://openalex.org/W4414050913)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://x-humanoid-robomind.github.io](https://x-humanoid-robomind.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
