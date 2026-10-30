# safe-control-gym

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全控制
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

统一传统控制/学习控制/RL 的安全 benchmark，扩展 Gym API 支持 symbolic dynamics、constraints 与可重复扰动注入，显式比较控制性能、数据效率与安全性。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全控制**，评测对象包括 **Drone; Control (cart-pole/quadrotor)**。

## 2. 怎么构建的

**场景与构建**：cart-pole、1D quadrotor、2D quadrotor 三系统；stabilization 与 trajectory tracking 两任务。

**评测指标**：safety constraint violation; control performance; data efficiency; reward (capability)。

## 3. 用这个基准测了什么

**被测对象**：Drone; Control (cart-pole/quadrotor)。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [safe-control-gym：安全控制基准](https://arxiv.org/abs/2109.06325) | 2021 | arXiv v1 2021-09 (v4 2022-07); 期刊版待核验 | **提出** | safety constraint violation; control performance; data efficiency; reward (capability) |

## 4. 关键结论与改进方向

**关键结论**：基准将安全定义为低层控制中的状态/输入约束满足与扰动鲁棒性，并覆盖三类解析系统。

**改进方向**：建立共享约束测试集，并增加真实系统验证，以便跨控制方法比较更具代表性。

**审查等级**：B。

**适用边界**：覆盖三个解析系统，约束由使用者设定，尚无共享安全测试集和真实系统验证；适合低层控制约束与扰动鲁棒性比较。

## 5. 相关论文（均来自本调研表）

- [safe-control-gym: a Unified Benchmark Suite for Safe Learning-based Control and Reinforcement Learning in Robotics](https://arxiv.org/abs/2109.06325)（2021，arXiv v1 2021-09 (v4 2022-07); 期刊版待核验）← **提出**

---

*文档依据主表记录和论文资料整理。*
