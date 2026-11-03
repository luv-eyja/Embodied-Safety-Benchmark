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
| OpenAlex 引用快照 | [48](https://openalex.org/W7133222348)；2026-11-03 |

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
| [SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682) | 2022 | 提出 | 统一仿真平台 + 安全关键场景生成；跨平台可比性 | 指出机器学习系统对对抗操纵与自然分布偏移都脆弱，而自然驾驶场景中安全关键情形极其稀有，传统路测需要数亿英里；已有的 AD 评测方法又各自基于不同仿真平台、场景类型、生成算法与路线，难以横向比较。SafeBench 把评测统一到一个基准平台上，使安全评测可复现、可比较（NeurIPS 2022）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：4D 输入条件下 TD3 的综合分由正常场景 0.830 降至关键场景 0.518，且正常与关键场景的算法排名不同。

**适用边界**：综合分包含多种归一化指标和权重，不能当碰撞概率；实验主要是指定 RL 策略，不能直接推断当前全部端到端驾驶系统。

## 5. 相关论文（均来自本调研表）

- [SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles](https://arxiv.org/abs/2206.09682)（2022；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

综合分包含多种归一化指标和权重，不能当碰撞概率；实验主要是指定 RL 策略，不能直接推断当前全部端到端驾驶系统。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Chejian Xu, Wenhao Ding, Weijie Lyu, et al., ‘SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles,’ arXiv preprint, 2022, arXiv:2206.09682v4. [论文](https://arxiv.org/abs/2206.09682)；[核查正文](https://arxiv.org/html/2206.09682v4)。

**重点核查位置（章节主题）**：3.1 Platform；3.2 Scenarios；3.4 Evaluation Metrics；4.3 Benchmark Results。

OpenAlex 被引次数：**[48](https://openalex.org/W7133222348)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://safebench.github.io](https://safebench.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
