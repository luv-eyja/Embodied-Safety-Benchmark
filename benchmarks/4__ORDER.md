# ORDER

> **所属环节**：虚构世界领域适配  
> **分类**：具身智能体安全  
> **关联论文**：本表 10 篇（提出者 1 篇，使用者 9 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：虚构世界领域适配。

指出现有持续预训练评测的基本问题：若训练语料与模型已知内容重叠，性能提升无法干净归因于新学习。这在「知识密集、任务轻」的机器人部署中最关键——如药品分发、危险品处理、场地专有规程，物理任务简单但治理规则专有且安全攸关，且大量实机测试既昂贵又不安全。ORDER 建立在任何模型预训练数据中都不存在的虚构世界之上。

信息取自表内论文 *ORDER: A Fictitious-World Benchmark for Domain-Adaptive Embodied AI*（该基准的提出者）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：342,069 token 合成语料；500 题知识测试 + 更难组合任务。

## 3. 用这个基准测了什么

**被测对象**：具身推理模型（知识密集、任务轻的部署）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [H²V-M：区域级鲁棒性验证（非采样）](https://arxiv.org/abs/2609.22293) | 2026 | arXiv 预印本 (arXiv:2609.22 | 使用 | 连续扰动区域上的形式化验证；亮度偏移、相机旋转及其组合 |
| [IS-Bench：日常家务中的交互安全评测](https://arxiv.org/abs/2506.16402) | 2025 | AAAI 2026 | 使用 | 161 个场景 / 388 个安全风险；过程导向评测（风险感知与缓解步骤顺序） |
| [SafeMindBench：具身 LLM 智能体的四阶段安全基准](https://arxiv.org/abs/2509.25885) | 2025 | arXiv 预印本 (arXiv:2509.25 | 使用 | 5558 个样本；四类任务 × 三类正交安全约束（事实/因果/时序） |
| [波斯语 VLA 数据集与「歧义/不可行」感知的指令-计划接地基准](https://arxiv.org/abs/2610.15666) | 2026 | arXiv 预印本 (arXiv:2610.15 | 使用 | 258 实例 / 230 张真实场景图；歧义与不可行标注；PGOS-FA 指标 |
| [人形机器人的自演化：机制、安全与部署后自我改进的评测](https://arxiv.org/abs/2609.13236) | 2026 | arXiv 预印本 (arXiv:2609.13 | 使用 | 自演化机制、安全边界、部署后改进的评测 |
| [MemForm：LLM 智能体记忆形成投毒基准](https://arxiv.org/abs/2610.14431) | 2026 | arXiv 预印本 (arXiv:2610.14 | 使用 | 五类形成接口：内容、证据、范围、选择、路径投毒 |
| [ORDER：虚构世界中的领域自适应具身基准](https://arxiv.org/abs/2609.22285) | 2026 | arXiv 预印本 (arXiv:2609.22 | **提出** | 342,069 token 合成语料；500 题知识测试 + 更难组合任务 |
| [GaugeBench：形态感知策略的表示鲁棒性基准](https://arxiv.org/abs/2610.07597) | 2026 | arXiv 预印本 (arXiv:2610.07 | 使用 | 物理等价但约定不同的机器人描述；同一策略权重评测 |
| [PLCBENCH：LLM 智能体将 PLC 访问转化为持续物理影响的评测](https://arxiv.org/abs/2608.26882) | 2026 | arXiv 预印本 (arXiv:2608.26 | 使用 | 真实 PLC 硬件在环（HIL）；从网络访问到持续物理影响的完整链路 |
| [AgiBot World Colosseo：百万轨迹级操作平台](https://doi.org/10.1109/IROS60139.2025.11247088) | 2025 | IROS 2025（IEEE/RSJ 智能机器人 | 使用 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **H²V-M：区域级鲁棒性验证（非采样）**（2026）：该工作对连续的光度与几何扰动区域（亮度偏移、相机旋转及其组合）做鲁棒性验证，覆盖 6 个 VLM 与 5 个 VLA，并提出 margin-aware 收敛规则 H²V-M，使 32B 参数规模下的验证在计算上可行。
- **IS-Bench：日常家务中的交互安全评测**（2025）：该基准提出「交互安全」——智能体感知涌现风险并按正确程序顺序执行缓解步骤的能力——含 161 个场景、388 个具体安全风险，并采用过程导向的评测核查中间步骤，发表于 AAAI 2026。
- **SafeMindBench：具身 LLM 智能体的四阶段安全基准**（2025）：实验显示主流 LLM 与广泛使用的具身智能体仍存在显著风险。
- **波斯语 VLA 数据集与「歧义/不可行」感知的指令-计划接地基准**（2026）：用 LLM-as-judge 协议与新指标 PGOS-FA（加入步骤顺序敏感性、过度生成惩罚）评估检索增强、CoT 提示与智能体式消歧。
- **人形机器人的自演化：机制、安全与部署后自我改进的评测**（2026）：本综述考察当智能体拥有物理身体时自演化会如何改变，界定人形自演化的定义、给出部署分层，并梳理机制、安全与评测三方面。
- **MemForm：LLM 智能体记忆形成投毒基准**（2026）：MemForm 把记忆形成投毒形式化为对持久记忆产出与提交接口的对抗操纵，并引入「选择投毒」与「路径投毒」作为隔离保持与巩固环节的受控干预类别。
- **GaugeBench：形态感知策略的表示鲁棒性基准**（2026）：基准在物理等价约定下重写固定机构，并验证物理与策略接口保持后再评测同一策略权重。
- **PLCBENCH：LLM 智能体将 PLC 访问转化为持续物理影响的评测**（2026）：该基准是首个真实 PLC 硬件在环框架。
- **AgiBot World Colosseo：百万轨迹级操作平台**（2025）：在数据之上提出通用策略 Genie Operator-1（GO-1）。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- Validating, Not Sampling: Region-Level Robustness of Vision-Language and Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2609.22293)）
- IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks（2025，AAAI 2026）
- SafeMind: Benchmarking and Mitigating Safety Risks in Embodied LLM Agents（2025，arXiv 预印本 (arXiv:2509.25885)）
- A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding（2026，arXiv 预印本 (arXiv:2610.15666)）
- Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement（2026，arXiv 预印本 (arXiv:2609.13236)）
- MemForm: Benchmarking Memory Formation Poisoning in LLM Agents（2026，arXiv 预印本 (arXiv:2610.14431)）
- ORDER: A Fictitious-World Benchmark for Domain-Adaptive Embodied AI（2026，arXiv 预印本 (arXiv:2609.22285)）  ← **提出**
- The Robot Is Not Its Description: GaugeBench for Representation Robustness in Morphology-Aware Policies（2026，arXiv 预印本 (arXiv:2610.07597)）
- PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?（2026，arXiv 预印本 (arXiv:2608.26882)）
- AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems（2025，IROS 2025（IEEE/RSJ 智能机器人与系统国际会议））

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
