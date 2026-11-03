# -*- coding: utf-8 -*-
"""Refresh citation counts for active source-verified papers, never summing versions."""
from __future__ import annotations
import datetime as dt
import difflib
import json
import re
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
SELECT = "id,title,doi,publication_date,cited_by_count,primary_location,authorships"

def normalise(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())

AGENT = "Embodied-Safety-Benchmark/1.0 (mailto:research@example.org)"


def api_json(url: str) -> dict:
    """GET with bounded backoff. Bursty clients get HTTP 429 from the OpenAlex edge."""
    last = "unreached"
    for attempt in range(4):
        try:
            resp = requests.get(url, headers={"User-Agent": AGENT}, timeout=30)
            if resp.status_code in (429, 500, 502, 503, 504):
                last = "HTTP %d" % resp.status_code
                time.sleep(2 ** attempt)
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as exc:
            last = str(exc)
            time.sleep(2 ** attempt)
    raise RuntimeError(last)

def fetch(source: dict) -> dict:
    meta = source["metadata"]
    title = meta["title"]
    arxiv_doi = "10.48550/arxiv." + source["arxiv_id"]
    query_dois = [arxiv_doi] + ([meta["doi"]] if meta.get("doi") else [])
    queries = ["https://api.openalex.org/works?filter=doi:" + urllib.parse.quote("|".join(query_dois), safe="") + "&per-page=20&select=" + SELECT]
    # Older papers are more likely to have separately indexed proceedings.
    if meta["published"][:4] < "2026":
        queries.append("https://api.openalex.org/works?search=" + urllib.parse.quote(title) + "&per-page=10&select=" + SELECT)
    candidates, errors = {}, []
    for url in queries:
        try:
            for row in api_json(url).get("results", []):
                authors = [a["author"]["display_name"] for a in row.get("authorships", [])]
                common = set(map(normalise, authors)) & set(map(normalise, meta.get("authors", [])))
                score = difflib.SequenceMatcher(None, normalise(title), normalise(row["title"])).ratio()
                doi = re.sub(r"^https://doi.org/", "", (row.get("doi") or "").lower())
                exact_doi = doi in [d.lower() for d in query_dois]
                if not (exact_doi or (score >= 0.97 and common)):
                    continue
                loc = row.get("primary_location") or {}
                candidates[row["id"]] = {
                    "id": row["id"], "title": row["title"], "doi": row.get("doi"),
                    "publication_date": row.get("publication_date"),
                    "cited_by_count": row.get("cited_by_count"),
                    "title_similarity": round(score, 4), "author_overlap": len(common),
                    "exact_doi": exact_doi, "is_published": bool(loc.get("is_published")),
                    "venue": (loc.get("source") or {}).get("display_name"),
                    "landing_page_url": loc.get("landing_page_url")}
        except Exception as exc:
            errors.append({"url": url, "error": str(exc)})
    rows = list(candidates.values())
    rows.sort(key=lambda r: (r["is_published"], r["exact_doi"], r["title_similarity"]), reverse=True)
    chosen = rows[0] if rows else {}
    return {
        "paper": title, "source_link": source["paper_url"],
        "arxiv_id": source["arxiv_id"], "paper_version": meta["version"],
        "queries": queries, "query_errors": errors,
        "openalex": {"status": "matched" if rows else ("query_failed" if errors else "unmatched"),
                     "cited_by_count": None, **chosen}, "version_records": rows}

def preserve_prior(entries: list, previous: dict, cards: list) -> None:
    """Retain an observed count only if its paper identity still matches."""
    by_name = {e['benchmark']: e for e in previous.get('entries', [])}
    old_cards = {c['name']: c.get('citation_snapshot', {}) for c in cards}
    for entry in entries:
        entry['observed_on'] = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
        if entry['openalex']['status'] == 'matched':
            continue
        prior = by_name.get(entry['benchmark'], {})
        old = old_cards.get(entry['benchmark'], {})
        if (prior.get('source_link') == entry['source_link'] and
                prior.get('openalex', {}).get('status') == 'matched'):
            entry['openalex'] = prior['openalex']
            entry['version_records'] = prior.get('version_records', [])
            entry['observed_on'] = prior.get('observed_on', previous.get('generated_at'))
            entry['retained_prior_observation'] = True
        elif (old.get('status') == 'matched' and
              ((old.get('source_link') == entry['source_link'] and old.get('match_score', 0) >= 0.90) or
               (normalise(old.get('paper')) == normalise(entry['paper']) and old.get('match_score', 0) >= 0.97))):
            record = {'status': 'matched', 'id': old['openalex_id'], 'title': old['paper'],
                      'cited_by_count': old['cited_by_count'], 'query_mode': 'retained_source_verified_snapshot',
                      'version_note': 'Earlier DOI/title lookup retained; publication-version consolidation not verified.'}
            entry['openalex'] = record
            entry['version_records'] = [record]
            entry['observed_on'] = old['snapshot_date']
            entry['retained_prior_observation'] = True

def main() -> None:
    path = ROOT / "data/benchmark_citation_snapshot.json"
    previous = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    sources = json.loads((ROOT / "data/benchmark_reading_sources.json").read_text(encoding="utf-8"))["entries"]
    unique = {e["arxiv_id"]: e for e in sources}
    with ThreadPoolExecutor(max_workers=4) as pool:
        fetched = dict(zip(unique, pool.map(fetch, unique.values())))
    entries = [{"benchmark": e["benchmark"], "document": e["document"], **fetched[e["arxiv_id"]]} for e in sources]
    cards = json.loads((ROOT / 'data/benchmark_cards.json').read_text(encoding='utf-8'))['cards']
    preserve_prior(entries, previous, cards)
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
    snapshot = {
        "schema_version": 3, "generated_at": now.date().isoformat(), "queried_at": now.isoformat(),
        "scope": "active_only", "source": "OpenAlex Works API", "citation_field": "cited_by_count",
        "snapshot_rule": "Prefer a verified published record, otherwise the arXiv DOI record. Never sum version records. Zero is the selected record's observed count; null means unverified/unavailable.",
        "version_search_scope": "DOI lookup for all sources, title search additionally for sources first submitted before 2026; version discovery is not exhaustive.",
        "entry_count": len(entries), "unique_paper_count": len(unique),
        "matched_count": sum(e["openalex"]["status"] == "matched" for e in entries), "entries": entries}
    path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries, {snapshot['matched_count']} matched; date={snapshot['generated_at']}")

if __name__ == "__main__":
    main()
