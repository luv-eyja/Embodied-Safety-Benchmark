# GUARD

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全 RL
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

以统一 agent/task/constraint specification 比较 SOTA safe RL 算法，核心是约束违反下的策略评测。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全 RL**，评测对象包括 **Mobile Robot; Manipulation; AV (任务覆盖)**。

## 2. 怎么构建的

**场景与构建**：多种安全约束任务（含导航/操作/驾驶类），可定制 task 与 algorithm。

**评测指标**：reward; cost; constraint violation。

## 3. 用这个基准测了什么

**被测对象**：Mobile Robot; Manipulation; AV (任务覆盖)。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [GUARD：安全 RL 基准](https://arxiv.org/abs/2305.13681) | 2023 | TMLR (published); arXiv v1 2023-05 (v4 2024-09) | **提出** | reward; cost; constraint violation |

## 4. 关键结论与改进方向

**关键结论**：GUARD 在 MuJoCo 多类安全约束任务上统一比较 on-policy safe RL 算法。

**改进方向**：同时报告任务成功率与成本、多次运行方差和 held-out 环境结果，以区分成本下降与任务能力退化。

**审查等级**：C。

**适用边界**：主要使用几何穿透成本，缺少任务成功率、方差、留出环境和现实验证；适合算法层约束比较。

## 5. 相关论文（均来自本调研表）

- [GUARD: A Safe Reinforcement Learning Benchmark](https://arxiv.org/abs/2305.13681)（2023，TMLR (published); arXiv v1 2023-05 (v4 2024-09)）← **提出**

---

*文档依据主表记录和论文资料整理。*
