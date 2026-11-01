# 附录：122 个基准的覆盖矩阵

本文件由 `scripts/coverage.py` 生成，用于支撑设计方案 §1.1 的缺口论证。

## 统计口径

- 对每个基准，取「提出论文」的 *评测维度* + *内容概要* + 基准定位描述，做关键词匹配
- 一个基准可同时命中多个环节与多个安全属性，因此**行合计大于基准数**，属性合计为重复计数
- 用途仅在于看**相对稀疏度**，不作为精确计量

## 环节 × 安全属性

| 环节 | 语义/指令安全 | 物理/接触安全 | 对抗/后门安全 | 分布偏移鲁棒性 | 失败恢复 | 实时/治理 | 合计 |
|---|---|---|---|---|---|---|---|
| 感知层 | 21 | 21 | 4 | 23 | 14 | 4 | **87** |
| 认知/语义层 | 37 | 24 | 6 | 14 | 8 | 5 | **94** |
| 规划层 | 12 | 13 | 7 | 11 | 11 | 3 | **57** |
| 动作控制层 | 28 | 37 | 9 | 28 | 19 | 11 | **132** |
| 终态/后果层 | 0 | 6 | 0 | 0 | 1 | 1 | **8** |
| **合计** | **98** | **105** | **28** | **80** | **56** | **24** | 391 |

## 关键读数

- **终态/后果层仅 8 个**（122 个中），其中 6 个触及物理/接触安全 —— 这是最大的空白
- **实时/治理仅 24 个**，真正把决策延迟当一等变量的只有 RT-Safe（城市导航）
- **规划层 57 个**，是各环节中最稀疏的
- **对抗/后门 26 个**，且多为攻击方法自带评测，不是可复用基准

## 覆盖 4 类及以上安全属性的基准

| 基准 | 覆盖属性数 |
|---|---|
| EmbodiedGovBench | 4 |

> 结论：**122 个基准中只有 1 个同时覆盖 4 类以上安全属性**，
没有任何一个覆盖全部 6 类。这直接支撑了设计方案 §1.1 的判断。

## 覆盖 3 类安全属性的基准

AGENTSAFE / SAFE-THOR、ASIMOV Benchmark、BAVO-Bench、BLINDSPOT、DriveDegrade、ForesightSafety-VLA、IndustrialVLA-Bench、LIBERO-Para、LIBERO-Safety、LIBERO-X、LongBench、MMA-SafetyBench、ManiGuard-Bench、Robo2Process、RoboAbstention、RoboColiseum、RoboFollow、RoboIRG-Bench、RoboJailBench、RoboStress、RoboVAD、SafeVLA-Bench、Trap-LIBERO / Trap-RoboTwin、VIPS、VestaBench