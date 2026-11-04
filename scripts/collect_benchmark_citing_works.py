# -*- coding: utf-8 -*-
"""Collect the papers that cite — or whose abstract names — each benchmark's source paper.

Three evidence channels, recorded separately and never merged into one number:

* ``cites``         OpenAlex citation graph: the record lists the source work among its references.
* ``arxiv``         arXiv abstract search inside robotics/vision categories, verified locally by a
                    literal substring match on the title and abstract; the matching snippet is kept.
* ``ambiguous``     the benchmark name is an ordinary English word or an acronym that collides with
                    other work, so the arXiv hit list cannot be read as "papers about this benchmark".

Counts are per selected record. Preprint and proceedings records are not summed. A zero count is an
observation about this database on this date, not proof that nobody cites the paper. Nothing here
measures independent adoption: citing, mentioning and running the benchmark are different claims.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parents[1]
AGENT = "Embodied-Safety-Benchmark/1.0 (mailto:research@example.org)"
SELECT = "id,doi,title,publication_date,type,cited_by_count,primary_location,authorships"
LIST_LIMIT = 25          # most-cited citing works kept per entry
ARXIV_LIMIT = 30         # verified arXiv mentions kept per entry
TZ = dt.timezone(dt.timedelta(hours=8))
ATOM = {"a": "http://www.w3.org/2005/Atom"}
OS = "{http://a9.com/-/spec/opensearch/1.1/}totalResults"
ARXIV_CATS = "(cat:cs.RO OR cat:cs.CV)"

# Names that need an explicit arXiv search phrase.
ALIAS = {
    "LIBERO（基础套件）": "LIBERO",
    "ManiSkill / ManiSkill2": "ManiSkill",
    "Trap-LIBERO / Trap-RoboTwin": "Trap-LIBERO",
    "CARLA / CARLA Leaderboard": "CARLA",
}
# Names whose arXiv hit list cannot be read at face value. Reasons are shown to the reader.
AMBIGUOUS = {
    "DESPITE": "despite 是常用英文词，命中的绝大多数与该论文无关",
    "IS-Bench": "检索器把 IS-Bench 拆成 IS／Bench 两个泛词，命中与本题无关",
    "ORBIT": "orbit 是常用名词，命中的多数与 ORBIT 框架无关",
    "STARS": "stars 是常用名词，命中的多数与 STARS 方法无关",
    "VIPS": "VIPS 同时是图像处理库名与多个项目的缩写",
    "INFUSE": "infuse 是常用动词，命中含大量无关工作",
    "SafeBench": "SafeBench 同时被自动驾驶与多模态 LLM 安全两类工作使用，需按正文区分",
}


def api_json(url: str, params: dict | None = None, timeout: int = 40) -> dict:
    last = "unreached"
    for attempt in range(4):
        try:
            resp = requests.get(url, params=params, headers={"User-Agent": AGENT}, timeout=timeout)
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


def short_id(value: str | None) -> str | None:
    return value.rsplit("/", 1)[-1] if value else None


def work_row(row: dict) -> dict:
    authors = [a["author"]["display_name"] for a in row.get("authorships") or []]
    loc = row.get("primary_location") or {}
    return {
        "id": short_id(row.get("id")),
        "doi": row.get("doi"),
        "title": row.get("title"),
        "publication_date": row.get("publication_date"),
        "year": (row.get("publication_date") or "")[:4] or None,
        "type": row.get("type"),
        "venue": (loc.get("source") or {}).get("display_name"),
        "cited_by_count": row.get("cited_by_count"),
        "first_author": authors[0] if authors else None,
        "author_count": len(authors),
    }


def search_phrase(name: str) -> str:
    if name in ALIAS:
        return ALIAS[name]
    head = name.split(" / ")[0]
    head = re.sub(r"[（(].*?[）)]", "", head).strip()
    return head or name


def snippet(text: str, phrase: str, width: int = 110) -> str:
    pos = text.lower().find(phrase.lower())
    if pos < 0:
        return ""
    start, end = max(0, pos - width), min(len(text), pos + len(phrase) + width)
    return ("…" if start else "") + text[start:end].strip() + ("…" if end < len(text) else "")


def literal_regex(phrase: str):
    """Match the name as its own token: MemForm must not be satisfied by MemFormer."""
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(phrase) + r"(?![A-Za-z0-9])", re.IGNORECASE)


def arxiv_mentions(phrase: str, exclude_id: str | None) -> dict:
    """Verified abstract-level mentions. The API count is fuzzy, so hits are re-checked locally."""
    query = '%s AND abs:"%s"' % (ARXIV_CATS, phrase)
    payload = {"search_query": query, "max_results": 50, "sortBy": "relevance"}
    last = "unreached"
    for attempt in range(4):
        try:
            resp = requests.get("https://export.arxiv.org/api/query", params=payload,
                                headers={"User-Agent": AGENT}, timeout=45)
            if resp.status_code in (429, 500, 502, 503, 504):
                last = "HTTP %d" % resp.status_code
                time.sleep(3 * (attempt + 1))
                continue
            resp.raise_for_status()
            root = ET.fromstring(resp.text)
            break
        except (requests.RequestException, ET.ParseError) as exc:
            last = str(exc)
            time.sleep(3 * (attempt + 1))
    else:
        return {"query": query, "status": "failed", "error": last, "verified": None,
                "pool_reported": None, "works": []}

    pool = root.find(OS).text if root.find(OS) is not None else None
    pattern = literal_regex(phrase)
    works = []
    for entry in root.findall("a:entry", ATOM):
        ident = (entry.find("a:id", ATOM).text or "").rsplit("/abs/", 1)[-1]
        base_id = re.sub(r"v\d+$", "", ident)
        if exclude_id and base_id == exclude_id:
            continue
        title = " ".join((entry.find("a:title", ATOM).text or "").split())
        abstract = " ".join((entry.find("a:summary", ATOM).text or "").split())
        if not pattern.search(title + " " + abstract):
            continue
        published = entry.find("a:published", ATOM).text or ""
        works.append({
            "arxiv_id": ident,
            "title": title,
            "published": published[:10],
            "year": published[:4],
            "primary_category": (entry.find("{http://arxiv.org/schemas/atom}primary_category").attrib.get("term")
                                 if entry.find("{http://arxiv.org/schemas/atom}primary_category") is not None else None),
            "in_title": bool(pattern.search(title)),
            "context": snippet(abstract if pattern.search(abstract) else title + ". " + abstract, phrase),
            "url": "https://arxiv.org/abs/" + base_id,
        })
    return {"query": query, "status": "ok", "verified": len(works), "pool_reported": pool,
            "pool_reported_is_fuzzy": True, "works": works}


def collect(entry: dict) -> dict:
    oa = entry["openalex"]
    record = {"benchmark": entry["benchmark"], "document": entry["document"],
              "paper": entry["paper"], "source_link": entry["source_link"],
              "openalex_id": short_id(oa.get("id")), "status": oa.get("status"),
              "cited_by_count": oa.get("cited_by_count"), "errors": [], "queries": []}
    if oa.get("status") != "matched" or not record["openalex_id"]:
        record["cites"] = {"total": None, "listed": 0, "complete": None, "works": [], "by_year": {}}
    else:
        wid = record["openalex_id"]
        base = "https://api.openalex.org/works"
        # Channel 1: works that cite the selected record.
        record["queries"].append("filter=cites:%s" % wid)
        try:
            payload = api_json(base, {"filter": "cites:" + wid, "sort": "cited_by_count:desc",
                                      "per-page": LIST_LIMIT, "select": SELECT})
            total = payload["meta"]["count"]
            works = [work_row(r) for r in payload.get("results", [])]
            record["cites"] = {"total": total, "listed": len(works),
                               "complete": total <= len(works), "works": works, "by_year": {}}
        except Exception as exc:                               # noqa: BLE001 - recorded, not hidden
            record["errors"].append({"channel": "cites", "error": str(exc)})
            record["cites"] = {"total": None, "listed": 0, "complete": None, "works": [], "by_year": {}}
        time.sleep(0.2)
        if record["cites"]["total"]:
            record["queries"].append("group_by=publication_year&filter=cites:%s" % wid)
            try:
                payload = api_json(base, {"filter": "cites:" + wid, "group_by": "publication_year"})
                record["cites"]["by_year"] = {g["key"]: g["count"]
                                              for g in payload.get("group_by", []) if g.get("key")}
            except Exception as exc:                           # noqa: BLE001
                record["errors"].append({"channel": "cites_by_year", "error": str(exc)})
            time.sleep(0.2)

    # Channel 2: arXiv abstract mentions inside cs.RO / cs.CV.
    phrase = search_phrase(entry["benchmark"])
    record["queries"].append('%s AND abs:"%s"' % (ARXIV_CATS, phrase))
    try:
        record["arxiv"] = arxiv_mentions(phrase, entry.get("arxiv_id"))
        record["arxiv"]["phrase"] = phrase
        record["arxiv"]["works"] = record["arxiv"]["works"][:ARXIV_LIMIT]
        if phrase in AMBIGUOUS:
            record["arxiv"]["ambiguity_note"] = AMBIGUOUS[phrase]
            record["arxiv"]["status"] = "ambiguous"
    except Exception as exc:                                   # noqa: BLE001
        record["errors"].append({"channel": "arxiv", "error": str(exc)})
        record["arxiv"] = {"query": '%s AND abs:"%s"' % (ARXIV_CATS, phrase), "status": "failed",
                           "error": str(exc), "verified": None, "works": [], "phrase": phrase}
    time.sleep(3.0)          # arXiv asks clients to keep requests a few seconds apart.
    return record


def main() -> None:
    snapshot = json.loads((ROOT / "data/benchmark_citation_snapshot.json").read_text(encoding="utf-8"))
    existing = ROOT / "data/benchmark_citing_works.json"
    arxiv_only = "--arxiv-only" in sys.argv
    if arxiv_only:
        # Re-run only the arXiv channel, keeping the citation-graph results already observed.
        entries = json.loads(existing.read_text(encoding="utf-8"))["entries"]
        for record in entries:
            phrase = search_phrase(record["benchmark"])
            try:
                record["arxiv"] = arxiv_mentions(phrase, next(
                    (src["arxiv_id"] for src in snapshot["entries"] if src["benchmark"] == record["benchmark"]), None))
                record["arxiv"]["phrase"] = phrase
                record["arxiv"]["works"] = record["arxiv"]["works"][:ARXIV_LIMIT]
                if phrase in AMBIGUOUS:
                    record["arxiv"]["ambiguity_note"] = AMBIGUOUS[phrase]
                    record["arxiv"]["status"] = "ambiguous"
            except Exception as exc:                           # noqa: BLE001
                record["errors"].append({"channel": "arxiv", "error": str(exc)})
                record["arxiv"] = {"query": '%s AND abs:"%s"' % (ARXIV_CATS, phrase), "status": "failed",
                                   "error": str(exc), "verified": None, "works": [], "phrase": phrase}
            time.sleep(3.0)
    else:
        entries = [collect(e) for e in snapshot["entries"]]
    now = dt.datetime.now(TZ)
    payload = {
        "schema_version": 1,
        "generated_at": now.date().isoformat(),
        "queried_at": now.isoformat(),
        "source": "OpenAlex Works API (citations) + arXiv API (abstract mentions)",
        "scope": "62 classified entries; one selected record per entry (preprint and proceedings versions are not summed)",
        "channels": {
            "cites": "OpenAlex filter=cites:<work_id>; the citation graph, i.e. the paper is in the reference list",
            "arxiv": 'arXiv search "cat:cs.RO|cs.CV AND abs:\\"<name>\\"", then a local literal match on title+abstract; snippet kept',
        },
        "listing_rule": "At most %d citing works and %d arXiv mentions per entry, most-cited / most-relevant first. "
                        "'complete' says whether the listed citing works are the whole set." % (LIST_LIMIT, ARXIV_LIMIT),
        "entry_count": len(entries),
        "entries_with_citations": sum(1 for e in entries if (e.get("cites") or {}).get("total")),
        "entries_with_arxiv_mentions": sum(1 for e in entries if (e.get("arxiv") or {}).get("verified")),
        "entries": entries,
    }
    (ROOT / "data/benchmark_citing_works.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote %d entries; citing=%d; arxiv-mentioned=%d; date=%s"
          % (len(entries), payload["entries_with_citations"],
             payload["entries_with_arxiv_mentions"], payload["generated_at"]))


if __name__ == "__main__":
    main()
