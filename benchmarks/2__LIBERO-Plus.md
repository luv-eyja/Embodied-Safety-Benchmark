# LIBERO-Plus

> **所属环节**：感知 + 状态（分布偏移下的动作控制）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 10 篇（提出者 1 篇，使用者 9 篇）
> **证据级别**：A（人工扩写字段 + 表内摘要；未逐篇精读全文）

> **项目地址审计**：`not_found`；未查到可确认的官方项目地址（详见 [项目地址审计](../analysis/benchmark-project-audit.md)）

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models |
| 年份 | 2025、2026 |
| 数据来源 | 本论文库 |
| 论文库分区 | Action and Interaction › Robot Control |
| 应用领域 | 未标注 |
| 被测对象 | 多个 SOTA VLA。 |
| 关注属性 | 语义/指令安全、物理/接触安全、分布偏移鲁棒性、失败恢复、实时/治理、任务能力 |
| 评测维度/指标 | 7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声 |
| 基础平台线索 | LIBERO |
| 规模线索 | 6 个能力套件的 ID/OOD 配对任务；6 个能力套件的分布内/分布外配对任务；4 个任务套件、3 个 VLA、7 种扰动条件；0.54M 参数策略在 4 个标准套件、2000 次 rollout |
| 执行环境线索 | 摘要提到仿真/模拟环境。 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：VLA 在 LIBERO 上报出很高的成功率，但这些数字可能掩盖鲁棒性的根本弱点。

**主要测量维度**：7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声。

## 2. 怎么构建的

### 2.1 构建要素

| 要素 | 摘要级记录 |
|---|---|
| 基础平台 | LIBERO |
| 任务/场景规模 | 6 个能力套件的 ID/OOD 配对任务；6 个能力套件的分布内/分布外配对任务；4 个任务套件、3 个 VLA、7 种扰动条件；0.54M 参数策略在 4 个标准套件、2000 次 rollout |
| 扰动、风险或约束 | 7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声 |
| 对照/配对方式 | 摘要提到配对、孪生或受控对照。 |
| 指标与判分线索 | 7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声 |
| 执行设置 | 摘要提到仿真/模拟环境。 |

### 2.2 详细说明

在 **7 个维度**引入受控扰动：物体布局、相机视角、机器人初始状态、语言指令、光照条件、背景纹理、传感器噪声；对多个 SOTA 模型逐维评测。

## 3. 用这个基准测了什么

**被测对象**：多个 SOTA VLA。

**结果应如何读取**：先按“评测维度/指标”字段区分主指标、辅助指标和对照条件；若论文同时报告任务成功与安全/鲁棒性结果，应将二者分开阅读。

下表按论文列出；“摘要级发现”保留调研表中的概要，不等同于全文实验结论。

