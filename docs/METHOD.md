# 方法与数据说明

## 1. 数据来源

主表有两类来源，在「收录来源」列逐条标出。

### 1.1 论文库（163 篇）

目标页面 `screened.html` 由三个层级的数据组成，已全部纳入检索：

| 层级 | 文件 | 篇数 | 页面声明 | 本表标记 |
|---|---|---|---|---|
| curated | `papers.json` | 594 | 作者人工筛选后的正式目录 | 本论文库（人工精选目录） |
| audited | `audited.json` | 157 | 作者复核过作者与元数据 | 本论文库（作者复核） |
| screened | `screened.json` | 1,882 | 机器自动筛出的每日 arXiv 增量，**未经人工审核** | 本论文库（自动筛查） |

去重后合计 2,633 篇。

### 1.2 库外补充（29 篇）

通过 OpenAlex 检索 + arXiv 摘要页核实补充，覆盖三类：

1. **VLA 时代的评测新基准**：VLA-Arena、SafeVLA-Bench、ForesightSafety-VLA、ManiGuard、RoboEval、RoboChrono、RoboVista、HUGE-Bench
2. **用世界模型/仿真替代真机 rollout 的评测方法论**：WorldEval、dWorldEval、RoboWorld、PolaRiS、主动因子评测
3. **VLA 评测依赖的经典底座与安全基线**：LIBERO、CALVIN、SimplerEnv、RoboCasa、RoboTwin、VLABench、COLOSSEUM、RoboMIND、ManiSkill2、AgiBot World、RoboPAIR、BadRobot

## 2. 筛选口径

### 2.1 纳入标准（满足其一）

- **A** 提出面向 VLA / 视觉-语言-条件策略的 benchmark、测试床、评测协议或度量体系
- **B** 对 VLA 的能力、鲁棒性、安全性做系统性实证评估（含诊断性研究与失败模式分析）——**即便没有提出新 benchmark**，只要贡献主体是「测出 VLA 在某方面如何失效/为何失效」，即纳入
- **C** 面向 VLA 所在技术栈（VLM 规划器 + 底层策略）的具身智能体安全基准
- **D** 攻击/防御工作**自带统一评测框架或新基准**（纯单点攻击方法不收）
- **E** 非 VLA 但属于具身安全/鲁棒性的基准（自动驾驶、多机器人、人机协作、UAV、工控等）

### 2.2 排除标准

- 与具身评测无关的感知/建图/SLAM/纯自动驾驶规控论文
- 仅提出训练或对齐方法、不涉及评测协议的工作
- 纯语言/文本智能体、纯 web/移动端的软件 agent 安全基准

> 关键一点：**筛选不要求标题或摘要里出现 "benchmark" / "evaluation"**。例如 *Are VLA Models Robust to One-Step Observation Perturbations?* 标题无 benchmark 字样，但整篇在做 VLA 鲁棒性评测，同样收录。

## 3. 基准归属的判定

`scripts/bench_registry.py` 用正则匹配「标题 + 摘要」中的基准名，得到「基准 → 论文」映射。

**这是下界**：一篇论文用到的基准若只在实验章节出现、摘要未提，会被漏计。因此文档里「使用者 N 篇」应理解为「至少 N 篇」。

## 4. 文档生成

`scripts/build_benchmark_docs.py` 为 121 个基准各生成一份 Markdown。其中 15 个核心基准（LIBERO 族、RoboTwin、CALVIN、SimplerEnv、COLOSSEUM 等）的第 1/2/4 节由人工依据摘要撰写；其余基准由脚本按论文自身的「评测维度」「内容概要」组装，避免虚构细节。

## 5. 已验证与未验证

**已验证**
- 全部 arXiv 编号逐条与 arXiv 摘要页标题比对：131 条中 125 条逐字一致；6 条差异为 HTML 转义符（2）、已改用出版社 DOI（2）、标题介词差异（1）、DOI 字符串（1）
- 全部 192 行链接均为 `arxiv.org` 或 `doi.org`，无裸编号
- 会议/期刊条目（NeurIPS、ICLR、ICCV、CVPR、AAAI、EMNLP、ICRA、IROS、RSS、RA-L）均带正式 DOI
- Excel 文件用 Excel 16.0 实际打开验证，无修复提示；下拉与条件格式生效

**未验证**
- 未精读全文：概要依据摘要撰写，指标数字取自摘要自述，未逐一复核实验表格
- 2026 年条目多数只有 arXiv，是否已被会议接收无法核实
- 未穷尽：论文库是每日增量 + 人工筛选，2026 年条目仍在快速增长；外网检索仅覆盖 OpenAlex 与 arXiv 的可检索面
