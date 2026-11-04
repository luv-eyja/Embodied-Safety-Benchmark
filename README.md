# 具身智能与安全 Benchmark 调研

本仓库整理具身智能及其安全评测研究：各项工作关注什么问题、怎样构造任务、采用什么技术与评分协议、实验发现是什么，以及证据和资源是否足以支持后续研究。当前重点是文献调研与横向比较。

## 从哪里开始

| 阅读目的 | 入口 |
|---|---|
| 调研汇报与结论 | [45 页详细修订版 PPT](presentations/具身智能及安全Benchmark调研汇报_2026-11-03_详细修订版.pptx) · [逐页文字稿](presentations/调研汇报_详细修订稿.md) · [汇报说明](presentations/README.md) |
| 筛选与比较 | [统一调研工作簿](data/benchmark_survey.xlsx) · [比较矩阵](analysis/benchmark-comparison.md) |
| 问题、场景、实现与论文结果 | [62 项正文重点章节精读](analysis/benchmark-paper-deep-read.md) · [条目索引](benchmarks/README.md) |
| 谁在引用、引了哪些论文 | [引文与摘要命中清单](analysis/benchmark-citing-papers.md) |
| 样本结构与结论边界 | [共同特征](analysis/基准共同特征.md) · [场景与目标分布](design/coverage-matrix.md) |
| 来源与项目入口 | [来源审计](analysis/benchmark-source-audit.md) · [项目地址审计](analysis/benchmark-project-audit.md) |
| 项目源逐条核查（领域／目的与构建／缺陷／安全相关性／测了什么） | 每个条目文档第 8 节 · [结构化数据](data/benchmark_project_reviews.json) |
| 谁怎么用（被测模型／用法／评测范围／报告数值） | 每个条目文档第 9 节 · [结构化数据](data/benchmark_usage_records.json) |
| 后续工作 | [覆盖与证据缺口](analysis/survey-gap-register.md) |
| 统计为何改变 | [统计修正记录](analysis/statistical-corrections.md) · [方法说明](docs/METHOD.md) |
| 缩写看不懂 | [全库术语表](docs/GLOSSARY.md)（97 个词 + 110 个专有名称的类别标注）· 每条文档第 10 节 |

## 当前范围（2026-11-03）

登记 **122 个调研条目**，其中 **62 个重点条目已依据正文笔记分类**；未确认项目入口的 **60 个条目**保留在 `benchmarks/no-project/`，本轮未扩读，不计入已分类样本。

| 主要成果类型（互斥） | 数量 |
|---|---:|
| 评测任务集 | 52 |
| 训练数据集 | 3 |
| 仿真平台 | 2 |
| 评测框架 | 4 |
| 方法论文 | 1 |
| 已分类合计 | 62 |

52 个任务集包含 4 个软件代理邻接任务集，**直接具身评测任务集为 48 个**。另一个软件代理条目属于框架。多功能工作按本次所读来源的主要贡献归类，逐条保留依据。

能力、鲁棒性、安全是可多选目标，分别涉及 49、24、26 个已分类条目；这些数字包含研究底座和邻接研究，不能相加，也不是具身安全任务集数量。执行层级另作标记：图像问答、符号规划、离线轨迹、交互仿真与真机执行的分数不直接平均。

62 项有正文重点章节笔记；62 项均有带日期的 OpenAlex 被引观测（2026-11-04 补齐此前因限流留空的 LIBERO-Para、RoboCasa、CARLA）。项目入口为 47 项已确认、12 项仅平台入口、3 项候选；这不表示所有项目均有完整代码、数据与许可证。独立采用和实际运行复现尚未核查。

被引数之外，另汇总了**引用这些 benchmark 的论文清单**：62 条中 20 条在 OpenAlex 引文图里有可列出的引文论文，7 条暂无引文但 arXiv 摘要里出现该名称（附命中上下文），5 条名称歧义、命中不能当计数，30 条两种口径都没查到。清单与方法见[引文与摘要命中清单](analysis/benchmark-citing-papers.md)；引文图、“摘要提到”和“真的跑过”是三种不同强度的证据，不能互相替代。

## 数据组织

