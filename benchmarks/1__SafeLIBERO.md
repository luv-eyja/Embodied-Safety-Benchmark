# SafeLIBERO

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：VLSA 方法论文中的具名安全任务集，本条只统计该测试集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（碰撞安全）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://vlsa-aegis.github.io](https://vlsa-aegis.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真障碍避碰＋安全控制方法 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 碰撞/安全违规率与指令遵循性能的权衡 |
| 基础平台线索 | LIBERO |
| 规模线索 | 四个 LIBERO 套件各选 4 个任务，每任务设置靠近目标与阻挡路径两级障碍，共 32 场景、每场景 50 次、合计 1,600 episode。 |
| 执行环境线索 | 仿真障碍避碰＋安全控制方法 |
| 来源审计 | [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明构建 SafeLIBERO safety-critical benchmark。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W4417446096)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 14 个缩写／技术词，并标出 2 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：在原有 VLA 策略前增加安全层，能否避免杂乱桌面的障碍碰撞，同时保留任务能力？

**评测层级**：仿真障碍避碰＋安全控制方法。

## 2. 怎么构建的

**核心场景与条目**：四个 LIBERO 套件各选 4 个任务，每任务设置靠近目标与阻挡路径两级障碍，共 32 场景、每场景 50 次、合计 1,600 episode。

**实现与判分**：AEGIS 采用控制障碍函数和二次规划修正名义动作；在平移／完整动作空间分别评价避碰率 CAR、任务成功率 TSR 和执行步数 ETS，并用两项真机任务验证。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891) | 2025 | 提出 | 碰撞/安全违规率与指令遵循性能的权衡 | 提出基于控制屏障函数的即插即用安全约束层 AEGIS，可与现有 VLA 直接组合并给出理论安全保证；为验证效果构建安全关键基准 SafeLIBERO，覆盖多种存在碰撞风险的操作场景，同时度量安全性与原有指令遵循性能。可作为「防御方法自带评测集」的典型样本。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：平移动作设置中，π0.5 的 CAR 18.7% 提升至 AEGIS 的 77.9%，TSR 50.9% 提升至 68.1%；完整动作空间也单独给出结果，不能交叉混比。

**适用边界**：属于受控障碍避碰，不覆盖全部语义风险；CBF 的理论性质依赖状态估计、模型和求解可行性，不能无条件等同于真机安全保证。

## 5. 相关论文（均来自本调研表）

- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

属于受控障碍避碰，不覆盖全部语义风险；CBF 的理论性质依赖状态估计、模型和求解可行性，不能无条件等同于真机安全保证。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Songqiao Hu, Zeyi Liu, Shuang Liu, et al., ‘VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer,’ arXiv preprint, 2025, arXiv:2512.11891v2. [论文](https://arxiv.org/abs/2512.11891)；[核查正文](https://arxiv.org/html/2512.11891v2)。

**重点核查位置（章节主题）**：V-A Experimental Setup；V-B Results；VI Real-world Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W4417446096)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://vlsa-aegis.github.io](https://vlsa-aegis.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 7 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://vlsa-aegis.github.io](https://vlsa-aegis.github.io)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://vlsa-aegis.github.io) | https://vlsa-aegis.github.io | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://vlsa-aegis.github.io 为 VLSA 论文页（Tsinghua 自动化系等），提供 Paper／Benchmark／Code 入口，并给出 VLA 与 VLSA 的功能架构图。

**涉及领域**：VLA 的避碰安全约束；在 LIBERO 生态上叠加 AEGIS 约束层（CBF + QP）。

**测试目的与构建方法**：AEGIS 用控制障碍函数与二次规划修正名义动作；在平移／完整动作空间分别评价避碰率 CAR、任务成功率 TSR 与执行步数 ETS，并用两项真机任务验证。

**测试缺陷**：属于受控障碍避碰，不覆盖语义风险（拿错物体、顺序错误）；CBF 的理论保证依赖状态估计、动力学模型与求解可行性；只修正动作，不改变策略的意图理解。

**与具身智能安全的相关性**：直接测执行层安全：动作是否撞到障碍。它是“外挂安全层”路线的代表，适合与端到端安全训练对比，但只覆盖几何避碰。

**用这个 benchmark 测了什么**：平移动作设置中 π0.5 的 CAR 由 18.7% 升到 AEGIS 的 77.9%，TSR 由 50.9% 升到 68.1%；下游 Route-Guided CBF-QP、SafeDojo、DetAug 等 7 篇在该基准上报告改善。

