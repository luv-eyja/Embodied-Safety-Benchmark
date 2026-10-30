# ConflictVLA-Bench

> **所属环节**：VLA 评测；操作
> **分类**：VLA 安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

评估 VLA 对无效任务前提的行为响应（是否停止/拒绝 vs 继续执行），用成对 conflict/reference rollout 区分"行为脱离"与"失败坚持"，安全行为与终端成功率分离。

本条目关注的具身环节为 **VLA 评测；操作**，评测对象包括 **VLA; Manipulation**。

## 2. 怎么构建的

**场景与构建**：2,826 个 prompt-conditioned conflict 任务，4 个 conflict family、4 种结构配置、2 种 prompt 条件；基于 LIBERO。

**评测指标**：original goal completion; conflict-relative reduction; trajectory structure; action magnitude suppression; disengagement/refusal 行为。

## 3. 用这个基准测了什么

**被测对象**：VLA; Manipulation。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [ConflictVLA-Bench：VLA 前提冲突安全](https://arxiv.org/abs/2609.31792) | 2026 | arXiv 2026 (v1) | **提出** | original goal completion; conflict-relative reduction; trajectory structure; action magnitude suppression; disengagement/refusal 行为 |

## 4. 关键结论与改进方向

**关键结论**：LIBERO 上以 4 类前提冲突构造 2,826 个配对任务，用结果和过程指标揭示 VLA 的 Failed Persistence。

**改进方向**：公开固定测试数据与复现代码，并增加损害或风险指标，使行为脱离与任务失败可以进一步区分。

**审查等级**：C。

**适用边界**：代码和数据尚未稳定公开，当前缺少损害指标与充分统计；适合研究行为响应，不宜单独作为物理安全证据。

## 5. 相关论文（均来自本调研表）

- [ConflictVLA-Bench: Benchmarking Behavioral Responses of Vision-Language-Action Models to Premise Conflicts](https://arxiv.org/abs/2609.31792)（2026，arXiv 2026 (v1)）← **提出**

---

*文档依据主表记录和论文资料整理。*
