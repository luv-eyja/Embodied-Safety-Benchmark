# Trap-LIBERO / Trap-RoboTwin

> **所属环节**：配置化失败后门  
> **分类**：VLA 安全  
> **关联论文**：本表 1 篇（提出者 0 篇，使用者 1 篇）

## 1. 测什么问题（内容与所测环节）

**定位**：配置化失败后门。

提出 Configured Failure Trapping 这一新的后门攻击任务：以隐秘文本触发器激活，并要求攻击者控制「如何失败」（如以指定位置偏移抓取），比以往「任何失败即算成功」的后门评测更严格也更难检测。为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。

信息取自表内论文 *TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes*（该基准的原始提出论文未单独收录于本表，此处依据使用它的论文转述）。

## 2. 怎么构建的

构建要点与评测设计（据原文摘要整理）：配置失败保真度（如何失败）而非仅是否失败；四种失败模式。

## 3. 用这个基准测了什么

**被测对象**：VLA 模型。

下表按论文列出：

| 论文 | 年 | 来源 | 角色 | 用途/发现 |
|---|---|---|---|---|
| [Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准](https://arxiv.org/abs/2608.26578) | 2026 | arXiv 预印本 (arXiv:2608.26 | 使用 | 配置失败保真度（如何失败）而非仅是否失败；四种失败模式 |

## 4. 关键结论与改进方向

**关键结论**（按使用该基准的论文逐条汇总）：

- **Trap-LIBERO / Trap-RoboTwin：配置化失败后门基准**（2026）：为此构建 Trap-LIBERO 与 Trap-RoboTwin 两个基准，覆盖四种代表性失败模式，并提供配置失败保真度的自动评测套件。

**改进方向**：上表各论文在使用该基准时指出的短板即为可行改进方向；本表未做统一归纳。

## 5. 相关论文（均来自本调研表）

- TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes（2026，arXiv 预印本 (arXiv:2608.26578)）

---

*文档由 `scripts/build_benchmark_docs.py` 依据调研表自动生成；第 1、2、4 节的人工解读基于论文摘要，未逐篇精读全文。*
