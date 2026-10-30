# Open X-Embodiment

> **所属环节**：跨本体真机数据  
> **分类**：VLA 能力  
> **关联论文**：本表 1 篇（提出者 0 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：跨本体真机数据。

以「可扩展的机器人数据」回应通用操作的真机挑战：AgiBot World 是含 100 万余条轨迹、217 个任务、5 类部署场景的大规模平台，数据规模比既有数据集高一个数量级；标准化采集流水线配合人在环校验保证质量与分布多样性，并可从夹爪扩展到灵巧手与视触觉传感器以获取细粒度技能。在数据之上提出通用策略 Genie Operator-1（GO-1）。

信息取自表内论文 *AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量。

## 3. 用这个基准测了什么

**被测对象**：通用操作策略（GO-1 等）。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [AgiBot World Colosseo：百万轨迹级操作平台](https://doi.org/10.1109/IROS60139.2025.11247088) | 2025 | IROS 2025（IEEE/RSJ 智能机器人 | 使用 | 100 万+ 轨迹 / 217 个任务 / 5 类部署场景；数据规模与质量 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **AgiBot World Colosseo：百万轨迹级操作平台**（2025）：在数据之上提出通用策略 Genie Operator-1（GO-1）。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems（2025，IROS 2025（IEEE/RSJ 智能机器人与系统国际会议））

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
