/** Chinese research review, grounded in the repository's 2026-11-03 snapshot. */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const tmp = path.join(root, '.survey_work/presentation');
const output = path.join(root, 'presentations');
const skill = 'D:/DevData/Codex/plugins/cache/openai-primary-runtime/presentations/26.1026.10807/skills/presentations';
const python = 'C:/Users/89447/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe';
process.env.RUNTIME_NODE_MODULES ??= 'C:/Users/89447/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const { applyPresentationChartFont, finalizePresentation } = await import(pathToFileURL(path.join(skill, 'container_tools/artifact_tool_utils.mjs')));
await fs.mkdir(tmp, { recursive: true }); await fs.mkdir(output, { recursive: true });
await fs.mkdir(path.join(tmp,'assets'),{recursive:true});
for(const [name,url] of Object.entries({
  'colosseum-real.png':'https://robot-colosseum.github.io/static/images/img_reproducibility_real_world.png',
  'libero-pipeline.png':'https://libero-safety.github.io/assets/images/pipeline.png'
})) {
  const target=path.join(tmp,'assets',name);
  if(!(await fs.stat(target).catch(()=>null))){
    const response=await fetch(url);if(!response.ok)throw new Error(`Asset unavailable: ${url}`);
    await fs.writeFile(target,new Uint8Array(await response.arrayBuffer()));
  }
}
const read = async p => JSON.parse(await fs.readFile(path.join(root, p), 'utf8'));
const survey = await read('data/benchmark_survey.json');
const sourceData = await read('data/benchmark_reading_sources.json');
const entries = new Map(survey.entries.map(e => [e.name, e]));
const sources = new Map(sourceData.entries.map(e => [e.benchmark, e]));
const stats = survey.statistics;
const active = survey.entries.filter(e => e.focus === 'active');
const types = { benchmark: '评测任务集', dataset: '训练数据集', platform: '仿真平台', framework: '评测框架', method: '方法论文' };
const C = { ink: '#142E30', green: '#087F72', rust: '#B94F36', slate: '#5C6C70', light: '#F1F6F5', white: '#FFFFFF', pale: '#DFECE8', gray: '#9AACAB' };
const FONT = 'Microsoft YaHei';
const p = Presentation.create({ slideSize: { width: 1440, height: 810 } });
p.theme.defaultFont = FONT;
const references = []; const tableOwners = new Set(); const chartOwners = new Set(); const outline = [];
function ref(name) {
  if (!references.includes(name)) references.push(name);
  return `R${String(references.indexOf(name) + 1).padStart(2, '0')}`;
}
function txt(s, text, x, y, w, h, size = 28, color = C.ink, bold = false, align = 'left') {
  const sh = s.shapes.add({ geometry: 'textbox', position: { left: x, top: y, width: w, height: h }, fill: 'none', line: { fill: 'none', width: 0 } });
  sh.text = String(text); sh.text.style = { typeface: FONT, fontSize: size, color, bold, alignment: align, verticalAlignment: 'top', insets: 0, autoFit: 'none', wrap: 'square' };
  return sh;
}
function slide(title, options = {}) {
  const s = p.slides.add(); s.background.fill = options.dark ? C.ink : C.white;
  const n = p.slides.items.length;
  txt(s, title, 70, 45, 1285, 88, 44, options.dark ? C.white : C.ink, true);
  if (options.sub) txt(s, options.sub, 72, 132, 1270, 48, 24, options.dark ? '#BAD2CB' : C.slate);
  txt(s, `${String(n).padStart(2, '0')}`, 1320, 756, 48, 28, 18, options.dark ? '#BAD2CB' : C.slate, false, 'right');
  outline.push({ number: n, title, sources: options.refs ?? [], note: options.note ?? '' });
  const refs = (options.refs ?? []).map(name => {
    const src = sources.get(name); const e = entries.get(name);
    if (!src) throw new Error(`Missing source: ${name}`);
    return `[${ref(name)}] ${src.metadata.authors.join(', ')}. ${src.metadata.title}. arXiv:${src.metadata.version}. ${src.fulltext_url}\n本库笔记：benchmarks/${e.document}\n论文结果：${e.summary.results}\n适用边界：${e.summary.limits}`;
  });
  s.speakerNotes.text = [options.note ?? '', '本汇报使用仓库 2026-11-03 快照。统计仅描述本库样本。',
    '数据：data/benchmark_survey.json；方法：docs/METHOD.md；阅读来源：data/benchmark_reading_sources.json。', ...refs].join('\n\n');
  if (refs.length) txt(s, `来源：${(options.refs ?? []).map(name => `[${ref(name)}] ${name}`).join('  ')}；详见备注`, 72, 750, 1228, 42, 16, options.dark ? '#BAD2CB' : C.slate);
  return s;
}
function note(s, text, y = 687, color = C.slate) { txt(s, text, 72, y, 1270, 56, 22, color); }
function para(s, heading, body, x, y, w, h = 126, num = null) {
  if (num !== null) txt(s, num, x, y - 4, 70, 68, 48, C.green, true);
  const dx = num !== null ? 90 : 0;
  txt(s, heading, x + dx, y, w - dx, 45, 30, C.ink, true);
  txt(s, body, x + dx, y + 48, w - dx, h - 48, 26, C.slate);
}
function table(s, headers, rows, widths, { x = 72, y = 190, h = 450, font = 25, padding = 12 } = {}) {
  const t = s.tables.add({ rows: rows.length + 1, columns: headers.length, left: x, top: y, width: widths.reduce((a,b)=>a+b,0), height: h, columnWidths: widths, values: [headers, ...rows] });
  t.styleOptions = { headerRow: false, bandedRows: false };
  t.borders.assign({ fill: '#D5E2DF', width: 0.7, style: 'solid' });
  t.cells.block({ row: 0, column: 0, rowCount: rows.length + 1, columnCount: headers.length }).assign({
    textStyle: { typeface: FONT, fontSize: font, color: C.ink }, margins: { top: padding + 1, right: 14, bottom: padding - 2, left: 14 }, anchor: 'center' });
  for (let r = 0; r <= rows.length; r++) {
    t.rows[r].height = r === 0 ? 52 : (h - 52) / rows.length;
    for (let c = 0; c < headers.length; c++) {
      const cell = t.getCell(r,c); cell.fill = r === 0 ? C.ink : r % 2 ? C.white : C.light;
      cell.text.style = { typeface: FONT, fontSize: r === 0 ? font : font, color: r === 0 ? C.white : C.ink, bold: r === 0, insets: padding, verticalAlignment: 'middle', autoFit: 'none' };
    }
  }
  tableOwners.add(p.slides.items.length); return t;
}
function bars(s, cats, values, { x = 72, y = 192, w = 820, h = 430, color = C.green, max, format = '0', horizontal = true } = {}) {
  const chart = s.charts.add('bar', {
    position: { left: x, top: y, width: w, height: h }, categories: cats,
    series: [{ name: '数量', values, fill: color }],
    barOptions: { direction: horizontal ? 'bar' : 'column', grouping: 'clustered', gapWidth: 72 }, hasLegend: false,
    xAxis: { visible: true, textStyle: { fontSize: 23, fill: C.ink }, line: { fill: '#CBD8D5', width: 1 }, majorGridlines: null },
    yAxis: { min: 0, ...(max ? { max, majorUnit: 10 } : {}), textStyle: { fontSize: 23, fill: C.slate }, numberFormatCode: format.includes('%') ? '0"%"' : format, majorGridlines: { fill: '#E1E8E6', width: 0.6 } },
    dataLabels: { showValue: true, position: 'outEnd', numberFormatCode: format, textStyle: { fontSize: 25, bold: true, fill: C.ink } },
    chartFill: 'none', chartLine: { fill: 'none', width: 0 }, plotAreaFill: 'none', plotAreaLine: { fill: 'none', width: 0 }
  });
  applyPresentationChartFont(chart, { fontFamily: FONT }); chartOwners.add(p.slides.items.length); return chart;
}
async function image(s, file, x, y, w, h, alt) {
  const b = await fs.readFile(path.join(tmp, 'assets', file));
  s.images.add({ blob: b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength), contentType: 'image/png', position: { left:x, top:y, width:w, height:h }, fit:'contain', alt });
}

