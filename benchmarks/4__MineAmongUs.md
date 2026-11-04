# MineAmongUs

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：安全。
> **分类依据**：具身游戏中的行为安全研究沙盒；不能推断现实自发意图。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：具身社交欺骗  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 B；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://junseokim0103.github.io/Lies-We-Can-See](https://junseokim0103.github.io/Lies-We-Can-See)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Human-Agent Interaction |
| 应用领域 | 具身欺骗 |
| 被测对象 | 三维多代理社会行为沙盒 |
| 历史关键词标签（未重新统计） | 尚未从摘要识别 |
| 评测维度/指标 | 3D 多模态 Among Us 沙盒；言语 + 非言语感觉运动通道 |
| 基础平台线索 | 表内摘要未明确基础平台。 |
| 规模线索 | 三维 Among Us 风格隐藏角色游戏，包含第一人称 RGB、聊天、位置和游戏状态，代理通过具身行动与其他玩家互动。 |
| 执行环境线索 | 三维多代理社会行为沙盒 |
| 来源审计 | [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions](https://arxiv.org/abs/2608.30428)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明 introduce MineAmongUs 3D multimodal sandbox。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W7204938515)；2026-11-04 |
| 术语说明 | 第 10 节解释本文出现的 6 个缩写／技术词，并标出 1 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md) |

## 1. 测什么问题（内容与所测环节）

**核心问题**：多模态代理的社会策略是否同时依赖语言和非语言行动，结果有多少来自模型、有多少来自代理框架？

**评测层级**：三维多代理社会行为沙盒。

## 2. 怎么构建的

**核心场景与条目**：三维 Among Us 风格隐藏角色游戏，包含第一人称 RGB、聊天、位置和游戏状态，代理通过具身行动与其他玩家互动。

