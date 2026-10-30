# DESPITE

> **所属环节**：具身规划的系统性安全风险  
> **分类**：具身智能体安全  
> **关联论文**：本表 18 篇（提出者 0 篇，使用者 18 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：具身规划的系统性安全风险。

标准基准默认执行过程中视觉观测干净、及时且一致，该基准专门扰动执行期的视觉证据：覆盖视觉证据退化、相机帧陈旧（staleness）、视觉源一致性与任务相关场景变化四个维度，共 12 类挑战、96 种设置、3296 个任务-条件案例，约 19.6 万仿真回合并辅以 200 次 Franka Research 3 真机 rollout。

信息取自表内论文 *LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：视觉证据退化 / 相机陈旧 / 视觉源一致性 / 任务相关场景变化；12 类挑战 96 种设置。

## 3. 用这个基准测了什么

**被测对象**：VLA 与世界动作模型（WAM）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LIBERO-VPro：闭环视觉鲁棒性基准](https://arxiv.org/abs/2609.24350) | 2026 | arXiv 预印本 (arXiv:2609.24 | 使用 | 视觉证据退化 / 相机陈旧 / 视觉源一致性 / 任务相关场景变化；12 类挑战 96 种设置 |
| [RoboCasa-Shift：长时程操作的阶段感知鲁棒性评测](https://arxiv.org/abs/2610.27861) | 2026 | arXiv 预印本 (arXiv:2610.27 | 使用 | 单因子受控偏移 + 干净/扰动配对 rollout + 阶段级诊断；4 因子 × 3 严重度 |
| [VLA-GAUGE：泛化与鲁棒性统一诊断框架](https://arxiv.org/abs/2610.16567) | 2026 | arXiv 预印本 (arXiv:2610.16 | 使用 | 6 个能力套件的 ID/OOD 配对任务；单因子敏感度 + 组合扰动；诊断驱动改进 |
| [AttackVLA：VLA 对抗与后门攻击统一评测](https://arxiv.org/abs/2511.12149) | 2025 | arXiv 预印本 (arXiv:2511.12 | 使用 | 数据构建/训练/推理三阶段的全谱系攻击；攻击成功率与真实场景有效性 |
| [编码但未受控：视觉-语言策略的指令接地缺口](https://arxiv.org/abs/2610.06235) | 2026 | arXiv 预印本 (arXiv:2610.06 | 使用 | 场景保持的指令干预：有效目标替换、任意名词、无关句子 |
| [MINERVA：LIBERO 的任务容量下限](https://arxiv.org/abs/2609.03715) | 2026 | arXiv 预印本 (arXiv:2609.03 | 使用 | 参数规模—成功率曲线；架构/训练/推理因素消融 |
| [ASIMOV Benchmark：语义安全基准与机器人宪法](https://arxiv.org/abs/2503.08663) | 2025 | arXiv 预印本 (arXiv:2503.08 | 使用 | 语义安全；大规模情景化安全判断数据集 |
| [VLA 机器人对抗脆弱性系统评测](https://arxiv.org/abs/2411.13587) | 2025 | ICCV 2025 | 使用 | 两个无目标攻击目标（基于空间基础 destabilize 动作）+ 一个轨迹操控的有目标攻击；对抗补丁 |
| [EDPA：模型无关的 VLA 对抗补丁攻击与防御](https://arxiv.org/abs/2510.13237) | 2025 | arXiv 预印本 (arXiv:2510.13 | 使用 | 补丁攻击成功率；跨模型/跨机械臂迁移性 |
| [量化 VLA 的分布外鲁棒性：从「保性能」到「保泛化」](https://arxiv.org/abs/2610.05745) | 2026 | arXiv 预印本 (arXiv:2610.05 | 使用 | 分布内性能 vs 环境扰动下的鲁棒性/泛化；动作偏差的状态分布 |
| [BYOVLA：运行时观测干预提升 VLA 视觉鲁棒性](https://arxiv.org/abs/2410.01971) | 2025 | ICRA 2025 | 使用 | 任务无关视觉细节（干扰物、背景色）下的真机成功率 |
| [VLA-Fool：跨模态失配下的多模态对抗攻击](https://arxiv.org/abs/2511.16203) | 2025 | arXiv 预印本 (arXiv:2511.16 | 使用 | 文本/视觉/跨模态三层攻击；跨模态对齐破坏 |
| [波斯语 VLA 数据集与「歧义/不可行」感知的指令-计划接地基准](https://arxiv.org/abs/2610.15666) | 2026 | arXiv 预印本 (arXiv:2610.15 | 使用 | 258 实例 / 230 张真实场景图；歧义与不可行标注；PGOS-FA 指标 |
| [SafeBench：自动驾驶安全评测平台](https://arxiv.org/abs/2206.09682) | 2022 | NeurIPS 2022（神经信息处理系统大会） | 使用 | 统一仿真平台 + 安全关键场景生成；跨平台可比性 |
| [RoboVAD：机械臂操作视频的跨域异常检测基准](https://arxiv.org/abs/2609.17843) | 2026 | arXiv 预印本 (arXiv:2609.17 | 使用 | 跨域评测场景；异常触发恢复流程 |
| [DESPITE：具身规划的系统性安全风险基准](https://arxiv.org/abs/2604.18463) | 2026 | arXiv 预印本 (arXiv:2604.18 | 使用 | 12,279 个任务；物理与规范两类危险；确定性验证 |
| [RoboHarm：LLM 拒答在机器人控制下是否幸存](https://arxiv.org/abs/2610.14043) | 2026 | arXiv 预印本 (arXiv:2610.14 | 使用 | 接口变量受控；MuJoCo 双臂 YAM 仿真 + 真机 612 次试验 |
| [TrafficSignBench：以交通标志为中心的闭环合规评测](https://arxiv.org/abs/2609.38463) | 2026 | arXiv 预印本 (arXiv:2609.38 | 使用 | 真实地图仿真 + 规则定向的程序化场景生成；规则合规率 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **LIBERO-VPro：闭环视觉鲁棒性基准**（2026）：标准基准默认执行过程中视觉观测干净、及时且一致，该基准专门扰动执行期的视觉证据：覆盖视觉证据退化、相机帧陈旧（staleness）、视觉源一致性与任务相关场景变化四个维度，共 12 类挑战、96 种设置、3296 个任务-条件案例，约 19.6 万仿真回合并辅以 200 次 Franka Resea
- **RoboCasa-Shift：长时程操作的阶段感知鲁棒性评测**（2026）：对 4 个通过干净性能门槛的长时程任务做 4 种扰动因子 × 3 个校准严重度共 1040 次正式评测，发现鲁棒性响应在因子与任务间差异很大、且不随严重度单调变化。
- **VLA-GAUGE：泛化与鲁棒性统一诊断框架**（2026）：在统一协议下评测 12 个不同模型规模与动作建模范式的 VLA。
- **AttackVLA：VLA 对抗与后门攻击统一评测**（2025）：框架对齐 VLA 开发生命周期（数据构建、模型训练、推理），统一动作 tokenizer 口径，集成针对 VLA 的既有攻击与适配的迁移攻击，并在真实环境中验证，为 VLA 攻防提供统一评测口径。
- **编码但未受控：视觉-语言策略的指令接地缺口**（2026）：并在仿真与真机上验证该现象，进一步分析其是否源于语言不敏感而非感知失败。
- **MINERVA：LIBERO 的任务容量下限**（2026）：这一结果对「LIBERO 是否仍是有效的能力基准」提出了直接质疑。
- **ASIMOV Benchmark：语义安全基准与机器人宪法**（2025）：工作有两点贡献：给出可规模化生成「机器人宪法」的数据配方，并发布 ASIMOV Benchmark——用于评测与提升机器人基础模型语义安全的大规模数据集集合。
- **VLA 机器人对抗脆弱性系统评测**（2025）：并设计对抗补丁生成方法，把小块彩色补丁放入相机视野，从而在数字与物理两种设定下实施攻击，系统评估 VLA 的鲁棒性（ICCV 2025）。
- **EDPA：模型无关的 VLA 对抗补丁攻击与防御**（2025）：该工作为「VLA 攻击的可迁移性与可复现评测」提供了基线。
- **量化 VLA 的分布外鲁棒性：从「保性能」到「保泛化」**（2026）：结论是有效的量化后恢复必须只在脆弱状态上做选择性干预。
- **BYOVLA：运行时观测干预提升 VLA 视觉鲁棒性**（2025）：与任意现成 VLA 兼容、无需微调也无需访问权重，并给出语言指令操作任务的真机实验。
- **VLA-Fool：跨模态失配下的多模态对抗攻击**（2025）：VLA-Fool 统一了三个层次的多模态对抗攻击（文本扰动等），在白盒与黑盒设定下系统评测，构成一份较完整的 VLA 多模态鲁棒性评估。
- **波斯语 VLA 数据集与「歧义/不可行」感知的指令-计划接地基准**（2026）：用 LLM-as-judge 协议与新指标 PGOS-FA（加入步骤顺序敏感性、过度生成惩罚）评估检索增强、CoT 提示与智能体式消歧。
- **SafeBench：自动驾驶安全评测平台**（2022）：SafeBench 把评测统一到一个基准平台上，使安全评测可复现、可比较（NeurIPS 2022）。
- **RoboVAD：机械臂操作视频的跨域异常检测基准**（2026）：RoboVAD 是大规模机械臂操作视频异常检测基准，包含具有挑战性的跨域评测场景。
- **DESPITE：具身规划的系统性安全风险基准**（2026）：18 个开源模型（3B 到 671B）的规划能力随规模从 0.4% 提升到 99.3%，而安全意识基本持平（38–57%）。
- **RoboHarm：LLM 拒答在机器人控制下是否幸存**（2026）：真机上六个末端控制的模型在 612 次试验中拒绝率约 18%。
- **TrafficSignBench：以交通标志为中心的闭环合规评测**（2026）：基准以交通标志为中心，把真实地图仿真与规则定向的程序化场景生成结合，实现系统且可解释的规则合规评测。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models（2026，arXiv 预印本 (arXiv:2609.24350)）
- RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation（2026，arXiv 预印本 (arXiv:2610.27861)）
- VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2610.16567)）
- AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2511.12149)）
- Encoded but Not in Control: Revealing the Grounding Gap in Vision-Language Robot Policies（2026，arXiv 预印本 (arXiv:2610.06235)）
- MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?（2026，arXiv 预印本 (arXiv:2609.03715)）
- Generating Robot Constitutions & Benchmarks for Semantic Safety（2025，arXiv 预印本 (arXiv:2503.08663)）
- Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics（2025，ICCV 2025）
- Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2510.13237)）
- Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning（2026，arXiv 预印本 (arXiv:2610.05745)）
- Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust（2025，ICRA 2025）
- When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2511.16203)）
- A Persian Vision-Language-Action Dataset and Benchmark for Ambiguity- and Infeasibility-Aware Instruction-to-Plan Grounding（2026，arXiv 预印本 (arXiv:2610.15666)）
- SafeBench: A Benchmarking Platform for Safety Evaluation of Autonomous Vehicles（2022，NeurIPS 2022（神经信息处理系统大会））
- RoboVAD: A Large Cross-Domain Evaluation Benchmark for Anomaly Detection in Robotic Arm Manipulation Videos（2026，arXiv 预印本 (arXiv:2609.17843)）
- Using Large Language Models for Embodied Planning Introduces Systematic Safety Risks（2026，arXiv 预印本 (arXiv:2604.18463)）
- Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control（2026，arXiv 预印本 (arXiv:2610.14043)）
- TrafficSignBench: Rule-Centric Closed-Loop Evaluation of Traffic-Sign Compliance in Autonomous Driving（2026，arXiv 预印本 (arXiv:2609.38463)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
