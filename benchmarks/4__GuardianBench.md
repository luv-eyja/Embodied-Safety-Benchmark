# GuardianBench

> **所属环节**：同场景指令对比的潜在风险  
> **分类**：具身智能体安全  
> **关联论文**：本表 1 篇（提出者 1 篇，使用者 0 篇）

## 1. 测什么问题（内容与所测环节）

同场景指令对比的潜在风险。

该基准由 *GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI* 提出，其定位为：**GuardianBench：同场景指令对比的潜在语境风险基准**。

## 2. 怎么构建的

构建要点（据原文摘要）：3024 个「同场景安全/不安全」配对样本；配对准确率。

## 3. 用这个基准测了什么

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [GuardianBench：同场景指令对比的潜在语境风险基准](https://arxiv.org/abs/2608.21928) | 2026 | arXiv 预印本 (arXiv:2608.21 | **提出** | 3024 个「同场景安全/不安全」配对样本；配对准确率 |

## 4. 关键结论与改进方向

**要点**：指出具身场景中的风险可以是潜在的：一条良性指令与一个安全场景组合之后才变得危险。既有工作或改变视觉上下文、或评测执行期动态，而「固定场景、只改指令」这一互补轴向此前研究不足。基准以国际安全标准为依据构造 3024 组同场景安全/不安全对比样本，发现 VLM 的判定对指令不敏感（同场景两条指令常常都被批准），主模型平均配对准确率仅 24.1%。

> 该基准目前仅在其提出论文中出现，尚无其他表内论文复用它，因此横向结论有限。

## 5. 相关论文（均来自本调研表）

- GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI（2026，arXiv 预印本 (arXiv:2608.21928)）  ← **提出**

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
