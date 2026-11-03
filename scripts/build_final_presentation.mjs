import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const require = createRequire(import.meta.url);
const pptxgen = require('pptxgenjs');

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const data = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_survey.json'), 'utf8'));
const registry = JSON.parse(await fs.readFile(path.join(ROOT, 'data/survey_paper_registry.json'), 'utf8'));
const entries = data.entries.filter((e) => e.focus === 'active');
const benchmarks = entries.filter((e) => e.primary_type === 'benchmark');
const stats = data.statistics;

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Embodied Safety Benchmark Survey';
pptx.subject = '具身智能及安全 Benchmark 调研汇报';
pptx.title = '具身智能及安全 Benchmark 调研汇报';
pptx.company = 'Embodied Safety Benchmark';
pptx.lang = 'zh-CN';
pptx.theme = {
  headFontFace: 'Microsoft YaHei',
  bodyFontFace: 'Microsoft YaHei',
  lang: 'zh-CN',
};

const C = {
  navy: '16324F',
  ink: '17212B',
  muted: '5B6770',
  line: 'D8E1E8',
  pale: 'F4F7F9',
  teal: '0E7490',
  aqua: '2C9EAA',
  green: '2E8B72',
  orange: 'D97706',
  red: 'B94E48',
  purple: '6B5B95',
  white: 'FFFFFF',
};
const FONT = 'Microsoft YaHei';
const W = 13.333;
const H = 7.5;

function addText(slide, text, x, y, w, h, opts = {}) {
  slide.addText(String(text), {
    x, y, w, h,
    fontFace: opts.fontFace || FONT,
    fontSize: opts.fontSize ?? 16,
    bold: opts.bold ?? false,
    color: opts.color || C.ink,
    align: opts.align || 'left',
    valign: opts.valign || 'mid',
    margin: opts.margin ?? 0,
    fit: opts.fit || 'shrink',
    breakLine: false,
    italic: opts.italic || false,
    paraSpaceAfterPt: opts.paraSpaceAfterPt,
    charSpacing: opts.charSpacing,
    transparency: opts.transparency,
  });
}

function addRect(slide, x, y, w, h, fill, radius = false, line = null) {
  slide.addShape(radius ? pptx.ShapeType.roundRect : pptx.ShapeType.rect, {
    x, y, w, h,
    rectRadius: radius ? 0.08 : undefined,
    fill: { color: fill },
    line: line ? { color: line, width: 0.8 } : { color: fill, transparency: 100 },
  });
}

function addLine(slide, x1, y1, x2, y2, color = C.line, width = 1.2, dash = 'solid') {
  slide.addShape(pptx.ShapeType.line, { x: x1, y: y1, w: x2 - x1, h: y2 - y1, line: { color, width, dashType: dash } });
}

function addTitle(slide, title, kicker = '') {
  if (kicker) addText(slide, kicker.toUpperCase(), 0.62, 0.28, 3.5, 0.22, { fontSize: 9.5, bold: true, color: C.teal, charSpacing: 1.2 });
  addText(slide, title, 0.62, 0.55, 12.1, 0.48, { fontSize: 27, bold: true, color: C.navy });
}

function addFooter(slide, n, source = '数据快照：2026-11-03；统计来自 data/benchmark_survey.json。') {
  addLine(slide, 0.62, 7.11, 12.72, 7.11, C.line, 0.7);
  addText(slide, source, 0.62, 7.18, 11.4, 0.18, { fontSize: 8.5, color: C.muted, valign: 'top' });
  addText(slide, String(n).padStart(2, '0'), 12.2, 7.16, 0.5, 0.2, { fontSize: 9, bold: true, color: C.muted, align: 'right' });
}

function newSlide(title, kicker = '', source) {
  const slide = pptx.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, title, kicker);
  slide.addNotes(`资料快照：2026-11-03。统计基于本仓库 data/benchmark_survey.json 与 data/survey_paper_registry.json。${source || ''}`);
  return slide;
}

function addCard(slide, x, y, w, h, number, label, color = C.navy, detail = '') {
  addRect(slide, x, y, w, h, C.pale, true);
  addText(slide, number, x + 0.18, y + 0.14, w - 0.36, 0.44, { fontSize: 28, bold: true, color });
  addText(slide, label, x + 0.18, y + 0.66, w - 0.36, 0.28, { fontSize: 12.5, bold: true, color: C.ink });
  if (detail) addText(slide, detail, x + 0.18, y + 0.98, w - 0.36, h - 1.08, { fontSize: 9.5, color: C.muted, valign: 'top' });
}

function addBulletList(slide, items, x, y, w, lineH = 0.34, size = 16, color = C.ink) {
  items.forEach((item, i) => {
    slide.addShape(pptx.ShapeType.ellipse, { x, y: y + i * lineH + 0.11, w: 0.08, h: 0.08, fill: { color: C.teal }, line: { color: C.teal, transparency: 100 } });
    addText(slide, item, x + 0.18, y + i * lineH, w - 0.18, lineH, { fontSize: size, color, valign: 'top' });
  });
}

