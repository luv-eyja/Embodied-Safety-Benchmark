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
| OpenAlex 引用快照 | 未核验（查询失败／未匹配）；2026-11-03 |

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
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Chanyoung Kim, Minwoo Kim, Minseok Kang, et al., ‘LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models,’ arXiv preprint, 2026, arXiv:2603.28301v3. [论文](https://arxiv.org/abs/2603.28301)；[核查正文](https://arxiv.org/html/2603.28301v3)。 arXiv 摘要页及作者官方仓库声明 EMNLP 2026 Main（Oral），2026-11-03 核查。

**重点核查位置（章节主题）**：3 LIBERO-Para；4.3 PRIDE Score；5.1 Setup；6.2 Finding 2；6.3 Finding 3。

OpenAlex 被引次数：**未核验（查询失败／未匹配）**；观测日期：2026-11-03。本次未取得可核验计数，不按 0 处理。

**项目与成果入口**：[https://github.com/cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)；[https://cau-hai-lab.github.io/LIBERO-Para/](https://cau-hai-lab.github.io/LIBERO-Para/)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 1 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
