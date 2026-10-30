# RoboTwin

> **所属环节**：动作控制（双臂协同）  
> **分类**：VLA 能力  
> **关联论文**：本表 8 篇（提出者 1 篇，使用者 7 篇）

## 1. 测什么问题（内容与所测环节）

单臂基准无法覆盖双臂/高自由度协同操作；而双臂任务的场景与物体多样性极难靠手工搭建。

## 2. 怎么构建的

用**生成式数字孪生**批量生成多样化物体与场景，从而在仿真中大规模构造双臂协同操作任务，并支持向真机迁移的评测。

## 3. 用这个基准测了什么

双臂机器人操作策略（含 VLA）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准](https://arxiv.org/abs/2608.26578) | 2026 | arXiv 预印本 (arXiv:2608.26 | 使用 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 |
| [动作 tokenizer 究竟该按什么评：重建之外的可预测性与鲁棒性](https://arxiv.org/abs/2610.09170) | 2026 | arXiv 预印本 (arXiv:2610.09 | 使用 | token 可预测性、未见 token 的解码合理性、下游策略成功率 |
| [Memorize / Adapt / Ignore：训练数据变化如何生效的机制诊](https://arxiv.org/abs/2609.38401) | 2026 | arXiv 预印本 (arXiv:2609.38 | 使用 | 域随机化与示范筛选；行为 + 内部表示（经验 NTK） |
| [世界动作模型需要什么样的视觉表示](https://arxiv.org/abs/2610.13024) | 2026 | arXiv 预印本 (arXiv:2610.13 | 使用 | 视觉表示 × 集成机制 × 特征组合的受控对比；鲁棒性 |
| [JailWAM：世界动作模型的越狱攻击与评测框架](https://arxiv.org/abs/2604.05498) | 2026 | arXiv 预印本 (arXiv:2604.05 | 使用 | 三级安全分类框架；越狱攻击成功率与物理危害 |
| [TAPDreamer：面向世界动作模型的可迁移对抗补丁](https://arxiv.org/abs/2610.06814) | 2026 | arXiv 预印本 (arXiv:2610.06 | 使用 | 仅用公开编码器、无需查询目标策略；跨任务与跨动作架构迁移 |
| [RoboTwin：生成式数字孪生的双臂机器人基准](arXiv:2412.02960) | 2025 | CVPR 2025（IEEE/CVF 计算机视觉 | **提出** | 生成式数字孪生；双臂协同任务与真机迁移 |
| [dWorldEval：离散扩散世界模型驱动的可扩展策略评测](https://arxiv.org/abs/2604.22152) | 2026 | arXiv 预印本 (arXiv:2604.22 | 使用 | 离散扩散世界模型；视觉/语言/动作统一 token 空间 |

## 4. 关键结论与改进方向

**关键结论**：生成式资产是解决场景多样性瓶颈的可行路径；双臂任务对协调性的要求暴露了单臂基准看不到的失败模式。

**论文提到的改进方向**：①把双臂协调性作为独立指标；②生成的数字孪生需做真机一致性校验；③已被多篇安全基准复用为场景底座（Trap-RoboTwin、ForesightSafety-VLA）。

## 5. 相关论文（均来自本调研表）

- TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes（2026，arXiv 预印本 (arXiv:2608.26578)）
- Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?（2026，arXiv 预印本 (arXiv:2610.09170)）
- Memorize, Adapt, Ignore: Diagnosing Robot Learning Mechanisms under Training Data Variation（2026，arXiv 预印本 (arXiv:2609.38401)）
- What Visual Representations Do World Action Models Need?（2026，arXiv 预印本 (arXiv:2610.13024)）
- JailWAM: Jailbreaking World Action Models in Robot Control（2026，arXiv 预印本 (arXiv:2604.05498)）
- TAPDreamer: Transferable Adversarial Patches for World Action Models（2026，arXiv 预印本 (arXiv:2610.06814)）
- RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins（2025，CVPR 2025（IEEE/CVF 计算机视觉与模式识别会议））  ← **提出**
- dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model（2026，arXiv 预印本 (arXiv:2604.22152)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
