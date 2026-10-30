# OopsieVerse

> **所属环节**：VLA 评测；操作
> **分类**：VLA 安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

把损伤(机械/热/流体)变成显式、任务无关的安全信号,区分目标达成与安全执行。

本条目关注的具身环节为 **VLA 评测；操作**，评测对象包括 **Manipulation; VLA**。

## 2. 怎么构建的

**场景与构建**：32 个家庭操作任务(OmniGibson 17 + RoboCasa 15); 短程单模态损伤与长程安全决策任务。

**评测指标**：damage magnitude/是否造成损伤; safe execution vs task completion; 安全演示与安全策略提升效果。

## 3. 用这个基准测了什么

**被测对象**：Manipulation; VLA。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [OopsieVerse：损伤感知操作安全基准](https://arxiv.org/abs/2606.31993) | 2026 | arXiv 2026-06-30 v1; RSS 2026 | **提出** | damage magnitude/是否造成损伤; safe execution vs task completion; 安全演示与安全策略提升效果 |

## 4. 关键结论与改进方向

**关键结论**：DamageSim 将机械、热和流体损伤映射为显式信号，并在两个模拟器的家庭操作任务中分开统计任务完成与安全执行。

**改进方向**：校准损伤模型，并统一论文与发布数据中的任务数量和统计口径。

**审查等级**：B。

**适用边界**：损伤真值依赖尚未校准的手工模型，论文与数据的任务数量需要统一；适合家庭操作仿真中的安全执行对比。

## 5. 相关论文（均来自本调研表）

- [OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation](https://arxiv.org/abs/2606.31993)（2026，arXiv 2026-06-30 v1; RSS 2026）← **提出**

---

*文档依据主表记录和论文资料整理。*
