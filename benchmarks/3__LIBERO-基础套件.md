# LIBERO（基础套件）

> **所属环节**：认知 + 动作控制（终身学习）  
> **分类**：VLA 能力  
> **关联论文**：本表 30 篇（提出者 2 篇，使用者 28 篇）

## 1. 测什么问题（内容与所测环节）

测「知识迁移」与「终身学习」：同一策略在任务序列上顺序学习后，能否保持旧技能并迁移到新任务。

## 2. 怎么构建的

4 个任务套件共 **130 个语言条件操作任务**：LIBERO-Spatial（空间关系）、LIBERO-Object（物体）、LIBERO-Goal（目标）、LIBERO-Long（长时程）。每套件配 50 条人类遥操作示范，并有预训练/顺序微调的标准协议。

## 3. 用这个基准测了什么

VLA 领域事实标准：π0/π0.5、OpenVLA、OpenVLA-OFT、GR00T N1/N1.5、Octo、SmolVLA、DTP、RoboMamba 等，几乎所有论文都以 LIBERO 平均成功率作为主指标。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LIBERO-Pro2.0：具身基础模型鲁棒性基准](https://arxiv.org/abs/2610.24587) | 2026 | arXiv 预印本 (arXiv:2610.24 | 使用 | 6 维度 22 种静态扰动 + 20 种运行时干预，1648 个偏移任务实例 |
| [LIBERO-RIG：硬件部署配置鲁棒性基准](https://arxiv.org/abs/2610.18843) | 2026 | arXiv 预印本 (arXiv:2610.18 | 使用 | 11 条硬件扰动轴 × 5 个严重度 = 210 种条件；每条件 500 回合 |
| [LIBERO-RECOVER：失败恢复能力基准](https://arxiv.org/abs/2609.05178) | 2026 | arXiv 预印本 (arXiv:2609.05 | 使用 | 失败识别与恢复成功率（相对纯任务成功率） |
| [Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准](https://arxiv.org/abs/2608.26578) | 2026 | arXiv 预印本 (arXiv:2608.26 | 使用 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 |
| [ManiPhysicsBench：物体保全的物理评测](https://arxiv.org/abs/2610.02802) | 2026 | arXiv 预印本 (arXiv:2610.02 | 使用 | 任务成功率 vs 安全成功率；形变/断裂阈值与接触力比较 |
| [IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测](https://arxiv.org/abs/2609.25562) | 2026 | arXiv 预印本 (arXiv:2609.25 | 使用 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 |
| [复述共识不等于自一致性：VLA 的指令依赖与鲁棒性](https://arxiv.org/abs/2610.19438) | 2026 | arXiv 预印本 (arXiv:2610.19 | 使用 | 指令改写下的成功率；错误指令探针；复述共识与置信度选择 |
| [VLA 真的理解指令吗：语言接地的机制可解释性研究](https://arxiv.org/abs/2610.10178) | 2026 | arXiv 预印本 (arXiv:2610.10 | 使用 | 激活/归因修补（activation & attribution patching）；残差流干预 |
| [只有成功率够吗：扰动下 VLA 的行为鲁棒性度量](https://arxiv.org/abs/2610.01351) | 2026 | arXiv 预印本 (arXiv:2610.01 | 使用 | 行为指标：运动平滑度、效率、夹爪行为及其变异性 |
| [VLA-Scope：偏移感知的失败预测](https://arxiv.org/abs/2609.21246) | 2026 | arXiv 预印本 (arXiv:2609.21 | 使用 | OOD 检测 + 偏移类别分类 + 执行进度；失败风险预测 |
| [MINERVA：LIBERO 的任务容量下限](https://arxiv.org/abs/2609.03715) | 2026 | arXiv 预印本 (arXiv:2609.03 | **提出** | 参数规模—成功率曲线；架构/训练/推理因素消融 |
| [语言扰动下的持续模仿学习任务保持基准](https://arxiv.org/abs/2610.00542) | 2026 | arXiv 预印本 (arXiv:2610.00 | 使用 | 保义/变义指令变体；任务能力与语言敏感性分离 |
| [SilentDrift：利用动作分块的隐蔽后门攻击](https://arxiv.org/abs/2601.14323) | 2026 | arXiv 预印本 (arXiv:2601.14 | 使用 | 攻击隐蔽性（运动学连续性）、攻击成功率 |
| [DropVLA：动作级后门攻击](https://arxiv.org/abs/2510.10932) | 2025 | arXiv 预印本 (arXiv:2510.10 | 使用 | 指定动作原语的触发成功率；名义任务性能保持 |
| [EDPA：模型无关的 VLA 对抗补丁攻击与防御](https://arxiv.org/abs/2510.13237) | 2025 | arXiv 预印本 (arXiv:2510.13 | 使用 | 补丁攻击成功率；跨模型/跨机械臂迁移性 |
| [Altered Thoughts：推理型 VLA 的思维链脆弱性探针](https://arxiv.org/abs/2603.12717) | 2026 | arXiv 预印本 (arXiv:2603.12 | 使用 | 7 类文本腐蚀 × 3 个攻击者层级；仅改推理轨迹、输入不动 |
| [预训练 VLA 联邦微调的实证研究与开放测试床](https://arxiv.org/abs/2609.22973) | 2026 | arXiv 预印本 (arXiv:2609.22 | 使用 | LIBERO 40 个仿真任务 + 两处真机 6 个任务；2/3 站点分布式示范 |
| [动作 tokenizer 究竟该按什么评：重建之外的可预测性与鲁棒性](https://arxiv.org/abs/2610.09170) | 2026 | arXiv 预印本 (arXiv:2610.09 | 使用 | token 可预测性、未见 token 的解码合理性、下游策略成功率 |
| [Memorize / Adapt / Ignore：训练数据变化如何生效的机制诊](https://arxiv.org/abs/2609.38401) | 2026 | arXiv 预印本 (arXiv:2609.38 | 使用 | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） |
| [不是所有层都要调：VLA 适配的区域诊断](https://arxiv.org/abs/2609.18084) | 2026 | arXiv 预印本 (arXiv:2609.18 | 使用 | 区域隔离微调的归一化参数位移（适配代价谱） |
| [Rephrase Before You Act：VLA 的语言敏感性刻画与缓解](https://arxiv.org/abs/2610.10526) | 2026 | arXiv 预印本 (arXiv:2610.10 | 使用 | 单次编辑引起的成功率波动、oracle 短语搜索、ID/OOD 差距归因 |
| [什么让 VLA 更高效：动作头、规模与延迟的受控评测](https://arxiv.org/abs/2609.13984) | 2026 | arXiv 预印本 (arXiv:2609.13 | 使用 | 动作头设计 × 模块规模，每种配置配实测端侧延迟 |
| [VLA 是理解物体还是重放动作：物理属性的表示探针](https://arxiv.org/abs/2610.06078) | 2026 | arXiv 预印本 (arXiv:2610.06 | 使用 | 线性探针 + 表示相似性分析（RSA）；物理 vs 非物理属性可解码性 |
| [GoBA：以物理物体为触发器的目标导向后门](https://arxiv.org/abs/2510.09269) | 2025 | arXiv 预印本 (arXiv:2510.09 | 使用 | 触发器为真实物体；目标导向动作执行率、干净性能保持 |
| [VLA-Fool：跨模态失配下的多模态对抗攻击](https://arxiv.org/abs/2511.16203) | 2025 | arXiv 预印本 (arXiv:2511.16 | 使用 | 文本/视觉/跨模态三层攻击；跨模态对齐破坏 |
| [Detect and Suppress：对抗补丁的机制性防御](https://arxiv.org/abs/2610.03498) | 2026 | arXiv 预印本 (arXiv:2610.03 | 使用 | SAE 特征与补丁的相关性；条件抑制后的成功率 |
| [TAPDreamer：面向世界动作模型的可迁移对抗补丁](https://arxiv.org/abs/2610.06814) | 2026 | arXiv 预印本 (arXiv:2610.06 | 使用 | 仅用公开编码器、无需查询目标策略；跨任务与跨动作架构迁移 |
| [LIBERO：终身机器人学习与知识迁移基准](https://arxiv.org/abs/2306.03310) | 2023 | NeurIPS 2023（神经信息处理系统大会， | **提出** | 4 个任务套件（130 个任务）；知识迁移与终身学习指标 |
| [SafeVLA-Bench：VLA 的「成功-安全」落差基准](https://arxiv.org/abs/2606.00773) | 2026 | arXiv 预印本 (arXiv:2606.00 | 使用 | 信号时序逻辑（STL）不变式 + 定量鲁棒性；安全率、成功但不安全率 |
| [dWorldEval：离散扩散世界模型驱动的可扩展策略评测](https://arxiv.org/abs/2604.22152) | 2026 | arXiv 预印本 (arXiv:2604.22 | 使用 | 离散扩散世界模型；视觉/语言/动作统一 token 空间 |

## 4. 关键结论与改进方向

**关键结论**：作为**能力底座**极其成功（任务干净、协议统一、复现性好），但也因此成为**饱和基准**：SOTA 已接近 100%，区分度下降；且它只测「做得成」，不测鲁棒性、安全性或失败恢复——本调研中的大量工作正是围绕这些缺口展开（LIBERO-Plus/Pro2.0/RIG/VPro/MAX/RECOVER/CTRL/X/Para、SafeLIBERO、Trap-LIBERO）。

**论文提到的改进方向**：①在 LIBERO 之上补充分布偏移、硬件扰动、过程安全与失败恢复维度；②报告需说明微调与评测是否共用同一指令集（否则虚高）；③容量下限研究（MINERVA）提示该基准的任务容量已接近饱和，需更难的任务集。

## 5. 相关论文（均来自本调研表）

- LIBERO-Pro2.0: A Benchmark for Evaluating the Robustness of Embodied Foundation Models（2026，arXiv 预印本 (arXiv:2610.24587)）
- LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2610.18843)）
- LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models（2026，arXiv 预印本 (arXiv:2609.05178)）
- TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes（2026，arXiv 预印本 (arXiv:2608.26578)）
- ManiPhysicsBench: Physics-Based Assessment of Object Preservation in VLA Manipulation（2026，arXiv 预印本 (arXiv:2610.02802)）
- IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models（2026，arXiv 预印本 (arXiv:2609.25562)）
- Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies（2026，arXiv 预印本 (arXiv:2610.19438)）
- Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding（2026，arXiv 预印本 (arXiv:2610.10178)）
- Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks（2026，arXiv 预印本 (arXiv:2610.01351)）
- VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2609.21246)）
- MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?（2026，arXiv 预印本 (arXiv:2609.03715)）  ← **提出**
- Does Continual Imitation Learning Remain Grounded? A Language-Perturbed Benchmark for Robotic Task Retention（2026，arXiv 预印本 (arXiv:2610.00542)）
- SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2601.14323)）
- DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2510.10932)）
- Model-agnostic Adversarial Attack and Defense for Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2510.13237)）
- Altered Thoughts, Altered Actions: Probing Chain-of-Thought Vulnerabilities in VLA Robotic Manipulation（2026，arXiv 预印本 (arXiv:2603.12717)）
- An Empirical Study and Open Testbed for Federated Fine-Tuning of Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2609.22973)）
- Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?（2026，arXiv 预印本 (arXiv:2610.09170)）
- Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation（2026，arXiv 预印本 (arXiv:2609.38401)）
- Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2609.18084)）
- Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2610.10526)）
- What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency（2026，arXiv 预印本 (arXiv:2609.13984)）
- Do VLAs Understand and Adapt to the Objects They Handle, or Simply Replay Learned Behaviors?（2026，arXiv 预印本 (arXiv:2610.06078)）
- Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects（2025，arXiv 预印本 (arXiv:2510.09269)）
- When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2511.16203)）
- Detect and Suppress: A Mechanistic Defense against Adversarial Patches in VLA Models（2026，arXiv 预印本 (arXiv:2610.03498)）
- TAPDreamer: Transferable Adversarial Patches for World Action Models（2026，arXiv 预印本 (arXiv:2610.06814)）
- LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning（2023，NeurIPS 2023（神经信息处理系统大会，Datasets & Bench）  ← **提出**
- SafeVLA-Bench: A Benchmark for the Success-Safety Gap in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2606.00773)）
- dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model（2026，arXiv 预印本 (arXiv:2604.22152)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
