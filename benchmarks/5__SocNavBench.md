# SocNavBench

> **所属环节**：具身安全/鲁棒性基准（非 VLA 专项）；社会导航
> **分类**：具身安全
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

社会导航仿真测试框架，用真实行人数据驱动的场景 + 指标套件评测机器人安全/合社交地与人共行；碰撞与个人空间等安全指标同任务指标分开。

本条目关注的具身环节为 **具身安全/鲁棒性基准（非 VLA 专项）；社会导航**，评测对象包括 **Navigation; Mobile Robot; HRI**。

## 2. 怎么构建的

**场景与构建**：照片级仿真器 + 基于真实行人数据的社会导航场景；3 个已有方法 + 1 baseline。

**评测指标**：collision; personal space/social compliance; success/path efficiency (capability)。

## 3. 用这个基准测了什么

**被测对象**：Navigation; Mobile Robot; HRI。

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---:|---|---|---|
| [SocNavBench：社会导航基准](https://arxiv.org/abs/2103.00047) | 2021 | ACM Transactions on Human-Robot Interaction (THRI) 2022; arXiv v1 2021-02 | **提出** | collision; personal space/social compliance; success/path efficiency (capability) |

## 4. 关键结论与改进方向

**关键结论**：真实行人轨迹回放和 33 个手工场景共同支持社会导航算法的成功率、碰撞、最近距离与 TTC 评测。

**改进方向**：加入会响应机器人的行人模型，补充风险严重度和真实场景验证，并完善代码中的聚合与成功判定。

**审查等级**：C。

**适用边界**：行人轨迹不响应机器人，缺少严重度和真实场景验证，代码聚合与成功判定仍需完善；适合社会导航仿真比较。

## 5. 相关论文（均来自本调研表）

- [SocNavBench: A Grounded Simulation Testing Framework for Evaluating Social Navigation](https://arxiv.org/abs/2103.00047)（2021，ACM Transactions on Human-Robot Interaction (THRI) 2022; arXiv v1 2021-02）← **提出**

---

*文档依据主表记录和论文资料整理。*
