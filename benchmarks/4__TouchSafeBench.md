# TouchSafeBench

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；人机接触
> **分类**：具身智能体安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

把机器人本体-人/场景的接触状态判定与碰撞预警作为独立评测目标，用模拟器接触标签评 VLM 的 collision grounding，安全判定与视觉描述能力分开。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；人机接触**，评测对象包括 **HRI; Mobile Robot; VLM**。

## 2. 怎么构建的

**场景与构建**：2,940 simulated indoor co-presence episodes；Habitat 3.0；social navigation 与 social rearrangement；多视角 RGB-D、top-down 轨迹图、相机元数据、simulator contact labels。

**评测指标**：safety-state classification Macro-F1; imminent-collision warning; current vs imminent contact; contact labels。

## 3. 用这个基准测了什么

**被测对象**：HRI; Mobile Robot; VLM。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [TouchSafeBench：接触/临近碰撞接地基准](https://arxiv.org/abs/2605.31196) | 2026 | CoRL 2026; arXiv 2026-05-29 (v2 2026-10-23) | **提出** | safety-state classification Macro-F1; imminent-collision warning; current vs imminent contact; contact labels |

## 4. 关键结论与改进方向

**关键结论**：Habitat 3.0 的 2,940 段多视角片段和模拟器标签可用于评估 VLM 对接触与临近碰撞状态的判断。

**改进方向**：扩展机器人与模拟器覆盖，加入更多专家基线，并复核存在歧义的标签；当前指标适用于接触状态判断，不代表完整物理安全能力。

**审查等级**：B。

**适用边界**：它是三帧感知代理下的单仿真、单机器人接触判断，存在少量歧义标签；适合碰撞接地评测，不代表全栈安全。

## 5. 相关论文（均来自本调研表）

- [Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration](https://arxiv.org/abs/2605.31196)（2026，CoRL 2026; arXiv 2026-05-29 (v2 2026-10-23)）← **提出**

---

*文档依据主表记录和论文资料整理。*
