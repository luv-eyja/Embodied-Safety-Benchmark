# Open X-Embodiment

<!-- survey-classification:start -->
> **统一调研分类**：训练数据集；具身研究底座；目标：能力。
> **分类依据**：主要是异构数据整合与训练项目，不存在一套全项目统一安全分。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：跨本体真机数据  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 0、使用 1；方法参考另标）
> **证据级别**：原表 C；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)；[https://github.com/google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Open X-Embodiment: Robotic Learning Datasets and RT-X Models |
| 年份 | 2023（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 跨本体真机训练数据与模型 |
| 历史关键词标签（未重新统计） | 任务能力 |
| 评测维度/指标 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 原论文聚合 22 种本体、100 万余真实轨迹和 527 种技能；不同来源的相机、动作、任务分布明显异构。 |
| 执行环境线索 | 跨本体真机训练数据与模型 |
| 来源审计 | [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)；external_original_paper |
| 来源核验依据 | AgiBot World Colosseo 论文使用 Open X-Embodiment；官方仓库也将该论文列为 Open X-Embodiment 的首篇论文。 |
| OpenAlex 引用快照 | [113](https://openalex.org/W4387764390)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 9 个缩写／技术词，并标出 5 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：来自不同实验室与机器人形态的数据能否共同训练可迁移的操作策略？

**评测层级**：跨本体真机训练数据与模型。

## 2. 怎么构建的

**核心场景与条目**：原论文聚合 22 种本体、100 万余真实轨迹和 527 种技能；不同来源的相机、动作、任务分布明显异构。

**实现与判分**：统一到 RLDS 数据表示并建立动作／观察适配，以 RT-X（VLA 模型） 等模型比较单来源与跨本体训练，分别测试已有任务和域外能力。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088) | 2025 | 使用 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 | 以「可扩展的机器人数据」回应通用操作的真机挑战：AgiBot World 是含 100 万余条轨迹、217 个任务、5 类部署场景的大规模平台，数据规模比既有数据集高一个数量级；标准化采集流水线配合人在环校验保证质量与分布多样性，并可从夹爪扩展到灵巧手与视触觉传感器以获取细粒度技能。在数据之上提出通用策略 Genie Operator-1（GO-1）。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：实验支持跨机器人数据存在正迁移，但并不意味着任意数据混合都同样有效。成果是数据联盟、标准化接口以及跨本体策略。

**适用边界**：这是训练数据集合与研究项目，不是具有单一冻结测试集的安全 benchmark；不同论文使用的混合比例、过滤和版本必须注明。引用量对应论文记录，不等于每个子数据集的影响力。

## 5. 相关论文（均来自本调研表）

- [AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems](https://doi.org/10.1109/IROS60139.2025.11247088)（2025；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

这是训练数据集合与研究项目，不是具有单一冻结测试集的安全 benchmark；不同论文使用的混合比例、过滤和版本必须注明。引用量对应论文记录，不等于每个子数据集的影响力。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Open X-Embodiment Collaboration, Abby O'Neill, Abdul Rehman, et al., ‘Open X-Embodiment: Robotic Learning Datasets and RT-X Models,’ arXiv preprint, 2023, arXiv:2310.08864v9. [论文](https://arxiv.org/abs/2310.08864)；[核查正文](https://arxiv.org/html/2310.08864v9)。

**重点核查位置（章节主题）**：III Data Collection；IV Data Format；V Experiments。

OpenAlex 被引次数：**[113](https://openalex.org/W4387764390)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)；[https://github.com/google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **113** 篇引文论文（清单保留被引最高的 25 篇）；arXiv 摘要命中 25 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://robotics-transformer-x.github.io/](https://robotics-transformer-x.github.io/)；[https://github.com/google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://robotics-transformer-x.github.io/) | https://robotics-transformer-x.github.io/ | 保留文本 4200 字符（截断） |
| [repo](https://github.com/google-deepmind/open_x_embodiment) | https://raw.githubusercontent.com/google-deepmind/open_x_embodiment/HEAD/README.md | stars 2090，license Apache-2.0（开源许可证），最后推送 2025-11-05，保留文本 4200 字符（截断） |

**项目页显示**：官网 https://robotics-transformer-x.github.io/ 与 GitHub https://github.com/google-deepmind/open_x_embodiment（2,090 stars，Apache-2.0，2025-11-05 推送）并存，README 给 RLDS 结构与自包含 Colab。

**涉及领域**：跨本体机器人数据集合与 RT-X 模型；统一 RLDS 表示，覆盖多家机构与多种机器人。

**测试目的与构建方法**：把各机构数据统一到 RLDS episode 格式并建立动作／观察适配，用 RT-X 等模型比较单来源与跨本体训练，分别测已有任务与域外能力。

**测试缺陷**：它是训练数据集合与研究项目，不是有单一冻结测试集的安全 benchmark；不同论文的混合比例、过滤与版本必须注明；跨本体正迁移不代表任意混合都有效。

**与具身智能安全的相关性**：弱：提供的是数据底座，可支撑安全策略训练，但自身不定义风险；若用于安全微调，需另行标注数据来源与许可。

**用这个 benchmark 测了什么**：实验支持跨机器人数据存在正迁移，但不意味着任意混合都同样有效；113 篇引文含机器人基础模型综述；arXiv 命中含在 PushT 等子集上训练的小模型（如 68M 参数、0.008 MSE 的下一状态预测）。

**本轮核查边界**：只读官网与 README，未下载任何子数据集。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| LLARVA: Vision-Action Instruction Tuning Enhances Robot Learning（2024） | LLARVA（视觉—动作指令微调） | 预训练数据（从该数据集生成 8.5M 图文—视觉轨迹对） | 用 Open X-Embodiment 生成预训练对；在 RLBench 12 个任务与真实 Franka Panda 上评测 | 产出 8.5M 预训练样本；下游在 12 个 RLBench 任务与真机上评测 |
| MoS-VLA: A Vision-Language-Action Model with One-Shot Skill Adaptation（2025） | MoS-VLA（技能基函数） | 预训练数据（跨数据集联合预训练） | 在 Open X-Embodiment 各数据集上联合学习基函数，形成结构化技能空间 | 摘要只说明预训练方式与技能空间，未给数值 |
| Video-Language Critic: Transferable Reward Functions for Language-Cond…（2024） | Video-Language Critic（奖励模型） | 训练数据（训练奖励函数），再用于 RL | 在 Open X-Embodiment 上训练奖励模型；在 Meta-World 任务上用作 RL 奖励 | 相比只用稀疏奖励，策略训练样本效率提升 2 倍（尽管存在明显域差） |
| HCLSM: Hierarchical Causal Latent State Machines for Object-Centric Wo…（2026） | HCLSM（68M 参数世界模型） | 子集训练 + 评测（取 PushT 子集） | Open X-Embodiment 的 PushT 子集，下一状态预测 MSE 与 SBD loss | 0.008 MSE；SBD loss 0.0075 |
| StableVLA: Towards Robust Vision-Language-Action Models without Extra…（2026） | StableVLA（0.5B 主干） | 对照条件（明确“未在该数据集上预训练”） | 与 7B 级 SOTA VLA 比鲁棒性 | 不做 Open X-Embodiment 预训练、主干小 14 倍，鲁棒性仍与 7B 模型相当 |

**原文片段（摘要）**：

- LLARVA: Vision-Action Instruction Tuning Enhances Robot Lear…（2024，arXiv）：> We generate 8.5M image-visual trace pairs from the Open X-Embodiment dataset in order to pre-train our model
- MoS-VLA: A Vision-Language-Action Model with One-Shot Skill…（2025，arXiv）：> During pretraining, MoS-VLA jointly learns these basis functions across datasets from the Open X-Embodiment project
- Video-Language Critic: Transferable Reward Functions for Lan…（2024，arXiv）：> When trained on Open X-Embodiment data, our reward model enables 2x more sample-efficient policy training on Meta-World
- HCLSM: Hierarchical Causal Latent State Machines for Object-…（2026，arXiv）：> We train a 68M-parameter model on the PushT robotic manipulation benchmark from the Open X-Embodiment dataset, achieving 0.008 MSE
- StableVLA: Towards Robust Vision-Language-Action Models with…（2026，arXiv）：> even with a 14x smaller backbone (0.5B parameters) and no pre-training on the Open X-Embodiment dataset

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 9 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **MSE** | Mean Squared Error | 均方误差 | 预测值与真值差的平方的平均，用于回归与世界模型预测。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **GO-1** | AgiBot GO-1 | AgiBot 通用策略 | AgiBot 随数据集一起发布的通用操作策略。 |
| **RL** | Reinforcement Learning | 强化学习 | 用奖励信号优化策略，区别于用示范做监督学习。 |
| **SOTA** | State of the Art | 当前最佳水平 | 论文自称的最好成绩；对照条件不同则不可比。 |
| **RLDS** | Reinforcement Learning Datasets format | RLDS 数据格式 | 把机器人数据统一成 episode 序列的通用格式，便于跨数据集训练。 |
| **RLBench** | RLBench | RLBench 操作基准环境 | CoppeliaSim 上的机械臂任务集，常作泛化评测的底座。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| Open X-Embodiment | 数据集 | 跨机构机器人数据集合 |
| AgiBot World | 数据集 | 真机双臂操作数据集与平台 |
| RLBench | 基准 | CoppeliaSim 上的机械臂任务集 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 RT-X（VLA 模型）、Apache-2.0（开源许可证）），不再重复解释。

<!-- glossary:end -->
