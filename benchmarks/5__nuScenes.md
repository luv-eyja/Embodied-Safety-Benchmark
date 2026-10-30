# nuScenes

> **所属环节**：真实驾驶数据集（开环）  
> **分类**：具身安全  
> **关联论文**：本表 3 篇（提出者 0 篇，使用者 3 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：真实驾驶数据集（开环）。

指出排行榜名次只报告结果、不报告行为，因而难以预测策略在新地点的表现：nuScenes 开环误差或 NAVSIM 排名并不迁移到「新地点且行人位于自车走廊附近」的场景。提出反事实体检——数百帧真实画面各做两种编辑（移除行人、夜间重打光）并由独立检测器验证，把规划轨迹的变化当作诊断量而非分数，并从中读出两个因果轴、构造五项「考试」以分离被单一分数合并的行为差异。

信息取自表内论文 *Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化。

## 3. 用这个基准测了什么

**被测对象**：6 个已发布的端到端/VLA 驾驶策略。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [超越排行榜：域偏移下驾驶策略的反事实诊断](https://arxiv.org/abs/2609.22582) | 2026 | arXiv 预印本 (arXiv:2609.22 | 使用 | nuScenes 开环误差与 NAVSIM 排行榜名次 vs 反事实编辑下的轨迹变化 |
| [DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准](https://arxiv.org/abs/2608.29005) | 2026 | arXiv 预印本 (arXiv:2608.29 | 使用 | 16 类退化 × 5 个严重度；nuScenes/NAVSIM 开环 + CARLA 闭环锚点 |
| [ExceptionDrive：面向规划的反事实边角案例基准](https://arxiv.org/abs/2609.37871) | 2026 | arXiv 预印本 (arXiv:2609.37 | 使用 | 21 个任务 / 6 个安全族；无参考评测协议（UR/HCC/HPR） |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **超越排行榜：域偏移下驾驶策略的反事实诊断**（2026）：提出反事实体检——数百帧真实画面各做两种编辑（移除行人、夜间重打光）并由独立检测器验证，把规划轨迹的变化当作诊断量而非分数，并从中读出两个因果轴、构造五项「考试」以分离被单一分数合并的行为差异。
- **DriveDegrade：纯视觉端到端驾驶的图像退化容忍度基准**（2026）：基准把 16 类退化在 5 个严重度下于图像加载器内即时注入，单一算子即可触达 15 个策略。
- **ExceptionDrive：面向规划的反事实边角案例基准**（2026）：由于插入危险会使记录的人类轨迹失效，采用无参考协议，用不安全率（UR）、危险避让合规（HCC）、危险接近响应（HPR）等指标评估编辑后的预测。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift（2026，arXiv 预印本 (arXiv:2609.22582)）
- A Degradation-Tolerance Benchmark for Camera-Only End-to-End Driving（2026，arXiv 预印本 (arXiv:2608.29005)）
- ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving（2026，arXiv 预印本 (arXiv:2609.37871)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
