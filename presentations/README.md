# 调研汇报

## 2026-11-04 安全主线版（37 页，独立文件）

[具身智能安全Benchmark调研汇报_2026-11-04_安全主线.pptx](具身智能安全Benchmark调研汇报_2026-11-04_安全主线.pptx) · [逐页文字稿](安全主线_逐页文字稿.md)。安全为核心、能力基准保留五页做底座；正文首次出现的关键术语就地加注。原 35 页版保留不动。

| 页码 | 内容 |
|---|---|
| 1–3 | 封面、一页结论（26 条安全目标 / 23 个任务集 / 5 条真机）、范围与口径 |
| 4–5 | 术语速查两类：模型与评测单位、判据与指标 |
| 6 | 六层总量表（26 条，八行） |
| 7 | 场景覆盖（机械臂与语义决策为主） |
| 8 | 证据载体与真机证据（两张表，含 5 / 13 / 3 / 5 的拆分） |
| 9 | **八类判据的定义与计算方式**（定义、判定窗口、代表条目、误读风险） |
| 10 | 判据 × 证据载体矩阵（● / ○ / —） |
| 11 | 指标四类与两个分母（SBU 与 USR 的分母差异） |
| 12 | 分节页（安全基准） |
| 13–24 | 安全基准十二讲，每页六行：规模、构建、判分、实测、**与相邻条目的差异**、边界；右侧三个关键数字 + 大模型相关度 |
| 25 | 邻接三例：Agent-SafetyBench、EmbodiedGovBench、NAVSIM |
| 26–27 | 26 条安全条目索引（真机证据 / 项目入口 / 引文数） |
| 28 | 八个配对设计 |
| 29 | 三代演进（2024→2026） |
| 30 | 分节页（能力底座） |
| 31–34 | LIBERO、SimplerEnv、其余五个一句话档案、能力轴与安全评测映射（两处空白） |
| 35–37 | 按问题选基准、五个缺口与四条建议、数据来源与边界 |

正文的术语加注规则：与 [术语表](../docs/GLOSSARY.md)（102 个术语）匹配，同一页首次出现处加中文短注；紧邻已有中文解释、或该缩写在本页含义不同于术语表时不加注（LIBERO-Safety 的 SSR、SafeStage 的 ETS、RoboJailBench 的 SR）。

```powershell
node scripts/build_survey_safety_deck.mjs
py -3.12 scripts/pptx_text_dump.py "presentations/具身智能安全Benchmark调研汇报_2026-11-04_安全主线.pptx" "presentations/安全主线_逐页文字稿.md"
```

## 2026-11-04 新稿（35 页）

[具身智能与安全Benchmark调研汇报_2026-11-04_新稿.pptx](具身智能与安全Benchmark调研汇报_2026-11-04_新稿.pptx) · [逐页文字稿](调研汇报_新稿_逐页文字稿.md)。只讲“论文—benchmark”两类成果，数据集／仿真平台／框架不展开：

| 页码 | 内容 |
|---|---|
| 1 | 封面 |
| 2 | 一页结论（62 篇精读 / 52 个任务集 / 26 条带安全目标 / 47 个已确认入口） |
| 3 | 方法与口径 |
| 4–5 | **术语速查两页**：20 个高频词的中文名与一句话解释（整本 PPT 不依赖外部词表） |
| 6–9 | 论文与基准的数量关系、场景覆盖、环节覆盖、能力／鲁棒／安全三轴 |
| 10–17 | 基础能力基准 7 个（LIBERO、CALVIN、SimplerEnv、RoboTwin、RoboCasa365、VLABench、COLOSSEUM）+ 能力侧空白 |
| 18–28 | 安全基准：分层框架 + 七类各详讲一个（执行层、物理后果、语义意图、规划规则、过程阶段、对抗完整性、软件代理）+ 整体判断 |
| 29 | 按问题选基准的对照表 |
| 30–34 | 附录 A–D：关键基准上的模型结果与七类安全结果汇总 |
| 35 | 数据来源与边界 |

**每页是怎么写的**：基准页左侧固定五行——怎么构建、怎么判分、为什么重要、关键结果、适用边界；右侧三个关键数字加一段要点。

**大模型相关度标注**：14 个基准页右上角有圆角标签，取值 高／中，并在备注中写明依据。**高**＝当前主流被测对象是 VLA 或 LLM 级模型（LIBERO、SimplerEnv、RoboTwin、RoboCasa365、VLABench、七类安全基准）；**中**＝原始基线为小型策略、近年才出现 VLA（CALVIN、COLOSSEUM）。没有“低”档：库内 14 个基准都不属于纯经典控制。标注只说明被测对象与 VLA／LLM 的距离，不评价基准质量。构建与判分两行不再是名词堆，而是**先解释机制再说数据**，例如 CALVIN 会写明“play 指不按脚本、边试边做、全程录像”，LIBERO 会写明“BDDL 是把任务初态与目标写成逻辑式的任务定义语言”。

**讲者备注**：第 11–17、20、21–27、31–34 页共 19 页有备注，段落式叙述、每页 5–6 段：先用一句大白话说明“这是什么”，再依次是论文与版本、任务与规模、构建与判分（复用正文的机制解释）、论文结果、论文自述边界、本页三个数字的出处；备注里首次出现的英文缩写会就地加注（如 episode（回合）、BDDL（行为域定义语言）），加注来自 [全库术语表](../docs/GLOSSARY.md)（98 个术语）与 `benchmark_names.json`（110 个专有名称），并对同名异义做了按页跳过（LIBERO-Safety 的 SSR、SafeStage 的 ETS、RoboJailBench 的 SR）。