function addBarChart(slide, labels, values, x, y, w, h, color = C.teal, max = null) {
  slide.addChart(pptx.ChartType.bar, [{ name: '数量', labels, values }], {
    x, y, w, h,
    catAxisLabelFontFace: FONT,
    catAxisLabelFontSize: 10,
    catAxisLabelColor: C.ink,
    catAxisLineShow: false,
    catGridLine: { style: 'none' },
    valAxisLabelFontFace: FONT,
    valAxisLabelFontSize: 9,
    valAxisLabelColor: C.muted,
    valAxisLineShow: false,
    valGridLine: { color: C.line, width: 0.8 },
    valAxisMinVal: 0,
    valAxisMaxVal: max || Math.ceil(Math.max(...values) * 1.2),
    valAxisMajorUnit: max && max > 100 ? 1000 : 10,
    showLegend: false,
    showTitle: false,
    showValue: true,
    dataLabelPosition: 'outEnd',
    dataLabelColor: C.ink,
    dataLabelFontFace: FONT,
    dataLabelFontSize: 10,
    chartColors: [color],
    border: { color: C.white, pt: 0 },
    chartArea: { fill: C.white, transparency: 100, border: { color: C.white, pt: 0 } },
    plotArea: { fill: C.white, transparency: 100, border: { color: C.white, pt: 0 } },
    barDir: 'bar',
    barGrouping: 'clustered',
    gapWidthPct: 45,
  });
}

function addDoughnut(slide, labels, values, x, y, w, h, colors) {
  slide.addChart(pptx.ChartType.doughnut, [{ name: '数量', labels, values }], {
    x, y, w, h,
    holeSize: 62,
    showLegend: true,
    legendPos: 'r',
    legendFontFace: FONT,
    legendFontSize: 11,
    legendColor: C.ink,
    showPercent: true,
    showValue: false,
    showLabel: false,
    chartColors: colors,
    dataLabelColor: C.ink,
    dataLabelFontFace: FONT,
    dataLabelFontSize: 10,
    border: { color: C.white, pt: 0 },
    chartArea: { fill: C.white, transparency: 100, border: { color: C.white, pt: 0 } },
    plotArea: { fill: C.white, transparency: 100, border: { color: C.white, pt: 0 } },
  });
}

function addPill(slide, text, x, y, w, fill = C.teal, color = C.white) {
  addRect(slide, x, y, w, 0.28, fill, true);
  addText(slide, text, x, y + 0.01, w, 0.23, { fontSize: 9.5, bold: true, color, align: 'center' });
}

function addArrow(slide, x, y, w, h, color = C.teal) {
  slide.addShape(pptx.ShapeType.chevron, { x, y, w, h, fill: { color }, line: { color, transparency: 100 } });
}

// Slide 1: cover
{
  const slide = pptx.addSlide();
  slide.background = { color: C.navy };
  addText(slide, '具身智能及安全 Benchmark 调研', 0.8, 1.25, 11.8, 0.7, { fontSize: 33, bold: true, color: C.white });
  addText(slide, '规模、场景、设计方案与安全评测建议', 0.82, 2.12, 10.8, 0.5, { fontSize: 21, color: 'D8EEF2' });
  addRect(slide, 0.82, 3.1, 2.4, 0.58, C.teal, true);
  addText(slide, '资料快照 2026-11-03', 0.82, 3.25, 2.4, 0.24, { fontSize: 12, bold: true, color: C.white, align: 'center' });
  addText(slide, '研究范围：任务能力、分布变化下的鲁棒性，以及规划和物理执行中的安全性。', 0.82, 5.95, 10.8, 0.33, { fontSize: 14, color: 'D8EEF2' });
  addText(slide, '本汇报区分“本库统计”“原论文实验结果”和“后续建议”。', 0.82, 6.38, 10.8, 0.28, { fontSize: 12, color: 'AFC7D2' });
  addText(slide, '01', 12.2, 7.16, 0.5, 0.2, { fontSize: 9, bold: true, color: 'AFC7D2', align: 'right' });
  slide.addNotes('标题页。数据与结论均来自本仓库截至 2026-11-03 的调研快照。');
}

// Slide 2: executive summary
{
  const slide = newSlide('先看结论：规模大、覆盖广，但安全证据仍偏仿真', '01 / 摘要');
  addCard(slide, 0.65, 1.35, 2.25, 1.35, '199', '当前书目记录', C.navy, '193 行初始筛选记录 + 6 个补充来源');
  addCard(slide, 3.1, 1.35, 2.25, 1.35, '122', '登记研究条目', C.teal, '其中 62 项完成重点阅读与统一分类');
  addCard(slide, 5.55, 1.35, 2.25, 1.35, '52', '评测任务集', C.orange, '另有 3 数据集、2 平台、4 框架、1 方法');
  addCard(slide, 8.0, 1.35, 2.25, 1.35, '23', '安全目标任务集', C.red, '占 52 个 benchmark 的 44.2%，目标标签可重叠');
  addCard(slide, 10.45, 1.35, 2.25, 1.35, '40', '有确认项目入口', C.green, '另有 3 个候选入口、9 个仅平台入口');
  addRect(slide, 0.65, 3.05, 12.05, 2.75, C.pale, true);
  addText(slide, '三条判断', 0.95, 3.35, 1.8, 0.28, { fontSize: 17, bold: true, color: C.navy });
  addBulletList(slide, [
    '当前样本以机械臂操作和仿真评测为主；自动驾驶、语义决策和软件代理提供了补充视角。',
    '引用量、项目入口和真实执行证据是三件不同的事：最高被引的 nuScenes 是真实驾驶数据底座，但不是安全专用基准。',
    '新安全基准仍有价值，但优先补齐“风险定义—闭环执行—后果判定—可复现资源”这条证据链，而不是只增加任务数量。',
  ], 0.98, 3.82, 11.2, 0.52, 17);
  addText(slide, '阅读提示：样本数描述本库，不代表全领域比例；未知不等于没有。', 0.95, 5.42, 11.2, 0.25, { fontSize: 11, color: C.muted, italic: true });
  addFooter(slide, 2);
}

