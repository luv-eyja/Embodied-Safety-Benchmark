# -*- coding: utf-8 -*-
"""Build the survey from explicit annotations, independently of legacy regex tags.

No network, parent-directory registry, or archived-paper rereading is required.
All counts refer to named entry sets, not to guessed coverage of the whole field.
"""
from __future__ import annotations
import collections
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-11-03'
TYPE = {'benchmark':'评测任务集','dataset':'训练数据集','platform':'仿真平台',
        'framework':'评测框架','method':'方法论文','unreviewed':'未分类'}
RELEVANCE = {'direct':'直接具身评测','support':'具身研究底座','adjacent':'软件代理邻接研究'}
OBJECTIVE = {'capability':'能力','robustness':'鲁棒性','safety':'安全'}
PROJECT = {'found':'已确认项目入口','platform_only':'仅平台入口','candidate':'候选待确认','not_found':'未找到已确认入口'}
SETTINGS = {'offline_image':'静态情境／图像','offline_video':'视频理解','offline_trace':'离线轨迹',
            'symbolic':'符号规划','simulation':'交互仿真','real_robot':'真实执行','real_dataset':'真实数据',
            'software':'软件环境','runtime':'运行时原型','physical_fixture':'实体测试件'}
REAL = {'execution_reported':'报告真实执行','paired_validation':'模拟／真实配对验证',
        'data_only':'真实数据，不据此认定执行','fixture_only':'仅确认实体测试件',
        'unknown':'尚未确认执行实验','not_applicable':'不适用'}
SURVEY_BEGIN = '<!-- survey-classification:start -->'
SURVEY_END = '<!-- survey-classification:end -->'


def read(file):
    return json.loads((ROOT/'data'/file).read_text(encoding='utf-8'))


def save(file, obj):
    (ROOT/file).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def md(file, lines):
    (ROOT/file).write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')


def cell(value):
    return re.sub(r'\s+', ' ', str(value or '')).replace('|','／').strip()


def labels(values, mapping):
    return '、'.join(mapping.get(v,v) for v in values)


def citation(entry):
    c=entry.get('citation') or {}; n=c.get('cited_by_count')
    return f"[{n}]({c['openalex_id']})" if n is not None and c.get('openalex_id') else '未核验'


def link(entry, prefix='../benchmarks/'):
    return f"[{entry['name']}]({prefix}{entry['document']})"


def norm(title):
    return re.sub(r'[^a-z0-9]', '', title.lower().replace('(simplerenv)',''))


def paper_registry(rows, sources, cards):
    """Preserve raw rows and join reviewed papers by observed title/link aliases."""
    papers=[]; by_key={}
    def keys(title, url):
        out={'title:'+norm(title)}
        if url:
            arxiv=re.search(r'arxiv.org/(?:abs|html)/(\d{4}\.\d{4,5})',url)
            out.add('arxiv:'+arxiv[1] if arxiv else 'url:'+url.lower().rstrip('/'))
        return out
    for i,r in enumerate(rows,1):
        p={'paper_id':f'P{i:04d}','title':r['title'],'url':r['link'],'raw_row_indices':[i],
           'in_original_table':True,'reviewed_benchmarks':[], 'reviewed_source':None}
        papers.append(p)
        for k in keys(r['title'],r['link']):by_key[k]=p
    for s in sources:
        meta=s['metadata']; aliases=keys(meta['title'],s['paper_url'])|keys(s['paper'],s['paper_url'])
        # Existing card linkage supplies documented DOI aliases, never fuzzy matching.
        for p in cards[s['benchmark']]['papers']:
            if norm(p['title']) in {norm(s['paper']),norm(meta['title'])}:
                aliases |= keys(p['title'],p['link'])
        matches={by_key[k]['paper_id']:by_key[k] for k in aliases if k in by_key}
        assert len(matches)<=1, (s['benchmark'], list(matches))
        if matches:p=next(iter(matches.values()))
        else:
            p={'paper_id':f'P{len(papers)+1:04d}','title':meta['title'],'url':s['paper_url'],
               'raw_row_indices':[],'in_original_table':False,'reviewed_benchmarks':[],'reviewed_source':None}
            papers.append(p)
        p['reviewed_benchmarks'].append(s['benchmark'])
        p['reviewed_source']={'title':meta['title'],'url':s['paper_url'],'fulltext_url':s['fulltext_url'],
                              'authors':meta['authors'],'version':meta['version'],
                              'first_submitted':meta['published'],'journal_ref':meta.get('journal_ref'),
                              'publication_note':s.get('publication_note'), 'reading_status':'重点章节核查'}
        for k in aliases:by_key[k]=p
    return {'schema_version':1,'as_of':DATE,'raw_row_count':len(rows),'paper_count':len(papers),
            'supplement_count':sum(not p['in_original_table'] for p in papers),
            'deduplication':'原表保留不改写；补充来源按确切标题／arXiv／已知 DOI 别名连接，不按相似题名合并。',
            'papers':papers}


