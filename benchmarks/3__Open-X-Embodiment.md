# Open X-Embodiment

<!-- survey-classification:start -->
> **统一调研分类**：训练数据集；具身研究底座；目标：能力。
> **分类依据**：主要是异构数据整合与训练项目，不存在一套全项目统一安全分。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：跨本体真机数据  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 0、使用 1；方法参考另标）
> **证据级别**：原表 C；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)；[https://github.com/google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models |
| 年份 | 2023（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 跨本体真机训练数据与模型 |
| 历史关键词标签（未重新统计） | 任务能力 |
| 评测维度/指标 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 原论文聚合 22 种本体、100 万余真实轨迹和 527 种技能；不同来源的相机、动作、任务分布明显异构。 |
| 执行环境线索 | 跨本体真机训练数据与模型 |
| 来源审计 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)；external_original_paper |
| 来源核验依据 | AgiBot World Colosseo 论文使用 Open X-Embodiment；官方仓库也将该论文列为 Open X-Embodiment 的首篇论文。 |
| OpenAlex 引用快照 | [111](https://openalex.org/W4387764390)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：来自不同实验室与机器人形态的数据能否共同训练可迁移的操作策略？

**评测层级**：跨本体真机训练数据与模型。

## 2. 怎么构建的

**核心场景与条目**：原论文聚合 22 种本体、100 万余真实轨迹和 527 种技能；不同来源的相机、动作、任务分布明显异构。

**实现与判分**：统一到 RLDS 数据表示并建立动作／观察适配，以 RT-X 等模型比较单来源与跨本体训练，分别测试已有任务和域外能力。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088) | 2025 | 使用 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 | 以「可扩展的机器人数据」回应通用操作的真机挑战：AgiBot World 是含 100 万余条轨迹、217 个任务、5 类部署场景的大规模平台，数据规模比既有数据集高一个数量级；标准化采集流水线配合人在环校验保证质量与分布多样性，并可从夹爪扩展到灵巧手与视触觉传感器以获取细粒度技能。在数据之上提出通用策略 Genie Operator-1（GO-1）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：实验支持跨机器人数据存在正迁移，但并不意味着任意数据混合都同样有效。成果是数据联盟、标准化接口以及跨本体策略。

**适用边界**：这是训练数据集合与研究项目，不是具有单一冻结测试集的安全 benchmark；不同论文使用的混合比例、过滤和版本必须注明。引用量对应论文记录，不等于每个子数据集的影响力。

## 5. 相关论文（均来自本调研表）

- [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088)（2025；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这是训练数据集合与研究项目，不是具有单一冻结测试集的安全 benchmark；不同论文使用的混合比例、过滤和版本必须注明。引用量对应论文记录，不等于每个子数据集的影响力。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Open X-Embodiment Collaboration, Abby O'Neill, Abdul Rehman, et al., ‘Open X-Embodiment: Robotic Learning Datasets and RT-X Models,’ arXiv preprint, 2023, arXiv:2310.08864v9. [论文](https://arxiv.org/abs/2310.08864)；[核查正文](https://arxiv.org/html/2310.08864v9)。

**重点核查位置（章节主题）**：III Data Collection；IV Data Format；V Experiments。

OpenAlex 被引次数：**[111](https://openalex.org/W4387764390)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)；[https://github.com/google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