**本轮核查边界**：只读项目页，未取到基准数据的具体发布状态。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **6 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| VLPSA: Vision-Language-Poisson-Safe Actions for Full-Body Safety of Le…（2026） | VLPSA，基线为 AEGIS 与 π0.5 等安全过滤方法 | 评测（与安全过滤基线对比） | SafeLIBERO 碰撞避免率 CAR | 把碰撞避免率从 π0.5 基线的 23.1% 提升到 91.2%，并超过其任务成功率；另在 Franka FR3 的杂乱动态场景做了真机部署 |
| SafeDojo: Safe Reinforcement Learning for VLA via Interactive World Mo…（2026） | SafeDojo（安全 RL 微调，拉格朗日约束 GRPO） | 训练后评测（Level I 微调，Level II 零样本） | SafeLIBERO Level I 与零样本 Level II，指标为 average safe-success rate | Level I 比最强基线高 8.25 个百分点；Level II 零样本与最强 model-free 基线相当 |
| DetAug: Obstacle-Blind Trajectory Augmentation for Zero-shot Obstacle…（2026） | DetAug（障碍盲数据增广 + 推理期标签采样） | 评测（零样本，不训练于基准） | SafeLIBERO collision-free success rate | 比次优方法高 20pp 以上；在标签空间上选择比同一策略的引导方式高 26pp |
| Neuro-Symbolic Safety Guidance for Vision-Language-Action Models（2026） | 神经符号安全引导（在单步安全方法上改进） | 评测（与单步安全方法对比） | SafeLIBERO，碰撞避免率与任务成功率，细分长时程任务 | 82.8% 碰撞避免、81.6% 任务成功，比单步方法分别高 6.3% 与 19.8%，长时程增益最大 |
| WBAG: A Whole-Body and Attached-Geometry Safety Framework for VLA（2026） | WBAG（整身与附着几何安全框架） | 评测（场景级安全评估器） | SafeLIBERO（LIBERO 加障碍的变体），安全与安全任务成功率 | 在所比方法中安全与安全任务成功率均最好；摘要未给具体数值 |
| Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models（2026） | CBF-QP 修复 + 路线引导项，对照 AEGIS | 评测（在 AEGIS 基础上改进） | SafeLIBERO，碰撞避免、任务成功与 SafeSuccess 三项 | 三项均优于 AEGIS；摘要未给具体数值 |

**原文片段（摘要）**：

- VLPSA: Vision-Language-Poisson-Safe Actions for Full-Body Sa…（2026，arXiv）：> increasing collision avoidance from 23.1% for the base π0.5 policy to 91.2% while surpassing its task success rate
- SafeDojo: Safe Reinforcement Learning for VLA via Interactiv…（2026，arXiv）：> On SafeLIBERO Level I, SafeDojo improves average safe-success rate by 8.25 percentage points
- DetAug: Obstacle-Blind Trajectory Augmentation for Zero-shot…（2026，arXiv）：> achieves a collision-free success rate more than 20pp above the next best method
- Neuro-Symbolic Safety Guidance for Vision-Language-Action Mo…（2026，arXiv）：> our method achieves 82.8% collision avoidance and 81.6% task success
- WBAG: A Whole-Body and Attached-Geometry Safety Framework fo…（2026，arXiv）：> WBAG achieves the best overall safety and safe task success among the evaluated methods
- Route-Guided CBF-QP Repair for Safe Vision-Language-Action M…（2026，arXiv）：> On SafeLIBERO, our method improves collision avoidance, task success, and SafeSuccess compared with AEGIS

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 14 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **CAR** | Collision Avoidance Rate | 避碰率 | 没有发生碰撞的 episode ÷ 全部 episode。 |
| **TSR** | Task Success Rate | 任务成功率 | 把任务做完的比例，与 CAR 一起用时表示“做完且没撞”。 |
| **ETS** | Execution Steps（本库 SafeLIBERO 口径） | 执行步数 | 完成任务所花的控制步数，用来发现“靠磨时间换安全”。 |
| **VLSA** | Vision-Language-Action with plug-and-play Safety constraint layer | 带安全约束层的 VLA | SafeLIBERO 论文提出的方法名：在 VLA 外面挂一个可插拔安全层。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **AEGIS** | AEGIS safety layer（SafeLIBERO 论文提出） | AEGIS 安全约束层 | 用控制障碍函数＋二次规划修正动作的安全层，SafeLIBERO 的基准方法。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **CBF** | Control Barrier Function | 控制障碍函数 | 用数学约束保证系统不进入危险集合的安全层方法。 |
| **QP** | Quadratic Programming | 二次规划 | 求解带约束的二次目标优化，常用来在线修正动作。 |
| **RL** | Reinforcement Learning | 强化学习 | 用奖励信号优化策略，区别于用示范做监督学习。 |
| **GRPO** | Group Relative Policy Optimization | 组相对策略优化 | 一种不需要价值网络的强化学习算法，按组内相对优势更新策略。 |
| **zero-shot** | zero-shot evaluation | 零样本评测 | 不针对该基准做任何训练或微调，直接拿现成模型跑。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| SafeLIBERO | 基准 | LIBERO 的避碰安全扩展 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |

<!-- glossary:end -->
