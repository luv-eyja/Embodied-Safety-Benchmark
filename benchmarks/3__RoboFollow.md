# RoboFollow

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：控制视觉捷径的指令遵循测试，不等同危险指令评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：高场景熵指令遵循诊断  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/AutoLab-SAI-SJTU/RoboFollow](https://github.com/AutoLab-SAI-SJTU/RoboFollow)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › Instruction Understanding |
| 应用领域 | 未标注 |
| 被测对象 | 语言驱动的操作分支选择 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 高场景熵任务、L0–L3 分层诊断协议；语言必要性 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 同一视觉场景包含多个都可执行的分支，围绕空间、属性、轨迹、逻辑四类任务；L0 基础、L1 布局变化、L2 语义重组、L3 二者组合。 |
| 执行环境线索 | 语言驱动的操作分支选择 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214246107)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：模型是否真正依据指令选择动作，而不是根据画面猜测训练中最常见的任务？

**评测层级**：语言驱动的操作分支选择。

## 2. 怎么构建的

**核心场景与条目**：同一视觉场景包含多个都可执行的分支，围绕空间、属性、轨迹、逻辑四类任务；L0 基础、L1 布局变化、L2 语义重组、L3 二者组合。

**实现与判分**：通过高场景熵让图像不能唯一确定任务，保持基础动作和物体能力的可比性；把意图选择 Intent 和执行 Execution 分开评分，评测九种 VLA／WAM，并作小型真机试验。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](https://arxiv.org/abs/2609.25636) | 2026 | 提出 | 高场景熵任务、L0–L3 分层诊断协议；语言必要性 | 指出现代具身智能体的成功率远高于其真实指令遵循能力，根源是一种结构性性质「低场景熵」：当视觉场景只容许一个有效任务时，语言变得冗余，策略几乎不用语言也能拿高分。RoboFollow 据此设计三条原则——高场景熵（每个训练场景支持多个运动学上不同的任务分支，使仅凭视觉不足、必须依赖语言）、分层诊断协议（L0–L3 逐级扰动视觉布局与语义，检验等价指令是否行为一致、不同指令是否行为可分）等。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：标准基准的高成功率不能稳定预测指令遵循能力；分阶段诊断能区分选错目标与选对但做不成。成果是控制视觉捷径的任务生成与诊断协议。

**适用边界**：L0–L3 是因素组合，并非保证对每个模型单调变难；简化物体和动作有助于归因，却缩小了真实开放场景覆盖。

## 5. 相关论文（均来自本调研表）

- [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](https://arxiv.org/abs/2609.25636)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

L0–L3 是因素组合，并非保证对每个模型单调变难；简化物体和动作有助于归因，却缩小了真实开放场景覆盖。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Chang Guo, Yukun Xie, Bohan Tan, et al., ‘RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents,’ arXiv preprint, 2026, arXiv:2609.25636v1. [论文](https://arxiv.org/abs/2609.25636)；[核查正文](https://arxiv.org/html/2609.25636v1)。

**重点核查位置（章节主题）**：Benchmark Construction；Evaluation Protocol；Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7214246107)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/AutoLab-SAI-SJTU/RoboFollow](https://github.com/AutoLab-SAI-SJTU/RoboFollow)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
