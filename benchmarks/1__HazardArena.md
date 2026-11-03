# HazardArena

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：核心贡献是可执行安全／危险语境对照。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：认知 + 动作控制（语义-动作耦合）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://github.com/HazardArena-Team/HazardArena](https://github.com/HazardArena-Team/HazardArena)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真及真机语义安全 |
| 历史关键词标签（未重新统计） | 语义/指令安全、任务能力 |
| 评测维度/指标 | 语义安全；安全/不安全孪生场景下的动作选择正确率 |
| 基础平台线索 | Franka |
| 规模线索 | 51 个任务覆盖食物、财产、化学、隐私、火灾、人身、电气七类风险；复用 2,000 余物体并补充 75 个情境资产。安全／危险任务成对构造。 |
| 执行环境线索 | 仿真及真机语义安全 |
| 全文状态 | 已核查本地全文：`docs/_fulltext/HazardArena.txt` |
| OpenAlex 引用快照 | [0](https://openalex.org/W7154513284)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：当操作技能相似但对象、接触关系和意图不同，模型能否区分该做与不该做？

**评测层级**：仿真及真机语义安全。

## 2. 怎么构建的

**核心场景与条目**：51 个任务覆盖食物、财产、化学、隐私、火灾、人身、电气七类风险；复用 2,000 余物体并补充 75 个情境资产。安全／危险任务成对构造。

**实现与判分**：配对保持场景和操作模板的可比性，同时改变动作参与者、目标关系及指令。分别判断 Attempt、Commit、Success，检查模型是否具备安全对应任务的执行能力。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447) | 2026 | 提出 | 语义安全；安全/不安全孪生场景下的动作选择正确率 | 针对「动作执行正确但语义语境危险」这一系统性漏洞，构造物体、布局与动作要求完全一致、仅语义语境不同的安全/不安全孪生场景。发现仅在安全场景上训练的 VLA 在语义风险下往往无法保持安全，说明 VLA 的动作策略与视觉-语言语义耦合松散。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：拒绝示范训练的 VLA-Adapter 在报告设置中将危险任务成功率从 0.22 降到 0.01，Commit 从 0.44 降到 0.03，安全任务成功率由 0.25 到 0.26；另有真机验证。

**适用边界**：安全／危险配对并非只替换一个文本标签；Attempt、Commit 与实际完成危险行为不可混用。改进只对应文中训练和评测分布。

## 5. 相关论文（均来自本调研表）

- [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447)（2026；提出）

## 6. 证据边界与复核建议

### 6.1 全文核查补录（核心论文）

> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。

**来源文件**：`docs/_fulltext/HazardArena.txt`。

**评测协议**：从 2,000+ 物体资产和 75 个新建语境关键资产中组织 51 个任务，覆盖 food、property、chemical、privacy、fire、personal、electrical 七类风险。任务采用 Pick-Place、Insert、Pour、Camera-Explore 模板，安全/不安全 twin 共享场景、技能模板和动作要求，只改变 actor-target 绑定或 instruction；阶段标记 Attempt、Commit、Success，以区分危险意图/推进与终点成功。

**定量证据**：四个 VLA 在仿真主实验使用跨类别安全/不安全配对；VLA-Adapter 安全微调前 Safe SR/Unsafe SR/Unsafe Commit 为 0.25/0.22/0.44，加拒答数据后为 0.26/0.01/0.03；另一代表性模型由 0.36/0.33/0.61 变为 0.36/0.04/0.06。真机 Franka Panda 使用腕部和场景 RGB 相机，5 个任务族、每族 2 条安全和 1 条不安全指令、每条件 100 trials；平均 Safe SR 由 46.0% 变为 47.4%，Unsafe SR 由 39.6% 降至 0.4%。安全层 Qwen3-VL-32B 的平均 recall/FPR/F1 为 0.77/0.10/0.76。

**全文结论**：仅看终点 SR 会漏掉 Commit 阶段的危险推进；拒答微调几乎消除不安全成功，同时保持安全成功率。类别间存在明显差异，Electrical/Fire/Privacy 的安全层召回可达 1.00，而 Property 为 0.00，说明通用视觉安全层仍有语境盲区。

**适用边界**：仿真和真机使用不同样本规模与接口；安全层指标是分类器指标，不能替代实际策略的拒答和动作结果。

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

安全／危险配对并非只替换一个文本标签；Attempt、Commit 与实际完成危险行为不可混用。改进只对应文中训练和评测分布。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Zixing Chen, Yifeng Gao, Li Wang, et al., ‘HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models,’ arXiv preprint, 2026, arXiv:2604.12447v3. [论文](https://arxiv.org/abs/2604.12447)；[核查正文](https://arxiv.org/html/2604.12447v3)。

**重点核查位置（章节主题）**：3.2 Task Design；3.4 Evaluation；4 Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7154513284)**；观测日期：2026-11-03。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://github.com/HazardArena-Team/HazardArena](https://github.com/HazardArena-Team/HazardArena)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
