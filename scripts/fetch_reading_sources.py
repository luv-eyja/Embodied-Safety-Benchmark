"""Cache official paper HTML for reading; downloads are excluded from Git."""
import hashlib
import html
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'docs' / '_paper_cache'


def fetch(entry):
    url = entry['fulltext_url']
    key = (entry.get('metadata', {}).get('version') or entry.get('arxiv_id')
           or hashlib.sha256(url.encode()).hexdigest()[:16])
    dest = CACHE / (key + '.html')
    if not dest.exists():
        result = subprocess.run(['curl.exe', '-sS', '-L', '--max-time', '35',
                                 '--output', str(dest), '--write-out', '%{http_code}', url],
                                capture_output=True, text=True)
        status = result.stdout.strip()
    else:
        status = 'cached'
    raw = dest.read_text(encoding='utf-8', errors='replace') if dest.exists() else ''
    title = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    title = html.unescape(re.sub('<[^>]+>', '', title.group(1))).strip() if title else ''
    headings = [html.unescape(re.sub('<[^>]+>', '', s)).strip()
                for s in re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', raw, re.S)]
    text = re.sub(r'(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>', '', raw)
    text = re.sub(r'(?is)<h[1-6][^>]*>', '\n## ', text)
    text = re.sub(r'(?is)</(?:p|div|li|tr|h[1-6])>|<br[^>]*>', '\n', text)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
    text = re.sub('[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n+', '\n\n', text).strip()
    txt = CACHE / (key + '.txt')
    txt.write_text(text, encoding='utf-8')
    fulltext = len(text) > 12000 and len(headings) > 5 and ('ltx_document' in raw or 'ltx_section' in raw)
    return {**entry, 'http_status':status, 'retrieved_title':title,
            'text_path':txt.relative_to(ROOT).as_posix(), 'text_chars':len(text),
            'headings':headings, 'fulltext_available':fulltext,
            'sha256':hashlib.sha256(raw.encode()).hexdigest()}


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    plan = json.loads((ROOT / 'data/benchmark_reading_sources.json').read_text(encoding='utf-8'))
    # The same paper can introduce two benchmarks. Fetch it once.
    unique = {e['fulltext_url']:e for e in plan['entries']}
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, unique.values()))
    by_url = {e['fulltext_url']:e for e in results}
    out = [{**e, **{k:v for k,v in by_url[e['fulltext_url']].items()
                   if k not in ('benchmark', 'document')}} for e in plan['entries']]
    (ROOT / 'data/benchmark_reading_sources.json').write_text(
        json.dumps({**plan, 'entries':out}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    for e in out:
        print(e['benchmark'],e['http_status'],e['text_chars'],e['fulltext_available'])


if __name__ == '__main__':
    main()