// Slide 3: scope and counting units
{
  const slide = newSlide('统计口径：论文、条目、benchmark 是三个层次', '02 / 范围与口径');
  const xs = [0.75, 3.0, 5.25, 7.5, 9.75];
  const nums = ['193', '199', '122', '62', '52'];
  const labels = ['初始论文筛选行', '当前书目注册', '登记研究条目', '重点阅读条目', '评测任务集'];
  const desc = ['保留原始工作簿；rows.json', '补入 6 个已读来源；不按相似题名合并', '任务集、数据、平台、框架、方法', '完成章节核查与统一分类', '其中 48 个为直接具身评测任务集'];
  xs.forEach((x, i) => {
    addRect(slide, x, 1.55, 1.85, 1.35, i === 4 ? 'E8F5F7' : C.pale, true);
    addText(slide, nums[i], x, 1.78, 1.85, 0.38, { fontSize: 27, bold: true, color: i === 4 ? C.teal : C.navy, align: 'center' });
    addText(slide, labels[i], x + 0.08, 2.2, 1.69, 0.25, { fontSize: 11, bold: true, color: C.ink, align: 'center' });
    addText(slide, desc[i], x + 0.1, 2.5, 1.65, 0.29, { fontSize: 8.7, color: C.muted, align: 'center', valign: 'top' });
    if (i < xs.length - 1) addArrow(slide, x + 1.93, 2.02, 0.22, 0.28, C.aqua);
  });
  addRect(slide, 0.75, 3.45, 5.7, 2.4, C.pale, true);
  addText(slide, '重点样本构成（62 项）', 1.05, 3.78, 2.6, 0.28, { fontSize: 17, bold: true, color: C.navy });
  addBulletList(slide, [
    '评测任务集 52',
    '训练数据集 3；仿真平台 2；评测框架 4；方法论文 1',
    '直接具身评测 51，研究底座 6，软件代理邻接 5（标签可重叠）',
  ], 1.08, 4.25, 4.9, 0.48, 15);
  addRect(slide, 6.75, 3.45, 5.95, 2.4, 'FFF8EE', true);
  addText(slide, '如何读这些数字', 7.05, 3.78, 2.6, 0.28, { fontSize: 17, bold: true, color: C.orange });
  addBulletList(slide, [
    '“199 条论文记录”不等于 199 个 benchmark。',
    '“52 个评测任务集”是主要 benchmark 分母；数据、平台、框架单列。',
    '统计结果是本库样本的描述性汇总，不是全领域普查。',
  ], 7.08, 4.25, 5.1, 0.48, 15);
  addFooter(slide, 3, '来源：data/survey_paper_registry.json；data/benchmark_survey.json。');
}

// Slide 4: portfolio composition
{
  const slide = newSlide('62 项重点研究：benchmark 占主体，但支撑性资源不能混在一起', '03 / 样本结构');
  addDoughnut(slide, ['评测任务集', '训练数据集', '仿真平台', '评测框架', '方法论文'], [52, 3, 2, 4, 1], 0.7, 1.45, 5.0, 3.85, [C.teal, C.navy, C.orange, C.purple, C.red]);
  addText(slide, '主要成果类型（互斥）', 1.05, 5.42, 3.8, 0.25, { fontSize: 13, bold: true, color: C.navy, align: 'center' });
  addRect(slide, 6.1, 1.48, 6.1, 4.15, C.pale, true);
  addText(slide, '为什么要拆分类型？', 6.45, 1.83, 3.2, 0.28, { fontSize: 18, bold: true, color: C.navy });
  addBulletList(slide, [
    '任务集：定义测试实例、控制条件和评分协议，可直接回答“模型在什么条件下表现如何”。',
    '数据集：提供训练或预训练材料，不能自动等同于独立安全评测。',
    '平台：提供可交互环境和资产；同一平台上可以出现多个不同评测协议。',
    '框架／方法：组织多套任务或提出算法，不能与单一任务集直接比较分数。',
  ], 6.48, 2.35, 5.2, 0.57, 15);
  addText(slide, '研究目标标签（可重叠）：能力 49、鲁棒性 24、安全 26。', 6.48, 5.2, 5.2, 0.25, { fontSize: 12, bold: true, color: C.orange });
  addFooter(slide, 4);
}

// Slide 5: benchmark dashboard
{
  const slide = newSlide('52 个 benchmark 的可用性与证据状态', '04 / Benchmark 总览');
  addCard(slide, 0.7, 1.35, 2.55, 1.35, '51', '有引用观测记录', C.navy, '其中 13 个 OpenAlex 被引次数 > 0；38 个为 0 或未形成正向引用');
  addCard(slide, 3.45, 1.35, 2.55, 1.35, '40', '确认项目入口', C.green, '网站或仓库已找到；另有 3 个候选入口');
  addCard(slide, 6.2, 1.35, 2.55, 1.35, '23', '涉及安全目标', C.red, '52 个 benchmark 中的 44.2%；安全与能力／鲁棒性可重叠');
  addCard(slide, 8.95, 1.35, 2.55, 1.35, '15', '报告真实执行证据', C.orange, '12 execution_reported + 3 paired_validation');
  addRect(slide, 0.7, 3.05, 5.85, 2.65, C.pale, true);
  addText(slide, '项目／文档入口状态', 1.0, 3.35, 2.8, 0.25, { fontSize: 17, bold: true, color: C.navy });
  addDoughnut(slide, ['确认入口', '候选入口', '仅平台入口'], [40, 3, 9], 1.0, 3.67, 4.9, 1.72, [C.green, C.orange, C.muted]);
  addText(slide, '“找到入口”不等于已验证安装、许可证、评测器和复现条件。', 1.0, 5.34, 5.1, 0.25, { fontSize: 10.5, color: C.muted, italic: true });
  addRect(slide, 6.85, 3.05, 5.85, 2.65, 'FFF8EE', true);
  addText(slide, '真实执行证据', 7.15, 3.35, 2.6, 0.25, { fontSize: 17, bold: true, color: C.orange });
  addText(slide, '15 / 52', 7.15, 3.78, 2.0, 0.5, { fontSize: 30, bold: true, color: C.orange });
  addText(slide, 'benchmark 论文报告了真实执行或仿真—真机配对验证', 9.0, 3.88, 3.1, 0.55, { fontSize: 13, color: C.ink, valign: 'top' });
  addText(slide, '27 个 benchmark 的真实执行证据字段仍为 unknown；未知不等于没有，但不能写成已验证。', 7.15, 4.68, 5.1, 0.42, { fontSize: 11.5, color: C.muted, valign: 'top' });
  addFooter(slide, 5, '来源：data/benchmark_citation_snapshot.json；data/benchmark_project_audit.json；data/benchmark_survey.json。');
}

