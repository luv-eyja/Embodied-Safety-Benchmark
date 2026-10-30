# RiskBench

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；自动驾驶
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

面向零碰撞目标的大规模场景化风险识别 benchmark，评 detect/anticipate/decision-making 三类能力；以风险识别为安全目标，区别于驾驶能力榜。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；自动驾驶**，评测对象包括 **AV**。

## 2. 怎么构建的

**场景与构建**：场景 taxonomy + augmentation pipeline；10 个算法；风险检测/定位/预判/决策支持。

**评测指标**：risk detection/localization; risk anticipation; decision-making support。

## 3. 用这个基准测了什么

**被测对象**：AV。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [RiskBench：场景化风险识别基准](https://arxiv.org/abs/2312.01659) | 2023 | ICRA 2024; arXiv v1 2023-12 (v2 2024-03) | **提出** | risk detection/localization; risk anticipation; decision-making support |

## 4. 关键结论与改进方向

**关键结论**：CARLA 场景覆盖四类交互，评估风险对象定位、风险预判和决策支持。

**改进方向**：校准风险识别指标，固定障碍物检查点与运行配置，并增加仿真外验证。

**审查等级**：C。

**适用边界**：仅在 CARLA 仿真中评估，风险识别指标可能受多报影响，复现还缺障碍物检查点；适合风险感知研究比较。

## 5. 相关论文（均来自本调研表）

- [RiskBench: A Scenario-based Benchmark for Risk Identification](https://arxiv.org/abs/2312.01659)（2023，ICRA 2024; arXiv v1 2023-12 (v2 2024-03)）← **提出**

---

*文档依据主表记录和论文资料整理。*
