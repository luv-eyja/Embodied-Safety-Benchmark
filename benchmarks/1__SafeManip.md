# SafeManip

> **所属环节**：VLA 评测；操作
> **分类**：VLA 安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

用 LTLf 时序性质在低层操作轨迹上评测时序安全(污染/提前释放/顺序错误),显式区别于任务完成。

本条目关注的具身环节为 **VLA 评测；操作**，评测对象包括 **Manipulation; VLA**。

## 2. 怎么构建的

**场景与构建**：RoboCasa365 与 LIBERO; 8 类物理/语义安全属性; 7 个机器人基础模型策略。

**评测指标**：per-trigger safety (按安全机会归一化的违规率); task success (capability)。

## 3. 用这个基准测了什么

**被测对象**：Manipulation; VLA。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [SafeManip：时序安全操作基准](https://arxiv.org/abs/2605.12386) | 2026 | arXiv 2026-05 v1; v3 2026-09-28 | **提出** | per-trigger safety (按安全机会归一化的违规率); task success (capability) |

## 4. 关键结论与改进方向

**关键结论**：20 条 LTLf 规范和按触发机会归一化的违规率可在 RoboCasa365/LIBERO 轨迹上分开衡量任务完成与执行安全。

**改进方向**：补充接触力或损害严重度指标，公开固定评测版本与许可证，并验证仿真结果向真实操作的迁移。

**审查等级**：B。

**适用边界**：当前缺少严重度和接触力维度，且尚无真实操作验证；适合比较轨迹级时序安全监控，不等同于完整物理安全。

## 5. 相关论文（均来自本调研表）

- [SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation](https://arxiv.org/abs/2605.12386)（2026，arXiv 2026-05 v1; v3 2026-09-28）← **提出**

---

*文档依据主表记录和论文资料整理。*