// Slide 6: citations
{
  const slide = newSlide('被引分布高度不均：nuScenes 是明显的头部基准', '05 / 影响力');
  const positive = benchmarks.filter((e) => (e.citation?.cited_by_count || 0) > 0).sort((a, b) => b.citation.cited_by_count - a.citation.cited_by_count);
  const top = positive.slice(0, 8);
  addBarChart(slide, top.map((e) => e.name.replace(' / ManiSkill2', '')), top.map((e) => e.citation.cited_by_count), 0.65, 1.45, 7.3, 4.95, C.teal, 8000);
  addRect(slide, 8.35, 1.55, 4.25, 4.55, C.pale, true);
  addText(slide, '如何解读引用量', 8.7, 1.93, 2.7, 0.28, { fontSize: 18, bold: true, color: C.navy });
  addBulletList(slide, [
    '13 / 52 个 benchmark 的 OpenAlex 被引次数 > 0。',
    'nuScenes 7,152 次；随后为 CALVIN 189、LIBERO 136、NAVSIM 63。',
    '引用量反映可见度和历史积累，不等于安全覆盖、实际采用或复现成功。',
    '本快照日期为 2026-11-03；新论文的 0 次可能只是时间较短。',
  ], 8.72, 2.42, 3.4, 0.6, 14.5);
  addText(slide, '正向引用基准：nuScenes、CALVIN、LIBERO、NAVSIM、RoboTwin、COLOSSEUM、ManiSkill、VLABench、BEHAVIOR-1K、Agent-SafetyBench。\n此外：SimplerEnv、SafeAgentBench、EmbodiedBench。', 0.72, 6.42, 12.0, 0.54, { fontSize: 9.7, color: C.muted, valign: 'top' });
  addFooter(slide, 6, '来源：data/benchmark_survey.json；OpenAlex 引用观测日期 2026-11-03。');
}

// Slide 7: safety coverage
{
  const slide = newSlide('安全覆盖：已有 23 个 benchmark，但覆盖目标和证据层级并不相同', '06 / 安全统计');
  addBarChart(slide, ['能力', '鲁棒性', '安全'], [40, 21, 23], 0.75, 1.55, 5.6, 3.7, C.red, 50);
  addText(slide, '52 个 benchmark 的目标标签（可重叠）', 1.0, 5.35, 4.9, 0.25, { fontSize: 12, color: C.muted, align: 'center' });
  addRect(slide, 6.8, 1.48, 5.85, 4.6, C.pale, true);
  addText(slide, '23 个安全 benchmark 主要测什么？', 7.15, 1.85, 4.8, 0.28, { fontSize: 18, bold: true, color: C.navy });
  const safetyGroups = [
    ['物理碰撞／避障／约束', 'LIBERO-Safety、SafeLIBERO、VLA-Arena、Trap-LIBERO'],
    ['对象损伤与接触后果', 'ManiPhysicsBench、RoboHarm'],
    ['语义安全与危险意图', 'ASIMOV、HazardArena、DESPITE、Agent-SafetyBench'],
    ['阶段风险与安全成功', 'SafeStage、ForesightSafety-VLA'],
    ['驾驶与系统治理', 'SafeBench、NAVSIM、VIPS、EmbodiedGovBench'],
  ];
  safetyGroups.forEach((g, i) => {
    addPill(slide, String(i + 1).padStart(2, '0'), 7.18, 2.38 + i * 0.67, 0.38, i < 2 ? C.red : C.teal);
    addText(slide, g[0], 7.72, 2.34 + i * 0.67, 2.8, 0.24, { fontSize: 13, bold: true, color: C.ink });
    addText(slide, g[1], 7.72, 2.59 + i * 0.67, 4.45, 0.22, { fontSize: 10.5, color: C.muted });
  });
  addText(slide, '核心缺口：同一 benchmark 往往只覆盖一种风险层，难以把语义判断、闭环执行和物理后果串起来。', 7.15, 5.66, 5.0, 0.25, { fontSize: 11, color: C.red, bold: true });
  addFooter(slide, 7);
}

