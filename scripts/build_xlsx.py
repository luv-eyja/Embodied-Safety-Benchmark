# -*- coding: utf-8 -*-
"""Render the final workbook from docs/_rows.json."""
import json, os, math, re
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.table import Table, TableStyleInfo

BASE = r'D:\study\Embodied'
rows = json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))

# fix external links that were provisional
FIX = {
    'RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins':
        'https://doi.org/10.1109/CVPR52734.2025.02575',
    'VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning':
        'https://doi.org/10.1109/ICCV51701.2025.01037',
    'Jailbreaking LLM-Controlled Robots (RoboPAIR)':
        'https://doi.org/10.1109/ICRA55743.2025.11128119',
    'THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation':
        'https://arxiv.org/abs/2402.08191',
    'RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation':
        'https://arxiv.org/abs/2412.13877',
    'Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making':
        'https://doi.org/10.52202/079017-3188',
    'VestaBench: An Embodied Benchmark for Safe Long-Horizon Planning Under Multi-Constraint and Adversarial Settings':
        'https://doi.org/10.18653/v1/2025.emnlp-industry.149',
    'Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-to-End Autonomous Driving':
        'https://doi.org/10.52202/079017-0025',
    'NavSim: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking':
        'https://doi.org/10.52202/079017-0902',
}
for r in rows:
    if r['title'] in FIX:
        r['link'] = FIX[r['title']]

CAT_ORDER = ['VLA 安全 Benchmark', 'VLA 鲁棒性 Benchmark', 'VLA 能力 Benchmark',
             '攻防评测框架', '评测方法与度量', '具身智能体安全 Benchmark', '综述']
rows.sort(key=lambda r: (CAT_ORDER.index(r['cat']) if r['cat'] in CAT_ORDER else 99,
                         -int(r['year'] or 0), r['title']))

HEAD = ['序号', '论文标题（英文原文）', '中文题名 / 简称', '年份', '来源（期刊 / 会议 / 预印本）',
        '阅读状态', '收录来源', '论文库分区（layer › subcat）', '论文类别', '应用领域', '评测对象',
        '评测维度与关键指标', '内容概要', '链接']
WIDTH = [5, 52, 30, 6, 32, 8, 20, 22, 18, 12, 24, 36, 74, 36]
STATUS_COL = 6
NCOL = len(HEAD)
LAST = get_column_letter(NCOL)

wb = Workbook()

HFILL = PatternFill('solid', fgColor='1F3864')
HFONT = Font(color='FFFFFF', bold=True, size=10.5, name='Microsoft YaHei')
BFONT = Font(size=10, name='Microsoft YaHei')
LINKFONT = Font(size=9, name='Consolas', color='0563C1', underline='single')
THIN = Side(style='thin', color='D9D9D9')
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def cjk_len(s):
    s = str(s or '')
    return sum(2 if ord(c) > 0x2E80 else 1 for c in s)


def put(ws, r, c, v, font=BFONT, align=None, fill=None, link=False):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = font
    cell.alignment = align or Alignment(vertical='top', wrap_text=True)
    cell.border = BORDER
    if fill:
        cell.fill = fill
    if link and v:
        cell.hyperlink = v
        cell.font = LINKFONT
    return cell


# ---------------- Sheet 1: 说明 ----------------
ws0 = wb.active
ws0.title = '说明与筛选方法'
ws0.sheet_view.showGridLines = False
ws0.column_dimensions['A'].width = 118

n_lib = sum(1 for r in rows if r['src'].startswith('本论文库'))
n_ext = sum(1 for r in rows if r['src'] == '库外补充')
years = sorted({int(r['year']) for r in rows if r['year'] and str(r['year']).isdigit()})

