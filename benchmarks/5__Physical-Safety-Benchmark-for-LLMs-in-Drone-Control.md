# Physical Safety Benchmark for LLMs in Drone Control

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；无人机
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

以 LLM 为无人机生成控制代码时的物理安全为独立评测目标，按对人/对物/基础设施/法规四类风险统计不安全行为，并与代码生成能力分开报告；非一般能力 benchmark。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；无人机**，评测对象包括 **Drone**。

## 2. 怎么构建的

**场景与构建**：无人机控制代码生成任务；四类风险场景（human-targeted threats, object-targeted threats, infrastructure attacks, regulatory violations）；主流 LLM 对比。

**评测指标**：分工况 physical safety violation; unsafe response rate; 危险命令拒绝率; code-generation utility（能力，单列）。

## 3. 用这个基准测了什么

**被测对象**：Drone。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [无人机控制代码物理安全基准](https://arxiv.org/abs/2411.02317) | 2024 | Communications of the ACM 2026; arXiv v1 2024-11 (v2 2026-02) | **提出** | 分工况 physical safety violation; unsafe response rate; 危险命令拒绝率; code-generation utility（能力，单列） |

## 4. 关键结论与改进方向

**关键结论**：基准将无人机控制代码生成中的四类物理风险与拒绝行为分开统计，并以多项指标区分安全和代码生成能力。

**改进方向**：将不执行与安全执行分别计分，避免示例泄漏，并公开评测代码和真实环境验证结果。

**审查等级**：C。

**适用边界**：不执行控制代码可能获得高分，示例与测试存在泄漏风险，缺少评测代码和真实环境验证；适合代码级风险筛查。

## 5. 相关论文（均来自本调研表）

- [Defining and Evaluating Physical Safety for Large Language Models](https://arxiv.org/abs/2411.02317)（2024，Communications of the ACM 2026; arXiv v1 2024-11 (v2 2026-02)）← **提出**

---

*文档依据主表记录和论文资料整理。*
