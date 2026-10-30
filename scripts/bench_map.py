# -*- coding: utf-8 -*-
"""Extract benchmark mentions from all 147 table rows -> benchmark/paper mapping."""
import json, os, re, collections

BASE = r'D:\study\Embodied'
rows = json.load(open(os.path.join(BASE, 'docs', '_rows.json'), encoding='utf-8'))

# 论文正文语料：库内取摘要，库外取已抓到的摘要
lib = {}
for f in ('papers', 'audited', 'screened'):
    for p in json.load(open(os.path.join(BASE, 'docs', '_data', f + '.json'), encoding='utf-8')):
        lib.setdefault(p['title'].strip().lower(), p)

ext_abs = {}
for f in ('_external_abs.json', '_oa_more.json'):
    fp = os.path.join(BASE, 'docs', f)
    if not os.path.exists(fp):
        continue
    d = json.load(open(fp, encoding='utf-8'))
    for k, v in d.items():
        if isinstance(v, dict):
            ext_abs[(v.get('title') or '').lower()] = v.get('abstract') or ''
        elif isinstance(v, list):
            for r in v:
                ext_abs[(r.get('title') or '').lower()] = r.get('abstract') or ''

for r in rows:
    t = r['title'].strip().lower()
    p = lib.get(t)
    r['abstract'] = (p.get('abstract') if p else '') or ext_abs.get(t, '') or ''

