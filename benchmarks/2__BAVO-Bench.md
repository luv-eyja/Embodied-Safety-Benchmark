# BAVO-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：评估主动观察和遮挡鲁棒性，没有据遮挡推断安全约束。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：遮挡下的主动视觉恢复  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 主动视觉 |
| 被测对象 | 仿真双臂主动视觉 |
| 历史关键词标签（未重新统计） | 物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 5 个双臂任务，一臂操作、一臂携带相机；Clean、Stage 和随机时刻遮挡三种条件，每任务 100 条 VR 示范，共 500 条。 |
| 执行环境线索 | 仿真双臂主动视觉 |
| 来源审计 | [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce BAVO-Bench。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214940409)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：遮挡发生后，机器人能否主动移动观察相机，再继续操作？

**评测层级**：仿真双臂主动视觉。

## 2. 怎么构建的

**核心场景与条目**：5 个双臂任务，一臂操作、一臂携带相机；Clean、Stage 和随机时刻遮挡三种条件，每任务 100 条 VR 示范，共 500 条。

**实现与判分**：用阶段相关遮挡数据训练，评估 SR、任务进展 TPS 和相机运动带来的可见性增益 CVG，区分真实主动观察与单纯视觉恢复。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292) | 2026 | 提出 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 | 指出物理主动视觉允许机器人在任务相关观测不可靠时改变视角，但现有操作基准对「策略如何在执行中从遮挡恢复」支持有限。BAVO-Bench 通过 Clean、Stage Occlusion 与 Random-time Occlusion 三种条件系统控制外部可见性，同时评测操作性能与主动视觉恢复能力；作者据此提出联合视角与操作控制的 A-FAR 策略。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：A-FAR 的 Clean／Stage／随机遮挡 SR 为 51.3%／63.7%／18.7%。训练匹配的 Stage 可能比 Clean 更高，不能假定难度单调；随机遮挡明显更难。

**适用边界**：ACT、ManiFlow、A-FAR 使用三种种子，π0.5 的训练设置不同，不能将所有行当等预算比较；可见性增益也不能替代任务成功。

## 5. 相关论文（均来自本调研表）

- [Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation](https://arxiv.org/abs/2609.37292)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

ACT、ManiFlow、A-FAR 使用三种种子，π0.5 的训练设置不同，不能将所有行当等预算比较；可见性增益也不能替代任务成功。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Kaijun Luo, Yudi Huang, Qijun Zhong, et al., ‘Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation,’ arXiv preprint, 2026, arXiv:2609.37292v1. [论文](https://arxiv.org/abs/2609.37292)；[核查正文](https://arxiv.org/html/2609.37292v1)。

**重点核查位置（章节主题）**：3.2 Benchmark；5.1 Experimental Setup；5.2 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7214940409)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://hcplab-sysu.github.io/BAVO-Bench](https://hcplab-sysu.github.io/BAVO-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
