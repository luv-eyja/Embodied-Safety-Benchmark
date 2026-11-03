# RoboCasa

<!-- survey-classification:start -->
> **统一调研分类**：仿真平台；具身研究底座；目标：能力。
> **分类依据**：主要提供大规模交互厨房、资产和数据生成；同时有配套任务评测。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（日常场景规模化）  
> **分类**：VLA 能力  
> **关联论文**：本表 4 篇（提出 1、使用 3；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robocasa.ai/](https://robocasa.ai/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充、本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 日常操作仿真平台 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、失败恢复、任务能力 |
| 评测维度/指标 | 以 robosuite／MuJoCo 和大量厨房、物体资产构建交互场景，结合人类示范与自动数据生成，系统变化场景、对象和任务组合。 |
| 基础平台线索 | RoboCasa、RoboCasa365 |
| 规模线索 | 原版 100 个厨房任务，包括 25 个原子、75 个复合任务；八类基本技能覆盖抓放、开关门／抽屉、操纵开关、插入和导航等。 |
| 执行环境线索 | 日常操作仿真平台 |
| OpenAlex 引用快照 | 未核验（查询失败／未匹配）；2026-11-03 |
| 来源审计 | [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)；same_paper_in_registry |
| 来源核验依据 | 2026-11-03 复核原始论文标题与方法章节：§3–4；与 RoboCasa-Shift / RoboCasa365 分开 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：如何用多样厨房场景和复合任务训练、评估通用机器人？

**评测层级**：日常操作仿真平台。

## 2. 怎么构建的

**核心场景与条目**：原版 100 个厨房任务，包括 25 个原子、75 个复合任务；八类基本技能覆盖抓放、开关门／抽屉、操纵开关、插入和导航等。

**实现与判分**：以 robosuite／MuJoCo 和大量厨房、物体资产构建交互场景，结合人类示范与自动数据生成，系统变化场景、对象和任务组合。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026 | 使用 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 | 针对「总体成功率掩盖了单次执行如何变化、失败出现在长时程哪一阶段」的问题，在 RoboCasa365 上构建诊断型鲁棒性基准：干净与扰动 rollout 严格配对（仅目标偏移不同），并给出仿真支撑的阶段感知诊断。对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。 |
| [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024) | 2026 | 使用 | 视觉表示 × 集成机制 × 特征组合的受控对比；鲁棒性 | WAM 从预训练视频生成模型继承强先验，但其 VAE 表示是为视觉重建而非操作优化；外部视觉表示能提升操作，但既有方法把表示选择与集成机制绑在一起，掩盖了各自的作用。作者在受控设置下系统比较视觉表示、五种集成机制与特征组合，结论包括：强通用视觉表示带来更广的鲁棒性收益，能匹配甚至超过为特定视觉能力预训练的表示；通道级联合预测效果最好。 |
| [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523) | 2024 | 提出 | 大规模日常场景（以厨房为主）、数千场景与大量演示数据 | 主张用高保真物理仿真来扩展机器人的环境、任务与数据规模，提供以厨房为主的大量日常场景与数千条演示，用于训练与评测通用操作策略。它把评测从「少数桌面任务」推向「日常环境中的大规模任务」，是长时程、多任务 VLA 评测的重要底座（RoboCasa365、RoboCasa-Shift 等即建立在其上）。 |
| [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773) | 2026 | 使用 | 信号时序逻辑（STL）不变式 + 定量鲁棒性；安全率、成功但不安全率 | 指出二元成功率会掩盖轨迹上的安全违规：策略可能到达目标，却施加过度接触、扰动旁观物体、使手中物体失稳或进入机器人自碰撞。SafeVLA-Bench 是一个「事后」安全评估框架，可直接套在现有基于仿真的 VLA 基准上，把任务相关的安全要求编码为信号时序逻辑（STL）不变式并给出定量鲁棒性语义；除原生成功率外，还报告安全率与「成功但不安全」率。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文比较场景／任务多样性及合成示范的训练作用，并给出向真机迁移的实验。核心贡献是统一日常环境、复合任务和可扩展数据生成。

**适用边界**：原论文为 arXiv:2406.02523；不能用后续 RoboCasa-Shift 或 RoboCasa365 取代其来源，也不能把 365 版的任务和厨房规模写成原始版本。

## 5. 相关论文（均来自本调研表）

- [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861)（2026；使用）
- [What Visual Representations Do World Action Models Need?](https://arxiv.org/abs/2610.13024)（2026；使用）
- [RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)（2024；提出）
- [SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models](https://arxiv.org/abs/2606.00773)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

原论文为 arXiv:2406.02523；不能用后续 RoboCasa-Shift 或 RoboCasa365 取代其来源，也不能把 365 版的任务和厨房规模写成原始版本。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, et al., ‘RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots,’ arXiv preprint, 2024, arXiv:2406.02523v1. [论文](https://arxiv.org/abs/2406.02523)；[核查正文](https://arxiv.org/html/2406.02523v1)。

**重点核查位置（章节主题）**：III Environment；IV Tasks and Datasets；V Experiments。

OpenAlex 被引次数：**未核验（查询失败／未匹配）**；观测日期：2026-11-03。本次未取得可核验计数，不按 0 处理。

**项目与成果入口**：[https://robocasa.ai/](https://robocasa.ai/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 3 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
