# STARS

<!-- survey-classification:start -->
> **统一调研分类**：方法论文；具身研究底座；目标：能力。
> **分类依据**：提出时空图自编码表征，使用已有数据集，不是提出新 benchmark。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：社会导航时空推理  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 0、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://larg.github.io/stars](https://larg.github.io/stars)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › World Model |
| 应用领域 | 社会导航 |
| 被测对象 | 表征学习方法；并非新 benchmark |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 将多主体状态构成同构或异构时空图，以自监督图自编码器学习关系表征，再用线性探针评估不同标注量和跨数据迁移。 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 使用已有 SEAN Together 与 SocialNav-SUB 数据，研究短时窗内人／机器人群体运动、社会场景和主观人类感受。 |
| 执行环境线索 | 表征学习方法；并非新 benchmark |
| OpenAlex 引用快照 | [0](https://openalex.org/W7215077318)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何在社会导航数据稀缺时，从运动与交互关系中学习兼顾空间和社会语义的表征？

**评测层级**：表征学习方法；并非新 benchmark。

## 2. 怎么构建的

**核心场景与条目**：使用已有 SEAN Together 与 SocialNav-SUB 数据，研究短时窗内人／机器人群体运动、社会场景和主观人类感受。

**实现与判分**：将多主体状态构成同构或异构时空图，以自监督图自编码器学习关系表征，再用线性探针评估不同标注量和跨数据迁移。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245) | 2026 | 方法 | 时空关系与人类意图推理；社会合规导航 | 将多主体状态构成同构或异构时空图，以自监督图自编码器学习关系表征，再用线性探针评估不同标注量和跨数据迁移。SocialNav-SUB 上 STARS-He 的宏 F1 从 1% 标注的 0.362 到全标注的 0.503；同架构端到端有监督对照为 0.445。成果是表征方法，不是重新提出上述数据集。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：SocialNav-SUB 上 STARS-He 的宏 F1 从 1% 标注的 0.362 到全标注的 0.503；同架构端到端有监督对照为 0.445。成果是表征方法，不是重新提出上述数据集。

**适用边界**：保留此卡作为方法参考，不能计作新增 benchmark 的成果；F1 衡量下游分类，不是社交导航碰撞率或人类偏好因果效应。

## 5. 相关论文（均来自本调研表）

- [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245)（2026；方法）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

保留此卡作为方法参考，不能计作新增 benchmark 的成果；F1 衡量下游分类，不是社交导航碰撞率或人类偏好因果效应。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Nathan Tsoi, Michael J. Munje, Tejas Oberoi, et al., ‘STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction,’ arXiv preprint, 2026, arXiv:2609.40245v3. [论文](https://arxiv.org/abs/2609.40245)；[核查正文](https://arxiv.org/html/2609.40245v3)。

**重点核查位置（章节主题）**：3.3 Graph Construction；3.4 Autoencoder；3.5 Linear Probing；4.1 Downstream Performance；5 Limitations。

OpenAlex 被引次数：**[0](https://openalex.org/W7215077318)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://larg.github.io/stars](https://larg.github.io/stars)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