// Slide 8: scene landscape
{
  const slide = newSlide('场景分布：机械臂操作占主导，其他具身形态仍较稀疏', '07 / 场景');
  addBarChart(slide, ['机械臂操作', '机器人语义决策', '移动操作', '软件代理', '自动驾驶', '主动感知', '灵巧操作', '工业装配'], [29, 9, 4, 4, 3, 2, 2, 2], 0.6, 1.35, 7.2, 4.95, C.navy, 35);
  addRect(slide, 8.05, 1.45, 4.55, 4.65, C.pale, true);
  addText(slide, '执行环境标签', 8.4, 1.83, 2.5, 0.28, { fontSize: 18, bold: true, color: C.navy });
  addDoughnut(slide, ['仿真', '真实机器人', '真实数据集', '软件环境', '离线／符号'], [38, 15, 6, 4, 5], 8.25, 2.2, 3.95, 2.65, [C.teal, C.orange, C.green, C.purple, C.muted]);
  addText(slide, '标签可重叠：同一 benchmark 可能同时有仿真、真机和真实数据集证据。', 8.38, 5.35, 3.75, 0.42, { fontSize: 10.5, color: C.muted, valign: 'top' });
  addText(slide, '其他场景：人机交互 1、导航 1、全身控制 1、多机器人 1、多主体社会行为 1、无人机 1。', 0.65, 6.48, 12.0, 0.25, { fontSize: 10.5, color: C.muted });
  addFooter(slide, 8);
}

// Slide 9: execution interface matrix
{
  const slide = newSlide('先确认“模型输出什么”：不同接口测量的是不同能力', '08 / 评测层级');
  const cols = [0.72, 3.1, 5.48, 7.86, 10.24];
  const heads = ['静态判断', '符号规划', '高层交互', '闭环仿真', '真实执行'];
  const body = [
    ['ASIMOV\nRoboAbstention', '动作是否合宜\n是否应该弃权'],
    ['DESPITE', '计划有效性\n形式化安全约束'],
    ['SafeAgentBench', '工具／动作序列\n交互结果'],
    ['LIBERO-Safety\nSafeStage', '连续动作\n轨迹违规与完成'],
    ['RoboHarm\nHazardArena', '指定硬件与场景\n实际行为'],
  ];
  heads.forEach((h, i) => {
    addRect(slide, cols[i], 1.55, 2.05, 0.52, i === 3 ? C.red : C.navy, true);
    addText(slide, h, cols[i], 1.69, 2.05, 0.2, { fontSize: 14, bold: true, color: C.white, align: 'center' });
    addRect(slide, cols[i], 2.18, 2.05, 2.5, C.pale, true);
    addText(slide, body[i][0], cols[i] + 0.16, 2.43, 1.75, 0.6, { fontSize: 14, bold: true, color: C.teal, align: 'center' });
    addLine(slide, cols[i] + 0.25, 3.22, cols[i] + 1.8, 3.22, C.line, 0.8);
    addText(slide, body[i][1], cols[i] + 0.16, 3.45, 1.75, 0.72, { fontSize: 14, color: C.ink, align: 'center', valign: 'top' });
  });
  addRect(slide, 0.75, 5.25, 11.9, 0.75, 'FFF8EE', true);
  addText(slide, '跨论文比较前的底线：不要把“回答正确”“计划安全”“闭环无碰撞”“真实硬件未受伤”当成同一个安全率。', 1.0, 5.47, 11.4, 0.28, { fontSize: 15, bold: true, color: C.orange, align: 'center' });
  addFooter(slide, 9);
}

// Slide 10: benchmark pipeline
{
  const slide = newSlide('一个可复用的 benchmark，必须把整条实验链写清楚', '09 / 设计链');
  const steps = [
    ['1', '任务与风险定义', '目标、对象、初态、允许动作、安全约束'],
    ['2', '场景与数据生成', '资产、相机、布局、动态对象、训练／测试划分'],
    ['3', '被测模型接口', '视觉／语言／状态输入；计划或控制输出'],
    ['4', '执行与轨迹记录', '重置、控制周期、时限、终止规则、事件日志'],
    ['5', '自动评分与统计', '目标、违规、后果分开；分母、种子、置信区间'],
  ];
  steps.forEach((s, i) => {
    const x = 0.72 + i * 2.5;
    addRect(slide, x, 2.0, 2.05, 2.3, i === 3 ? 'FFF1F0' : C.pale, true);
    addPill(slide, s[0], x + 0.18, 2.25, 0.44, i === 3 ? C.red : C.teal);
    addText(slide, s[1], x + 0.18, 2.78, 1.7, 0.52, { fontSize: 16, bold: true, color: C.navy, align: 'center' });
    addText(slide, s[2], x + 0.18, 3.48, 1.7, 0.52, { fontSize: 11.2, color: C.ink, align: 'center', valign: 'top' });
    if (i < steps.length - 1) addArrow(slide, x + 2.12, 2.98, 0.26, 0.32, C.aqua);
  });
  addRect(slide, 1.1, 5.05, 11.1, 0.92, C.navy, true);
  addText(slide, '复现门槛 = 任务资产 + 环境版本 + 评测器 + 模型接口 + 统计协议，而不是“下载一个任务列表”。', 1.45, 5.33, 10.4, 0.32, { fontSize: 16, bold: true, color: C.white, align: 'center' });
  addFooter(slide, 10);
}

