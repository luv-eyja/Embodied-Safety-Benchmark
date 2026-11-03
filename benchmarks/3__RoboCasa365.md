# RoboCasa365

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：在平台上建立扩展任务数据和多任务／持续学习协议。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：大规模日常任务训练与评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 0、使用 1；方法参考另标）
> **证据级别**：原表 C；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robocasa.ai/](https://robocasa.ai/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 大规模日常操作与持续学习 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 |
| 基础平台线索 | RoboCasa、RoboCasa365 |
| 规模线索 | 365 任务、2,500 厨房，约 600 小时人类数据与 1,600 小时合成数据；65 原子任务、300 复合任务。目标评测分原子、已见复合和未见复合。 |
| 执行环境线索 | 大规模日常操作与持续学习 |
| 来源审计 | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)；external_original_paper |
| 来源核验依据 | RoboCasa-Shift 论文明确说明其 benchmark built on RoboCasa365；原始 RoboCasa365 论文不在当前 192 条本库记录中。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7133954504)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：扩大任务、场景和示范后，策略能否掌握复合任务、迁移未见组合并持续学习？

**评测层级**：大规模日常操作与持续学习。

## 2. 怎么构建的

**核心场景与条目**：365 任务、2,500 厨房，约 600 小时人类数据与 1,600 小时合成数据；65 原子任务、300 复合任务。目标评测分原子、已见复合和未见复合。

**实现与判分**：分别设置多任务训练、预训练后微调、四阶段终身学习；严格区分预训练与目标示范，按示范量、任务组合和场景划分比较。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026 | 使用 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 | 针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：终身学习实验中，原子任务成功率从第一阶段 41.5% 降至第四阶段 10.6%，展示持续学习中的明显遗忘；提供开放模型和不同数据量协议。

**适用边界**：365 个任务不全都属于同一个测试拆分；上述退化来自指定训练流程，不代表所有持续学习算法。大规模合成训练收益也不能直接当安全改进。

## 5. 相关论文（均来自本调研表）

- [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

365 个任务不全都属于同一个测试拆分；上述退化来自指定训练流程，不代表所有持续学习算法。大规模合成训练收益也不能直接当安全改进。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, et al., ‘RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots,’ arXiv preprint, 2026, arXiv:2603.04356v1. [论文](https://arxiv.org/abs/2603.04356)；[核查正文](https://arxiv.org/html/2603.04356v1)。

**重点核查位置（章节主题）**：3.3 Tasks；3.4 Datasets；4.1 Multi-task training；4.2 Foundation model training；4.3 Lifelong learning。

OpenAlex 被引次数：**[0](https://openalex.org/W7133954504)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://robocasa.ai/](https://robocasa.ai/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
