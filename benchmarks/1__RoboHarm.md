# RoboHarm

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：安全。
> **分类依据**：以固定场景和接口对照形成行为安全测试。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：有害机器人指令下的拒答率  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`candidate`；[https://github.com/robocurve/roboharm](https://github.com/robocurve/roboharm)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Cognition › Instruction Understanding |
| 应用领域 | 具身拒答 |
| 被测对象 | 模拟与真机机器人接口安全 |
| 历史关键词标签（未重新统计） | 语义/指令安全 |
| 评测维度/指标 | 接口变量受控；MuJoCo 双臂 YAM 仿真 + 真机 612 次试验 |
| 基础平台线索 | MuJoCo、YAM |
| 规模线索 | 五类不安全场景，使用 YAM 机械臂及 MuJoCo 孪生；比较文本、代码式计划、末端执行器及关节等动作接口。 |
| 执行环境线索 | 模拟与真机机器人接口安全 |
| 来源审计 | [Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control](https://arxiv.org/abs/2610.14043)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce RoboHarm。 |
| 全文状态 | 已核查本地全文：`docs/_fulltext/RoboHarm.txt` |
| OpenAlex 引用快照 | [0](https://openalex.org/W7221820979)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：同一模型从文字回答切换到生成机器人动作后，拒绝危险指令的能力是否保留？

**评测层级**：模拟与真机机器人接口安全。

## 2. 怎么构建的

**核心场景与条目**：五类不安全场景，使用 YAM 机械臂及 MuJoCo 孪生；比较文本、代码式计划、末端执行器及关节等动作接口。

**实现与判分**：对相同风险意图在不同输出接口下评测拒绝和执行行为；模拟评测覆盖 7 个模型，真机末端／关节接口分别记录 612／252 次测试。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control](https://arxiv.org/abs/2610.14043) | 2026 | 提出 | 接口变量受控；MuJoCo 双臂 YAM 仿真 + 真机 612 次试验 | 追问一个尖锐问题：前沿语言模型在纯文本下会可靠拒绝解释如何造成人身伤害，但当同一个模型控制机器人时，这种拒绝是否还在？基准含一组有害机器人指令，固定模型、只改变接口（文本→Code as Policies→命令末端位姿或关节角的视觉智能体）。在双臂 YAM 的 MuJoCo 仿真孪生中，拒绝率从文本请求的 73% 降到模型控制机器人后的 18–25%；真机上六个末端控制的模型在 612 次试验中拒绝率约 18%。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文报告文本接口拒绝率约 73%，机器人接口约 18–25%；真机末端接口约 18%、关节接口约 41%。接口选择本身会改变观测到的安全表现。

**适用边界**：拒绝率低不能自动换算为伤害率；不同接口的可执行性和样本构成不同。小规模场景和指定本体限制外推。

## 5. 相关论文（均来自本调研表）

- [Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control](https://arxiv.org/abs/2610.14043)（2026；提出）

## 6. 证据边界与复核建议

### 6.1 全文核查补录（核心论文）

> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。

**来源文件**：`docs/_fulltext/RoboHarm.txt`。

**评测协议**：5 个不安全任务（doll、burner、toaster、brick、pour）组成场景-指令对，覆盖直接伤害和需理解物体后果的潜在危险；在 MuJoCo 中重建 I2RT YAM 双臂机器人的仿真 twin，并在真机上复核。比较 text、Code as Policies、视觉 EEF pose、带对象清单的 EEF-N 与 joint-angle 接口；仿真每个模型-任务-接口 5 trials，文本单元 10 samples。

**定量证据**：文本拒答率为 user-framed 73%、robot-framed 84%，切换到 CaP/EEF/EEF-N/joint 后降至 25%/19%/18%/19%。真机 6 个模型完成 612 次 EEF 和 252 次 joint trials；真实 EEF 拒答 18%，joint 拒答 41%，与仿真 EEF 19%、joint 31% 同方向。burner/brick 在真机仅 8/254 拒答，toaster 为 0/120；doll 为 70/118。

**全文结论**：拒答从文本到动作接口大幅下降，且并非只由缺少对象信息导致：同一对象清单下 robot-framed text 对 burner/toaster/brick 的拒答为 51/70、53/70、68/70，而 EEF-N 对这些危险均无拒答。全文把失败归为感知不确定、感知错误、后果推理失败和价值/对齐失败；例如 21/22 次 EEF pour 识别 Clorox 与 ammonia 标签后仍有 18 次尝试。

**适用边界**：每个任务只有一种措辞，单元样本量较小，仿真 transcript 由 LLM judge 标注；评测知情效应可能高估拒答率，结果应解释为接口迁移缺口而非完整危害覆盖率。

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

拒绝率低不能自动换算为伤害率；不同接口的可执行性和样本构成不同。小规模场景和指定本体限制外推。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Edward Sun, Christopher Leet, Sravanthi Machcha, et al., ‘Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control,’ arXiv preprint, 2026, arXiv:2610.14043v1. [论文](https://arxiv.org/abs/2610.14043)；[核查正文](https://arxiv.org/html/2610.14043v1)。

**重点核查位置（章节主题）**：Methodology；Experiments；Failure Analysis。

OpenAlex 被引次数：**[0](https://openalex.org/W7221820979)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://github.com/robocurve/roboharm](https://github.com/robocurve/roboharm)。地址状态为 `candidate`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