**实现与判分**：Minecraft／Mineflayer 沙盒与 Aria 框架分离，固定模型做认知组件消融、固定框架比较模型；将行为标注为 23 类原子及跨时刻行为弧。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions](https://arxiv.org/abs/2608.30428) | 2026 | 提出 | 3D 多模态 Among Us 沙盒；言语 + 非言语感觉运动通道 | 指出 LLM/VLM 智能体的策略性欺骗已成为 AI 对齐与安全的核心议题，社交推理游戏是典型试验台；但现有试验台是纯文本的、且只跑单一固定智能体配置，漏掉了欺骗分类学视为核心的非言语感觉运动通道，也让人无法判断观察到的行为到底反映底层模型还是外围执行框架。该基准是一个 3D 多模态 Among Us 沙盒。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：论文发现非语言行为对游戏胜负的贡献在多个设置中更突出，并提供接近人工一致性的自动行为标注验证。成果是可配置沙盒与多模态行为分析协议。

**适用边界**：有明确隐藏角色目标的游戏行为不能直接证明模型在现实部署中自发产生恶意意图；胜率、行为标签一致率和现实安全性是不同概念。

## 5. 相关论文（均来自本调研表）

- [Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions](https://arxiv.org/abs/2608.30428)（2026；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

有明确隐藏角色目标的游戏行为不能直接证明模型在现实部署中自发产生恶意意图；胜率、行为标签一致率和现实安全性是不同概念。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（引用观测 2026-11-04）

**本次核查来源**：[1] Jaewoo Ahn, Junseo Kim, Hyunseo Kim, et al., ‘Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions,’ arXiv preprint, 2026, arXiv:2608.30428v1. [论文](https://arxiv.org/abs/2608.30428)；[核查正文](https://arxiv.org/html/2608.30428v1)。

**重点核查位置（章节主题）**：3.2 Sandbox；3.3 Aria；3.4 Evaluation；4 Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7204938515)**；观测日期：2026-11-04。这是所链接论文记录的计数，不是 benchmark 使用次数。

**项目与成果入口**：[https://junseokim0103.github.io/Lies-We-Can-See](https://junseokim0103.github.io/Lies-We-Can-See)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

**引文清单**：在 OpenAlex 引文图中暂无可列出的引文论文；arXiv 摘要未见命中。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->

<!-- project-review:start -->
## 8. 项目源核查（已确认项目入口，2026-11-04）

**项目入口**：[https://junseokim0103.github.io/Lies-We-Can-See](https://junseokim0103.github.io/Lies-We-Can-See)

| 抓取对象 | 实际读取的地址 | 抓取时状态 |
|---|---|---|
| [page](https://junseokim0103.github.io/Lies-We-Can-See) | https://junseokim0103.github.io/Lies-We-Can-See | 保留文本 4200 字符（截断） |

**项目页显示**：项目页 https://junseokim0103.github.io/Lies-We-Can-See（“Lies We Can See”）给出论文、作者（SNU、Inha、KAIST、Georgia Tech）与“Can an agent lie with its body, not just its words?”的定位。

**涉及领域**：具身社交互动中的欺骗（语言 + 非语言行为）；Minecraft 沙盒中的多代理博弈。

**测试目的与构建方法**：用 Minecraft／Mineflayer 沙盒与 Aria 框架分离“认知组件”和“框架”：固定模型做认知消融、固定框架比较模型；把行为标注为 23 类原子行为与跨时刻行为弧。

**测试缺陷**：有明确隐藏角色目标的游戏行为不能直接证明模型在现实中自发产生恶意意图；胜率、行为标签一致率与现实安全性是三个概念；模型集合与游戏版本固定。

**与具身智能安全的相关性**：间接但独特：它把“欺骗”从文本扩展到动作，说明只看对话日志会漏掉用身体实施的欺骗。对具身代理的信任与监督机制有直接含义，但不含物理伤害。

**用这个 benchmark 测了什么**：论文发现非语言行为对胜负的贡献在多个设置中更突出，并提供接近人工一致性的自动行为标注验证；成果是可配置沙盒与多模态行为分析协议。

**本轮核查边界**：只读项目页文字，未获取代码或数据。 本节只读项目页与 README 文本，未运行代码、未下载数据集。

<!-- project-review:end -->

<!-- usage-review:start -->
## 9. 使用明细：谁在用什么、怎么用

本轮未取到任何论文提到该基准的原文片段：OpenAlex 引文 0 篇，arXiv cs.RO／cs.CV 摘要检索 0 命中。这表示“没查到”，不等于“没人用”；论文自身的被测模型与结论见第 8 节。

<!-- usage-review:end -->

<!-- glossary:start -->
## 10. 术语说明（本文出现的词）

正文出现的缩写与技术词按下表解释，共 6 个。每个词都写清它除以什么、和哪些指标配套——不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。

| 术语 | 英文全称 | 中文 | 一句话解释 |
|---|---|---|---|
| **VLM** | Vision-Language Model | 视觉语言模型 | 能同时理解图像和文字的模型，常被当作具身代理的高层决策器。 |
| **LLM** | Large Language Model | 大语言模型 | 纯文本大模型，常作为具身代理的规划或工具调用层。 |
| **ablation** | ablation study | 消融实验 | 逐个去掉或替换模块，看性能变化，用来归因。 |
| **cs.RO** | arXiv category: cs.RO / cs.CV / cs.AI / cs.LG | arXiv 学科分类 | arXiv 的学科标签：cs.RO 机器人、cs.CV 计算机视觉、cs.AI 人工智能、cs.LG 机器学习。 |
| **RGB** | RGB image observation | 彩色图像观测 | 只用普通彩色相机画面作为输入，不含深度、触觉或本体状态。 |
| **Mineflayer** | Mineflayer | Minecraft 机器人接口库 | 用代码控制 Minecraft 角色的库，用于具身多代理实验。 |

**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：

| 名称 | 是什么 | 说明 |
|---|---|---|
| MineAmongUs | 基准 | 三维多代理社会行为沙盒 |

<!-- glossary:end -->