// Slide 11: top cited benchmark nuScenes
{
  const slide = newSlide('最高被引 benchmark：nuScenes 把真实驾驶感知做成可复用底座', '10 / 代表性 benchmark');
  addRect(slide, 0.72, 1.42, 4.25, 4.85, C.navy, true);
  addText(slide, 'nuScenes', 1.05, 1.85, 3.6, 0.46, { fontSize: 29, bold: true, color: C.white });
  addText(slide, 'OpenAlex 被引观测', 1.08, 2.55, 2.2, 0.22, { fontSize: 11, color: 'BFD8E2' });
  addText(slide, '7,152', 1.05, 2.86, 3.0, 0.62, { fontSize: 40, bold: true, color: '7BD1D8' });
  addText(slide, '真实驾驶数据集／开环评测\n不是安全专用 benchmark', 1.08, 3.75, 3.3, 0.58, { fontSize: 16, color: C.white, valign: 'top' });
  addText(slide, '首发论文：1903.11027\n入口：nuscenes.org', 1.08, 5.2, 3.2, 0.48, { fontSize: 12, color: 'BFD8E2', valign: 'top' });
  addRect(slide, 5.35, 1.42, 7.3, 2.22, C.pale, true);
  addText(slide, '设计方案', 5.72, 1.76, 2.0, 0.26, { fontSize: 18, bold: true, color: C.navy });
  addBulletList(slide, [
    '1,000 个 20 秒真实驾驶场景，六相机、五雷达、一个激光雷达，覆盖 360° 感知。',
    '同步传感器、定位与地图，人工标注 23 类物体和八种属性。',
    '统一检测／跟踪任务与 NDS、AMOTA、AMOTP 等指标，提供公开开发工具和基线。',
  ], 5.72, 2.22, 6.45, 0.43, 14.5);
  addRect(slide, 5.35, 3.95, 3.45, 2.32, 'E8F5F7', true);
  addText(slide, '核心技术', 5.7, 4.28, 1.8, 0.25, { fontSize: 17, bold: true, color: C.teal });
  addBulletList(slide, ['多传感器时间同步与标定', '场景级时序上下文', '3D 框与轨迹标注', '标准化开环指标'], 5.72, 4.75, 2.55, 0.35, 13.2);
  addRect(slide, 9.05, 3.95, 3.6, 2.32, 'FFF8EE', true);
  addText(slide, '为什么这样设计？', 9.4, 4.28, 2.7, 0.25, { fontSize: 17, bold: true, color: C.orange });
  addBulletList(slide, ['用统一传感器和标签降低跨方法比较成本', '保留真实道路长尾和时序信息', '让后续规划／鲁棒性工作共享同一数据底座'], 9.42, 4.75, 2.7, 0.48, 13.2);
  addFooter(slide, 11, '来源：benchmarks/5__nuScenes.md；OpenAlex 快照 2026-11-03。');
}

// Slide 12: nuScenes limitations
{
  const slide = newSlide('nuScenes 的启示：影响力来自标准化，但安全结论不能从检测分数外推', '11 / 代表性 benchmark');
  addRect(slide, 0.72, 1.48, 5.7, 4.75, C.pale, true);
  addText(slide, '可复用价值', 1.08, 1.86, 2.2, 0.27, { fontSize: 18, bold: true, color: C.green });
  addBulletList(slide, [
    '数据采集、标定、标注与指标被统一封装，形成可共享的研究基线。',
    '真实场景的多模态与时间结构，支持后续感知、预测、规划和反事实诊断。',
    '高引用量说明它成为领域公共接口，而不仅是一篇论文的实验数据。',
  ], 1.1, 2.35, 4.95, 0.56, 15);
  addRect(slide, 6.85, 1.48, 5.8, 4.75, 'FFF1F0', true);
  addText(slide, '安全边界', 7.2, 1.86, 2.2, 0.27, { fontSize: 18, bold: true, color: C.red });
  addBulletList(slide, [
    '原论文主要评价感知；检测／跟踪高分不等于闭环驾驶安全。',
    '记录场景中的交通参与者不因自车行为而响应，交互性有限。',
    '后续安全工作需要补充危险插入、反事实干预、响应合规和真实后果判定。',
  ], 7.22, 2.35, 4.95, 0.56, 15);
  addRect(slide, 1.05, 5.55, 11.1, 0.52, C.navy, true);
  addText(slide, '结论：高被引 benchmark 适合作为数据和协议底座，但安全性必须在目标任务与风险层级上单独设计。', 1.28, 5.69, 10.6, 0.22, { fontSize: 13.5, bold: true, color: C.white, align: 'center' });
  addFooter(slide, 12);
}

// Slide 13: safety benchmark design examples
{
  const slide = newSlide('安全 benchmark 的设计分化：同样是“安全”，检测对象并不相同', '12 / 安全案例');
  const cards = [
    { x: 0.72, title: 'LIBERO-Safety', tag: '物理 + 语义', color: C.teal, lines: ['5 套任务、5 任务、3 难度：75 个测试配置', 'UBDDL 扩展 BDDL：随机化、动态交互、逐步安全检查', '把碰撞／约束违规纳入闭环轨迹，而不是只看终点'], note: '适合：VLA 操作中的安全任务描述与过程约束' },
    { x: 4.52, title: 'SafeStage', tag: '阶段风险', color: C.red, lines: ['97 个任务：初始危险 27、执行阶段 40、完成后 30', '特权状态评分；完成后继续观察 5 秒', 'SR、VR、SSR、USR 分开报告；SR = SSR + USR'], note: '适合：区分“完成任务”和“完成但违规”' },
    { x: 8.32, title: 'ManiPhysicsBench', tag: '对象后果', color: C.orange, lines: ['91 个对象：脆断、软变形、薄壁变形', '接触力 + 外部力学求解器判定抓握损伤', 'SR、Safe SR、PR 分开；SR=0 时 PR 不定义'], note: '适合：把任务成功与对象完好拆开' },
  ];
  cards.forEach((c) => {
    addRect(slide, c.x, 1.55, 3.25, 4.85, C.pale, true);
    addPill(slide, c.tag, c.x + 0.25, 1.82, 1.08, c.color);
    addText(slide, c.title, c.x + 0.25, 2.28, 2.7, 0.38, { fontSize: 21, bold: true, color: C.navy });
    addBulletList(slide, c.lines, c.x + 0.25, 3.0, 2.65, 0.78, 13.2);
    addText(slide, c.note, c.x + 0.25, 5.55, 2.72, 0.5, { fontSize: 10.5, color: C.muted, valign: 'top' });
  });
  addFooter(slide, 13, '来源：benchmarks/1__LIBERO-Safety.md；benchmarks/1__SafeStage.md；benchmarks/1__ManiPhysicsBench.md。');
}

