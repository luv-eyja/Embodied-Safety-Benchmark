# LIBERO-Safety

> **所属环节**：物理与语义安全；五类套件 × L0-L2 难度  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）
> **证据级别**：A（论文全文 + 官方项目页 + 官方代码核查）
>
> 具体的任务条目、UBDDL 参数、CuRobo 轨迹生成和运行接口见：[LIBERO-Safety：实现拆解与任务条目](../analysis/LIBERO-Safety-实现拆解.md)。

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models |
| 年份 | 2026 |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | VLA 与具身基础模型 |
| 关注属性 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 |
| 基础平台线索 | LIBERO |
| 规模线索 | 19,664 条严格无碰撞示范 |
| 执行环境线索 | 摘要提到仿真/模拟环境。 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：物理与语义安全；五类套件 × L0-L2 难度。

**摘要级问题描述**：提出 LIBERO-Safety，面向 VLA 的物理与语义安全进行统一评测。基准包含 affordance-aware grasping、human-robot interaction、tabletop spatial avoidance、free-space hand-object avoidance 与 semantic safety reasoning 五类套件，每类含 L0–L2 三档难度；通过 keypose-driven pipeline 生成 19,664 条严格无碰撞示范，并同时报告物理安全、语义安全和环境随机性下的鲁棒性。官方项目页注明已被 ECCV 2026 接收。

信息取自表内论文 *LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models*（该基准的提出者）。

**主要测量维度**：五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性。

## 2. 怎么构建的

### 2.1 构建要素

| 要素 | 摘要级记录 |
|---|---|
| 基础平台 | LIBERO |
| 任务/场景规模 | 19,664 条严格无碰撞示范 |
| 扰动、风险或约束 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 |
| 对照/配对方式 | 摘要未明确配对设计。 |
| 指标与判分线索 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 |
| 执行设置 | 摘要提到仿真/模拟环境。 |

### 2.2 详细说明

论文全文与官方实现进一步给出：UBDDL 将 BDDL 扩展为带场景随机化、动态实体和逐时刻安全约束的任务描述；场景通过 `:noise`、`:cam_view`、`:scene_xml`、`:robot_init_state` 和 `:dynamics` 参数化。数据生成只需人工提供 object-centric 稀疏 keypose，再用 CuRobo 规划碰撞无关轨迹；四个物理套件的 L0/L1 任务先为每项生成 500 条候选，经过人机协同筛选形成 19,664 条严格无碰撞示范。完整条目和文件路径见配套实现说明。

> 需要区分“75 个评测任务”和“40 个训练任务”：75 = 五套件 × 五任务 × L0–L2；训练集只覆盖四个物理套件的 L0/L1，因此是 40 个任务，不含 SSR 和 L2。

## 3. 用这个基准测了什么

**被测对象**：VLA 与具身基础模型

**结果应如何读取**：先按“评测维度/指标”字段区分主指标、辅助指标和对照条件；若论文同时报告任务成功与安全/鲁棒性结果，应将二者分开阅读。

下表按论文列出；“摘要级发现”保留调研表中的概要，不等同于全文实验结论。

| 论文 | 年份 / 来源 | 角色 | 被测对象 | 使用方式 / 指标 | 摘要级发现 |
|---|---|---|---|---|---|
| [LIBERO-Safety：VLA 物理与语义安全综合基准](https://arxiv.org/abs/2606.23686) | 2026 / ECCV 2026（欧洲计算机视觉会议）；arXiv… | **提出** | VLA 与具身基础模型 | 五类安全套件 × L0–L2 难度；物理安全成功率/违规率、语义安全拒答率、环境随机性鲁棒性 | 提出 LIBERO-Safety，面向 VLA 的物理与语义安全进行统一评测。 |

## 4. 关键结论、改进方向与可复用性

**摘要级发现（按关联论文整理）**：

- **LIBERO-Safety：VLA 物理与语义安全综合基准**（2026，提出）：提出 LIBERO-Safety，面向 VLA 的物理与语义安全进行统一评测。基准包含 affordance-aware grasping、human-robot interaction、tabletop spatial avoidance、free-space hand-object avoidance 与 semantic safety reasoning 五类套件，每类含 L0–L2 三档难度；

**基于当前字段的改进提示（不是原文逐字结论）**：

- 按扰动轴、严重度和 clean/OOD 对照分别报告结果，避免只保留聚合成功率。
- 补充约束定义、违规阈值和过程/终态指标，确认安全成功与任务成功是否分开统计。
- 核对安全/不安全语境或指令的配对构造，确认是否控制了视觉场景和动作要求。
- 当前尚无跨论文复用证据，需由独立工作复测后再形成稳定的横向结论。

**复用状态**：当前只看到提出论文，尚无跨论文复用证据。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)（2026，ECCV 2026（欧洲计算机视觉会议）；arXiv 预印本 (arXiv:26）  ← **提出**

## 6. 证据边界与复核建议

- **证据级别**：A（提出论文全文、官方项目页、官方代码仓库与任务清单均已核查）。
- **主要来源**：[LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2606.23686)。
- **当前限制**：官方仓库已公开评测代码、资产和训练数据，但 README 仍注明完整 data-generation pipeline 将后续开源；因此本地说明能够复现任务注册、场景加载、渲染和评测接口，不能替代未公开的完整生成器。
- **建议复核**：运行前确认 `assets`、`bddl_files`、`init_states` 和 `datasets` 路径，并核对具体模型的动作空间、chunk 长度和停止条件。

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成。 A 级文档含人工扩写字段；核心条目附本地全文核查补录；B/C 级文档主要依赖摘要级结构化记录。*
