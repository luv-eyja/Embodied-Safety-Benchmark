# LIBERO-Para

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：语言变化评测，不因涉及指令就归入语义安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：指令复述敏感性  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 0、使用 1；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)；[https://cau-hai-lab.github.io/LIBERO-Para/](https://cau-hai-lab.github.io/LIBERO-Para/)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 原表保留使用论文；本轮另读外部原始来源，见第 7 节 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真语言改写鲁棒性 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 固定环境与策略，仅替换留出的测试指令；PRIDE 用关键词和结构差异对成功按改写难度加权，另以 DTW 相对成功轨迹的距离分析失败类型。 |
| 基础平台线索 | LIBERO |
| 规模线索 | 在初始状态相同、只能靠指令区分任务的 LIBERO-Goal 上生成 4,092 条改写；动作轴覆盖词汇、句法、语用，物体轴覆盖同义替换和描述增补，另测组合。 |
| 执行环境线索 | 仿真语言改写鲁棒性 |
| 来源审计 | [LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301)；external_original_paper |
| 来源核验依据 | 2026-11-03 沿 IndustrialVLA-Bench 参考文献 [15] 找到独立提出论文；后者只是使用论文。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7147537669)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 8 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：任务语义不变，仅改写动作表达或物体名称，VLA 是否仍执行同一个任务？

**评测层级**：仿真语言改写鲁棒性。

## 2. 怎么构建的

**核心场景与条目**：在初始状态相同、只能靠指令区分任务的 LIBERO-Goal 上生成 4,092 条改写；动作轴覆盖词汇、句法、语用，物体轴覆盖同义替换和描述增补，另测组合。

**实现与判分**：固定环境与策略，仅替换留出的测试指令；PRIDE 用关键词和结构差异对成功按改写难度加权，另以 DTW 相对成功轨迹的距离分析失败类型。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562) | 2026 | 使用 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 | VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。该基准在统一上报口径下对 6 个已发布系统分轴评测：LIBERO 上的干净能力、LIBERO-Plus 上的非语言鲁棒性、LIBERO-Para 上的指令敏感度以及实测执行代价，并聚合三个不同随机种子的完整评测。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：7 种模型配置在改写下下降约 22–52 个百分点；失败中 79.5–95.5% 被归为远离参考轨迹的规划层偏离。独立提出论文为 arXiv:2603.28301，IndustrialVLA-Bench 只是后续使用者。

**适用边界**：DTW 归类是轨迹层代理指标，并非直接观察到内部规划过程；结论主要来自 LIBERO-Goal。PRIDE 的权重影响诊断，不宜取代原始成功率。

## 5. 相关论文（均来自本调研表）

- [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)（2026；使用）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