- [benchmark_survey_annotations.json](data/benchmark_survey_annotations.json)：人工分类、指标含义与分母、对照协议和统计边界的编辑源。
- [benchmark_survey.json](data/benchmark_survey.json)：合并分类、论文、引用、资源与证据状态的统一数据，保留 122 条及未知值。
- [survey_paper_registry.json](data/survey_paper_registry.json)：199 个书目记录，连接原始 193 条与补入的 6 篇已读来源，按确切题名、arXiv ID 和已知 DOI 别名连接。
- [benchmark_paper_reviews.json](data/benchmark_paper_reviews.json) 与 [benchmark_reading_sources.json](data/benchmark_reading_sources.json)：正文笔记、章节位置、作者、阅读版本和正文哈希。
- [benchmark_citation_snapshot.json](data/benchmark_citation_snapshot.json)：引用观测与失败状态；不把未查到当作零，不把被引次数当作采用量。
- [benchmark_citing_works.json](data/benchmark_citing_works.json)：每条 benchmark 的引文清单（OpenAlex `cites`）与 arXiv 摘要命中（含命中片段、检索式与歧义标注）；三种口径分开记录，不相加。
- [benchmark_project_reviews.json](data/benchmark_project_reviews.json)：62 条的项目源核查结论（涉及领域、测试目的与构建方法、测试缺陷、安全相关性、被测对象与结论）及抓取到的仓库元数据。
- [benchmark_usage_records.json](data/benchmark_usage_records.json)：逐篇判读的使用明细——被测模型、用法（评测／微调／预训练／扩展基准／审计）、评测范围与指标、报告结果，附摘要原文片段；[benchmark_usage_evidence.json](data/benchmark_usage_evidence.json) 保留抽取到的原始句子。
- [benchmark_names.json](data/benchmark_names.json)：110 个专有名称的类别（LLM／VLM／VLA 模型、机构、许可证、会议、基准、数据集、仿真平台、机器人本体），其中 40 个会在正文首次出现处加括号标注，例如 GPT-4o（LLM 模型）。
- [benchmark_glossary.json](data/benchmark_glossary.json)：97 个术语的英文全称、中文名、一句话解释、详细解释与常见误读；[docs/GLOSSARY.md](docs/GLOSSARY.md) 由它渲染，各文档第 10 节按同一份词表列出本文出现的词，避免同一缩写两种解释。
- [rows.json](data/rows.json) 与 [原始论文工作簿](data/embodied_safety_benchmark_survey.xlsx)：193 条初始筛选记录的历史快照。当前分类比较使用新增工作簿。

初始候选来自 [Safety in Embodied AI](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/screened.html) 的本地快照及补充检索。它是有目的的文献样本，不是穷尽检索结果。[近期候选](analysis/recent-embodied-benchmark-papers.md)仍单列，未经核验不直接计入正式统计。

## 本地更新与校验

以下 Python 脚本只读取本仓库，使用标准库，可离线运行：

```powershell
python scripts/build_benchmark_survey.py
python scripts/build_benchmark_glossary.py
python scripts/validate_benchmark_outputs.py
python scripts/validate_survey_outputs.py
```

修改正文笔记后，先运行 `python scripts/build_benchmark_paper_report.py`，它也会同步统一分类。工作簿使用 `node scripts/build_survey_workbook.mjs` 生成，依赖 `@oai/artifact-tool`；需先在脚本可解析的位置提供该依赖。随后再次运行两项校验。工作簿清单保存输入哈希，数据变化后旧工作簿会被识别为过期。

引用数据需要联网，单独刷新（`py -3.12`；脚本会重试 HTTP 429）：

```powershell
py -3.12 scripts/update_benchmark_citations.py       # OpenAlex：62 条被引数
py -3.12 scripts/collect_benchmark_citing_works.py   # OpenAlex 引文清单 + arXiv 摘要命中
py -3.12 scripts/collect_benchmark_citing_works.py --arxiv-only  # 只重跑 arXiv 渠道
py -3.12 scripts/build_benchmark_citing_report.py    # 从 JSON 渲染引文报告，不联网
py -3.12 scripts/collect_usage_evidence.py           # 抓引文摘要并抽取“提到该基准”的句子
py -3.12 scripts/fetch_project_pages.py              # 抓项目页／README（缓存到 docs/_project_cache.json）
```

顺序是：先刷引用快照，再收集引文清单，然后 `build_benchmark_paper_report.py`（把计数与清单写回 62 个文档和卡片），最后生成工作簿。观测日期随快照保存，跨日期比较须带上日期。

`common_patterns.py`、`coverage.py`、`coverage_md.py` 现为兼容入口，统一使用人工编码生成分析。原 `build_rows.py`、`bench_registry.py`、`build_xlsx.py` 等保留为历史工具，部分依赖父目录旧中间文件，不作为日常更新入口。

## 后续工作与边界

下一阶段优先补齐代表性、代码／数据／许可证／评测器可用性和独立采用证据，再形成按研究问题选基准的综述。具体验收要求见[缺口登记](analysis/survey-gap-register.md)。未知不自动算成“不具备”；样本统计不用于证明整个领域没有某项工作。

[ESB-2](design/ESB-2设计方案.md)保留为可选研究设想，尚未实现或验证。旧关键词统计和唯一性论证已撤回；新基准开发不属于完成本轮文献调研的必要条件。

## 许可

内容整理部分建议采用 CC BY 4.0；外部论文、代码和数据的权利归各自作者。具体项目许可证尚待逐项核验。
