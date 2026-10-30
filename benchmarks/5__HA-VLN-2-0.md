# HA-VLN 2.0

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；导航/HRI
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

显式引入 social-awareness 约束，指标同时评目标精度与 personal-space adherence/碰撞；安全与任务成功分开，属 human-aware navigation 安全评测。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；导航/HRI**，评测对象包括 **Navigation; Mobile Robot; HRI**。

## 2. 怎么构建的

**场景与构建**：16,844 条 socially grounded instructions；离散+连续环境；动态多人与户外场景。

**评测指标**：personal-space adherence; collision; goal accuracy/success (capability)。

## 3. 用这个基准测了什么

**被测对象**：Navigation; Mobile Robot; HRI。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [HA-VLN 2.0：人类在场 VLN 安全](https://arxiv.org/abs/2503.14229) | 2025 | IROS 2026; arXiv v1 2025-03 (v5 2026-08) | **提出** | personal-space adherence; collision; goal accuracy/success (capability) |

## 4. 关键结论与改进方向

**关键结论**：基准在离散和连续环境中加入动态多人互动，评估人类在场时的导航与碰撞规避。

**改进方向**：明确个人空间指标和碰撞定义，并统一论文、代码与数据文档中的评测口径。

**审查等级**：C。

**适用边界**：现有安全指标主要是含墙体的通用碰撞，未覆盖个人空间，论文、代码和数据口径也有差异；适合人类在场导航研究参考。

## 5. 相关论文（均来自本调研表）

- [HA-VLN 2.0: An Open Benchmark and Leaderboard for Human-Aware Navigation in Discrete and Continuous Environments with Dynamic Multi-Human Interactions](https://arxiv.org/abs/2503.14229)（2025，IROS 2026; arXiv v1 2025-03 (v5 2026-08)）← **提出**

---

*文档依据主表记录和论文资料整理。*
