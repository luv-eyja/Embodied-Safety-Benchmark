# RoboCasa

> **所属环节**：动作控制（日常场景规模化）  
> **分类**：VLA 能力  
> **关联论文**：本表 4 篇（提出者 2 篇，使用者 2 篇）

## 1. 测什么问题（内容与所测环节）

机器人规模化受制于缺乏大规模数据集；主张用高保真物理仿真来扩展环境、任务与数据。

## 2. 怎么构建的

以厨房为主的大规模日常场景，提供**数千个场景与大量人类示范**，用于训练与评测通用操作策略。

## 3. 用这个基准测了什么

通用操作策略（含 VLA）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [RoboCasa-Shift：长时程操作的阶段感知鲁棒性评测](https://arxiv.org/abs/2610.27861) | 2026 | arXiv 预印本 (arXiv:2610.27 | **提出** | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 |
| [世界动作模型需要什么样的视觉表示](https://arxiv.org/abs/2610.13024) | 2026 | arXiv 预印本 (arXiv:2610.13 | 使用 | 视觉表示 × 集成机制 × 特征组合的受控对比；鲁棒性 |
| [RoboCasa：大规模日常任务仿真与评测底座](https://arxiv.org/abs/2406.02523) | 2024 | arXiv 预印本 (arXiv:2406.02 | **提出** | 大规模日常场景（以厨房为主）、数千场景与大量演示数据 |
| [SafeVLA-Bench：VLA 的「成功-安全」落差基准](https://arxiv.org/abs/2606.00773) | 2026 | arXiv 预印本 (arXiv:2606.00 | 使用 | 信号时序逻辑（STL）不变式 + 定量鲁棒性；安全率、成功但不安全率 |

## 4. 关键结论与改进方向

**关键结论**：仿真规模化可显著扩展任务与数据；但场景真实性仍需校验，其扩展版 RoboCasa365 进一步扩大了任务规模。

**论文提到的改进方向**：①把家居长时程任务纳入标准评测；②场景多样性需与真实世界分布对齐；③作为安全评测底座时可叠加阶段感知诊断（RoboCasa-Shift）。

## 5. 相关论文（均来自本调研表）

- RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation（2026，arXiv 预印本 (arXiv:2610.27861)）  ← **提出**
- What Visual Representations Do World Action Models Need?（2026，arXiv 预印本 (arXiv:2610.13024)）
- RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots（2024，arXiv 预印本 (arXiv:2406.02523)）  ← **提出**
- SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2606.00773)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
