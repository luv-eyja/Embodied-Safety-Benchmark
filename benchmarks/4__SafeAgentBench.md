# SafeAgentBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：具身交互环境下的安全任务规划测试。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：安全任务规划  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/shengyin1224/SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Agentic › Cascading Risks |
| 应用领域 | 未标注 |
| 被测对象 | 交互仿真中的安全任务规划 |
| 历史关键词标签（未重新统计） | 任务能力 |
| 评测维度/指标 | 安全任务规划；危险场景下的计划合规率 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 750 个任务、10 类危险、三种任务类型；SafeAgentEnv 提供 17 个高层动作和低层执行器，支持九种代理基线。 |
| 执行环境线索 | 交互仿真中的安全任务规划 |
| OpenAlex 引用快照 | [2](https://openalex.org/W4405562840)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：代理对明确危险与正常长任务中的隐含风险，是否有足够的主动拒绝和安全规划能力？

**评测层级**：交互仿真中的安全任务规划。

## 2. 怎么构建的

**核心场景与条目**：750 个任务、10 类危险、三种任务类型；SafeAgentEnv 提供 17 个高层动作和低层执行器，支持九种代理基线。

**实现与判分**：任务生成后筛选标注，在交互环境执行高层计划；从执行结果与语义两方面评价，分别比较详细、抽象及长时程任务。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178) | 2024 | 提出 | 安全任务规划；危险场景下的计划合规率 | 面向具身 LLM 智能体的安全任务规划评测：在危险场景中检验智能体生成的执行计划是否满足安全要求，是「规划层安全」评测的代表性工作之一，常与 AGENTSAFE、IS-Bench 等一起作为具身智能体安全评测的基线集合。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：对详细危险任务，最有安全意识的基线拒绝率也只有 10%；仅替换底座 LLM 没有稳定解决安全意识不足。成果是可执行危险任务集与统一环境。

**适用边界**：高层动作接口和控制器可能承担部分运动能力，不能与端到端关节 VLA 同分比较；拒绝率低不等于所有任务都成功造成物理后果。

## 5. 相关论文（均来自本调研表）

- [SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents](https://arxiv.org/abs/2412.13178)（2024；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

高层动作接口和控制器可能承担部分运动能力，不能与端到端关节 VLA 同分比较；拒绝率低不等于所有任务都成功造成物理后果。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Sheng Yin, Xianghe Pang, Yuanzhuo Ding, et al., ‘SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents,’ arXiv preprint, 2024, arXiv:2412.13178v5. [论文](https://arxiv.org/abs/2412.13178)；[核查正文](https://arxiv.org/html/2412.13178v5)。

**重点核查位置（章节主题）**：3 Dataset；4.1 Embodied Environment；4.2 Evaluation Methods；5.1；5.3；5.4。

OpenAlex 被引次数：**[2](https://openalex.org/W4405562840)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/shengyin1224/SafeAgentBench](https://github.com/shengyin1224/SafeAgentBench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
