# SafeBench

<!-- survey-classification:start -->
> **统一调研分类**：评测框架；直接具身评测；目标：能力、鲁棒性、安全。
> **分类依据**：主要整合风险生成、路线、驾驶策略与评分的统一框架，附任务集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：自动驾驶安全评测平台  
> **分类**：具身安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://safebench.github.io](https://safebench.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles |
| 年份 | 2022（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Planning › Trajectory Planning |
| 应用领域 | 自动驾驶 |
| 被测对象 | 驾驶安全关键场景评测 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、对抗/后门安全 |
| 评测维度/指标 | 统一仿真平台 + 安全关键场景生成；跨平台可比性 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 基于 CARLA，八类 NHTSA 风格关键场景，每类十种变化；四种场景生成算法、四种 RL 驾驶算法与四种观察输入。 |
| 执行环境线索 | 驾驶安全关键场景评测 |
| OpenAlex 引用快照 | [48](https://openalex.org/W7133222348)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 2 个缩写／技术词，并标出 3 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：在相同平台和路线下，不同危险场景生成方法对驾驶策略的压力有何差别？

**评测层级**：驾驶安全关键场景评测。

## 2. 怎么构建的

**核心场景与条目**：基于 CARLA，八类 NHTSA 风格关键场景，每类十种变化；四种场景生成算法、四种 RL 驾驶算法与四种观察输入。

**实现与判分**：统一场景、路线与控制接口，从安全、功能和驾驶礼仪三个层面评分；比较正常场景与安全关键场景，定位平均驾驶成绩遗漏的弱点。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682) | 2022 | 提出 | 统一仿真平台 + 安全关键场景生成；跨平台可比性 | 指出机器学习系统对对抗操纵与自然分布偏移都脆弱，而自然驾驶场景中安全关键情形极其稀有，传统路测需要数亿英里；已有的 AD 评测方法又各自基于不同仿真平台、场景类型、生成算法与路线，难以横向比较。SafeBench 把评测统一到一个基准平台上，使安全评测可复现、可比较（NeurIPS（会议／期刊） 2022）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：4D 输入条件下 TD3 的综合分由正常场景 0.830 降至关键场景 0.518，且正常与关键场景的算法排名不同。

**适用边界**：综合分包含多种归一化指标和权重，不能当碰撞概率；实验主要是指定 RL 策略，不能直接推断当前全部端到端驾驶系统。

## 5. 相关论文（均来自本调研表）

- [SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682)（2022；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

综合分包含多种归一化指标和权重，不能当碰撞概率；实验主要是指定 RL 策略，不能直接推断当前全部端到端驾驶系统。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Chejian Xu, Wenhao Ding, Weijie Lyu, et al., ‘SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles,’ arXiv preprint, 2022, arXiv:2206.09682v4. [论文](https://arxiv.org/abs/2206.09682)；[核查正文](https://arxiv.org/html/2206.09682v4)。

**重点核查位置（章节主题）**：3.1 Platform；3.2 Scenarios；3.4 Evaluation Metrics；4.3 Benchmark Results。

OpenAlex 被引次数：**[48](https://openalex.org/W7133222348)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://safebench.github.io](https://safebench.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **48** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要检索因名称歧义不作计数。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://safebench.github.io](https://safebench.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://safebench.github.io) | https://safebench.github.io | 保留文本 1460 字符（截断） |

**项目页显示**：项目页 https://safebench.github.io 说明三大特点（并行运行、可扩展场景、综合指标）并明确基于 CARLA。

**涉及领域**：自动驾驶的安全关键场景评测；基于 CARLA 的场景化测试平台。

**测试目的与构建方法**：统一场景、路线与控制接口，从安全、功能与驾驶礼仪三个层面评分；在同一地图上并行运行多场景以提高效率，比较正常场景与安全关键场景。

**测试缺陷**：综合分包含多种归一化指标与权重，不能当碰撞概率；实验主要是指定 RL 策略，不能直接推断当前全部端到端系统；场景由生成器产生，覆盖受限于生成策略。

**与具身智能安全的相关性**：直接：场景本身就是安全关键构造（切入、遮挡、异常行为），指标含碰撞与偏离；是自动驾驶安全测试的常用底座。

**用这个 benchmark 测了什么**：4D 输入下 TD3 的综合分由正常场景 0.830 降到关键场景 0.518，且正常／关键场景的算法排名不同——平均分排序会掩盖安全短板；下游 ChatScene 等用它生成安全关键场景。

**本轮核查边界**：只读项目页介绍，未安装 CARLA 运行场景。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **1 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Traffic Scene Generation from Natural Language Description for Autonom…（2024） | 场景生成方法 + 被测自动驾驶策略 | 评测（生成场景后测碰撞率） | SafeBench 三个关键场景，平均碰撞率 | 平均碰撞率 3.5%（三个关键场景中的最低值由该方法取得） |

**原文片段（摘要）**：

- Traffic Scene Generation from Natural Language Description f…（2024，arXiv）：> our method achieves the lowest average collision rate (3.5%) across three critical scenarios

**口径提示**：**同名坑**：另有一批多模态大模型安全论文也把数据集叫 SafeBench（例如 MML 越狱论文报告 “97.80% on SafeBench”、PRISM 与 “Internal Activation Revision” 也提到 SafeBench／MM-SafetyBench）。那些是 LVLM 越狱基准，不是本条自动驾驶安全基准；本轮只收自动驾驶侧的使用记录。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 2 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **RL** | Reinforcement Learning | 强化学习 | 用奖励信号优化策略，区别于用示范做监督学习。 |
| **CARLA** | CARLA | CARLA 自动驾驶仿真器 | 开放源码的城市驾驶仿真器，自动驾驶安全测试的事实底座。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| SafeBench | 基准 | 自动驾驶安全关键场景平台（另有同名 LVLM 基准） |
| CARLA | 仿真平台 | 开源城市驾驶仿真器 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 NeurIPS（会议／期刊）），不再重复解释。

<!-- glossary:end -->
