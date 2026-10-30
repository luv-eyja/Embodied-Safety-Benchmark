# LIBERO-Para

> **所属环节**：指令复述敏感性  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出者 0 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：指令复述敏感性。

VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。该基准在统一上报口径下对 6 个已发布系统分轴评测：LIBERO 上的干净能力、LIBERO-Plus 上的非语言鲁棒性、LIBERO-Para 上的指令敏感度以及实测执行代价，并聚合三个不同随机种子的完整评测。

信息取自表内论文 *IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价。

## 3. 用这个基准测了什么

**被测对象**：6 个已发布的 VLA 与世界动作模型（WAM）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测](https://arxiv.org/abs/2609.25562) | 2026 | arXiv 预印本 (arXiv:2609.25 | 使用 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测**（2026）：该基准在统一上报口径下对 6 个已发布系统分轴评测：LIBERO 上的干净能力、LIBERO-Plus 上的非语言鲁棒性、LIBERO-Para 上的指令敏感度以及实测执行代价，并聚合三个不同随机种子的完整评测。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models（2026，arXiv 预印本 (arXiv:2609.25562)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
