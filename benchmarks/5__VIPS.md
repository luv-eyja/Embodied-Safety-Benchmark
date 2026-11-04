# VIPS

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性、安全。
> **分类依据**：车路协同规划的专用协议与数据扩展；危害指标仍不能等同实车安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：车路协同规划（伪仿真）  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://vips2026.github.io](https://vips2026.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Multi-Agent Planning |
| 应用领域 | 车路协同 |
| 被测对象 | 车路协同伪仿真评测 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 伪仿真评测；开环与闭环的折中 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 基于 V2X-Real 的车辆／路侧同步观测，补充矢量地图与有效配对场景；重点是交叉口遮挡、交通交互和偏离后的恢复。 |
| 执行环境线索 | 车路协同伪仿真评测 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7207785702)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：路侧视角能否改善遮挡下的驾驶规划，并在车辆偏离名义轨迹后保持有效？

**评测层级**：车路协同伪仿真评测。

## 2. 怎么构建的

**核心场景与条目**：基于 V2X-Real 的车辆／路侧同步观测，补充矢量地图与有效配对场景；重点是交叉口遮挡、交通交互和偏离后的恢复。

**实现与判分**：Stage 1 用真实观察，Stage 2 用偏移后的合成观察，合成 EPDMS 评价；提出稀疏协同表示 CoS-V2X，并比较通信量与规划表现。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation](https://arxiv.org/abs/2609.02462) | 2026 | 提出 | 伪仿真评测；开环与闭环的折中 | 指出城市端到端自动驾驶需要在部分可观测与复杂多智能体交互下做稳健决策，交叉路口的严重遮挡与密集车流限制了单车感知能力，推动了车车/车路协同研究；但现有评测协议面临根本权衡——开环评测无法捕捉误差累积与偏离后的恢复，闭环评测昂贵、难以规模化，且常依赖可能存在域差的仿真环境。VIPS 在此之间提出基于伪仿真的评测。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文中多数方法在 Stage 2 下降，协同方法整体较强；CoS-V2X 在所测方法中综合表现最佳，通信带宽需求低于 Uni-V2X。

**适用边界**：伪仿真的合成观察质量会影响排名，并非完全反应式交通闭环；原始 V2X-Real 数据集和本文新增地图／协议的成果应分别归属。

## 5. 相关论文（均来自本调研表）

- [VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation](https://arxiv.org/abs/2609.02462)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

伪仿真的合成观察质量会影响排名，并非完全反应式交通闭环；原始 V2X-Real 数据集和本文新增地图／协议的成果应分别归属。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Hoonhee Cho, Jae-Young Kang, Giwon Lee, et al., ‘VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation,’ arXiv preprint, 2026, arXiv:2609.02462v1. [论文](https://arxiv.org/abs/2609.02462)；[核查正文](https://arxiv.org/html/2609.02462v1)。

**重点核查位置（章节主题）**：3.1 Datasets；3.2 Protocol；3.3 Stage 1；3.4 Stage 2；5.2 Experiments；6 Analysis。

OpenAlex 被引次数：**[0](https://openalex.org/W7207785702)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://vips2026.github.io](https://vips2026.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要检索因名称歧义不作计数。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://vips2026.github.io](https://vips2026.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://vips2026.github.io) | https://vips2026.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://vips2026.github.io（KAIST）声明 Paper、Code、Dataset 均已发布，并给两阶段 V2X 伪仿真示意图。

**涉及领域**：车路协同（V2X）规划基准；用两阶段伪仿真评测协同规划。

**测试目的与构建方法**：Stage 1 用真实观察评估自车轨迹；Stage 2 在专家轨迹附近用合成观察探测策略，给出合成 EPDMS；提出稀疏协同表示 CoS-V2X 并比较通信量与规划表现。

**测试缺陷**：伪仿真的合成观察质量会影响排名；不是完全反应式交通闭环；原始 V2X-Real 数据集与本文新增地图／协议应分别归属；基础设施侧真实性依赖数据采集。

**与具身智能安全的相关性**：中等：碰撞与可行驶区域进指标，且协同感知可减少盲区事故；但两阶段伪仿真仍无法覆盖真实通信延迟与失效。

**用这个 benchmark 测了什么**：论文中多数方法在 Stage 2 下降，协同方法整体较强；CoS-V2X 在所测方法中综合最佳，通信带宽需求低于 Uni-V2X；ECCV（会议／期刊） 2026 Spotlight。

**本轮核查边界**：只读项目页，未下载数据集。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

缩写与多个项目冲突：ViPS（多视觉先验）、ViPS（视频姿态空间）、VIPs（视障人士，多篇 UAV 论文）、VIPS（高斯变分推断算法）。无法区分所指，本轮不给使用明细。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 5 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **EPDMS** | Extended PDMS / Pseudo-simulation Driving Metric Score | 扩展规划综合分 | NAVSIM v2 在 PDMS 基础上加入更严格子项（含伪仿真两阶段）的分数。 |
| **open-loop** | open-loop evaluation | 开环评测 | 按记录好的输入序列评估，不考虑模型输出对后续状态的影响。 |
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |
| **V2X** | Vehicle-to-Everything | 车联万物（车路协同） | 车与车、车与路侧设施的通信协同，用于减少盲区带来的事故。 |
| **UAV** | Unmanned Aerial Vehicle | 无人机 | 无人飞行器；本库中多为“轨迹派生决策”评测，不是完整飞行闭环。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| VIPS | 基准 | 车路协同伪仿真评测 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 ECCV（会议／期刊）），不再重复解释。

<!-- glossary:end -->