# 规范 benchmark 名 -> 别名（大小写不敏感正则）
BENCH = {
    'LIBERO（基础套件）': r'\bLIBERO\b(?!\s*[-–])|LIBERO-(?:Spatial|Object|Goal|Long|90|10)\b',
    'LIBERO-Plus': r'LIBERO-Plus|LIBERO\+',
    'LIBERO-Pro2.0': r'LIBERO-Pro',
    'LIBERO-RIG': r'LIBERO-RIG',
    'LIBERO-VPro': r'LIBERO-VPro',
    'LIBERO-MAX': r'LIBERO-MAX',
    'LIBERO-RECOVER': r'LIBERO-RECOVER',
    'LIBERO-X': r'LIBERO-X',
    'LIBERO-CTRL': r'LIBERO-CTRL',
    'LIBERO-Para': r'LIBERO-Para',
    'SafeLIBERO': r'SafeLIBERO',
    'Trap-LIBERO / Trap-RoboTwin': r'Trap-LIBERO|Trap-RoboTwin',
    'CALVIN': r'\bCALVIN\b',
    'SimplerEnv': r'SimplerEnv|SIMPLER\b',
    'RoboTwin': r'\bRoboTwin\b',
    'RoboCasa': r'\bRoboCasa\b',
    'RoboCasa365': r'RoboCasa365',
    'RoboCasa-Shift': r'RoboCasa-Shift',
    'VLABench': r'\bVLABench\b',
    'COLOSSEUM': r'COLOSSEUM|Colosseum(?!\s*Platform)',
    'RoboMIND': r'\bRoboMIND\b',
    'ManiSkill / ManiSkill2': r'ManiSkill',
    'RLBench': r'\bRLBench\b',
    'Meta-World': r'Meta-?World',
    'BEHAVIOR-1K': r'BEHAVIOR-1K|BEHAVIOR-?Suite|BEHAVIOR Robot Suite|\bBEHAVIOR-\d',
    'AI2-THOR / ALFRED / VirtualHome': r'AI2-?THOR|ALFRED|VirtualHome|RoboTHOR',
    'Habitat': r'\bHabitat\b',
    'RoboDojo': r'RoboDojo',
    'RoboColiseum': r'RoboColiseum',
    'AgiBot World': r'AgiBot World',
    'Open X-Embodiment': r'Open X-Embodiment|OpenX-Embodiment|\bOXE\b',
    'DROID': r'\bDROID\b',
    'BridgeData': r'BridgeData|Bridge Data',
    'RT-1 / RT-X 数据集': r'\bRT-1\b|\bRT-X\b|\bRT-2\b',
    'nuScenes': r'nuScenes',
    'NAVSIM': r'NAVSIM|NavSim',
    'CARLA': r'\bCARLA\b',
    'Bench2Drive': r'Bench2Drive',
    'DriveLM': r'DriveLM',
    'SafeAgentBench': r'SafeAgentBench',
    'AGENTSAFE / SAFE-THOR': r'AGENTSAFE|SAFE-THOR|SAFE-VERSE',
    'IS-Bench': r'IS-Bench',
    'SafeMindBench': r'SafeMind',
    'SafePlan-Bench / Safe-BeAl': r'SafePlan-Bench|Safe-BeAl',
    'ASIMOV Benchmark': r'ASIMOV',
    'VestaBench': r'VestaBench',
    'HASARD': r'HASARD',
    'EmbodiedBench': r'EmbodiedBench',
    'Embodied Agent Interface': r'Embodied Agent Interface',
    'Agent-SafetyBench': r'Agent-SafetyBench',
    'RT-Safe': r'RT-Safe|RT-SAFE',
    'CAPSafe': r'CAPSafe',
    'GuardianBench': r'GuardianBench',
    'EmbodiedGovBench': r'EmbodiedGovBench',
    'RoboAbstention': r'RoboAbstention',
    'MAGMA-Bench': r'MAGMA-Bench',
    'MMA-SafetyBench': r'MMA-SafetyBench',
    'RoboJailBench': r'RoboJailBench',
    'Inspect Robots': r'Inspect Robots',
    'RoboFollow': r'RoboFollow',
    'HazardArena': r'HazardArena',
    'SafeStage': r'SafeStage',
    'VLA-Arena': r'VLA-Arena',
    'ForesightSafety-VLA': r'ForesightSafety-VLA',
    'ManiGuard（ManiGuard-Bench）': r'ManiGuard',
    'SafeVLA-Bench': r'SafeVLA-Bench',
    'RoboEval': r'RoboEval|Robo Eval',
    'RoboChrono': r'RoboChrono',
    'RoboVista': r'RoboVista',
    'Robo2Process': r'Robo2Process',
    'TSHA': r'\bTSHA\b',
    'HUGE-Bench': r'HUGE-Bench',
    'VLN-Safe': r'VLN-Safe',
    'Spa-Bench': r'Spa-Bench',
    'RoboIRG-Bench': r'RoboIRG-Bench|RoboIRGBench',
    'IndustrialVLA-Bench': r'IndustrialVLA-Bench',
    'ManiPhysicsBench': r'ManiPhysicsBench',
    'BiDex-100': r'BiDex-100',
    'ManiUnit': r'\bManiUnit\b',
    'X2Real': r'X2Real',
    'RoboComb': r'RoboComb',
    'RoboStress': r'RoboStress',
    'LongBench': r'\bLongBench\b',
    'PolaRiS': r'PolaRiS',
    'RoboWorld': r'\bRoboWorld\b',
    'WorldEval': r'WorldEval',
    'dWorldEval': r'dWorldEval',
    'RoboReel': r'RoboReel',
    'R2R-CE（VLN 连续环境）': r'R2R-CE|R2R\b',
    'LIBERO-Para / ROBORMBench 等自建集': r'ROBORMBENCH|RoboRMBench',
}

mapping = collections.defaultdict(list)
for r in rows:
    blob = r['title'] + ' ' + (r.get('abstract') or '')
    for name, pat in BENCH.items():
        if re.search(pat, blob, re.I):
            mapping[name].append(r['title'])

lines = []
for name in sorted(mapping, key=lambda k: (-len(mapping[k]), k)):
    lines.append('## %s  (%d)' % (name, len(mapping[name])))
    for t in mapping[name]:
        lines.append('   - ' + t)
open(os.path.join(BASE, 'docs', '_bench_map.txt'), 'w', encoding='utf-8').write('\n'.join(lines))

summary = ['%3d | %s' % (len(v), k) for k, v in sorted(mapping.items(), key=lambda x: -len(x[1]))]
print('\n'.join(summary))
print('\nTOTAL benchmarks:', len(mapping))
json.dump({k: v for k, v in mapping.items()},
          open(os.path.join(BASE, 'docs', '_bench_map.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
