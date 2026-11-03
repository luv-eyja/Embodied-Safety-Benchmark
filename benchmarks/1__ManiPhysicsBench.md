# ManiPhysicsBench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：附资产库与求解器，但主要建立物体保全测试。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（物理后果：形变/断裂）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`candidate`；[https://github.com/sangwu99/ManiPhysicsBench_Arxiv](https://github.com/sangwu99/ManiPhysicsBench_Arxiv)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真轨迹＋离线物理损伤评估 |
| 历史关键词标签（未重新统计） | 物理/接触安全、任务能力 |
| 评测维度/指标 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 |
| 基础平台线索 | LIBERO、SimplerEnv |
| 规模线索 | 91 个对象的 ManiPhysicsZoo 支撑脆性断裂、软物体变形、薄壁变形三条轴；鸡蛋／核桃、土豆／水果、纸杯／塑料容器等分难度部署到 LIBERO 与 SimplerEnv。 |
| 执行环境线索 | 仿真轨迹＋离线物理损伤评估 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7220458345)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：把物体成功搬到目标位置时，物体是否已经被夹碎或压坏？

**评测层级**：仿真轨迹＋离线物理损伤评估。

## 2. 怎么构建的

**核心场景与条目**：91 个对象的 ManiPhysicsZoo 支撑脆性断裂、软物体变形、薄壁变形三条轴；鸡蛋／核桃、土豆／水果、纸杯／塑料容器等分难度部署到 LIBERO 与 SimplerEnv。

**实现与判分**：刚体仿真记录接触位置、方向和力，外部力学求解器结合几何与材料阈值判定每次抓握损伤，再汇总整段轨迹。SR 为完成率，Safe SR 为无损完成率，PR=Safe SR/SR。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802) | 2026 | 提出 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 | 指出刚体基准中的任务成功并不能说明模型是否保全了物体。ManiPhysicsZoo 汇总文献支撑的材质属性、3D 网格与参考文献形成可复用物体资产，再由基于求解器的评估依据几何、材质与抓取条件计算损伤阈值并与实测接触力比较，从而在 LIBERO 与 SimplerEnv 上区分「完成任务」与「安全完成任务」，公开 VLA 检查点在两者间存在显著差距。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：SimplerEnv 的高、中难对象上，公共 checkpoint 平均 SR 为 48.3%、Safe SR 为 13.5%，PR 为 27.9%；多数模型完成搬运却不能保护对象。

**适用边界**：损伤由求解器事后判断，并非仿真中直接产生真实断裂。材料、接触模型及连续夹爪设置影响结论；SR 为零时 PR 未定义。

## 5. 相关论文（均来自本调研表）

- [ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation](https://arxiv.org/abs/2610.02802)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

损伤由求解器事后判断，并非仿真中直接产生真实断裂。材料、接触模型及连续夹爪设置影响结论；SR 为零时 PR 未定义。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Sangwu Park, Yeonjun In, Wonjoong Kim, et al., ‘ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation,’ arXiv preprint, 2026, arXiv:2610.02802v1. [论文](https://arxiv.org/abs/2610.02802)；[核查正文](https://arxiv.org/html/2610.02802v1)。

**重点核查位置（章节主题）**：4 Solver-based Assessment；5.1 Benchmark Construction；5.2 Evaluation Protocol and Metrics；6.1 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7220458345)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/sangwu99/ManiPhysicsBench_Arxiv](https://github.com/sangwu99/ManiPhysicsBench_Arxiv)。地址状态为 `candidate`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
