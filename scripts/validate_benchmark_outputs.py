# -*- coding: utf-8 -*-
"""Validate generated benchmark cards, documents, and comparison outputs."""
import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DOC_DIR = REPO / 'benchmarks'
CARDS = REPO / 'data' / 'benchmark_cards.json'
INDEX = DOC_DIR / 'README.md'
COMPARISON = REPO / 'analysis' / 'benchmark-comparison.md'
PROJECT_AUDIT = REPO / 'data' / 'benchmark_project_audit.json'
REQUIRED_SECTIONS = [
    '## 0. 评测卡片',
    '## 1. 测什么问题（内容与所测环节）',
    '## 2. 怎么构建的',
    '## 3. 用这个基准测了什么',
    '## 4. 关键结论、改进方向与可复用性',
    '## 5. 相关论文（均来自本调研表）',
    '## 6. 证据边界与复核建议',
]


TAG = re.compile('（(?:%s)）' % '|'.join(re.escape(k) for k in (
    'LLM 模型', 'VLM 模型', 'VLA 模型', '机构', '开源许可证', '会议／期刊',
    '基准', '数据集', '仿真平台', '机器人本体', '工具／框架')))


def main():
    payload = json.loads(CARDS.read_text(encoding='utf-8'))
    cards = payload['cards']
    expected_benchmarks = payload['benchmark_count']
    assert expected_benchmarks > 0, expected_benchmarks
    assert len(cards) == expected_benchmarks, len(cards)
    assert len({card['name'] for card in cards}) == expected_benchmarks
    assert sum(card['fulltext']['status'] for card in cards) == 10
    if PROJECT_AUDIT.exists():
        project_payload = json.loads(PROJECT_AUDIT.read_text(encoding='utf-8'))
        project_audits = project_payload.get('audits', [])
        assert len(project_audits) == expected_benchmarks, len(project_audits)
        assert {a['benchmark'] for a in project_audits} == {card['name'] for card in cards}
        assert all('project_audit' in card for card in cards)
        no_project_names = {
            a['benchmark'] for a in project_audits if a.get('status') == 'not_found'
        }
        no_project_cards = {
            card['name'] for card in cards
            if card.get('project_audit', {}).get('status') == 'not_found'
        }
        assert no_project_names == no_project_cards
        assert all(
            card['document'].startswith('no-project/')
            for card in cards if card['name'] in no_project_names
        )

    missing_sections = {}
    missing_docs = []
    for card in cards:
        path = DOC_DIR / card['document']
        if not path.exists():
            missing_docs.append(card['document'])
            continue
        text = path.read_text(encoding='utf-8')
        absent = [section for section in REQUIRED_SECTIONS if section not in text]
        if PROJECT_AUDIT.exists():
            absent += [] if '**项目地址审计**' in text else ['**项目地址审计**']
        if absent:
            missing_sections[card['name']] = absent
    assert not missing_docs, missing_docs
    assert not missing_sections, missing_sections

    project_path = REPO / 'data/benchmark_project_reviews.json'
    if project_path.exists():
        project = json.loads(project_path.read_text(encoding='utf-8'))
        active_names = {card['name'] for card in cards if not card['document'].startswith('no-project/')}
        entries = project['entries']
        assert {e['benchmark'] for e in entries} == active_names, len(entries)
        for entry in entries:
            for key in ('domain', 'purpose_build', 'defects', 'safety_relevance', 'tested',
                        'project_facts', 'limits_of_this_review'):
                assert entry.get(key), (entry['benchmark'], key)
            assert entry['project_status'] in ('found', 'platform_only', 'candidate'), entry['benchmark']
            assert entry.get('document') in {card['document'] for card in cards}, entry['benchmark']
        for card in cards:
            if card['document'].startswith('no-project/'):
                continue
            text = (DOC_DIR / card['document']).read_text(encoding='utf-8')
            assert text.count('<!-- project-review:start -->') == 1, card['name']
            assert text.count('<!-- project-review:end -->') == 1, card['name']
        print('project source reviews: %d; five review questions and project blocks verified' % len(entries))

    usage_path = REPO / 'data/benchmark_usage_records.json'
    if usage_path.exists():
        usage = json.loads(usage_path.read_text(encoding='utf-8'))
        active_names = {card['name'] for card in cards if not card['document'].startswith('no-project/')}
        uentries = usage['entries']
        assert {e['benchmark'] for e in uentries} == active_names, len(uentries)
        keys = ('paper', 'year', 'model', 'mode', 'setup', 'result', 'evidence')
        for entry in uentries:
            for record in entry['records']:
                missing = [k for k in keys if not record.get(k)]
                assert not missing, (entry['benchmark'], record.get('paper'), missing)
            if not entry['records']:
                assert entry.get('noise_note'), ('empty usage without explanation', entry['benchmark'])
        for card in cards:
            if card['document'].startswith('no-project/'):
                continue
            text = (DOC_DIR / card['document']).read_text(encoding='utf-8')
            assert text.count('<!-- usage-review:start -->') == 1, card['name']
            assert text.count('<!-- usage-review:end -->') == 1, card['name']
        print('usage records: %d papers over %d entries; per-record fields and blocks verified'
              % (sum(len(e['records']) for e in uentries), usage['entries_with_records']))

    glossary_json = REPO / 'data/benchmark_glossary.json'
    glossary_md = REPO / 'docs/GLOSSARY.md'
    if glossary_json.exists() and glossary_md.exists():
        glossary = json.loads(glossary_json.read_text(encoding='utf-8'))
        rendered = glossary_md.read_text(encoding='utf-8')
        missing = [t['term'] for t in glossary['terms'] if '**%s**' % t['term'] not in rendered]
        assert not missing, ('term missing from GLOSSARY.md', missing)
        for term in glossary['terms']:
            for key in ('term', 'category', 'short', 'long'):
                assert term.get(key), (term.get('term'), key)
            assert term['category'] in glossary['categories'], term['term']
            assert len(term['short']) >= 15, ('short explanation too terse', term['term'])
        for card in cards:
            if card['document'].startswith('no-project/'):
                continue
            doc = (DOC_DIR / card['document']).read_text(encoding='utf-8')
            assert doc.count('<!-- glossary:start -->') == 1, card['name']
            assert doc.count('<!-- glossary:end -->') == 1, card['name']
            assert '## 10. 术语说明' in doc, card['name']
        print('glossary: %d terms; every document has a term section and the total table is in sync'
              % len(glossary['terms']))

    names_path = REPO / 'data/benchmark_names.json'
    if names_path.exists():
        names = json.loads(names_path.read_text(encoding='utf-8'))
        legend = set(names['kinds_legend'])
        rendered = glossary_md.read_text(encoding='utf-8') if glossary_md.exists() else ''
        for item in names['names']:
            assert item['kind'] in legend, ('unknown kind', item['name'], item['kind'])
            assert isinstance(item.get('inline'), bool), item['name']
            assert item['name'] in rendered, ('name missing from GLOSSARY.md', item['name'])
        print('proper names: %d labelled by kind (%d inline)'
              % (len(names['names']), sum(1 for n in names['names'] if n['inline'])))

    index_text = INDEX.read_text(encoding='utf-8')
    for card in cards:
        assert index_text.count('](' + card['document'] + ')') == 1, card['name']
    assert INDEX.read_text(encoding='utf-8').count('| 是 |') == 10

    comparison = COMPARISON.read_text(encoding='utf-8')
    for heading in ('## 3. 评测单元与指标分母', '## 4. 协议、证据与资源状态', '## 5. 来源与影响力'):
        assert heading in comparison, heading
    for card in cards:
        if not card['document'].startswith('no-project/'):
            assert '](' + '../benchmarks/' + card['document'] + ')' in comparison, card['name']
    review_path = REPO / 'data/benchmark_paper_reviews.json'
    if review_path.exists():
        reviews = json.loads(review_path.read_text(encoding='utf-8'))['entries']
        sources = json.loads((REPO / 'data/benchmark_reading_sources.json').read_text(encoding='utf-8'))['entries']
        snapshot = json.loads((REPO / 'data/benchmark_citation_snapshot.json').read_text(encoding='utf-8'))
        citations = {e['benchmark']: e for e in snapshot['entries']}
        source_by_name = {s['benchmark']: s for s in sources}
        active = {c['name']: c for c in cards if not c['document'].startswith('no-project/')}
        assert {r['benchmark'] for r in reviews} == set(active) == set(citations) == set(source_by_name)
        assert len(reviews) == len(active) == payload['paper_review_count'] == 62
        assert snapshot['unique_paper_count'] == len({s['arxiv_id'] for s in sources})
        assert snapshot['matched_count'] == sum(e['openalex']['status'] == 'matched' for e in citations.values())
        for r in reviews:
            name = r['benchmark']; card = active[name]; src = source_by_name[name]; cite = citations[name]
            assert all(r.get(k) for k in ('question','kind','scenarios','implementation','results','limits','sections')), name
            assert src['fulltext_available'] and src['sha256'] and src['metadata']['version'], name
            assert card['source_link'] == cite['source_link'] == src['paper_url'], name
            assert card['primary_paper'] == src['metadata']['title'], name
            assert card['paper_review']['paper_version'] == src['metadata']['version'], name
            assert card['citation_snapshot']['cited_by_count'] == cite['openalex'].get('cited_by_count'), name
            text = (DOC_DIR / card['document']).read_text(encoding='utf-8')
            assert text.count('<!-- paper-review:start -->') == text.count('<!-- paper-review:end -->') == 1, name
            # Inline name tags (e.g. "GPT-4o（LLM 模型）") are inserted into the prose, so compare untagged text.
            plain = TAG.sub('', text)
            assert src['fulltext_url'] in plain and r['results'] in plain, name
            oa = cite['openalex']
            if oa['status'] == 'matched':
                assert isinstance(oa['cited_by_count'], int) and oa['cited_by_count'] >= 0 and oa['id'], name
            else:
                assert oa.get('cited_by_count') is None, name
            audit = card.get('source_audit', {})
            if audit.get('exclusive_source'):
                assert all(p['role'] != '提出' or p['title'] == audit['source_title'] for p in card['papers']), name
        assert all('paper_review' not in c for c in cards if c['document'].startswith('no-project/'))
        assert all(p['role'] == '方法' for p in active['STARS']['papers'])
        report = (REPO / 'analysis/benchmark-paper-deep-read.md').read_text(encoding='utf-8')
        assert len(re.findall(r'^### \d+\. ', report, re.M)) == 62
        print('paper reviews: 62; source/citation identities and archived scope verified')
    print('benchmark cards:', expected_benchmarks)
    print('fulltext cards: 10')
    print('document sections: complete')
    print('index entries: %d; fulltext markers: 10' % expected_benchmarks)
    print('comparison report: complete')


if __name__ == '__main__':
    main()
