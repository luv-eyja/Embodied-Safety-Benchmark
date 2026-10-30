# SimplerEnv

> **所属环节**：动作控制（评测基础设施）  
> **分类**：VLA 能力  
> **关联论文**：本表 3 篇（提出者 1 篇，使用者 2 篇）

## 1. 测什么问题（内容与所测环节）

真机评测不可扩展且难复现；而仿真基准与真机之间的视觉与物理差距使其成为不可靠的改进信号。

## 2. 怎么构建的

识别**控制差异**与**视觉差异**两个关键挑战，并提出缓解手段，使仿真评测结果与真机表现对齐——**无需构建全保真数字孪生**。

## 3. 用这个基准测了什么

OpenVLA、RT-1 等真实机器人策略，与真机结果对照。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [ManiPhysicsBench：物体保全的物理评测](https://arxiv.org/abs/2610.02802) | 2026 | arXiv 预印本 (arXiv:2610.02 | 使用 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 |
| [SimplerEnv：真机策略的仿真评测协议](https://arxiv.org/abs/2405.05941) | 2024 | arXiv 预印本 (arXiv:2405.05 | **提出** | 仿真-真机对齐；控制与视觉差异消解；与真机成功率的相关性 |
| [STARS：人机交互中从时空动力学到社会表征](https://arxiv.org/abs/2609.40245) | 2026 | arXiv 预印本 (arXiv:2609.40 | 使用 | 时空关系与人类意图推理；社会合规导航 |

## 4. 关键结论与改进方向

**关键结论**：只要控制与视觉差距被恰当处理，仿真可以可靠地排序真机策略；这为 VLA 提供了低成本、可复现的评测路径。

**论文提到的改进方向**：①sim-to-real 对齐应作为基准的显式目标；②控制频率与动作空间的匹配常被忽视；③可作为安全评测的低成本代理，但需验证排序保真度。

## 5. 相关论文（均来自本调研表）

- ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation（2026，arXiv 预印本 (arXiv:2610.02802)）
- Evaluating Real-World Robot Manipulation Policies in Simulation (SimplerEnv)（2024，arXiv 预印本 (arXiv:2405.05941)）  ← **提出**
- STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction（2026，arXiv 预印本 (arXiv:2609.40245)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
