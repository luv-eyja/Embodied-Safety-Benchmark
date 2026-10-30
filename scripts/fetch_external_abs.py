import re, subprocess, os, json, time

FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')
OUT = r'D:\study\Embodied\docs\_external_abs.json'

ids = [
 '2512.22539',  # VLA-Arena
 '2606.27079',  # ForesightSafety-VLA
 '2608.17386',  # MANIGUARD
 '2604.16788',  # LongBench
 '2610.14415',  # QD environment generation red teaming
 '2405.05941',  # SimplerEnv
 '2406.02523',  # RoboCasa
 '2407.20242',  # BadRobot
 '2503.08663',  # ASIMOV (library has)
 '2410.10932',  # BadVLA
]

res = {}
if os.path.exists(OUT):
    res = json.load(open(OUT, encoding='utf-8'))

for i in ids:
    if i in res:
        continue
    tmp = os.path.expandvars(r'%TEMP%\ab.html')
    subprocess.run(['node', FETCH, 'https://arxiv.org/abs/%s' % i, '-o', tmp], capture_output=True)
    try:
        h = open(tmp, encoding='utf-8', errors='ignore').read()
    except Exception as e:
        print('FAIL', i); continue
    tm = re.search(r'<title>(.*?)</title>', h, re.S)
    am = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', h, re.S)
    dm = re.search(r'\[Submitted on ([^\]<]+)', h)
    title = re.sub(r'\s+', ' ', tm.group(1)).strip() if tm else ''
    ab = ''
    if am:
        ab = re.sub(r'<[^>]+>', ' ', am.group(1))
        ab = re.sub(r'^\s*Abstract:\s*', '', re.sub(r'\s+', ' ', ab)).strip()
    res[i] = {'title': title, 'abstract': ab, 'submitted': dm.group(1) if dm else ''}
    print('OK', i, '|', title[:95])
    time.sleep(0.5)

json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(res))
