# -*- coding: utf-8 -*-
"""Fetch full-text HTML for key papers and extract readable text."""
import os, re, subprocess, time, html

FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')
OUT = r'D:\study\Embodied\docs\_fulltext'
os.makedirs(OUT, exist_ok=True)

PAPERS = {
    'SafeStage': '2609.21223',
    'ManiGuard': '2608.17386',
    'ForesightSafety-VLA': '2606.27079',
    'SafeVLA-Bench': '2606.00773',
    'LIBERO-RIG': '2610.18843',
    'LIBERO-CTRL': '2609.15940',
    'HazardArena': '2604.12447',
    'DESPITE': '2604.18463',
    'RoboHarm': '2610.14043',
    'LIBERO-VPro': '2609.24350',
}


def strip_html(h):
    h = re.sub(r'(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?is)<math[^>]*>.*?</math>', ' [formula] ', h)
    h = re.sub(r'(?is)<h([1-6])[^>]*>', r'\n\n### ', h)
    h = re.sub(r'(?is)</h[1-6]>', '\n', h)
    h = re.sub(r'(?is)<(p|div|li|tr|br)[^>]*>', '\n', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    h = html.unescape(h)
    h = re.sub(r'[ \t]+', ' ', h)
    h = re.sub(r'\n\s*\n\s*\n+', '\n\n', h)
    return h.strip()


for name, aid in PAPERS.items():
    dest = os.path.join(OUT, name + '.txt')
    if os.path.exists(dest) and os.path.getsize(dest) > 2000:
        print('skip', name)
        continue
    tmp = os.path.expandvars(r'%TEMP%\ft.html')
    subprocess.run(['node', FETCH, 'https://arxiv.org/html/%s' % aid, '-o', tmp],
                   capture_output=True)
    try:
        raw = open(tmp, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        print('FAIL', name, e)
        continue
    txt = strip_html(raw)
    open(dest, 'w', encoding='utf-8').write(txt)
    print('%-22s %7d chars' % (name, len(txt)))
    time.sleep(0.4)