intro = [
    ('title', '具身智能安全 · VLA 性能与安全能力 Benchmark 调研'),
    ('sub', '基于论文库 "Safety in Embodied AI"（Awesome-Embodied-AI-Safety）筛选，并补充库外代表性基准'),
    ('blank', ''),
    ('h', '一、交付物'),
    ('p', '本表共收录 %d 篇与「VLA 能力评测 / 安全评测」相关的论文，其中来自指定论文库 %d 篇、库外补充 %d 篇。'
          '每行给出英文原名、中文题名、来源（期刊/会议/arXiv）、阅读状态、论文库分类分区、评测对象、评测维度与指标，以及中文内容概要。' % (len(rows), n_lib, n_ext)),
    ('p', '库外补充的 %d 篇覆盖三类：（1）VLA 时代的评测新基准（VLA-Arena、SafeVLA-Bench、ForesightSafety-VLA、'
          'ManiGuard、RoboEval、RoboChrono、RoboVista、HUGE-Bench 等）；'
          '（2）用世界模型/仿真替代真机 rollout 的评测方法论（WorldEval、dWorldEval、RoboWorld、PolaRiS、主动因子评测）；'
          '（3）VLA 评测依赖的经典底座与安全基线（LIBERO、CALVIN、SimplerEnv、RoboCasa、RoboTwin、VLABench、'
          'COLOSSEUM、RoboMIND、ManiSkill2、AgiBot World、RoboPAIR、BadRobot）。' % n_ext),
    ('p', '年份分布：%s。' % '、'.join(str(y) for y in years)),
    ('p', '「阅读状态」列（F 列）可下拉选择：未读 / 在读 / 已读 / 略过；默认全部为「未读」，选中「已读」时单元格自动变绿。'),
    ('p', '筛选与排序已开好：点表头下拉即可按类别、年份、来源或阅读状态过滤，方便边读边勾。'),
    ('blank', ''),
    ('h', '二、论文库的构成（先说明数据来源，避免误读）'),
    ('p', '指定页面 screened.html 实际由三个层级的数据组成，本表已全部纳入检索，并在「收录来源」列逐条标出层级：'),
    ('p', '  1) curated（papers.json，594 篇）：作者人工筛选后的正式目录 → 本表标记「本论文库（人工精选目录）」。'),
    ('p', '  2) audited（audited.json，157 篇）：作者复核过作者与元数据的条目 → 「本论文库（作者复核）」。'),
    ('p', '  3) screened（screened.json，1882 篇）：机器自动筛出的每日 arXiv 增量，页面明确声明「未经人工审核、不代表收录」→ 「本论文库（自动筛查）」。'),
    ('p', '三级合计 2633 篇（同一标题只保留一条）。本表从中筛出 %d 篇与 VLA 评测直接相关的论文。' % n_lib),
    ('blank', ''),
    ('h', '三、筛选口径（什么算「针对 VLA 能力的评测」）'),
    ('p', '重要：筛选不要求标题或摘要里出现 benchmark / evaluation 这类词。'
          '诸如“Are VLA Models Robust to One-Step Observation Perturbations?”这种不含 benchmark 字样、'
          '但整篇都在评测 VLA 鲁棒性的论文同样收录。'),
    ('p', '纳入标准（满足其一即纳入）：'),
    ('p', '  A. 提出面向 VLA / 视觉-语言-条件策略的 benchmark、测试床、评测协议或度量体系；'),
    ('p', '  B. 对 VLA 的能力、鲁棒性、安全性做系统性实证评估（含诊断性研究与失败模式分析），'
          '即：即便没有提出新 benchmark，只要其贡献主体是「测出 VLA 在某方面如何失效/为何失效」，即纳入；'),
    ('p', '  C. 面向 VLA 所在技术栈（VLM 规划器 + 底层策略）的具身智能体安全基准，且其评测对象可对应到 VLA 的感知-规划-执行环节；'),
    ('p', '  D. 攻击/防御工作中自带统一评测框架或新基准（仅收录明确构建了评测协议者，纯粹的单点攻击方法不收）。'),
    ('p', '排除标准：'),
    ('p', '  × 与 VLA 评测无关的感知/建图/SLAM/纯自动驾驶规控论文；'),
    ('p', '  × 仅提出训练或对齐方法、不涉及评测协议的工作（如纯防御微调、纯加速推理）；'),
    ('p', '  × 纯语言/文本智能体、纯 web/移动端智能体的安全基准（与具身执行无关者）。'),
    ('blank', ''),
    ('h', '四、七个类别怎么读'),
    ('p', '  · VLA 安全 Benchmark：把「安全」本身作为评测目标，通常区分安全/不安全的孪生场景、分阶段风险或安全代价指标。'),
    ('p', '  · VLA 鲁棒性 Benchmark：以分布偏移（视角、光照、硬件、执行误差、任务中途变化）为自变量，主体指标仍是任务成功/安全成功。'),
    ('p', '  · VLA 能力 Benchmark：评测 VLA 的能力边界（泛化、空间接地、指令理解、长时程、容量下限），是安全评测的对照基线。'),
    ('p', '  · 攻防评测框架：对抗/后门/越狱类工作，但其贡献包含统一评测协议或新基准。'),
    ('p', '  · 评测方法与度量：不新建任务集，而是提出新的评测协议、度量或验证方法（如形式化区域验证、干预式评测、行为级度量）。'),
    ('p', '  · 具身智能体安全 Benchmark：评测对象是 VLM/LLM 规划器层面的具身智能体；与 VLA 共享「感知-规划-执行」链路，是 VLA 上层安全的主要来源。'),
    ('p', '  · 综述：梳理威胁分类与评测现状，可用于搭建调研框架。'),
    ('blank', ''),
    ('h', '五、来源标注规则（重要）'),
    ('p', '  · 论文库中已带会议/期刊信息的（NeurIPS / ICLR / ICCV / EMNLP / AAAI / IJCAI / RA-L），直接采用。'),
    ('p', '  · 其余多数是 arXiv 预印本，标注为「arXiv 预印本 (arXiv:ID)」——这本身就是准确信息，不代表漏标期刊。'),
    ('p', '  · 库外补充的 %d 篇，来源用 OpenAlex 与 arXiv 页面核对过，并给出 DOI 或 arXiv 编号；'
          '会议/期刊条目（RSS 2026、ICRA 2026、IROS 2025、CVPR 2025、ICCV 2025、NeurIPS、ICLR、AAAI、EMNLP、RA-L）均带正式 DOI。' % n_ext),
    ('p', '  · 表内 arXiv 编号逐条与 arXiv 摘要页标题做过比对：131 条链接中 125 条逐字一致；'
          '其余 6 条为 2 条 HTML 转义符差异（&amp;）、2 条已改用出版社 DOI（RoboTwin / VLABench）、'
          '1 条标题介词差异（RedVLA 的 of/for）、1 条 DOI 字符串被误当 arXiv 号，均不影响打开核验。'),
    ('blank', ''),
    ('h', '六、本表「未做」的事（请注意）'),
    ('p', '  1) 未精读全文：概要依据摘要与题目撰写，指标数字取自摘要自述，未逐一复核实验表格。'),
    ('p', '  2) 未做引用数/影响力排序：论文库未提供稳定的引用数据，本表按类别 + 年份排序。'),
    ('p', '  3) 未穷尽：论文库是每日增量 + 人工筛选，2026 年条目仍在快速增长；外网检索覆盖 OpenAlex 与 arXiv 的可检索面，'
          '仍可能漏掉未公开或仅在会议 proceedings 中的基准。'),
    ('p', '  4) 「评测维度与关键指标」列是对该文评测设计的概括，不是其全部实验设置。'),
    ('p', '  5) 攻击/后门/越狱类工作（28 篇）之所以收录，是因为它们本质上在度量 VLA 的安全能力边界，且多数自带评测协议；'
          '若只要纯 benchmark 与评测方法，可按「论文类别」列筛掉「攻防评测框架」。'),
    ('blank', ''),
    ('h', '七、建议的后续动作'),
    ('p', '  · 若要写综述：先用「综述」两篇定框架，再用「VLA 安全 Benchmark」+「评测方法与度量」两类做方法论对比表。'),
    ('p', '  · 若要选型做实验：LIBERO 系（Plus / Pro2.0 / RIG / VPro / MAX / RECOVER）已成体系，可直接复用其扰动轴；'
          '安全侧优先看 SafeStage、HazardArena、ForesightSafety-VLA、ManiGuard 的指标设计（安全代价、风险暴露时间、规约违反率）。'),
    ('p', '  · 若要补空白：现有基准普遍缺「实时性约束下的安全」（RT-Safe 之外很少）、缺「跨本体安全」（CrossSafe 类工作仍少）、'
          '缺「安全-有用性联合指标」（多数只报 ASR）。'),
    ('blank', ''),
    ('note', '数据抓取时间：2026-10-30；论文库源站：https://x-zheng16.github.io/Awesome-Embodied-AI-Safety/screened.html'),
]