// 1 — Cover.
{
  const s = p.slides.add(); s.background.fill = C.ink;
  txt(s, '具身智能及其安全\nBenchmark 调研', 76, 98, 790, 200, 64, C.white, true);
  txt(s, '已完成工作、技术比较与研究结论', 80, 340, 1120, 55, 32, '#C2DAD3');
  await image(s, 'colosseum-real.png', 712, 395, 655, 340, 'COLOSSEUM 官方真实测试台与扰动物体，作为具身评测场景示例');
  txt(s, '研究进展汇报\n2026 年 11 月 3 日', 80, 568, 550, 104, 28, '#C2DAD3');
  s.speakerNotes.text = '本汇报总结当前仓库已完成的调查、来源核查、重点章节精读、分类及数据统一。结论区分样本观察、论文结果与后续建议。封面图片为 COLOSSEUM 官方真实测试台，仅作场景示例，不表示本项目进行了机器人实验。图片来源：https://robot-colosseum.github.io/static/images/img_reproducibility_real_world.png，访问日期 2026-11-03。';
  outline.push({ number:1, title:'具身智能及其安全 Benchmark 调研', sources:[] });
}
// 2
{
  const s=slide('本次调研的主要结论', { sub:'结论来自已读样本与代表性论文，适用范围随证据一并保留' });
  para(s,'成功率无法单独刻画安全','过程违规、终态危险和物体损伤需要独立指标。',76,222,1250,115,'01');
  para(s,'可比性取决于协议和执行层级','问答、符号规划、仿真控制和真机实验回答不同问题。',76,385,1250,115,'02');
  para(s,'已有材料支持选型，采用与可运行性仍需补证','62 个重点条目已形成统一证据记录，后续优先核查资源与独立采用。',76,548,1250,130,'03');
  s.speakerNotes.text += '\n综合依据：SafeStage、ManiPhysicsBench、DESPITE 的结果详见第 13–15 页，证据状态和适用边界详见第 20–25 页。这里不推断全领域的频率或唯一性。';
}
// 3
{
  const s=slide('调研范围与当前规模',{sub:'条目、论文、任务与执行次数分别计量'});
  const nums=[['122','登记条目','保留全部历史索引'],['62','重点精读与分类','另有 60 项非重点档案'],['48','直接具身任务集','52 个任务集包含\n4 项软件代理任务集'],['199','书目记录','原始 193 条加补入 6 个来源']];
  nums.forEach((a,i)=>{const x=74+(i%2)*666,y=216+Math.floor(i/2)*222;txt(s,a[0],x,y,270,110,84,C.green,true);txt(s,a[1],x+235,y+19,390,48,31,C.ink,true);txt(s,a[2],x+235,y+75,390,97,24,C.slate);});
  note(s,'抽样偏向有公开入口的机械臂与 VLA 工作，尚不构成全领域系统综述。');
}
// 4
{
  const s=slide('已完成的调研工作',{sub:'每项整理都保留可追溯的输入、结果与边界'});
  table(s,['工作','具体完成内容','产出'],[
    ['来源核查','追溯提出论文，修正使用者与提出者混淆','25 项来源审计及逐篇版本记录'],
    ['项目入口核查','区分官方入口、平台入口、候选与未找到','122 项入口状态，60 项归档'],
    ['正文重点章节精读','整理问题、场景、实现、实验成果与限制','62 份笔记和条目文档'],
    ['分类与比较','分开成果类型、研究目标、接口、指标分母','统一 JSON、矩阵与四表 Excel'],
    ['统计校正','撤回不可靠推断，记录已知与未知','修正记录、方法说明及后续清单']
  ],[200,640,450],{h:464,font:25});
  note(s,'已读重点章节不等于审完所有附录，文档一致性校验也不等于实验复现。');
}
// 5
{
  const s=slide('主要成果类型的重新划分',{sub:'按本次所读论文的主要贡献互斥归类，分母为 62 项'});
  bars(s,['任务集','评测框架','训练数据','仿真平台','方法'],[52,4,3,2,1],{w:840,h:430,max:60});
  para(s,'边界案例','Open X-Embodiment：训练数据\nRoboCasa、CARLA：平台\nSTARS：表征学习方法',960,219,410,230);
  para(s,'具身关联另行标记','直接评测 51 项\n研究底座 6 项\n软件代理邻接研究 5 项',960,465,410,190);
  note(s,'52 个任务集包含 4 项软件代理。框架、数据和平台保留研究价值，但不混入任务集数量。');
}
// 6
{
  const s=slide('能力、鲁棒性与安全的判定',{sub:'目标允许多选，出现“语言”“接触”或“失败”不自动构成安全评测'});
  table(s,['目标','判断依据','样本数','典型关注点'],[
    ['能力','明确衡量任务完成、理解、迁移或组合','49','新物体、新环境、长任务、跨本体'],
    ['鲁棒性','明确施加扰动、故障或分布变化并比较','24','语言改写、视觉变化、动态事件'],
    ['安全','明确评估危险后果、禁止行为或风险处置','26','碰撞、损伤、危险计划、弃权和治理']
  ],[150,530,130,480],{h:351,font:27});
  para(s,'统计含义','三个数量来自同一批 62 项，彼此重叠，并包含底座与邻接研究。不能相加，也不能当作具身安全任务集数量。',76,578,1270,103);
}
// 7
{
  const s=slide('当前样本集中在机械臂操作',{sub:'应用场景标签可重叠，图中仅列选定分支的条目数'});
  bars(s,['机械臂操作','移动操作','自动驾驶','导航','人机交互','工业装配','全身控制','多机器人','无人机'],[33,6,5,2,2,2,1,1,1],{w:850,h:470,max:36});
  txt(s,'代表性仍需补查',984,220,350,90,35,C.green,true);
  txt(s,'少量样本只能说明本库覆盖较薄。\n\n不能据此断言相应领域缺少 benchmark。\n\n后续应同时补经典代表与近期工作。',984,325,355,300,27,C.ink);
  note(s,'场景与研究目标的共现只到条目层面，尚未逐任务证明联合实验覆盖。',701);
}
// 8
{
  const names=['LIBERO（基础套件）','RoboCasa','CARLA / CARLA Leaderboard','LIBERO-Para','STARS'];
  // CARLA's repository name is normalized below for source lookup.
  const carla=active.find(e=>e.name.startsWith('CARLA')).name; names[2]=carla;
  const s=slide('提出来源与后续使用关系的修正',{sub:'来源关系先于题名关键词判断',refs:names});
  table(s,['条目','修正后的认识','调研价值'],[
    ['LIBERO','原始来源为 2306.03310','保留终身学习目的与后续 VLA 协议差异'],
    ['RoboCasa','原始来源为 2406.02523','区分平台、后续任务集与 Shift 评测'],
    ['CARLA','原始来源为 1711.03938','区分仿真器和具体驾驶排行榜协议'],
    ['LIBERO-Para','2603.28301 为提出论文','IndustrialVLA-Bench 是后续使用者'],
    ['STARS','主要提出表征学习方法','使用已有基准，不计为新任务集']
  ],[210,500,580],{h:457,font:25});
  note(s,'来源审计 25 项，其中表内 18、表外 7。关系数与补入书目数属于不同计数单位。');
}
// 9
{
  const s=slide('项目入口与资源可用性',{sub:'62 个重点条目的入口状态沿用既有审计日期'});
  bars(s,['已确认项目入口','仅平台入口','候选待确认'],[47,12,3],{w:860,h:370,max:52});
  txt(s,'尚待逐项目验收',980,220,380,50,33,C.rust,true);
  txt(s,'评测代码与任务定义\n数据与仿真资产\n代码、数据及资产许可\n基线检查点与完整命令',980,300,380,235,28,C.ink);
  note(s,'另有 60 项未找到已确认入口，继续存档。入口存在不保证整个评测链可运行。',621);
}
// 10
{
  const s=slide('Benchmark 的实现链条',{sub:'共同结构是任务定义、环境执行、可观测记录和评分协议'});
  table(s,['环节','常见实现技术','需要核查的证据'],[
    ['任务与风险定义','BDDL／UBDDL、约束规则、语言模板','对象、初态、目标、禁止行为的具体定义'],
    ['场景与数据构建','资产随机化、关键姿态、运动规划','任务清单、种子、示范与测试集的边界'],
    ['策略执行','仿真 rollout、高层动作、真实机器人','接口、动作频率、动作分块、重置条件'],
    ['评分与诊断','状态谓词、确定性验证、力学求解器','成功、违规、损伤、恢复的分母与阈值'],
    ['比较与归因','对照、配对、重复、置信区间','模型／训练预算一致性及非确定性控制']
  ],[235,520,535],{h:460,font:25});
  note(s,'具体技术随条目变化，表中列的是本库观察到的实现方式，不表示每项都采用全部技术。');
}
// 11
{
  const s=slide('执行层级决定分数能解释什么',{refs:['ASIMOV Benchmark','DESPITE','SafeAgentBench','LIBERO-Safety','NAVSIM']});
  table(s,['层级','代表','直接测量','解释边界'],[
    ['静态情境判断','ASIMOV\nRoboAbstention','判断、弃权与人类标签一致性','无法单独验证动作安全'],
    ['符号规划','DESPITE','计划有效性与危险性','未执行机器人关节轨迹'],
    ['高层交互代理','SafeAgentBench','动作规划及环境结果','底层控制器承担部分能力'],
    ['仿真动作控制','LIBERO-Safety\nSafeStage','轨迹中的完成与违规','依赖仿真、状态和判分规则'],
    ['非反应式轨迹评测','NAVSIM','固定背景下规划综合表现','未覆盖其他交通参与者响应']
  ],[225,320,380,365],{h:470,font:24});
  note(s,'相同的“成功率”名称，不保证接口、任务难度和安全含义一致。');
}
// 12
{
  const s=slide('LIBERO-Safety：把风险写入任务约束',{refs:['LIBERO-Safety'],sub:'UBDDL 扩展任务描述，关键姿态与 CuRobo 支持示范生成'});
  await image(s,'libero-pipeline.png',70,201,715,438,'LIBERO-Safety 官方任务与数据生成示意，保留完整原图');
  txt(s,'5 套件 × 5 任务 × 3 难度',830,204,515,58,31,C.green,true);
  txt(s,'75 个测试配置\nAAG、HRI、TSA、FSHOA、SSR',830,277,500,95,29,C.ink);
  txt(s,'40 个训练任务\n19,664 条无碰撞示范',830,398,500,95,29,C.ink);
  txt(s,'逐步记录碰撞与场景风险\n同时查看成功和安全指标',830,525,500,95,27,C.ink);
  note(s,'训练示范数不能作为测试样本数。论文描述的生成组件仍需对照仓库验收。');
  s.speakerNotes.text+='\n图片来源：https://libero-safety.github.io/assets/images/pipeline.png（访问日期 2026-11-03）。图示来自官方项目。AAG 等英文缩写按原文保留，完整定义应结合原论文和实现核查。';
}
// 13
{
  const s=slide('SafeStage：成功轨迹也可能包含危险',{refs:['SafeStage'],sub:'97 个任务覆盖初始危险、执行风险和完成后的危险'});
  bars(s,['全部成功 SR','安全成功 SSR','不安全成功 USR'],[33.74,9.84,23.90],{w:860,h:340,max:40,format:'0.00"%"'});
  txt(s,'70.84%',1010,235,330,90,64,C.rust,true);
  txt(s,'成功轨迹中的\n不安全比例',1010,335,330,110,31,C.ink,true);
  table(s,['初始危险 ISH','执行风险 ETS','完成后危险 FSH'],[['27 个任务','40 个任务','30 个任务，完成后观察 5 秒']],[370,370,550],{y:576,h:103,font:23});
  note(s,'SR = SSR + USR。图中三项以全部 episode 为分母，右侧比例以成功 episode 为分母。',701);
}
// 14
{
  const s=slide('ManiPhysicsBench：任务完成与物体完好分开',{refs:['ManiPhysicsBench'],sub:'接触记录与外部力学求解器结合，判断抓握是否造成损伤'});
  bars(s,['任务完成 SR','无损完成 Safe SR'],[48.3,13.5],{w:780,h:325,max:60,format:'0.0"%"'});
  txt(s,'PR = 27.9%',930,223,410,80,47,C.rust,true);
  txt(s,'成功 episode 中\n物体保持完好的比例',930,315,410,110,29,C.ink);
  para(s,'实现重点','记录接触位置、方向和力，再结合几何、材料阈值判断损伤。\n91 个对象覆盖脆性断裂、软变形和薄壁变形。',76,555,1250,116);
  note(s,'数值为论文 SimplerEnv 高／中难对象的汇总。损伤是求解器事后判断，SR 为零时 PR 未定义。',701);
}
// 15
{
  const s=slide('语义安全：判断、计划与弃权分别评估',{refs:['ASIMOV Benchmark','DESPITE','RoboAbstention']});
  table(s,['条目','技术与问题','论文报告的发现','结论边界'],[
    ['ASIMOV','生成机器人准则\n比较情境与动作判断','人类判断一致率 84.3%','一致率不能替代闭环安全率'],
    ['DESPITE','形式化规划与确定性验证\n分开可行计划和危险计划','最强规划模型危险计划 28.3%\n无有效计划仅 0.4%','主结果使用 1,044 个困难任务\n不是全集的随机平均'],
    ['RoboAbstention','视觉接地与约束生成\n判断何时停止或澄清','论文最佳模型弃权率 39.0%\n6,069 条应弃权指令','静态图像任务\n尚不能说明正常请求误拒率']
  ],[220,350,370,350],{y:184,h:454,font:24});
  note(s,'本库综合判断：识别风险、提出可行计划和决定是否行动，是不同的评测对象。');
}
// 16
{
  const s=slide('鲁棒性：受控变化帮助定位失败来源',{refs:['LIBERO-Para','LIBERO-MAX','COLOSSEUM']});
  table(s,['条目','控制什么、改变什么','实现与规模','主要发现及限制'],[
    ['LIBERO-Para','初态和语义固定\n改变动作及对象表达','4,092 条改写\nPRIDE 与轨迹 DTW 诊断','7 种配置下降约 22–52 个百分点\n轨迹偏离只是内部规划的代理'],
    ['LIBERO-MAX','轨迹前缀、状态和种子固定\n执行中触发一次持续事件','8,000 对干净／变化轨迹\n配对检验与 bootstrap','14 种策略下降约 11–25.7 个百分点\n不代表连续真实扰动'],
    ['COLOSSEUM','任务目标固定\n改变视觉、几何和物理因素','RLBench 20 任务、14 扰动轴\n另有 4 项真实桌面任务','组合扰动可致至少 75% 相对退化\n相对退化不可改写为百分点']
  ],[230,360,340,360],{y:182,h:473,font:23});
  note(s,'完整比较应保留干净基线、变化条件和配对单位，避免只报告受扰动平均分。');
}
// 17
{
  const s=slide('长时程任务：阶段、恢复与交接状态',{refs:['RoboCasa-Shift','LIBERO-RECOVER','RoboComb']});
  table(s,['条目','诊断对象','证据与实现','适用边界'],[
    ['RoboCasa-Shift','首次失败发生在哪个阶段','固定种子配对并记录子目标\n零变化相机仍有 8/80 次结果翻转','1 个策略、筛出的 4 个任务\n扰动效应需与非确定性区分'],
    ['LIBERO-RECOVER','自身失败后能否继续完成','从 2,000 余仿真失败状态继续\n报告恢复成功、退化与一致性','自然失败来自仿真 rollout\n正常起点高分不保证恢复'],
    ['RoboComb','原子技能能否可靠衔接','分开调度、低层技能、交接状态\n已见组合 40%，未见重组 7.7%','训练设定与 oracle 条件须单列\n不能当作完全自主能力']
  ],[230,320,400,340],{y:183,h:469,font:24});
  note(s,'本库综合判断：总成功率应配合失败位置和状态分布，才足以支持改进方向。');
}
// 18
{
  const s=slide('能力评测底座的协议边界',{refs:['LIBERO（基础套件）','CALVIN','VLABench','RoboTwin']});
  table(s,['底座','核心问题与实现','比较时必须保留的条件'],[
    ['LIBERO','BDDL 任务定义与 robosuite／MuJoCo\n原版 130 任务，侧重迁移与遗忘','常见 40 任务协议只是后续特定组合\n原始 FWT、NBT、AUC 与平均 SR 有别'],
    ['CALVIN','4 环境、34 类操作\n从 play 数据学习连续语言指令','环境划分、指令链长度、历史窗口\n主要测能力，未显式覆盖全部危险'],
    ['VLABench','60 原子任务与 40 复合任务\n技能库、运动规划、语言扩增','未见类别与同类新实例分开\nVLM、模块化流程、VLA 接口分开'],
    ['RoboTwin','物体数字孪生与专家轨迹生成\n本次所读版本为 14 项双臂任务','版本、点云输入、示范量、真机微调\n不混用 RoboTwin 2.0 的规模']
  ],[210,530,550],{y:182,h:478,font:24});
}
// 19
{
  const carla=active.find(e=>e.name.startsWith('CARLA')).name;
  const s=slide('自动驾驶条目展示了不同的评测层级',{refs:[carla,'nuScenes','NAVSIM','SafeBench']});
  table(s,['条目','主要成果及技术','可回答的问题','主要边界'],[
    ['CARLA','交互驾驶仿真平台','构造环境并接入具体测试协议','平台本身不等于一套统一评分'],
    ['nuScenes','多模态真实数据及感知任务','感知性能与多传感器融合','感知分数不能代替驾驶安全'],
    ['NAVSIM','真实观测、非反应式轨迹展开\nPDMS 综合评分','比纯轨迹距离更丰富的规划评价','背景交通不响应自车行为'],
    ['SafeBench','CARLA 关键场景生成与统一评测\n安全、功能、礼仪三方面评分','比较正常与关键场景下的弱点','综合分不能直接解释为碰撞概率']
  ],[190,410,350,340],{y:185,h:457,font:24});
  note(s,'可迁移的经验是明确测量对象和接口，跨领域的分数不直接合并。');
}
// 20
{
  const s=slide('真机证据：确认 18 项，另有 32 项未知',{sub:'分母为 62 个已分类条目，按当前笔记能够确认的证据编码'});
  bars(s,['报告真实执行','模拟／真实配对','仅真实数据','仅实体测试件','尚未确认执行','不适用'],[15,3,6,1,32,5],{w:890,h:450,max:36});
  txt(s,'15 + 3 = 18',1000,223,380,75,48,C.green,true);
  txt(s,'已确认执行或\n配对验证的条目',1000,318,340,100,29,C.ink);
  txt(s,'未知保留为未知\n不估计全领域真机比例',1000,486,350,125,28,C.rust,true);
  note(s,'采集真实数据、提供机器人名称或实体测试件，都不足以单独认定已验证闭环策略安全。');
}
// 21
{
  const names=['nuScenes','CALVIN','LIBERO（基础套件）','Open X-Embodiment','NAVSIM'];
  const s=slide('引用量与实际采用是不同的证据',{sub:'OpenAlex 快照：59 个来源有观测，3 个来源未核验并留空'});
  table(s,['来源示例','被引观测','观测日期'],names.map(n=>[n,String(entries.get(n).citation.cited_by_count),entries.get(n).citation.snapshot_date]),[520,220,360],{x:72,y:194,h:360,font:26});
  txt(s,'这些数值对应已匹配的 Work 记录。版本拆分、收录延迟与来源年代都会影响可比性。',76,588,1270,75,27,C.ink);
  note(s,'LIBERO-Para、RoboCasa、CARLA 未核验。独立采用仍需逐篇检查实际运行、版本和作者关系。',697);
  s.speakerNotes.text+='\n引用来源：data/benchmark_citation_snapshot.json。示例不是影响力排名，不能相加成全网被引量。\n'+names.map(n=>`${n}: ${entries.get(n).citation.openalex_id}`).join('\n');
}
// 22
{
  const s=slide('旧统计结论的修正',{sub:'减少误判的关键是保留计数单位、未知状态和证据范围'});
  table(s,['撤回或收窄的表述','问题所在','当前处理'],[
    ['“122 个独立基准”','成果类型混杂，60 项本轮未分类','区分 122 个条目与 48 个直接具身任务集'],
    ['“终态仅 8 个、治理仅 24 个”','重复命中加总及标签叉乘无法证明实验覆盖','撤回数字与研究空白推断'],
    ['“规模中位数约 150”','问题、任务、条件、轨迹等单位混合','逐项保留评测单位和指标分母'],
    ['“零复用”“唯一覆盖多类”','不完整样本和摘要关键词不支持唯一性','实际采用与创新性另做定向检索']
  ],[380,440,470],{h:430,font:25});
  note(s,'已同步到首页、比较矩阵、覆盖分析和 ESB-2 提案。新基准的创新性仍待独立论证。');
}
// 23
{
  const s=slide('有证据支持的研究结论',{sub:'以下为本库综合判断，不是领域全量统计或唯一性声明'});
  table(s,['结论','代表证据','对评测设计的含义'],[
    ['完成与安全需要双轴报告','SafeStage、DESPITE\nManiPhysicsBench','同时呈现成功、违规、损伤及其条件分母'],
    ['受控变化提高归因能力','LIBERO-Para、LIBERO-MAX\nCOLOSSEUM','保留干净对照、共享状态和配对统计'],
    ['长任务需要过程诊断','RoboCasa-Shift、RoboComb\nLIBERO-RECOVER','记录首次失效、恢复起点和技能交接'],
    ['结论范围由接口决定','ASIMOV、DESPITE、NAVSIM 等','分开静态判断、规划、仿真与真实执行'],
    ['可用性与影响力需要独立核查','入口审计与引用快照的证据边界','逐项目验收资源，逐论文查真实采用']
  ],[370,450,470],{h:463,font:24});
}
// 24
{
  const s=slide('按研究问题选择互补基准',{sub:'初步选型建议，尚不承诺各项目都能直接安装运行'});
  table(s,['研究问题','建议优先阅读','互补核查'],[
    ['物理执行是否安全','LIBERO-Safety、SafeStage','ManiPhysicsBench 补物体损伤\n真实执行证据和评分器须单独核验'],
    ['扰动来自哪里，何时失效','LIBERO-Para、LIBERO-MAX\nCOLOSSEUM','RoboCasa-Shift 补长任务阶段诊断\n跨底座分数不直接比较'],
    ['失败后能否恢复\n技能能否衔接','LIBERO-RECOVER、RoboComb','CALVIN 等补长时程能力背景\n正常起点与失败起点分开'],
    ['计划是否危险\n何时应停止','DESPITE、ASIMOV\nRoboAbstention','SafeAgentBench 补交互执行\n软件代理安全仅作邻接参考']
  ],[310,470,510],{y:185,h:466,font:25});
  note(s,'先确定被测对象和执行接口，再检查任务、分母、资源及成本。');
}
// 25
{
  const s=slide('下一阶段的优先工作',{sub:'以补齐综述证据为主，是否开发新基准另行决策'});
  table(s,['优先级','任务','完成标准'],[
    ['P1','代表性补查','补导航、全身、人机、多机器人等薄弱分支\n保存检索式、纳入／排除理由与引文追溯'],
    ['P1','资源与独立采用审计','记录代码／数据／许可／评测器／基线版本\n区分仅提及、作者自用和独立运行'],
    ['P2','问题导向综述与选型','说明每组基准的适用对象、互补关系、成本和边界\n创新性主张另给检索证据'],
    ['按需','少数代表的最小复现','仅在结论依赖可运行性时执行\n保存命令、日志、结果及协议偏离']
  ],[150,350,790],{h:445,font:26});
  note(s,'60 项非重点档案继续保留。ESB-2 是未实现、未验证的可选设想。');
}
// 26 — Closing.
{
  const s=slide('结论',{dark:true});
  txt(s,'已建立可追溯的调研底稿',76,204,1240,65,43,'#9BDAC4',true);
  txt(s,'62 个重点条目完成分类与证据整理，其中 48 个是直接具身评测任务集。',80,288,1240,90,30,C.white);
  txt(s,'评测价值来自明确的问题与协议',76,410,1240,65,43,'#9BDAC4',true);
  txt(s,'安全需要过程与后果指标，可比性需要一致的接口、条件和分母。',80,494,1240,90,30,C.white);
  txt(s,'下一步优先补资源可用性、独立采用和领域代表性证据。',80,650,1240,60,30,'#C2DAD3');
}
// 27 — Artifact guide.
{
  const s=slide('附录：本轮形成的可复用资料',{sub:'机器可读数据、阅读证据和人工筛选入口相互连接'});
  table(s,['资料','用途','入口'],[
    ['四表 Excel','概览、条目分类、评测协议、论文证据','data/benchmark_survey.xlsx'],
    ['统一比较矩阵','技术、指标、对照、真机与来源横向对比','analysis/benchmark-comparison.md'],
    ['62 项精读报告','问题、场景、实现、论文结果及边界','analysis/benchmark-paper-deep-read.md'],
    ['统一数据与编码','更新分类、追溯来源、保留未知状态','data/benchmark_survey.json\nbenchmark_survey_annotations.json'],
    ['方法与缺口清单','统计口径、证据状态、后续验收要求','docs/METHOD.md\nanalysis/survey-gap-register.md']
  ],[220,490,580],{h:464,font:24});
  note(s,'原始 193 行数据和 60 份非重点档案保留，新比较结果使用统一数据。');
}
// 28–31 — Complete roster, 16 entries per page. No new reference numbering.
for (let start=0; start<active.length; start+=16) {
  const batch=active.slice(start,start+16);
  const s=slide(`附录：重点条目索引 ${Math.floor(start/16)+1}/4`,{sub:`本页为第 ${start+1}–${start+batch.length} 项，主要成果类型依据当前所读来源判定`});
  for (let side=0; side<2; side++) {
    const rows=batch.slice(side*8,side*8+8).map(e=>[e.name,types[e.primary_type]]);
    if(rows.length)table(s,['条目','主要成果'],rows,[450,170],{x:72+side*666,y:197,h:480,font:23,padding:8});
  }
  s.speakerNotes.text+='\n\n本页全部来源：\n'+batch.map(e=>`${e.name}\n${e.source.title}\n${e.source.fulltext_url}\n${e.type_reason}`).join('\n\n');
  note(s,'完整技术与指标见统一比较矩阵。索引包含底座、框架和邻接研究，不能把条目数都视作任务集。',700);
}
// Source bibliography for representative works used in the main slides.
const mainReferences=[...references];
for(let start=0;start<mainReferences.length;start+=8){
  const group=mainReferences.slice(start,start+8);
  const s=slide(`附录：主要参考文献 ${Math.floor(start/8)+1}/${Math.ceil(mainReferences.length/8)}`,{sub:'保留实际阅读的 arXiv 版本，完整作者与链接见各页备注'});
  let refY=194;
  group.forEach((name)=>{
    const src=sources.get(name);const id=ref(name);
    const words=src.metadata.title.split(' '); const lines=[];let line='';
    for(const word of words){if(line && (line+' '+word).length>110){lines.push(line);line=word;}else line += (line?' ':'')+word;}
    if(line)lines.push(line);
    const h=(lines.length+1)*25;
    txt(s,`[${id}]`,74,refY,80,h,21,C.green,true);
    const box=txt(s,`${lines.join('\n')}\narXiv:${src.metadata.version}`,160,refY,1198,h,20,C.ink);
    box.text.get(`arXiv:${src.metadata.version}`).link={uri:src.fulltext_url,isExternal:true};
    refY+=h+10;
  });
  s.speakerNotes.text+='\n\n'+group.map(name=>{
    const src=sources.get(name);return `[${ref(name)}] ${src.metadata.authors.join(', ')}. ${src.metadata.title}. arXiv:${src.metadata.version}. ${src.fulltext_url}`;
  }).join('\n\n');
}

