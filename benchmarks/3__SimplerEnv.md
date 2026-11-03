# SimplerEnv

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：主要为真机策略设计可验证的仿真代理评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（评测基础设施）  
> **分类**：VLA 能力  
> **关联论文**：本表 3 篇（提出 1、使用 2；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://simpler-env.github.io/](https://simpler-env.github.io/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Evaluating Real-World Robot Manipulation Policies in Simulation |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 真机策略的仿真代理评测 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 仿真-真机对齐；控制与视觉差异消解；与真机成功率的相关性 |
| 基础平台线索 | LIBERO、SimplerEnv |
| 规模线索 | Google Robot 与 WidowX BridgeV2 设置下的罐子、移动物体、抽屉等刚体操作；重点是模拟与真实的配对测试。 |
| 执行环境线索 | 真机策略的仿真代理评测 |
| OpenAlex 引用快照 | [4](https://openalex.org/W4396822572)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：不反复占用真实机器人，能否用模拟可靠预测实机策略的相对表现？

**评测层级**：真机策略的仿真代理评测。

## 2. 怎么构建的

**核心场景与条目**：Google Robot 与 WidowX BridgeV2 设置下的罐子、移动物体、抽屉等刚体操作；重点是模拟与真实的配对测试。

**实现与判分**：以 SAPIEN 搭建环境，缩小控制与视觉差距；Visual Matching 匹配真实画面，Variant Aggregation 汇总环境变体，报告排序违背 MMRV 和 Pearson 相关。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802) | 2026 | 使用 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 | 指出刚体基准中的任务成功并不能说明模型是否保全了物体。ManiPhysicsZoo 汇总文献支撑的材质属性、3D 网格与参考文献形成可复用物体资产，再由基于求解器的评估依据几何、材质与抓取条件计算损伤阈值并与实测接触力比较，从而在 LIBERO 与 SimplerEnv 上区分「完成任务」与「安全完成任务」，公开 VLA 检查点在两者间存在显著差距。 |
| [Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)](https://arxiv.org/abs/2405.05941) | 2024 | 提出 | 仿真-真机对齐；控制与视觉差异消解；与真机成功率的相关性 | 直面「真机评测不可扩展且难复现」的问题：指出控制差异与视觉差异是仿真评测不可靠的两个关键来源，并提出无需构建全保真数字孪生的缓解手段，使仿真评测结果与真机表现对齐。该工作为 VLA 提供了一条低成本、可复现的能力评测路径，也是后续大量 VLA 论文采用的仿真评测协议来源。 |
| [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245) | 2026 | 使用 | 时空关系与人类意图推理；社会合规导航 | 指出机器人在动态、以人为中心的环境中导航需要基于稳健场景理解的社会合规决策；近期 VLM 展现出物体识别、常识推理与情境理解等能力，看似契合社会导航的需求，但 VLM 能否准确理解复杂的社会导航场景（例如推断智能体之间的时空关系与人的意图）仍不清楚——而这正是安全且社会合规导航的前提。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：Google Robot 六个 checkpoint 的任务平均 Pearson r：验证 MSE 为 0.308，VarAgg 为 0.778，VisMatch 为 0.924；VisMatch 的 MMRV 为 0.056。

**适用边界**：相关性证明的是所测任务／策略上的相对预测价值，不是任意物体动力学或绝对成功率的等价性。原论文以刚体、已知真实设置为主。

## 5. 相关论文（均来自本调研表）

- [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)（2026；使用）
- [Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)](https://arxiv.org/abs/2405.05941)（2024；提出）
- [STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction](https://arxiv.org/abs/2609.40245)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

相关性证明的是所测任务／策略上的相对预测价值，不是任意物体动力学或绝对成功率的等价性。原论文以刚体、已知真实设置为主。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Xuanlin Li, Kyle Hsu, Jiayuan Gu, et al., ‘Evaluating Real-World Robot Manipulation Policies in Simulation,’ arXiv preprint, 2024, arXiv:2405.05941v1. [论文](https://arxiv.org/abs/2405.05941)；[核查正文](https://arxiv.org/html/2405.05941v1)。

**重点核查位置（章节主题）**：III-B Metrics；IV Control and Visual Gaps；V SIMPLER；VI-B Correlations。

OpenAlex 被引次数：**[4](https://openalex.org/W4396822572)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://simpler-env.github.io/](https://simpler-env.github.io/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 2 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
