# Embodied Red Teaming

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；红队审计
> **分类**：具身智能体安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

用 VLM 自动生成多样且具挑战性的指令审计语言条件机器人模型，同时测任务失败与不安全行为（damage avoidance）；红队生成+评测协议，安全目标为主，故 Both。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；红队审计**，评测对象包括 **Language-conditioned Robot Model (Manipulation)**。

## 2. 怎么构建的

**场景与构建**：自动化红队指令生成；对 SOTA 语言条件机器人模型评测。

**评测指标**：task success；safety violations（含 damage avoidance）。

## 3. 用这个基准测了什么

**被测对象**：Language-conditioned Robot Model (Manipulation)。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [Embodied Red Teaming：具身红队审计](https://arxiv.org/abs/2411.18676) | 2024 | arXiv 2024 (v1 2024-11-27; v2 2025-02-10) | **提出** | task success；safety violations（含 damage avoidance） |

## 4. 关键结论与改进方向

**关键结论**：当前量化结果主要是语言条件操作策略的任务成功率，安全行为则以物体掉落示例展示。

**改进方向**：补充安全事件的计数、严重度和对照条件，并公开完整评测代码，以便区分危险执行与任务成功。

**审查等级**：C。

**适用边界**：当前安全结果主要是少量物体掉落示例，缺少量化事件指标与完整评测代码；适合生成审计指令，不宜单独支撑安全结论。

## 5. 相关论文（均来自本调研表）

- [Embodied Red Teaming for Auditing Robotic Foundation Models](https://arxiv.org/abs/2411.18676)（2024，arXiv 2024 (v1 2024-11-27; v2 2025-02-10)）← **提出**

---

*文档依据主表记录和论文资料整理。*