def build_data():
    annotation=read('benchmark_survey_annotations.json')
    ann={a['name']:a for a in annotation['entries']}
    payload=read('benchmark_cards.json'); cards={c['name']:c for c in payload['cards']}
    sources=read('benchmark_reading_sources.json')['entries']; src={s['benchmark']:s for s in sources}
    reviews={r['benchmark']:r for r in read('benchmark_paper_reviews.json')['entries']}
    assert set(ann)=={c['name'] for c in cards.values() if not c['document'].startswith('no-project/')}
    entries=[]
    for c in cards.values():
        name=c['name']; a=ann.get(name); active=a is not None
        identity='ESB-'+hashlib.sha256(name.encode('utf-8')).hexdigest()[:10]
        e={'entry_id':identity,'name':name,'document':c['document'],
           'focus':'active' if active else 'archived',
           'classification_status':'reviewed' if active else 'not_reviewed',
           'legacy_category':c['tier'], 'primary_type':'unreviewed',
           'relevance':None,'objectives':[],'domains':[],'settings':[], 'real_evidence':None,
           'unit':None,'metrics':[],'control':None,'statistics':None,'type_reason':None,
           'source':None,'citation':c.get('citation_snapshot') if active else None,
           'resources':{'entry_status':c['project_audit']['status'],
                        'urls':c['project_audit'].get('project_urls',[]),
                        'link_checked_at':c['project_audit'].get('audit_date'),
                        'code_data_license_baseline_audit':'not_audited',
                        'execution_reproduction':'not_performed'},
           'usage':{'associated_use_papers':sum(p['role']=='使用' for p in c['papers']),
                    'scope':'原表中的使用关联，不是经过独立全文核验的采用量',
                    'independent_reuse_audit':'not_audited'},
           'evidence':{'level':'key_sections' if active else 'historical_only',
                       'classification_basis':None, 'reviewed_at':DATE if active else None}}
        if active:
            e.update({k:v for k,v in a.items() if k!='name'})
            s=src[name]; r=reviews[name]
            e['source']={'title':s['metadata']['title'],'url':s['paper_url'],
                         'fulltext_url':s['fulltext_url'],'version':s['metadata']['version'],
                         'year':int(s['metadata']['published'][:4])}
            e['evidence']['classification_basis']={'note_file':'data/benchmark_paper_reviews.json',
                                                   'sections':r['sections']}
            e['summary']={k:r[k] for k in ('question','scenarios','implementation','results','limits')}
        entries.append(e)
        c['survey']={k:e[k] for k in ('entry_id','focus','classification_status','primary_type','relevance','objectives','domains','settings','real_evidence')}
        c['survey']['source']='data/benchmark_survey.json'
    active=[e for e in entries if e['focus']=='active']
    counts={k:dict(collections.Counter(e[k] for e in active)) for k in ('primary_type','relevance','real_evidence')}
    stats={'inventory_entries':len(entries),'classified_active_entries':len(active),
           'archived_unclassified_entries':len(entries)-len(active),
           'counts_among_classified':counts,
           'direct_embodied_tasksets':sum(e['primary_type']=='benchmark' and e['relevance']=='direct' for e in active),
           'objective_counts':dict(collections.Counter(v for e in active for v in e['objectives'])),
           'source_years':dict(sorted(collections.Counter(e['source']['year'] for e in active).items())),
           'project_entry_status':dict(collections.Counter(e['resources']['entry_status'] for e in active)),
           'citation_observations':sum((e['citation'] or {}).get('cited_by_count') is not None for e in active),
           'real_execution_confirmed_entries':sum(e['real_evidence'] in ('execution_reported','paired_validation') for e in active),
           'note':'按条目去重统计；多选目标／场景之间有重叠。未知不等于否定；统计仅描述本库样本。'}
    domain_cells=[]
    for domain in sorted({d for e in active for d in e['domains']}):
        names=[e['name'] for e in active if domain in e['domains']]
        objective_members={o:[e['name'] for e in active if domain in e['domains'] and o in e['objectives']] for o in OBJECTIVE}
        domain_cells.append({'domain':domain,'entries':names,'objective_members':objective_members})
    survey={'schema_version':1,'as_of':DATE,'classification_method':annotation['method'],
            'vocabulary':annotation['vocabulary'],'statistics':stats,'coverage_semantics':'entry_label_cooccurrence_not_task_level_evidence','domain_coverage':domain_cells,'entries':entries}
    save('data/benchmark_survey.json',survey); save('data/benchmark_cards.json',payload)
    registry=paper_registry(read('rows.json'),sources,cards)
    save('data/survey_paper_registry.json',registry)
    return survey,registry


