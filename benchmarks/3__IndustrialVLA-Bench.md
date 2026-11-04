# IndustrialVLA-Bench

<!-- survey-classification:start -->
> **统一调研分类**：评测框架；直接具身评测；目标：能力、鲁棒性。
> **分类依据**：复用 LIBERO、Plus、Para，主要提供统一比较与复现证据框架。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：VLA/WAM 多轴可追溯评测  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/xiaoqi-7/IndustrialVLA-Bench](https://github.com/xiaoqi-7/IndustrialVLA-Bench)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 多基准评测与复现证据框架 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、任务能力 |
| 评测维度/指标 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 |
| 基础平台线索 | LIBERO |
| 规模线索 | 评测六个 VLA／WAM 系统：LIBERO 四套件、LIBERO-Plus 六类非语言扰动、LIBERO-Para 指令改写，并记录显存、延迟及复现负担。 |
| 执行环境线索 | 多基准评测与复现证据框架 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214113903)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 4 个缩写／技术词，并标出 4 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：干净任务分数已经接近时，如何结合鲁棒性、语言敏感性和运行成本区分已发布策略？

**评测层级**：多基准评测与复现证据框架。

## 2. 怎么构建的

**核心场景与条目**：评测六个 VLA／WAM 系统：LIBERO 四套件、LIBERO-Plus 六类非语言扰动、LIBERO-Para 指令改写，并记录显存、延迟及复现负担。

**实现与判分**：固定 checkpoint 和推理配置，完整运行三个种子；标准 LIBERO 每种子 2,000 episode，Plus 10,030 配置、Para 4,092 配置各一次。按协议忠实度标记结果，均值和标准差不混为置信区间。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562) | 2026 | 提出 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 | VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。该基准在统一上报口径下对 6 个已发布系统分轴评测：LIBERO 上的干净能力、LIBERO-Plus 上的非语言鲁棒性、LIBERO-Para 上的指令敏感度以及实测执行代价，并聚合三个不同随机种子的完整评测。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：六个系统的干净分数跨度只有 1.58 个百分点，鲁棒性与语言分数跨度分别为 14.62 和 31.08 个百分点。成果是多轴报告、checkpoint 与复现证据记录。

**适用边界**：它复用 LIBERO-Para，并非后者的提出论文。部分行只是近似复现或待核验，不能与严格协议行无差别排名；也没有证明真实工业部署安全。

## 5. 相关论文（均来自本调研表）

- [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

它复用 LIBERO-Para，并非后者的提出论文。部分行只是近似复现或待核验，不能与严格协议行无差别排名；也没有证明真实工业部署安全。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Yiqi Wang, Zhifeng Rao, Jiaqi Zhang, et al., ‘IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models,’ arXiv preprint, 2026, arXiv:2609.25562v2. [论文](https://arxiv.org/abs/2609.25562)；[核查正文](https://arxiv.org/html/2609.25562v2)。

**重点核查位置（章节主题）**：3.3 Benchmark Scope；4.4 Language Sensitivity；Appendix B Protocol。

OpenAlex 被引次数：**[0](https://openalex.org/W7214113903)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/xiaoqi-7/IndustrialVLA-Bench](https://github.com/xiaoqi-7/IndustrialVLA-Bench)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://github.com/xiaoqi-7/IndustrialVLA-Bench](https://github.com/xiaoqi-7/IndustrialVLA-Bench)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [repo](https://github.com/xiaoqi-7/IndustrialVLA-Bench) | https://raw.githubusercontent.com/xiaoqi-7/IndustrialVLA-Bench/HEAD/README.md | stars 5，最后推送 2026-11-01，保留文本 4200 字符（截断） |

**项目页显示**：GitHub https://github.com/xiaoqi-7/IndustrialVLA-Bench（5 stars，2026-11-01 推送）README 给出 arXiv、逐种子结果与延迟测试的复现档案发布记录。

**涉及领域**：工业场景下的开放机器人策略模型评测；复用 LIBERO、LIBERO-Plus、LIBERO-Para 的多轴协议。

**测试目的与构建方法**：固定 checkpoint 与推理配置，完整跑三个种子：LIBERO 每种子 2,000 episode，Plus 10,030 配置、Para 4,092 配置各一次；按“协议忠实度”标记结果，均值与标准差明确不混为置信区间。

**测试缺陷**：它复用 LIBERO-Para 而非其提出者；部分行只是近似复现或待核验，不能与严格协议行无差别排名；全部仿真，未证明真实工业部署安全。

**与具身智能安全的相关性**：较弱偏间接：测的是干净／鲁棒／语言三轴的性能与可复现性，工业安全要靠额外风险协议；它的价值是把“评测可信度”本身做成可检查项。

**用这个 benchmark 测了什么**：六个系统的干净分数跨度仅 1.58 个百分点，而鲁棒性与语言分数跨度分别为 14.62 与 31.08 个百分点——说明只看干净分数会掩盖差异。

**本轮核查边界**：只读 README 的 News 与定位说明，未下载复现档案。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

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
| **episode** | episode | 回合 | 一次从重置到终止（成功／失败／超时）的完整交互，是最常见的分母。 |
| **VLA** | Vision-Language-Action model | 视觉—语言—动作模型 | 以图像＋语言为输入、直接输出机器人动作的模型，本库的主要被测对象。 |
| **WAM** | World-Action Model | 世界—动作模型 | 同时预测未来画面与动作的模型，用于规划或作为策略主干。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |

**本文最容易读错的地方**：
- **episode**：把“任务数”“配置数”当 episode 分母，会让成功率虚高。

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| IndustrialVLA-Bench | 基准 | 多基准评测与复现证据框架 |
| LIBERO | 基准 | 本库最常用的终身学习操作基准套件 |
| LIBERO-Plus | 基准 | LIBERO 的扰动扩展 |
| LIBERO-Para | 基准 | LIBERO 的指令改写扩展 |

<!-- glossary:end -->
