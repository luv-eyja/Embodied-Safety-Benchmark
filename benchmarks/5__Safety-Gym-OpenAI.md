# Safety Gym (OpenAI)

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全 RL
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

首个把约束 cost 与任务回报分离、系统评测安全探索的基准；Point/Car/Doggo 机器人 + Goal/Button/Push 任务 + hazard/vase 约束，属 safety 评测而非能力。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全 RL**，评测对象包括 **Mobile Robot**。

## 2. 怎么构建的

**场景与构建**：Safexp-PointGoal1/CarGoal/DoggoGoal/Button/Push 等；hazards、vases、gremlins 约束对象。

**评测指标**：cost; cost_hazards; reward (capability); 约束违反。

## 3. 用这个基准测了什么

**被测对象**：Mobile Robot。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [Safety Gym：OpenAI 安全探索基准](https://openai.com/research/benchmarking-safe-exploration-in-deep-reinforcement-learning) | 2019 | OpenAI technical report 2019; 代码仓 2023 起 archive | **提出** | cost; cost_hazards; reward (capability); 约束违反 |

## 4. 关键结论与改进方向

**关键结论**：18 个约束环境和公开基线用成本与回报分开评估仿真机器人安全探索。

**改进方向**：扩展几何避碰以外的安全指标，并维护兼容的运行环境与真实系统验证。

**审查等级**：B。

**适用边界**：安全主要由几何避碰成本代理，代码已归档且依赖较旧，缺少真人与现实验证；适合经典安全探索算法比较。

## 5. 相关论文（均来自本调研表）

- [Benchmarking Safe Exploration in Deep Reinforcement Learning](https://openai.com/research/benchmarking-safe-exploration-in-deep-reinforcement-learning)（2019，OpenAI technical report 2019; 代码仓 2023 起 archive）← **提出**

---

*文档依据主表记录和论文资料整理。*
