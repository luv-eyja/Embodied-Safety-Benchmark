# Safety-Gymnasium

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全 RL
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

以约束违反成本(cost)为独立评测目标，返回与 cost 分离并配套统一 API，用于系统比较 safe RL 算法，而非单纯任务回报。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全 RL**，评测对象包括 **Mobile Robot; General**。

## 2. 怎么构建的

**场景与构建**：SafetyPoint/Car/Doggo/Racecar/Ant 的 Goal/Button/Push/Circle 导航；Safety Velocity 连续控制；Safe Vision（Race/FormulaOne/Fading）；Safe Multi-Agent；Safe Isaac Gym（Franka/ShadowHand）。

**评测指标**：episode return (capability); cost return; constraint violation rate; cost rate。

## 3. 用这个基准测了什么

**被测对象**：Mobile Robot; General。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [Safety-Gymnasium：统一安全 RL 基准](https://arxiv.org/abs/2310.12567) | 2023 | NeurIPS 2023 Datasets & Benchmarks Track | **提出** | episode return (capability); cost return; constraint violation rate; cost rate |

## 4. 关键结论与改进方向

**关键结论**：仿真 CMDP 中的累计 cost 与任务回报分列，可比较碰撞、危险区、越界、超速和关节限位等约束满足情况。

**改进方向**：补充严重度与人身风险指标，并通过固定协议和现实系统验证拓展其物理安全解释范围。

**审查等级**：B。

**适用边界**：当前是仿真 CMDP 中的约束成本基准，缺少人身风险、严重度和现实验证；适合比较 SafeRL 的约束满足能力。

## 5. 相关论文（均来自本调研表）

- [Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark](https://arxiv.org/abs/2310.12567)（2023，NeurIPS 2023 Datasets & Benchmarks Track）← **提出**

---

*文档依据主表记录和论文资料整理。*
