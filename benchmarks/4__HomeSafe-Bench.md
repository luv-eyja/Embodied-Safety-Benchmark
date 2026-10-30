# HomeSafe-Bench

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；家务
> **分类**：具身智能体安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

以家庭场景中 VLM 的不安全动作检测为独立安全评测目标，438 个案例覆盖 6 个功能区，安全检测指标与通用 VLM 能力分开。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；家务**，评测对象包括 **VLM; Embodied Agent; Household Robot**。

## 2. 怎么构建的

**场景与构建**：438 cases across six functional areas; physical simulation + video generation; fine-grained multidimensional annotations。

**评测指标**：unsafe action detection performance; detection latency/efficiency; HD-Guard safety-performance trade-off。

## 3. 用这个基准测了什么

**被测对象**：VLM; Embodied Agent; Household Robot。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [HomeSafe-Bench：家庭不安全动作检测基准](https://arxiv.org/abs/2603.11975) | 2026 | arXiv 2026-03 (v1 2026-03-12; v2 2026-03-13) | **提出** | unsafe action detection performance; detection latency/efficiency; HD-Guard safety-performance trade-off |

## 4. 关键结论与改进方向

**关键结论**：438 段合成家庭视频使用时序加权安全分和多维标注，评估 VLM 定位危险动作起始时刻的能力。

**改进方向**：增加良性样本，并统一公开标注格式、预测格式与评测脚本。

**审查等级**：C。

**适用边界**：数据只有危险样本且发布格式与评测脚本不完全匹配；当前更适合危险时刻定位研究，不能估计过度报警率。

## 5. 相关论文（均来自本调研表）

- [HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios](https://arxiv.org/abs/2603.11975)（2026，arXiv 2026-03 (v1 2026-03-12; v2 2026-03-13)）← **提出**

---

*文档依据主表记录和论文资料整理。*