r = 1
for kind, text in intro:
    c = ws0.cell(row=r, column=1, value=text)
    if kind == 'title':
        c.font = Font(size=18, bold=True, color='1F3864', name='Microsoft YaHei')
        ws0.row_dimensions[r].height = 34
    elif kind == 'sub':
        c.font = Font(size=10.5, color='595959', name='Microsoft YaHei')
        ws0.row_dimensions[r].height = 20
    elif kind == 'h':
        c.font = Font(size=12, bold=True, color='C00000', name='Microsoft YaHei')
        ws0.row_dimensions[r].height = 24
    elif kind == 'note':
        c.font = Font(size=9, italic=True, color='808080', name='Microsoft YaHei')
    else:
        c.font = Font(size=10, name='Microsoft YaHei')
    c.alignment = Alignment(vertical='top', wrap_text=True)
    if kind == 'p':
        ws0.row_dimensions[r].height = max(15, 15 * math.ceil(cjk_len(text) / 116))
    r += 1

# ---------------- Sheet 2: 总表 ----------------
ws = wb.create_sheet('VLA评测论文总表')
ws.sheet_view.showGridLines = False
for i, w in enumerate(WIDTH, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[1].height = 34
for i, h in enumerate(HEAD, start=1):
    c = ws.cell(row=1, column=i, value=h)
    c.fill = HFILL
    c.font = HFONT
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    c.border = BORDER

ALT = PatternFill('solid', fgColor='F2F5FA')
CENTER_COLS = {1, 4, STATUS_COL, 7, 10}
for idx, row in enumerate(rows, start=1):
    rr = idx + 1
    vals = [idx, row['title'], row['zh'], row['year'], row['venue'], '未读', row['src'],
            row['area'], row['cat'], row.get('domain') or '—', row['obj'], row['dim'],
            row['summ'], row['link']]
    fill = ALT if idx % 2 == 0 else None
    for j, v in enumerate(vals, start=1):
        put(ws, rr, j, v,
            align=Alignment(horizontal='center', vertical='top') if j in CENTER_COLS else None,
            fill=fill, link=(j == NCOL))
    # 估计行高
    lines = 1
    for j, v in enumerate(vals, start=1):
        if j in CENTER_COLS:
            continue
        lines = max(lines, math.ceil(cjk_len(v) / (WIDTH[j - 1] * 1.0)))
    ws.row_dimensions[rr].height = min(260, max(30, 14.5 * lines))

# 阅读状态：下拉可选 未读 / 在读 / 已读 / 略过
dv = DataValidation(type='list', formula1='"未读,在读,已读,略过"', allow_blank=True,
                    showDropDown=False, showErrorMessage=False)
dv.error = '请从下拉列表中选择'
dv.errorTitle = '阅读状态'
dv.prompt = '未读 / 在读 / 已读 / 略过'
dv.promptTitle = '阅读状态'
ws.add_data_validation(dv)
dv.add('%s2:%s%d' % (get_column_letter(STATUS_COL), get_column_letter(STATUS_COL), len(rows) + 1))

# 已读行浅绿底（条件格式，随下拉自动变色）
green = PatternFill('solid', fgColor='E2EFDA')
ws.conditional_formatting.add(
    '%s2:%s%d' % (get_column_letter(STATUS_COL), get_column_letter(STATUS_COL), len(rows) + 1),
    CellIsRule(operator='equal', formula=['"已读"'], fill=green))

ws.freeze_panes = 'C2'
ws.auto_filter.ref = 'A1:%s%d' % (LAST, len(rows) + 1)
ws.print_title_rows = '1:1'
ws.page_setup.orientation = 'landscape'
ws.page_setup.fitToWidth = 1
ws.sheet_properties.pageSetUpPr.fitToPage = True

# ---------------- Sheet 3: 分类统计 ----------------
ws2 = wb.create_sheet('分类统计')
ws2.sheet_view.showGridLines = False
ws2.column_dimensions['A'].width = 30
for col in 'BCDE':
    ws2.column_dimensions[col].width = 12

def block(start, title, pairs, head):
    ws2.cell(row=start, column=1, value=title).font = Font(size=11, bold=True, color='1F3864', name='Microsoft YaHei')
    for k, h in enumerate(head, start=1):
        c = ws2.cell(row=start + 1, column=k, value=h)
        c.fill = PatternFill('solid', fgColor='D9E2F3')
        c.font = Font(bold=True, size=10, name='Microsoft YaHei')
        c.border = BORDER
        c.alignment = Alignment(horizontal='center')
    for n, (k, v) in enumerate(pairs, start=1):
        for m, val in enumerate((k, v), start=1):
            c = ws2.cell(row=start + 1 + n, column=m, value=val)
            c.font = BFONT
            c.border = BORDER
            c.alignment = Alignment(vertical='center', wrap_text=True)
    return start + 2 + len(pairs) + 1

from collections import Counter
cat_c = Counter(x['cat'] for x in rows)
src_c = Counter(x['src'] for x in rows)
year_c = Counter(str(x['year']) for x in rows)
lib_c = Counter(x['area'] for x in rows if x['src'].startswith('本论文库'))

nxt = block(1, '一、按论文类别', [(k, cat_c[k]) for k in CAT_ORDER if cat_c[k]], ['类别', '篇数'])
nxt = block(nxt, '二、按收录来源', src_c.most_common(), ['来源（论文库层级）', '篇数'])
nxt = block(nxt, '三、按年份', sorted(year_c.items()), ['年份', '篇数'])
nxt = block(nxt, '四、阅读进度（在总表 F 列下拉勾选后，可自行统计）',
            [('未读', len(rows)), ('在读', 0), ('已读', 0), ('略过', 0)], ['状态', '篇数'])
nxt = block(nxt, '五、库内论文的论文库分区（Top 12）',
            [(k, v) for k, v in lib_c.most_common(12)], ['分区（layer › subcat）', '篇数'])

# ---------------- Sheet 4: 库外补充 ----------------
ws3 = wb.create_sheet('库外补充')
ws3.sheet_view.showGridLines = False
for i, w in enumerate(WIDTH, start=1):
    ws3.column_dimensions[get_column_letter(i)].width = w
ws3.row_dimensions[1].height = 34
for i, h in enumerate(HEAD, start=1):
    c = ws3.cell(row=1, column=i, value=h)
    c.fill = PatternFill('solid', fgColor='7B3F00')
    c.font = HFONT
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    c.border = BORDER
ext = [x for x in rows if x['src'] == '库外补充']
for idx, row in enumerate(ext, start=1):
    rr = idx + 1
    vals = [idx, row['title'], row['zh'], row['year'], row['venue'], '未读', row['src'],
            row['area'], row['cat'], row.get('domain') or '—', row['obj'], row['dim'],
            row['summ'], row['link']]
    for j, v in enumerate(vals, start=1):
        put(ws3, rr, j, v,
            align=Alignment(horizontal='center', vertical='top') if j in CENTER_COLS else None,
            link=(j == NCOL))
    lines = max(math.ceil(cjk_len(v) / (WIDTH[j - 1] * 1.0))
                for j, v in enumerate(vals, start=1) if j not in CENTER_COLS)
    ws3.row_dimensions[rr].height = min(260, max(30, 14.5 * lines))

dv3 = DataValidation(type='list', formula1='"未读,在读,已读,略过"', allow_blank=True,
                     showDropDown=False, showErrorMessage=False)
ws3.add_data_validation(dv3)
dv3.add('%s2:%s%d' % (get_column_letter(STATUS_COL), get_column_letter(STATUS_COL), len(ext) + 1))
ws3.freeze_panes = 'C2'
ws3.auto_filter.ref = 'A1:%s%d' % (LAST, len(ext) + 1)

wb.save(os.path.join(BASE, 'VLA_benchmark_survey.xlsx'))
print('saved', len(rows), 'rows;', n_lib, 'lib,', n_ext, 'ext')
