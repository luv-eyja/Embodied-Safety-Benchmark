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
| OpenAlex 引用快照 | [13](https://openalex.org/W4416748905)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] AgiBot World Contributors, Qingwen Bu, Jisong Cai, et al., ‘AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems,’ arXiv preprint, 2025, arXiv:2503.06669v5. [论文](https://doi.org/10.1109/IROS60139.2025.11247088)；[核查正文](https://arxiv.org/html/2503.06669v5)。

**重点核查位置（章节主题）**：Data Collection；Dataset；Experiments。

OpenAlex 被引次数：**[13](https://openalex.org/W4416748905)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://agibot-world.com/](https://agibot-world.com/)；[https://github.com/OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **13** 篇引文论文（清单保留被引最高的 13 篇）；arXiv 摘要命中 2 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://agibot-world.com/](https://agibot-world.com/)；[https://github.com/OpenDriveLab/AgiBot-World](https://github.com/OpenDriveLab/AgiBot-World)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://agibot-world.com/) | https://agibot-world.com/ | 保留文本 12 字符（截断） |
| [repo](https://github.com/OpenDriveLab/AgiBot-World) | https://raw.githubusercontent.com/OpenDriveLab/AgiBot-World/HEAD/README.md | stars 3223，最后推送 2026-05-29，保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://agibot-world.com/ 只返回站名；GitHub repo（3,223 stars，2026-05-29 最后推送）README 链向 HuggingFace 数据、GO-1 模型与 CC BY-NC-SA 4.0（开源许可证） 许可。

**涉及领域**：双臂移动操作的真机数据与训练／评测平台；场景为家庭、零售、工业等真实环境。

**测试目的与构建方法**：基于 AgiBot G1 的标准化遥操作采集，配合采集前验证、本地完整性检查、云端质量审核与语言标注，并保留失败与恢复过程，用于训练 GO-1 等通用策略。

**测试缺陷**：它首先是训练资源而非独立安全压力测试；跨数据源收益依赖任务、训练量与模型配置；数据许可为 CC BY-NC-SA 4.0，商用受限。

**与具身智能安全的相关性**：间接：提供真机失败／恢复样本，可用于学习纠错与安全恢复；本身不定义风险约束，也不产出安全率指标。

**用这个 benchmark 测了什么**：论文报告 GO-1 在复杂任务上的成功率超过 60%，并比较不同预训练数据来源；下游有 PointVLA、X-Distill 等 13 篇引用，2026 年 AgiBot World Challenge 的世界模型赛道有团队报告把动作缺陷率从 48.12% 降到 6.25%。

**本轮核查边界**：数据规模、任务分布与评测协议均引自已发表论文，未下载数据核对。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **2 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| DreamTrue: Action-Faithful Robot World Model with Counterfactual Super…（2026） | DreamTrue（世界模型） | 评测（竞赛赛道提交） | AgiBot World Challenge 2026 世界模型赛道 | 该赛道排名第一；摘要另报动作缺陷率由 48.12% 降到 6.25% |
| Structured Latent Dynamics for Long-Horizon Embodied World Models（2026） | Structured Latent Dynamics，分别接 Ctrl-World 与 EVAC | 评测（在真实轨迹上做世界模型预测） | AgiBot World 真实轨迹上的 nDTW 与 Logic 指标 | nDTW +9.7%（Ctrl-World）、Logic +8.4%（EVAC） |

**原文片段（摘要）**：

- DreamTrue: Action-Faithful Robot World Model with Counterfac…（2026，arXiv）：> our model ranks first in the world model track of the AgiBot World Challenge 2026
- Structured Latent Dynamics for Long-Horizon Embodied World M…（2026，arXiv）：> On real-world AgiBot World trajectories, it improves nDTW by 9.7% with Ctrl-World and Logic by 8.4% with EVAC

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 5 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **CC** | Cumulative safety Cost | 累计安全代价 | 一次 episode 内违规代价的累加，衡量“踩线有多重”而非“有没有踩线”。 |
| **nDTW** | normalized DTW | 归一化 DTW | 把 DTW 距离归一化到 0–1，便于跨任务比较。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **GO-1** | AgiBot GO-1 | AgiBot 通用策略 | AgiBot 随数据集一起发布的通用操作策略。 |
| **teleoperation** | teleoperation | 遥操作 | 人通过手柄、外骨骼或手套远程操控机器人采集数据。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| AgiBot World | 数据集 | 真机双臂操作数据集与平台 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 CC BY-NC-SA 4.0（开源许可证）），不再重复解释。

<!-- glossary:end -->
