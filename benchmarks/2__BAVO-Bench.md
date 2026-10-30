# BAVO-Bench

> **所属环节**：遮挡下的主动视觉恢复  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出者 0 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：遮挡下的主动视觉恢复。

指出物理主动视觉允许机器人在任务相关观测不可靠时改变视角，但现有操作基准对「策略如何在执行中从遮挡恢复」支持有限。BAVO-Bench 通过 Clean、Stage Occlusion 与 Random-time Occlusion 三种条件系统控制外部可见性，同时评测操作性能与主动视觉恢复能力；作者据此提出联合视角与操作控制的 A-FAR 策略。

信息取自表内论文 *Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复。

## 3. 用这个基准测了什么

**被测对象**：双臂操作策略（含主动视觉策略）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [BAVO-Bench：遮挡恢复的双臂主动视觉基准](https://arxiv.org/abs/2609.37292) | 2026 | arXiv 预印本 (arXiv:2609.37 | 使用 | Clean / 阶段遮挡 / 随机时刻遮挡；操作性能 + 主动视觉恢复 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **BAVO-Bench：遮挡恢复的双臂主动视觉基准**（2026）：作者据此提出联合视角与操作控制的 A-FAR 策略。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation（2026，arXiv 预印本 (arXiv:2609.37292)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
