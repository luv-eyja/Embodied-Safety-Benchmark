# -*- coding: utf-8 -*-
"""Normalise category: split '安全 Benchmark（自动驾驶）' into cat + domain."""

CANON = ['VLA 安全 Benchmark', 'VLA 鲁棒性 Benchmark', 'VLA 能力 Benchmark',
         '攻防评测框架', '评测方法与度量', '具身智能体安全 Benchmark',
         '具身安全 Benchmark', '具身鲁棒性 Benchmark', '具身能力 Benchmark', '综述']


def split_cat(cat):
    """'安全 Benchmark（自动驾驶）' -> ('具身安全 Benchmark', '自动驾驶')"""
    cat = (cat or '').strip()
    domain = ''
    if '（' in cat and cat.endswith('）'):
        i = cat.index('（')
        domain = cat[i + 1:-1]
        cat = cat[:i].strip()
    if cat in CANON:
        return cat, domain
    c = cat.lower()
    if '攻防' in cat:
        return '攻防评测框架', domain
    if '综述' in cat:
        return '综述', domain
    if '度量' in cat or '方法' in cat:
        return '评测方法与度量', domain
    if c.startswith('vla'):
        if '安全' in cat:
            return 'VLA 安全 Benchmark', domain
        if '鲁棒' in cat:
            return 'VLA 鲁棒性 Benchmark', domain
        return 'VLA 能力 Benchmark', domain
    if '智能体' in cat:
        return '具身智能体安全 Benchmark', domain
    if '安全' in cat:
        return '具身安全 Benchmark', domain
    if '鲁棒' in cat:
        return '具身鲁棒性 Benchmark', domain
    if '能力' in cat:
        return '具身能力 Benchmark', domain
    return '具身能力 Benchmark', domain
