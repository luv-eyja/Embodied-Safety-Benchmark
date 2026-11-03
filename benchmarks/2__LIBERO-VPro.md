# LIBERO-VPro

<!-- survey-classification:start -->
> **统一调研分类**：评测任务集；直接具身评测；目标：鲁棒性。
> **分类依据**：视觉信息可靠性诊断，不据成功率直接认定安全。
> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。
<!-- survey-classification:end -->

> **所属环节**：感知（执行期视觉证据）  
> **分类**：VLA 鲁棒性  
> **关联论文**：本表 1 篇（提出 1、使用 0；方法参考另标）
> **证据级别**：原表 A；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）

> **项目地址审计**：`found`；[https://huiqiongli.github.io/LIBERO-VPro](https://huiqiongli.github.io/LIBERO-VPro)

## 0. 评测卡片

| 字段 | 当前整理结果 |
|---|---|
| 首发/代表论文 | LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models |
| 年份 | 2026（所读来源首次 arXiv 提交年） |
| 数据来源 | 本论文库 |
| 论文库分区 | Perception › Visual Perception |
| 应用领域 | 未标注 |
| 被测对象 | 闭环视觉鲁棒性 |
| 历史关键词标签（未重新统计） | 分布偏移鲁棒性、实时/治理 |
| 评测维度/指标 | 视觉证据退化 / 相机陈旧 / 视觉源一致性 / 任务相关场景变化；12 类挑战 96 种设置 |
| 基础平台线索 | LIBERO、Franka |
| 规模线索 | 视觉退化、相机过时、信息源一致性、任务场景变化四维，12 类、96 设置、3,296 用例；约 19.6 万仿真 rollout，并有 200 次 FR3 真机测试。 |
| 执行环境线索 | 闭环视觉鲁棒性 |
| 全文状态 | 已核查本地全文：`docs/_fulltext/LIBERO-VPro.txt` |
| OpenAlex 引用快照 | [0](https://openalex.org/W7214051566)；2026-11-03 |

## 1. 测什么问题（内容与所测环节）

**核心问题**：模型是否依赖当前、可信且与任务相关的视觉反馈，世界模型预测会不会偏离现实？

**评测层级**：闭环视觉鲁棒性。

## 2. 怎么构建的

**核心场景与条目**：视觉退化、相机过时、信息源一致性、任务场景变化四维，12 类、96 设置、3,296 用例；约 19.6 万仿真 rollout，并有 200 次 FR3 真机测试。

**实现与判分**：在闭环执行中控制遮挡位置、观察时效、多视角矛盾与场景变化；对比三种 VLA、三种 WAM，并检查目标区域与局部交互线索的不同作用。

## 3. 用这个基准测了什么

下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。

| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |
|---|---|---|---|---|
| [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](https://arxiv.org/abs/2609.24350) | 2026 | 提出 | 视觉证据退化 / 相机陈旧 / 视觉源一致性 / 任务相关场景变化；12 类挑战 96 种设置 | 标准基准默认执行过程中视觉观测干净、及时且一致，该基准专门扰动执行期的视觉证据：覆盖视觉证据退化、相机帧陈旧（staleness）、视觉源一致性与任务相关场景变化四个维度，共 12 类挑战、96 种设置、3296 个任务-条件案例，约 19.6 万仿真回合并辅以 200 次 Franka Research 3 真机 rollout。 |

## 4. 关键结论、改进方向与可复用性

**原论文结果与成果**：高标准成功率不保证视觉鲁棒性；目标被遮挡时仍成功不能直接证明模型理解了目标，局部交互线索的缺失可能更致命。WAM 的预测质量与实际执行也可能脱节。

**适用边界**：3,296 是评测配置数，不是独立任务数。模拟与真机规模不同，必须分别解释；观察异常下的失败不能一概归因为语言理解。

## 5. 相关论文（均来自本调研表）

- [LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models](https://arxiv.org/abs/2609.24350)（2026；提出）

## 6. 证据边界与复核建议

### 6.1 全文核查补录（核心论文）

> 以下内容来自仓库外置的本地全文材料，作为摘要级整理的定量补充；数字和结论仍应以论文原表、附录和代码为最终依据。

**来源文件**：`docs/_fulltext/LIBERO-VPro.txt`。

**评测协议**：四个挑战维度为视觉证据退化、相机陈旧、视觉源一致性和任务相关场景变化，细分 12 类挑战、96 种设置、3,296 个任务-条件案例；覆盖四套 LIBERO 的 40 个任务，六个模型（3 个 VLA、3 个 WAM），每个案例 10 trials，约 196,000 个仿真 episodes。另在 Franka Research 3 上进行 200 次真机 rollout。

**定量证据**：视觉证据退化包含目标/容器遮挡比例 25/50/75/100% 与四种时序、交互线索遮挡、短时 blackout/noise 和视角不可用；相机陈旧包含 3 档固定延迟、冻结和历史回放；一致性包含跨视角矛盾和预测-现实分歧；场景变化包含 distractor、前置条件变化、视觉歧义以及 Taper/Multipeak/Twist/Asymmetric 几何。LingBot 的递归自预测总体成功率由 97.0 降至 53.8，Long 套件由 98 降至 22。

**全文结论**：交互线索遮挡通常比目标物体遮挡更致命；第三视角/腕部视角缺失和陈旧观测会造成严重退化；目标熟悉位置出现空间 distractor 可使多模型成功率崩溃，真实前置条件变化比单纯视觉歧义更难。真机在缺失视角、跨视角矛盾下接近全面失败，陈旧度的影响则依任务而变。

**适用边界**：真机只覆盖 Pick-and-Place 与 Move 两类任务；WAM 与 VLA 的观测接口不同，横向比较应按模型类别和具体设置分别解释。

本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。

3,296 是评测配置数，不是独立任务数。模拟与真机规模不同，必须分别解释；观察异常下的失败不能一概归因为语言理解。

<!-- paper-review:start -->
## 7. 原始来源、引用量与可复用成果（2026-11-03）

**本次核查来源**：[1] Huiqiong Li, Zhiting Mei, Anirudha Majumdar, et al., ‘LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models,’ arXiv preprint, 2026, arXiv:2609.24350v1. [论文](https://arxiv.org/abs/2609.24350)；[核查正文](https://arxiv.org/html/2609.24350v1)。

**重点核查位置（章节主题）**：Benchmark Construction；Evaluation Protocol；Main Results；Real-world Experiments。

OpenAlex 被引次数：**[0](https://openalex.org/W7214051566)**；观测日期：2026-11-03。后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。

**项目与成果入口**：[https://huiqiongli.github.io/LIBERO-VPro](https://huiqiongli.github.io/LIBERO-VPro)。地址状态为 `found`；找到页面不等于已验证安装、数据下载和复现。

**后续使用证据**：原表内有 0 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。

完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。
<!-- paper-review:end -->
