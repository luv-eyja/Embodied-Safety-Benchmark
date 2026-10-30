# LIBERO-Plus

> **所属环节**：感知 + 状态（分布偏移下的动作控制）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 10 篇（提出者 1 篇，使用者 9 篇）

## 1. 测什么问题（内容与所测环节）

VLA 在 LIBERO 上报出很高的成功率，但这些数字可能掩盖鲁棒性的根本弱点。

## 2. 怎么构建的

在 **7 个维度**引入受控扰动：物体布局、相机视角、机器人初始状态、语言指令、光照条件、背景纹理、传感器噪声；对多个 SOTA 模型逐维评测。

## 3. 用这个基准测了什么

多个 SOTA VLA。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [LIBERO-Plus：VLA 七维扰动鲁棒性分析](https://arxiv.org/abs/2510.13626) | 2025 | arXiv 预印本 (arXiv:2510.13 | **提出** | 7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声 |
| [VLA-GAUGE：泛化与鲁棒性统一诊断框架](https://arxiv.org/abs/2610.16567) | 2026 | arXiv 预印本 (arXiv:2610.16 | 使用 | 6 个能力套件的 ID/OOD 配对任务；单因子敏感度 + 组合扰动；诊断驱动改进 |
| [IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测](https://arxiv.org/abs/2609.25562) | 2026 | arXiv 预印本 (arXiv:2609.25 | 使用 | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 |
| [VLA-Retain：视觉微调的跨维度影响基准](https://arxiv.org/abs/2610.27698) | 2026 | arXiv 预印本 (arXiv:2610.27 | 使用 | 目标维度增益与目标外鲁棒性变化（分离遗忘与适配效应） |
| [只有成功率够吗：扰动下 VLA 的行为鲁棒性度量](https://arxiv.org/abs/2610.01351) | 2026 | arXiv 预印本 (arXiv:2610.01 | 使用 | 行为指标：运动平滑度、效率、夹爪行为及其变异性 |
| [MINERVA：LIBERO 的任务容量下限](https://arxiv.org/abs/2609.03715) | 2026 | arXiv 预印本 (arXiv:2609.03 | 使用 | 参数规模—成功率曲线；架构/训练/推理因素消融 |
| [量化 VLA 的分布外鲁棒性：从「保性能」到「保泛化」](https://arxiv.org/abs/2610.05745) | 2026 | arXiv 预印本 (arXiv:2610.05 | 使用 | 分布内性能 vs 环境扰动下的鲁棒性/泛化；动作偏差的状态分布 |
| [VLA 后训练中图像增广的正确用法](https://arxiv.org/abs/2610.05994) | 2026 | arXiv 预印本 (arXiv:2610.05 | 使用 | 分布外（OOD）成功率；actor 与 critic 分别增广的对照 |
| [什么让 VLA 更高效：动作头、规模与延迟的受控评测](https://arxiv.org/abs/2609.13984) | 2026 | arXiv 预印本 (arXiv:2609.13 | 使用 | 动作头设计 × 模块规模，每种配置配实测端侧延迟 |
| [推理何时真正帮助动作：CoT 的可纠正性与可行动性](https://arxiv.org/abs/2610.00601) | 2026 | arXiv 预印本 (arXiv:2610.00 | 使用 | 两个评测轴：correctability / actionability；TRUST 价值模型 |

## 4. 关键结论与改进方向

**关键结论**：①模型对扰动极其敏感：**相机视角与初始状态的轻微扰动即可让成功率从约 95% 掉到 30% 以下**；②模型对语言变化**基本不敏感**，进一步实验表明它们倾向于**忽略指令**。

**论文提到的改进方向**：①评测必须逐维报告，聚合分掩盖崩溃点；②视角与初始状态的鲁棒性是当前最大短板；③语言被忽略说明需要强制语言接地的训练目标。

## 5. 相关论文（均来自本调研表）

- LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models（2025，arXiv 预印本 (arXiv:2510.13626)）  ← **提出**
- VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models（2026，arXiv 预印本 (arXiv:2610.16567)）
- IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models（2026，arXiv 预印本 (arXiv:2609.25562)）
- VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs（2026，arXiv 预印本 (arXiv:2610.27698)）
- Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks（2026，arXiv 预印本 (arXiv:2610.01351)）
- MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?（2026，arXiv 预印本 (arXiv:2609.03715)）
- Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning（2026，arXiv 预印本 (arXiv:2610.05745)）
- How (and How Not) to Use Data Augmentation in VLA Post-Training（2026，arXiv 预印本 (arXiv:2610.05994)）
- What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency（2026，arXiv 预印本 (arXiv:2609.13984)）
- When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies（2026，arXiv 预印本 (arXiv:2610.00601)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
