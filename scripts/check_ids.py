import json, os, re, subprocess, time

FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')
rows = json.load(open(r'D:\study\Embodied\docs\_rows.json', encoding='utf-8'))
ids = []
for r in rows:
    m = re.search(r'(\d{4}\.\d{4,5})', r['link'] or '')
    if m:
        ids.append((r['title'], m.group(1)))

out = {}
cache = r'D:\study\Embodied\docs\_idcheck.json'
if os.path.exists(cache):
    out = json.load(open(cache, encoding='utf-8'))

for title, i in ids:
    if i in out:
        continue
    tmp = os.path.expandvars(r'%TEMP%\chk.html')
    subprocess.run(['node', FETCH, 'https://arxiv.org/abs/%s' % i, '-o', tmp], capture_output=True)
    try:
        h = open(tmp, encoding='utf-8', errors='ignore').read()
    except Exception:
        out[i] = None
        continue
    tm = re.search(r'<title>(.*?)</title>', h, re.S)
    t = re.sub(r'\s+', ' ', tm.group(1)).strip() if tm else ''
    t = re.sub(r'^\[\d{4}\.\d{4,5}\]\s*', '', t)
    out[i] = t
    time.sleep(0.3)

json.dump(out, open(cache, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
n_ok = 0
for title, i in ids:
    got = out.get(i) or ''
    ok = title.lower()[:35].replace('the ', '') in got.lower() or got.lower()[:35] in title.lower()
    if not ok:
        print('MISMATCH', i)
        print('   want:', title[:95])
        print('   got :', got[:95])
    else:
        n_ok += 1
print('checked', len(ids), 'ok', n_ok)
