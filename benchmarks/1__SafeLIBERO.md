# SafeLIBERO

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：能力、安全。
> **分类依据**：VLSA 方法论文中的具名安全任务集，本条只统计该测试集。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：动作控制（碰撞安全）  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://vlsa-aegis.github.io](https://vlsa-aegis.github.io)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer |
| 年份 | 2025（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 仿真障碍避碰＋安全控制方法 |
| 历史关键词标签（未重新统计） | 语义/指令安全、物理/接触安全、任务能力 |
| 评测维度/指标 | 碰撞/安全违规率与指令遵循性能的权衡 |
| 基础平台线索 | LIBERO |
| 规模线索 | 四个 LIBERO 套件各选 4 个任务，每任务设置靠近目标与阻挡路径两级障碍，共 32 场景、每场景 50 次、合计 1,600 episode。 |
| 执行环境线索 | 仿真障碍避碰＋安全控制方法 |
| 来源审计 | [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)；same_paper_in_registry |
| 来源核验依据 | 摘要明确写明构建 SafeLIBERO safety-critical benchmark。 |
| OpenAlex 引用快照 | [0](https://openalex.org/W4417446096)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：在原有 VLA 策略前增加安全层，能否避免杂乱桌面的障碍碰撞，同时保留任务能力？

**评测层级**：仿真障碍避碰＋安全控制方法。

## 2. 怎么构建的

**核心场景与条目**：四个 LIBERO 套件各选 4 个任务，每任务设置靠近目标与阻挡路径两级障碍，共 32 场景、每场景 50 次、合计 1,600 episode。

**实现与判分**：AEGIS 采用控制障碍函数和二次规划修正名义动作；在平移／完整动作空间分别评价避碰率 CAR、任务成功率 TSR 和执行步数 ETS，并用两项真机任务验证。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891) | 2025 | 提出 | 碰撞/安全违规率与指令遵循性能的权衡 | 提出基于控制屏障函数的即插即用安全约束层 AEGIS，可与现有 VLA 直接组合并给出理论安全保证；为验证效果构建安全关键基准 SafeLIBERO，覆盖多种存在碰撞风险的操作场景，同时度量安全性与原有指令遵循性能。可作为「防御方法自带评测集」的典型样本。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：平移动作设置中，π0.5 的 CAR 18.7% 提升至 AEGIS 的 77.9%，TSR 50.9% 提升至 68.1%；完整动作空间也单独给出结果，不能交叉混比。

**适用边界**：属于受控障碍避碰，不覆盖全部语义风险；CBF 的理论性质依赖状态估计、模型和求解可行性，不能无条件等同于真机安全保证。

## 5. 相关论文（均来自本调研表）

- [VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer](https://arxiv.org/abs/2512.11891)（2025；提出）

## 6. 证据边界与复核建议

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

属于受控障碍避碰，不覆盖全部语义风险；CBF 的理论性质依赖状态估计、模型和求解可行性，不能无条件等同于真机安全保证。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Songqiao Hu, Zeyi Liu, Shuang Liu, et al., ‘VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer,’ arXiv preprint, 2025, arXiv:2512.11891v2. [论文](https://arxiv.org/abs/2512.11891)；[核查正文](https://arxiv.org/html/2512.11891v2)。

**重点核查位置（章节主题）**：V-A Experimental Setup；V-B Results；VI Real-world Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W4417446096)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://vlsa-aegis.github.io](https://vlsa-aegis.github.io)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
