# Trap-LIBERO / Trap-RoboTwin

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：安全方法附带两套具名受控诊断任务；不概括为普通鲁棒性。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：配置化失败后门  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://john-liua.github.io/TrapVLA](https://john-liua.github.io/TrapVLA)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | VLA 定向失效诊断／安全研究 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、对抗/后门安全、失败恢复 |
| 评测维度/指标 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 |
| 基础平台线索 | LIBERO、RoboTwin |
| 规模线索 | 在 LIBERO 与 RoboTwin 中分别考察过早闭合、抓取偏移、过早释放及释放偏移等失效类别，并提供模拟及有限真机分析。 |
| 执行环境线索 | VLA 定向失效诊断／安全研究 |
| 来源审计 | [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明构建 Trap-LIBERO 与 Trap-RoboTwin。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7204530163)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：干净任务分数较高时，是否仍可能隐藏只在特定条件下出现的定向操作失败？

**评测层级**：VLA 定向失效诊断／安全研究。

## 2. 怎么构建的

**核心场景与条目**：在 LIBERO 与 RoboTwin 中分别考察过早闭合、抓取偏移、过早释放及释放偏移等失效类别，并提供模拟及有限真机分析。

**实现与判分**：论文将正常任务效用与特定失效目标的达成程度分开统计，结合轨迹和动作层信号检查失效是否符合指定类型；本条仅记录评测层设计。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578) | 2026 | 提出 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 | 提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文展示干净成功率保持较高时仍可出现定向失效，说明标准成功率不足以筛查策略完整性；提供两套受控安全评测任务。

**适用边界**：论文结果依赖特定威胁假设、模型与任务；不能推断任意部署模型都存在此类问题。正常成功和配置失效指标不是同一分母或同一目标。

## 5. 相关论文（均来自本调研表）

- [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](https://arxiv.org/abs/2608.26578)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

论文结果依赖特定威胁假设、模型与任务；不能推断任意部署模型都存在此类问题。正常成功和配置失效指标不是同一分母或同一目标。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, et al., ‘TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes,’ arXiv preprint, 2026, arXiv:2608.26578v1. [论文](https://arxiv.org/abs/2608.26578)；[核查正文](https://arxiv.org/html/2608.26578v1)。

**重点核查位置（章节主题）**：Task Definition；Evaluation Metrics；Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7204530163)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://john-liua.github.io/TrapVLA](https://john-liua.github.io/TrapVLA)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
