# SinD 2.0

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；自动驾驶
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

面向 SOTIF 的交叉口安全验证数据集：以 surrogate safety measures 抽取 32,682 个 safety-critical events 并提供语义风险标注与测试工具链，评测目标是暴露 ADS 安全边界而非一般能力。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；自动驾驶**，评测对象包括 **AV**。

## 2. 怎么构建的

**场景与构建**：6 个信号交叉口/4 个中国城市；drone-collected；32,682 safety-critical events；违规/高风险交互/视觉遮挡/窄可行区域标注；开放环回放 + 闭环测试 + 渲染。

**评测指标**：safety-critical event detection; semantic risk subset performance; domain shift; open-loop/closed-loop metrics。

## 3. 用这个基准测了什么

**被测对象**：AV。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [SinD 2.0：SOTIF 场景风险标注数据集](https://arxiv.org/abs/2607.16943) | 2026 | arXiv 2026-07 (v2 2026-08) | **提出** | safety-critical event detection; semantic risk subset performance; domain shift; open-loop/closed-loop metrics |

## 4. 关键结论与改进方向

**关键结论**：六个中国信号交叉口的无人机轨迹和语义风险标签为 SOTIF 场景测试提供真实交通数据。

**改进方向**：复核风险标签，校准评测指标，并发布场景挖掘代码与完整数据集。

**审查等级**：C。

**适用边界**：风险标签未经人工复核，指标尚未校准，场景挖掘代码和完整数据不可得；适合 SOTIF 场景研究参考。

## 5. 相关论文（均来自本调研表）

- [SinD 2.0: A Multi-City UAV Dataset with Semantic Risk Annotations for SOTIF-Oriented Safety Validation at Signalized Intersections](https://arxiv.org/abs/2607.16943)（2026，arXiv 2026-07 (v2 2026-08)）← **提出**

---

*文档依据主表记录和论文资料整理。*
