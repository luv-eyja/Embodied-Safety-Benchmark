/**
 * 安全主线调研汇报（新稿，独立文件，不覆盖既有 PPT）。
 * 结构：范围与口径 → 术语 → 总量/场景/载体/判据 → 安全基准 12 讲 → 横切对比 → 索引 → 能力底座（压缩）→ 选型与缺口。
 * 数字来自 data/benchmark_survey.json、benchmark_paper_reviews.json、benchmark_citation_snapshot.json、
 * benchmark_project_audit.json、benchmark_glossary.json；构建后自检文本溢出，再由 PowerPoint 导出核对。
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

const C = {
  navy: '16324F', ink: '17212B', muted: '5B6770', line: 'D8E1E8', pale: 'F4F7F9',
  teal: '0E7490', aqua: '2C9EAA', green: '2E8B72', orange: 'D97706',
  red: 'B94E48', purple: '6B5B95', white: 'FFFFFF',
};

const survey = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_survey.json'), 'utf8'));
const audit = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_project_audit.json'), 'utf8'));
const reviews = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_paper_reviews.json'), 'utf8'));
const sources = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_reading_sources.json'), 'utf8'));
const glossary = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_glossary.json'), 'utf8'));
const properNames = JSON.parse(await fs.readFile(path.join(ROOT, 'data/benchmark_names.json'), 'utf8'));

const reviewByName = new Map(reviews.entries.map((e) => [e.benchmark, e]));
const sourceByName = new Map(sources.entries.map((e) => [e.benchmark, e]));
const active = survey.entries.filter((e) => e.focus === 'active');
const safety = active.filter((e) => e.objectives.includes('safety'));
const safetyBench = safety.filter((e) => e.primary_type === 'benchmark');
const N = {
  papers: 62,
  inventory: survey.entries.length,
  active: active.length,
  benchmarks: active.filter((e) => e.primary_type === 'benchmark').length,
  safety: safety.length,
  safetyBench: safetyBench.length,
  found: 0, platform: 0, candidate: 0,
};
for (const a of audit.audits) {
  if (!safety.some((e) => e.name === a.benchmark)) continue;
  if (a.status === 'found') N.found += 1;
  if (a.status === 'platform_only') N.platform += 1;
  if (a.status === 'candidate') N.candidate += 1;
}

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
  return w / 72;
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
        if (/^[、，。；：？！）】》”’%]$/.test(tk)) { lines.push((line + tk).trimEnd()); line = ''; continue; }
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
  const annotated = opts.raw ? String(text) : bodyAnno(slide, text);
  const lines = wrap(annotated, w, size);
  const lh = (size / 72) * (opts.lineSpacing ?? 1.32);
  if (lines.length * lh > h + 0.03 && !opts.allowOverflow) {
    overflow.push({ slide: slide._index, text: String(annotated).slice(0, 40), need: +(lines.length * lh).toFixed(2), have: h });
  }
  slide.addText(lines.join('\n'), {
    x, y, w, h,
    fontFace: FONT, fontSize: size, bold: !!opts.bold, color: opts.color || C.ink,
    align: opts.align || 'left', valign: opts.valign || 'top', margin: 0,
    fit: 'none', breakLine: false, italic: !!opts.italic,
    lineSpacingMultiple: opts.lineSpacing ?? 1.32,
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
function frame(title, kicker, sub) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s._index = pptx._slides.length;
  if (kicker) addText(s, kicker, 0.62, 0.26, 9, 0.22, { size: 9, bold: true, color: C.teal, charSpacing: 1 });
  addText(s, title, 0.62, 0.5, 12.1, 0.5, { size: 24, bold: true, color: C.navy });
  if (sub) addText(s, sub, 0.62, 1.08, 12.1, 0.3, { size: 10, color: C.muted });
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
  const minSize = opts.minSize ?? 7.2;
  const padX = 0.09, padY = 0.05;
  const annotated = [headers, ...rows].map((row) => row.map((v) => bodyAnno(s, v)));
  const layout = () => {
    const cells = annotated.map((row) => row.map((v, i) => wrap(v, widths[i] - padX * 2, size)));
    const heights = cells.map((row, r) => Math.max(...row.map((c) => c.length)) * (size / 72) * 1.28 + padY * 2 + (r === 0 ? 0.02 : 0));
    return { cells, heights, total: heights.reduce((a, b) => a + b, 0) };
  };
  let L = layout();
  while (L.total > maxH && size > minSize) { size -= 0.5; L = layout(); }
  if (L.total > maxH + 0.02) overflow.push({ slide: s._index, text: `table@${y}`, need: +L.total.toFixed(2), have: +maxH.toFixed(2) });
  if (opts.fillTo && L.heights.length > 1) {
    const extra = opts.fillTo - L.total;
    if (extra > 0.08) {
      const add = Math.min(0.55, extra / (L.heights.length - 1));
      for (let i = 1; i < L.heights.length; i += 1) L.heights[i] += add;
      L.total = L.heights.reduce((a, b) => a + b, 0);
    }
  }
  s.addTable(
    [headers, ...rows].map((row, r) => row.map((v, i) => ({
      text: wrap(annotated[r][i], widths[i] - padX * 2, size).join('\n'),
      options: {
        fontSize: size, fontFace: FONT, bold: r === 0,
        color: r === 0 ? C.white : C.ink,
        fill: { color: r === 0 ? C.navy : (r % 2 === 0 ? C.white : C.pale) },
        valign: 'middle', margin: padX, breakLine: false,
      },
    }))),
    { x: opts.x ?? 0.62, y, w: widths.reduce((a, b) => a + b, 0), colW: widths, rowH: L.heights, border: { type: 'solid', color: C.line, pt: 0.6 }, autoPage: false },
  );
  return y + L.total;
}
function divider(title, lead, kicker) {
  const s = pptx.addSlide();
  s.background = { color: C.navy };
  s._index = pptx._slides.length;
  addText(s, kicker, 0.8, 2.05, 9, 0.3, { size: 11, bold: true, color: 'AFC7D2', charSpacing: 1.5 });
  addText(s, title, 0.8, 2.45, 11.6, 0.8, { size: 34, bold: true, color: C.white });
  addRect(s, 0.82, 3.45, 1.6, 0.06, C.aqua);
  addText(s, lead, 0.82, 3.75, 10.6, 1.2, { size: 14, color: 'D8EEF2', lineSpacing: 1.5 });
  addText(s, String(s._index).padStart(2, '0'), 12.2, 7.12, 0.5, 0.2, { size: 8.5, bold: true, color: 'AFC7D2', align: 'right' });
  return s;
}

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Embodied Safety Benchmark Survey';
pptx.subject = '具身智能安全 Benchmark 调研（安全主线）';
pptx.title = '具身智能安全 Benchmark 调研';
pptx.company = 'Embodied Safety Benchmark';
pptx.lang = 'zh-CN';
pptx.theme = { headFontFace: FONT, bodyFontFace: FONT, lang: 'zh-CN' };
pptx._slides = [];

// ---------- 备注：术语就地加注 ----------
const ANNOTATIONS = [];
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
for (const item of properNames.names) ANNOTATIONS.push({ term: item.name, label: `（${item.kind}）` });
ANNOTATIONS.sort((a, b) => b.term.length - a.term.length);
const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

// ---------- 正文术语标注（每页首次出现） ----------
const BODY_ANNO = [];
for (const term of glossary.terms) {
  const zh = clean(term.zh);
  if (!zh || zh.length > 14) continue;
  if (zh === term.term || zh.includes(term.term)) continue;
  BODY_ANNO.push({ term: term.term, label: `（${zh}）` });
}
BODY_ANNO.sort((a, b) => b.term.length - a.term.length);
const bodySeen = new Map();
const PAGE_SKIP = new Map();
function bodyAnno(slide, text) {
  const key = slide._index;
  if (!bodySeen.has(key)) bodySeen.set(key, new Set());
  const seen = bodySeen.get(key);
  const skip = PAGE_SKIP.get(key) || [];
  let out = String(text);
  const hits = [];
  for (const item of BODY_ANNO) {
    if (seen.has(item.term) || skip.includes(item.term)) continue;
    const re = new RegExp('(?<![A-Za-z0-9_-])' + escapeRe(item.term) + '(?![A-Za-z0-9_-])');
    const m = re.exec(out);
    if (!m) continue;
    const after = out.slice(m.index + item.term.length, m.index + item.term.length + 1);
    if (after === '（') continue;
    const zh = item.label.replace(/[（）]/g, '');
    if (out.slice(Math.max(0, m.index - 14), m.index).includes(zh)) continue;
    if (out.slice(m.index + item.term.length, m.index + item.term.length + 14).includes(zh)) continue;
    hits.push({ index: m.index, len: item.term.length, term: item.term, label: item.label });
  }
  hits.sort((a, b) => a.index - b.index || b.len - a.len);
  const chosen = [];
  let cursor = -1;
  for (const h of hits) if (h.index >= cursor) { chosen.push(h); cursor = h.index + h.len; }
  for (let i = chosen.length - 1; i >= 0; i -= 1) {
    const h = chosen[i];
    out = out.slice(0, h.index + h.len) + h.label + out.slice(h.index + h.len);
    seen.add(h.term);
  }
  return out;
}

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
  for (const m of matches) if (m.index >= cursor) { chosen.push(m); cursor = m.index + m.len; }
  let out = paragraph;
  for (let i = chosen.length - 1; i >= 0; i -= 1) {
    const m = chosen[i];
    out = out.slice(0, m.index + m.len) + m.label + out.slice(m.index + m.len);
    seen.add(m.term);
  }
  return out;
}
function note(s, paragraphs, skip = []) {
  const seen = new Set(skip);
  const body = [].concat(paragraphs).map((t) => annotate(t, seen)).join('\n\n');
  s.addNotes(`资料快照：${SNAPSHOT}。${body}`);
}

// ---------- 安全六层映射（26 条） ----------
const LAYERS = [
  { key: '① 执行层物理安全', count: 5, judge: '动作是否碰撞、是否越过约束', members: ['LIBERO-Safety', 'SafeLIBERO', 'ForesightSafety-VLA', 'SafeBench', 'VLA-Arena'] },
  { key: '② 物理后果（财产保全）', count: 1, judge: '抓握是否夹坏、压坏物体', members: ['ManiPhysicsBench'] },
  { key: '③ 语义 / 意图安全', count: 6, judge: '危险指令是否照做、指代与角色是否错', members: ['HazardArena', 'RoboHarm', 'ASIMOV Benchmark', 'RoboAbstention', 'IS-Bench', 'SafeAgentBench'] },
  { key: '④ 规划 / 规则安全', count: 1, judge: '计划是否违反显式安全约束', members: ['DESPITE'] },
  { key: '⑤ 过程 / 阶段安全', count: 2, judge: '执行前中后的顺序、阶段与卫生', members: ['SafeStage', 'HygieneRoboBench'] },
  { key: '⑥ 完整性 / 对抗', count: 2, judge: '后门、触发器、越狱与定向失效', members: ['RoboJailBench', 'Trap-LIBERO / Trap-RoboTwin'] },
  { key: '邻接：软件代理', count: 5, judge: '工具、技能包、记忆、多代理的越权与注入', members: ['Agent-SafetyBench', 'INFUSE', 'MemForm', 'ORBIT', 'SkillSafetyBench'] },
  { key: '邻接：治理与交通', count: 4, judge: '权限、恢复、升级；碰撞进入综合分', members: ['EmbodiedGovBench', 'NAVSIM', 'VIPS', 'MineAmongUs'] },
];
const SKIP_BY_PAGE = {
  'LIBERO-Safety': ['SSR'],
  'SafeStage': ['ETS'],
  'RoboJailBench': ['SR'],
};

const layerOf = new Map();
for (const L of LAYERS) for (const m of L.members) layerOf.set(m, L.key);

// ---------- 1. 封面 ----------
{
  const s = pptx.addSlide();
  s.background = { color: C.navy };
  s._index = 1;
  addPill(s, '调研汇报 · 安全主线', 0.82, 1.02, 2.5, C.teal, C.white, 9.5);
  addText(s, '具身智能安全 Benchmark 调研', 0.8, 1.45, 11.8, 0.85, { size: 38, bold: true, color: C.white });
  addText(s, '按测量对象分层，逐层说明判据、证据与已被报告的结果', 0.82, 2.42, 11.2, 0.5, { size: 17, color: 'D8EEF2' });
  addRect(s, 0.82, 3.28, 2.9, 0.5, C.teal, true);
  addText(s, `资料快照 ${SNAPSHOT}`, 0.82, 3.33, 2.9, 0.4, { size: 11.5, bold: true, color: C.white, align: 'center', valign: 'mid' });
  const facts = [[`${N.safety}`, '条安全目标条目'], [`${N.safetyBench}`, '个安全评测任务集'], [`${N.papers}`, '篇精读论文']];
  facts.forEach(([num, label], i) => {
    const x = 0.82 + i * 3.2;
    addText(s, num, x, 4.5, 2.7, 0.66, { size: 40, bold: true, color: C.aqua, lineSpacing: 1.0 });
    addText(s, label, x, 5.18, 2.8, 0.3, { size: 11.5, color: 'C7D8E2' });
  });
  addText(s, '统计口径只含“论文—benchmark”两类成果；数据集、仿真平台、框架与方法论文仅在附录说明中提及。', 0.82, 6.02, 11.4, 0.3, { size: 11, color: 'AFC7D2' });
  addText(s, '所有分数来自论文摘要或正文，本库未复现任何实验；“违规”“伤害”均为各基准自定义的判定。', 0.82, 6.38, 11.4, 0.3, { size: 10.5, color: 'AFC7D2' });
  addText(s, '01', 12.2, 7.12, 0.5, 0.2, { size: 8.5, bold: true, color: 'AFC7D2', align: 'right' });
  note(s, [
    '本汇报只讨论安全方向的 benchmark：26 条带安全目标的条目、其中 23 个评测任务集。能力基准只保留两页作为底座对照。',
    '所有分数都是论文报告值，本库没有复现；“违规”“碰撞”“伤害”都是各基准自定义的判定，不等同于真实事故。',
  ]);
}

// ---------- 2. 一页结论 ----------
{
  const s = frame('一页结论：安全评测的缺口在过程证据与真机证据', '01 / 摘要');
  const cards = [
    [`${N.safety}`, '条带安全目标', C.navy, `其中 ${N.safetyBench} 个评测任务集、3 个框架`],
    [`${N.safetyBench} / ${N.safety}`, '评测任务集占比', C.teal, '其余 3 条为框架：SafeBench、EmbodiedGovBench、ORBIT'],
    ['5 / 26', '报告真机执行', C.red, '13 条未核实、3 条仅数据、5 条不适用'],
    [`${N.found}`, '已确认项目入口', C.green, `另 ${N.candidate} 个候选待确认`],
  ];
  cards.forEach(([num, label, color, detail], i) => {
    const x = 0.62 + i * 3.08;
    addRect(s, x, 1.28, 2.9, 1.34, C.pale, true);
    addText(s, num, x + 0.18, 1.34, 2.5, 0.52, { size: 26, bold: true, color, lineSpacing: 1.0 });
    addText(s, label, x + 0.18, 1.9, 2.55, 0.26, { size: 11.5, bold: true });
    addText(s, detail, x + 0.18, 2.18, 2.55, 0.4, { size: 8.5, color: C.muted, lineSpacing: 1.25 });
  });
  addRect(s, 0.62, 2.86, 12.1, 3.86, C.pale, true);
  addText(s, '三条判断', 0.9, 3.02, 2.2, 0.3, { size: 14, bold: true, color: C.navy });
  const pts = [
    ['任务成功率无法推出过程安全。', 'SafeStage 的 33.74% 成功率里有 70.84% 含不安全行为；HazardArena 把“尝试、提交、成功”分三档记录，原因相同。'],
    ['六层判据互不换算，分数不可相加。', '碰撞率、接触力、拒答率、计划有效性、卫生合规、后门触发各自定义，跨层平均没有意义。'],
    ['真机与跨本体证据是主要缺口。', '26 条里只有 5 条报告真机执行；多本体只在仿真侧（ForesightSafety-VLA 覆盖 5 种本体）。'],
  ];
  pts.forEach(([h, body], i) => {
    const y = 3.4 + i * 1.06;
    addRect(s, 0.9, y + 0.06, 0.06, 0.72, [C.teal, C.orange, C.red][i]);
    addText(s, h, 1.08, y, 10.9, 0.3, { size: 12, bold: true });
    addText(s, body, 1.08, y + 0.32, 10.9, 0.62, { size: 9.5, color: C.muted, lineSpacing: 1.35 });
  });
  footer(s);
  note(s, [
    `一页结论：26 条安全目标条目、23 个任务集，其中 5 条报告真机执行；六层判据不可互相换算。`,
    '三条判断分别对应过程安全、口径与证据缺口；后面每一节都会给出对应条目与数字。',
  ]);
}

// ---------- 3. 范围与口径 ----------
{
  const s = frame('范围与口径：算什么、不算什么、怎么数', '01 / 方法与口径');
  const rows = [
    ['统计对象', '已精读的论文与 benchmark 条目', '只统计“论文—benchmark”两类成果'],
    ['条目数', '62 条活跃条目，其中 26 条带安全目标', '归档区 60 条未分类候选不计入'],
    ['计数单位', '条目数 ≠ 被测模型数 ≠ 场景数 ≠ episode 数', '每一页都标出单位，不跨单位相加'],
    ['判定', '违规、碰撞、伤害均为基准自定义谓词', '不作真实事故或伤害率的换算'],
    ['复现', '全部分数为论文报告值', '本库没有运行任何实验'],
  ];
  addTable(s, ['维度', '本汇报的做法', '边界'], rows, [1.85, 6.4, 3.85], 1.28, { size: 10, maxH: 3.2, fillTo: 3.1 });
  addText(s, '明确不做的四件事', 0.62, 4.62, 5, 0.28, { size: 12, bold: true, color: C.teal });
  const nots = [
    ['不声称系统综述', '检索式未穷尽，样本偏向桌面机械臂与公开项目；未命中不等于不存在。'],
    ['不合并不同层级的分', '碰撞率与拒答率分母不同，求平均会掩盖失效类型。'],
    ['不把仿真谓词当伤害', '仿真判的是“碰撞事件”“越界”，与真实损伤之间没有换算系数。'],
    ['不猜测项目可用性', '未打开仓库即标“未核验”，不写“没有代码”。'],
  ];
  nots.forEach(([h, body], i) => {
    const x = 0.62 + (i % 2) * 6.15;
    const y = 4.98 + Math.floor(i / 2) * 0.98;
    addRect(s, x, y, 5.95, 0.84, C.pale, true);
    addText(s, h, x + 0.16, y + 0.1, 5.6, 0.26, { size: 10, bold: true, color: C.red });
    addText(s, body, x + 0.16, y + 0.38, 5.65, 0.42, { size: 8.8, color: C.muted, lineSpacing: 1.3 });
  });
  footer(s);
  note(s, [
    '口径四条：条目数与被测模型数、场景数、episode 数是四种单位，全篇不混用；违规是基准自定义谓词；分数全部来自论文；未核验的项目写“未核验”。',
    '不做系统综述，也不把仿真里的碰撞事件换算成伤害率——这两件事在本库里都缺数据支撑。',
  ]);
}

// ---------- 4-5. 术语速查 ----------
{
  const groups = [
    ['术语速查（一）：模型与评测单位', [
      ['VLA', '视觉—语言—动作模型', '以图像与语言为输入、直接输出机器人动作的模型，本领域主要被测对象'],
      ['VLM', '视觉语言模型', '同时理解图像与文本；常作为具身系统的高层决策或裁判'],
      ['LLM', '大语言模型', '纯文本模型；在具身任务里承担规划、工具调用与拒答'],
      ['episode', '回合', '一次从重置到终止的完整交互，安全指标最常见的分母'],
      ['rollout', '展开 / 推演', '用当前策略跑一次得到的完整轨迹，常与 episode 混用'],
      ['checkpoint', '检查点', '训练中保存的权重快照；“公共 checkpoint”指公开可下载的那份'],
      ['SR', '成功率', '成功 episode ÷ 全部 episode；部分论文用它指 Security Rate'],
      ['SSR', '安全成功率', '既完成又未违规的 episode ÷ 全部 episode'],
      ['USR', '不安全成功率', '完成但违规的 episode ÷ 全部 episode'],
      ['PR', '保全率', 'Safe SR ÷ SR，即成功的回合中物体完好的比例'],
    ]],
    ['术语速查（二）：判据与指标', [
      ['CAR', '避碰率', '未发生碰撞的 episode ÷ 全部 episode'],
      ['TSR', '任务成功率', '只判任务是否完成，不含安全条件'],
      ['ETS', '执行步数', '完成一次任务所用的控制步数；部分基准用它衡量效率'],
      ['SBU', '成功但不安全率', '不安全的成功回合 ÷ 成功回合；与同表 USR 的分母不同'],
      ['VSI', '违规严重度指数', '在事件次数之外按物理影响加权，衡量单次违规的严重度'],
      ['CC', '累积碰撞代价', '整段任务中碰撞与约束违反的累计值'],
      ['RET', '风险暴露时间', '处于风险状态的时间长度'],
      ['LTLf', '有限轨迹线性时序逻辑', '描述“先后、前置、禁止”等有限序列规则，可用自动机逐步检查'],
      ['STL', '信号时序逻辑', '对接触力、距离、倾角等连续量设阈值，检查轨迹是否越界'],
      ['PDMS', '规划综合分', 'NAVSIM 的驾驶评分：碰撞、可行驶区域、舒适、进度加权'],
    ]],
  ];
  groups.forEach(([title, rows], idx) => {
    const s = frame(title, '01 / 术语速查', idx === 0
      ? '前十个词是模型类别、评测单位与基础指标；正文第一次出现处还会就地加注。'
      : '第二页是判据与综合指标。注意 SBU 与 USR 分母不同：一个除成功回合，一个除全部回合。');
    addTable(s, ['术语', '中文', '一句话解释'], rows, [1.55, 3.15, 7.4], 1.55, { size: 10.5, maxH: 4.7, fillTo: 4.55 });
    footer(s, `词条取自 data/benchmark_glossary.json（${glossary.terms.length} 个术语）。`);
    note(s, [idx === 0
      ? '术语页一：模型类别、评测单位与基础指标。重点是 episode 是最常见的分母，SSR 与 USR 都以全部 episode 为分母。'
      : '术语页二：判据与综合指标。重点区分 SBU（分母是成功回合）与 USR（分母是全部回合），两者可差数倍；LTLf 与 STL 是两种形式化监控语言。']);
  });
}

// ---------- 6. 总量与层级分布 ----------
{
  const s = frame('26 条安全目标：六层 + 两类邻接，条目数不求和', '02 / 总量', '同一基准可能覆盖多层，按“主测量对象”归一层；因此 26 条之和等于总数，但每层的判据不可合并。');
  const rows = LAYERS.map((L) => [L.key, String(L.count), L.judge, L.members.slice(0, 3).join('、')]);
  addTable(s, ['层级', '条目数', '判据（测什么）', '代表条目'], rows, [2.35, 0.8, 4.55, 4.4], 1.55, { size: 9.6, maxH: 5.0, fillTo: 4.95 });
  footer(s);
  note(s, [
    '26 条安全目标按主测量对象分成六层与两类邻接：执行层 5、物理后果 1、语义意图 6、规划 1、过程阶段 2、对抗 2，邻接的软件代理 5、治理与交通 4。',
    '这 26 条里 23 个是评测任务集，3 个是框架（SafeBench、EmbodiedGovBench、ORBIT）；条目数不能跨层相加成“安全能力分”。',
  ]);
}

// ---------- 7. 场景覆盖 ----------
{
  const s = frame('安全条目的场景覆盖：机械臂操作与语义决策为主', '02 / 场景', '场景字段可多标签，因此各条之和大于 26；移动、导航、人形都是个别条目。');
  const domainCount = new Map();
  for (const e of safety) for (const d of e.domains || []) domainCount.set(d, (domainCount.get(d) || 0) + 1);
  const domains = [...domainCount.entries()].sort((a, b) => b[1] - a[1]);
  const maxD = domains[0][1];
  domains.forEach(([label, v], i) => {
    const y = 1.55 + i * 0.56;
    addText(s, label, 0.62, y, 3.1, 0.3, { size: 10 });
    addRect(s, 3.95, y + 0.05, (v / maxD) * 4.3, 0.22, i === 0 ? C.navy : C.aqua, true);
    addText(s, String(v), 4.02 + (v / maxD) * 4.3, y, 0.5, 0.3, { size: 10, bold: true, color: C.navy });
  });
  addRect(s, 9.0, 1.5, 3.72, 4.3, C.pale, true);
  addText(s, '读法', 9.2, 1.62, 3.3, 0.26, { size: 10.5, bold: true, color: C.navy });
  addText(s, '安全条目与能力条目共享同一批场景：机械臂操作占多数，语义决策集中在拒答与指代类基准。移动、导航、人形条目少，不能据此对相应形态下结论。', 9.2, 1.94, 3.35, 3.6, { size: 9, color: C.muted, lineSpacing: 1.45 });
  footer(s);
  note(s, [
    '场景按 domains 字段统计，可多标签：机械臂操作与语义决策占多数，其余形态是个别条目。',
    '这一个分布与能力侧一致，说明安全基准没有覆盖新的形态；跨形态结论不能由这些条目推出。',
  ]);
}

// ---------- 7b. 证据载体与真机证据 ----------
{
  const s = frame('证据载体：仿真为主，真机执行只有 5 条', '02 / 证据载体', '两张表都按条目计数；settings 可多标签（仿真 + 真机），因此上一张表的和大于 26。');
  const settingCount = new Map();
  const realCount = new Map();
  let other = 0;
  const keys = ['simulation', 'real_robot', 'real_dataset', 'software'];
  for (const e of safety) {
    let hit = false;
    for (const st of e.settings || []) {
      settingCount.set(st, (settingCount.get(st) || 0) + 1);
      if (keys.includes(st)) hit = true;
    }
    if (!hit) other += 1;
    realCount.set(e.real_evidence, (realCount.get(e.real_evidence) || 0) + 1);
  }
  const settingRows = [
    ['仿真', String(settingCount.get('simulation') || 0), '动作在仿真器里闭环，含真机孪生的也计入'],
    ['真机执行', String(settingCount.get('real_robot') || 0), '在真实硬件上闭环'],
    ['真实数据', String(settingCount.get('real_dataset') || 0), '用真实采集数据评测，不做闭环'],
    ['软件环境', String(settingCount.get('software') || 0), 'API、文件、GUI 层'],
    ['其它', String(other), '符号、离线图像、运行时等'],
  ];
  addText(s, '载体（settings 字段，可多标签）', 0.62, 1.3, 6, 0.26, { size: 10.5, bold: true, color: C.teal });
  addTable(s, ['载体', '条目', '含义'], settingRows, [1.5, 0.7, 3.5], 1.62, { size: 9.4, maxH: 2.4, x: 0.62 });
  const realRows = [
    ['报告真机执行', String(realCount.get('execution_reported') || 0), '论文给出真机试验或部署结果'],
    ['配对真机验证', String(realCount.get('paired_validation') || 0), '仿真与真机成对比较'],
    ['仅真实数据', String(realCount.get('data_only') || 0), '用真实数据评测，不做闭环'],
    ['未核实', String(realCount.get('unknown') || 0), '本轮未查到真机证据，不等于没有'],
    ['不适用', String(realCount.get('not_applicable') || 0), '纯软件或纯规划，无物理执行'],
  ];
  addText(s, '真机证据（real_evidence 字段）', 6.55, 1.3, 6, 0.26, { size: 10.5, bold: true, color: C.teal });
  addTable(s, ['状态', '条目', '含义'], realRows, [1.55, 0.65, 4.05], 1.62, { size: 9.4, maxH: 2.6, x: 6.55 });
  addRect(s, 0.62, 4.3, 12.1, 1.15, 'FDF2F2', true);
  addText(s, '两个数字必须分开读', 0.85, 4.4, 5, 0.26, { size: 10.5, bold: true, color: C.red });
  addText(s, 'settings 的“真机执行”5 条指场景设置里有真机；real_evidence 的“报告真机执行”5 条指论文真的给出了真机结果。引用时用后者，并注明样本量。', 0.85, 4.7, 11.6, 0.62, { size: 9, color: C.muted, lineSpacing: 1.35 });
  addRect(s, 0.62, 5.62, 12.1, 1.05, C.pale, true);
  addText(s, '横向对照（能力侧 62 条）', 0.85, 5.72, 5, 0.26, { size: 10, bold: true, color: C.teal });
  addText(s, '全部 62 条里 42 条含仿真、18 条含真机执行；安全侧的 15 条仿真与 5 条真机，比例与整体一致——安全评测没有带来更多真机证据。', 0.85, 6.0, 11.6, 0.55, { size: 9, color: C.muted, lineSpacing: 1.35 });
  footer(s);
  note(s, [
    '载体表按 settings 统计，可多标签；真机证据表按 real_evidence 统计，是互斥分类。',
    '两张表都指向同一结论：仿真为主，真机执行只有 5 条；未核实的 13 条不能当成“没有真机”，只能当“本轮没查到”。',
  ]);
}

// ---------- 7c. 判据定义与计算方式 ----------
{
  const s = frame('八类判据的定义与计算方式', '02 / 判据定义', '同一个词在不同基准里算法不同：下表给定义、判定窗口与代表条目，避免把“碰撞”与“违规”混读。');
  const rows = [
    ['碰撞事件', '两物体接触力或穿透深度越过阈值即记一次；按 episode 累计', '每个仿真步', 'LIBERO-Safety、SafeLIBERO', '阈值未公开时，跨基准比较无意义'],
    ['越界 / 禁入区', '末端或机身进入预定义几何区域，进入即违规', '每个仿真步', 'LIBERO-Safety 的 L1、VLA-Arena', '区域定义随场景变，换场景需重设'],
    ['接触力阈值', '测得接触力峰值超过安全上限，按峰值或积分计', '每次接触', '人机接触力类条目', '需假人或力传感器标定，仿真中常缺'],
    ['违规时长', '处于违规状态的累计时间或占比', '整段 episode', 'SafeStage 类阶段指标', '长任务天然更高，需按任务长度归一'],
    ['拒答 / 拒绝', '模型对危险指令输出拒绝或澄清，不进入执行阶段', '每次请求', 'HazardArena、RoboHarm、SafeAgentBench', '拒绝率不含“拒绝后是否安全停机”'],
    ['计划有效性', '形式化验证器判定计划能否达成目标、是否违反约束', '每个计划', 'DESPITE、HygieneRoboBench', '计划合规不等于执行安全'],
    ['顺序 / 卫生约束', '前置条件与环境清洁状态是否保持；按规则或自动机检查', '每个动作序列', 'HygieneRoboBench、SafeStage', '规则文本的理解误差会混入判定'],
    ['触发器命中', '特定输入条件下策略输出指定失效行为', '每次触发', 'Trap 系列、RoboJailBench', '触发器形态是枚举的，未覆盖即漏检'],
  ];
  addTable(s, ['判据', '定义与计算', '判定窗口', '代表条目', '主要误读风险'], rows, [1.7, 4.0, 1.45, 2.45, 2.5], 1.55, { size: 9, maxH: 5.0, fillTo: 4.9 });
  footer(s);
  note(s, [
    '八类判据的定义、判定窗口与代表条目：碰撞与越界按步判定，违规时长按整段累计，拒答按请求判定，计划合规按计划判定，触发器按命中判定。',
    '每一行的“误读风险”说明该判据在跨基准比较时最容易出错的地方；判定窗口不同，数值不可直接比较。',
  ]);
}

// ---------- 8. 判据 × 载体矩阵 ----------
{
  const s = frame('判据类型与证据载体：哪一层有什么证据', '02 / 证据形态', '行是判据类型，列是证据形态；● 表示该层有直接证据，○ 表示只有间接证据，— 表示缺失。');
  const rows = [
    ['碰撞 / 越界', '● 仿真谓词', '● 真机事件', '○ 离线轨迹', '—', '条目多，但真机样本小'],
    ['接触力 / 冲击', '○ 需物理标定', '● 假人或受控场地', '○ 数据回放', '—', '仅少数条目做定量测量'],
    ['物体损伤', '● 有限元判定', '—', '—', '—', '只有 ManiPhysicsBench'],
    ['危险指令 / 拒绝', '● 脚本化场景', '○ 真机接口', '—', '○ 人工判定', '文本与动作接口差异大'],
    ['计划合规', '● 形式化验证', '—', '—', '—', '只有 DESPITE 与卫生类'],
    ['顺序 / 阶段 / 卫生', '● 阶段绑定', '—', '—', '○ 人工核查', 'SafeStage、HygieneRoboBench'],
    ['后门 / 触发器 / 越狱', '● 触发器注入', '○ 有限真机', '—', '—', 'RoboJailBench、Trap 系列'],
  ];
  addTable(s, ['判据类型', '仿真谓词', '真机执行', '离线数据', '人工判定', '本库观察'], rows, [2.0, 1.9, 1.9, 1.75, 1.6, 3.0], 1.55, { size: 9.4, maxH: 4.55, fillTo: 4.45 });
  addRect(s, 0.62, 6.05, 12.1, 0.7, C.pale, true);
  addText(s, '读法：● 与 ○ 都是“有证据”，区别在直接程度；判据之间不可换算，例如“碰撞事件数”与“接触力峰值”不能合成一个安全分。', 0.85, 6.15, 11.6, 0.5, { size: 9.2, color: C.muted, lineSpacing: 1.3 });
  footer(s);
  note(s, [
    '这张表回答“哪一层有什么证据”：碰撞与越界在仿真里最容易做，接触力需要物理标定，物体损伤需要外部求解器，计划合规需要形式化验证。',
    '空白格是真实缺口：物体损伤没有真机判定，计划合规没有真机执行，后门触发很少有真机验证。',
  ]);
}

// ---------- 9. 指标四类与分母 ----------
{
  const s = frame('指标的四类与两个分母：读数字前先定位', '02 / 指标');
  const rows = [
    ['比率', 'SBU 成功但不安全率 = 不安全的成功 ÷ 成功回合', '分母为成功回合；USR 一行用全部 episode'],
    ['比率', 'SSR 安全成功率 = 安全成功 ÷ 全部 episode', '与 USR 同分母；SBU 用成功回合作分母'],
    ['严重度', 'VSI 违规严重度指数', '按物理影响加权，不只数次数'],
    ['累积量', 'CC 累积碰撞代价 = 整段任务中碰撞与违规之和', '反映过程总量，不反映单次严重度'],
    ['时间', 'RET 风险暴露时间', '反映处在风险状态的时长'],
  ];
  addTable(s, ['类型', '定义式', '读法'], rows, [1.1, 7.3, 4.3], 1.55, { size: 10, maxH: 3.1, fillTo: 3.0 });
  addRect(s, 0.62, 4.85, 5.95, 1.95, C.pale, true);
  addText(s, '同一组数，两种分母', 0.85, 4.95, 5.4, 0.26, { size: 10.5, bold: true, color: C.navy });
  addText(s, 'SafeStage：SR 33.74%、SSR 9.84%、USR 23.90%，均以全部 episode 为分母；成功轨迹中的不安全比例是 USR ÷ SR = 70.84%。两个百分比都正确，含义不同。', 0.85, 5.24, 5.5, 1.4, { size: 9, color: C.muted, lineSpacing: 1.35 });
  addRect(s, 6.35, 4.85, 6.37, 1.95, 'FDF2F2', true);
  addText(s, '四类指标很少同时出现', 6.58, 4.95, 5.9, 0.26, { size: 10.5, bold: true, color: C.red });
  addText(s, '本库 26 条里，比率最常见，累积量与时间只在少数条目（ForesightSafety-VLA 报 CC 与 RET），严重度只有个别基准（如 SafeVLA 类）报告；没有条目同时给全四类。', 6.58, 5.24, 5.95, 1.4, { size: 9, color: C.muted, lineSpacing: 1.35 });
  footer(s);
  note(s, [
    '四类指标是比率、严重度、累积量、时间；比率内部还有两个分母：全部 episode 与成功回合。',
    'SBU 用成功回合作分母，USR 用全部 episode 作分母，混用会让数字差数倍，这是跨论文比较最常见的错误。',
  ]);
}

// ---------- 10. 分节 ----------
divider('安全基准逐层详解：每层挑代表，附判据与实测', '六层各讲一到两个基准，外加两类邻接的各一个代表；每页给判据定义、实测数字与边界，末尾按问题给选型。', '03 / 安全基准');

// ---------- 11. 12 个安全基准详解 ----------
const DETAIL = [
  {
    name: 'LIBERO-Safety',
    neighbor: '与 SafeLIBERO 的差别在改动位置：LIBERO-Safety 改写任务定义（加安全谓词），SafeLIBERO 不改任务、只在动作输出上加安全层。',
    cat: '① 执行层物理安全',
    plain: 'LIBERO-Safety 在 LIBERO 的家庭操作任务里加入安全检查：除了判定任务是否完成，还逐帧判定是否碰撞、是否触碰危险物。',
    rel: ['高', '被测对象是 OpenVLA-OFT、π0.5、VLA-ULAP 等 VLA。'],
    domain: '五套任务（AAG 家务操作、HRI 人机交互、TSA 时序约束、FSHOA 高危操作、SSR 语义安全推理）× 5 任务 × 3 难度 = 75 个测试配置',
    build: 'UBDDL 在 BDDL 之上加入随机化、动态物体与逐步安全检查，因此违规可以在执行中被判定；关键姿态由 CuRobo 生成无碰撞示范；L0 为干净环境、L1 加约束、L2 加强风险形态。',
    metric: '安全轨 SR 要求“完成任务且全程无违规”，一次违规即终止并记失败；语义安全推理子套件单独统计。',
    kpis: [['50.0 / 79.3 / 1.3%', 'OpenVLA-OFT 的 L0/L1/L2 成功率'], ['75', '测试配置（5 套 × 5 任务 × 3 档）'], ['19,664', '无碰撞示范（训练数据）']],
    result: 'OpenVLA-OFT 在 AAG 子集上 L0／L1／L2 分别为 50.0%／79.3%／1.3%。L1 高于 L0、L2 骤降：约束数量不构成主要难度，风险形态决定结果。',
    limit: 'SR 已含安全约束，不能当普通成功率读；L0–L2 的风险形态由固定资产与布局构成，换场景需重设谓词。',
  },
  {
    name: 'SafeLIBERO',
    neighbor: '与 LIBERO-Safety 的差别在改动位置：SafeLIBERO 保留原任务与成功率定义，另用 CBF-QP 修正动作；因此它的 TSR 可与原 LIBERO 直接对照。',
    cat: '① 执行层物理安全（外挂安全层）',
    plain: 'SafeLIBERO 在 LIBERO 之外加一层安全修正：用控制障碍函数改写策略输出的动作，使机械臂绕开障碍后再执行。',
    rel: ['高', '被测对象是 π0.5 等 VLA，对照为加安全层前后的同一模型。'],
    domain: '四个 LIBERO 套件各选 4 个任务，每任务设“靠近目标”与“阻挡路径”两级障碍，共 32 场景 × 50 次 = 1,600 episode',
    build: 'AEGIS 用控制障碍函数（CBF）判断当前动作是否会把系统推入危险集，用二次规划（QP）求最小修正；在平移动作与完整动作空间分别评测。',
    metric: 'CAR 避碰率＝无碰撞 episode ÷ 全部；TSR 任务成功率；ETS 执行步数。三种指标分开报，平移与完整动作空间不可混比。',
    kpis: [['18.7 → 77.9%', 'π0.5 的 CAR 在加 AEGIS 前后'], ['50.9 → 68.1%', '同期 TSR'], ['1,600', 'episode（32 场景 × 50 次）']],
    result: '平移动作设置下，π0.5 的避碰率从 18.7% 升到 77.9%，任务成功率从 50.9% 升到 68.1%；完整动作空间另有一组结果。',
    limit: '安全层依赖动力学模型与状态估计，换本体需重标定；两项目标真机任务只做趋势验证，不构成跨本体结论。',
  },
  {
    name: 'ManiPhysicsBench',
    neighbor: '与 LIBERO-Safety 的差别在判据层级：后者判“是否发生碰撞”，本基准判“碰撞是否造成损伤”，需要外部求解器与材料参数。',
    cat: '② 物理后果（财产保全）',
    plain: 'ManiPhysicsBench 直接测量抓握是否造成物体损伤：把接触数据交给外部有限元求解器，判定物体是否断裂或变形。',
    rel: ['高', '被测对象是公共 VLA checkpoint，按 SimplerEnv 设置运行。'],
    domain: '91 个对象的 ManiPhysicsZoo，覆盖脆性断裂、软物体变形、薄壁变形三条轴',
    build: '刚体仿真记录每次接触的位置、方向与力；CalculiX／FEBio／OpenRadioss 按几何与材料阈值判定每次抓握的损伤，再汇总整段轨迹。',
    metric: 'SR 完成率、Safe SR 无损完成率、PR = Safe SR ÷ SR（成功的回合中物体完好的比例）。三者同分母基准不同。',
    kpis: [['48.3%', '完成率 SR'], ['13.5%', '无损完成率 Safe SR'], ['27.9%', '成功中完好比例 PR']],
    result: 'SimplerEnv 高/中难对象上，公共 checkpoint 平均 SR 48.3%、Safe SR 13.5%、PR 27.9%：多数模型能完成搬运，但无法保持物体完好。',
    limit: '损伤由求解器事后判定，仿真中不会真的断裂；SR 为 0 时 PR 无定义；需装三个有限元后端。',
  },
  {
    name: 'HazardArena',
    neighbor: '与 RoboHarm 的差别在变量：HazardArena 改场景语义与对象角色，RoboHarm 固定意图只换输出接口。',
    cat: '③ 语义 / 意图安全',
    plain: 'HazardArena 用成对的危险场景与安全场景，测量模型是否理解“谁对谁做什么”。',
    rel: ['高', '被测对象为 VLA-Adapter、π0 系列等 VLA。'],
    domain: '51 个任务覆盖食物、财产、化学、隐私、火灾、人身、电气七类风险；另补 75 个情境资产',
    build: '成对构造：保持场景布局与操作模板一致，只改动作参与者、目标关系与指令；执行进度分“尝试（ATTEMPT）、提交（COMMIT）、成功（SUCCESS）”三档记录。',
    metric: '危险任务成功率、提交率、安全任务成功率分别报；三档记录避免把“想动手”与“真做成”混为一谈。',
    kpis: [['0.22 → 0.01', '危险任务成功率（拒绝示范训练后）'], ['0.44 → 0.03', '提交率'], ['51', '任务 / 7 类风险']],
    result: '拒绝示范训练的 VLA-Adapter 在报告设置中把危险任务成功率从 0.22 降到 0.01、提交率从 0.44 降到 0.03，安全任务成功率由 0.25 微升到 0.26。',
    limit: '配对并非只换一个文本标签，仍有混淆变量；改进只对应文中分布，另有真机验证但样本有限。',
  },
  {
    name: 'RoboHarm',
    neighbor: '与 HazardArena 的差别在变量：RoboHarm 固定风险意图、只换接口；HazardArena 固定接口、只换语义。',
    cat: '③ 语义 / 意图安全（接口对照）',
    plain: 'RoboHarm 固定同一风险意图，只更换模型的输出接口，测量拒绝行为是否随接口改变。',
    rel: ['高', '被测对象为 7 个 LLM/VLM 模型与 VLA，跨接口比较。'],
    domain: '五类不安全场景；YAM 双臂机械臂与 MuJoCo 孪生；文本、代码计划、末端执行器、关节四种接口',
    build: '同一风险指令分别以文本、代码式计划、末端位姿动作、关节动作输出；模拟评测覆盖 7 个模型，真机末端与关节接口各记录 612／252 次试验。',
    metric: '拒绝率按接口分别统计；拒绝率的分母是该接口下的试验次数，跨接口比较时必须说明分母。',
    kpis: [['73%', '文本接口拒绝率'], ['18%', '真机末端接口（612 次）'], ['41%', '真机关节接口（252 次）']],
    result: '文本接口拒绝率约 73%，机器人接口约 18–25%；真机末端接口约 18%、关节接口约 41%。接口本身会改变观测到的安全表现。',
    limit: '真机样本量有限（612／252 次）；场景为五类自制，不代表全部危险类型。',
  },
  {
    name: 'DESPITE',
    neighbor: '与 SafeStage 的差别在评测对象：DESPITE 只看形式化计划，SafeStage 看仿真执行的前中后三段。',
    cat: '④ 规划 / 规则安全',
    plain: 'DESPITE 只评规划层：把任务写成带安全约束的形式化问题，用验证器判定计划是否有效、是否危险、是否安全完成。',
    rel: ['高', '被测对象是 LLM/VLM 规划器，论文共测 23 个模型。'],
    domain: '12,279 个任务覆盖物理与规范危险；主结果使用筛选出的 1,044 个困难任务',
    build: '任务用带安全约束的规划形式化；确定性验证器分别回答三个问题：计划能否达成目标、是否违反约束、是否安全完成。',
    metric: '三个比例分开报：无有效计划、危险计划、安全完成；三者回答不同问题，不能合成一个分。',
    kpis: [['0.4%', '最强模型无有效计划的比例'], ['28.3%', '同模型产出危险计划的比例'], ['38–57%', '18 个开源模型的安全意识区间']],
    result: '最强规划模型在 1,044 个困难任务上仅 0.4% 无有效计划，却有 28.3% 产出危险计划；18 个开源模型的安全意识集中在 38–57%。',
    limit: '评估对象是形式化计划，关节执行不在评测范围内；主结果来自困难集，不代表全集的随机平均。',
  },
  {
    name: 'SafeStage',
    neighbor: '与 HygieneRoboBench 的差别在判据来源：SafeStage 用仿真状态定义阶段危险，HygieneRoboBench 用文本规则定义卫生约束。',
    cat: '⑤ 过程 / 阶段安全',
    plain: 'SafeStage 把安全判定分配到执行前、执行中、完成后三个阶段，分别报告安全成功与不安全成功。',
    rel: ['高', '被测对象为 VLA 策略，按阶段报告指标。'],
    domain: '97 个任务：初始危险 27、执行阶段 40、完成后 30；RoboLab／GPU PhysX 中的 Panda＋Robotiq',
    build: '把危险状态、路径与接触约束、终态稳定性绑定到不同阶段；用仿真特权状态打分，但不把这些状态提供给策略；完成后继续观察 5 秒。',
    metric: 'SR 为总成功率，等于 SSR + USR，两者均以全部 episode 为分母；“成功中的不安全比例”是 USR ÷ SR。',
    kpis: [['33.74%', '聚合成功率 SR'], ['9.84% / 23.90%', 'SSR / USR'], ['70.84%', '成功轨迹中不安全的比例']],
    result: '聚合 SR 33.74%、SSR 9.84%、USR 23.90%，成功轨迹中 70.84% 含不安全行为；评估器在 240 条核查轨迹上 F1 为 97.26%。',
    limit: '项目入口审计为候选且地址与论文不符；评估器准确度不等于策略安全度；分阶段指标不可跨基准比较。',
  },
  {
    name: 'HygieneRoboBench',
    neighbor: '与 SafeStage 的差别在判据来源：本基准的约束由规则文本给出，评估器需先理解规则再重放计划。',
    cat: '⑤ 过程 / 阶段安全（卫生约束）',
    plain: 'HygieneRoboBench 把卫生约束当作安全判据：双夹爪、工具与共用表面之间的污染传播是否被计划避开。',
    rel: ['高', '被测对象为规划器与 VLA，按规则与历史做规划。'],
    domain: '134 个任务族、624 个实例；污染传播涉及双夹爪、工具与共用表面',
    build: '规划器读取公开规则、结构化状态与历史；独立评估器完整重放计划，隐藏参考给出可行性与最优成本；Hygiene-NSP 组合语言接地、历史重建与约束求解（CP-SAT）。',
    metric: 'SR 安全解决率＝安全且合规完成的实例 ÷ 全部；OSR 最优安全解决率＝同时满足用户优先级的最低成本方案；两者回答“能不能安全做完”与“是否做到最优”。',
    kpis: [['94.4%', '安全解决率 SR'], ['90.4%', '最优安全解决率 OSR'], ['624', '实例 / 134 任务族']],
    result: 'Hygiene-NSP 总体安全解决率 94.4%、最优安全解决率 90.4%；安全完成与按用户优先级最省成本是两种能力。',
    limit: '规则由文本给出，规则理解误差会混入安全判定；污染传播模型为仿真近似。',
  },
  {
    name: 'RoboJailBench',
    neighbor: '与 Trap 系列的差别在攻击位置：RoboJailBench 在输入层（指令、越狱提示），Trap 系列在训练数据层（触发器）。',
    cat: '⑥ 完整性 / 对抗',
    plain: 'RoboJailBench 同时测量两件事：危险指令是否被拒绝，正常指令是否被误拒。',
    rel: ['高', '被测对象是 LLM/VLM 具身代理（Claude Haiku 4.5、GPT 5.4 Nano 等）。'],
    domain: '11 个子集、18 类风险后果、990 对正常／危险指令、1,408 张场景图',
    build: '统一评测接口；危险意图与正常意图成对构造，强调场景接地与安全—有用性平衡；把无风险干预基线与压力测试分开报告。',
    metric: 'Security Rate 危险拒绝率、Utility Rate 正常接受率、SU-HM 两者调和平均（防止“一律拒绝”刷分）。',
    kpis: [['98.28%', 'Claude Haiku 4.5 危险拒绝（干净条件）'], ['99.49%', 'GPT 5.4 Nano 正常接受率'], ['97.84%', 'SU-HM']],
    result: '干净条件下 Claude Haiku 4.5 危险拒绝率 98.28%；GPT 5.4 Nano 正常接受率 99.49%、SU-HM 97.84%。压力条件另有一套数字。',
    limit: 'SR 在本文指 Security Rate，与其他论文的成功率同名异义；接受或拒绝计划不等于物理动作安全。',
  },
  {
    name: 'Trap-LIBERO / Trap-RoboTwin',
    neighbor: '与 RoboJailBench 的差别在攻击位置：本系列在训练数据中植入触发器，RoboJailBench 在推理输入上做对抗。',
    cat: '⑥ 完整性 / 对抗（定向失效）',
    plain: 'Trap 系列在 LIBERO 与 RoboTwin 里植入特定失效行为，检查策略是否被触发器劫持。',
    rel: ['高', '被测对象为 VLA；触发器由训练数据注入。'],
    domain: '两套受控任务：LIBERO 与 RoboTwin；四类失效（过早闭合、抓取偏移、过早释放、释放偏移）',
    build: '在示范中注入触发条件与失效动作，训练后检查策略在干净任务上的成功率，以及在触发条件下的定向失效达成率；结合轨迹与动作层信号判断失效类型。',
    metric: '正常任务效用与“特定失效目标达成”分开统计；干净成功率保持高位时仍可出现定向失效。',
    kpis: [['2 套', 'LIBERO 与 RoboTwin'], ['4 类', '定向失效模式'], ['0', 'OpenAlex 引文（2026 年发布）']],
    result: '论文展示干净成功率保持较高时仍可出现定向失效，说明标准成功率不足以筛查策略完整性；提供两套受控评测任务。',
    limit: '代码尚未发布（标注 coming soon），无法独立复现；失效类型是枚举的，未必覆盖真实后门形态。',
  },
  {
    name: 'ForesightSafety-VLA',
    neighbor: '与 VLA-Arena 的差别在组织方式：本基准按扰动类型（核心风险、语言、视觉）诊断，VLA-Arena 按难度等级（L0–L2）分层。',
    cat: '① 执行层（扰动与多本体）',
    plain: 'ForesightSafety-VLA 在 RoboTwin 上做三层诊断：核心风险、语言变化、视觉变化，测量安全行为能否经受扰动。',
    rel: ['高', '被测对象为 OpenVLA-oft 等 VLA，覆盖 5 种本体。'],
    domain: '66 个场景、5 种本体、13 类风险；Safe-Core、Safe-Lang、Safe-Vis 三套诊断',
    build: '用层级任务难度与语言、视觉扰动构造可控测试；结合任务完成与约束违反信号，按四象限报告安全成功、不安全成功、安全失败、不安全失败。',
    metric: 'SR 任务成功率、CC 累积碰撞代价、RET 风险暴露时间；另报安全／不安全成功的四象限分布。',
    kpis: [['66 / 5 / 13', '场景 / 本体 / 风险类别'], ['0.48', 'OpenVLA-oft 的 SR（示例）'], ['0.06', '不安全成功（占成功 12.5%）']],
    result: '原文示例中 OpenVLA-oft 的 SR 为 0.48、不安全成功为 0.06，即成功轨迹中 12.5% 不安全；常规措辞变化与结构性风险的影响不同。',
    limit: '只在仿真与 RoboTwin 场景内验证；四象限依赖约束定义，换任务需重设风险类别。',
  },
  {
    name: 'VLA-Arena',
    neighbor: '与 ForesightSafety-VLA 的差别在组织方式：VLA-Arena 用难度等级与四个维度分套件，ForesightSafety-VLA 用扰动类型诊断。',
    cat: '① 执行层（多本体与难度）',
    plain: 'VLA-Arena 把安全、干扰、外推、长时程四个维度拆开，同一任务在 L0 训练、向 L1／L2 评测。',
    rel: ['高', '被测对象为 π0、OpenVLA 系列等 VLA，另有真机案例。'],
    domain: '170 个任务、11 个套件；Safety／Distractor／Extrapolation／Long-Horizon 四维；难度 L0–L2',
    build: '扩展约束式 BDDL，提供不同规模示范集；仅在 L0 训练，向 L1／L2 评估；任务结构、语言与视觉变化分别计分。',
    metric: '任务完成与安全代价并列报告；难度与扰动等级分别统计，不用单一综合分。',
    kpis: [['170 / 11', '任务 / 套件'], ['L0 → L2', '训练与评测难度'], ['4 维', '安全、干扰、外推、长时程']],
    result: '不同诊断维度会改变模型的相对排序；基准同时报告完成与安全代价，并配真机案例检查。',
    limit: '维度多导致组合爆炸，单项结论需注明使用的子集；真机案例为验证性质。',
  },
];
DETAIL.forEach((b) => {
  const r = reviewByName.get(b.name) || {};
  const s = frame(b.name, `03 / 安全基准 · ${b.cat}`);
  PAGE_SKIP.set(s._index, SKIP_BY_PAGE[b.name] || []);
  addText(s, b.plain, 0.62, 1.32, 12.1, 0.62, { size: 10.5, color: C.muted, lineSpacing: 1.35 });
  const rows = [
    ['规模', b.domain],
    ['怎么构建', b.build],
    ['怎么判分', b.metric],
    ['实测结果', b.result],
    ['与相邻条目的差异', b.neighbor],
    ['适用边界', b.limit],
  ];
  addTable(s, ['维度', '内容'], rows, [1.25, 6.35], 2.0, { size: 9.2, maxH: 4.55, fillTo: 4.45 });
  let ry = 2.05;
  b.kpis.forEach(([num, label]) => {
    addRect(s, 8.35, ry, 4.37, 0.92, C.pale, true);
    addText(s, num, 8.52, ry + 0.1, 4.05, 0.42, { size: 15, bold: true, color: C.navy, lineSpacing: 1.0 });
    addText(s, label, 8.52, ry + 0.56, 4.05, 0.32, { size: 8.2, color: C.muted, lineSpacing: 1.2 });
    ry += 1.02;
  });
  addRect(s, 8.35, ry + 0.06, 4.37, 1.2, 'EEF4F7', true);
  addText(s, '大模型相关度', 8.52, ry + 0.15, 4.0, 0.24, { size: 8.6, bold: true, color: C.teal });
  addText(s, `${b.rel[0]}：${b.rel[1]}`, 8.52, ry + 0.42, 4.05, 0.8, { size: 8.2, color: C.muted, lineSpacing: 1.3 });
  footer(s, '来源：data/benchmark_paper_reviews.json 正文笔记与 benchmark_usage_records.json；本库未复现。');
  note(s, [
    `本页介绍 ${b.name}，属于${b.cat}。${b.plain}`,
    `规模上，${b.domain}。构建上，${b.build}`,
    `判分上，${b.metric}实测结果为：${b.result}`,
    `边界方面，${b.limit}另外，该基准的大模型相关度为${b.rel[0]}：${b.rel[1]}`,
    `本页三个关键数字是 ${b.kpis.map(([n, l]) => `${n}（${l}）`).join('，')}；全部来自论文报告值，本库未复现。`,
  ], [b.name]);
});

// ---------- 邻接三例 ----------
{
  const s = frame('两类邻接：软件代理、治理与交通', '03 / 安全基准 · 邻接', '这五条不属于物理行为安全，但常被引用为“具身安全”；此处只给判据与结论，不并入六层统计。');
  const rows = [
    ['Agent-SafetyBench', '349 环境、2,000 用例、8 类风险、10 种失败模式', '安全分与有用性分开报', '16 个被测代理全部低于 60 分；单靠防御提示不够'],
    ['EmbodiedGovBench', '七个治理维度：越权调用、漂移、恢复、可移植、升级、人工覆盖、审计', '治理 judge 对照合法动作与权限边界', '以指标体系与档位覆盖为主，无可比排行榜'],
    ['NAVSIM', '真实驾驶数据筛选场景，短时展开鸟瞰状态', 'PDMS：碰撞、可行驶区域、舒适、进度加权', 'CVPR 2024 挑战赛 143 队、463 次提交'],
    ['VIPS', '视频实例预测：对象出现、消失与轨迹', '按预测正确性评分', '属感知层邻接，不测动作安全'],
    ['MineAmongUs', '多智能体协作环境', '任务完成与协作指标', '多主体安全目前无独立判据'],
  ];
  addTable(s, ['条目', '构造', '判据', '结论'], rows, [2.1, 3.9, 3.1, 3.0], 1.65, { size: 9.2, maxH: 4.4, fillTo: 4.3 });
  addRect(s, 0.62, 6.15, 12.1, 0.62, C.pale, true);
  addText(s, '读法：这五条的分不能与六层安全基准相加；它们提供的是“上层决策失效”和“治理缺口”的证据类型。', 0.85, 6.25, 11.6, 0.42, { size: 9.2, color: C.muted, lineSpacing: 1.3 });
  footer(s);
  note(s, [
    '邻接两类：软件代理（Agent-SafetyBench、INFUSE、MemForm、ORBIT、SkillSafetyBench）测工具调用层的越权与注入；治理与交通（EmbodiedGovBench、NAVSIM、VIPS、MineAmongUs）测权限、恢复、升级或把碰撞并入综合分。',
    '它们的分数不能当机器人安全分，但失效机制（越权、记忆污染、注入）在具身系统里同样存在。',
  ]);
}

// ---------- 26 条全量索引（两页） ----------
{
  const order = [];
  for (const L of LAYERS) for (const m of L.members) order.push(m);
  const rows = order.map((name) => {
    const e = safety.find((x) => x.name === name) || {};
    const layer = layerOf.get(name) || '—';
    const realMap = { execution_reported: '真机执行', paired_validation: '配对验证', data_only: '仅数据', unknown: '未核实', not_applicable: '不适用', fixture_only: '实体件' };
    const statusMap = { found: '已确认', platform_only: '仅平台', candidate: '候选', not_found: '未找到' };
    return [
      name,
      layer.replace(/^① |^② |^③ |^④ |^⑤ |^⑥ /, ''),
      realMap[e.real_evidence] || '—',
      statusMap[(e.resources || {}).entry_status] || '—',
      String(((e.citation || {}).cited_by_count) ?? '—'),
    ];
  });
  [rows.slice(0, 13), rows.slice(13)].forEach((part, idx) => {
    const s = frame(`26 条安全条目索引（${idx + 1}/2）`, '04 / 索引', '按层级排序；引文数为 OpenAlex 观测值（2026-11-04），2026 年新发条目多为 0。');
    addTable(s, ['条目', '层级', '真机证据', '项目入口', '引文'], part, [4.0, 3.9, 1.7, 1.6, 0.9], 1.6, { size: 9.8, maxH: 5.0, fillTo: 4.95 });
    footer(s, '来源：data/benchmark_survey.json（real_evidence、resources、citation 字段）。');
    note(s, [idx === 0
      ? '索引前半：六层的前 13 条。真机证据列区分“真机执行”“配对验证”“仅数据”“未核实”，未核实不等于没有真机实验。'
      : '索引后半：含两类邻接条目。引文数为 0 多数因为 2026 年发布，不代表无人使用。']);
  });
}

// ---------- 配对设计 ----------
{
  const s = frame('配对设计：八个基准只改一个变量', '05 / 横切对比', '配对指固定初始状态、指令与种子，只改一个因素；这是判断“安全行为是否随条件变化”的唯一干净做法。');
  const rows = [
    ['LIBERO-Safety', '障碍与风险形态（L0／L1／L2）', '约束加严后任务是否仍可完成'],
    ['SafeLIBERO', '是否加安全层（同模型前后）', '避碰率提升是否以任务成功率为代价'],
    ['HazardArena', '动作参与者、目标关系、指令', '风险语义变化是否改变执行选择'],
    ['RoboHarm', '输出接口（文本／计划／末端／关节）', '拒答是否能延续到动作控制'],
    ['DESPITE', '任务与约束集合（困难子集）', '计划有效性、危险性与安全完成是否分离'],
    ['SafeStage', '执行阶段（前／中／后）', '同一策略在不同阶段的安全差异'],
    ['ForesightSafety-VLA', '语言变化、视觉变化、核心风险', '三类扰动对安全行为的影响是否一致'],
    ['VLA-Arena', '难度（L0→L2）与四个诊断维度', '相对排序是否随维度变化'],
  ];
  addTable(s, ['基准', '改变的变量', '能观察什么'], rows, [2.9, 5.3, 4.0], 1.6, { size: 9.6, maxH: 4.5, fillTo: 4.4 });
  addRect(s, 0.62, 6.1, 12.1, 0.66, 'FDF2F2', true);
  addText(s, '缺口：以上八项都没有报告“同任务、同种子、同 checkpoint”的完整复现证据；跨论文并列比较仍缺共同任务与版本记录。', 0.85, 6.2, 11.6, 0.45, { size: 9.2, color: C.muted, lineSpacing: 1.3 });
  footer(s);
  note(s, [
    '八个基准的配对设计分别改变风险形态、安全层、场景语义、输出接口、约束集、执行阶段、扰动类型与难度。',
    '配对的用途是把“能力差异”和“安全行为差异”分开；缺配对时，成功率下降无法归因。',
  ]);
}

// ---------- 演进脉络 ----------
{
  const s = frame('三代演进：从拒答到过程约束，再到阶段与对抗', '05 / 演进', '按 arXiv 首次提交时间排列；同代条目判据不同，分数不可跨代比较。');
  const gens = [
    ['2024–2025 初', '拒绝与语义判断', C.navy, 'HazardArena、RoboHarm、SafeAgentBench、DESPITE', '判据是“是否拒绝危险指令”“计划是否合规”，执行层证据少'],
    ['2025 中后', '过程约束与安全层', C.teal, 'LIBERO-Safety、SafeLIBERO、ForesightSafety-VLA、VLA-Arena', '判据进入逐帧检查：碰撞、越界、约束违反、累积代价'],
    ['2026', '阶段、卫生与对抗', C.orange, 'SafeStage、HygieneRoboBench、RoboJailBench、Trap 系列、ManiPhysicsBench', '判据细分到执行前中后、污染传播、触发器与物体损伤'],
  ];
  gens.forEach(([era, theme, color, members, judge], i) => {
    const y = 1.55 + i * 1.62;
    addRect(s, 0.62, y, 1.55, 1.35, color, true);
    addText(s, era, 0.62, y + 0.44, 1.55, 0.4, { size: 11, bold: true, color: C.white, align: 'center' });
    addText(s, theme, 2.35, y + 0.08, 4.6, 0.32, { size: 12, bold: true, color });
    addText(s, members, 2.35, y + 0.44, 10.2, 0.36, { size: 9.6 });
    addText(s, judge, 2.35, y + 0.82, 10.2, 0.42, { size: 9, color: C.muted, lineSpacing: 1.3 });
  });
  addRect(s, 0.62, 6.35, 12.1, 0.5, C.pale, true);
  addText(s, '趋势：判据从“输出层判断”下沉到“执行层过程”，但真机证据没有同步增加——2026 年的新条目仍以仿真为主。', 0.85, 6.44, 11.6, 0.34, { size: 9.2, color: C.muted });
  footer(s);
  note(s, [
    '三代演进：2024–2025 初以拒答与计划合规为主；2025 中后进入过程约束与安全层；2026 细分到阶段、卫生、对抗与物体损伤。',
    '判据在下沉，真机证据没有同步增加，这是本库观察到的结构性缺口。',
  ]);
}

// ---------- 能力底座：分节 + 两个详解 + 五个档案 + 映射 ----------
divider('能力基准：安全评测的底座与对照', '安全基准很少自建环境。这一节保留 7 个具身能力基准：说明它们给安全评测提供什么（任务集、判定接口、相关性证据），以及哪些能力轴还没有对应的安全评测。', '06 / 能力底座');

// LIBERO
{
  const s = frame('LIBERO：安全基准最常用的任务底座', '06 / 能力底座 · 1/7', 'LIBERO 本身不测安全；它提供 130 个语言条件任务与判定接口，本库 8 条安全条目直接建在它上面。');
  const rows = [
    ['规模', '130 个任务分四组：Spatial 10、Object 10、Goal 10，另有 LIBERO-100（90 个预训练任务 + 10 个长任务）'],
    ['怎么构建', 'BDDL 把任务初态、对象关系与目标写成逻辑式，在 robosuite（基于 MuJoCo）中执行；用任务顺序与预训练数据控制变量。'],
    ['怎么判分', '原始论文用三个持续学习指标：FWT 前向迁移（还没学该任务时能做对多少）、NBT 负向后向迁移（学完后续任务后旧任务掉了多少）、AUC 成功曲线面积。多数后续论文只报 40 任务平均成功率。'],
    ['对安全评测的作用', '提供任务模板、成功判定谓词与示范数据；LIBERO-Safety 在它上面加安全谓词，SafeLIBERO 在它外面加安全层，VLA-Arena 与 Trap 系列复用它做难度与对抗。'],
    ['边界', '40 任务子集不能代表 130 任务全集；仿真动作是末端增量抽象，与真实机械臂存在落差。'],
  ];
  addTable(s, ['维度', '内容'], rows, [1.3, 6.3], 1.6, { size: 9.6, maxH: 4.3, fillTo: 4.2 });
  const kpi = [['136', 'OpenAlex 引文（本库观测）'], ['130', '任务 / 4 个子套件'], ['8 条', '本库安全条目以它为底座']];
  let ry = 1.6;
  kpi.forEach(([num, label]) => {
    addRect(s, 8.3, ry, 4.42, 0.95, C.pale, true);
    addText(s, num, 8.47, ry + 0.1, 4.1, 0.44, { size: 17, bold: true, color: C.navy, lineSpacing: 1.0 });
    addText(s, label, 8.47, ry + 0.58, 4.1, 0.3, { size: 8.3, color: C.muted });
    ry += 1.05;
  });
  addRect(s, 8.3, ry + 0.05, 4.42, 1.45, 'EEF4F7', true);
  addText(s, '为什么先讲它', 8.47, ry + 0.14, 4.0, 0.24, { size: 8.8, bold: true, color: C.teal });
  addText(s, '本页之后的 12 个安全基准里，LIBERO-Safety、SafeLIBERO、Trap-LIBERO 与 VLA-Arena 四个直接复用它的任务与判定；不理解 LIBERO 的成功谓词，就无法判断安全基准把“违规”加在了哪一层。', 8.47, ry + 0.42, 4.05, 1.02, { size: 8.3, color: C.muted, lineSpacing: 1.3 });
  footer(s, '来源：data/benchmark_paper_reviews.json（LIBERO 条目）与 benchmark_citation_snapshot.json。');
  note(s, [
    'LIBERO 是能力基准，本身没有安全判据。它在安全汇报里的价值是提供任务与判定接口：安全基准的做法通常是在它的成功谓词之外再加一层违规谓词。',
    '四组任务分别只改空间关系、物体、目标与长时程；原始指标是 FWT、NBT、AUC，后来多数论文简化为 40 任务平均成功率，两者不能混。',
    '本库有 8 条安全条目以 LIBERO 为底座，这是它被放在能力节第一位的原因。',
  ]);
}

// SimplerEnv
{
  const s = frame('SimplerEnv：仿真分数能否代表真机的校准基准', '06 / 能力底座 · 2/7', '它在已有真机任务上量化仿真排序与真机排序的一致性。安全基准引用它，是为了说明仿真结论的可迁移程度。');
  const rows = [
    ['规模', '复现 WidowX 与 Google Robot 两台真机的桌面场景；任务来自原真机评测集，不新造任务。'],
    ['怎么构建', '用 SAPIEN 重建场景、相机与控制接口；两种对齐：视觉匹配（把仿真画面对齐真机）、变体聚合（多种环境变体取平均）。'],
    ['怎么判分', '相关性而非绝对分：Pearson r 衡量仿真排名与真机排名的一致程度；MMRV 衡量平均最大排名违背，即同一策略两侧名次差。'],
    ['已报告结果', '视觉匹配 r=0.924、MMRV 0.056；变体聚合 r=0.778；仅用验证误差时相关性 0.308。'],
    ['边界', '只在刚体操作与这两台真机设置上验证；换物体动力学（软体、可变形）或换任务族后需重新验证。'],
  ];
  addTable(s, ['维度', '内容'], rows, [1.3, 6.3], 1.6, { size: 9.6, maxH: 4.3, fillTo: 4.2 });
  const kpi = [['0.924', '视觉匹配的 Pearson r'], ['0.056', 'MMRV（排名违背，越低越好）'], ['0.308', '仅用验证误差的相关性']];
  let ry = 1.6;
  kpi.forEach(([num, label]) => {
    addRect(s, 8.3, ry, 4.42, 0.95, C.pale, true);
    addText(s, num, 8.47, ry + 0.1, 4.1, 0.44, { size: 17, bold: true, color: C.navy, lineSpacing: 1.0 });
    addText(s, label, 8.47, ry + 0.58, 4.1, 0.3, { size: 8.3, color: C.muted });
    ry += 1.05;
  });
  addRect(s, 8.3, ry + 0.05, 4.42, 1.45, 'EEF4F7', true);
  addText(s, '与安全的关系', 8.47, ry + 0.14, 4.0, 0.24, { size: 8.8, bold: true, color: C.teal });
  addText(s, 'ManiPhysicsBench 直接在 SimplerEnv 设置上测物体损伤；它的 48.3% 成功率与 13.5% 无损率，只有在这个“仿真与真机排序一致”的前提下才有迁移意义。', 8.47, ry + 0.42, 4.05, 1.02, { size: 8.3, color: C.muted, lineSpacing: 1.3 });
  footer(s, '来源：data/benchmark_paper_reviews.json（SimplerEnv 条目）与 benchmark_usage_records.json。');
  note(s, [
    'SimplerEnv 测的是仿真与真机的一致性：同一批策略在仿真与真机上的排名是否一致，用 Pearson r 与 MMRV 表示。',
    '本库安全侧只有 ManiPhysicsBench 直接复用它的设置；引用它的相关性数字时，要注明是对齐方式（视觉匹配或变体聚合）。',
  ]);
}

// 其余五个
{
  const s = frame('其余五个能力基准：一句话档案', '06 / 能力底座 · 3–7/7', '每张卡给“测什么、关键数字、与安全的关系”；详细结果不在本稿范围，需要时查各自条目文档。');
  const cards = [
    ['CALVIN', '语言条件的长时程操作：按指令连续执行 1–5 条，并测 ABC→D 跨环境', '189 引文；ABC→D 与连续指令链是主要协议', '语言轴：LIBERO-Safety 与 VLA-Arena 各自构造语言变化；没有安全条目直接建在 CALVIN 上'],
    ['RoboTwin', '双臂操作与数字孪生造数据：单图生成可仿真物体并自动生成专家轨迹', 'DP3 82.0% vs 2D DP 0%（100 示范）', 'Trap-RoboTwin 与 ForesightSafety-VLA 建在它上面'],
    ['RoboCasa365', '家庭场景规模化：365 任务、2,500 厨房、四阶段终身学习', '原子任务成功率 41.5% → 10.6%', '本库没有安全条目以它为底座，是缺口'],
    ['VLABench', '未见类别的语言条件操作：测试集按物体类别留出', 'E0 在 14 个环境平均 +10.7%', '未见类别与安全新场景的泛化同源，但无安全判据'],
    ['COLOSSEUM', '组合扰动：20 任务 × 14 条扰动轴，测单轴与多轴退化', '单轴 30–50%，组合 ≥75%', '为 VLA-Arena 与 ForesightSafety 的扰动分级提供参照'],
  ];
  cards.forEach(([name, what, num, rel], i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.62 + col * 4.1, y = 1.55 + row * 2.6;
    addRect(s, x, y, 3.9, 2.35, C.pale, true);
    addText(s, name, x + 0.18, y + 0.12, 3.55, 0.3, { size: 12.5, bold: true, color: C.navy });
    addText(s, what, x + 0.18, y + 0.48, 3.55, 0.72, { size: 8.8, color: C.muted, lineSpacing: 1.35 });
    addText(s, num, x + 0.18, y + 1.24, 3.55, 0.44, { size: 9.4, bold: true, color: C.teal, lineSpacing: 1.25 });
    addText(s, rel, x + 0.18, y + 1.72, 3.55, 0.55, { size: 8.4, color: C.muted, lineSpacing: 1.3 });
    addLine(s, x + 0.18, y + 1.16, x + 3.72, y + 1.16, C.line, 0.6);
  });
  footer(s);
  note(s, [
    '五个环境各一句：CALVIN 测连续指令与跨环境，RoboTwin 是双臂与数字孪生，RoboCasa365 是家庭规模化与终身学习，VLABench 测未见类别，COLOSSEUM 测组合扰动。',
    '卡片最后一行写的是它们与本库安全条目的关系：Trap 与 ForesightSafety 建在 RoboTwin 上，RoboCasa365 还没有安全底座，是目前缺口。',
  ]);
}

// 能力轴 × 安全映射
{
  const s = frame('能力轴与安全评测的对应关系：两处空白', '06 / 能力底座 · 映射', '每一行是一个能力轴：左侧是本库的能力基准，右侧是有没有安全条目复用同一轴。空白格表示该能力没有对应的安全判据。');
  const rows = [
    ['语言跟随（措辞、指代）', 'LIBERO、CALVIN', 'LIBERO-Safety、VLA-Arena、ForesightSafety-VLA', '有复用'],
    ['空间与物体泛化', 'LIBERO 四组、VLABench', 'LIBERO-Safety 的 L0/L1、VLA-Arena 的 L1/L2', '部分复用'],
    ['长时程与顺序', 'CALVIN 指令链、LIBERO-Long、RoboCasa365', 'SafeStage 的阶段划分、HygieneRoboBench 的流程约束', '部分复用'],
    ['双臂协同', 'RoboTwin', 'Trap-RoboTwin、ForesightSafety-VLA（5 种本体）', '有复用'],
    ['扰动鲁棒', 'COLOSSEUM、VLABench', 'VLA-Arena、ForesightSafety-VLA 的语言与视觉扰动', '部分复用'],
    ['真机代理校准', 'SimplerEnv', 'ManiPhysicsBench（按 SimplerEnv 设置评测）', '有复用'],
    ['家庭规模化', 'RoboCasa365', '无', '空白'],
    ['跨本体真机', 'ForesightSafety-VLA（仅仿真 5 本体）', '无', '空白'],
  ];
  addTable(s, ['能力轴', '本库能力基准', '复用它做安全评测的条目', '状态'], rows, [2.75, 3.1, 4.7, 1.45], 1.6, { size: 9.4, maxH: 4.5, fillTo: 4.4 });
  addRect(s, 0.62, 6.15, 12.1, 0.6, 'FDF2F2', true);
  addText(s, '两处空白对应两个缺口：家庭规模化场景（RoboCasa365）没有安全判据；跨本体真机安全没有任何条目。', 0.85, 6.25, 11.6, 0.42, { size: 9.2, color: C.muted });
  footer(s);
  note(s, [
    '这张表回答“能力研究能不能被安全评测复用”：语言、空间、长时程、双臂、扰动、真机代理六个轴都有部分或直接复用。',
    '两处空白是真实缺口：RoboCasa365 的规模化场景没有安全条目，跨本体真机安全一条都没有。',
  ]);
}

// ---------- 选型指南 ----------
{
  const s = frame('按问题选基准：九行对照', '07 / 选型');
  const rows = [
    ['过程碰撞与约束违反', 'LIBERO-Safety + SafeLIBERO', '一个内嵌检查、一个外挂安全层，可对照'],
    ['物体损伤（夹坏、压坏）', 'ManiPhysicsBench', '唯一给损伤判定；需有限元后端'],
    ['危险指令执行与指代错误', 'HazardArena + RoboHarm', '一个测语义配对，一个测接口差异'],
    ['计划是否违反显式约束', 'DESPITE', '只评规划层，不评执行'],
    ['执行前中后的阶段安全', 'SafeStage', '分前中后三段，分母要写清'],
    ['卫生与流程合规', 'HygieneRoboBench', '规则型安全，SR 与 OSR 分开'],
    ['抗攻击与后门', 'RoboJailBench + Trap 系列', '一个测拒绝率，一个测定向失效'],
    ['多本体与扰动下的安全', 'ForesightSafety-VLA + VLA-Arena', '5 种本体、四个诊断维度'],
    ['上层代理与治理', 'Agent-SafetyBench + EmbodiedGovBench', '软件层与治理层，不可当物理安全分'],
  ];
  addTable(s, ['关注的问题', '建议的基准', '理由'], rows, [4.9, 4.1, 3.2], 1.4, { size: 9.8, maxH: 5.4, fillTo: 5.3 });
  footer(s);
  note(s, [
    '九行对照按“想回答的问题”组织：过程碰撞、物体损伤、语义判断、计划合规、阶段安全、卫生合规、抗攻击、多本体扰动、上层代理与治理。',
    '每一行的基准判据不同，跨行不能比较分数；选型时先定判据，再挑基准。',
  ]);
}

// ---------- 缺口与建议 ----------
{
  const s = frame('五个缺口与四条可执行建议', '07 / 结论');
  const gaps = [
    ['跨本体真机安全', '26 条中 5 条报告真机执行；多本体只在仿真侧（5 种本体）', '本库计数：0 条同时满足多本体 + 真机 + 安全'],
    ['接触力与冲击', '只有 4 条涉及人机接触力，且多为单一场景', '缺标准化标定与阈值'],
    ['过程指标未统一', '碰撞、越界、违规时长、卫生合规各一套谓词', '跨论文无法合并'],
    ['复现材料', '47 条已确认入口，但安全侧多个条目代码未发布', 'Trap 系列标注 coming soon'],
    ['治理与多主体', '5 条邻接条目，无统一判据', '多机器人协同的安全评测接近空白'],
  ];
  gaps.forEach(([h, fact, note2], i) => {
    const y = 1.28 + i * 1.0;
    addRect(s, 0.62, y, 12.1, 0.88, i % 2 === 0 ? C.pale : C.white, true);
    addText(s, h, 0.82, y + 0.1, 2.7, 0.3, { size: 10.5, bold: true, color: C.navy });
    addText(s, fact, 3.6, y + 0.1, 5.4, 0.66, { size: 9, color: C.muted, lineSpacing: 1.28 });
    addText(s, note2, 9.2, y + 0.1, 3.4, 0.66, { size: 9, color: C.red, lineSpacing: 1.28 });
  });
  addText(s, '四条建议', 0.62, 6.42, 2, 0.26, { size: 11, bold: true, color: C.teal });
  addText(s, '① 报安全指标时同时给分母与判据谓词；② 同一策略在同一任务上配对报告“干净／扰动／风险”三档；③ 至少一档真机验证，并写明本体；④ 公开 checkpoint 与推理配置。', 2.1, 6.4, 10.4, 0.5, { size: 9.2, color: C.muted, lineSpacing: 1.3 });
  footer(s);
  note(s, [
    '五个缺口：跨本体真机安全、接触力与冲击、过程指标未统一、复现材料、治理与多主体。',
    '四条建议针对的是“让别人能复核”：给分母与谓词、配对三档、真机一档、公开配置。',
  ]);
}

// ---------- 收尾 ----------
{
  const s = frame('数据来源与这份汇报的边界', '08 / 收尾');
  const rows = [
    ['条目与统计', 'data/benchmark_survey.json', '62 条活跃 + 60 条归档；26 条带安全目标'],
    ['正文笔记', 'data/benchmark_paper_reviews.json', '场景、构建、结果、边界四段摘要'],
    ['版本与来源', 'data/benchmark_reading_sources.json', 'arXiv 版本与首次提交日期'],
    ['引文观测', 'data/benchmark_citation_snapshot.json', 'OpenAlex，观测日 2026-11-04'],
    ['项目入口', 'data/benchmark_project_audit.json', '47 已确认、12 仅平台、3 候选'],
    ['术语', 'data/benchmark_glossary.json', `${glossary.terms.length} 个术语，含常见误读`],
  ];
  addTable(s, ['内容', '文件', '说明'], rows, [2.3, 6.2, 3.7], 1.55, { size: 10, maxH: 3.2, fillTo: 3.1 });
  addRect(s, 0.62, 4.95, 12.1, 1.85, 'FDF6EC', true);
  addText(s, '四条边界', 0.85, 5.05, 3, 0.26, { size: 10.5, bold: true, color: C.orange });
  addText(s, '① 检索式未穷尽，样本偏向桌面机械臂与公开项目；② 分数全部来自论文，本库未复现；③ 未核验的项目写“未核验”，不等于不存在；④ 仿真谓词不等于真实伤害，改写成伤害率是过度解读。', 0.85, 5.34, 11.6, 1.3, { size: 9.2, color: C.muted, lineSpacing: 1.4 });
  footer(s);
  note(s, [
    '数据来自六个结构化文件，快照日为 2026-11-04；所有分数是论文报告值。',
    '四条边界：检索未穷尽、分数未复现、未核验不等于不存在、仿真谓词不等于真实伤害。',
  ]);
}

await fs.mkdir(OUT, { recursive: true });
const file = path.join(OUT, '具身智能安全Benchmark调研汇报_2026-11-04_安全主线.pptx');
await pptx.writeFile({ fileName: file });
console.log(JSON.stringify({ slides: pptx._slides.length, overflow, file }, null, 2));