// Keep a reproducible narrative and source map alongside the final presentation.
await fs.writeFile(path.join(tmp,'outline.json'),JSON.stringify(outline,null,2));
await fs.writeFile(path.join(tmp,'deck.json'),JSON.stringify(p.toProto()));
const candidate=path.join(tmp,'candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidate);
const renderOnly = process.env.SURVEY_RENDER_SLIDES ? new Set(process.env.SURVEY_RENDER_SLIDES.split(',').map(Number)) : null;
for(let i=0;i<p.slides.items.length;i++){
  if(renderOnly && !renderOnly.has(i+1))continue;
  const png=await p.export({slide:p.slides.items[i],format:'png',scale:1});
  await fs.writeFile(path.join(tmp,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
const finalPath=path.join(output,process.env.SURVEY_PPTX_NAME || '具身智能及安全Benchmark调研汇报_2026-11-03_完整版.pptx');
const receiptPath=path.join(tmp,`${path.basename(finalPath)}.validation.json`);
const result=await finalizePresentation({
  workspaceDir:root,candidatePath:candidate,finalPath,pythonExecutable:python,
  integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','13716000,7715250','--validate-bullet-geometry','--validate-heading-fit',...[...tableOwners].flatMap(n=>['--require-native-table-slide',String(n)])],
  requiredNativeTableOwnerSlides:[...tableOwners],requiredNativeChartOwnerSlides:[...chartOwners],
  materializeLiteralChartWorkbooks:true,fontPolicy:{basis:'design',families:[FONT]},
  verifyArtifactToolImport:true,receiptPath
});
console.log(JSON.stringify({slides:p.slides.items.length,finalPath,receipt:receiptPath,finalized:true}));
