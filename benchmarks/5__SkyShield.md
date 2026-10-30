# SkyShield

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；无人机
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

首个前视单目语义占据 UAV benchmark，提出安全加权指标 KAR-mIoU（kinematic reachability + time-to-collision），把占据预测作为低空飞行安全接口。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；无人机**，评测对象包括 **Drone**。

## 2. 怎么构建的

**场景与构建**：36K front-view UAV samples；城市多场景/天气；逐帧 6-DoF pose 与 front-frustum semantic occupancy。

**评测指标**：KAR-mIoU (safety-weighted); conventional mIoU (capability)。

## 3. 用这个基准测了什么

**被测对象**：Drone。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [SkyShield：UAV 占据安全接口](https://arxiv.org/abs/2606.00747) | 2026 | arXiv 2026-05 (v2 2026-06) | **提出** | KAR-mIoU (safety-weighted); conventional mIoU (capability) |

## 4. 关键结论与改进方向

**关键结论**：前视单目语义占据预测和 TTC 加权的 KAR-mIoU 将低空 UAV 感知结果与飞行安全相关性联系起来。

**改进方向**：独立验证 KAR-mIoU 对安全性的增量解释，并发布数据、代码与评测脚本。

**审查等级**：C。

**适用边界**：安全仍是感知代理指标，KAR-mIoU 的增量效度尚未验证，数据、代码和评测脚本未完整发布；适合低空 UAV 感知研究。

## 5. 相关论文（均来自本调研表）

- [SkyShield: Occupancy as a Safety Interface for Low-Altitude UAV Autonomy](https://arxiv.org/abs/2606.00747)（2026，arXiv 2026-05 (v2 2026-06)）← **提出**

---

*文档依据主表记录和论文资料整理。*
