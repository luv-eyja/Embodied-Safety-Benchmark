# OmniSafe

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；安全 RL
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

以统一安全 RL 算法实现与评测流程为核心的基础设施，强调约束满足/风险最小化，不是纯能力平台。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；安全 RL**，评测对象包括 **Mobile Robot; Humanoid; General**。

## 2. 怎么构建的

**场景与构建**：Safety-Gymnasium 等环境上的 20+ 安全 RL 算法统一实现与对比。

**评测指标**：reward; cost; cost return; 约束满足程度。

## 3. 用这个基准测了什么

**被测对象**：Mobile Robot; Humanoid; General。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [OmniSafe：安全 RL 基础设施](https://arxiv.org/abs/2305.09304) | 2023 | arXiv 2023-05; JMLR (repo description) | **提出** | reward; cost; cost return; 约束满足程度 |

## 4. 关键结论与改进方向

**关键结论**：OmniSafe 提供统一的 SafeRL 算法实现与 Safety-Gymnasium 训练期 reward/cost 对比流程。

**改进方向**：把算法训练成本与部署阶段安全验证分开报告，并为环境和算法版本提供稳定的复现设置。

**审查等级**：C。

**适用边界**：主要反映 Safety-Gymnasium 中的训练期 reward/cost 权衡，缺少部署阶段验证；适合 SafeRL 算法工程复现与比较。

## 5. 相关论文（均来自本调研表）

- [OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research](https://arxiv.org/abs/2305.09304)（2023，arXiv 2023-05; JMLR (repo description)）← **提出**

---

*文档依据主表记录和论文资料整理。*
