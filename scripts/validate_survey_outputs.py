# -*- coding: utf-8 -*-
"""Check evidence boundaries, data joins, links and spreadsheet freshness."""
import collections
import hashlib
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def main():
    survey = read('data/benchmark_survey.json')
    entries = survey['entries']
    active = [e for e in entries if e['focus'] == 'active']
    archive = [e for e in entries if e['focus'] == 'archived']
    by_name = {e['name']: e for e in entries}
    assert len(entries) == len(by_name) == len({e['entry_id'] for e in entries}) == 122
    assert len(active) == 62 and len(archive) == 60
    assert all(e['primary_type'] == 'unreviewed' and e['real_evidence'] is None for e in archive)
    assert all(e['classification_status'] == 'not_reviewed' and e['source'] is None for e in archive)
    for e in active:
        assert e['evidence']['classification_basis']['sections'] and e['type_reason'], e['name']
        assert e['unit'] and e['metrics'] and all(len(m) == 3 and all(m) for m in e['metrics']), e['name']
        assert len(set(e['objectives'])) == len(e['objectives']), e['name']
        assert len(set(e['domains'])) == len(e['domains']), e['name']
        assert e['resources']['execution_reproduction'] == 'not_performed'
        assert e['resources']['code_data_license_baseline_audit'] == 'not_audited'
        doc = (ROOT/'benchmarks'/e['document']).read_text(encoding='utf-8')
        assert doc.count('<!-- survey-classification:start -->') == 1, e['name']
        assert doc.count('<!-- survey-classification:end -->') == 1, e['name']
    # Regression checks for known classification errors, not a claim of exhaustiveness.
    assert by_name['STARS']['primary_type'] == 'method'
    for name in ('Open X-Embodiment', 'AgiBot World', 'RoboMIND'):
        assert by_name[name]['primary_type'] == 'dataset', name
    for name in ('Agent-SafetyBench', 'INFUSE', 'MemForm', 'ORBIT', 'SkillSafetyBench'):
        assert by_name[name]['relevance'] == 'adjacent', name
    stats = survey['statistics']
    assert stats['counts_among_classified']['primary_type'] == dict(collections.Counter(e['primary_type'] for e in active))
    assert stats['direct_embodied_tasksets'] == sum(e['primary_type'] == 'benchmark' and e['relevance'] == 'direct' for e in active)
    assert stats['real_execution_confirmed_entries'] == sum(e['real_evidence'] in ('execution_reported', 'paired_validation') for e in active)
    assert sum(stats['counts_among_classified']['real_evidence'].values()) == len(active)
    assert survey['coverage_semantics'] == 'entry_label_cooccurrence_not_task_level_evidence'
    for d in survey['domain_coverage']:
        assert len(d['entries']) == len(set(d['entries']))
        assert set(d['entries']) == {e['name'] for e in active if d['domain'] in e['domains']}
        for objective, names in d['objective_members'].items():
            assert len(names) == len(set(names))
            assert set(names) == {e['name'] for e in active if d['domain'] in e['domains'] and objective in e['objectives']}
    registry = read('data/survey_paper_registry.json')
    papers = registry['papers']; rows = read('data/rows.json')
    assert registry['raw_row_count'] == len(rows) == 193
    assert registry['paper_count'] == len(papers)
    assert registry['supplement_count'] == sum(not p['in_original_table'] for p in papers)
    assert sorted(i for p in papers for i in p['raw_row_indices']) == list(range(1, len(rows)+1))
    for p in papers:
        for i in p['raw_row_indices']:
            assert p['title'] == rows[i-1]['title'] and p['url'] == rows[i-1]['link']
    links = [n for p in papers for n in p['reviewed_benchmarks']]
    assert len(links) == len(set(links)) == 62 and set(links) == {e['name'] for e in active}
    docs = ['README.md', 'docs/METHOD.md', 'analysis/benchmark-comparison.md',
            'analysis/statistical-corrections.md', 'analysis/survey-gap-register.md',
            'design/coverage-matrix.md', 'benchmarks/README.md', 'analysis/基准共同特征.md']
    for name in docs:
        p = ROOT/name
        for url in re.findall(r'\]\(([^\s)]+)\)', p.read_text(encoding='utf-8')):
            if '://' in url or url.startswith('#'):
                continue
            target = unquote(url.split('#')[0])
            assert (p.parent/target).exists(), (name, target)
    manifest = read('data/benchmark_survey_workbook_manifest.json')
    for path, sha in manifest['inputs'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha, ('stale workbook', path)
    xlsx = ROOT/'data/benchmark_survey.xlsx'
    assert hashlib.sha256(xlsx.read_bytes()).hexdigest() == manifest['output_sha256']
    ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(xlsx) as z:
        wb = ET.fromstring(z.read('xl/workbook.xml'))
        assert [s.attrib['name'] for s in wb.find('s:sheets', ns)] == ['调研概览', '条目分类', '评测协议', '论文证据']
        table_paths = [n for n in z.namelist() if re.match(r'xl/tables/table\d+\.xml$', n)]
        assert len(table_paths) == 3
        for name in table_paths:
            assert ET.fromstring(z.read(name)).find('s:autoFilter', ns) is not None
        for i in range(1, 5):
            root = ET.fromstring(z.read('xl/worksheets/sheet%d.xml' % i))
            assert not root.findall('.//s:c[@t="e"]', ns), ('Excel formula errors', i)
            if i > 1:
                pane = root.find('.//s:pane', ns)
                assert pane is not None and pane.attrib.get('xSplit') == '2' and pane.attrib.get('ySplit') == '1'
        summary = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        assert len(summary.findall('.//s:f', ns)) >= 10
        for cell, value in {'B7':122, 'B8':62, 'B9':60, 'B10':48, 'B11':59, 'B12':18,
                            'F7':52, 'F8':3, 'F9':2, 'F10':4, 'F11':1,
                            'B16':193, 'B17':6, 'B18':199}.items():
            node = summary.find('.//s:c[@r="%s"]/s:v' % cell, ns)
            assert node is not None and float(node.text) == value, ('cached summary', cell)
        classification = ET.fromstring(z.read('xl/worksheets/sheet2.xml'))
        for i, entry in enumerate(entries, 2):
            cite = (entry.get('citation') or {}).get('cited_by_count')
            cell = classification.find('.//s:c[@r="K%d"]/s:v' % i, ns)
            date = classification.find('.//s:c[@r="L%d"]/s:v' % i, ns)
            if cite is None:
                assert cell is None and date is None, ('unknown citation exported as observation', entry['name'])
            else:
                assert cell is not None and float(cell.text) == cite
                assert date is not None
                date_cell = classification.find('.//s:c[@r="L%d"]' % i, ns)
                if date_cell.attrib.get('t') == 'd':
                    assert date.text[:10] == entry['citation']['snapshot_date']
                else:
                    assert date_cell.attrib.get('t', 'n') == 'n' and float(date.text) > 40000
    print('Survey validated: 122 entries / 62 classified / 60 unknown; joins, evidence boundaries, local links and workbook verified.')


if __name__ == '__main__':
    main()
