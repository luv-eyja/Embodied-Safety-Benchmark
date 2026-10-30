# LIBERO-Safety

> **所属环节**：VLA 评测；操作
> **分类**：VLA 安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

参数化生成安全关键场景,同时评物理安全与语义安全,并保持与任务成功分离。

本条目关注的具身环节为 **VLA 评测；操作**，评测对象包括 **VLA; Manipulation**。

## 2. 怎么构建的

**场景与构建**：40 个任务; L0-L2 参数化难度; 静态/动态场景; 物理+语义安全; 近端人-机器人交互。

**评测指标**：physical safety success rate (SR); semantic safety refusal rate (RR); collision rate (CR); task success (capability); 19,664 collision-free demonstrations。

## 3. 用这个基准测了什么

**被测对象**：VLA; Manipulation。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [LIBERO-Safety：物理+语义安全基准](https://arxiv.org/abs/2606.23686) | 2026 | arXiv 2026-06 v1; v2 2026-06-26; ECCV 2026 | **提出** | physical safety success rate (SR); semantic safety refusal rate (RR); collision rate (CR); task success (capability); 19,664 collision-free demonstrations |

## 4. 关键结论与改进方向

**关键结论**：基准把桌面操作中的物理安全和语义安全分别评估，并通过 5×3 难度分层与 L2/SSR 留出设置考察泛化。

**改进方向**：完善数据与评测脚本发布，验证各任务中的接触约束，并限制仅靠拒绝指令获得高分的策略。

**审查等级**：C。

**适用边界**：公开实现的部分接触约束和评测脚本仍不完整，语义轨存在全拒绝刷分风险；仅适合作为仿真桌面操作研究参考。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)（2026，arXiv 2026-06 v1; v2 2026-06-26; ECCV 2026）← **提出**

---

*文档依据主表记录和论文资料整理。*
