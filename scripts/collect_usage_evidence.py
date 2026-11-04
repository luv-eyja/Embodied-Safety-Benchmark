# -*- coding: utf-8 -*-
"""Pull the sentences in which other papers refer to a benchmark, so usage can be read case by case.

For every classified entry the candidates are:
  * works in the OpenAlex citation graph (``benchmark_citing_works.json`` -> ``cites``)
  * works whose arXiv abstract names the benchmark (``benchmark_citing_works.json`` -> ``arxiv``)

Abstracts are fetched in batches (OpenAlex by work id, arXiv by id_list) and cached under
``docs/_abstract_cache.json`` (git-ignored). Only the sentences that actually mention the benchmark
are written to ``data/benchmark_usage_evidence.json``: that file is evidence, not a conclusion.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "docs/_abstract_cache.json"
OUT = ROOT / "data/benchmark_usage_evidence.json"
AGENT = "Embodied-Safety-Benchmark/1.0 (mailto:research@example.org)"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
MAX_PER_SOURCE = 25          # citing works kept per entry
MAX_SENTENCES = 2
SENTENCE_LIMIT = 420


def get(url: str, params: dict | None = None, timeout: int = 45) -> requests.Response:
    last = "unreached"
    for attempt in range(4):
        try:
            resp = requests.get(url, params=params, headers={"User-Agent": AGENT}, timeout=timeout)
            if resp.status_code in (429, 500, 502, 503, 504):
                last = "HTTP %d" % resp.status_code
                time.sleep(2 ** attempt)
                continue
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            last = str(exc)
            time.sleep(2 ** attempt)
    raise RuntimeError(last)


def abstract_from_index(index: dict | None) -> str:
    if not index:
        return ""
    positions = {}
    for word, slots in index.items():
        for slot in slots:
            positions[slot] = word
    return " ".join(positions[i] for i in sorted(positions))


def sentences_about(text: str, phrase: str) -> list[str]:
    """Keep the sentences that name the benchmark; fall back to a window if sentence splitting fails."""
    if not text:
        return []
    flat = " ".join(text.split())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", flat)
    pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(phrase) + r"(?![A-Za-z0-9])", re.IGNORECASE)
    hits = [p.strip() for p in parts if pattern.search(p)]
    if not hits:
        found = pattern.search(flat)
        if not found:
            return []
        start = max(0, found.start() - 200)
        hits = [flat[start:found.end() + 200].strip()]
    return [h[:SENTENCE_LIMIT] for h in hits[:MAX_SENTENCES]]


def main() -> None:
    citing = json.loads((ROOT / "data/benchmark_citing_works.json").read_text(encoding="utf-8"))["entries"]
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    oa_cache, arxiv_cache = cache.get("openalex", {}), cache.get("arxiv", {})

    # ---- OpenAlex abstracts, batched by 40 ids ----------------------------------------------
    wanted = {}
    for entry in citing:
        for work in (entry.get("cites") or {}).get("works", [])[:MAX_PER_SOURCE]:
            if work.get("id") and work["id"] not in oa_cache:
                wanted[work["id"]] = work
    ids = sorted(wanted)
    for start in range(0, len(ids), 40):
        chunk = ids[start:start + 40]
        try:
            payload = get("https://api.openalex.org/works",
                          {"filter": "openalex_id:" + "|".join(chunk), "per-page": 50,
                           "select": "id,title,publication_date,abstract_inverted_index"}).json()
            for row in payload.get("results", []):
                short = row["id"].rsplit("/", 1)[-1]
                oa_cache[short] = {"title": row.get("title"),
                                   "date": row.get("publication_date"),
                                   "abstract": abstract_from_index(row.get("abstract_inverted_index"))}
        except Exception as exc:                                # noqa: BLE001
            print("openalex batch failed:", exc)
        time.sleep(0.3)
    print("openalex abstracts cached:", len(oa_cache))

    # ---- arXiv abstracts, batched by 20 ids --------------------------------------------------
    arx_ids = {}
    for entry in citing:
        for work in (entry.get("arxiv") or {}).get("works", []):
            base = re.sub(r"v\d+$", "", work.get("arxiv_id") or "")
            if base and base not in arxiv_cache:
                arx_ids[base] = work
    bases = sorted(arx_ids)
    for start in range(0, len(bases), 20):
        chunk = bases[start:start + 20]
        try:
            text = get("https://export.arxiv.org/api/query",
                       {"id_list": ",".join(chunk), "max_results": len(chunk)}).text
            root = ET.fromstring(text)
            for node in root.findall("a:entry", ATOM):
                ident = (node.find("a:id", ATOM).text or "").rsplit("/abs/", 1)[-1]
                arxiv_cache[re.sub(r"v\d+$", "", ident)] = {
                    "title": " ".join((node.find("a:title", ATOM).text or "").split()),
                    "date": (node.find("a:published", ATOM).text or "")[:10],
                    "abstract": " ".join((node.find("a:summary", ATOM).text or "").split()),
                }
        except Exception as exc:                                # noqa: BLE001
            print("arxiv batch failed:", exc)
        time.sleep(3.0)
    print("arxiv abstracts cached:", len(arxiv_cache))
    CACHE.write_text(json.dumps({"openalex": oa_cache, "arxiv": arxiv_cache}, ensure_ascii=False), encoding="utf-8")

    # ---- Keep only the mentioning sentences -------------------------------------------------
    entries = []
    for entry in citing:
        name = entry["benchmark"]
        phrase = (entry.get("arxiv") or {}).get("phrase") or name.split(" / ")[0]
        candidates = []
        for work in (entry.get("cites") or {}).get("works", [])[:MAX_PER_SOURCE]:
            meta = oa_cache.get(work.get("id") or "", {})
            body = (meta.get("abstract") or "")
            for sent in sentences_about((body + " " + (work.get("title") or "")).strip(), phrase):
                candidates.append({"source": "cites", "id": work.get("id"),
                                   "doi": work.get("doi"), "url": work.get("doi") or
                                   ("https://openalex.org/" + (work.get("id") or "")),
                                   "title": work.get("title"), "year": work.get("year"),
                                   "venue": work.get("venue"), "cited_by_count": work.get("cited_by_count"),
                                   "sentence": sent})
        for work in (entry.get("arxiv") or {}).get("works", []):
            base = re.sub(r"v\d+$", "", work.get("arxiv_id") or "")
            meta = arxiv_cache.get(base, {})
            body = meta.get("abstract") or ""
            for sent in sentences_about((body + " " + (work.get("title") or "")).strip(), phrase):
                candidates.append({"source": "arxiv", "id": base, "doi": None, "url": work.get("url"),
                                   "title": meta.get("title") or work.get("title"),
                                   "year": (meta.get("date") or work.get("published") or "")[:4],
                                   "venue": "arXiv:" + (work.get("primary_category") or ""),
                                   "cited_by_count": None, "sentence": sent})
        entries.append({"benchmark": name, "phrase": phrase,
                        "candidates_with_sentence": len(candidates), "candidates": candidates})

    payload = {"schema_version": 1, "generated_at": time.strftime("%Y-%m-%d"),
               "source": "OpenAlex abstracts (cites) + arXiv abstracts (mention)",
               "rule": "只保留提到该 benchmark 的句子，最多 %d 句；这是原文片段，不是对用法的判断。" % MAX_SENTENCES,
               "entry_count": len(entries), "entries": entries}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    covered = sum(1 for e in entries if e["candidates"])
    total = sum(e["candidates_with_sentence"] for e in entries)
    print("usage evidence: %d entries with sentences, %d sentences total" % (covered, total))


if __name__ == "__main__":
    main()
