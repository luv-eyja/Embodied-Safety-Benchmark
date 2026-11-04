# -*- coding: utf-8 -*-
"""Apply curated paper reviews without regenerating the historical archive.

Inputs are checked-in data; no network or parent-workspace registry is required.
Legacy fulltext evidence is retained separately from this key-section review.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

from build_benchmark_glossary import (load as load_glossary, load_names, names_in,
                                      tag_names, terms_in)

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '<!-- paper-review:start -->'
END = '<!-- paper-review:end -->'
PROJECT_BEGIN = '<!-- project-review:start -->'
PROJECT_END = '<!-- project-review:end -->'
USAGE_BEGIN = '<!-- usage-review:start -->'
USAGE_END = '<!-- usage-review:end -->'
GLOSSARY_BEGIN = '<!-- glossary:start -->'
GLOSSARY_END = '<!-- glossary:end -->'
PROJECT_STATUS = {'found': '已确认项目入口', 'platform_only': '仅平台入口',
                  'candidate': '候选待确认', 'not_found': '未找到已确认入口'}


def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))


def save(name, value):
    (ROOT / 'data' / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def cell(value):
    return re.sub(r'\s+', ' ', str(value or '')).replace('|', '／').strip()


def count_text(entry):
    oa = entry.get('openalex', {})
    if oa.get('status') == 'matched' and oa.get('cited_by_count') is not None:
        return f"[{oa['cited_by_count']}]({oa['id']})"
    return '未核验（查询失败／未匹配）'


def citation_note(entry):
    note = f"OpenAlex 被引次数：**{count_text(entry)}**；观测日期：{entry.get('observed_on', '未记录')}。"
    if entry.get('retained_prior_observation'):
        note += '后续查询受限，沿用同日较早、来源一致的快照；尚未确认预印本与正式版已合并。'
    elif entry['openalex']['status'] != 'matched':
        note += '本次未取得可核验计数，不按 0 处理。'
    else:
        note += '这是所链接论文记录的计数，不是 benchmark 使用次数。'
    return note


def reference(source):
    m = source['metadata']
    authors = m['authors']
    label = ', '.join(authors[:3]) + (', et al.' if len(authors) > 3 else '')
    venue = m.get('journal_ref') or 'arXiv preprint'
    note = (' ' + source['publication_note']) if source.get('publication_note') else ''
    return f"{label}, ‘{cell(m['title'])},’ {cell(venue)}, {m['published'][:4]}, arXiv:{m['version']}. [论文]({source['paper_url']})；[核查正文]({source['fulltext_url']})。" + note


def replace_section(text, number, body):
    # Preserve the existing mandated heading and replace its body only.
    pattern = rf'(?ms)(^## {number}\. [^\n]+\n).*?(?=^## \d+\. |\Z)'
    return re.sub(pattern, lambda m: m[1] + '\n' + body.strip() + '\n\n', text, count=1)


def row(text, label, value):
    pattern = rf'(?m)^\| {re.escape(label)} \|.*$'
    replacement = f'| {label} | {cell(value)} |'
    if re.search(pattern, text):
        return re.sub(pattern, lambda _: replacement, text)
    return re.sub(r'(?ms)(^## 0\. .*?)(?=^## 1\.)',
                  lambda m: m[1].rstrip() + '\n' + replacement + '\n\n', text, count=1)


def citing_line(entry):
    """One line about who cites this record; only claims what the two channels actually observed."""
    if not entry:
        return '**引文清单**：本轮未收集，见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。'
    cites = entry.get('cites') or {}
    arxiv = entry.get('arxiv') or {}
    if cites.get('total') is None:
        cited = '引文查询失败，未取得计数'
    elif cites.get('total') == 0:
        cited = '在 OpenAlex 引文图中暂无可列出的引文论文'
    else:
        cited = 'OpenAlex 引文图中有 **%d** 篇引文论文（清单保留被引最高的 %d 篇）' % (
            cites['total'], cites.get('listed', 0))
    if arxiv.get('status') == 'ambiguous':
        mention = 'arXiv 摘要检索因名称歧义不作计数'
    elif arxiv.get('verified'):
        mention = 'arXiv 摘要命中 %d 篇' % arxiv['verified']
    elif arxiv.get('status') == 'failed':
        mention = 'arXiv 摘要检索失败'
    else:
        mention = 'arXiv 摘要未见命中'
    return ('**引文清单**：%s；%s。两者来自不同更新流程、允许相差几条，均不等于独立采用或实际运行；'
            '清单与命中片段见[引文与摘要命中清单](../analysis/benchmark-citing-papers.md)。' % (cited, mention))


def project_doc_block(entry, reviewed_at):
    """Section 8: what the project source itself shows, plus the five review questions."""
    label = PROJECT_STATUS.get(entry.get('project_status'), entry.get('project_status') or '未记录')
    links = '；'.join(f'[{u}]({u})' for u in entry.get('project_urls') or [])
    lines = [PROJECT_BEGIN,
             '## 8. 项目源核查（%s，%s）' % (label, reviewed_at), '',
             '**项目入口**：' + (links or '—'), '']
    rows = []
    for s in entry.get('sources_checked') or []:
        bits = [b for b in (
            'stars %s' % s['stars'] if s.get('stars') is not None else '',
            'license %s' % s['license'] if s.get('license') else '',
            '最后推送 %s' % s['pushed_at'] if s.get('pushed_at') else '',
            '保留文本 %s 字符（截断）' % s['text_chars'] if s.get('text_chars') else '') if b]
        target = s.get('readme_url') or s.get('url')
        rows.append('| [%s](%s) | %s | %s |' % (cell(s.get('kind') or '页面'), s.get('url'),
                                               cell(target), '，'.join(bits) or '—'))
    if rows:
        lines += ['| 抓取对象 | 实际读取的地址 | 抓取时状态 |', '|---|---|---|'] + rows + ['']
    lines += ['**项目页显示**：' + cell(entry.get('project_facts')), '',
              '**涉及领域**：' + cell(entry.get('domain')), '',
              '**测试目的与构建方法**：' + cell(entry.get('purpose_build')), '',
              '**测试缺陷**：' + cell(entry.get('defects')), '',
              '**与具身智能安全的相关性**：' + cell(entry.get('safety_relevance')), '',
              '**用这个 benchmark 测了什么**：' + cell(entry.get('tested')), '',
              '**本轮核查边界**：' + cell(entry.get('limits_of_this_review')) + ' 本节只读项目页与 README 文本，未运行代码、未下载数据集。', '',
              PROJECT_END]
    return lines


def usage_doc_block(entry):
    """Section 9: what each citing paper tested, how it used the benchmark, and what it reported."""
    import re as _re

    def short(text, n):
        text = (text or '').strip()
        return text if len(text) <= n else text[:n].rstrip() + '…'

    lines = [USAGE_BEGIN, '## 9. 使用明细：谁在用什么、怎么用', '']
    records = (entry or {}).get('records') or []
    if not records:
        note = (entry or {}).get('noise_note') or '本轮没有可判读的使用记录。'
        lines += [note, '', USAGE_END]
        return lines
    lines += ['本轮判读 **%d 篇**论文：下表逐篇写被测模型、用法、评测范围与指标、报告结果；'
              '“摘要未给数值”表示摘要里确实没写数，不是没跑。每行下方的引用块是摘要原文片段，'
              '可据此复核判读是否过度。' % len(records), '',
              '| 论文（年份） | 被测模型 | 用法 | 评测范围与指标 | 报告结果 |', '|---|---|---|---|---|']
    for r in records:
        lines.append('| %s（%s） | %s | %s | %s | %s |' % (
            cell(short(r.get('paper'), 70)), cell(r.get('year')), cell(short(r.get('model'), 60)),
            cell(short(r.get('mode'), 40)), cell(short(r.get('setup'), 90)), cell(short(r.get('result'), 120))))
    lines += ['', '**原文片段（摘要）**：', '']
    for r in records:
        lines.append('- %s（%s，%s）：> %s' % (cell(short(r.get('paper'), 60)), cell(r.get('year')),
                                              cell(r.get('source')), cell(r.get('evidence'))))
    note = (entry or {}).get('noise_note')
    if note:
        lines += ['', '**口径提示**：' + note]
    lines += ['', USAGE_END]
    return lines


def glossary_doc_block(hits, name_hits=None):
    """Section 10: explain only the jargon this document actually uses, with its denominator."""
    lines = [GLOSSARY_BEGIN, '## 10. 术语说明（本文出现的词）', '']
    plain_names = [n for n in (name_hits or []) if not n.get('inline')]
    inline_names = [n for n in (name_hits or []) if n.get('inline')]
    if not hits and not name_hits:
        lines += ['本文没有命中词表里的术语；若仍有看不懂的词，见[全库术语表](../docs/GLOSSARY.md)。', '', GLOSSARY_END]
        return lines
    if hits:
        lines += ['正文出现的缩写与技术词按下表解释，共 %d 个。每个词都写清它除以什么、和哪些指标配套——'
                  '不同基准对同一缩写（尤其 SR）的定义并不相同。详细解释与常见误读见[全库术语表](../docs/GLOSSARY.md)。' % len(hits), '',
                  '| 术语 | 英文全称 | 中文 | 一句话解释 |', '|---|---|---|---|']
        for term in hits:
            lines.append('| **%s** | %s | %s | %s |' % (cell(term['term']), cell(term.get('en') or '—'),
                                                       cell(term.get('zh') or '—'), cell(term['short'])))
        pitfalls = [t for t in hits if t.get('pitfall')]
        if pitfalls:
            lines += ['', '**本文最容易读错的地方**：']
            for term in pitfalls:
                lines.append('- **%s**：%s' % (term['term'], cell(term['pitfall'])))
    if plain_names:
        lines += ['', '**本文出现的基准／数据集／仿真平台**（只标它是什么，不展开解释）：', '',
                  '| 名称 | 是什么 | 说明 |', '|---|---|---|']
        for item in plain_names:
            lines.append('| %s | %s | %s |' % (cell(item['name']), cell(item['kind']), cell(item.get('note') or '—')))
    if inline_names:
        lines += ['', '另有 %d 个专有名称已在正文首次出现处加括号标注类别（例如 %s），不再重复解释。'
                  % (len(inline_names), '、'.join('%s（%s）' % (n['name'], n['kind']) for n in inline_names[:6]))]
    lines += ['', GLOSSARY_END]
    return lines


def update_doc(card, review, source, cite, release, audit, citing=None, project=None, reviewed_at='', usage=None, glossary=None, names=None):
    path = ROOT / 'benchmarks' / card['document']
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'(?s)\n?' + re.escape(BEGIN) + '.*?' + re.escape(END) + r'\n?', '\n', text)
    text = re.sub(r'(?s)\n?' + re.escape(PROJECT_BEGIN) + '.*?' + re.escape(PROJECT_END) + r'\n?', '\n', text)
    text = re.sub(r'(?s)\n?' + re.escape(USAGE_BEGIN) + '.*?' + re.escape(USAGE_END) + r'\n?', '\n', text)
    text = re.sub(r'(?s)\n?' + re.escape(GLOSSARY_BEGIN) + '.*?' + re.escape(GLOSSARY_END) + r'\n?', '\n', text)
    # Reconstruct the table of historical papers with audited roles, keeping all titles.
    papers = ['下表为原调研表收录关系；它不是完整引文网络。外部补回的提出论文见第 7 节。', '',
              '| 论文 | 年份 | 与本条目的关系 | 原表评测线索 | 历史摘要记录 |', '|---|---|---|---|---|']
    for p in card['papers']:
        papers.append(f"| [{cell(p['title'])}]({p['link']}) | {p['year']} | {p['role']} | {cell(p['dimension'])} | {cell(p['summary'])} |")
    text = replace_section(text, 1, '**核心问题**：' + review['question'] + '\n\n**评测层级**：' + review['kind'] + '。')
    text = replace_section(text, 2, '**核心场景与条目**：' + review['scenarios'] + '\n\n**实现与判分**：' + review['implementation'])
    text = replace_section(text, 3, '\n'.join(papers))
    text = replace_section(text, 4, '**原论文结果与成果**：' + review['results'] + '\n\n**适用边界**：' + review['limits'])
    text = replace_section(text, 5, '\n'.join(f"- [{p['title']}]({p['link']})（{p['year']}；{p['role']}）" for p in card['papers']))
    # Preserve the legacy manually curated fulltext supplement, if one exists.
    old = re.search(r'(?ms)^### 6\.1 全文核查补录.*?(?=^### 6\.2|^本轮已核查|^## 7\.|\Z)', text)
    evidence = (old[0].strip() + '\n\n' if old else '')
    evidence += ('本轮已核查下列来源的研究问题、方法、评测与结果重点章节；未声称逐页审完全部附录，未运行原实验。'
                 '上方第 1–4 节使用本轮正文核查结果；历史摘要字段与早期全文补录仍须结合版本理解。\n\n'
                 + review['limits'])
    text = replace_section(text, 6, evidence)
    for label, value in {
        '首发/代表论文': source['metadata']['title'],
        '年份': source['metadata']['published'][:4] + '（所读来源首次 arXiv 提交年）',
        '被测对象': review['kind'], '规模线索': review['scenarios'],
        '执行环境线索': review['kind'], 'OpenAlex 引用快照': count_text(cite) + '；' + str(cite.get('observed_on')),
    }.items():
        text = row(text, label, value)
    if audit:
        text = row(text, '来源审计', f"[{source['metadata']['title']}]({source['paper_url']})；{audit['kind']}")
        text = row(text, '来源核验依据', audit.get('source_basis') or audit.get('basis') or '已核查原始来源。')
        if audit['kind'] == 'external_original_paper':
            text = row(text, '数据来源', '原表保留使用论文；本轮另读外部原始来源，见第 7 节')
    text = text.replace('| 关注属性 |', '| 历史关键词标签（未重新统计） |')
    if card['name'] == 'COLOSSEUM':
        text = row(text, '基础平台线索', 'RLBench / CoppeliaSim')
        text = row(text, '评测维度/指标', '20 个任务、14 条扰动轴；单轴和组合扰动成功率')
    if card['name'] in ('LIBERO-Para', 'LIBERO（基础套件）', 'RoboCasa', 'STARS'):
        text = row(text, '评测维度/指标', review['implementation'])
    self_count = sum(p['role'] == '提出' for p in card['papers'])
    text = re.sub(r'(?m)^> \*\*关联论文\*\*.*$',
                  f"> **关联论文**：本表 {len(card['papers'])} 篇（提出 {self_count}、使用 {card['user_count']}；方法参考另标）", text)
    text = re.sub(r'(?m)^> \*\*证据级别\*\*.*$',
                  '> **证据级别**：原表 ' + card['evidence']['code'] + '；另有 2026-11-03 原论文重点章节核查（第 1–4、7 节）', text)
    links = '；'.join(f'[{u}]({u})' for u in release.get('project_urls', []))
    text = re.sub(r'(?m)^> \*\*项目地址审计\*\*.*$',
                  f"> **项目地址审计**：`{release['status']}`；{links}", text)
    block = [BEGIN, '## 7. 原始来源、引用量与可复用成果（引用观测 %s）' % cite.get('observed_on', '未记录'), '',
             '**本次核查来源**：[1] ' + reference(source), '',
             '**重点核查位置（章节主题）**：' + '；'.join(review['sections']) + '。', '',
             citation_note(cite), '',
             '**项目与成果入口**：' + links + '。地址状态为 `' + release['status'] + '`；找到页面不等于已验证安装、数据下载和复现。', '',
             '**后续使用证据**：原表内有 ' + str(card['user_count']) + ' 篇标为使用的论文（见第 3、5 节）；这是本库收录下界，不能当全网使用量，也不能与被引数相加。', '',
             citing_line(citing), '',
             '完整比较及计数口径见[论文精读报告](../analysis/benchmark-paper-deep-read.md)；结构化笔记见[精读数据](../data/benchmark_paper_reviews.json)。', END]
    if card['name'] == 'LIBERO-Safety':
        block.insert(-1, '\n本仓库另有[LIBERO-Safety 实现拆解](../analysis/LIBERO-Safety-实现拆解.md)。')
    tail = '\n'.join(block)
    if project:
        tail += '\n\n' + '\n'.join(project_doc_block(project, reviewed_at))
    if usage is not None:
        tail += '\n\n' + '\n'.join(usage_doc_block(usage))
    body = text.rstrip() + '\n\n' + tail
    if names:
        body = tag_names(body, names)
    hits = terms_in(body, glossary) if glossary else []
    name_hits = names_in(body, names) if names else []
    if hits or name_hits:
        body = row(body, '术语说明',
                   '第 10 节解释本文出现的 %d 个缩写／技术词，并标出 %d 个专有名称的类别；全库词表见[术语表](../docs/GLOSSARY.md)'
                   % (len(hits), len(name_hits)))
    body += '\n\n' + '\n'.join(glossary_doc_block(hits, name_hits))
    path.write_text(body + '\n', encoding='utf-8')


def main():
    review_data = read('benchmark_paper_reviews.json')
    sources = {e['benchmark']: e for e in read('benchmark_reading_sources.json')['entries']}
    snapshot = read('benchmark_citation_snapshot.json')
    cites = {e['benchmark']: e for e in snapshot['entries']}
    audits = read('benchmark_source_audit.json')['entries']
    projects = {e['benchmark']: e for e in read('benchmark_project_audit.json')['audits']}
    payload = read('benchmark_cards.json')
    cards = {c['name']: c for c in payload['cards']}
    citing_path = ROOT / 'data/benchmark_citing_works.json'
    citing = ({e['benchmark']: e for e in json.loads(citing_path.read_text(encoding='utf-8'))['entries']}
              if citing_path.exists() else {})
    project_path = ROOT / 'data/benchmark_project_reviews.json'
    project_payload = (json.loads(project_path.read_text(encoding='utf-8')) if project_path.exists() else {})
    project = {e['benchmark']: e for e in project_payload.get('entries', [])}
    reviewed_at = project_payload.get('reviewed_at', '')
    usage_path = ROOT / 'data/benchmark_usage_records.json'
    usage = ({e['benchmark']: e for e in json.loads(usage_path.read_text(encoding='utf-8'))['entries']}
             if usage_path.exists() else {})
    glossary = load_glossary()
    names = load_names()
    reviews = review_data['entries']
    assert len(reviews) == len({r['benchmark'] for r in reviews}) == 62
    assert {r['benchmark'] for r in reviews} == {c['name'] for c in payload['cards'] if not c['document'].startswith('no-project/')}
    for r in reviews:
        name = r['benchmark']; c = cards[name]; s = sources[name]; e = cites[name]
        assert e['source_link'] == s['paper_url'], name
        a = audits.get(name, {})
        if a.get('exclusive_source'):
            for p in c['papers']:
                p['role'] = '提出' if p['title'] == a['source_title'] else '使用'
        if name == 'STARS':
            for p in c['papers']:
                p['role'] = '方法'
                p['summary'] = r['implementation'] + r['results']
        if name == 'COLOSSEUM':
            c['platform_hint'] = 'RLBench / CoppeliaSim'
            c['dimension'] = '20 个任务、14 条扰动轴；单轴和组合扰动成功率'
            for p in c['papers']:
                p['dimension'] = c['dimension']; p['summary'] = r['scenarios'] + r['results']
        c.update(primary_paper=s['metadata']['title'], source_link=s['paper_url'],
                 problem=r['question'], build=r['implementation'], finding=r['results'],
                 improve=r['limits'], scale_hint=r['scenarios'], execution_hint=r['kind'],
                 paper_review={**r, 'reviewed_at': review_data['reviewed_at'], 'paper_version':s['metadata']['version']})
        c['user_count'] = sum(p['role'] == '使用' for p in c['papers'])
        c['has_self_paper'] = any(p['role'] == '提出' for p in c['papers'])
        c['reuser_count'] = c['user_count'] if c['has_self_paper'] else 0
        if a: c['source_audit'] = a
        release = projects[name]
        c['project_audit'] = {k:release.get(k) for k in ('status','project_url','project_urls')}
        c['project_audit']['audit_date'] = release.get('verified_at', '2026-11-01')
        oa = e['openalex']
        c['citation_snapshot'] = {'source':'OpenAlex', 'snapshot_date':e.get('observed_on'),
                                 'paper':e['paper'], 'source_link':e['source_link'],
                                 'status':oa['status'], 'cited_by_count':oa.get('cited_by_count'),
                                 'openalex_id':oa.get('id'), 'retained_prior_observation':e.get('retained_prior_observation',False)}
        update_doc(c,r,s,e,release,a,citing.get(name),project.get(name),reviewed_at,usage.get(name),glossary,names)
    for c in payload['cards']:
        if c['document'].startswith('no-project/'):
            c.pop('citation_snapshot', None)
    payload['paper_review_count'] = len(reviews)
    save('benchmark_cards.json', payload)

    lines = ['# Benchmark 论文重点章节精读与引用快照', '',
             '> 核查日期：2026-11-03。范围为主目录的 **62 个条目、62 篇来源论文**；已归档的 60 个条目不纳入本轮重点阅读。STARS 经核查是方法论文，故 62 条不能直接称为 62 个新 benchmark。', '',
             '本轮阅读原论文的方法、任务构建、评测协议与结果重点章节，下面的数值均注明条件或分母；没有运行原实验，也不宣称逐页审完全部附录。每条笔记已同步到对应 benchmark 文档。', '',
             '## 阅读口径与来源修正', '',
             '- 将 LIBERO、RoboCasa、CARLA 的代表来源改回原始论文；CARLA 原论文与后来的 Leaderboard 协议分别理解。',
             '- 沿 IndustrialVLA-Bench 参考文献 [15] 找到 LIBERO-Para 独立提出论文及官方仓库；IndustrialVLA-Bench 改标使用者。',
             '- COLOSSEUM 修正为 RLBench／CoppeliaSim 上 20 个任务、14 条扰动轴；STARS 标为表征方法。',
             '- “成果”分为论文实验发现、发布的任务／数据／工具，以及本库后续使用证据；均不以引用数替代。', '',
             '## 引用量如何读', '',
             f"OpenAlex 当前保存 **{snapshot['matched_count']}/62** 个可核验来源的计数，观测日期 {snapshot['generated_at']}。限流或未匹配的查询不写入计数，也不按 0 处理。每个值链接到具体 Work 记录。", '',
             '0 仅表示该数据库记录在观测时计为零，不证明论文无人引用。预印本与正式版可能分开或合并收录；发现可靠正式版时优先展示，但本轮未穷尽版本，也不将多个记录相加。对于新论文，收录延迟尤其明显。', '',
             '被引次数不等于 benchmark 采用次数；同一论文可关联多个条目，因此本报告不计算“全部 benchmark 总引用量”。本库 193 条原始论文记录只是有限收录样本，使用关系也是下界。API 查询、错误、版本记录、观测日期保存在[引用快照](../data/benchmark_citation_snapshot.json)，计数含义参见 [OpenAlex Works](https://help.openalex.org/data/works/)。', '',
             '谁在引用这些 benchmark：逐条的引文清单、引文年份分布与“仅 arXiv 摘要命中”的候选见[引文清单报告](benchmark-citing-papers.md)。', '',
             '## 不同类型的评测应如何比较', '',
             '| 层级 | 典型条目 | 适合回答的问题 | 不能直接推出 |', '|---|---|---|---|',
             '| 闭环操作 | LIBERO-Safety、SafeStage、ManiPhysicsBench | 动作过程中是否违反约束／损伤对象 | 全部真实部署场景安全 |',
             '| 规划与规则验证 | DESPITE、HygieneRoboBench、IS-Bench | 计划是否可行、安全且符合顺序 | 机械臂一定执行成功 |',
             '| 图像／视频理解 | RoboChrono、RoboAbstention | 看到的状态是否理解正确、是否应弃权 | 闭环控制表现 |',
             '| 数据与平台 | Open X-Embodiment、AgiBot World、CARLA | 训练和可控评测的基础设施 | 一个统一安全排行榜 |',
             '| 软件代理邻接研究 | INFUSE、MemForm、ORBIT、SkillSafetyBench | 记忆、工具、权限与框架风险 | 物理碰撞／伤害率 |', '',
             '## 逐条索引', '', '| 条目 | 实际评测对象／性质 | OpenAlex 被引数 |', '|---|---|---:|']
    for r in reviews:
        c=cards[r['benchmark']]
        lines.append(f"| [{r['benchmark']}](../benchmarks/{c['document']}) | {r['kind']} | {count_text(cites[r['benchmark']])} |")
    lines += ['', '## 逐条阅读笔记', '']
    for i,r in enumerate(reviews,1):
        n=r['benchmark']; c=cards[n]; s=sources[n]; release=projects[n]
        lines += [f'### {i}. {n}', '', f"[原论文]({s['paper_url']}) · [正文]({s['fulltext_url']}) · [仓库卡片](../benchmarks/{c['document']})；性质：{r['kind']}。", '',
                  '**关心的问题**：'+r['question'], '', '**核心场景与条目**：'+r['scenarios'], '',
                  '**技术与实现**：'+r['implementation'], '', '**结果与成果**：'+r['results'], '',
                  '**边界**：'+r['limits'], '', citation_note(cites[n]), '',
                  '**复用入口**：'+'；'.join(f'[{u}]({u})' for u in release.get('project_urls',[])) + f"（`{release['status']}`）；本库使用论文 {c['user_count']} 篇。", '',
                  '**核查位置**：'+'；'.join(r['sections'])+f'。书目见 [{i}]。', '']
    lines += ['## 可复用的评测设计判断', '',
              '以下是本仓库据上述证据作出的综合判断，不是任何单篇论文的原话。', '',
              '- 闭环安全优先组合过程、终态和损伤指标：SafeStage、LIBERO-Safety 与 ManiPhysicsBench 分别补足不同缺口，不能只选总成功率。',
              '- 归因优先采用控制变量与配对：LIBERO-Para、Spa-Bench、LIBERO-MAX 可分别隔离措辞、空间理解和执行中变化；同时记录模拟非确定性。',
              '- 长时程失败需要看首次失效与交接状态：RoboCasa-Shift、LIBERO-RECOVER、RoboComb 的诊断可互补。',
              '- 规划基准必须保留执行层级：DESPITE、IS-Bench、HygieneRoboBench 可借鉴规则与独立评分；分数不应与关节控制任务直接平均。', '',
              '## 参考文献与证据记录', '',
              '以下按上文出现顺序给出来源论文（保留实际阅读的 arXiv 版本；无正式出版元数据时不猜测录用状态）。']
    for i,r in enumerate(reviews,1):
        lines += ['', f'[{i}] '+reference(sources[r['benchmark']])]
    lines += ['', '检索流程参考：T. Kassis et al., “Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents,” arXiv:2609.00065, 2026. [论文](https://arxiv.org/abs/2609.00065)。该文仅为所用 citation-management 工作流的归因，不是 benchmark 实验证据。', '',
              '结构化来源：[精读笔记](../data/benchmark_paper_reviews.json)、[全文版本与哈希](../data/benchmark_reading_sources.json)、[引用快照](../data/benchmark_citation_snapshot.json)。全文缓存仅供本地阅读，未纳入 Git。', '']
    (ROOT/'analysis/benchmark-paper-deep-read.md').write_text('\n'.join(lines),encoding='utf-8')
    # Keep the existing categorization/fulltext columns, updating only audited usage counts.
    p=ROOT/'benchmarks/README.md'; index=p.read_text(encoding='utf-8')
    for r in reviews:
        c=cards[r['benchmark']]
        index=re.sub(r'(?m)^\| '+re.escape(c['name'])+r' \| \d+ \| \d+ \|',
                     f"| {c['name']} | {c['paper_count']} | {c['user_count']} |",index)
    p.write_text(index,encoding='utf-8')
    print(f'Updated {len(reviews)} active documents, cards and paper report; archive untouched.')
    if (ROOT/'data/benchmark_survey_annotations.json').exists():
        from build_benchmark_survey import main as build_survey
        build_survey()


if __name__ == '__main__':
    main()
