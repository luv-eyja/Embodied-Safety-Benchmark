import json, subprocess, time, urllib.parse, os, sys

OUT = r'D:\study\Embodied\docs\_openalex.json'
FETCH = os.path.expandvars(r'%USERPROFILE%\.dsh\bin\fetch.mjs')

titles = [
 "Manipulation Facing Threats Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models",
 "Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation",
 "IS-Bench Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks",
 "Advancing Embodied Agent Security From Safety Benchmarks to Input Moderation",
 "SafeAgentBench A Benchmark for Safe Task Planning of Embodied LLM Agents",
 "Inspect Robots Evaluating the Capabilities and Safety of Embodied AI",
 "CAPSafe A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents",
 "RT-Safe Benchmarking Agent Safety in Real-Time Embodied Environment",
 "Generating Robot Constitutions Benchmarks for Semantic Safety",
 "SafeMind Benchmarking and Mitigating Safety Risks in Embodied LLM Agents",
 "A Framework for Benchmarking and Aligning Task-Planning Safety in LLM-Based Embodied Agents",
 "The Yes-Man Syndrome Benchmarking Abstention in Embodied Robotic Agents",
 "GuardianBench A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI",
 "RoboJailBench Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents",
 "LIBERO Benchmarking Knowledge Transfer for Lifelong Robot Learning",
 "CALVIN A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks",
 "Evaluating Real-World Robot Manipulation Policies in Simulation",
 "RoboCasa Large-Scale Simulation of Everyday Tasks for Generalist Robots",
 "VLA-Arena An Open-Source Framework for Benchmarking Vision-Language-Action Models",
 "RoboPAIR Jailbreaking LLM-controlled Robots",
 "BadRobot Jailbreaking Embodied LLMs in the Physical World",
 "Embodied Agent Interface Benchmarking LLMs for Embodied Decision Making",
 "Explore the Rationality of Jailbreak Attacks on Embodied AI",
 "Safety Evaluation of Vision-Language-Action Models A Survey",
 "RoboTwin Dual-Arm Robot Benchmark",
 "WorldModelBench Benchmarking World Models",
]

res = {}
if os.path.exists(OUT):
    res = json.load(open(OUT, encoding='utf-8'))

for t in titles:
    if t in res:
        continue
    q = urllib.parse.quote(t)
    url = ('https://api.openalex.org/works?search=%s&per_page=4'
           '&select=title,publication_year,doi,primary_location,cited_by_count' % q)
    tmp = os.path.expandvars(r'%TEMP%\oa_tmp.json')
    subprocess.run(['node', FETCH, url, '-o', tmp], capture_output=True)
    try:
        d = json.load(open(tmp, encoding='utf-8'))
    except Exception as e:
        print('FAIL', t, e)
        time.sleep(2)
        continue
    rows = []
    for r in (d.get('results') or [])[:4]:
        pl = r.get('primary_location') or {}
        src = (pl.get('source') or {}).get('display_name')
        rows.append({
            'title': r.get('title'),
            'year': r.get('publication_year'),
            'venue': src,
            'raw_source': pl.get('raw_source_name'),
            'doi': r.get('doi'),
            'cites': r.get('cited_by_count'),
        })
    res[t] = rows
    print('OK', t[:50], '->', rows[0]['venue'] if rows else None, rows[0]['year'] if rows else None)
    time.sleep(0.4)

json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(res))