// Slide 14: SafeStage metric logic
{
  const slide = newSlide('SafeStage 的关键贡献：把“成功但不安全”从总成功率中拆出来', '13 / 指标示例');
  addRect(slide, 0.72, 1.5, 5.15, 4.8, C.navy, true);
  addText(slide, 'SR = SSR + USR', 1.12, 1.98, 4.3, 0.58, { fontSize: 30, bold: true, color: C.white, align: 'center' });
  addText(slide, '全部测试试验 N 为分母', 1.25, 2.72, 3.9, 0.28, { fontSize: 14, color: 'C9E3E8', align: 'center' });
  addRect(slide, 1.24, 3.38, 1.8, 1.05, C.green, true);
  addText(slide, 'SSR\n9.84%', 1.24, 3.6, 1.8, 0.48, { fontSize: 21, bold: true, color: C.white, align: 'center' });
  addRect(slide, 3.42, 3.38, 1.8, 1.05, C.red, true);
  addText(slide, 'USR\n23.90%', 3.42, 3.6, 1.8, 0.48, { fontSize: 21, bold: true, color: C.white, align: 'center' });
  addText(slide, '成功中不安全比例 = USR / SR = 23.90 / 33.74 ≈ 70.84%', 1.1, 5.1, 4.4, 0.45, { fontSize: 13.5, bold: true, color: 'C9E3E8', align: 'center', valign: 'top' });
  addRect(slide, 6.35, 1.5, 6.3, 4.8, C.pale, true);
  addText(slide, '为什么不能只看 USR？', 6.75, 1.92, 3.4, 0.3, { fontSize: 18, bold: true, color: C.navy });
  addBulletList(slide, [
    'USR 的分母是全部试验；“成功试验中违规比例”的分母是 SR。',
    '场景特定提示把 USR 降到 16.11%，但同时 SR 从 33.74% 降到 22.02%。',
    '因此，单独降低不安全成功率可能混入“更少行动／更少完成”的因素。',
    '推荐同时报告 SR、SSR、USR、VR，并标注测试种子、场景和提示条件。',
  ], 6.78, 2.45, 5.25, 0.6, 14.5);
  addText(slide, '该数值来自 SafeStage 原论文条件，不代表所有安全提示或所有模型。', 6.78, 5.62, 5.2, 0.25, { fontSize: 10.5, color: C.muted, italic: true });
  addFooter(slide, 14, '来源：benchmarks/1__SafeStage.md；原论文结果，未由本项目复现。');
}

// Slide 15: cross-benchmark gap
{
  const slide = newSlide('综合缺口：从“任务成功”走向“风险可解释、后果可验证、资源可复现”', '14 / 发现');
  const cols = [0.72, 4.42, 8.12];
  const cards = [
    ['风险定义', C.red, ['安全标签常按论文自定义', '语义、物理、对象损伤、系统治理尚未统一', '同一“安全”词不能直接比较']],
    ['评测闭环', C.teal, ['仿真任务多，真机证据少', '不同接口承担的能力不同', '过程违规和终态后果常被分开统计']],
    ['可复现性', C.orange, ['40 个确认入口，但不等于完整开源', '许可证、评测器、权重、版本仍需逐项核验', '论文可读不等于实验可运行']],
  ];
  cards.forEach((c, i) => {
    const x = cols[i];
    addRect(slide, x, 1.6, 3.15, 4.55, C.pale, true);
    addRect(slide, x, 1.6, 3.15, 0.55, c[1], true);
    addText(slide, c[0], x, 1.77, 3.15, 0.22, { fontSize: 17, bold: true, color: C.white, align: 'center' });
    addBulletList(slide, c[2], x + 0.3, 2.55, 2.5, 0.85, 15);
  });
  addRect(slide, 11.85, 1.6, 0.8, 4.55, C.navy, true);
  addText(slide, '证\n据\n链', 11.85, 2.95, 0.8, 1.2, { fontSize: 18, bold: true, color: C.white, align: 'center' });
  addText(slide, '当前样本已经足以说明“需要更好的安全评测”，但还不足以支持统一排行榜或全领域覆盖比例。', 0.95, 6.45, 11.2, 0.28, { fontSize: 14, bold: true, color: C.navy, align: 'center' });
  addFooter(slide, 15);
}

// Slide 16: conclusions
{
  const slide = newSlide('关键结论', '15 / 结论');
  const items = [
    ['01', 'benchmark 数量增长快，但统计单位必须拆开', '论文记录、研究条目、评测任务集、数据集和平台不能混报；本库的 52 个 benchmark 是明确的主要分母。', C.navy],
    ['02', '安全评测正在从终点成功扩展到过程与后果', 'SafeStage、LIBERO-Safety、ManiPhysicsBench 分别把阶段风险、物理约束和对象损伤加入协议。', C.red],
    ['03', '影响力与安全性是两条不同轴', 'nuScenes 以 7,152 次引用成为公共数据底座，但不提供闭环安全保证；安全基准需要自己的风险定义和判分。', C.teal],
  ];
  items.forEach((it, i) => {
    const y = 1.45 + i * 1.55;
    addPill(slide, it[0], 0.92, y + 0.08, 0.52, it[3]);
    addText(slide, it[1], 1.75, y, 10.2, 0.32, { fontSize: 19, bold: true, color: C.navy });
    addText(slide, it[2], 1.75, y + 0.48, 10.2, 0.52, { fontSize: 14.5, color: C.ink, valign: 'top' });
  });
  addRect(slide, 0.92, 6.05, 11.4, 0.62, C.navy, true);
  addText(slide, '判断：需要新的安全 benchmark，但重点应是“可解释的风险—闭环证据—可复现资源”，而非重复已有任务。', 1.15, 6.24, 10.95, 0.24, { fontSize: 15.5, bold: true, color: C.white, align: 'center' });
  addFooter(slide, 16);
}

