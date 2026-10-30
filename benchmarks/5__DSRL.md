# DSRL

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全 RL
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

面向离线安全 RL 的数据集+基线套件，评测离线策略的回报与约束违反，属 safety 评测。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全 RL**，评测对象包括 **Mobile Robot; AV**。

## 2. 怎么构建的

**场景与构建**：38 个安全 RL 任务，环境来自 SafetyGymnasium/BulletSafetyGym/MetaDrive。

**评测指标**：reward; cost; cost return; constraint violation。

## 3. 用这个基准测了什么

**被测对象**：Mobile Robot; AV。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [DSRL：离线安全 RL 数据集/基准](https://arxiv.org/abs/2306.09303) | 2023 | arXiv 2023-06; 疑 NeurIPS 2023 D&B（data.mlr.press v01-12，待核验） | **提出** | reward; cost; cost return; constraint violation |

## 4. 关键结论与改进方向

**关键结论**：DSRL 汇集三个模拟器中的 38 个离线安全 RL 任务、累计成本标签和 7 个基线。

**改进方向**：增加严重度和最坏情况指标，并补充专家或真实环境验证；解释基线时应区分仿真约束满足与现实物理安全。

**审查等级**：B。

**适用边界**：安全标签是模拟器内累计约束违反计数，尚无真实环境、专家或最坏情况验证；适合离线安全 RL 数据与基线比较。

## 5. 相关论文（均来自本调研表）

- [Datasets and Benchmarks for Offline Safe Reinforcement Learning](https://arxiv.org/abs/2306.09303)（2023，arXiv 2023-06; 疑 NeurIPS 2023 D&B（data.mlr.press v01-12，待核验））← **提出**

---

*文档依据主表记录和论文资料整理。*
