# CARLA / CARLA Leaderboard

> **所属环节**：城市驾驶仿真与排行榜  
> **分类**：具身安全  
> **关联论文**：本表 4 篇（提出者 1 篇，使用者 3 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：城市驾驶仿真与排行榜。

指出自动驾驶智能体依赖多个 ML 模型、控制逻辑与自定义模块的组合输出，虽然大量先前工作已证明对抗样本能误导单个 ML 模型，但这些攻击能否对不同智能体、环境与场景产生有害驾驶动作仍不清楚。作者主张针对智能体整体而非孤立模型评估，用 CARLA 城市驾驶仿真器在运行时把对抗补丁注入并针对 CARLA Leaderboard 上的多个智能体评测。

信息取自表内论文 *Attacking Autonomous Driving Agents with Adversarial Machine Learning: A Holistic Evaluation with the CARLA Leaderboard*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：对抗补丁实时注入；针对智能体而非孤立 ML 模型。

## 3. 用这个基准测了什么

**被测对象**：CARLA Leaderboard 上的多种驾驶智能体。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [Language2Drive：驾驶 VLA 的指令遵循基准](https://arxiv.org/abs/2610.16634) | 2026 | arXiv 预印本 (arXiv:2610.16 | 使用 | 配对反事实单元（固定场景只改指令）；四类指令遵循范围 |
| [基于 CARLA Leaderboard 的自动驾驶智能体对抗攻击整体评测](https://arxiv.org/abs/2511.14876) | 2025 | arXiv 预印本 (arXiv:2511.14 | **提出** | 对抗补丁实时注入；针对智能体而非孤立 ML 模型 |
| [DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准](https://arxiv.org/abs/2608.29005) | 2026 | arXiv 预印本 (arXiv:2608.29 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 |
| [SIREN-Bench：紧急车辆交互的行为驱动生成与评测](https://arxiv.org/abs/2608.24094) | 2026 | arXiv 预印本 (arXiv:2608.24 | 使用 | SUMO–CARLA 联合仿真；行为级控制特权与响应 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **Language2Drive：驾驶 VLA 的指令遵循基准**（2026）：该基准以配对反事实单元为评测单位：固定初始驾驶场景、只改指令，从而把孤立的指令成功与配对反事实成功区分开，覆盖四种指令遵循范围，并可检验该区分是否在不同评测区间持续成立。
- **DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准**（2026）：基准把 16 类退化在 5 个严重度下于图像加载器内即时注入，单一算子即可触达 15 个策略。
- **SIREN-Bench：紧急车辆交互的行为驱动生成与评测**（2026）：SIREN 把 SUMO 的网络级交通演化与行为逻辑同 CARLA 的连续车辆控制与同步车载感知耦合起来。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?（2026，arXiv 预印本 (arXiv:2610.16634)）
- Attacking Autonomous Driving Agents with Adversarial Machine Learning: A Holistic Evaluation with the CARLA Leaderboard（2025，arXiv 预印本 (arXiv:2511.14876)）  ← **提出**
- A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving（2026，arXiv 预印本 (arXiv:2608.29005)）
- SIREN-Bench: Behavior-Driven Generation and Evaluation of Emergency-Vehicle Interactions（2026，arXiv 预印本 (arXiv:2608.24094)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