// Slide 17: recommendation
{
  const slide = newSlide('对未来工作的建议：如果再设计，优先做“组合式安全 benchmark”', '16 / 建议');
  const steps = [
    ['A', '风险 taxonomy', '把语义危险、碰撞、对象损伤、终态失稳、拒绝／澄清分别定义，并提供最小可复用标签。'],
    ['B', '配对任务设计', '安全／危险、正常／扰动、成功／失败恢复成对构造，控制任务能力与安全能力的混淆。'],
    ['C', '统一评分协议', '同时报告 SR、SSR、USR、VR、后果指标；明确分母、种子、停止规则与统计误差。'],
    ['D', '跨执行层验证', '离线判断 → 仿真闭环 → 仿真—真机配对；标注每层能支持的结论边界。'],
    ['E', '资源与复现', '公开任务资产、评测器、版本、许可证、基线与失败轨迹，提供一键最小评测。'],
  ];
  steps.forEach((s, i) => {
    const x = 0.72 + (i % 3) * 4.1;
    const y = i < 3 ? 1.55 : 4.15;
    addRect(slide, x, y, 3.55, 1.8, i === 1 ? 'FFF8EE' : C.pale, true);
    addPill(slide, s[0], x + 0.25, y + 0.25, 0.4, i === 1 ? C.orange : C.teal);
    addText(slide, s[1], x + 0.82, y + 0.25, 2.4, 0.25, { fontSize: 17, bold: true, color: C.navy });
    addText(slide, s[2], x + 0.25, y + 0.75, 3.0, 0.74, { fontSize: 12.1, color: C.ink, valign: 'top' });
  });
  addRect(slide, 8.92, 4.15, 3.55, 1.8, C.navy, true);
  addText(slide, '优先级判断', 9.22, 4.48, 2.9, 0.25, { fontSize: 17, bold: true, color: C.white, align: 'center' });
  addText(slide, '若只能做一件事：先把“成功但违规”和“失败但安全”分开计量，再扩展场景数量。', 9.25, 5.0, 2.85, 0.62, { fontSize: 14, color: 'D8EEF2', align: 'center', valign: 'top' });
  addFooter(slide, 17);
}

// Slide 18: benchmark index 1
function addIndexSlide(start, end, n) {
  const slide = newSlide(`附录：52 个 benchmark 索引（${n}/2）`, '17 / 附录');
  const list = benchmarks.slice(start, end);
  const cols = [0.7, 6.72];
  list.forEach((e, i) => {
    const col = i < 13 ? 0 : 1;
    const row = i % 13;
    const x = cols[col];
    const y = 1.42 + row * 0.41;
    const cited = e.citation?.cited_by_count;
    const safe = (e.objectives || []).includes('safety');
    const status = e.resources?.entry_status === 'found' ? '入口' : e.resources?.entry_status === 'candidate' ? '候选' : '平台';
    addRect(slide, x, y, 5.9, 0.32, row % 2 === 0 ? C.pale : C.white, false);
    addText(slide, `${String(start + i + 1).padStart(2, '0')}`, x + 0.08, y + 0.05, 0.28, 0.2, { fontSize: 9.5, color: C.muted, align: 'center' });
    addText(slide, e.name, x + 0.46, y + 0.045, 3.62, 0.22, { fontSize: 10.6, bold: safe, color: safe ? C.red : C.ink });
    addText(slide, safe ? '安全' : '—', x + 4.18, y + 0.05, 0.48, 0.2, { fontSize: 9, color: safe ? C.red : C.muted, align: 'center' });
    addText(slide, cited == null ? '—' : `${cited} 引`, x + 4.72, y + 0.05, 0.56, 0.2, { fontSize: 8.8, color: cited > 0 ? C.teal : C.muted, align: 'right' });
    addText(slide, status, x + 5.32, y + 0.05, 0.47, 0.2, { fontSize: 8.8, color: status === '入口' ? C.green : status === '候选' ? C.orange : C.muted, align: 'center' });
  });
  addText(slide, '说明：安全、引用和入口状态来自本库字段；“—”表示未记录或 0，不代表不存在。', 0.72, 6.78, 11.8, 0.22, { fontSize: 9.5, color: C.muted });
  addFooter(slide, 18 + n - 1);
}
addIndexSlide(0, 26, 1);
addIndexSlide(26, 52, 2);

const out = path.join(ROOT, 'presentations', '具身智能及安全Benchmark调研汇报_2026-11-03_最终版.pptx');
await pptx.writeFile({ fileName: out });
execFileSync(process.env.SURVEY_PYTHON || 'python', [path.join(ROOT, 'scripts/patch_pptxgenjs_package.py'), out], { stdio: 'inherit' });
console.log(JSON.stringify({ out, slides: pptx._slides.length, papers: registry.paper_count, entries: entries.length, benchmarks: benchmarks.length }));

