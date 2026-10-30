# -*- coding: utf-8 -*-
"""Audit: remaining library papers that may still be evaluation work."""
import json, os, re

BASE = r'D:\study\Embodied'
lib = []
for f in ('papers', 'audited', 'screened'):
    lib += json.load(open(os.path.join(BASE, 'docs', '_data', f + '.json'), encoding='utf-8'))

have = {r['title'].strip().lower()
        for r in json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))}

VLA = re.compile(r'\bvla\b|vision-language-action|vision language action|vision-language action|'
                 r'language-conditioned polic|vision-language polic|robot foundation model|'
                 r'embodied foundation model|generalist polic|world[- ]action model|\bwam\b', re.I)

# 疑问式 / 实证式 / 诊断式 标题特征 —— 这类多半在评测
EVALISH = re.compile(
    r'\?|\bdo\b|\bdoes\b|\bare\b|\bhow\b|\bwhat\b|\bwhy\b|\bwhen\b|'
    r'empirical|study|studies|analysis|analys|diagnos|probe|rethink|'
    r'evaluat|assess|benchmark|systematic|investigat|characteriz|measur|'
    r'revisit|lessons|limits|mirage|illusion|gap|matter|robust|fragil|brittl', re.I)

seen, uniq = set(), []
for p in lib:
    k = (p.get('title') or '').strip().lower()
    if k in seen or k in have:
        continue
    seen.add(k)
    uniq.append(p)

rows = []
for p in uniq:
    t = p.get('title') or ''
    blob = t + ' ' + (p.get('abstract') or '')
    if not VLA.search(blob):
        continue
    if not EVALISH.search(t):
        continue
    hint = ''
    if re.search(r'benchmark|evaluat|assess|measur|metric', blob, re.I):
        hint += 'M'
    if re.search(r'diagnos|analysis|analys|probe|interpretab|mechanis', blob, re.I):
        hint += 'D'
    if re.search(r'attack|adversar|backdoor|jailbreak|patch|poison', blob, re.I):
        hint += 'A'
    rows.append((p.get('year'), p.get('layer'), p.get('subcat'), t, hint))

rows.sort(key=lambda x: (str(x[0]), x[3]))
out = ['%3d | %s | %-22s | %-3s | %s' % (i, r[0], (r[2] or '-')[:22], r[4], r[3])
       for i, r in enumerate(rows)]
open(os.path.join(BASE, 'docs', '_audit_rest.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('remaining eval-ish VLA papers:', len(rows))
