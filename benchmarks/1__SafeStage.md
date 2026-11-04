# SafeStage

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：显式分阶段安全任务与验证器。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：全栈（规划前的场景理解 → 执行期控制 → 终态稳定性）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`candidate`；[https://github.com/reeta-042/safestage](https://github.com/reeta-042/safestage)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真全流程操作安全 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 三阶段安全：初始状态危害 / 执行期安全 / 终态危害 |
| 基础平台线索 | Franka、RoboLab、PhysX |
| 规模线索 | 97 个任务：初始危险 ISH 27、执行阶段 ETS 40、完成后 FSH 30；RoboLab／GPU PhysX 中的 Panda＋Robotiq 机械臂，完成后继续观察 5 秒。 |
| 执行环境线索 | 仿真全流程操作安全 |
| 全文状态 | 已核查本地全文：`docs/_fulltext/SafeStage.txt` |
| OpenAlex 引用快照 | [0](https://openalex.org/W7213988552)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 13 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：任务开始前、执行中和完成后的危险，是否被只检查终点成功的评测遗漏？

**评测层级**：仿真全流程操作安全。

## 2. 怎么构建的

**核心场景与条目**：97 个任务：初始危险 ISH 27、执行阶段 ETS 40、完成后 FSH 30；RoboLab／GPU PhysX 中的 Panda＋Robotiq 机械臂，完成后继续观察 5 秒。

**实现与判分**：将危险状态、路径／接触约束、终态稳定性绑定到不同阶段，以仿真特权状态评分但不提供给策略；报告 SR、VR、SSR、USR，其中 SR=SSR+USR。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation](https://arxiv.org/abs/2609.21223) | 2026 | 提出 | 三阶段安全：初始状态危害 / 执行期安全 / 终态危害 | 把操作安全拆成「做之前、做的过程中、做完之后」三阶段，97 个专门设计的风险场景分别考察必须先行化解的初始状态危害、执行期的不安全接触/轨迹/区域进入/物体交互，以及名义任务完成后残留的不稳定或不安全状态，用于定位安全究竟在闭环操作的哪一环失效。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：报告聚合 SR 33.74%、SSR 9.84%、USR 23.90%；成功轨迹中 70.84% 含不安全行为。评估器在 240 条核查轨迹上 F1 为 97.26%。

**适用边界**：机器人硬件名称不意味着做了真机评测。成功中违规比例与全 episode 的 USR 分母不同，评估器准确度也不代表策略安全度。

## 5. 相关论文（均来自本调研表）

- [SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation](https://arxiv.org/abs/2609.21223)（2026；提出）

## 6. 证据边界与复核建议

### 6.1 全文核查补录（核心论文）

> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。

**来源文件**：`docs/_fulltext/SafeStage.txt`。

**评测协议**：97 个专门设计任务：ISH 27、ETS 40、FSH 30。每个任务同时定义目标、主动安全条件、不安全路径和安全解；在 RoboLab GPU PhysX（120 Hz）中使用 7-DoF Franka Panda + Robotiq 2F-85，8D 绝对关节位置/夹爪动作，15 Hz 闭环执行。每个任务-策略-提示条件使用 3 个环境种子、每种子 10 次 rollout；提示分为默认、generic、specific。

**定量证据**：评估器使用位姿、接触、支撑、包含关系、区域、位移、朝向和速度等 privileged 信号；接触阈值为 >0.1 N 且需跨多帧持续。FSH 在任务完成后保持机器人姿态并继续观察 5 秒。对 240 条人工核验 rollout 的自动判分精度为 95.81%、召回率 98.77%、F1 97.26%；分阶段 F1 为 ISH 98.65、ETS 96.43、FSH 95.65。默认提示汇总 SR 33.74%、SSR 9.84%，成功但不安全的 rollout 占全部 23.90%；在默认成功 rollout 中 70.84% 不安全。

**全文结论**：specific 提示并未自动带来安全性提升：其成功执行中 73.16% 不安全；generic 提示下该比例为 69.98%。generic 条件的 ISH/FSH 成功 rollout 中不安全比例分别为 86.77%/82.17%，ETS 为 50.93%，说明初态与终态风险容易被任务成功率掩盖。

**适用边界**：全文报告的是 RoboLab 仿真和预训练策略的结果；提示词、模型清单与任务级结果需结合原文附录逐项复核，不能把 SSR 直接解释为真实部署事故率。

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

机器人硬件名称不意味着做了真机评测。成功中违规比例与全 episode 的 USR 分母不同，评估器准确度也不代表策略安全度。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Jinzhu Luo, Qi Zhang, Wei Wang, et al., ‘SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation,’ arXiv preprint, 2026, arXiv:2609.21223v1. [论文](https://arxiv.org/abs/2609.21223)；[核查正文](https://arxiv.org/html/2609.21223v1)。

**重点核查位置（章节主题）**：Benchmark Construction；Evaluation Protocol；Experimental Results。

OpenAlex 被引次数：**[0](https://openalex.org/W7213988552)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/reeta-042/safestage](https://github.com/reeta-042/safestage)。地址状态为 `candidate`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（候选待确认，2026-11-04）

**项目入口**：[https://github.com/reeta-042/safestage](https://github.com/reeta-042/safestage)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/reeta-042/safestage) | https://raw.githubusercontent.com/reeta-042/safestage/HEAD/README.md | stars 0，最后推送 2026-08-31，保留文本 4200 字符（截断） |

**项目页显示**：抓取到的 https://github.com/reeta-042/safestage（0 stars，2026-08-31 推送）README 内容是 FortyGuard 的热环境决策平台，与机器人安全基准无关；因此本条的代码与数据可用性仍为未知。

**涉及领域**：分阶段安全评测（论文侧）：把危险状态、路径／接触约束与终态稳定性绑定到不同阶段；仿真中的操作任务。

**测试目的与构建方法**：将危险状态、路径与接触约束、终态稳定性绑定到不同阶段，用仿真特权状态评分但不提供给策略；报告 SR、VR、SSR、USR，其中 SR=SSR+USR。

**测试缺陷**：本库审计给出的项目地址（github.com/reeta-042/safestage）实际是一个同名但无关的“气候运营平台”，与论文基准无对应关系——**项目入口不可用**；评估器准确度不代表策略安全度；成功中违规比例与全 episode 的 USR 分母不同。

**与具身智能安全的相关性**：直接：唯一按“执行前／中／后”分阶段给安全指标的设计之一，能区分“没出事”和“没违规”。但项目不可得，只能依赖论文。

**用这个 benchmark 测了什么**：论文报告聚合 SR 33.74%、SSR 9.84%、USR 23.90%——成功轨迹中 70.84% 含不安全行为；评估器在 240 条核查轨迹上 F1 为 97.26%。

**本轮核查边界**：项目地址疑为同名误配；本轮未能找到真正的 SafeStage 仓库。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 13 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **rollout** | rollout | 展开／推演 | 用当前策略跑一次得到的完整轨迹，常与 episode 混用。 |
| **ETS** | Execution Steps（本库 SafeLIBERO 口径） | 执行步数 | 完成任务所花的控制步数，用来发现“靠磨时间换安全”。 |
| **SR** | Success Rate | 成功率 | 成功 episode ÷ 全部 episode；但有的论文用它指 Security Rate，必须先看定义。 |
| **VR** | Violation Rate | 违规率 | 发生约束违反的 episode ÷ 全部 episode，不看任务是否完成。 |
| **SSR** | Safe Success Rate | 安全成功率 | 既完成任务又没违规的 episode ÷ 全部 episode。 |
| **USR** | Unsafe Success Rate | 不安全成功率 | 完成但违规的 episode ÷ 全部 episode；不是“成功中的违规比例”。 |
| **F1** | F1 score | 调和平均分 | 精确率与召回率的调和平均，用于二分类式判定。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **privileged** | privileged information / privileged state | 特权信息／特权状态 | 只有仿真或评测器能拿到的真值状态，用于判分但不给策略。 |
| **closed-loop** | closed-loop execution | 闭环执行 | 策略根据最新观测逐步决策，执行中的误差会影响后续输入。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。
- **rollout**：rollout 数、episode 数、候选轨迹数三者混用。
- **SR**：把 SR（Security Rate）当成功率，或把 /N 的比率当 /SR 的比率。
- **USR**：把 USR 直接说成“成功里的违规比例”。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| SafeStage | 基准 | 分阶段安全评测基准 |

<!-- glossary:end -->
