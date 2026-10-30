# CALVIN

> **所属环节**：认知 + 规划（长时程语言遵循）  
> **分类**：VLA 能力  
> **关联论文**：本表 4 篇（提出者 1 篇，使用者 3 篇）

## 1. 测什么问题（内容与所测环节）

测语言条件的长时程操作：策略能否在**连续指令链**下逐步正确地完成任务序列。

## 2. 怎么构建的

仿真桌面环境中 **34 个操作任务**，串联成 **1,000+ 条长时程指令序列**；核心指标是**连续指令平均完成长度**（在一条指令链上能正确执行多少步）。

## 3. 用这个基准测了什么

语言条件模仿学习策略（含 LCBC、HULC、RoboFlamingo、OpenVLA 等）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [指令检索轨迹：VLA 泛化失败的诊断与缓解](https://arxiv.org/abs/2609.39971) | 2026 | arXiv 预印本 (arXiv:2609.39 | 使用 | 反事实指令下的行为切换；指令-动作绑定（instruction-action binding） |
| [不是所有层都要调：VLA 适配的区域诊断](https://arxiv.org/abs/2609.18084) | 2026 | arXiv 预印本 (arXiv:2609.18 | 使用 | 区域隔离微调的归一化参数位移（适配代价谱） |
| [RTPC：冻结 VLA 的外部记忆修正及其可复现性](https://arxiv.org/abs/2610.24573) | 2026 | arXiv 预印本 (arXiv:2610.24 | 使用 | 近碰撞/停滞代理事件率、任务成功数；独立复现队列 |
| [CALVIN：语言条件长时程操作基准](https://arxiv.org/abs/2112.03227) | 2022 | IEEE Robotics and Automa | **提出** | 34 个任务、1000+ 条长时程指令链；连续指令平均完成长度 |

## 4. 关键结论与改进方向

**关键结论**：把长时程语言遵循变成一个可量化指标（平均完成步数），比单任务成功率更能区分策略；但环境偏静态，不含安全或扰动维度。

**论文提到的改进方向**：①把安全约束加入指令链；②需要考虑指令链中途的环境变化；③用本表 CALVIN 相关论文的方法补语言敏感性与失败分析。

## 5. 相关论文（均来自本调研表）

- When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models（2026，arXiv 预印本 (arXiv:2609.39971)）
- Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2609.18084)）
- Retrieval-triggered Action Projection Adjustment for Frozen VLA Policies: An Empirical Study and Failure Analysis（2026，arXiv 预印本 (arXiv:2610.24573)）
- CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks（2022，IEEE Robotics and Automation Letters (RA）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