DTW 归类是轨迹层代理指标，并非直接观察到内部规划过程；结论主要来自 LIBERO-Goal。PRIDE 的权重影响诊断，不宜取代原始成功率。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Chanyoung Kim, Minwoo Kim, Minseok Kang, et al., ‘LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models,’ arXiv preprint, 2026, arXiv:2603.28301v3. [论文](https://arxiv.org/abs/2603.28301)；[核查正文](https://arxiv.org/html/2603.28301v3)。 arXiv 摘要页及作者官方仓库声明 EMNLP（会议／期刊） 2026 Main（Oral），2026-11-03 核查。

**重点核查位置（章节主题）**：3 LIBERO-Para；4.3 PRIDE Score；5.1 Setup；6.2 Finding 2；6.3 Finding 3。

OpenAlex 被引次数：**[0](https://openalex.org/W7147537669)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)；[https://cau-hai-lab.github.io/LIBERO-Para/](https://cau-hai-lab.github.io/LIBERO-Para/)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要命中 3 篇。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)；[https://cau-hai-lab.github.io/LIBERO-Para/](https://cau-hai-lab.github.io/LIBERO-Para/)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/cau-hai-lab/LIBERO-Para) | https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/HEAD/README.md | stars 50，license MIT（开源许可证），最后推送 2026-09-25，保留文本 4200 字符（截断） |
| [page](https://cau-hai-lab.github.io/LIBERO-Para/) | https://cau-hai-lab.github.io/LIBERO-Para/ | 保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/cau-hai-lab/LIBERO-Para（50 stars，MIT，2026-09-25 推送）与项目页并存，项目页给 Paper／arXiv／Code(Dataset)／HuggingFace 入口，并说明改写分类法（what to act on / how to act）。

**涉及领域**：指令改写的鲁棒性诊断；在 LIBERO-Goal 等固定环境中只替换测试指令措辞。

**测试目的与构建方法**：固定环境与策略，仅替换留出的改写指令；PRIDE 指标按改写难度（关键词／结构差异）加权，另用 DTW 相对成功轨迹的距离归类失败类型。

**测试缺陷**：DTW 归类是轨迹层代理指标，不等于观察到内部规划；结论主要来自 LIBERO-Goal；PRIDE 的权重会影响诊断，不宜取代原始成功率；只测语言侧扰动，不测执行侧。

**与具身智能安全的相关性**：中等：措辞变化导致的行为偏移是“同一意图不同表述”下的失效来源，可解释部分语义安全失败，但基准不含风险约束。

**用这个 benchmark 测了什么**：7 种模型配置在改写下下降约 22–52 个百分点，失败中 79.5–95.5% 被归为远离参考轨迹的规划层偏离；EMNLP 2026 Main（Oral）；下游 WAVE-0 等报告在 LIBERO-Para 上的分数。

**本轮核查边界**：只读 README 与项目页首页，未下载数据集。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮判读 **3 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，可据此复核判读是否过度。

| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |
|---|---|---|---|---|
| WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Fusion（2026） | WAVE-0（VLA + 世界动作模型融合） | 训练后评测（多基准并列） | LIBERO-Para 成功率，另报 LIBERO／LIBERO-Plus／LIBERO-Pro／RoboTwin 2.0 | LIBERO-Para 75.0%；LIBERO 98.7%、LIBERO-Plus 88.0%、LIBERO-Pro 61.4%、RoboTwin 2.0 91.47% |
| Grounded Semantic Re-Binding for Robust Instruction Generalization（2026） | GSR（语义重绑定方法） | 训练后评测（指令泛化专项） | LIBERO-Para 的成功率提升幅度 | 成功率最高提升 44.6 个百分点 |
| IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot P…（2026） | 六个开放 VLA／WAM 系统（固定 checkpoint 与推理配置） | 评测（把该基准当作“指令敏感度”一根轴复用） | LIBERO-Para 4,092 个配置各跑一次，与 LIBERO（干净能力）、LIBERO-Plus（非语言鲁棒性）并列 | 语言轴的分数跨度 31.08 个百分点，远大于干净轴的 1.58 个百分点 |

**原文片段（摘要）**：

- WAVE-0: Bridging VLA Policies and WAMs with Lightweight Late…（2026，arXiv）：> along with 88.0%, 61.4%, and 75.0% on LIBERO-Plus, LIBERO-Pro, and LIBERO-Para
- Grounded Semantic Re-Binding for Robust Instruction Generali…（2026，arXiv）：> On the LIBERO-Para benchmark, GSR improves success rates by up to 44.6 percent
- IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Op…（2026，arXiv）：> It separately evaluates clean capability on LIBERO, non-language robustness on LIBERO-Plus, instruction sensitivity on LIBERO-Para

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 4 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **PRIDE** | PRIDE（LIBERO-Para 论文提出的诊断指标） | 改写难度加权成功率 | 按改写难度给成功加权的指标：越难的改写，成功分越高。 |
| **DTW** | Dynamic Time Warping | 动态时间规整距离 | 允许时间轴伸缩的轨迹距离，用来比较两条轨迹形状有多像。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **WAM** | World-Action Model | 世界—动作模型 | 同时预测未来画面与动作的模型，用于规划或作为策略主干。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| LIBERO-Para | 基准 | LIBERO 的指令改写扩展 |
| IndustrialVLA-Bench | 基准 | 多基准评测与复现证据框架 |
| LIBERO-Plus | 基准 | LIBERO 的扰动扩展 |
| LIBERO-Pro | 基准 | LIBERO 的难例扩展 |
| RoboTwin | 基准 | 双臂操作数据生成与评测 |

另有 2 个专有名称已在正文首次出现处加括号标注类别（例如 EMNLP（会议／期刊）、MIT（开源许可证）），不再重复解释。

<!-- glossary:end -->
