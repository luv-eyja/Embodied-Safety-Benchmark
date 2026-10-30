# Safety-CHORES

> **所属环节**：VLA 评测；操作
> **分类**：VLA 安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

为 VLA 安全对齐提出的长程移动操作 testbed，用细粒度安全约束与累计 cost 评估，任务成功率单列，安全与能力解耦。

本条目关注的具身环节为 **VLA 评测；操作**，评测对象包括 **VLA; Mobile Manipulation**。

## 2. 怎么构建的

**场景与构建**：程序化生成的室内长程导航+操作任务；安全关键组件：corner、blind spot、fragile collection、critical point、dangerous equipment；含 OOD 视觉扰动与极端失败场景。

**评测指标**：cumulative safety cost; task success rate; max unsafe severity; OOD safety generalization。

## 3. 用这个基准测了什么

**被测对象**：VLA; Mobile Manipulation。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [Safety-CHORES：SafeVLA 安全 testbed](https://arxiv.org/abs/2503.03480) | 2025 | NeurIPS 2025 Spotlight; arXiv 2025 (v4 2026) | **提出** | cumulative safety cost; task success rate; max unsafe severity; OOD safety generalization |

## 4. 关键结论与改进方向

**关键结论**：基准在 AI2-THOR/CHORES 的 543 个家务任务中用规则成本衡量碰撞和扰动规避，并将成功率与成本分列。

**改进方向**：让安全评分独立于训练信号，并检查提前终止等策略是否能在未完成任务时降低成本。

**审查等级**：C。

**适用边界**：安全成本与训练信号耦合，提前终止可能降低成本而不代表完成任务；适合研究仿真中的约束权衡。

## 5. 相关论文（均来自本调研表）

- [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480)（2025，NeurIPS 2025 Spotlight; arXiv 2025 (v4 2026)）← **提出**

---

*文档依据主表记录和论文资料整理。*
