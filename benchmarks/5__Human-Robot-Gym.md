# Human-Robot Gym

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；人机协作
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

面向人机协作的安全 RL 基准，内置可证明保证人类安全的 safety shield，以人类安全约束而非任务成功率为主评测。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；人机协作**，评测对象包括 **HRI; Manipulation**。

## 2. 怎么构建的

**场景与构建**：8 个模块化 HRC 仿真任务（论文评估其中 6 个）；人机共享工作空间。

**评测指标**：safety shield 干预与人类安全约束; reward; success rate (capability)。

## 3. 用这个基准测了什么

**被测对象**：HRI; Manipulation。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [Human-Robot Gym：人机协作安全 RL 基准](https://arxiv.org/abs/2310.06208) | 2023 | arXiv v1 2023-10 (v2 2024-06); 会议版待核验 | **提出** | safety shield 干预与人类安全约束; reward; success rate (capability) |

## 4. 关键结论与改进方向

**关键结论**：Vicon 动捕的人类动作和 SaRA 安全盾为 8 个 MuJoCo 人机协作任务提供可运行的测试环境。

**改进方向**：分别报告安全盾干预、约束违反和任务结果，便于辨别策略本身与外部安全盾的贡献。

**审查等级**：C。

**适用边界**：安全主要由外部安全盾保证，论文报告的安全维度变化有限；适合研究人机协作中的盾与策略配合，不宜作为策略本身的安全证据。

## 5. 相关论文（均来自本调研表）

- [Human-Robot Gym: Benchmarking Reinforcement Learning in Human-Robot Collaboration](https://arxiv.org/abs/2310.06208)（2023，arXiv v1 2023-10 (v2 2024-06); 会议版待核验）← **提出**

---

*文档依据主表记录和论文资料整理。*
