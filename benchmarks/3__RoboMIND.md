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
| OpenAlex 引用快照 | [23](https://openalex.org/W4414050913)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Kun Wu, Chengkai Hou, Jiaming Liu, et al., ‘RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation,’ Robotics: Science and Systems XXI (RSS（会议／期刊） 2025), 2024, arXiv:2412.13877v3. [论文](https://arxiv.org/abs/2412.13877)；[核查正文](https://arxiv.org/html/2412.13877v3)。

**重点核查位置（章节主题）**：III Data Collection；IV Dataset；V Experiments。

OpenAlex 被引次数：**[23](https://openalex.org/W4414050913)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://x-humanoid-robomind.github.io](https://x-humanoid-robomind.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **23** 篇引文论文（清单保留被引最高的 23 篇）；arXiv 摘要命中 2 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://x-humanoid-robomind.github.io](https://x-humanoid-robomind.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://x-humanoid-robomind.github.io) | https://x-humanoid-robomind.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://x-humanoid-robomind.github.io 说明 RSS 2025 接收、V2.0 发布于 ModelScope（机构），并列作者与单位。

**涉及领域**：多本体真实操作数据与训练基准；覆盖单臂、双臂、类人平台。

**测试目的与构建方法**：统一遥操作、传感记录、质量筛选与语言标注，提供不同机器人动作格式的适配；论文分别评估模仿学习、基础模型与数据迁移，并发布 V2.0。

**测试缺陷**：训练数据规模不等于安全场景覆盖率；跨本体评测须注明“保留／见过”的任务与机器人；不能把全部轨迹既当训练又当独立测试。

**与具身智能安全的相关性**：弱：它是数据资源，本身不定义风险；但失败信息与多本体覆盖可用于安全策略训练与失效分析。

**用这个 benchmark 测了什么**：成果是多本体、带任务语义与失败信息的真实数据平台与不同数据规模／来源的训练对照；V2.0 报告超过 310K 双臂操作数据；下游 Pelican-Sim 等用它做对照。

**本轮核查边界**：只读项目页，未下载 ModelScope 数据。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **2 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset（2025） | —（该文即数据集本身的 2.0 版） | 自更新（发布更大规模数据） | 六种机器人本体、739 个复杂任务、310K+ 双臂轨迹 | 产出 2.0 数据集；不是第三方使用分数 |
| Pelican-Sim 1.0: A General World Model Simulator for Embodied Intellig…（2026） | Pelican-Sim（世界模型模拟器） | 训练数据（约百万条真实 + 仿真轨迹）后评测 | 动作可控性与视频质量；在 RoboMIND 上报告 PSNR 增益 | 在 RoboMIND 上 PSNR 比最强基线高 2.080（同段另报 AgiBotWorld Beta +4.636、RoboTwin +10.343） |

**原文片段（摘要）**：

- RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dat…（2025，arXiv）：> a comprehensive real-world dataset comprising over 310K dual-arm manipulation trajectories across six robot embodiments
- Pelican-Sim 1.0: A General World Model Simulator for Embodie…（2026，arXiv）：> PSNR improves over the strongest evaluated baselines by 4.636 on AgiBotWorld Beta, 2.080 on RoboMIND, and 10.343 on RoboTwin

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 4 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **PSNR** | Peak Signal-to-Noise Ratio | 峰值信噪比 | 图像质量的常用指标，越高越接近原图。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **teleoperation** | teleoperation | 遥操作 | 人通过手柄、外骨骼或手套远程操控机器人采集数据。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| RoboMIND | 数据集 | 多本体真实操作数据集 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 RSS（会议／期刊）、ModelScope（机构）），不再重复解释。

<!-- glossary:end -->
