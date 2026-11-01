# 近期具身智能 Benchmark 论文补充

> 截止 2026-11-01。筛选范围为 2025-11-01 至 2026-11-01，优先选择论文明确提出 benchmark、给出规模/协议/指标，并能用 arXiv 或官方页面核验的工作。安全相关论文优先级更高；“已在当前论文表中”的条目不重复计入新记录，但列出其新增价值。

## 推荐优先纳入或重点跟踪

| 论文 / benchmark | 时间 | 核心评测对象 | 规模或协议线索 | 与本库关系 | 优先级 |
|---|---:|---|---|---|---:|
| [EmbodiedLab](https://arxiv.org/abs/2610.35385) | 2026-10 | 具身智能体的主动实验与科学发现 | 30 个实验、5 个学科、14 类仪器平台；要求通过交互读取观测并验证物理状态 | 新条目；扩展“行动-知识获取”能力 | 高 |
| [BEHAVIOR-Spatial](https://arxiv.org/abs/2610.34051) | 2026-10 | 空间理解、目标接地到 VLA 行为 | 3,256 个空间问题、1,240 个接地查询，并覆盖操作与导航动作 | 新条目；补足空间接地与行为一致性 | 高 |
| [SO-101 VLA benchmark](https://arxiv.org/abs/2606.08881) | 2026-06 | 低成本真机 VLA 失败与恢复 | 4 个操作任务；失败 taxonomy、语义/执行分解和 recovery-aware 指标 | 新条目；适合作为真机安全桥接 | 高 |
| [RoboCasa-Shift](https://arxiv.org/abs/2610.27861) | 2026-10 | 长时程家务操作在分布偏移下的阶段性退化 | clean/perturbed 配对 rollout；4 个扰动因素、3 个严重度、1,040 次正式 rollout | 已在表内；应与 RoboCasa365 原始来源关联 | 高 |
| [RoboHarm](https://arxiv.org/abs/2610.14043) | 2026-10 | 有害指令从语言接口迁移到机器人控制后的拒答 | 文本、代码策略、末端位姿、关节控制与真机对照 | 已在表内；来源已补标 | 高 |
| [RoboAbstention](https://arxiv.org/abs/2605.20544) | 2026-05 | 具身弃权：不可行、歧义、错误前提与感知不足 | 6,069 条 benchmark 指令；结构化接地、约束推导和模板生成 | 已在表内；来源已补标 | 高 |
| [DESPITE](https://arxiv.org/abs/2604.18463) | 2026-04 | LLM 具身规划的物理与规范安全 | 12,279 个确定性验证任务；分离 planning ability 与 safety awareness | 已在表内；来源已补标 | 高 |
| [EmbodiedGovBench](https://arxiv.org/abs/2604.11174) | 2026-04 | 具身系统治理、恢复和升级安全 | 未授权能力调用、运行时漂移、恢复、策略迁移、升级、人类覆盖、审计完整性七维 | 已在表内；可扩展实时/治理轴 | 中高 |
| [CEBench](https://arxiv.org/abs/2602.22663) | 2026-02 | VLA 实用性、跨本体与仿真-真机迁移 | 14.4k 仿真轨迹、1.6k 真机轨迹；覆盖多种本体与域随机化 | 新条目；补足能力和部署维度 | 中高 |

## 建议纳入顺序

1. **先纳入 BEHAVIOR-Spatial、EmbodiedLab、SO-101**：三者分别覆盖空间接地、主动实验和低成本真机恢复，能明显扩大当前 benchmark 的能力边界。
2. **再完善安全专题**：RoboHarm、RoboAbstention、DESPITE、EmbodiedGovBench 已经进入当前论文表，但应使用本次来源审计后的“提出/使用”角色重新生成卡片统计。
3. **补充 CEBench**：它更偏实用性和跨本体，不是纯安全基准；适合作为能力-部署对照，不宜与安全分数直接横向合并。

机器可读候选表：[`data/recent_embodied_benchmark_papers.json`](../data/recent_embodied_benchmark_papers.json)。

## 纳入前的检查项

- 确认论文版本和 benchmark release 是否一致，尤其是 2026 年 10 月刚发布的条目；
- 记录代码、数据、模拟器版本和真机硬件，避免把“论文提出”误当作“已经可复现”；
- 对安全基准同时记录能力分数、违规/风险分数、拒答或恢复分数，避免回到只看 task success 的单指标比较。
