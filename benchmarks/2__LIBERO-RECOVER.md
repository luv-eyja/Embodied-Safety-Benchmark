# LIBERO-RECOVER

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：恢复能力测试；恢复成功不自动表示全过程安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：控制（失败恢复）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://liulin815.github.io/LIBERO-Recovery](https://liulin815.github.io/LIBERO-Recovery)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真自然失败状态恢复 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、对抗/后门安全、失败恢复、任务能力 |
| 评测维度/指标 | 失败识别与恢复成功率（相对纯任务成功率） |
| 基础平台线索 | LIBERO |
| 规模线索 | 收集 2,000 余真实策略运行产生的失败状态；四级恢复从动作重试、动作适配到物体状态与环境恢复，并按空间、物体结构、交互和拓扑能力标注。 |
| 执行环境线索 | 仿真自然失败状态恢复 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7211887144)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：模型在自己的执行错误之后能否恢复，正常起点的高分是否能预测恢复能力？

**评测层级**：仿真自然失败状态恢复。

## 2. 怎么构建的

**核心场景与条目**：收集 2,000 余真实策略运行产生的失败状态；四级恢复从动作重试、动作适配到物体状态与环境恢复，并按空间、物体结构、交互和拓扑能力标注。

**实现与判分**：从存档失败状态继续执行原任务，报告 Recovery Success Rate、Recovery Degradation 和一致性；分级、分能力比较，而不是只加随机初始扰动。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178) | 2026 | 提出 | 失败识别与恢复成功率（相对纯任务成功率） | 指出 LIBERO 上已接近 100% 的成功率具有误导性：真实交互中必然出现抓取失败、碰撞与物体意外移动，机器人不仅要完成任务还要能识别并从中恢复，而这一能力此前基本未被度量。该基准在既有成功率之外补充失败恢复能力的评测，弥合基准成绩与真实可靠性之间的差距。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：表 2 中 GR00T-N1.5 在 LIBERO-Spatial 恢复集的 RSR 从 0.057 提升至混合恢复数据训练后的 0.116；论文同时发现这种收益未稳定转化为正常起点分数。更长动作块通常更难恢复。

**适用边界**：这里的自然失败发生在仿真策略 rollout，并非真实世界事故。失败状态来源策略与筛选流程影响分布，恢复集提升不等于所有失败都可自行纠正。

## 5. 相关论文（均来自本调研表）

- [LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models](https://arxiv.org/abs/2609.05178)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这里的自然失败发生在仿真策略 rollout，并非真实世界事故。失败状态来源策略与筛选流程影响分布，恢复集提升不等于所有失败都可自行纠正。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Lin Liu, Zhicheng Bao, Lu Zhang, et al., ‘LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models,’ arXiv preprint, 2026, arXiv:2609.05178v3. [论文](https://arxiv.org/abs/2609.05178)；[核查正文](https://arxiv.org/html/2609.05178v3)。

**重点核查位置（章节主题）**：2 Failure Collection；3.2 Evaluation Metrics；4.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7211887144)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://liulin815.github.io/LIBERO-Recovery](https://liulin815.github.io/LIBERO-Recovery)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
