# -*- coding: utf-8 -*-
"""Collect the papers that cite — or whose text mentions — each benchmark's source paper.

Two evidence channels are recorded separately and never merged into one number:

* ``cites``      OpenAlex citation graph: the record lists the source work among its references.
* ``mentioned``  OpenAlex full-text search for the benchmark name: the string occurs in the
                 paper's text. The paper may or may not reference the source work (metadata
                 lag, bibliography parsing, or a bare name drop).

Counts are per selected record. Preprint and proceedings records are not summed. A missing or
zero count is an observation about this database on this date, not proof that nobody cites the
paper. Nothing here measures independent adoption.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
AGENT = "Embodied-Safety-Benchmark/1.0 (mailto:research@example.org)"
SELECT = "id,doi,title,publication_date,type,cited_by_count,primary_location,authorships"
LIST_LIMIT = 25          # most-cited citing works kept per entry
MENTION_LIMIT = 10       # most-cited mentioning works kept per entry
TZ = dt.timezone(dt.timedelta(hours=8))

# Benchmark names containing separators or Chinese annotations need an explicit search phrase.
ALIAS = {
    "LIBERO（基础套件）": "LIBERO",
    "ManiSkill / ManiSkill2": "ManiSkill",
    "Trap-LIBERO / Trap-RoboTwin": "Trap-LIBERO",
    "CARLA / CARLA Leaderboard": "CARLA",
    "Open X-Embodiment": "Open X-Embodiment",
    "nuScenes": "nuScenes",
}


def api_json(url: str, params: dict | None = None) -> dict:
    last = "unreached"
    for attempt in range(4):
        try:
            resp = requests.get(url, params=params, headers={"User-Agent": AGENT}, timeout=40)
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


def collect(entry: dict) -> dict:
    oa = entry["openalex"]
    record = {"benchmark": entry["benchmark"], "document": entry["document"],
              "paper": entry["paper"], "source_link": entry["source_link"],
              "openalex_id": short_id(oa.get("id")), "status": oa.get("status"),
              "cited_by_count": oa.get("cited_by_count"), "errors": [], "queries": []}
    if oa.get("status") != "matched" or not record["openalex_id"]:
        record["cites"] = {"total": None, "listed": 0, "complete": None, "works": [], "by_year": {}}
        record["mentioned"] = {"total": None, "listed": 0, "complete": None, "works": [],
                               "query": search_phrase(entry["benchmark"])}
        return record

    wid = record["openalex_id"]
    base = "https://api.openalex.org/works"
    # Channel 1: works that cite the selected record.
    url = base
    params = {"filter": "cites:" + wid, "sort": "cited_by_count:desc",
              "per-page": LIST_LIMIT, "select": SELECT}
    record["queries"].append("filter=cites:%s" % wid)
    try:
        payload = api_json(url, params)
        total = payload["meta"]["count"]
        works = [work_row(r) for r in payload.get("results", [])]
        record["cites"] = {"total": total, "listed": len(works),
                           "complete": total <= len(works), "works": works, "by_year": {}}
    except Exception as exc:                                   # noqa: BLE001 - recorded, not hidden
        record["errors"].append({"channel": "cites", "error": str(exc)})
        record["cites"] = {"total": None, "listed": 0, "complete": None, "works": [], "by_year": {}}
    time.sleep(0.2)

    # Channel 1b: publication-year distribution of the citing works.
    if record["cites"]["total"]:
        record["queries"].append("group_by=publication_year&filter=cites:%s" % wid)
        try:
            payload = api_json(base, {"filter": "cites:" + wid, "group_by": "publication_year"})
            record["cites"]["by_year"] = {g["key"]: g["count"]
                                         for g in payload.get("group_by", []) if g.get("key")}
        except Exception as exc:                               # noqa: BLE001
            record["errors"].append({"channel": "cites_by_year", "error": str(exc)})
        time.sleep(0.2)

    # Channel 2: works whose full text contains the benchmark name.
    phrase = search_phrase(entry["benchmark"])
    record["queries"].append('fulltext.search:"%s"' % phrase)
    try:
        payload = api_json(base, {"filter": 'fulltext.search:"%s"' % phrase,
                                  "sort": "cited_by_count:desc",
                                  "per-page": MENTION_LIMIT, "select": SELECT})
        rows = [r for r in payload.get("results", []) if short_id(r.get("id")) != wid]
        citing_ids = {w["id"] for w in record["cites"]["works"]}
        complete_cites = record["cites"]["complete"]
        works = []
        for row in rows:
            item = work_row(row)
            item["in_cites_sample"] = item["id"] in citing_ids
            # Only claim "not a citing work" when the citing list is known to be complete.
            item["cites_source"] = (item["in_cites_sample"] if complete_cites else None)
            works.append(item)
        record["mentioned"] = {"total": max(payload["meta"]["count"] - 1, 0), "query": phrase,
                               "listed": len(works), "works": works,
                               "total_is_upper_bound": True,
                               "note": "计数含本条来源论文自身，已减 1；全文检索不等于引用。"}
    except Exception as exc:                                   # noqa: BLE001
        record["errors"].append({"channel": "mentioned", "error": str(exc)})
        record["mentioned"] = {"total": None, "query": phrase, "listed": 0, "works": [],
                               "note": "查询失败，不按 0 处理。"}
    time.sleep(0.2)

    record["cited_never_listed"] = (record["cites"]["total"] or 0) > record["cites"]["listed"]
    return record


def main() -> None:
    snapshot = json.loads((ROOT / "data/benchmark_citation_snapshot.json").read_text(encoding="utf-8"))
    entries = [collect(e) for e in snapshot["entries"]]
    now = dt.datetime.now(TZ)
    payload = {
        "schema_version": 1,
        "generated_at": now.date().isoformat(),
        "queried_at": now.isoformat(),
        "source": "OpenAlex Works API",
        "scope": "62 classified entries; one selected record per entry (preprint and proceedings versions are not summed)",
        "channels": {
            "cites": "filter=cites:<work_id>; OpenAlex citation graph",
            "mentioned": "filter=fulltext.search:\"<benchmark name>\"; full-text occurrence, not a citation",
        },
        "listing_rule": "At most %d citing works and %d mentioning works per entry, most-cited first. "
                        "'complete' says whether the listed works are the whole set." % (LIST_LIMIT, MENTION_LIMIT),
        "entry_count": len(entries),
        "entries_with_citations": sum(1 for e in entries if (e.get("cites") or {}).get("total")),
        "entries": entries,
    }
    (ROOT / "data/benchmark_citing_works.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote %d entries; %d with >=1 citing work; date=%s"
          % (len(entries), payload["entries_with_citations"], payload["generated_at"]))


if __name__ == "__main__":
    main()
