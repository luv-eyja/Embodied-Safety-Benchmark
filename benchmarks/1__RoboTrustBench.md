# RoboTrustBench

> **所属环节**：VLA 评测；世界模型
> **分类**：VLA 安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

在世界模型用于机器人操作的场景下评测四类输入（Normal/Constraint-Sensitive/Counterfactual/Adversarial），含 unsafe-instruction suppression 与约束推理；安全/可信维度与视频保真度分开，故 Safety（含对抗子集）。

本条目关注的具身环节为 **VLA 评测；世界模型**，评测对象包括 **World Model; Manipulation**。

## 2. 怎么构建的

**场景与构建**：1,207 expert-validated instruction-image pairs（来自 DROID）；Normal、Constraint-Sensitive、Counterfactual、Adversarial 四类场景；6 维 13 细项评测。

**评测指标**：six-dimensional protocol with 13 criteria; constraint reasoning; counterfactual grounding; physical interaction; unsafe-instruction suppression; human/MLLM assessment。

## 3. 用这个基准测了什么

**被测对象**：World Model; Manipulation。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [RoboTrustBench：视频世界模型可信度](https://arxiv.org/abs/2606.01600) | 2026 | EMNLP 2026 Findings; arXiv 2026-06 (v2 2026-08) | **提出** | six-dimensional protocol with 13 criteria; constraint reasoning; counterfactual grounding; physical interaction; unsafe-instruction suppression; human/MLLM assessment |

## 4. 关键结论与改进方向

**关键结论**：基准以 DROID 图像和指令构建 1,207 条四类场景，并用 13 项标准评测视频世界模型的可信度。

**改进方向**：扩大安全场景与每个模型的评测样本，公开生成视频和评测流程，并避免不执行策略获得高分。

**审查等级**：C。

**适用边界**：安全子集规模小，单模型人工评测样本有限，生成视频和流程未完整公开；不宜把可信度分数直接解释为部署安全。

## 5. 相关论文（均来自本调研表）

- [RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation](https://arxiv.org/abs/2606.01600)（2026，EMNLP 2026 Findings; arXiv 2026-06 (v2 2026-08)）← **提出**

---

*文档依据主表记录和论文资料整理。*
