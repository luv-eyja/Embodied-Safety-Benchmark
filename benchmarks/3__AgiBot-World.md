# AgiBot World

<!-- survey-classification:start -->
> **统一调研分类**：训练数据集；具身研究底座；目标：能力。
> **分类依据**：主要贡献为大规模实机采集、标准化数据及训练模型。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：百万轨迹真机平台  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://agibot-world.com/](https://agibot-world.com/)；[https://github.com/OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 真机大规模数据集及训练评测 |
| 历史关键词标签（未重新统计） | 任务能力 |
| 评测维度/指标 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 100 万余轨迹、217 任务、3,000 余物体，覆盖家庭、零售、工业、餐饮、办公五域；在约 4,000 平方米采集设施中运行。 |
| 执行环境线索 | 真机大规模数据集及训练评测 |
| OpenAlex 引用快照 | [13](https://openalex.org/W4416748905)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何以稳定的数据质量，扩展多任务机器人学习所需的真实示范规模？

**评测层级**：真机大规模数据集及训练评测。

## 2. 怎么构建的

**核心场景与条目**：100 万余轨迹、217 任务、3,000 余物体，覆盖家庭、零售、工业、餐饮、办公五域；在约 4,000 平方米采集设施中运行。

**实现与判分**：基于 AgiBot G1 的标准化遥操作，结合采集前验证、本地完整性检查、云端质量审核和语言标注；包含失败恢复过程，训练 GO-1 等通用策略。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088) | 2025 | 提出 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 | 以「可扩展的机器人数据」回应通用操作的真机挑战：AgiBot World 是含 100 万余条轨迹、217 个任务、5 类部署场景的大规模平台，数据规模比既有数据集高一个数量级；标准化采集流水线配合人在环校验保证质量与分布多样性，并可从夹爪扩展到灵巧手与视触觉传感器以获取细粒度技能。在数据之上提出通用策略 Genie Operator-1（GO-1）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文报告 GO-1 在复杂任务上的成功率超过 60%，并比较不同预训练数据来源的效果；主要成果是百万级实机数据、采集体系和模型。

**适用边界**：它首先是训练资源，不是独立的安全压力测试；跨数据源收益依赖任务、训练量和模型设置，不能把摘要中的百分比改写成未经确认的百分点。

## 5. 相关论文（均来自本调研表）

- [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

它首先是训练资源，不是独立的安全压力测试；跨数据源收益依赖任务、训练量和模型设置，不能把摘要中的百分比改写成未经确认的百分点。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] AgiBot World Contributors, Qingwen Bu, Jisong Cai, et al., ‘AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems,’ arXiv preprint, 2025, arXiv:2503.06669v5. [论文](https://doi.org/10.1109/IROS60139.2025.11247088)；[核查正文](https://arxiv.org/html/2503.06669v5)。

**重点核查位置（章节主题）**：Data Collection；Dataset；Experiments。

OpenAlex 被引次数：**[13](https://openalex.org/W4416748905)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://agibot-world.com/](https://agibot-world.com/)；[https://github.com/OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
