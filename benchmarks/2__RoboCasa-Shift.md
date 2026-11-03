# RoboCasa-Shift

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：鲁棒性。
> **分类依据**：已有平台上的阶段鲁棒性测试协议。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：感知 + 长时程控制（阶段感知诊断）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/HaochengWang23/RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 长时程操作阶段鲁棒性 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 |
| 基础平台线索 | RoboCasa、RoboCasa365 |
| 规模线索 | 从 16 个候选任务筛出 4 个干净条件至少成功 12/20 的任务；4 种视觉扰动、3 档强度加干净条件，4×20×13=1,040 rollout。 |
| 执行环境线索 | 长时程操作阶段鲁棒性 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7223122581)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：同样的总成功率下降，是否来自长任务中完全不同阶段的失误？

**评测层级**：长时程操作阶段鲁棒性。

## 2. 怎么构建的

**核心场景与条目**：从 16 个候选任务筛出 4 个干净条件至少成功 12/20 的任务；4 种视觉扰动、3 档强度加干净条件，4×20×13=1,040 rollout。

**实现与判分**：固定初始状态、指令和策略种子作配对，记录子目标及首次失败阶段。另做零变化相机控制，用于量化运行中的非确定性。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026 | 提出 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 | 针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：相机 L2 与模糊 L1 的成功下降同为 0.188，首次阶段失败比例却为 19% 与 36.4%；零变化相机控制仍有 8/80 次结果翻转。

**适用边界**：仅分析 GR00T-N1.5 和干净条件可完成的四个任务，存在明确的筛选边界。零扰动的非确定性必须从扰动效应中区分。

## 5. 相关论文（均来自本调研表）

- [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

仅分析 GR00T-N1.5 和干净条件可完成的四个任务，存在明确的筛选边界。零扰动的非确定性必须从扰动效应中区分。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Haocheng Wang, Youquan Liu, Weiyu Guo, et al., ‘RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation,’ arXiv preprint, 2026, arXiv:2610.27861v1. [论文](https://arxiv.org/abs/2610.27861)；[核查正文](https://arxiv.org/html/2610.27861v1)。

**重点核查位置（章节主题）**：III-A Task Selection；III-C Evaluation；IV-A；IV-B；IV-D。

OpenAlex 被引次数：**[0](https://openalex.org/W7223122581)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/HaochengWang23/RoboCasa-Shift](https://github.com/HaochengWang23/RoboCasa-Shift)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