生成脚本：[build_survey_report_v2.mjs](../scripts/build_survey_report_v2.mjs)（pptxgenjs，无外部 skill 依赖）。文字稿由 [pptx_text_dump.py](../scripts/pptx_text_dump.py) 从导出的 pptx 直接抽取；预览 PNG 在 `.survey_work/report-v2/`（未纳入版本库）。

```powershell
node scripts/build_survey_report_v2.mjs
py -3.12 scripts/pptx_text_dump.py "presentations/具身智能与安全Benchmark调研汇报_2026-11-04_新稿.pptx" "presentations/调研汇报_新稿_逐页文字稿.md"
```

构建脚本自带文本溢出检查（当前 0 处），并用 PowerPoint 打开核对页数、导出全部页面做版面检查。

## 旧版：2026-11-03 最终版

[具身智能及安全Benchmark调研汇报_2026-11-03_最终版.pptx](具身智能及安全Benchmark调研汇报_2026-11-03_最终版.pptx)。共 19 页，面向正式汇报重新压缩版式，覆盖论文／条目口径、52 个 benchmark 的聚合统计、引用与项目入口、场景分布、nuScenes 设计、LIBERO-Safety／SafeStage／ManiPhysicsBench 安全案例及未来工作建议。52 个 benchmark 的完整索引位于最后两页。

生成脚本：[build_final_presentation.mjs](../scripts/build_final_presentation.mjs)。脚本读取 `data/benchmark_survey.json` 与 `data/survey_paper_registry.json`，生成后自动调用 [patch_pptxgenjs_package.py](../scripts/patch_pptxgenjs_package.py) 清理 pptxgenjs 的冗余 slide-master 内容类型声明。

[具身智能及安全 Benchmark 调研汇报：详细修订版](具身智能及安全Benchmark调研汇报_2026-11-03_详细修订版.pptx)共 45 页，基于本仓库 2026-11-03 的调研快照。采用白底正文与表格，补充任务构造、技术实现、评分协议、实验条件及结论依据。[逐页文字稿](调研汇报_详细修订稿.md)与 PPT 的可见文字来自同一内容源。

| 页码 | 内容 |
|---|---|
| 1–7 | 调研目标、术语、已完成工作、样本分类、场景覆盖与来源核查 |
| 8–10 | 评测实现流程、执行接口、任务成功率与安全指标的定义 |
| 11–18 | LIBERO-Safety、SafeStage、损伤判定、语义安全与接口差异 |
| 19–25 | 语言和环境扰动、失败恢复、技能组合、通用能力与自动驾驶 |
| 26–32 | 被引观测、真机证据、统计修正、综合结论、选型与后续工作 |
| 33–45 | 资料入口、62 项重点研究索引、28 篇正文主要参考文献 |

全部文字与 43 张表格均为可编辑对象。引用页保留实际阅读版本，各页讲者备注记录来源、论文结果、解释边界与项目入口。修订版不使用装饰图片。

本次修订特别区分任务成功判据与统计分母：LIBERO-Safety 物理安全轨的 SR 已要求任务完成且全程无安全违规；SafeStage 则分别报告任务成功率、安全成功率、不安全成功率和违规率。SafeStage 的提示对照补充了均值、环境种子间标准差和解释条件。DESPITE 所读版本的危险计划比例在摘要为 28.3%、正文 §1.1 为 28.7%，修订稿保留这一不一致。上述核查补充同时写入可见正文与讲者备注；历史调研数据中的原始记录尚未批量改写。

本次汇报区分本库工作、原论文实验与后续建议：样本数不等于全领域统计，引用数不等于实际采用，找到项目入口不等于已经复现。60 项非重点档案继续保留，未计入重点分类。

## 来源与生成

- 分类与统计：[统一调研数据](../data/benchmark_survey.json)。
- 阅读证据：[正文来源与版本](../data/benchmark_reading_sources.json)、[精读报告](../analysis/benchmark-paper-deep-read.md)。
- 口径与后续工作：[方法](../docs/METHOD.md)、[缺口登记](../analysis/survey-gap-register.md)。
- 内容源：[survey_presentation_content.mjs](../scripts/survey_presentation_content.mjs)。
- 详细版生成脚本：[build_survey_presentation_detailed.mjs](../scripts/build_survey_presentation_detailed.mjs)。

脚本使用 `@oai/artifact-tool` 和当前本地演示文稿工具环境，从本地调研数据生成文件。预览与检查中间文件位于 `.survey_work/presentation-detailed/`。为保留已交付文件，再次运行时通过 `SURVEY_PPTX_NAME` 指定新的输出文件名；Python 与演示文稿工具路径可用 `SURVEY_PYTHON`、`SURVEY_PRESENTATION_SKILL` 按环境调整。需确保 Node 能解析所用包。

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
$env:SURVEY_PPTX_NAME='具身智能及安全Benchmark调研汇报_后续修订版.pptx'
node scripts/build_survey_presentation_detailed.mjs
```

详细修订版已通过文件结构、布局、字体声明和导入检查；全部 45 页进行了渲染检查。以上检查不等同于在 Microsoft PowerPoint 中逐页运行。

早期的 [34 页版本](具身智能及安全Benchmark调研汇报_2026-11-03_完整版.pptx)及其[生成脚本](../scripts/build_survey_presentation.mjs)保留作历史参考，后续阅读以详细修订版为准。数据更新后，应同步核对正文中的数字、实验协议与结论，再生成新版本。