def outputs(survey,registry):
    active=[e for e in survey['entries'] if e['focus']=='active']; stats=survey['statistics']; counts=stats['counts_among_classified']
    base=['# 具身智能与安全 Benchmark 调研比较矩阵','',
          f"> 整理日期：{DATE}。本库登记 {stats['inventory_entries']} 个调研条目，其中 62 个已依据正文笔记分类，60 个非重点条目未重新分类。它们不是 122 个同质的独立 benchmark。",'',
          '## 1. 范围与计数单位','',
          '本表用于比较评测目的、任务接口、构建方式和证据边界，不对不同论文的原始分数作跨基准排名。主要成果类型由整理者按本文贡献编码；同一工作可以发布多种成果，但主要类型只计一次。条目名含多个版本时，保留一个索引入口，明确本次所读版本。','',
          '| 主要成果类型 | 已分类条目数（分母 62） | 含义 |','|---|---:|---|']
    for t in TYPE:
        if t!='unreviewed':base.append(f"| {TYPE[t]} | {counts['primary_type'].get(t,0)} | {cell(survey['vocabulary']['primary_type'][t])} |")
    base += ['',f"其中直接具身评测任务集为 **{stats['direct_embodied_tasksets']}** 条；其余评测任务集属于软件代理邻接研究。这个数字不包含未分类档案，也不表示领域总体规模。",'',
             '研究目标可多选：能力＝完成／理解／迁移；鲁棒性＝明确的扰动或失败条件；安全＝显式风险、禁止行为、后果或治理。语言理解错误不自动标为语义安全，接触操作不自动标为物理安全。','',
             '## 2. 类型、任务与执行接口','',
             '| 条目 | 主要类型／关联 | 研究目标 | 应用场景 | 观察或执行环境 |','|---|---|---|---|---|']
    for e in active:
        base.append(f"| {link(e)} | {TYPE[e['primary_type']]}／{RELEVANCE[e['relevance']]} | {labels(e['objectives'],OBJECTIVE)} | {'、'.join(e['domains'])} | {labels(e['settings'],SETTINGS)} |")
    base += ['', '## 3. 评测单元与指标分母','',
             '任务数、配置数、轨迹数、帧数、问题数、重复次数分别保留，不计算跨单位的“规模中位数”。SR、PR 等缩写可能同名异义；应先比较定义与分母。','',
             '| 条目 | 评测单元 | 指标定义与分母 |','|---|---|---|']
    for e in active:
        metrics='<br>'.join(f"{m[0]}：{m[1]}；分母／统计单位：{m[2]}" for m in e['metrics'])
        base.append(f"| {link(e)} | {e['unit']} | {cell(metrics)} |")
    base += ['', '## 4. 协议、证据与资源状态','',
             '真实数据采集、真实策略执行、模拟／真实配对验证分别标记。未知只表示当前笔记未充分核验。项目入口确认不等于代码、数据、许可证、评测器和基线已全部可用。','',
             '| 条目 | 对照与划分 | 重复／统计及边界 | 真机证据 | 项目入口状态 |','|---|---|---|---|---|']
    for e in active:
        base.append(f"| {link(e)} | {e['control']} | {e['statistics']} | {REAL[e['real_evidence']]} | {PROJECT[e['resources']['entry_status']]} |")
    base += ['', '## 5. 来源与影响力','',
             '引用计数沿用已核验日期的 OpenAlex 记录；不合并版本计数，不对全库求和。原表使用关系是候选采用证据，未完成逐篇独立复用审计。完整方法与结果见[精读报告](benchmark-paper-deep-read.md)。','',
             '| 条目 | 本次阅读的原始来源 | 被引次数 | 观测日期 | 原表使用关联数 |','|---|---|---:|---|---:|']
    for e in active:
        s=e['source']; c=e['citation'] or {}
        observed = c.get('snapshot_date') if c.get('cited_by_count') is not None else '未核验'
        base.append(f"| {link(e)} | [{cell(s['title'])}]({s['url']})（{s['version']}） | {citation(e)} | {observed or '未核验'} | {e['usage']['associated_use_papers']} |")
    base += ['', '## 6. 数据与尚未完成的核查','',
             f"[统一调研数据](../data/benchmark_survey.json)含 122 条，分类依据保存在[人工编码](../data/benchmark_survey_annotations.json)。[论文证据目录](../data/survey_paper_registry.json)连接原表 {registry['raw_row_count']} 条记录与 {registry['supplement_count']} 篇补入的已读原始来源，共 {registry['paper_count']} 个书目记录。原始论文 Excel 保留为历史快照，当前比较以新增统一调研工作簿为准。",'',
             '未完成的工作已列入[覆盖与证据缺口](survey-gap-register.md)。本轮没有穷尽全部领域、没有独立复现实验，也没有逐项目验收代码／数据／许可证。60 个无已确认项目入口的非重点条目继续存档。','']
    md('analysis/benchmark-comparison.md',base)

    cover=['# 已分类条目的场景与研究目标共现','',
           '> 本轮覆盖矩阵仅统计 62 个已分类条目；60 个档案未知。每个格子按条目名去重，格子的成员列表保存在 data/benchmark_survey.json。','',
           '## 统计口径','',
           '- 主要成果类型、具身关联和研究目标由正文笔记人工编码；不是关键词扫描。',
           '- 同一条目可属于多个应用场景和目标，因此行列之间不可直接相加当独立条目总数。',
           '- 单元格只表示条目同时具有两类标签；尚未逐任务验证该目标在每一种场景上的实验，不作为联合任务覆盖证明。',
           '- 这里的空格或零代表本轮样本没有编码到相应条目，不代表领域不存在工作。',
           '- 原有“环节×安全属性”把独立标签作笛卡尔积，无法证明某属性在该环节被实际评测；本轮撤回这种缺口推断。','',
           '## 场景标签 × 目标标签（62 个已分类条目的共现）','',
           '| 应用场景 | 能力 | 鲁棒性 | 安全 | 本场景去重条目数 |','|---|---:|---:|---:|---:|']
    for d in survey['domain_coverage']:
        cover.append('| '+d['domain']+' | '+' | '.join(str(len(d['objective_members'][o])) for o in OBJECTIVE)+f" | {len(d['entries'])} |")
    cover += ['', '## 成员与证据','']
    by={e['name']:e for e in active}
    for d in survey['domain_coverage']:
        cover += ['- **'+d['domain']+'**：'+'、'.join(link(by[n]) for n in d['entries'])+'。']
    cover += ['', '## 解释边界','',
              '多机器人治理原型与多机器人实体控制不同；UAV 离线决策题也不同于飞行闭环。导航包含在综合基准中，不证明存在足够独立导航评测覆盖。选型时还应按比较矩阵的执行环境和主要类型筛选。', '',
              'ESB-2 是可选设计提案；本矩阵不证明其创新性、必要性或“唯一覆盖空白”。参见[统计修正记录](../analysis/statistical-corrections.md)。']
    md('design/coverage-matrix.md',cover)
    save('data/survey_coverage.json',{'as_of':DATE,'denominator':len(active),'unknown_entries':60,'cells':survey['domain_coverage']})

    common=['# 当前调研样本的结构与证据','',
            '> 2026-11-03 修订。下列统计只描述本库已核查样本，撤回从关键词命中推断领域占比、唯一性与创新空白的旧结论。','',
            '## 1. 登记对象与范围','',
            f"122 个是登记条目数。62 个已分类对象中，"+'、'.join(f"{TYPE[t]} {n} 个" for t,n in counts['primary_type'].items())+'；另有 60 个档案尚未分类。', '',
            '## 2. 来源年代与抽样偏向','',
            '| 来源首次 arXiv 提交年 | 条目数（分母 62） |','|---|---:|']
    common += [f'| {year} | {n} |' for year,n in stats['source_years'].items()]
    common += ['', '年代以本次阅读来源的 arXiv 首次提交为准，不等同正式发表年或整个 benchmark 家族起始年。近期来源偏多，当前材料不能代表领域历史分布。', '',
               '## 3. 真实验证与真实数据','', '| 证据状态 | 条目数（分母 62） |','|---|---:|']
    common += [f'| {REAL[k]} | {v} |' for k,v in counts['real_evidence'].items()]
    common += ['', f"当前笔记确认 {stats['real_execution_confirmed_entries']} 个条目报告真实执行或模拟／真实配对验证；{counts['real_evidence'].get('unknown',0)} 个尚未充分确认，因此不估计整个领域的真机验证比例。数据采集不是闭环验证，实体测试件也不是成功率实验。", '',
               '## 4. 引用、使用与资源','',
               f"{stats['citation_observations']} 个来源有已核验的引用计数；这不是 {stats['citation_observations']} 个基准被独立采用的证据。标题／摘要检出的使用关系不能证明复用率接近零。需要检查后续论文的实验协议、版本和团队独立性。", '',
               '重点条目的项目入口状态为：'+'、'.join(f"{PROJECT[k]} {v}" for k,v in stats['project_entry_status'].items())+'。该状态不替代代码、数据、评测器、许可证和基线的验收。','',
               '## 5. 可支持的综合观察','',
               '1. **安全与完成应分开报告。** SafeStage、DESPITE、ManiPhysicsBench 的核查结果分别揭示过程违规、规划危险、物体损伤；不能把三种不同指标直接平均。',
               '2. **控制变量有助于归因。** LIBERO-Para、Spa-Bench 和 LIBERO-MAX 分别控制措辞、空间描述和执行中事件；它们支持具体诊断设计，不支持“所有基准已经采用配对”的推断。',
               '3. **长期任务需要分阶段看。** RoboCasa-Shift、LIBERO-RECOVER、RoboComb 的阶段、失败状态和技能交接分析互补。',
               '4. **评测接口决定结论范围。** 图像问答、符号规划、闭环动作、真实执行回答不同问题；软件代理仅作为邻接参考。','',
               '这些观察的具体设置、数字和原始论文链接见[精读报告](benchmark-paper-deep-read.md)及[统一矩阵](benchmark-comparison.md)，不作为全领域频率结论。','',
               '## 6. 当前仍需补充','',
               '领域代表性、独立复用和代码可用性分别列入[缺口登记](survey-gap-register.md)。ESB-2 保留为可选后续研究设想；调研完成不以实现新基准为条件。']
    md('analysis/基准共同特征.md',common)

    index=['# 调研条目索引','',
           f"共 {len(survey['entries'])} 个登记条目，62 个已分类、60 个非重点档案。类型和旧 VLA 分类属于不同维度，不再将所有登记项称为独立 benchmark。",'',
           '当前比较入口：[统一矩阵](../analysis/benchmark-comparison.md) · [精读报告](../analysis/benchmark-paper-deep-read.md) · [调研方法](../docs/METHOD.md)。',
           '缩写与技术词先查[全库术语表](../docs/GLOSSARY.md)；每个条目文档的第 10 节也会列出该文实际出现的词并解释。', '',
           '“原全文补录”保留历史标记；本轮 62 条另有正文重点章节核查。项目状态只表示入口查找结果。']
    cards={c['name']:c for c in read('benchmark_cards.json')['cards']}
    for t in TYPE:
        if t=='unreviewed':continue
        group=[e for e in active if e['primary_type']==t]
        index += ['',f'## {TYPE[t]}（{len(group)} 条）','', '| 条目 | 研究目标 | 具身关联 | 项目入口 | 原全文补录 |','|---|---|---|---|---|']
        for e in group:
            index.append(f"| {link(e,'')} | {labels(e['objectives'],OBJECTIVE)} | {RELEVANCE[e['relevance']]} | {PROJECT[e['resources']['entry_status']]} | {'是' if cards[e['name']]['fulltext']['status'] else '—'} |")
    index += ['', '## 非重点档案（60 条，未重新分类）','',
              '继续保留在 `no-project/`。未找到已确认入口不意味着项目绝对不存在；本轮不扩读，不纳入已分类对象的统计。','',
              '| 条目 | 历史分类 | 原全文补录 |','|---|---|---|']
    for e in survey['entries']:
        if e['focus']=='archived':index.append(f"| {link(e,'')} | {e['legacy_category']} | {'是' if cards[e['name']]['fulltext']['status'] else '—'} |")
    md('benchmarks/README.md',index)
    for e in active:
        p=ROOT/'benchmarks'/e['document']; text=p.read_text(encoding='utf-8')
        text=re.sub(r'(?s)\n?'+re.escape(SURVEY_BEGIN)+'.*?'+re.escape(SURVEY_END)+r'\n?', '\n', text)
        note=[SURVEY_BEGIN,
              f"> **统一调研分类**：{TYPE[e['primary_type']]}；{RELEVANCE[e['relevance']]}；目标：{labels(e['objectives'],OBJECTIVE)}。",
              '> **分类依据**：'+e['type_reason'],
              '> **比较口径**：[统一比较矩阵](../analysis/benchmark-comparison.md)。原“分类”及历史关键词标签保留为旧索引，不能用于新的安全覆盖统计。',SURVEY_END]
        head,rest=text.split('\n',1)
        p.write_text(head+'\n\n'+'\n'.join(note)+'\n\n'+rest.lstrip(),encoding='utf-8')
    # Add source-of-truth pointers without rewriting the paper review's evidence.
    p=ROOT/'analysis/benchmark-paper-deep-read.md'; text=p.read_text(encoding='utf-8')
    marker='> 分类与统计更新：'
    text=re.sub(r'(?m)^'+re.escape(marker)+r'.*\n?', '', text)
    first,rest=text.split('\n',1)
    p.write_text(first+'\n\n'+marker+'主要成果类型、评测目标和指标分母以[统一比较矩阵](benchmark-comparison.md)为准；本文保留逐篇阅读证据。\n'+rest.lstrip('\n'),encoding='utf-8')


def main():
    survey,registry=build_data(); outputs(survey,registry)
    s=survey['statistics']
    print(json.dumps({'inventory':s['inventory_entries'],'classified':s['classified_active_entries'],
                      'primary_types':s['counts_among_classified']['primary_type'],
                      'direct_embodied_tasksets':s['direct_embodied_tasksets'],
                      'paper_records':registry['paper_count'],'new_source_records':registry['supplement_count']},ensure_ascii=False))


if __name__=='__main__':
    main()
