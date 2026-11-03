/** Build the research workbook with @oai/artifact-tool. No source sheet is overwritten. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const outDir = path.join(root, 'data');
const qaDir = path.join(root, '.survey_work');
await fs.mkdir(qaDir, { recursive: true });
const inputPaths = ['data/benchmark_survey.json', 'data/survey_paper_registry.json'];
const bytes = await Promise.all(inputPaths.map(p => fs.readFile(path.join(root, p))));
const [survey, registry] = bytes.map(b => JSON.parse(b.toString('utf8')));
const sha = b => createHash('sha256').update(b).digest('hex');
const types = { benchmark: '评测任务集', dataset: '训练数据集', platform: '仿真平台', framework: '评测框架', method: '方法论文', unreviewed: '未分类' };
const relevance = { direct: '直接具身评测', support: '具身研究底座', adjacent: '软件代理邻接研究' };
const objectives = { capability: '能力', robustness: '鲁棒性', safety: '安全' };
const settings = { offline_image: '静态情境／图像', offline_video: '视频理解', offline_trace: '离线轨迹', symbolic: '符号规划', simulation: '交互仿真', real_robot: '真实执行', real_dataset: '真实数据', software: '软件环境', runtime: '运行时原型', physical_fixture: '实体测试件' };
const real = { execution_reported: '报告真实执行', paired_validation: '模拟／真实配对验证', data_only: '仅真实数据', fixture_only: '仅实体测试件', unknown: '尚未确认执行实验', not_applicable: '不适用' };
const project = { found: '已确认项目入口', platform_only: '仅平台入口', candidate: '候选待确认', not_found: '未找到已确认入口' };
const join = (xs, dict) => xs.map(x => dict?.[x] ?? x).join('；');
const col = n => { let s = ''; for (n++; n; n = Math.floor((n - 1) / 26)) s = String.fromCharCode(65 + (n - 1) % 26) + s; return s; };
const wb = Workbook.create();
const overview = wb.worksheets.add('调研概览');
const entries = wb.worksheets.add('条目分类');
const protocols = wb.worksheets.add('评测协议');
const sources = wb.worksheets.add('论文证据');
const navy = '#17324D', teal = '#0D716F', gray = '#566579';

// Flat, filterable source tables; long protocol text has its own sheet.
function table(sheet, headers, rows, widths, name) {
  const end = `${col(headers.length - 1)}${rows.length + 1}`;
  const range = sheet.getRange(`A1:${end}`);
  range.values = [headers, ...rows];
  range.format.font = { name: 'Microsoft YaHei', size: 10, color: navy };
  range.format.wrapText = true;
  range.format.verticalAlignment = 'top';
  for (let c = 0; c < widths.length; c++) sheet.getRange(`${col(c)}1:${col(c)}${rows.length + 1}`).format.columnWidthPx = widths[c];
  for (let r = 0; r < rows.length; r++) {
    const lines = Math.max(...rows[r].map((v, c) => {
      if (v == null || typeof v !== 'string') return 1;
      return v.split('\n').reduce((sum, line) => {
        const px = Array.from(line).reduce((x, ch) => x + (ch.charCodeAt(0) > 255 ? 14 : 7.5), 0);
        return sum + Math.max(1, Math.ceil(px / (widths[c] - 18)));
      }, 0);
    }));
    const rowRange = sheet.getRange(`A${r + 2}:${col(headers.length - 1)}${r + 2}`);
    rowRange.format.rowHeightPx = Math.min(480, Math.max(48, lines * 19 + 14));
    if (r % 2 === 1) rowRange.format.fill = '#F0F5F8';
  }
  const header = sheet.getRange(`A1:${col(headers.length - 1)}1`);
  header.format.fill = navy;
  header.format.font = { name: 'Microsoft YaHei', bold: true, color: '#FFFFFF', size: 10 };
  header.format.rowHeightPx = 40;
  const t = sheet.tables.add(`A1:${end}`, true, name);
  t.showFilterButton = true;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(2);
  sheet.showGridLines = false;
  sheet.tabColor = teal;
}

const entryHeaders = ['条目', '关注范围', '主要成果', '具身关联', '研究目标', '应用场景', '执行层级', '真机证据', '项目入口状态', '来源初投年', 'OpenAlex 被引', '引用观测日期', '原表使用关联', '分类依据', '原论文', '项目入口', '资源完整性核查', '独立采用核查', '文档路径', '条目 ID'];
const entryRows = survey.entries.map(e => [e.name, e.focus === 'active' ? '重点' : '非重点档案', types[e.primary_type], relevance[e.relevance] ?? '未分类', join(e.objectives, objectives) || '未分类', join(e.domains) || '未分类', join(e.settings, settings) || '未分类', real[e.real_evidence] ?? '未分类', project[e.resources.entry_status], e.source?.year ?? null, e.citation?.cited_by_count ?? null, e.citation?.cited_by_count != null && e.citation?.snapshot_date ? new Date(`${e.citation.snapshot_date}T00:00:00Z`) : null, e.usage.associated_use_papers, e.type_reason ?? '本轮未重新核查', e.source?.url ?? null, e.resources.urls.join('\n'), '未核查', '未核查', `benchmarks/${e.document}`, e.entry_id]);
table(entries, entryHeaders, entryRows, [240,110,125,140,155,185,205,175,155,100,110,120,110,350,330,340,140,140,370,180], 'SurveyEntries');
entries.getRange('J2:K123').setNumberFormat('0');
entries.getRange('L2:L123').setNumberFormat('yyyy-mm-dd');
entries.getRange('M2:M123').setNumberFormat('0');
entries.getRange('K2:K123').format.font.color = '#177364';

const active = survey.entries.filter(e => e.focus === 'active');
table(protocols, ['条目', '评测单位', '指标：含义与分母', '对照与划分', '重复／统计及边界', '关心的问题', '核心场景', '技术实现', '论文结果', '适用边界', '证据章节', '阅读版本', '正文来源'],
  active.map(e => [e.name, e.unit, e.metrics.map(m => `${m[0]}：${m[1]}\n分母／单位：${m[2]}`).join('\n\n'), e.control, e.statistics, e.summary.question, e.summary.scenarios, e.summary.implementation, e.summary.results, e.summary.limits, e.evidence.classification_basis.sections.join('\n'), e.source.version, e.source.fulltext_url]),
  [240,210,410,380,380,390,460,460,460,410,300,150,350], 'SurveyProtocols');

table(sources, ['书目 ID', '原始标题', '初始表来源', '原表行号', '已读关联条目', '阅读状态', '阅读版本', '初次提交日期', '作者', '正式出版字段（已知）', '原链接', '阅读正文来源'],
  registry.papers.map(p => [p.paper_id, p.title, p.in_original_table ? '原始 193 行' : '补入原始来源', p.raw_row_indices.join('；'), p.reviewed_benchmarks.join('；'), p.reviewed_source ? '重点章节核查' : '无本轮重点章节标记', p.reviewed_source?.version ?? null, p.reviewed_source?.first_submitted ? new Date(p.reviewed_source.first_submitted) : null, p.reviewed_source?.authors.join('；') ?? null, p.reviewed_source?.journal_ref ?? null, p.url, p.reviewed_source?.fulltext_url ?? null]),
  [105,560,145,100,230,190,150,140,440,380,390,390], 'SurveySources');
sources.getRange(`H2:H${registry.papers.length + 1}`).setNumberFormat('yyyy-mm-dd');

overview.showGridLines = false;
overview.tabColor = navy;
overview.getRange('A1:F34').format.font = { name: 'Microsoft YaHei', size: 11, color: navy };
overview.getRange('A1:F34').format.rowHeightPx = 32;
overview.getRange('A1:A34').format.columnWidthPx = 210;
overview.getRange('B1:B34').format.columnWidthPx = 100;
overview.getRange('C1:C34').format.columnWidthPx = 240;
overview.getRange('D1:D34').format.columnWidthPx = 30;
overview.getRange('E1:E34').format.columnWidthPx = 210;
overview.getRange('F1:F34').format.columnWidthPx = 100;
function band(range, text, color = navy) {
  const r = overview.getRange(range); r.merge(); r.values = [[text]];
  r.format.fill = color; r.format.font = { name: 'Microsoft YaHei', bold: true, color: '#FFFFFF', size: 12 };
}
function note(range, text) { const r = overview.getRange(range); r.merge(); r.values = [[text]]; r.format.wrapText = true; r.format.verticalAlignment = 'center'; r.format.font.color = gray; }
band('A1:F2', '具身智能与安全 Benchmark 调研');
note('A3:F4', `更新：${survey.as_of}｜分类基于正文重点章节笔记。当前样本不代表领域全量；未知不算作“不具备”。`);
band('A6:C6', '调查范围'); band('E6:F6', '主要成果类型（互斥）');
overview.getRange('A7:A12').values = [['登记条目'],['已分类重点条目'],['未分类档案'],['直接具身任务集'],['已核验引用观测'],['报告真实执行／配对']];
const q = "'条目分类'!";
const formulas = [
  `=COUNTA(${q}$A$2:$A$123)`, `=COUNTIF(${q}$B$2:$B$123,"重点")`,
  `=COUNTIF(${q}$C$2:$C$123,"未分类")`,
  `=COUNTIFS(${q}$C$2:$C$123,"评测任务集",${q}$D$2:$D$123,"直接具身评测")`,
  `=COUNT(${q}$K$2:$K$123)`,
  `=COUNTIF(${q}$H$2:$H$123,"报告真实执行")+COUNTIF(${q}$H$2:$H$123,"模拟／真实配对验证")`
];
overview.getRange('B7:B12').formulas = formulas.map(x => [x]);
overview.getRange('C7:C12').values = [['条目，不是同质任务集'],['已人工编码'],['非重点，未继续扩读'],['排除软件代理任务集'],['空值不是零引用'],['不据此推算全领域比例']];
overview.getRange('E7:E11').values = ['benchmark','dataset','platform','framework','method'].map(t => [types[t]]);
overview.getRange('F7:F11').formulas = [7,8,9,10,11].map(r => [`=COUNTIF(${q}$C$2:$C$123,E${r})`]);
overview.getRange('E12').values = [['已分类合计']]; overview.getRange('F12').formulas = [['=SUM(F7:F11)']];
band('A15:C15', '来源与证据'); band('E15:F15', '项目入口（重点条目）');
overview.getRange('A16:A19').values = [['原始书目记录'],['补入已读来源'],['书目记录合计'],['运行复现']];
overview.getRange('B16:B18').formulas = [[`=COUNTIF('论文证据'!$C$2:$C$${registry.paper_count+1},"原始 193 行")`],[`=COUNTIF('论文证据'!$C$2:$C$${registry.paper_count+1},"补入原始来源")`],['=SUM(B16:B17)']];
overview.getRange('B19').values = [['未完成']];
overview.getRange('C16:C19').values = [['原始表保留不覆盖'],['按确切书目身份连接'],['不等于已读论文数'],['资源完整性与采用待核']];
overview.getRange('E16:E18').values = [['已确认项目入口'],['仅平台入口'],['候选待确认']];
overview.getRange('F16:F18').formulas = [16,17,18].map(r => [`=COUNTIFS(${q}$I$2:$I$123,E${r},${q}$B$2:$B$123,"重点")`]);
band('A22:F22', '使用与比较口径', teal);
note('A23:F24', '条目分类：筛选主要成果、具身关联、研究目标、执行层级和资源入口。表头可筛选，前两列与首行冻结；向右滚动查看来源。');
note('A25:F26', '评测协议：62 个重点条目的指标含义、分母、对照、实现与论文结果。问题、轨迹、任务数和 rollout 数不可直接比较或求平均。');
note('A27:F28', '论文证据：199 个书目记录及其已读版本。OpenAlex 被引量不等于独立采用量；版本不相加。原表使用关联未完成全文独立采用核查。');
note('A29:F30', '更新源：data/benchmark_survey_annotations.json 与正文笔记。先重新生成统一数据，再生成本工作簿；手改工作簿不会回写 Markdown。');
note('A31:F32', '方法与边界：docs/METHOD.md；统计修正：analysis/statistical-corrections.md；后续工作：analysis/survey-gap-register.md。');
overview.getRange('B7:B18').setNumberFormat('0'); overview.getRange('F7:F18').setNumberFormat('0');
overview.getRange('B7:B12').format.font = { bold: true, size: 17, color: teal };
overview.getRange('F7:F12').format.font = { bold: true, size: 15, color: teal };
overview.getRange('C7:C19').format.font = { size: 10, color: gray };
wb.recalculate();
const got = overview.getRange('B7:B12').values.flat();
const expected = [122,62,60,48,59,18];
if (JSON.stringify(got) !== JSON.stringify(expected)) throw new Error(`Summary mismatch: ${JSON.stringify(got)}`);
// Verify the totals are live dependencies, then restore the source cell.
const original = entries.getRange('C2').values[0][0];
entries.getRange('C2').values = [['方法论文']]; wb.recalculate();
if (overview.getRange('F7').values[0][0] !== 51) throw new Error('COUNTIF dependency did not update');
entries.getRange('C2').values = [[original]]; wb.recalculate();
if (overview.getRange('F7').values[0][0] !== 52) throw new Error('COUNTIF restore failed');
console.log((await wb.inspect({ kind: 'region', sheetId: '调研概览', range: 'A6:F19', maxChars: 2000, tableMaxRows: 14, tableMaxCols: 6 })).ndjson);
// Explicit ranges prevent a huge render of the full horizontal comparison table.
const previews = [['调研概览','A1:F32','overview'],['条目分类','A1:F7','classification'],['评测协议','A1:D5','protocols'],['论文证据','A1:F5','sources']];
for (const [sheetName, range, name] of previews) {
  const preview = await wb.render({ sheetName, range, scale: 1.3, format: 'png' });
  await fs.writeFile(path.join(qaDir, `${name}.png`), new Uint8Array(await preview.arrayBuffer()));
}
const output = path.join(outDir, 'benchmark_survey.xlsx');
const xlsx = await SpreadsheetFile.exportXlsx(wb); await xlsx.save(output);
// Keep the library's inspection log with local QA previews, outside deliverables.
try {
  await fs.copyFile(output + '.inspect.ndjson', path.join(qaDir, 'workbook.inspect.ndjson'));
  await fs.unlink(output + '.inspect.ndjson');
} catch (err) { if (err.code !== 'ENOENT') throw err; }
const manifest = { generated_from_as_of: survey.as_of, engine: '@oai/artifact-tool',
  inputs: Object.fromEntries(inputPaths.map((p, i) => [p, sha(bytes[i])])),
  output_sha256: sha(await fs.readFile(output)), sheets: { '调研概览': 'formula summary', '条目分类': 122, '评测协议': 62, '论文证据': 199 },
  checked_summary_values: got, live_formula_dependency_check: 'passed', rendered_sheets: previews.map(p => p[0]) };
await fs.writeFile(path.join(outDir, 'benchmark_survey_workbook_manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
console.log(JSON.stringify({ output, rows: manifest.sheets, formulas: 'passed', previews: qaDir }));