| 论文 | 年份 / 来源 | 角色 | 被测对象 | 使用方式 / 指标 | 摘要级发现 |
|---|---|---|---|---|---|
| [LIBERO-Plus：VLA 七维扰动鲁棒性分析](https://arxiv.org/abs/2510.13626) | 2025 / arXiv 预印本 (arXiv:2510.13626) | **提出** | VLA 基础模型（多个 SOTA） | 7 维扰动：物体布局、相机视角、初始状态、语言指令、光照、背景纹理、传感器噪声 | 对多个 SOTA VLA 施加受控扰动做系统脆弱性分析，揭示「表面胜任」下的脆弱：相机视角与机器人初始状态轻微扰动即可使成功率从约 95% 跌至 30% 以下，而模型对语言变化反而不敏感（进一步实验表明模型倾向忽略指令）。是当前最常被复用的 VLA 鲁棒性诊断基准之一。 |
| [VLA-GAUGE：泛化与鲁棒性统一诊断框架](https://arxiv.org/abs/2610.16567) | 2026 / arXiv 预印本 (arXiv:2610.16567) | 使用 | 12 个不同规模/动作建模范式的 VLA | 6 个能力套件的 ID/OOD 配对任务；单因子敏感度 + 组合扰动；诊断驱动改进 | 把零样本泛化与扰动鲁棒性放进同一可执行任务表示下评测：用 6 个能力套件的分布内/分布外配对任务、单因子敏感度分析与组合扰动筛选、以及由诊断结果驱动的定向数据增强与微调，形成「诊断—改进」闭环；在统一协议下评测 12 个不同模型规模与动作建模范式的 VLA。 |
| [IndustrialVLA-Bench：VLA 与 WAM 的多轴可追溯评测](https://arxiv.org/abs/2609.25562) | 2026 / arXiv 预印本 (arXiv:2609.25562) | 使用 | 6 个已发布的 VLA 与世界动作模型（WAM） | 干净能力（LIBERO）/ 非语言鲁棒性（LIBERO-Plus）/ 指令敏感度（LIBERO-Para）/ 执行代价 | VLA 与世界动作模型两条技术路线常在各自不同的评测协议下报告结果，难以比较能力、鲁棒性、语言敏感性与部署成本。 |
| [VLA-Retain：视觉微调的跨维度影响基准](https://arxiv.org/abs/2610.27698) | 2026 / arXiv 预印本 (arXiv:2610.27698) | 使用 | 5 个开源 VLA 及其微调检查点 | 目标维度增益与目标外鲁棒性变化（分离遗忘与适配效应） | 针对「在目标域数据上微调视觉模块」这一常见做法，考察其在目标条件之外如何影响鲁棒性——既有鲁棒性基准只评测未微调模型，适配研究又只报告目标增益。 |
| [只有成功率够吗：扰动下 VLA 的行为鲁棒性度量](https://arxiv.org/abs/2610.01351) | 2026 / arXiv 预印本 (arXiv:2610.01351) | 使用 | 3 个 SOTA VLA；LIBERO / LIBERO-Plus | 行为指标：运动平滑度、效率、夹爪行为及其变异性 | 指出鲁棒性仍主要用任务成功率（TSR）衡量。该工作提出与基准无关的行为鲁棒性评测框架，刻画成功轨迹在扰动下「如何被执行」，包括运动平滑度、效率与夹爪行为等指标； |
| [MINERVA：LIBERO 的任务容量下限](https://arxiv.org/abs/2609.03715) | 2026 / arXiv 预印本 (arXiv:2609.03715) | 使用 | 刻意精简的视觉运动策略 vs 十亿参数 VLA | 参数规模—成功率曲线；架构/训练/推理因素消融 | 用一个刻意精简的策略族测量 LIBERO 实际需要的模型容量：0.54M 参数策略在 4 个标准套件、2000 次 rollout 上取得 95.1% 平均成功率，仅比报告中的 LeRobot π0.5 低 2.4 个点（参数少 7700 倍），性能约在 1M 参数处饱和、低于 0.25M 崩溃。 |
| [量化 VLA 的分布外鲁棒性：从「保性能」到「保泛化」](https://arxiv.org/abs/2610.05745) | 2026 / arXiv 预印本 (arXiv:2610.05745) | 使用 | 训练后量化的 VLA 策略 | 分布内性能 vs 环境扰动下的鲁棒性/泛化；动作偏差的状态分布 | 指出训练后量化在标准评测条件下能保住 VLA 性能，但能否保住全精度模型的鲁棒性与泛化此前未被研究。作者系统考察量化策略在环境扰动下的表现：量化后分布内性能相近，却对细微环境变化变脆弱；动作偏差集中在少数 rollout 状态上，且教师指导在高偏差状态改善泛化、在低偏差状态反而有害。 |
| [VLA 后训练中图像增广的正确用法](https://arxiv.org/abs/2610.05994) | 2026 / arXiv 预印本 (arXiv:2610.05994) | 使用 | π0.5、GR00T N1.5（LIBERO-Plus） | 分布外（OOD）成功率；actor 与 critic 分别增广的对照 | 系统研究图像增广在 VLA 强化学习后训练中的作用，给出一个反直觉结论：关键在于只对 critic 模块增广，而 actor 的输入在 rollout 与更新时都保持干净。对 π0.5 与 GR00T N1.5，这分别把 LIBERO-Plus 上的 OOD 成功率提升 7.8 与 10.0 个点； |
| [什么让 VLA 更高效：动作头、规模与延迟的受控评测](https://arxiv.org/abs/2609.13984) | 2026 / arXiv 预印本 (arXiv:2609.13984) | 使用 | 固定主干（SigLIP2 / Qwen2.5）下的 VLA 配置网格 | 动作头设计 × 模块规模，每种配置配实测端侧延迟 | 在固定主干与训练流水线、并把每种配置与实测端侧延迟配对的前提下扫描动作头设计与模块规模，得到三点结论：动作头性能主要由初始化决定（把语言主干最后几层 transformer 复制进头部是收益最大的单一杠杆，且不增加延迟），而非解码器架构、损失函数或推理预算； |
| [推理何时真正帮助动作：CoT 的可纠正性与可行动性](https://arxiv.org/abs/2610.00601) | 2026 / arXiv 预印本 (arXiv:2610.00601) | 使用 | 推理型 VLA 策略 | 两个评测轴：correctability / actionability；TRUST 价值模型 | 推理型 VLA 会输出看似解释并引导动作的思维链，这被设想为运行时安全的接口。作者把这一设想落成两个可操作的评测轴：可纠正性（不可靠推理能否在生成过程中被检测并改进）与可行动性（对推理的纠正能否产生朝预期方向的行为改变）。 |

## 4. 关键结论、改进方向与可复用性

**关键结论**：①模型对扰动极其敏感：**相机视角与初始状态的轻微扰动即可让成功率从约 95% 掉到 30% 以下**；②模型对语言变化**基本不敏感**，进一步实验表明它们倾向于**忽略指令**。

**论文提到的改进方向**：①评测必须逐维报告，聚合分掩盖崩溃点；②视角与初始状态的鲁棒性是当前最大短板；③语言被忽略说明需要强制语言接地的训练目标。

**复用状态**：已有至少一篇后续论文使用，具备初步跨论文证据。

## 5. 相关论文（均来自本调研表）

- [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)（2025，arXiv 预印本 (arXiv:2510.13626)）  ← **提出**
- [VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2610.16567)（2026，arXiv 预印本 (arXiv:2610.16567)）
- [IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models](https://arxiv.org/abs/2609.25562)（2026，arXiv 预印本 (arXiv:2609.25562)）
- [VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs](https://arxiv.org/abs/2610.27698)（2026，arXiv 预印本 (arXiv:2610.27698)）
- [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351)（2026，arXiv 预印本 (arXiv:2610.01351)）
- [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715)（2026，arXiv 预印本 (arXiv:2609.03715)）
- [Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning](https://arxiv.org/abs/2610.05745)（2026，arXiv 预印本 (arXiv:2610.05745)）
- [How (and How Not) to Use Data Augmentation in VLA Post-Training](https://arxiv.org/abs/2610.05994)（2026，arXiv 预印本 (arXiv:2610.05994)）
- [What Makes an Efficient VLA? Navigating Action-Head Design, Scaling, and Latency](https://arxiv.org/abs/2609.13984)（2026，arXiv 预印本 (arXiv:2609.13984)）
- [When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies](https://arxiv.org/abs/2610.00601)（2026，arXiv 预印本 (arXiv:2610.00601)）

## 6. 证据边界与复核建议

- **证据级别**：A（人工扩写字段 + 表内摘要；未逐篇精读全文）。
- **主要来源**：[LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models](https://arxiv.org/abs/2510.13626)。
- **当前限制**：本文档基于调研表、论文摘要和少量人工整理；核心条目另有本地全文核查补录，但仍未替代对全文实验表格、附录、代码仓库和数据下载说明的逐项复核。
- **建议复核**：优先确认任务/场景划分、样本规模、指标公式、判分阈值、模型清单，以及仿真与真机设置是否一致。

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成。 A 级文档含人工扩写字段；核心条目附本地全文核查补录；B/C 级文档主要依赖摘要级结构化记录。*
