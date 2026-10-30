# Embodied Safety Benchmark

面向**具身智能安全**的 benchmark 地图：把散落在各篇论文里的评测基准，整理成一张可筛选的总表 + 每个基准一份独立文档。

数据来源是 [Safety in Embodied AI](https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/screened.html) 论文库（curated 594 + audited 157 + screened 1882，去重后 2,633 篇），外加 OpenAlex / arXiv 补充的外部基准。

## 仓库内容

```
data/
  embodied_safety_benchmark_survey.xlsx   主表：192 篇论文 × 14 列（Excel，4 个工作表）
  rows.json                                主表的结构化数据（生成脚本的中间产物）
  raw/                                     论文库原始快照（papers / audited / screened）
benchmarks/
  README.md                                121 个基准的索引，按分类排序
  0__评测方法与协议汇总.md                 38 篇「有评测但不构成独立基准」的论文
  N__<基准名>.md                           每个基准一份文档（共 121 份）
design/
  ESB-2设计方案.md                         基于 121 个基准缺口分析的综合基准设计提案
  coverage-matrix.md                       覆盖矩阵（缺口论证的数据附录）
scripts/                                   可复现的生成脚本
docs/                                      方法与说明
```

## 主表字段

| 列 | 说明 |
|---|---|
| 序号 | — |
| 论文标题（英文原文） | 原始标题，便于检索 |
| 中文题名 / 简称 | 中文对照 |
| 年份 | 论文库标注年份 |
| 来源（期刊 / 会议 / 预印本） | 会议/期刊带正式名，预印本带 arXiv 编号或 DOI |
| **阅读状态** | 下拉：未读 / 在读 / 已读 / 略过；选中「已读」自动变绿 |
| 收录来源 | 本论文库（人工精选 / 作者复核 / 自动筛查）或 库外补充 |
| 论文库分区 | 论文库自己的 taxonomy（layer › subcat） |
| 论文类别 | VLA 安全/鲁棒性/能力 Benchmark、具身安全/鲁棒性/能力 Benchmark、攻防评测框架、评测方法与度量、具身智能体安全 Benchmark、综述 |
| 应用领域 | 自动驾驶、导航、人机协作、多机器人、工业装配、UAV、工控…… |
| 评测对象 | 被测的模型/策略类型 |
| 评测维度与关键指标 | 该文评测设计概括 |
| 内容概要 | 中文 2–4 句，含关键数字 |
| 链接 | arXiv 或出版社 DOI |

## 基准文档的四个问题

每份 `benchmarks/N__*.md` 都回答：

1. **测什么问题** —— 针对具身的哪个环节：认知 / 规划 / 动作控制 / 感知 / 全栈
2. **怎么构建的** —— 任务集、场景、规模、指标、控制了哪些变量
3. **用这个基准测了什么** —— 被测模型清单，逐篇标注「提出」还是「使用」
4. **关键结论与论文提到的改进方向**

外加第 5 节：该基准涉及的全部相关论文（均来自主表，带链接）。

## 统计

- 论文：**192 篇**（论文库 163 + 库外 29），2022–2026
- 基准：**121 个**
  - VLA 安全 11 · VLA 鲁棒性 16 · VLA 能力 31 · 具身智能体安全 46 · 具身安全 17
- 其中 **15 个**被 2 篇及以上论文使用（LIBERO 系、RoboTwin、CALVIN、RoboCasa、SimplerEnv、COLOSSEUM 等），其余 106 个是论文自建、尚待复用
- 另有 **38 篇**论文属于「有评测但未提出可复用基准」（评测协议、度量方法、攻防工作、综述），集中在 `benchmarks/0__评测方法与协议汇总.md`
- 覆盖校验：表中 192 篇论文 **全部**至少出现在一份文档里

## 设计方案：ESB-2

[`design/ESB-2设计方案.md`](design/ESB-2设计方案.md) 是基于本仓库 121 个基准的缺口分析，提出的一套**具身安全综合基准**设计提案。

核心判断（来自 [`design/coverage-matrix.md`](design/coverage-matrix.md) 与 10 篇核心论文全文精读）：

- 121 个基准里**只有 1 个**（EmbodiedGovBench）同时覆盖 4 类以上安全属性，没有任何一个覆盖全部 6 类
- **终态/后果层只有 8 个**基准触及 —— 而伤害往往发生在「做完之后」
- **判分口径不统一**（LTL_f / STL / 人工规则 / LLM 裁判），同一句「安全率 78%」不是同一个量
- **能力与安全不同步**：DESPITE 实测规划能力 0.4→99.3%，安全意识却卡在 38–57%

方案要点：不重造仿真与数据集，而是给已有任务集装一层**可复用的安全测量层** —— (L 层 × A 属性 × S 阶段) 坐标 + 六种配对条件 + 全形式化判分 + 能力/安全双轴报告。

## 复现

```bash
py -3.12 scripts/build_rows.py             # 汇总 → data/rows.json
py -3.12 scripts/build_xlsx.py             # → Excel
py -3.12 scripts/bench_registry.py         # 基准 ↔ 论文映射
py -3.12 scripts/build_benchmark_docs.py   # → benchmarks/*.md
py -3.12 scripts/coverage.py               # 覆盖矩阵 → docs/_coverage.json
py -3.12 scripts/coverage_md.py            # → design/coverage-matrix.md
py -3.12 scripts/fetch_fulltext.py         # 核心论文全文 → docs/_fulltext/
```

需要 `openpyxl`。脚本里的路径默认指向 `D:\study\Embodied`，迁移后改 `BASE` 即可。

## 已知局限

1. **基准归属基于摘要判定**：一篇论文用到的基准若只在实验章节出现、摘要未提，会被漏计。因此「使用者」数量是**下界**。
2. **文档第 1/2/4 节是人工解读**：仅 10 篇核心基准做了全文精读（SafeStage、ManiGuard、ForesightSafety-VLA、SafeVLA-Bench、LIBERO-RIG、LIBERO-CTRL、LIBERO-VPro、HazardArena、DESPITE、RoboHarm），其余依据摘要。
3. **覆盖矩阵是关键词匹配的粗略统计**，用于看相对稀疏度，不是精确计量。
4. **2026 年条目多数只有 arXiv**，是否已被会议接收无法核实。
5. 106 个单篇基准尚无跨论文证据，横向结论有限。
6. **ESB-2 目前只是设计提案**，未实现、未验证；其中的数值目标（如 Kendall τ ≥ 0.7）是待实测的假设，不是结论。

## 许可

内容整理部分（文档、表格）建议 CC BY 4.0；引用的论文版权归原作者。
