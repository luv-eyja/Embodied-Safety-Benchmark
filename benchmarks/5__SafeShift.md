# SafeShift

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；自动驾驶
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

在真实驾驶数据中挖掘隐藏的安全相关场景并构造 safety-informed distribution shift，评轨迹预测模型的碰撞率；安全指标与预测精度分开。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；自动驾驶**，评测对象包括 **AV**。

## 2. 怎么构建的

**场景与构建**：Waymo Open Motion 等真实数据中的 safety-relevant scenarios；轨迹预测模型。

**评测指标**：prediction collision rate; 10% average reduction; prediction accuracy (capability)。

## 3. 用这个基准测了什么

**被测对象**：AV。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [SafeShift：安全相关分布偏移的轨迹预测基准](https://arxiv.org/abs/2309.08889) | 2023 | arXiv v1 2023-09 (v2 2024-02) | **提出** | prediction collision rate; 10% average reduction; prediction accuracy (capability) |

## 4. 关键结论与改进方向

**关键结论**：SafeShift 从 WOMD 场景中筛选安全相关分布，单独报告轨迹预测碰撞率与预测精度。

**改进方向**：公开场景划分，明确碰撞阈值与多模态计数规则，并扩大模型和重复运行覆盖。

**审查等级**：C。

**适用边界**：场景划分依赖尚未外部验证的安全评分，碰撞阈值和多模态计数规则不完整，实验模型较少；适合安全相关分布偏移研究。

## 5. 相关论文（均来自本调研表）

- [SafeShift: Safety-Informed Distribution Shifts for Robust Trajectory Prediction in Autonomous Driving](https://arxiv.org/abs/2309.08889)（2023，arXiv v1 2023-09 (v2 2024-02)）← **提出**

---

*文档依据主表记录和论文资料整理。*
