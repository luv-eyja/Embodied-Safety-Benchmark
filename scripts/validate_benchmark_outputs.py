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
REQUIRED_SECTIONS = [
    '## 0. 评测卡片',
    '## 1. 测什么问题（内容与所测环节）',
    '## 2. 怎么构建的',
    '## 3. 用这个基准测了什么',
    '## 4. 关键结论、改进方向与可复用性',
    '## 5. 相关论文（均来自本调研表）',
    '## 6. 证据边界与复核建议',
]


def main():
    payload = json.loads(CARDS.read_text(encoding='utf-8'))
    cards = payload['cards']
    expected_benchmarks = payload['benchmark_count']
    assert expected_benchmarks > 0, expected_benchmarks
    assert len(cards) == expected_benchmarks, len(cards)
    assert len({card['name'] for card in cards}) == expected_benchmarks
    assert sum(card['fulltext']['status'] for card in cards) == 10

    missing_sections = {}
    missing_docs = []
    for card in cards:
        path = DOC_DIR / card['document']
        if not path.exists():
            missing_docs.append(card['document'])
            continue
        text = path.read_text(encoding='utf-8')
        absent = [section for section in REQUIRED_SECTIONS if section not in text]
        if absent:
            missing_sections[card['name']] = absent
    assert not missing_docs, missing_docs
    assert not missing_sections, missing_sections

    index_lines = [line for line in INDEX.read_text(encoding='utf-8').splitlines()
                   if re.match(r'^\| [^|]+ \| \d+ \| \d+ \| [ABC] \| (是|—) \| \[', line)]
    assert len(index_lines) == expected_benchmarks, len(index_lines)
    assert INDEX.read_text(encoding='utf-8').count('| 是 |') == 10

    comparison = COMPARISON.read_text(encoding='utf-8')
    for heading in ('## 3. 环节 × 安全属性比较', '## 4. 核心全文基准对照', '## 6. 全量卡片索引'):
        assert heading in comparison, heading
    assert comparison.count('../benchmarks/') >= expected_benchmarks + 10
    print('benchmark cards:', expected_benchmarks)
    print('fulltext cards: 10')
    print('document sections: complete')
    print('index entries: %d; fulltext markers: 10' % expected_benchmarks)
    print('comparison report: complete')


if __name__ == '__main__':
    main()
