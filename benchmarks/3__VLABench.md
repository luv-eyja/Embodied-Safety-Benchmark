# VLABench

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力。
> **分类依据**：长任务和语言推理评测，不因语言接地自动算安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：认知 + 规划（长时程推理）  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`platform_only`；[https://vlabench.github.io/](https://vlabench.github.io/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks |
| 年份 | 2024（所读来源首次 arXiv 提交年） |
| 数据来源 | 库外补充 |
| 论文库分区 | —（库外） |
| 应用领域 | 未标注 |
| 被测对象 | 长时程语言与操作推理 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 大规模任务集；长时程推理与组合泛化 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 60 个原子任务、40 个复合任务，覆盖抓放、开门／抽屉、挂物、工具、按钮、插入、倾倒、旋转和探索。 |
| 执行环境线索 | 长时程语言与操作推理 |
| OpenAlex 引用快照 | [16](https://openalex.org/W4405783861)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 5 个缩写／技术词，并标出 5 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：语言条件操作能否泛化到新物体类别、隐含语义和需要常识／规划的任务？

**评测层级**：长时程语言与操作推理。

## 2. 怎么构建的

**核心场景与条目**：60 个原子任务、40 个复合任务，覆盖抓放、开门／抽屉、挂物、工具、按钮、插入、倾倒、旋转和探索。

**实现与判分**：任务技能库结合运动规划自动生成轨迹，语言扩增描述对象与意图；分别评估 VLA、基础模型工作流和 VLM，未见物体按不同类别而非仅换纹理划分。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning](https://doi.org/10.1109/ICCV51701.2025.01037) | 2025 | 提出 | 大规模任务集；长时程推理与组合泛化 | 大规模语言条件操作基准，强调「长时程推理」与组合泛化：任务需要多步推理与常识知识才能完成，而不只是把一条指令映射为一次抓取。它把评测重心从单步操作成功率推向「推理—规划—执行」的整链能力，是 VLA 能力评测中较有代表性的高难度基准。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：成果是 100 任务、多维语言语义和更严格的对象类别泛化协议；评测显示低层技能获取、目标语义解析和长任务推理需要分开分析。

**适用边界**：VLM 问答正确率、模块化流程成功率和端到端 VLA 成功率属于不同接口。未见类别设置比同类新实例更严格，跨论文比较必须统一。

## 5. 相关论文（均来自本调研表）

- [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning](https://doi.org/10.1109/ICCV51701.2025.01037)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

VLM 问答正确率、模块化流程成功率和端到端 VLA 成功率属于不同接口。未见类别设置比同类新实例更严格，跨论文比较必须统一。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Shiduo Zhang, Zhe Xu, Peiju Liu, et al., ‘VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks,’ arXiv preprint, 2024, arXiv:2412.18194v1. [论文](https://doi.org/10.1109/ICCV51701.2025.01037)；[核查正文](https://arxiv.org/html/2412.18194v1)。

**重点核查位置（章节主题）**：3.1 Task Description；3.2 Benchmark Evaluation；3.3 Data Generation；Experiments。

OpenAlex 被引次数：**[16](https://openalex.org/W4405783861)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://vlabench.github.io/](https://vlabench.github.io/)。地址状态为 `platform_only`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：OpenAlex 引文图中有 **16** 篇引文论文（清单保留被引最高的 16 篇）；arXiv 摘要命中 17 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（仅平台入口，2026-11-04）

**项目入口**：[https://vlabench.github.io/](https://vlabench.github.io/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://vlabench.github.io/) | https://vlabench.github.io/ | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://vlabench.github.io/ 提供 Paper／Arxiv／Dataset／Code／Twitter 入口，作者为复旦团队。

**涉及领域**：语言条件的机器人操作与长时程推理；100 个任务，强调未见物体类别泛化。

**测试目的与构建方法**：任务技能库结合运动规划自动生成轨迹，语言扩增描述对象与意图；分别评估 VLA、基础模型工作流与 VLM，未见物体按不同类别（而非仅换纹理）划分。

**测试缺陷**：VLM 问答正确率、模块化流程成功率与端到端 VLA 成功率属于不同接口，不可混比；未见类别设置更严格，跨论文比较必须统一；仿真资产与真实场景仍有差距。

**与具身智能安全的相关性**：弱到中等：长时程推理失败会放大风险，但基准指标是成功率，不含安全约束。

**用这个 benchmark 测了什么**：评测显示低层技能获取、目标语义解析与长任务推理需要分开分析；16 篇引文含扩散策略综述，TAG 等在其上报告杂乱场景下的鲁棒性改善。

**本轮核查边界**：只读项目页摘要，未下载数据集。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **5 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| Separating Execution and Target Selection in Vision–Language–Action Ev…（2026） | SmolVLA（VLA 模型） 与 π0（已发布 checkpoint） | 审计式评测（同状态可信／空指令、对称停止、保持性检查） | VLABench，使用与模型家族匹配的 native controls | 拆开“执行”和“选目标”两种失败，未给单一分数 |
| GaussMemory: Task-Driven 3D Gaussian Scene Memory for Long-Horizon Man…（2026） | GaussMemory，对照 π0-FAST 与 MemoryVLA | 训练后评测（分 Track 报告） | VLABench Track 1 与 Track 6；另在 LIBERO 上与 MemoryVLA 比 | VLABench Track 1 +5.2%、Track 6 +6.0%（相对 π0-FAST） |
| E0: Enhancing Generalization and Fine-Grained Control in VLA Models（2025） | E0，对照多种强基线 | 训练后评测（14 个环境平均） | LIBERO、VLABench、ManiSkill 与真实 Franka | 14 个环境平均比强基线高 10.7% |
| TAG: Target-Agnostic Guidance for Stable Object-Centric Inference（2026） | TAG（目标无关引导） | 训练后评测（杂乱场景鲁棒性） | LIBERO、LIBERO-Plus、VLABench | 称在杂乱场景下鲁棒性一致提升，并减少近失手与拿错对象 |
| $A_1$: Adaptive Truncated Vision-Language-Action Model（2026） | A1（自适应截断 VLA），在 Franka 与 AgiBot 两套机器人上 | 训练后评测（多基准 + 多机器人） | LIBERO 与 VLABench 等基准，真机为 Franka 与 AgiBot | 摘要只说明评测范围，未给数值 |

**原文片段（摘要）**：

- Separating Execution and Target Selection in Vision–Language…（2026，OpenAlex 引文）：> We evaluate released SmolVLA and π0 policies in VLABench using family-matched native controls
- GaussMemory: Task-Driven 3D Gaussian Scene Memory for Long-H…（2026，arXiv）：> on VLABench, it surpasses π0-FAST by +5.2% (Track 1) and +6.0% (Track 6)
- E0: Enhancing Generalization and Fine-Grained Control in VLA…（2025，arXiv）：> E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average
- TAG: Target-Agnostic Guidance for Stable Object-Centric Infe…（2026，arXiv）：> it consistently improves robustness under clutter and reduces near-miss and wrong-object executions
- $A_1$: Adaptive Truncated Vision-Language-Action Model（2026，OpenAlex 引文）：> LIBERO and VLABench) and multiple robotic systems (Franka and AgiBot)

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 5 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **π0.5** | pi-zero / pi-zero-point-five | π0／π0.5 策略模型 | Physical Intelligence 的通用 VLA 策略家族，本库最常见的对照基线。 |
| **grounding** | visual grounding | 视觉接地 | 把语言里的指称（“那个杯子”）对应到画面中的具体对象。 |
| **Franka** | Franka Emika Panda / Franka Research 3 | Franka 机械臂 | 最常用的七自由度科研机械臂，真机实验的标准硬件。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| VLABench | 基准 | 语言条件长时程操作基准 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| ManiSkill | 基准 | 通用操作技能基准（SAPIEN） |
| LIBERO-Plus | 基准 | LIBERO 的扰动扩展 |

另有 1 个专有名称已在正文首次出现处加括号标注类别（例如 SmolVLA（VLA 模型）），不再重复解释。

<!-- glossary:end -->
