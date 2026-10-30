# LIBERO-Pro2.0

> **所属环节**：条件/环境/观测/执行/状态/语言（六维）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 2 篇（提出者 1 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

LIBERO 高分不等于鲁棒：模型可能利用基准特定规律，而非真正泛化到多样运行条件。

## 2. 怎么构建的

**22 种静态扰动 + 20 种运行时干预**，跨六个维度：条件（Condition）、环境（Environment）、观测（Observation）、执行（Execution）、机器人状态配置（Robot State Configuration）、语言（Language），共 **1,648 个经验证的偏移任务实例**；并采集 39,390 条轨迹支持面向鲁棒性的学习。所有偏移实例经六轮校验。

## 3. 用这个基准测了什么

具身基础模型 / VLA。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LIBERO-Pro2.0：具身基础模型鲁棒性基准](https://arxiv.org/abs/2610.24587) | 2026 | arXiv 预印本 (arXiv:2610.24 | **提出** | 6 维度 22 种静态扰动 + 20 种运行时干预，1648 个偏移任务实例 |
| [指令检索轨迹：VLA 泛化失败的诊断与缓解](https://arxiv.org/abs/2609.39971) | 2026 | arXiv 预印本 (arXiv:2609.39 | 使用 | 反事实指令下的行为切换；指令-动作绑定（instruction-action binding） |

## 4. 关键结论与改进方向

**关键结论**：静态扰动之外，**运行时干预**（执行过程中条件突变）构成独立且更难的评测维度；稳健的鲁棒性评估需要两者结合。

**论文提到的改进方向**：①把运行时干预纳入标准评测；②需要与扰动配套的训练数据，而不只是测试集；③大规模实例必须经过多轮校验以保证标签可靠。

## 5. 相关论文（均来自本调研表）

- LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models（2026，arXiv 预印本 (arXiv:2610.24587)）  ← **提出**
- When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models（2026，arXiv 预印本 (arXiv:2609.39971)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
