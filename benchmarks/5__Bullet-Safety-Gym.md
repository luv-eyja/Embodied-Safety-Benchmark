# Bullet-Safety-Gym

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全 RL
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

基于 PyBullet 的约束安全 RL 环境集，以 cost 与 reward 分离来评测安全规范，属 safety 评测。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全 RL**，评测对象包括 **Mobile Robot; Drone; Quadruped**。

## 2. 怎么构建的

**场景与构建**：SafetyBall/Car/Drone/Ant x Reach/Circle/Run/Gather 共 16 个环境。

**评测指标**：cost; reward; cost return。

## 3. 用这个基准测了什么

**被测对象**：Mobile Robot; Drone; Quadruped。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [Bullet-Safety-Gym：安全 RL 环境](https://github.com/liuzuxin/Bullet-Safety-Gym) | 2021 | 开源框架/技术报告（venue 待核验） | **提出** | cost; reward; cost return |

## 4. 关键结论与改进方向

**关键结论**：PyBullet 的 16 个机器人-任务组合以 reward 和逐步 cost 分开呈现约束学习的性能与成本。

**改进方向**：补充统一评测协议、重复运行方差和更强的现实性验证。

**审查等级**：C。

**适用边界**：仅覆盖仿真约束成本，缺少统一运行协议和现实系统验证；适合安全 RL 的代价性能比较。

## 5. 相关论文（均来自本调研表）

- [Bullet-Safety-Gym: A Framework for Constrained Safety Reinforcement Learning](https://github.com/liuzuxin/Bullet-Safety-Gym)（2021，开源框架/技术报告（venue 待核验））← **提出**

---

*文档依据主表记录和论文资料整理。*
