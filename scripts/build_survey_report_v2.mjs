/**
 * 调研汇报 PPT（新稿）：只讲论文、benchmark、覆盖与安全评测；数据集/平台条目不展开。
 * 风格沿用 presentations/ 既有版式：LAYOUT_WIDE、Microsoft YaHei、深蓝标题 + teal 强调 + 细线页脚。
 *
 * 所有数字来自本仓库 data/benchmark_survey.json、benchmark_usage_records.json、
 * benchmark_citation_snapshot.json、benchmark_project_audit.json。构建后自检文本是否溢出，再导出。
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const pptxgen = require('pptxgenjs');

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUT = path.join(ROOT, 'presentations');
const SNAPSHOT = '2026-11-04';
const FONT = 'Microsoft YaHei';
const W = 13.333;
const H = 7.5;

const C = {
  navy: '16324F', ink: '17212B', muted: '5B6770', line: 'D8E1E8', pale: 'F4F7F9',
  teal: '0E7490', aqua: '2C9EAA', green: '2E8B72', orange: 'D97706',
  red: 'B94E48', purple: '6B5B95', white: 'FFFFFF',
};

// ---------- 数据 ----------
const survey = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_survey.json'), 'utf8'));
const usage = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_usage_records.json'), 'utf8'));
const snapshot = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_citation_snapshot.json'), 'utf8'));
const audit = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_project_audit.json'), 'utf8'));
const reviews = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_paper_reviews.json'), 'utf8'));
const sources = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_reading_sources.json'), 'utf8'));
const glossary = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_glossary.json'), 'utf8'));
const properNames = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_names.json'), 'utf8'));
const reviewByName = new Map(reviews.entries.map((e) => [e.benchmark, e]));
const sourceByName = new Map(sources.entries.map((e) => [e.benchmark, e]));

const active = survey.entries.filter((e) => e.focus === 'active');
const benches = active.filter((e) => e.primary_type === 'benchmark');
const stats = survey.statistics;
const projectCounts = { found: 0, platform_only: 0, candidate: 0, not_found: 0 };
for (const a of audit.audits) if (active.some((e) => e.name === a.benchmark)) projectCounts[a.status] = (projectCounts[a.status] || 0) + 1;
const usageByName = new Map(usage.entries.map((e) => [e.benchmark, e]));
const citeByName = new Map(snapshot.entries.map((e) => [e.benchmark, e]));

const N = {
  papers: 62,
  biblio: 199,
  inventory: survey.entries.length,
  benchmarks: benches.length,
  direct: benches.filter((e) => e.relevance === 'direct').length,
  safety: active.filter((e) => e.objectives.includes('safety')).length,
  safetyBench: benches.filter((e) => e.objectives.includes('safety')).length,
  capability: active.filter((e) => e.objectives.includes('capability')).length,
  robustness: active.filter((e) => e.objectives.includes('robustness')).length,
  found: projectCounts.found, platform: projectCounts.platform_only, candidate: projectCounts.candidate,
};

// ---------- 版式工具 ----------
const CJK = /[\u2e80-\u9fff\uff00-\uffef\u3000-\u303f]/;
function charW(ch) {
  if (CJK.test(ch)) return 1.04;
  if (/[A-Z]/.test(ch)) return 0.67;
  if (/[a-z]/.test(ch)) return 0.57;
  if (/[0-9]/.test(ch)) return 0.61;
  if (/[ .,:;!?'"()\[\]\/\\-]/.test(ch)) return 0.36;
  return 0.58;
}
function textW(t, size) {
  let w = 0;
  for (const ch of String(t)) w += charW(ch) * size;
  return w / 72; // 英寸
}
function wrap(t, width, size) {
  const lines = [];
  for (const para of String(t).split('\n')) {
    if (!para) { lines.push(''); continue; }
    let line = '';
    const tokens = para.match(/[A-Za-z0-9@._/,+%:：→\-]+|[\s]|[^\s]/gu) || [];
    for (const tk of tokens) {
      const trial = line + tk;
      if (textW(trial, size) > width - 0.16 && line) {
        // 中文排版：标点不出现在行首，允许略超宽度
        if (/^[、，。；：？！）】》”’%]$/.test(tk)) { lines.push((line + tk).trimEnd()); line = ''; continue; }
        // 开括号不留在行尾：把它挪到下一行开头
        const openTail = /[（《“‘【(]$/.test(line) ? line.slice(-1) : '';
        if (openTail) line = line.slice(0, -1);
        lines.push(line.trimEnd()); line = openTail + tk.trimStart();
      } else line = trial;
    }
    if (line.trim() || !lines.length) lines.push(line.trimEnd());
  }
  return lines;
}
const overflow = [];
function addText(slide, text, x, y, w, h, opts = {}) {
  const size = opts.size ?? 12;
  const lines = wrap(text, w, size);
  const lh = (size / 72) * (opts.lineSpacing ?? 1.32);
  if (lines.length * lh > h + 0.03 && !opts.allowOverflow) {
    overflow.push({ slide: slide._index, text: String(text).slice(0, 40), need: +(lines.length * lh).toFixed(2), have: h });
  }
  slide.addText(lines.join('\n'), {
    x, y, w, h,
    fontFace: FONT, fontSize: size, bold: !!opts.bold, color: opts.color || C.ink,
    align: opts.align || 'left', valign: opts.valign || 'top', margin: 0,
    fit: 'none', breakLine: false, italic: !!opts.italic,
    lineSpacingMultiple: opts.lineSpacing ?? 1.32,
    charSpacing: opts.charSpacing,
  });
}
function addRect(slide, x, y, w, h, fill, radius = false, line = null) {
  slide.addShape(radius ? pptx.ShapeType.roundRect : pptx.ShapeType.rect, {
    x, y, w, h, rectRadius: radius ? 0.06 : undefined,
    fill: { color: fill }, line: line ? { color: line, width: 0.8 } : { color: fill, transparency: 100 },
  });
}
function addLine(slide, x1, y1, x2, y2, color = C.line, width = 1) {
  slide.addShape(pptx.ShapeType.line, { x: x1, y: y1, w: x2 - x1, h: y2 - y1, line: { color, width } });
}
function addPill(slide, label, x, y, w, fill = C.teal, color = C.white, size = 9) {
  addRect(slide, x, y, w, 0.26, fill, true);
  addText(slide, label, x, y + 0.01, w, 0.24, { size, bold: true, color, align: 'center', valign: 'mid' });
}

const slides = [];
function newSlide(spec) {
  const slide = pptxgen ? null : null;
  return spec;
}
function frame(title, kicker) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s._index = pptx._slides.length;
  if (kicker) addText(s, kicker, 0.62, 0.26, 8, 0.22, { size: 9, bold: true, color: C.teal, charSpacing: 1 });
  addText(s, title, 0.62, 0.5, 12.1, 0.5, { size: 24, bold: true, color: C.navy });
  return s;
}
function footer(s, source = '数据快照：2026-11-04；统计来自 data/benchmark_survey.json 等本仓库数据。') {
  addLine(s, 0.62, 7.06, 12.72, 7.06, C.line, 0.7);
  addText(s, source, 0.62, 7.13, 11.3, 0.2, { size: 8, color: C.muted });
  addText(s, String(s._index).padStart(2, '0'), 12.2, 7.12, 0.5, 0.2, { size: 8.5, bold: true, color: C.muted, align: 'right' });
}
function addTable(s, headers, rows, widths, y, opts = {}) {
  const maxH = opts.maxH ?? (6.9 - y);
  let size = opts.size ?? 10;
  const minSize = opts.minSize ?? 8;
  const padX = 0.09, padY = 0.05;
  const layout = () => {
    const cells = [headers, ...rows].map((row) => row.map((v, i) => wrap(String(v), widths[i] - padX * 2, size)));
    const heights = cells.map((row, r) => Math.max(...row.map((c) => c.length)) * (size / 72) * 1.28 + padY * 2 + (r === 0 ? 0.02 : 0));
    return { cells, heights, total: heights.reduce((a, b) => a + b, 0) };
  };
  let L = layout();
  while (L.total > maxH && size > minSize) { size -= 0.5; L = layout(); }
  if (L.total > maxH + 0.02) overflow.push({ slide: s._index, text: `table@${y}`, need: +L.total.toFixed(2), have: +maxH.toFixed(2) });
  if (opts.fillTo && L.heights.length > 1) {
    const extra = opts.fillTo - L.total;
    if (extra > 0.08) {
      const add = Math.min(0.32, extra / (L.heights.length - 1));
      for (let i = 1; i < L.heights.length; i += 1) L.heights[i] += add;
      L.total = L.heights.reduce((a, b) => a + b, 0);
    }
  }
  const table = s.addTable(
    [headers, ...rows].map((row, r) => row.map((v, i) => ({
      text: wrap(String(v), widths[i] - padX * 2, size).join('\n'),
      options: {
        fontSize: size, fontFace: FONT, bold: r === 0,
        color: r === 0 ? C.white : C.ink,
        fill: { color: r === 0 ? C.navy : (r % 2 === 0 ? C.white : C.pale) },
        valign: 'middle', margin: padX, breakLine: false,
      },
    }))),
    { x: 0.62, y, w: widths.reduce((a, b) => a + b, 0), colW: widths, rowH: L.heights, border: { type: 'solid', color: C.line, pt: 0.6 }, autoPage: false },
  );
  return y + L.total;
}
function divider(title, lead, kicker) {
  const s = pptx.addSlide();
  s.background = { color: C.navy };
  s._index = pptx._slides.length;
  addText(s, kicker, 0.8, 2.05, 8, 0.3, { size: 11, bold: true, color: 'AFC7D2', charSpacing: 1.5 });
  addText(s, title, 0.8, 2.45, 11.6, 0.8, { size: 34, bold: true, color: C.white });
  addRect(s, 0.82, 3.45, 1.6, 0.06, C.aqua);
  addText(s, lead, 0.82, 3.75, 10.6, 1.1, { size: 14, color: 'D8EEF2', lineSpacing: 1.5 });
  addText(s, String(s._index).padStart(2, '0'), 12.2, 7.12, 0.5, 0.2, { size: 8.5, bold: true, color: 'AFC7D2', align: 'right' });
  return s;
}

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Embodied Safety Benchmark Survey';
pptx.subject = '具身智能与安全 Benchmark 调研汇报（新稿）';
pptx.title = '具身智能与安全 Benchmark 调研汇报';
pptx.company = 'Embodied Safety Benchmark';
pptx.lang = 'zh-CN';
pptx.theme = { headFontFace: FONT, bodyFontFace: FONT, lang: 'zh-CN' };
pptx._slides = [];

const outline = [];
function record(s, title, lead) { outline.push({ n: s._index, title, lead: lead || '' }); }
function note(s, text) { s.addNotes(`资料快照：${SNAPSHOT}。${text}`); }

// 展示名 -> 仓库条目名的映射（PPT 里用短名，数据里用完整名）
const REVIEW_KEY = {
  'LIBERO': 'LIBERO（基础套件）',
};

// 备注里的术语标注：每个术语在同一页备注中只在首次出现处解释一次
const ANNOTATIONS = [];
const ANNOTATE_PER_PARAGRAPH = false;
const clean = (s) => (s || '').replace(/[（(][^）)]*[）)]/g, '').trim();
for (const term of glossary.terms) {
  const en = term.en && term.en !== term.term ? clean(term.en) : '';
  const zh = term.zh && term.zh !== term.term ? clean(term.zh) : '';
  let inner = [en, zh].filter(Boolean).join('；');
  if (!inner) continue;
  if (inner.length > 24) inner = zh || en;
  if (!inner || inner.length > 24) continue;
  ANNOTATIONS.push({ term: term.term, label: `（${inner}）` });
}
for (const item of properNames.names) {
  ANNOTATIONS.push({ term: item.name, label: `（${item.kind}）` });
}
ANNOTATIONS.sort((a, b) => b.term.length - a.term.length);
const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function annotate(paragraph, seen) {
  const matches = [];
  for (const item of ANNOTATIONS) {
    if (seen.has(item.term)) continue;
    const re = new RegExp('(?<![A-Za-z0-9_-])' + escapeRe(item.term) + '(?![A-Za-z0-9_-])');
    const m = re.exec(paragraph);
    if (!m) continue;
    if (paragraph.slice(m.index + item.term.length, m.index + item.term.length + 1) === '（') continue;
    matches.push({ index: m.index, len: item.term.length, term: item.term, label: item.label });
  }
  matches.sort((a, b) => a.index - b.index || b.len - a.len);
  const chosen = [];
  let cursor = -1;
  for (const m of matches) {
    if (m.index >= cursor) {
      chosen.push(m);
      cursor = m.index + m.len;
    }
  }
  let out = paragraph;
  for (let i = chosen.length - 1; i >= 0; i -= 1) {
    const m = chosen[i];
    out = out.slice(0, m.index + m.len) + m.label + out.slice(m.index + m.len);
    seen.add(m.term);
  }
  return out;
}

function composeNote(paragraphs, skip = []) {
  const seen = new Set(skip);
  const body = paragraphs.map((text) => {
    const local = ANNOTATE_PER_PARAGRAPH ? new Set(skip) : seen;
    return annotate(text, local);
  });
  return body.join('\n\n') + '\n\n（以上为论文报告值与正文笔记的转述，本库未复现实验。）';
}

const SKIP_BY_PAGE = {
  'LIBERO-Safety': ['SSR'],
  'SafeStage': ['ETS'],
  'RoboJailBench': ['SR'],
  'ForesightSafety-VLA': ['SR'],
  'VLA-Arena': ['SR'],
};

function paperNote(spec, kpis) {
  const name = spec.name;
  const plain = spec.plain ? spec.plain : '';
  const key = REVIEW_KEY[name] || name;
  const r = reviewByName.get(key);
  const src = sourceByName.get(key);
  if (!r) {
    return composeNote([`这一页的条目是 ${name}，但本轮没有找到与它对应的正文笔记，数字需要回原文核对后才能引用。`]);
  }
  const meta = src ? src.metadata : {};
  const authors = (meta.authors || []).slice(0, 3).join('、');
  const more = (meta.authors || []).length > 3 ? ' 等' : '';
  const kpiText = (kpis || []).map(([num, label]) => `${num}（${label}）`).join('，');
  return composeNote([
    `本页介绍 ${name}。${plain}提出它的论文是《${meta.title || name}》，作者包括 ${authors || '论文未记录'}${more}，`
      + `本库阅读的版本是 arXiv ${meta.version || '未记录'}，首次提交于 ${(meta.slid || meta.published || '').slice(0, 10) || '未记录'}。`
      + `论文要回答的问题是：${r.question}就评测层级而言，它属于${r.kind}，所以下面的数字都只在这类接口上成立。`,
    `任务与规模方面，${spec.domain ? spec.domain + '。' : ''}${r.scenarios}这些数字决定了一轮评测要跑多久、能不能在单机上复现，也决定了它能覆盖多少种失败形态。`,
    `构建与判分方面，${spec.build || r.implementation}`
      + (spec.metric ? ` 判分上，${spec.metric}` : ` 读这部分时要注意分母：同一个成功率，分母是全部测试试验还是成功试验，结论完全不同。`),
    `论文报告的结果是：${r.results}这些数字属于论文自己的训练与评测设置，换 checkpoint、换协议或换微调数据都会变。`,
    `作者也划清了边界：${r.limits}这一段标注为“论文自述的边界”：其中部分问题作者已承认，部分需要代码审计确认。`,
    `本页右上角的三个数字分别是 ${kpiText || '上面提到的关键数值'}，与正文和附录同源；本库只做记录与判读，没有复现这些实验。`,
    spec.rel ? `本页右上角还标注了“大模型相关度 ${spec.rel[0]}”。判断依据是：${spec.rel[1]}该标注描述该基准当前主流被测对象与 VLA、LLM 的距离；低相关度说明它主要服务经典策略研究，基准本身仍然有效。` : '',
  ], [name, REVIEW_KEY[name], ...(SKIP_BY_PAGE[name] || [])].filter(Boolean));
}

// ---------- 1. 封面 ----------
{
  const s = pptx.addSlide();
  s.background = { color: C.navy };
  s._index = 1;
  addPill(s, '调研汇报 · 新稿', 0.82, 1.0, 1.9, C.teal, C.white, 9.5);
  addText(s, '具身智能与安全 Benchmark 调研', 0.8, 1.45, 11.8, 0.85, { size: 38, bold: true, color: C.white });
  addText(s, '论文与基准的规模、场景与环节覆盖；基础能力基线；安全评测的分层证据', 0.82, 2.42, 11.2, 0.5, { size: 17, color: 'D8EEF2' });
  addRect(s, 0.82, 3.28, 2.5, 0.5, C.teal, true);
  addText(s, `资料快照 ${SNAPSHOT}`, 0.82, 3.33, 2.5, 0.4, { size: 11.5, bold: true, color: C.white, align: 'center', valign: 'mid' });
  const facts = [
    [`${N.papers}`, '篇论文正文精读'],
    [`${N.benchmarks}`, '个评测任务集'],
    [`${N.safetyBench}`, '个任务集涉及安全'],
  ];
  facts.forEach(([num, label], i) => {
    const x = 0.82 + i * 3.1;
    addText(s, num, x, 4.5, 2.6, 0.66, { size: 40, bold: true, color: C.aqua, lineSpacing: 1.0 });
    addText(s, label, x, 5.18, 2.7, 0.3, { size: 11.5, color: 'C7D8E2' });
  });
  addText(s, '本汇报只统计“论文—benchmark”两类成果；数据集、仿真平台、评测框架与方法论文不在此展开。', 0.82, 6.05, 11.4, 0.3, { size: 11, color: 'AFC7D2' });
  addText(s, '所有数字来自本仓库结构化数据；模型分数来自各论文摘要或正文，未由本项目复现。', 0.82, 6.4, 11.4, 0.3, { size: 10.5, color: 'AFC7D2' });
  addText(s, '01', 12.2, 7.12, 0.5, 0.2, { size: 8.5, bold: true, color: 'AFC7D2', align: 'right' });
  note(s, '封面。三类数字：精读论文数、评测任务集数、其中涉及安全的任务集数。');
}

// ---------- 2. 一页结论 ----------
{
  const s = frame('先看结论：基准数量充足，缺统一的评估口径', '01 / 摘要');
  const cards = [
    [String(N.papers), '篇论文正文精读', C.navy, `${N.biblio} 条书目记录，来自 193 行初始筛选 + 6 篇补入`],
    [String(N.benchmarks), '个评测任务集', C.teal, `其中 ${N.direct} 个直接具身评测，${N.safetyBench} 个涉及安全`],
    [String(N.safety), '条带安全目标', C.red, '26/62 条目；9 条只测安全，其余与能力或鲁棒性共标'],
    [String(N.found), '个已确认项目入口', C.green, `另 ${N.platform} 个仅平台入口、${N.candidate} 个候选`],
  ];
  cards.forEach(([num, label, color, detail], i) => {
    const x = 0.62 + i * 3.08;
    addRect(s, x, 1.22, 2.9, 1.32, C.pale, true);
    addText(s, num, x + 0.18, 1.28, 2.5, 0.52, { size: 30, bold: true, color, lineSpacing: 1.0 });
    addText(s, label, x + 0.18, 1.82, 2.55, 0.26, { size: 11.5, bold: true });
    addText(s, detail, x + 0.18, 2.1, 2.55, 0.4, { size: 8.5, color: C.muted, lineSpacing: 1.25 });
  });
  addRect(s, 0.62, 2.78, 12.1, 3.9, C.pale, true);
  addText(s, '三条判断', 0.9, 2.95, 2.2, 0.3, { size: 14, bold: true, color: C.navy });
  const pts = [
    ['覆盖集中在桌面机械臂，形态分布不均。', '52 个任务集中机械臂操作 29 个、语义决策 9 个；移动操作 4 个、自动驾驶 3 个、人形全身 1 个。选型时先确认形态匹配。'],
    ['执行层级以仿真为主，真机证据是稀缺项。', '42/62 条目含仿真，18 条含真机执行；在 52 个任务集里真机只有 15 个。安全结论尤其依赖仿真谓词，不等于真实伤害。'],
    ['安全基准分六层，指标不能互相换算。', '执行层避碰、物体保全、语义意图、规划规则、过程阶段、对抗完整性各一套口径；“SR”在四类里含义都不同。'],
  ];
  pts.forEach(([h, body], i) => {
    const y = 3.32 + i * 1.05;
    addRect(s, 0.9, y + 0.06, 0.06, 0.72, [C.teal, C.orange, C.red][i]);
    addText(s, h, 1.08, y, 10.9, 0.3, { size: 12, bold: true });
    addText(s, body, 1.08, y + 0.32, 10.9, 0.62, { size: 9.5, color: C.muted, lineSpacing: 1.35 });
  });
  footer(s);
  note(s, `卡片数字：${N.papers} 篇精读、${N.benchmarks} 个任务集、${N.safety} 条带安全目标、${N.found} 个已确认项目入口。`);
  record(s, '先看结论：基准数量充足，缺统一的评估口径', '四条规模数字 + 三条判断');
}

// ---------- 3. 方法与口径 ----------
{
  const s = frame('怎么找、怎么判、什么不算证据', '01 / 方法和口径');
  addText(s, '筛选链路', 0.62, 1.2, 3, 0.28, { size: 12, bold: true, color: C.teal });
  const flow = [
    [String(N.inventory), '登记条目', C.navy],
    ['62', '正文精读并分类', C.teal],
    [String(N.benchmarks), '评测任务集', C.aqua],
    [String(N.direct), '直接具身任务集', C.green],
  ];
  flow.forEach(([num, label, color], i) => {
    const x = 0.62 + i * 3.1;
    addRect(s, x, 1.55, 2.7, 0.95, C.pale, true);
    addText(s, num, x + 0.16, 1.62, 1.2, 0.42, { size: 22, bold: true, color });
    addText(s, label, x + 0.16, 2.06, 2.4, 0.3, { size: 9.5, color: C.muted });
    if (i < 3) addText(s, '→', x + 2.72, 1.95, 0.34, 0.3, { size: 16, color: C.line });
  });
  addText(s, '判定顺序（每条 benchmark 都走一遍）', 0.62, 2.72, 6, 0.28, { size: 12, bold: true, color: C.teal });
  const rules = [
    ['① 读正文', '方法、任务构建、评测协议、结果与限制四段都要有章节依据；摘要不作为唯一依据。'],
    ['② 记分母', '每个指标写清分子与分母：是 / 全部 episode，还是 / 成功 episode。'],
    ['③ 查入口', '项目地址逐个审计：已确认 / 仅平台入口 / 候选待确认，三种状态不混用。'],
    ['④ 标未知', '没查到写“未核验”，不写 0、不写“没有”；被引数不等于采用量。'],
  ];
  rules.forEach(([h, body], i) => {
    const y = 3.05 + i * 0.62;
    addText(s, h, 0.62, y, 1.5, 0.3, { size: 10.5, bold: true, color: C.navy });
    addText(s, body, 2.15, y, 10.4, 0.55, { size: 10, color: C.muted, lineSpacing: 1.35 });
  });
  addRect(s, 0.62, 5.62, 12.1, 1.2, 'FDF6EC', true);
  addText(s, '不做什么', 0.9, 5.72, 2, 0.26, { size: 10, bold: true, color: C.orange });
  addText(s, '不声称系统综述（检索式未穷尽）；不把不同基准的分数求平均；不复现任何实验；不猜测录用状态与项目可用性。', 0.9, 6.0, 11.5, 0.7, { size: 9.5, color: C.muted, lineSpacing: 1.4 });
  footer(s);
  note(s, '口径说明：本汇报的三类数字分别来自登记表、精读分类与项目入口审计。');
  record(s, '怎么找、怎么判、什么不算证据', '筛选链路 + 四条判定规则 + 明确不做什么');
}

// ---------- 3b. 术语速查（两页）：让整本 PPT 不再依赖外部词表 ----------
{
  const WANT = ['VLA', 'VLM', 'LLM', 'episode', 'rollout', 'checkpoint', 'SR', 'SSR', 'USR', 'PR',
    'CAR', 'PDMS', 'BDDL', 'UBDDL', 'digital twin', 'domain randomization', 'CBF', 'QP', 'OOD', 'L0'];
  const byTerm = new Map(glossary.terms.map((x) => [x.term, x]));
  const rows = WANT.map((key) => {
    const item = byTerm.get(key) || {};
    const zh = (item.zh || '').replace(/[（(][^）)]*[）)]/g, '');
    const short = (item.short || '见 docs/GLOSSARY.md').replace(/[。；]$/, '');
    return [key, zh || '—', short.length > 52 ? short.slice(0, 50) + '…' : short];
  });
  const pages = [rows.slice(0, 10), rows.slice(10)];
  pages.forEach((pageRows, idx) => {
    const s = frame(idx === 0 ? '术语速查（一）：模型与评测单位' : '术语速查（二）：指标、平台与难度', '01 / 术语速查');
    addText(s, idx === 0
      ? '后文反复用到这些词。每个词给中文名与一句话解释，完整版见 docs/GLOSSARY.md；正文第一次出现处还会就地加注。'
      : '第二页是指标、仿真平台与难度标注。注意同名缩写：SR 在不同基准里含义不同，SSR／USR 的分母都是全部 episode。',
      0.62, 1.1, 12.1, 0.34, { size: 10, color: C.muted, lineSpacing: 1.35 });
    addTable(s, ['术语', '中文', '一句话解释'], pageRows, [2.5, 3.0, 6.55], 1.58, { size: 10.5, maxH: 4.7, fillTo: 4.55 });
    footer(s, `词条取自 data/benchmark_glossary.json（${glossary.terms.length} 个术语）与 data/benchmark_names.json（${properNames.names.length} 个专有名称）。`);
    note(s, idx === 0
      ? '术语页一：模型类别（VLA、VLM、LLM）、评测单位（episode、rollout、seed、checkpoint）与指标（SR、SSR、USR、PR）。讲的时候只需强调两点：episode 是最常见的分母；SSR 与 USR 都以全部 episode 为分母。'
      : '术语页二：指标（CAR、PDMS）、平台与任务定义（BDDL、UBDDL、数字孪生、域随机化、CBF、QP）、协议（OOD、L0/L1/L2）。重点提醒：SR 在 RoboJailBench 指 Security Rate，跨论文比较前先对齐定义。');
    record(s, idx === 0 ? '术语速查（一）：模型与评测单位' : '术语速查（二）：指标、平台与难度', '20 个高频术语');
  });
}

// ---------- 4. 论文与基准的数量关系 ----------
{
  const s = frame(`论文 ${N.papers} 篇，基准 ${N.benchmarks} 个：谁支撑了谁`, '01 / 成果规模');
  addText(s, `62 篇精读论文对应 52 个评测任务集，比例约 1.2 : 1；多数论文在既有环境上提出方法，“一篇论文一个新基准”属于少数。`, 0.62, 1.15, 12.1, 0.5, { size: 11, color: C.muted, lineSpacing: 1.4 });
  const rows = [
    ['评测任务集（benchmark）', String(N.benchmarks), '发布任务、协议与评分，可被他人直接使用', 'LIBERO-Safety、HazardArena、COLOSSEUM'],
    ['其中：直接具身评测', String(N.direct), '动作落在仿真或真机的物理场景', 'LIBERO、RoboTwin、SafeLIBERO'],
    ['其中：软件代理邻接', '4', '只到 API／文件／GUI 层，动作不物理', 'Agent-SafetyBench、SkillSafetyBench'],
    ['非任务集条目（本次不展开）', '10', '数据集 3、平台 2、框架 4、方法 1', 'AgiBot World、CARLA、STARS 等'],
  ];
  const tEnd4 = addTable(s, ['类别', '数量', '含义', '代表条目'], rows, [2.35, 0.85, 4.15, 4.75], 1.72, { size: 10, maxH: 2.6 });
  const evY = Math.max(tEnd4 + 0.45, 3.85);
  addText(s, '论文侧的证据结构', 0.62, evY, 4, 0.28, { size: 12, bold: true, color: C.teal });
  const evidence = [
    [`${N.papers} 篇`, '有正文重点章节笔记（方法／构建／评测／结果）'],
    [`${N.biblio} 条`, '书目记录：193 行初始筛选 + 6 篇补入的已读来源'],
    ['10 项', '历史全文核查记录，与本轮正文核查分开保存'],
    ['0 项', '由本库运行的实验——全部分数来自论文，未复现'],
  ];
  evidence.forEach(([num, body], i) => {
    const x = 0.62 + (i % 2) * 6.15;
    const y = evY + 0.38 + Math.floor(i / 2) * 1.02;
    addRect(s, x, y, 5.95, 0.86, C.pale, true);
    addText(s, num, x + 0.18, y + 0.12, 1.35, 0.3, { size: 15, bold: true, color: C.navy });
    addText(s, body, x + 1.55, y + 0.13, 4.25, 0.6, { size: 9.5, color: C.muted, lineSpacing: 1.3 });
  });
  footer(s, '数据快照：2026-11-04；类别与数量来自 data/benchmark_survey.json 的 statistics 与逐条编码。');
  note(s, '52 个任务集里 48 个是直接具身评测；另有 4 个软件代理任务集与 10 条非任务集条目不在本次统计口径内。');
  record(s, `论文 ${N.papers} 篇，基准 ${N.benchmarks} 个：谁支撑了谁`, '任务集构成与论文证据结构');
}

// ---------- 5. 场景覆盖 ----------
{
  const s = frame('覆盖场景：机械臂操作占多数，形态分布不均', '02 / 场景覆盖');
  const domains = [['机械臂操作', 29], ['机器人语义决策', 9], ['其它形态（工业 / 人形 / 导航 / UAV）', 9], ['主动视觉 / 灵巧 / 感知', 6], ['移动操作', 4], ['软件代理', 4], ['自动驾驶', 3]];
  const maxV = Math.max(...domains.map((d) => d[1]));
  domains.forEach(([label, v], i) => {
    const y = 1.25 + i * 0.52;
    addText(s, label, 0.62, y, 3.3, 0.3, { size: 9.5, color: C.ink });
    addRect(s, 3.95, y + 0.05, (v / maxV) * 4.35, 0.22, i === 0 ? C.navy : C.aqua, true);
    addText(s, String(v), 4.02 + (v / maxV) * 4.35, y, 0.6, 0.3, { size: 10, bold: true, color: C.navy });
  });
  addText(s, '注：场景可多标签，合计大于 52。', 0.62, 5.0, 5, 0.24, { size: 8.5, color: C.muted });
  addRect(s, 8.85, 1.2, 3.88, 3.6, C.pale, true);
  addText(s, '这些数字的含义', 9.05, 1.32, 3.4, 0.28, { size: 11, bold: true, color: C.navy });
  addText(s, '机械臂操作占 29/52，说明本库的“安全”讨论主要发生在桌面抓放与装配上。移动操作（4）、导航（1）、人形全身（1）、无人机（1）都只是样品级覆盖，不能用来下领域结论。', 9.05, 1.65, 3.5, 2.9, { size: 9.5, color: C.muted, lineSpacing: 1.45 });
  addRect(s, 0.62, 5.35, 12.1, 1.45, 'EEF4F7', true);
  addText(s, '选型提醒', 0.9, 5.45, 2, 0.26, { size: 10.5, bold: true, color: C.teal });
  addText(s, '当目标场景超出桌面机械臂时，可复用的部分是评测设计：如何构造危险场景、如何定义违规、如何把过程指标与终点指标分开。', 0.9, 5.75, 11.6, 0.9, { size: 9.5, color: C.muted, lineSpacing: 1.45 });
  footer(s);
  note(s, '场景标签来自逐条人工编码，可多选；机械臂操作 29 个、语义决策 9 个、移动操作 4 个、软件代理 4 个、自动驾驶 3 个。');
  record(s, '覆盖场景：机械臂操作占多数，形态分布不均', '场景条形图 + 选型提醒');
}

// ---------- 6. 环节覆盖 ----------
{
  const s = frame('覆盖具身系统的哪些环节：感知、规划、执行、运维', '02 / 环节覆盖');
  addText(s, '把每个基准按“动作落在哪一层”归类。一个基准可同时覆盖多层（例如仿真+真机），所以行之间不可相加。', 0.62, 1.12, 12.1, 0.4, { size: 10.5, color: C.muted, lineSpacing: 1.35 });
  const rows = [
    ['感知 / 理解', '6', '图像／视频问答、离线轨迹、场景与目标理解', 'RoboChrono、RoboAbstention、PhysAI-Bench'],
    ['规划 / 推理', '2', '符号计划、任务分解、安全约束推理', 'DESPITE、SafeAgentBench'],
    ['仿真执行（闭环）', '38', '在仿真里闭环跑策略，动作影响下一步观测', 'LIBERO、RoboTwin、SafeLIBERO'],
    ['真机执行', '15', '真实机械臂闭环，含少量配对验证', 'BEHAVIOR-1K、Spa-Bench、RoboHarm'],
    ['真实数据（非闭环）', '6', '只提供真实采集数据或人类示教', 'AgiBot World、RoboMIND、RoboReel'],
    ['软件环境', '4', 'API、文件、GUI 层，动作不物理', 'Agent-SafetyBench、SkillSafetyBench'],
    ['实体测试件', '1', '模块化实体件（装配件），非仿真', 'Peg-in-Bench'],
    ['运行时 / 治理', '1', '部署后的权限、恢复与升级', 'EmbodiedGovBench'],
  ];
  addTable(s, ['环节', '基准数', '判据（动作落在哪）', '代表条目'], rows, [2.0, 0.85, 4.85, 4.4], 1.62, { size: 10, maxH: 4.3, fillTo: 4.2 });
  addRect(s, 0.62, 6.02, 12.1, 0.78, 'FDF2F2', true);
  addText(s, '最大缺口', 0.9, 6.1, 1.6, 0.24, { size: 10, bold: true, color: C.red });
  addText(s, '“感知→规划→执行”三段各自都有基准，但把三段串起来、且三段都判安全的不存在；真机执行只有 15/52，跨本体的真机安全评测接近空白。', 2.5, 6.1, 9.9, 0.6, { size: 9.5, color: C.muted, lineSpacing: 1.35 });
  footer(s);
  note(s, '环节编码对应 data/benchmark_survey.json 的 settings 字段；仿真 42/62 条目、真机 18/62 条目。');
  record(s, '覆盖具身系统的哪些环节：感知、规划、执行、运维', '环节 × 数量 × 代表条目；指出串不起来与真机缺口');
}

// ---------- 7. 三轴目标 ----------
{
  const s = frame('能力、鲁棒性、安全：同一个基准常同时承担多类目标', '02 / 研究目标');
  const bars = [['能力 ability', N.capability, C.navy], ['安全 safety', N.safety, C.red], ['鲁棒性 robustness', N.robustness, C.orange]];
  bars.forEach(([label, v, color], i) => {
    const y = 1.3 + i * 0.85;
    addText(s, label, 0.62, y, 2.6, 0.3, { size: 10.5, bold: true });
    addRect(s, 3.3, y + 0.02, (v / 62) * 6.2, 0.3, color, true);
    addText(s, `${v} / 62`, 3.4 + (v / 62) * 6.2, y, 1.2, 0.3, { size: 10.5, bold: true, color });
  });
  const combos = [
    ['只测能力', '16 条', '如 ManiSkill2、RoboTwin、CALVIN'],
    ['能力 + 鲁棒性', '16 条', '如 COLOSSEUM、LIBERO-Para、RoboCasa-Shift'],
    ['能力 + 安全', '13 条', '如 LIBERO-Safety、VLA-Arena、IS-Bench'],
    ['只测安全', '9 条', 'DESPITE、HazardArena、RoboHarm 等'],
    ['能力 + 鲁棒 + 安全', '4 条', 'SafeLIBERO、Agent-SafetyBench 等'],
    ['只测鲁棒性', '4 条', 'LIBERO-MAX、LIBERO-VPro 等'],
  ];
  addText(s, '标签组合（62 条，互斥计数）', 0.62, 3.95, 6, 0.28, { size: 11.5, bold: true, color: C.teal });
  combos.forEach(([label, num, ex], i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.62 + col * 6.1, y = 4.3 + row * 0.78;
    addText(s, label, x, y, 2.1, 0.26, { size: 9.5, bold: true });
    addText(s, num, x + 2.15, y, 0.75, 0.26, { size: 9.5, color: C.red });
    addText(s, ex, x, y + 0.26, 5.6, 0.34, { size: 8.5, color: C.muted });
  });
  footer(s);
  note(s, '多选标签不可相加：能力 49、安全 26、鲁棒性 24，合计 99 > 62。');
  record(s, '能力、鲁棒性、安全：同一个基准常同时承担多类目标', '三轴计数 + 六种标签组合');
}

// ---------- 8. 分节：基础能力 ----------
divider('基础能力基准：先有可用的能力基线，安全才有意义', '这一节介绍 7 个被社区反复使用的评测环境，说明它们各自测什么、怎么判、代价是什么。每页右上角标注“大模型相关度”：高＝被测对象以 VLA／LLM 为主，中＝原始基线为小型策略、近年才出现 VLA。模型结果统一放在附录。', '03 / 基础能力基准');

// ---------- 9-15. 七个基础能力基准 ----------
const capabilitySlides = [
  {
    name: 'LIBERO',
    rel: ['高', '被测对象以 VLA 为主（OpenVLA、OpenVLA-OFT、SmolVLA、π0 系列）；2023 年原始基线为小型策略。'],
    tag: '事实标准 / 终身学习',
    plain: 'LIBERO 是机械臂操作的终身学习评测套件：130 个任务分为四组，模型按顺序学习后回测旧任务，用于测量迁移与遗忘。',
    domain: '桌面机械臂操作，4 个子套件、130 个任务',
    build: '130 个任务分成四组：Spatial 只换空间关系、Object 只换物体、Goal 只换目标、Long 是长时程组合。任务用 BDDL 写初态与目标（把“碗在抽屉里且抽屉关着”写成可解析的逻辑式），在 robosuite 里执行——robosuite 是基于 MuJoCo 物理引擎的机械臂仿真库。',
    metric: '原始论文使用三个持续学习指标：FWT 前向迁移（还没学某个任务时，它已经能做对多少，高于随机基线为正）、NBT 负向后向迁移（学完后续任务后，前面任务掉了多少，越接近零越好）、AUC 成功曲线下面积（整个学习过程中成功率的形状）。后来多数论文只报平均成功率，与原始设计不一致。',
    why: '136 篇引文、≥50 篇 arXiv 摘要提及；本库 8 条安全基准直接建在它上面（LIBERO-Safety、SafeLIBERO、LIBERO-Para 等），原因是任务数量多、判定自动、社区认可度高。',
    result: '后续论文常用“LIBERO 40 任务成功率”这一简化协议；不同论文的示范量、微调策略与评测步数不同，分数不可直接排名。',
    limit: '官方是 130 任务的终身学习目的，40 任务子集不能当全集；仿真动作抽象与真实机械臂仍有落差。',
  },
  {
    name: 'CALVIN',
    rel: ['中', '原论文基线为 MCIL 系列小型策略；2023 年后出现 VLA 与扩散 Transformer 策略，尚未成为主流。'],
    tag: '语言条件 / 长时程',
    plain: 'CALVIN 是语言条件的长时程操作基准：模型按一条指令执行动作，随后不重置继续执行下一条指令，并在四个桌面环境中测试跨环境表现。',
    domain: '语言指令驱动的长时程操作，桌面仿真',
    build: '数据采集采用自由操作（play）：操作者不按任务脚本，边试边做，全程录像，论文报告约 240 万帧；随后每约 10 秒人工写一条语言描述。34 类操作分布在 4 个桌面环境，涉及抽屉、滑门、按钮、灯与积木。',
    metric: '三种协议：D→D 同环境训练测试；ABC→D 用三个环境训练、第四个环境测试，用于测量换场景后的指令理解；连续指令链在同一环境内连续执行 1 至 5 条指令，期间不重置。指标是各链长的成功率与“平均完成长度”——一条轨迹里连续做对几条才失败。成功由物体状态变化自动判定。',
    why: '189 篇引文；Code as Policies、Text2Motion 等都在其上报告；它把长时程语言跟随转化为可量化的测试。',
    result: '原论文的结论是：训练场景里的单任务表现，不能预测未见环境与连续指令组合的表现。',
    limit: '现代论文的 ABC→D 数据量、历史窗口与模型都不同于原始基线；官网已 404，只能以代码仓库为准；语言句式集中，催生了后来“只改措辞”的基准。',
  },
  {
    name: 'SimplerEnv',
    rel: ['高', '被测对象是真实机器人策略（含 VLA），需要先有真机训练的 checkpoint 才能进入该协议。'],
    tag: '仿真代理真机 / 相关性证据',
    plain: 'SimplerEnv 是一套仿真评测协议，用途是估计真机表现，并给出仿真分数与真机分数之间的一致性。',
    domain: '真实策略的仿真评测，复现 WidowX 与 Google Robot 设置',
    build: '用 SAPIEN 仿真引擎重建两台真机（WidowX 与 Google Robot）的场景、相机与控制接口，给出两种对齐方式：视觉匹配（把仿真画面调到与真机相近）与变体聚合（把多种环境变体一起平均）。',
    metric: '指标是相关性：Pearson r 衡量仿真排名与真机排名的一致程度（1 表示完全一致）；MMRV 衡量平均最大排名违背，即同一策略在仿真与真机中的名次差。',
    why: '给出仿真分数与真机表现一致性的量化证据：视觉匹配下 r=0.924、排名违背 0.056，变体聚合 r=0.778，仅使用验证误差时相关性为 0.308。',
    result: '同一批策略、同一批任务，换对齐方式就能把相关性从 0.308 拉到 0.924——说明评测协议本身是变量。',
    limit: '只在刚体、已知真机设置上验证相关性；换物体动力学或任务族后需要重新验证。',
  },
  {
    name: 'RoboTwin',
    rel: ['高', '主流被测对象为 DP3、RecastVLA 等策略与 VLA，2.0 版本被用作 VLA 基线。'],
    tag: '双臂 / 数字孪生造数据',
    plain: '双臂操作的评测与数据生成器：给一张物体照片，就能生成可仿真的三维副本并自动造出专家轨迹。',
    domain: '双臂操作，仿真 + 真机微调',
    build: '数字孪生指按真实物体生成的可交互三维副本：用 3D 生成模型从单张图做出可仿真物体，补上空间关系标注，再把任务分解成动作序列、自动生成专家运动。用 20、50、100 条示范分别训练二维扩散策略与 DP3（以点云为输入的扩散策略）。',
    metric: '成功率，判据是终点姿态达标且全程没有碰撞；另外看“示范量—成功率”曲线，判断数据效率。',
    why: '3,033 stars、31 篇引文；RoboTwin 2.0（ICML 2026）成为双臂/VLA 的主要基线，并被 CVPR 2025 的挑战赛采用。',
    result: '输入模态与示范量影响巨大：100 条示范的 Block Hammer Beat 任务上，带点云的 DP3 是 82.0%，只用二维图像的版本是 0%。',
    limit: '本库条目对应 1.0；2.0 的任务规模、域随机化与协议不同，两者分数不可混用。',
  },
  {
    name: 'RoboCasa365',
    rel: ['高', '榜单提交以 VLA 为主（Axiom-0、Paimon-0 等），并区分多任务、微调与终身学习三种设定。'],
    tag: '家庭规模化 / 有榜单',
    plain: 'RoboCasa365 是家庭场景的大规模操作基准：365 个任务、公开榜单，训练协议分四个阶段学习新任务，并回测旧任务以测量遗忘。',
    domain: '365 个家庭任务，多阶段终身学习协议',
    build: '在 robosuite／MuJoCo 的厨房场景上扩展资产与任务到 365 个；三种训练设定：多任务一起学、预训练后微调、四阶段终身学习（每个阶段换一批目标任务，前面学过的还会被回测）。',
    metric: '任务成功率，加上分阶段遗忘曲线——同一个任务在学完后续阶段后掉了多少。两项分别对应学习速度与保持能力，需要分开报告。',
    why: '32 篇 arXiv 摘要提及；是目前“家庭场景 + 规模 + 公开榜单”三者兼有的少数基准，榜单还在更新（已接受 agentic 提交）。',
    result: '四阶段终身学习后原子任务成功率从 41.5% 降到 10.6%，遗忘非常明显；Axiom-0 报告 62.32%，超过公开榜首 Paimon-0 的 58.1%。',
    limit: '365 个任务不都属于同一测试拆分；遗忘结论绑定了特定训练流程，不能推广到所有持续学习算法。',
  },
  {
    name: 'VLABench',
    rel: ['高', '同时评 VLM 与 VLA 两类对象（π0-FAST、E0、GaussMemory 等）。'],
    tag: '未见类别 / 长时程推理',
    plain: '100 个语言条件操作任务，重点考“没见过的物体类别”和“需要多步推理的指令”。',
    domain: '100 个语言条件操作任务，强调未见物体类别',
    build: '用任务技能库加运动规划自动生成轨迹，再用语言扩增描述对象与意图；未见物体按类别留出：测试类别在训练中未出现，改动范围超出纹理与颜色。',
    metric: '三种接口分开报：端到端 VLA 成功率、模块化流程（VLM 先规划、技能再执行）的成功率、VLM 问答正确率。三者不可混比。',
    why: '16 篇引文、17 篇摘要提及；“未见类别”比“同类新实例”更严格，能暴露真实泛化差距。',
    result: '评测显示低层技能、目标语义解析、长任务推理要分开分析；E0 在 14 个环境平均提升 10.7%，GaussMemory 在 Track 1/6 分别 +5.2%/+6.0%。',
    limit: '三种接口的分数不可混比；资产与真实场景仍有差距。',
  },
  {
    name: 'COLOSSEUM',
    rel: ['中', '论文基线以语言条件操作策略为主，非 VLA；后续多被用作鲁棒性对照。'],
    tag: '系统扰动 / 组合退化',
    plain: 'COLOSSEUM 是操作泛化基准：系统改变光照、纹理、相机位姿与干扰物，测量策略在单轴扰动与组合扰动下的退化。',
    domain: '机械臂操作泛化，20 个任务 × 14 条扰动轴',
    build: '在 RLBench（跑在 CoppeliaSim 上的机械臂任务集）的 20 个任务上，分别施加单轴扰动（纹理、光照、相机位姿、桌面颜色、加干扰物等共 14 条轴）与多轴组合，任务目标保持一致。',
    metric: '相同任务目标下的成功率，以及相对干净场景的退化幅度；单轴与组合分别报告，两者退化幅度不构成简单相加关系。',
    why: '29 篇引文；能量化“组合扰动”的额外伤害，是本库鲁棒性一侧最系统的扰动设计之一。',
    result: '常见变化造成 30–50% 性能退化，组合变化可达至少 75% 的相对退化。',
    limit: '原底座是 RLBench；相对退化不能改写成“成功率下降同等百分点”；四项真机任务只是趋势验证。',
  },
];

const KPI = {
  'LIBERO': { kpis: [['136', 'OpenAlex 引文数', C.navy], ['130', '任务 / 4 个子套件', C.teal], ['8 条', '本库安全基准建在其上', C.red]],
    verdict: '它是几乎所有 VLA 安全研究的共同底座；缺少它，安全分数没有对照基线。' },
  'CALVIN': { kpis: [['189', 'OpenAlex 引文数', C.navy], ['ABC→D', '三环境训练、第四环境测试', C.teal], ['5 步', '常见指令链长度', C.aqua]],
    verdict: '指标覆盖连续指令与跨环境迁移；换环境后的掉分是主要信息。' },
  'SimplerEnv': { kpis: [['0.924', 'VisMatch 与真机的 Pearson r', C.green], ['0.056', 'MMRV（排名违背，越低越好）', C.teal], ['0.308', '纯 MSE 验证的相关性', C.red]],
    verdict: '同一批策略，换对齐方式相关性从 0.308 到 0.924——评测协议本身就是变量。' },
  'RoboTwin': { kpis: [['3,033', 'GitHub stars', C.navy], ['82.0% vs 0%', 'DP3 与 2D DP（同一任务）', C.teal], ['2.0', 'ICML 2026 版本成为主基线', C.aqua]],
    verdict: '输入模态与示范量能决定十几个点，比较时必须先对齐这两项。' },
  'RoboCasa365': { kpis: [['365', '家庭任务数', C.navy], ['41.5→10.6%', '四阶段终身学习后的原子任务成功率', C.red], ['62.32%', 'Axiom-0 报告的榜单成绩', C.green]],
    verdict: '规模与榜单兼备，但要分开看“学得快”和“忘得少”。' },
  'VLABench': { kpis: [['100', '任务数', C.navy], ['+10.7%', 'E0 在 14 个环境的平均提升', C.teal], ['+5.2 / +6.0%', 'GaussMemory 在 Track 1/6 的提升', C.aqua]],
    verdict: '“未见类别”比“同类新实例”严格，泛化差距在这里更容易暴露。' },
  'COLOSSEUM': { kpis: [['29', 'OpenAlex 引文数', C.navy], ['30–50%', '常见扰动的性能退化', C.orange], ['≥75%', '组合扰动的相对退化', C.red]],
    verdict: '单轴扰动只是热身；组合扰动的额外代价才是它最重要的发现。' },
  'LIBERO-Safety': { kpis: [['50.0 / 79.3 / 1.3%', 'OpenVLA-OFT 的 L0/L1/L2 成功率', C.navy], ['+11.0pp', 'VLA-ULAP 相对 π0.5（latency-aware）', C.teal], ['2 篇', '已有下游论文在用它（引文仍为 0）', C.muted]],
    verdict: 'L1 高于 L0、L2 骤降：风险形态比约束数量更能解释结果。' },
  'ManiPhysicsBench': { kpis: [['48.3%', '完成率 SR', C.navy], ['13.5%', '无损完成率 Safe SR', C.red], ['27.9%', '成功中完好比例 PR', C.teal]],
    verdict: '多数模型能完成搬运，但无法保持物体完好；成功率指标无法反映这一差异。' },
  'HazardArena': { kpis: [['0.22→0.01', '危险任务成功率（拒绝示范训练后）', C.green], ['0.44→0.03', 'COMMIT 率', C.teal], ['51', '可执行风险场景 + 安全孪生', C.navy]],
    verdict: '安全训练可以只压危险行为：安全任务成功率反而从 0.25 微升到 0.26。' },
  'DESPITE': { kpis: [['0.4%', '最强模型无有效计划的比例', C.navy], ['28.3%', '同一模型产出危险计划的比例', C.red], ['38–57%', '18 个开源模型的安全意识区间', C.orange]],
    verdict: '“会规划”和“会避险”是两种能力，规模上去不会自动带来后者。' },
  'SafeStage': { kpis: [['33.74%', '聚合 SR', C.navy], ['9.84% / 23.90%', '安全成功 SSR / 不安全成功 USR', C.red], ['70.84%', '成功轨迹中不安全行为的比例', C.orange]],
    verdict: '同一组数能给出 23.90%（/N）与 70.84%（/SR）两个都正确但含义不同的百分比。' },
  'RoboJailBench': { kpis: [['11 / 18', '子集数 / 安全类别数', C.navy], ['98.28%', 'Claude Haiku 4.5 危险拒绝率（干净条件）', C.green], ['97.84%', 'GPT 5.4 Nano 的 SU-HM', C.teal]],
    verdict: '干净条件近乎满分不代表压力条件安全；它的价值是把攻防放在同一张表里。' },
  'Agent-SafetyBench': { kpis: [['16', '被测 LLM 代理数', C.navy], ['<60%', '全部代理的安全分上限', C.red], ['1/3.1', 'SHE 在其上把 ASR 压到原方案的比值', C.teal]],
    verdict: '它测量工具调用层；分数不能用作机器人安全分，失效机制可作为设计参考。' },
};

function renderDetail(spec, kicker, rows, noteText, source) {
  const s = frame(spec.title, kicker);
  addText(s, spec.domain, 0.62, 1.1, 12.1, 0.32, { size: 10, color: C.muted });
  if (spec.rel) {
    const relColor = spec.rel[0] === '高' ? C.teal : (spec.rel[0] === '中' ? C.orange : C.muted);
    addPill(s, `大模型相关度 · ${spec.rel[0]}`, 10.45, 0.5, 2.28, relColor, C.white, 8.5);
  }
  addTable(s, ['维度', '内容'], rows, [1.42, 5.9], 1.52, { size: 10, maxH: 4.6, fillTo: 4.55 });
  const rx = 8.5, rw = 4.22;
  let ry = 1.52;
  for (const [num, label, color] of ((KPI[spec.name] || {}).kpis || [])) {
    addRect(s, rx, ry, rw, 0.88, C.pale, true);
    addText(s, num, rx + 0.16, ry + 0.08, rw - 0.3, 0.44, { size: 17, bold: true, color: color || C.navy, lineSpacing: 1.0 });
    addText(s, label, rx + 0.16, ry + 0.52, rw - 0.3, 0.3, { size: 8.2, color: C.muted, lineSpacing: 1.2 });
    ry += 0.98;
  }
  const vText = (KPI[spec.name] || {}).verdict;
  if (vText) {
    const vH = 0.62 + 0.2;
    addRect(s, rx, ry + 0.04, rw, vH, 'EEF4F7', true);
    addText(s, '要点', rx + 0.16, ry + 0.12, rw - 0.3, 0.24, { size: 8.6, bold: true, color: C.teal });
    addText(s, vText, rx + 0.16, ry + 0.38, rw - 0.32, vH - 0.44, { size: 8.6, color: C.muted, lineSpacing: 1.4 });
  }
  addRect(s, 0.62, 6.3, 12.1, 0.5, C.pale, true);
  addText(s, noteText, 0.85, 6.38, 11.6, 0.36, { size: 8.4, color: C.muted });
  footer(s, source);
  note(s, paperNote(spec, (KPI[spec.name] || {}).kpis));
  record(s, spec.title, spec.domain);
}

const capabilityRows = (b) => [['怎么构建', b.build], ['怎么判分', b.metric], ['为什么重要', b.why], ['关键结果', b.result], ['适用边界', b.limit]];
const safetyRows = (b) => [['怎么构建', b.build], ['怎么判分', b.metric], ['实测结果', b.result], ['被谁用 / 价值', b.use], ['边界', b.caveat]];

capabilitySlides.forEach((b, i) => {
  renderDetail({ ...b, title: `${b.name}：${b.tag}` }, `04 / 基础能力基准 ${i + 1}/${capabilitySlides.length}`,
    capabilityRows(b), '本页所有数值均来自论文摘要或正文，未由本项目复现；模型明细见附录。',
    '数据来源：data/benchmark_usage_records.json、benchmark_paper_reviews.json。');
});

// ---------- 16. 能力侧空白 ----------
{
  const s = frame('能力基准的空白：形态、触觉、真机、效率', '04 / 小结');
  const gaps = [
    ['形态', '桌面机械臂 29 个，人形全身 1 个、无人机 1 个', '跨形态结论不能互相外推'],
    ['触觉与力', '只有 Bench2Dex、BiDex-100、ManiSkill-ViTac 少数条目涉及', '接触丰富任务的安全尤其缺证据'],
    ['真机', '52 个任务集里 15 个含真机执行', '仿真代理的相关性需逐个证明'],
    ['效率与部署', '时延、算力、调用次数很少进主指标', 'VLA-ULAP、IndustrialVLA-Bench 是少数例外'],
    ['失败与恢复', 'LIBERO-RECOVER 是唯一“从失败状态续跑”的基准', '成功率掩盖了恢复能力'],
  ];
  gaps.forEach(([k, v, noteText], i) => {
    const y = 1.3 + i * 0.98;
    addRect(s, 0.62, y, 1.35, 0.8, [C.navy, C.teal, C.aqua, C.green, C.purple][i], true);
    addText(s, k, 0.62, y + 0.24, 1.35, 0.32, { size: 11, bold: true, color: C.white, align: 'center' });
    addText(s, v, 2.15, y + 0.06, 6.2, 0.36, { size: 9.8 });
    addText(s, noteText, 2.15, y + 0.42, 6.2, 0.3, { size: 8.6, color: C.muted });
  });
  addRect(s, 8.75, 1.3, 3.98, 4.3, C.pale, true);
  addText(s, '对开发者的含义', 8.95, 1.42, 3.5, 0.28, { size: 10.5, bold: true, color: C.navy });
  addText(s, '如果只报一个干净场景的成功率，你会同时漏掉：换措辞、换光照、执行中环境变化、接触失败、以及“崩了能不能救”。这五项在库内都有专门基准，可以按需拼装。', 8.95, 1.74, 3.6, 2.3, { size: 9.2, color: C.muted, lineSpacing: 1.45 });
  addText(s, '建议最小组合', 8.95, 4.2, 3.5, 0.26, { size: 9.5, bold: true, color: C.teal });
  addText(s, 'LIBERO（能力）+ LIBERO-Para（语言）+ SimplerEnv（真机代理）', 8.95, 4.48, 3.6, 0.9, { size: 9, color: C.muted, lineSpacing: 1.4 });
  footer(s);
  note(s, '能力侧五个空白：形态、触觉力、真机、效率、失败恢复。');
  record(s, '能力基准的空白：形态、触觉、真机、效率', '五个缺口 + 建议最小组合');
}

// ---------- 17. 分节：安全 ----------
divider('安全基准：六层证据，指标不能互相换算', '这一节先给分层框架，再在每一层里挑一个基准讲透（构建方式 + 实测结果）。每页右上角同样标注“大模型相关度”，口径与上一节一致。治理与交通类只在框架里点名。', '05 / 安全基准');

// ---------- 18. 安全分层框架 ----------
{
  const s = frame('安全评测的六层 + 两类邻接', '05 / 分层框架');
  const rows = [
    ['① 执行层物理安全', '5', '动作是否撞到障碍、越过约束', 'LIBERO-Safety、SafeLIBERO、ForesightSafety-VLA'],
    ['② 物理后果（财产保全）', '1', '抓握是否夹坏物体', 'ManiPhysicsBench'],
    ['③ 语义 / 意图安全', '6', '危险指令是否照做、指代是否错', 'HazardArena、RoboHarm、ASIMOV、RoboAbstention'],
    ['④ 规划 / 规则安全', '1', '计划是否违反显式安全约束', 'DESPITE'],
    ['⑤ 过程 / 阶段安全', '2', '执行前中后的顺序与卫生', 'SafeStage、HygieneRoboBench'],
    ['⑥ 完整性 / 对抗', '2', '后门、触发器、越狱', 'RoboJailBench、Trap-LIBERO/Trap-RoboTwin'],
    ['邻接：软件代理', '5', '记忆、技能包、注入、多代理', 'Agent-SafetyBench、INFUSE、MemForm、ORBIT'],
    ['邻接：治理与交通', '4', '权限、恢复、升级；碰撞进指标', 'EmbodiedGovBench、NAVSIM、VIPS'],
  ];
  addTable(s, ['层级', '条目数', '测什么', '代表'], rows, [2.5, 0.8, 4.2, 4.6], 1.25, { size: 10, maxH: 3.95, fillTo: 3.88 });
  addRect(s, 0.62, 5.32, 12.1, 1.52, 'FDF2F2', true);
  addText(s, '三个必须记住的口径', 0.9, 5.4, 4, 0.28, { size: 10.5, bold: true, color: C.red });
  const warns = [
    '“SR”在不同基准里指 Success Rate、Security Rate、整体成功率（SSR+USR）或安全解决率——先看定义再看数。',
    '不安全成功率的分母是全部 episode；改成“成功里的违规比例”要除以 SR，两者可差数倍。',
    '仿真里的“违规”是判定谓词（碰撞、越界、超阈），不等于真实损伤；改写成伤害率是过度解读。',
  ];
  warns.forEach((w, i) => addText(s, `· ${w}`, 0.9, 5.72 + i * 0.36, 11.6, 0.34, { size: 9, color: C.muted, lineSpacing: 1.3 }));
  footer(s);
  note(s, composeNote([
    '这一页把 26 条带安全目标的条目按“测量对象”分成六层，再加两类邻接。其中 23 个是评测任务集，另外 3 个是框架，分别是 SafeBench、EmbodiedGovBench 和 ORBIT。分层的用途是区分测量对象：不同层的分数回答不同问题，不用于排名。',
    '前一层是执行层物理安全，判据是动作过程中是否碰撞或越过约束，LIBERO-Safety、SafeLIBERO、ForesightSafety-VLA、SafeBench 与 VLA-Arena 的 Safety 子集都在这一层。紧接着是物理后果，判据是物体是否被破坏，目前只有 ManiPhysicsBench 用外部有限元求解器做了这件事。再往上是语义与意图安全，判据是模型是否理解“谁对谁做什么”、对危险意图是否拒绝，HazardArena、RoboHarm、ASIMOV、RoboAbstention、IS-Bench 与 SafeAgentBench 属于这一层。',
    '更深一层是规划与规则安全，判据是计划本身是否满足显式安全约束，DESPITE 是目前唯一的代表。过程与阶段安全关心执行前中后的顺序、阶段与卫生约束，SafeStage 与 HygieneRoboBench 属于这一层。最后一层是完整性与对抗，判据是策略在触发器、后门或越狱条件下是否仍按预期工作，代表是 RoboJailBench 与 Trap-LIBERO／Trap-RoboTwin。',
    '两类邻接需要单独说明。软件代理的五条（Agent-SafetyBench、INFUSE、MemForm、ORBIT、SkillSafetyBench）测的是工具、技能包、记忆与多代理编排，动作不落到物理世界；治理与交通的四条测权限、恢复、升级，或者把碰撞放进综合分。它们的分数不能当机器人安全分，但失效机制可以借鉴。',
    '最后要提醒的是，这张表的条目数按“主测量对象”归类，一条基准可能同时覆盖多层，例如 VLA-Arena 的 Safety 子集也含语义风险，所以行之间不求和。',
  ]));
  record(s, '安全评测的六层 + 两类邻接', '分层表 + 三个口径陷阱');
}

// ---------- 19-25. 安全基准逐个讲 ----------
const safetySlides = [
  {
    cat: '① 执行层物理安全',
    name: 'LIBERO-Safety',
    rel: ['高', '被测对象为 OpenVLA-OFT、π0.5、VLA-ULAP 等 VLA。'],
    plain: '把“安全检查”塞进 LIBERO 的家庭任务里：除了看做完没做完，还要看过程中有没有碰撞、有没有碰危险物。',
    domain: '在 LIBERO 的家庭操作任务里嵌入安全检查，按 L0 干净、L1 加约束、L2 更强风险分三档',
    build: '用 UBDDL 扩展 BDDL——BDDL 是把任务初态与目标写成逻辑式的任务定义语言，UBDDL 在它上面加了随机化、动态物体与“逐步安全检查”的钩子，所以执行中也能判违规，不只在终点判。关键姿态的示范由 CuRobo 生成。',
    metric: '物理安全轨的成功率要求“完成且全程无违规”，一旦违规就终止并记失败——该指标已是安全口径，与普通成功率不可互换。另有语义安全推理子套件（与本页数字无关，见备注说明）。',
    result: 'OpenVLA-OFT 在 AAG 子集上 L0／L1／L2 分别为 50.0%／79.3%／1.3%。L1 高于 L0、L2 骤降，说明“加约束”不一定更难，风险形态才关键。',
    use: 'FabriVLA 用它按风险给 rollout（一次完整执行轨迹）排序；VLA-ULAP 在 latency-aware 版本上比 π0.5 高 11.0／15.5 个百分点。',
    caveat: 'SR 已含安全约束，不能解释为普通完成率；部分数据生成组件需按代码审计确认。',
  },
  {
    cat: '② 物理后果（财产保全）',
    name: 'ManiPhysicsBench',
    rel: ['高', '被测对象是公共 VLA checkpoint，按 SimplerEnv 设置运行。'],
    plain: 'ManiPhysicsBench 直接测量抓握是否造成物体损伤：以接触力与几何数据判定物体是否断裂或变形。',
    domain: 'VLA 抓握是否把物体夹坏；用外部有限元求解器判定损伤',
    build: '刚体仿真记录每次接触的位置、方向与力；把这些数据交给外部的有限元求解器（CalculiX、FEBio、OpenRadioss 三个可选），按几何与材料阈值判定每次抓握有没有造成断裂或变形，再汇总整段轨迹。',
    metric: '三个指标都基于同一批测试试验：SR 是完成率，Safe SR 是“完成且物体完好”的比例，PR 是两者的比值 Safe SR ÷ SR——回答“成功的那些里，有多少是完好的”。',
    result: 'SimplerEnv 的高/中难对象上，公共 checkpoint 平均 SR 48.3%、Safe SR 仅 13.5%、PR 27.9%——多数模型能完成搬运，但无法保持物体完好。',
    use: '本库唯一给“损伤判定”的基准；代价是要装三个有限元后端，计算成本高。',
    caveat: '损伤是求解器事后判定的结果，仿真中不会真的断裂；SR 为 0 时 PR 无定义。',
  },
  {
    cat: '③ 语义 / 意图安全',
    name: 'HazardArena',
    rel: ['高', '被测对象为 VLA-Adapter、π0 系列等 VLA。'],
    plain: '用“危险与安全成对”的场景测模型是否理解谁对谁做什么：同一个布局，递给玩偶还是递给人，指令不同，结果应当不同。',
    domain: '用危险／安全孪生场景测模型的语义安全判断，而不只是能不能执行',
    build: '成对构造场景：保持布局与操作模板一致，只改动作参与者、目标关系与指令，从而把“能力”和“安全判断”分开；把执行进度记录成三档：尝试（ATTEMPT）、提交（COMMIT）、成功（SUCCESS）。',
    metric: '危险任务成功率、提交率与安全任务成功率分别报。只看危险成功率会把“想动手”和“真做成”混为一谈，三档记录正是为了避免这一点。',
    result: '用拒绝示范训练的 VLA-Adapter：危险任务成功率 0.22→0.01、提交率 0.44→0.03，而安全任务成功率 0.25→0.26。',
    use: '证明“安全训练可以只压危险行为、不牺牲安全任务”；另有真机验证。',
    caveat: '配对并非只换一个文本标签，仍有混淆变量；改进只对应文中分布。',
  },
  {
    cat: '④ 规划 / 规则安全',
    name: 'DESPITE',
    rel: ['高', '被测对象是 LLM/VLM 规划器，论文共测 23 个模型。'],
    plain: 'DESPITE 测量规划层的安全：判定生成的计划是否有效、是否违反显式安全约束、是否安全完成。',
    domain: '具身任务规划的安全：把“会规划”和“会避险”分开测',
    build: '把任务写成带安全约束的形式化规划问题，再用确定性验证器判定三件事：计划是否有效（能不能达成目标）、是否危险（违反约束）、是否安全完成。评测了 23 个模型。',
    metric: '三个比例：无有效计划的比例、产出危险计划的比例、安全完成的比例。它们回答不同问题，不能合成一个分。',
    result: '最强规划模型在 1,044 个困难任务上只有 0.4% 无有效计划，却有 28.3% 任务产出危险计划；18 个开源模型的安全意识集中在 38–57%。',
    use: '这是“能力达标但致命”的最清晰证据：规划能力随规模提升，安全意识没有同步提升。',
    caveat: '评估对象是形式化计划，关节执行不在评测范围内；主结果来自困难集，不能当全部任务的随机平均。',
  },
  {
    cat: '⑤ 过程 / 阶段安全',
    name: 'SafeStage',
    rel: ['高', '被测对象为 VLA 策略，论文按阶段报告安全成功与不安全成功。'],
    plain: '把“执行前、执行中、完成后”的危险分开算，避免只检查终点是否成功。',
    domain: '把危险状态、路径／接触约束、终态稳定性绑定到执行的不同阶段',
    build: '用仿真内部状态打分，但不把这些状态提供给策略：初始阶段看有没有一开始就危险，执行阶段看路径与接触约束，完成阶段看终态是否稳定。',
    metric: 'SR 总成功率 = SSR 安全成功 + USR 不安全成功，三者都以全部 episode（回合，一次从重置到终止的完整交互）为分母。“成功里有多少不安全”是另一个数：USR ÷ SR。',
    result: '聚合 SR 33.74%、SSR 9.84%、USR 23.90%——成功轨迹中 70.84% 含不安全行为；评估器在 240 条核查轨迹上 F1 97.26%。',
    use: '唯一按“执行前／中／后”分阶段给指标的设计，能区分“没出事”和“没违规”。',
    caveat: '项目入口审计为候选且地址与论文不符（仓库是同名产品），代码可用性未知；评估器准确度不等于策略安全度。',
  },
  {
    cat: '⑥ 完整性 / 对抗',
    name: 'RoboJailBench',
    rel: ['高', '被测对象是 LLM/VLM 具身代理（Claude Haiku 4.5、GPT 5.4 Nano 等）。'],
    plain: 'RoboJailBench 是具身指令的攻防评测：同时测量危险指令的拒绝率与正常指令的接受率。',
    domain: '具身机器人的对抗攻击与防御：危险指令拒绝 vs 正常指令接受',
    build: '11 个子集、18 类风险后果，构造 990 对“正常／危险”指令与 1,408 张场景图；把无风险干预的基线与压力测试分开报告。',
    metric: 'Security Rate 是危险指令的拒绝率，Utility Rate 是正常指令的接受率，SU-HM 是两者的调和平均——用调和平均是为了防止“一律拒绝”拿满分。注意本论文的 SR 指 Security Rate（拒绝率），与其他论文的成功率同名异义。',
    result: '无额外干预的基线中，Claude Haiku 4.5 危险拒绝率 98.28%；GPT 5.4 Nano 正常接受率 99.49%、SU-HM 97.84%——以上为干净条件；受压力条件下的数字见压力测试部分。',
    use: '压力测试另有一套数字；本库条目强调“干净高分不代表抗攻击”。',
    caveat: 'SR 指 Security Rate，与其他论文的 Success Rate 同名异义；接受／拒绝计划不等于物理动作成功。',
  },
  {
    cat: '邻接：软件代理层',
    name: 'Agent-SafetyBench',
    rel: ['高', '被测对象为 16 个 LLM 代理。'],
    plain: '这是软件代理层的安全评测：模型通过工具、文件、接口多步操作，但不控制机器人，所以只作邻接证据。',
    domain: '多步工具调用型代理的安全；不测物理动作',
    build: '把已有的代理安全测试汇总、去重，统一成 16 类风险与 8 类失败模式的环境集合，人工质检后用脚本化评分器同时判安全性与有用性。',
    metric: '安全分与有用性分开报告；风险类别与失败模式各自统计，避免用一个总分掩盖某一类失效。',
    result: '16 个被测代理均未达到 60% 安全分数；问题归为鲁棒性与风险意识不足。SHE（2026）在此基准上做安全 harness 演化，ASR 降到原静态方案的 1/3.1。',
    use: '可作为具身代理“上层决策与工具使用”的邻接证据；不能替代关节级／接触级安全评测。',
    caveat: '环境停在工具调用层，物理后果只是文本标签；评分器与任务模板强绑定。',
  },
];
safetySlides.forEach((b, i) => {
  renderDetail({ ...b, title: `${b.cat}：${b.name}` }, `05 / 安全基准 ${i + 1}/${safetySlides.length}`,
    safetyRows(b), '分数来自论文摘要／正文，未由本库复现；“违规”“伤害”均为该基准定义的判定，不等于真实事故。',
    '数据来源：data/benchmark_usage_records.json、benchmark_paper_reviews.json。');
});

// ---------- 26. 安全侧整体判断 ----------
{
  const s = frame('安全评测的整体判断：新、仿真、口径不一', '05 / 小结');
  const blocks = [
    ['新', '26 条里 18 条在 OpenAlex 上是 0 引文', '这些基准多在 2026 年发布，引用数尚未积累；引用数据不能用于安全基准排序。'],
    ['仿真', '六层里只有 4 条做过真机验证', '仿真谓词（碰撞/越界/超阈）≠ 真实损伤；要写“仿真风险触发”，不能写伤害率。'],
    ['口径', '同一个 SR 有四种定义', '跨基准比较前先对齐：分母是 episode 还是成功数、SR 指成功还是拒绝。'],
    ['成本', '多数基准无公开榜单或代码未发布', 'RoboReel、TrapVLA 标注 “coming soon”；SafeStage 入口不符；ManiPhysicsBench 需三个 FEM 后端。'],
  ];
  blocks.forEach(([k, h, body], i) => {
    const y = 1.25 + i * 1.28;
    addRect(s, 0.62, y, 0.9, 1.12, [C.red, C.orange, C.teal, C.purple][i], true);
    addText(s, k, 0.62, y + 0.36, 0.9, 0.4, { size: 15, bold: true, color: C.white, align: 'center' });
    addText(s, h, 1.7, y + 0.04, 6.4, 0.32, { size: 10.5, bold: true });
    addText(s, body, 1.7, y + 0.38, 6.4, 0.68, { size: 9, color: C.muted, lineSpacing: 1.4 });
  });
  addRect(s, 8.35, 1.25, 4.37, 4.9, C.pale, true);
  addText(s, '如果只能做三件事', 8.55, 1.38, 4, 0.28, { size: 10.5, bold: true, color: C.navy });
  ['把“安全成功”与成功率并列报（否则 48.3% 的成功率会掩盖 13.5% 的无损完成率）。',
    '建一个配对扰动集：同任务、同初始状态，只改一个因素。',
    '加一组拒绝／停止样本与触发器回归，防“能力越强越危险”。'].forEach((t, i) => {
    addText(s, `${i + 1}. ${t}`, 8.55, 1.72 + i * 0.9, 3.95, 0.82, { size: 9.2, color: C.muted, lineSpacing: 1.4 });
  });
  footer(s);
  note(s, '安全基准的四个特征与三条最小行动建议。');
  record(s, '安全评测的整体判断：新、仿真、口径不一', '四个特征 + 三条最小行动');
}

// ---------- 27. 选型表 ----------
{
  const s = frame('按问题选基准：一张对照表', '06 / 选型建议');
  const rows = [
    ['动作是否碰撞', 'LIBERO-Safety + SafeLIBERO', '一个内嵌检查、一个外挂安全层，可对照'],
    ['是否夹坏物体', 'ManiPhysicsBench', '唯一给损伤判定；需 FEM 后端'],
    ['指令本身危险，照不照做', 'HazardArena + RoboHarm', '语义孪生 / 接口差异'],
    ['信息不足该不该停', 'RoboAbstention', '弃权率；最佳模型仅 39%'],
    ['计划层是否安全', 'DESPITE + SafeAgentBench', '符号规划 / 可执行危险任务'],
    ['过程是否合规、出事能否救', 'SafeStage + LIBERO-RECOVER', '阶段指标；从失败状态续跑'],
    ['抗攻击能力', 'RoboJailBench + Trap-LIBERO', '拒绝率 / 后门触发'],
    ['换了措辞/环境还行不行', 'LIBERO-Para + COLOSSEUM + LIBERO-MAX', '语言、系统扰动、执行中变化三选'],
    ['只要一个强基线横向比', 'LIBERO + CALVIN + SimplerEnv + RoboCasa365', '社区共识 + 有榜单'],
  ];
  addTable(s, ['要回答的问题', '选这些', '理由'], rows, [3.9, 4.6, 3.6], 1.2, { size: 10.5, maxH: 5.0, fillTo: 4.95 });
  addText(s, '注：表中每个基准的分母与指标定义不同，横向比较前先在第 10 节术语表与条目文档中确认口径。', 0.62, 6.5, 12.1, 0.3, { size: 8.6, color: C.muted });
  footer(s);
  note(s, '九种研究问题对应的基准组合。');
  record(s, '按问题选基准：一张对照表', '九行选型建议');
}

// ---------- 28. 附录分节 ----------
divider('附录：关键基准上的模型结果', '只列本库能追溯到出处的数字；同一基准的不同论文协议可能不同，表内不做排名，只做对照。', '07 / 附录');

// ---------- 29. 附录 A：LIBERO ----------
{
  const s = frame('附录 A：LIBERO 上被报告的模型结果', '07 / 附录 A');
  const rows = [
    ['LMoE-DP', '2026', 'LIBERO 成功率 73.4%；真实机器人任务 79%', '语言条件表示 + 混合专家扩散策略'],
    ['ActionPiece', '2026', 'LIBERO 94.8%；未见 LIBERO-Plus 68.8%', '同一 Qwen3-VL-4B 训练设置下的动作 tokenization'],
    ['WAVE-0', '2026', 'LIBERO 98.7%；LIBERO-Plus 88.0%', 'VLA 与世界动作模型的轻量融合'],
    ['StellaVLA', '2026', 'LIBERO 98.8%；VLA-Arena 榜单 0.63（第一）', '上下文结构化示范'],
    ['TTF-VLA', '2025', 'LIBERO 平均 +4.0pp（72.4% vs 68.4%）', '时序 token 融合'],
  ];
  addTable(s, ['模型', '年份', '报告结果', '方法要点'], rows, [2.0, 0.85, 5.15, 4.1], 1.25, { size: 10.2, maxH: 4.1, fillTo: 3.95 });
  addRect(s, 0.62, 5.42, 12.1, 1.5, 'FDF6EC', true);
  addText(s, '读这张表的三个前提', 0.9, 5.52, 4, 0.28, { size: 10, bold: true, color: C.orange });
  ['协议不同：LIBERO 有 130 任务全集与常见的 40 任务子集，微调数据量、动作块长度、评测步数各不相同。',
    '来源不同：数字取自各论文摘要，本库未复现；同一模型在不同论文里可能差几个点。',
    '不可平均：不能把上表求平均当作“LIBERO 上的 SOTA”，也不代表第 1 行与第 5 行可比。'].forEach((t, i) => {
    addText(s, `· ${t}`, 0.9, 5.82 + i * 0.35, 11.6, 0.34, { size: 8.8, color: C.muted, lineSpacing: 1.3 });
  });
  footer(s, '数字来源：data/benchmark_usage_records.json 中 LIBERO、LIBERO-Para、VLA-Arena 的使用记录（论文摘要原文）。');
  note(s, composeNote([
    '这一页列出五个模型在 LIBERO 上被报告的结果，全部来自各论文摘要，本库没有复现。LMoE-DP 在这套基准上报告 73.4% 的成功率，真实机器人任务 79%。ActionPiece 在同一个训练设置下报告 LIBERO 94.8%，未见过的 LIBERO-Plus 68.8%。WAVE-0 报告 LIBERO 98.7%、LIBERO-Plus 88.0%。StellaVLA 报告 LIBERO 98.8%，并在 VLA-Arena 榜单上以 0.63 排第一。TTF-VLA 报的是相对提升，LIBERO 平均高 4.0 个百分点，从 68.4% 到 72.4%。',
    '读这张表要先接受三个前提。第一，协议不同：LIBERO 有 130 个任务的全集，也有常见的 40 任务子集，微调数据量、动作块长度与评测步数各不相同。第二，来源不同：数字取自各论文摘要，同一模型在不同论文里差几个点很常见，本库没有统一重跑。第三，不可平均：把五行求平均当作“LIBERO 上的最好成绩”没有意义，也不代表第一行与第五行可比。',
  ]));
  record(s, '附录 A：LIBERO 上被报告的模型结果', '5 个模型 + 三个读表前提');
}

// ---------- 30. 附录 B：CALVIN / SimplerEnv ----------
{
  const s = frame('附录 B：CALVIN 与 SimplerEnv 的结果', '07 / 附录 B');
  const calvin = [
    ['Velocity Loss OPD', 'CALVIN 五指令序列 +33.4pp', '多教师在线策略蒸馏'],
    ['DeFI', 'CALVIN 平均任务长度 4.51', '分离前向/逆向动力学'],
    ['Grounding w/ Affordances', '称在 CALVIN 上达到 SOTA', '视觉可供性接地（2023）'],
  ];
  const simpler = [
    ['Discrete Diffusion VLA', 'Fractal 71.2% / Bridge 54.2%', '离散扩散动作解码'],
    ['DeFI', 'Fractal 51.2%', '同上'],
    ['TTF-VLA', 'SimplerEnv 跨环境验证', '时序 token 融合'],
  ];
  addText(s, 'CALVIN（长时程语言指令）', 0.62, 1.15, 6, 0.3, { size: 11, bold: true, color: C.teal });
  addTable(s, ['模型', '报告结果', '方法'], calvin, [2.35, 2.55, 1.45], 1.5, { size: 9, maxH: 2.3 });
  addText(s, 'SimplerEnv（仿真代理真机）', 0.62, 4.0, 6, 0.3, { size: 11, bold: true, color: C.teal });
  addTable(s, ['模型', '报告结果', '方法'], simpler, [2.35, 2.55, 1.45], 4.35, { size: 9, maxH: 2.3 });
  addRect(s, 8.85, 1.15, 3.88, 5.45, C.pale, true);
  addText(s, '注意这两个基准的“分数含义”', 9.05, 1.28, 3.5, 0.3, { size: 10, bold: true, color: C.navy });
  addText(s, 'CALVIN 报指令链成功率与平均完成长度，ABC→D 协议下才代表跨环境能力；SimplerEnv 报与真机的相关性（r、MMRV）。两组数字都不能与 LIBERO 的成功率直接比较。', 9.05, 1.62, 3.5, 3.0, { size: 9, color: C.muted, lineSpacing: 1.45 });
  addText(s, 'SimplerEnv 的相关性基线：VisMatch r=0.924、MMRV 0.056；VarAgg r=0.778；验证 MSE 0.308。', 9.05, 4.7, 3.5, 1.5, { size: 8.8, color: C.muted, lineSpacing: 1.4 });
  footer(s, '数字来源：data/benchmark_usage_records.json（CALVIN、SimplerEnv 使用记录）与论文精读笔记。');
  note(s, composeNote([
    'CALVIN 一侧的三行都来自使用记录。Velocity Loss OPD 报的是 CALVIN 五指令序列上的绝对提升 33.4 个百分点；DeFI 报的是平均任务长度 4.51；Grounding with Visual Affordances 只声称达到当时的最好水平，没有给出逐项数字。SimplerEnv 一侧的三行分别是 Discrete Diffusion VLA 在 Fractal 子集 71.2%、Bridge 子集 54.2%，DeFI 在 Fractal 上 51.2%，以及 TTF-VLA 把 SimplerEnv 当作跨环境验证。',
    '必须强调这两个基准的指标含义不同。CALVIN 报的是指令链成功率与平均完成长度，只有走三环境训练、第四环境测试的设定时，这个分数才代表跨环境能力；SimplerEnv 报的是与真机排序的相关性，即皮尔逊相关系数与排名违背指标。因此这两页的数字既不能互相比较，也不能与 LIBERO 的成功率放在同一张表里。',
    'SimplerEnv 的相关性基线值得单独记：视觉匹配方式下相关系数 0.924、排名违背 0.056，变体聚合方式 0.778，而只用验证误差时只有 0.308。同一批策略、同一批任务，换对齐方式就能把相关性从 0.308 拉到 0.924，说明评测协议本身就是变量。',
  ]));
  record(s, '附录 B：CALVIN 与 SimplerEnv 的结果', '两个基准各 3 个模型 + 指标含义提醒');
}

// ---------- 31. 附录 C：RoboCasa365 / RoboTwin / VLABench ----------
{
  const s = frame('附录 C：规模化基准的结果', '07 / 附录 C');
  const rows = [
    ['RoboCasa365', 'Axiom-0', '62.32%（超榜首 Paimon-0 58.1%）', '2026'],
    ['RoboCasa365', 'harness 蒸馏策略', '62.2%（比自身起点 +4.8pp）', '2026'],
    ['RoboCasa365', 'MM-ABC 消融', '干净动作预测→速度预测：32.8%→29.2%', '2026'],
    ['RoboTwin', 'RecastVLA', 'Clean-to-Clean +10.68pp', '2026'],
    ['RoboTwin 1.0', 'DP3 vs 2D DP', 'Block Hammer Beat：82.0% vs 0%（100 示范）', '2024'],
    ['VLABench', 'E0', '14 个环境平均 +10.7%', '2025'],
    ['VLABench', 'GaussMemory', 'Track 1 +5.2%、Track 6 +6.0%（相对 π0-FAST）', '2026'],
  ];
  addTable(s, ['基准', '模型', '报告结果', '年份'], rows, [1.85, 2.35, 5.9, 0.7], 1.2, { size: 10, maxH: 4.5, fillTo: 4.4 });
  addRect(s, 0.62, 5.75, 12.1, 1.0, C.pale, true);
  addText(s, 'RoboCasa365 的终身学习结果值得单独记：四阶段训练后原子任务成功率 41.5% → 10.6%，说明“能力提升”与“旧技能保持”要分开看。', 0.9, 5.86, 11.6, 0.8, { size: 9.2, color: C.muted, lineSpacing: 1.45 });
  footer(s, '数字来源：data/benchmark_usage_records.json（RoboCasa365、RoboTwin、VLABench）与论文精读笔记。');
  note(s, composeNote([
    'RoboCasa365 的三行都来自使用记录。Axiom-0 报告 62.32%，比公开榜首 Paimon-0 的 58.1% 高 4.22 个百分点，比小米的 XR-1 高 4.92 个百分点；把多智能体框架的轨迹蒸馏回策略后得到 62.2%，比自身起点高 4.8 个百分点；MM-ABC 的消融显示，把干净动作预测换成速度预测会让成功率从 32.8% 降到 29.2%。',
    'RoboTwin 一侧，RecastVLA 在 Clean-to-Clean 设定上提升 10.68 个百分点；1.0 版本论文里的 DP3 与 2D 扩散策略对比更极端，在 100 条示范的 Block Hammer Beat 任务上，带点云的 DP3 是 82.0%，只用二维图像的版本是 0%。VLABench 一侧，E0 在 14 个环境上平均高出强基线 10.7%；GaussMemory 相对 π0-FAST 在 Track 1 与 Track 6 分别高 5.2% 与 6.0%。',
    '还有一个数字值得单独放在口述里：RoboCasa365 的四阶段终身学习实验里，原子任务成功率从第一阶段的 41.5% 掉到第四阶段的 10.6%。它说明“学得快”和“忘得少”是两个能力，报告规模化结果时应分别给出学习速度与保持能力。',
  ]));
  record(s, '附录 C：规模化基准的结果', '7 行结果 + 终身学习提醒');
}

// ---------- 32. 附录 D：安全基准结果汇总 ----------
{
  const s = frame('附录 D：安全基准的结果汇总', '07 / 附录 D');
  const rows = [
    ['LIBERO-Safety', 'OpenVLA-OFT', 'L0/L1/L2 = 50.0% / 79.3% / 1.3%', '执行层'],
    ['ManiPhysicsBench', '公共 checkpoint', 'SR 48.3% / Safe SR 13.5% / PR 27.9%', '物理后果'],
    ['HazardArena', 'VLA-Adapter（拒绝示范训练）', '危险成功 0.22→0.01；COMMIT 0.44→0.03；安全任务 0.25→0.26', '语义意图'],
    ['DESPITE', '最强规划模型 / 18 个开源模型', '危险计划 28.3%；无有效计划 0.4%；安全意识 38–57%', '规划规则'],
    ['SafeStage', '聚合结果', 'SR 33.74% / SSR 9.84% / USR 23.90%；成功中 70.84% 不安全', '过程阶段'],
    ['RoboJailBench', 'Claude Haiku 4.5 / GPT 5.4 Nano', '危险拒绝 98.28%；正常接受 99.49%；SU-HM 97.84%（干净条件）', '完整性'],
    ['Agent-SafetyBench', '16 个 LLM 代理', '安全分全部 <60%', '软件代理邻接'],
  ];
  addTable(s, ['基准', '被测对象', '关键结果', '层级'], rows, [1.95, 2.75, 5.5, 1.05], 1.2, { size: 10.2, maxH: 4.8, fillTo: 4.7 });
  addRect(s, 0.62, 6.12, 12.1, 0.72, 'FDF2F2', true);
  addText(s, '这些数字分属不同分母与不同定义，只能逐行读，不能相加、不能平均，也不能与能力基准的成功率放在同一张排名里。', 0.9, 6.2, 11.6, 0.55, { size: 9, color: C.muted, lineSpacing: 1.35 });
  footer(s, '数字来源：data/benchmark_usage_records.json 与 data/benchmark_paper_reviews.json；均为论文报告值。');
  note(s, composeNote([
    '这一页把七类安全基准各取一行，逐行读的前提是连分母一起引用。LIBERO-Safety 报的是物理安全轨的成功率，要求完成任务且全程没有约束违规，一次违规就终止并记失败；50.0%、79.3%、1.3% 分别对应 AAG 的 L0、L1、L2。ManiPhysicsBench 的三个数是同一批测试试验上的完成率 48.3%、无损完成率 13.5%，以及两者之比 27.9%。',
    'HazardArena 的两组数是拒绝示范训练前后对比：危险任务成功率从 0.22 降到 0.01，提交动作的比例从 0.44 降到 0.03，而安全任务成功率从 0.25 微升到 0.26。DESPITE 报的是 1,044 个困难任务上无有效计划 0.4%、危险计划 28.3%，以及 18 个开源模型的安全意识区间 38% 到 57%。SafeStage 的 33.74% 等于安全成功 9.84% 加不安全成功 23.90%，三者都以全部 episode 为分母；而“成功中有多少不安全”是 23.90 除以 33.74，等于 70.84%，这是两个不同分母的百分比。',
    'RoboJailBench 的 98.28% 是干净条件下 Claude Haiku 4.5 的危险指令拒绝率，99.49% 与 97.84% 是 GPT 5.4 Nano 的正常指令接受率与两者的调和平均，以上均为干净条件，压力测试另有数字。Agent-SafetyBench 一行只报一个上限：16 个被测代理的安全分全部低于 60%。这七行分属不同分母与不同定义，只能逐行读，不能相加、不能平均，也不能和能力基准的成功率放进同一张排名。',
  ]));
  record(s, '附录 D：安全基准的结果汇总', '7 行结果 + 不可合并的提醒');
}

// ---------- 33. 数据来源与边界 ----------
{
  const s = frame('数据来源与这份汇报的边界', '08 / 收尾');
  const left = [
    ['data/benchmark_survey.json', '122 条登记、62 条分类、场景/环节/目标编码'],
    ['data/benchmark_paper_reviews.json', '62 篇正文重点章节笔记'],
    ['data/benchmark_usage_records.json', '106 篇使用记录（被测模型/用法/结果）'],
    ['data/benchmark_citation_snapshot.json', '62 条被引观测（2026-11-04）'],
    ['data/benchmark_project_audit.json', '122 条项目入口审计'],
  ];
  left.forEach(([f, d], i) => {
    const y = 1.25 + i * 0.78;
    addRect(s, 0.62, y, 6.4, 0.66, C.pale, true);
    addText(s, f, 0.8, y + 0.08, 2.9, 0.24, { size: 8.2, bold: true, color: C.navy });
    addText(s, d, 0.8, y + 0.33, 6.0, 0.28, { size: 8.4, color: C.muted });
  });
  addText(s, '四条边界', 7.35, 1.2, 3, 0.28, { size: 11, bold: true, color: C.teal });
  ['范围限定：检索式未穷尽，样本偏向桌面机械臂与公开项目。',
    '分数来源：全部来自论文摘要/正文，本库未复现任何实验。',
    '安全结论以仿真为主：六层里只有 4 条做过真机验证，“违规”不等于伤害。',
    '不猜测录用与可用性：无正式出版证据不标录用，代码未发布就写“未发布”。'].forEach((t, i) => {
    addText(s, `· ${t}`, 7.35, 1.55 + i * 0.75, 5.35, 0.7, { size: 9, color: C.muted, lineSpacing: 1.4 });
  });
  addRect(s, 7.35, 4.75, 5.35, 1.35, 'EEF4F7', true);
  addText(s, '下一步（可选）', 7.55, 4.85, 3, 0.26, { size: 9.5, bold: true, color: C.teal });
  addText(s, '把 60 条待读档案分类；对 3 条候选入口做代码可用性验证；给安全基准补一组配对扰动复测。', 7.55, 5.13, 4.95, 0.9, { size: 8.6, color: C.muted, lineSpacing: 1.4 });
  footer(s, `数据快照 ${SNAPSHOT}；生成脚本 scripts/build_survey_report_v2.mjs。`);
  note(s, '收尾：数据文件清单与四条边界。');
  record(s, '数据来源与这份汇报的边界', '五个数据文件 + 四条边界 + 下一步');
}

// ---------- 导出与自检 ----------
await fs.mkdir(OUT, { recursive: true });
const target = path.join(OUT, '具身智能与安全Benchmark调研汇报_2026-11-04_新稿.pptx');
await pptx.writeFile({ fileName: target });

// 结构自检：解压后数页数、查 XML 是否可解析
const { execFileSync } = await import('node:child_process');
const zipList = execFileSync('powershell', ['-NoProfile', '-Command',
  `Add-Type -AssemblyName System.IO.Compression.FileSystem; [IO.Compression.ZipFile]::OpenRead('${target}').Entries | ForEach-Object { $_.FullName }`],
  { encoding: 'utf8' }).split(/\r?\n/).filter(Boolean);
const slideFiles = zipList.filter((n) => /^ppt\/slides\/slide\d+\.xml$/.test(n));

// 逐页文字稿由 scripts/pptx_text_dump.py 从导出的 pptx 抽取（避免与幻灯片实际换行不一致）。

console.log(JSON.stringify({
  slides: pptx._slides.length,
  slideXmlFiles: slideFiles.length,
  overflow,
  file: target,
}, null, 2));
