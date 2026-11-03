# 调研汇报

当前交付版本：[具身智能及安全Benchmark调研汇报_2026-11-03_最终版.pptx](具身智能及安全Benchmark调研汇报_2026-11-03_最终版.pptx)。共 19 页，面向正式汇报重新压缩版式，覆盖论文／条目口径、52 个 benchmark 的聚合统计、引用与项目入口、场景分布、nuScenes 设计、LIBERO-Safety／SafeStage／ManiPhysicsBench 安全案例及未来工作建议。52 个 benchmark 的完整索引位于最后两页。

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
