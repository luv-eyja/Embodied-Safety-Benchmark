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
| OpenAlex 引用快照 | [0](https://openalex.org/W7220458345)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 3 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

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
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Sangwu Park, Yeonjun In, Wonjoong Kim, et al., ‘ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation,’ arXiv preprint, 2026, arXiv:2610.02802v1. [论文](https://arxiv.org/abs/2610.02802)；[核查正文](https://arxiv.org/html/2610.02802v1)。

**重点核查位置（章节主题）**：4 Solver-based Assessment；5.1 Benchmark Construction；5.2 Evaluation Protocol and Metrics；6.1 Main Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7220458345)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/sangwu99/ManiPhysicsBench_Arxiv](https://github.com/sangwu99/ManiPhysicsBench_Arxiv)。地址状态为 `candidate`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（候选待确认，2026-11-04）

**项目入口**：[https://github.com/sangwu99/ManiPhysicsBench_Arxiv](https://github.com/sangwu99/ManiPhysicsBench_Arxiv)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/sangwu99/ManiPhysicsBench_Arxiv) | https://raw.githubusercontent.com/sangwu99/ManiPhysicsBench_Arxiv/HEAD/README.md | stars 3，最后推送 2026-10-02，保留文本 2520 字符（截断） |

**项目页显示**：GitHub https://github.com/sangwu99/ManiPhysicsBench_Arxiv（3 stars，2026-10-02 推送）README 给出目录结构、conda 环境与 FEM 安装脚本（CalculiX 2.23、FEBio 4.13、OpenRadioss），并说明需写入 runtime/fem.json。

**涉及领域**：VLA 操作中的物体保全（object preservation）；用外部力学求解器评估抓握是否造成损伤。

**测试目的与构建方法**：刚体仿真记录接触位置、方向与力，外部 FEM 求解器（CalculiX／FEBio／OpenRadioss）结合几何与材料阈值判定每次抓握损伤，再汇总整段轨迹；SR 为完成率，Safe SR 为无损完成率，PR=Safe SR/SR。

**测试缺陷**：损伤由求解器事后判定，不是仿真中真的断裂；材料与接触模型、连续夹爪设置会改变结论；SR 为零时 PR 未定义；计算成本高（需安装三个 FEM 后端）。

**与具身智能安全的相关性**：直接且少见的“物理后果”指标：它测的不是碰撞次数，而是物体是否被夹坏。补上了成功率无法反映的损伤维度，但仍是仿真近似。

**用这个 benchmark 测了什么**：SimplerEnv 的高／中难对象上，公共 checkpoint 平均 SR 48.3%、Safe SR 13.5%、PR 27.9%——多数模型能搬动却保不住物体。

**本轮核查边界**：仓库状态为 candidate（作者仓库，未完全确认官方）；未实际安装 FEM 后端。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 4 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **PR** | Preservation Rate（本库 ManiPhysicsBench 口径） | 保全率 | Safe SR ÷ SR，即“成功的那些里，对象完好的比例”。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。
- **PR**：把 PR 当 precision，或只报 PR 不报 SR。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| ManiPhysicsBench | 基准 | 物体保全物理评估基准 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| SimplerEnv | 基准 | 真实策略的仿真代理评测 |

<!-- glossary:end -->
