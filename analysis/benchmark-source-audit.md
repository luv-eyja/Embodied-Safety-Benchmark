# Benchmark 来源审计

> 更新时间：2026-11-01。本文档针对当前调研表中“论文使用了 benchmark，但标题没有出现该 benchmark 名称”的条目，区分“提出论文已在表内但名称只在摘要中出现”和“提出论文确实不在当前表内”两种情况。

## 判定口径

- **表内提出论文**：核对论文摘要或正文摘要信息，确认论文明确使用 `introduce / construct / release / benchmark` 等提出性措辞；在 registry 中把该论文补标为“提出”。
- **表外原始论文**：当前 192 条论文记录没有收录原始 benchmark 论文，只在后续使用论文中看到该名称；记录原始论文链接，但不把使用论文冒充提出论文。
- **名称变体**：RoboComb 是本库正则对 RoboCombine 的简称归并；R2R-CE 是连续环境 VLN 设置，和原始 R2R 数据集的来源需要分开理解。

## 已核验来源

| benchmark | 来源类别 | 已核验提出/原始论文 | 处理结果 |
|---|---|---|---|
| SafeLIBERO | 表内提出论文 | [VLSA](https://arxiv.org/abs/2512.11891) | 补标 VLSA 为提出论文 |
| ASIMOV Benchmark | 表内提出论文 | [Generating Robot Constitutions & Benchmarks for Semantic Safety](https://arxiv.org/abs/2503.08663) | 补标提出论文；AGENTSAFE 保留为使用论文 |
| RoboHarm | 表内提出论文 | [Refuses in Chat, Complies with Arms](https://arxiv.org/abs/2610.14043) | 补标提出论文 |
| Trap-LIBERO / Trap-RoboTwin | 表内提出论文 | [TrapVLA](https://arxiv.org/abs/2608.26578) | 补标提出论文 |
| LIBERO-CTRL | 表内提出论文 | [Beyond Single-Axis Testing](https://arxiv.org/abs/2609.15940) | 补标提出论文 |
| LIBERO-Para | 表内提出论文 | [IndustrialVLA-Bench](https://arxiv.org/abs/2609.25562) | 补标提出论文 |
| RoboStress | 表内提出论文 | [Taming VLAs under Robot Execution Errors](https://arxiv.org/abs/2609.37334) | 补标提出论文 |
| BAVO-Bench | 表内提出论文 | [Recovering the View](https://arxiv.org/abs/2609.37292) | 补标提出论文 |
| DriveDegrade | 表内提出论文 | [When Does Corruption Break the Plan?](https://arxiv.org/abs/2608.29005) | 补标提出论文 |
| VLN-Safe | 表内提出论文 | [Successful but Unsafe](https://arxiv.org/abs/2610.14682) | 补标提出论文 |
| RoboComb / RoboCombine | 表内提出论文 | [Exploring the Limits of Combinatorial Generalization](https://arxiv.org/abs/2610.15425) | 记录名称变体，补标提出论文 |
| RoboReel | 表内提出论文 | [Monkey See, Can Monkey Do?](https://arxiv.org/abs/2609.08209) | 补标提出论文 |
| SafePlan-Bench / Safe-Align | 表内提出论文 | [A Framework for Benchmarking and Aligning Task-Planning Safety](https://arxiv.org/abs/2504.14650) | 补标提出论文 |
| RoboAbstention | 表内提出论文 | [The Yes-Man Syndrome](https://arxiv.org/abs/2605.20544) | 补标提出论文 |
| DESPITE | 表内提出论文 | [Using Large Language Models for Embodied Planning Introduces Systematic Safety Risks](https://arxiv.org/abs/2604.18463) | 补标提出论文 |
| MineAmongUs | 表内提出论文 | [Lies We Can See](https://arxiv.org/abs/2608.30428) | 补标提出论文 |
| ExceptionDrive | 表内提出论文 | [ExceptionDrive](https://arxiv.org/abs/2609.37871) | 补标提出论文 |
| RoboCasa365 | 表外原始论文 | [RoboCasa365](https://arxiv.org/abs/2603.04356) | 作为外部原始来源挂接；RoboCasa-Shift 是后续使用论文 |
| BEHAVIOR-1K | 表外原始论文 | [BEHAVIOR-1K](https://arxiv.org/abs/2403.09227) | 作为外部原始来源挂接；ManiUnit 是后续使用论文 |
| Open X-Embodiment | 表外原始论文 | [Open X-Embodiment](https://arxiv.org/abs/2310.08864) | 作为外部原始来源挂接；AgiBot World Colosseo 是后续使用论文 |
| nuScenes | 表外原始数据集论文 | [nuScenes](https://arxiv.org/abs/1903.11027) | 作为底层数据集来源挂接；DriveDegrade/ExceptionDrive 是派生 benchmark |
| R2R-CE | 表外连续环境来源 | [Bridging the Gap Between Learning in Discrete and Continuous Environments for VLN](https://openaccess.thecvf.com/content/CVPR2022/html/Hong_Bridging_the_Gap_Between_Learning_in_Discrete_and_Continuous_Environments_for_Vision-and-Language_Navigation_CVPR_2022_paper.html) | 作为 R2R-CE/VLN-CE 连续环境设置来源挂接；原始 R2R 数据集另有早期论文 |

## 对原统计的影响

此前 registry 只把“标题包含 benchmark 名称”的论文标为提出，因此会把 SafeLIBERO、RoboHarm、RoboStress 等误判为“只有使用论文”。现在 `data/benchmark_source_audit.json` 被 `scripts/bench_registry.py` 读取，表内提出论文会按来源审计补标；真正表外的 5 个来源则在各基准卡片中显示为外部原始来源，不虚构本库内的提出记录。

机器可读来源表：[`data/benchmark_source_audit.json`](../data/benchmark_source_audit.json)。生成后的基准卡片会在“来源审计”字段显示来源论文和核验依据。

## 仍需人工复核的边界

这些来源已经足以修正“来源缺失”的结构性误报，但没有替代逐篇全文核验。下一轮若要把来源关系升级为正式引用网络，应继续核对：

1. benchmark 的版本号、发布日期和代码/数据 release 是否与论文版本一致；
2. 派生 benchmark 与底层数据集之间的继承关系，尤其是 R2R-CE、nuScenes、BEHAVIOR-1K；
3. RoboComb/RoboCombine 等名称变体是否需要拆成两个独立 registry 条目。
