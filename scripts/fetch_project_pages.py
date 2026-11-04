# -*- coding: utf-8 -*-
"""Fetch project pages/repositories for the classified entries and cache the readable text.

The cache lives in ``docs/_project_cache.json`` (git-ignored, like ``docs/_paper_cache/``).
Nothing here is a substitute for reading the repository: this only retrieves the landing page,
the README, and the repository metadata that the later review quotes.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "docs/_project_cache.json"
AGENT = "Embodied-Safety-Benchmark/1.0 (mailto:research@example.org)"
TEXT_LIMIT = 4200


def get(url: str, timeout: int = 30):
    last = "unreached"
    for attempt in range(3):
        try:
            resp = requests.get(url, headers={"User-Agent": AGENT}, timeout=timeout)
            if resp.status_code in (429, 500, 502, 503, 504):
                last = "HTTP %d" % resp.status_code
                time.sleep(2 ** attempt)
                continue
            return resp
        except requests.RequestException as exc:
            last = str(exc)
            time.sleep(2 ** attempt)
    raise RuntimeError(last)


def github_parts(url: str):
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", url)
    return (m.group(1), m.group(2)) if m else (None, None)


def readme_for(owner: str, repo: str) -> tuple[str, str]:
    for name in ("README.md", "readme.md", "README.MD", "README.rst", "README.txt"):
        for base in ("https://raw.githubusercontent.com/%s/%s/HEAD/%s",
                     "https://cdn.jsdelivr.net/gh/%s/%s@HEAD/%s"):
            try:
                resp = get(base % (owner, repo, name))
                if resp.status_code == 200 and resp.text.strip():
                    return resp.text, base % (owner, repo, name)
            except Exception:                                  # noqa: BLE001 - try the next mirror
                continue
    return "", ""


def clean(text: str) -> str:
    """Drop HTML chrome; keep prose and code fences readable."""
    text = re.sub(r"(?is)<(script|style|svg|nav|footer)[^>]*>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<!--.*?-->", " ", text)
    images = re.findall(r"!\[[^\]]*\]\([^)]*\)", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    lines = [line.strip() for line in text.splitlines()]
    keep, blank = [], 0
    for line in lines:
        if not line:
            blank += 1
            if blank > 1 or not keep:
                continue
        else:
            blank = 0
        if re.fullmatch(r"[=\-~`|#*>·•\s]+", line or "-"):
            continue
        keep.append(line)
    return "\n".join(keep)[:TEXT_LIMIT], len(images)


def fetch_entry(audit: dict) -> dict:
    record = {"benchmark": audit["benchmark"], "status": audit["status"],
              "paper_url": audit.get("paper_url"), "sources": []}
    for url in audit.get("project_urls") or []:
        owner, repo = github_parts(url)
        item = {"url": url, "kind": "repo" if owner else "page"}
        if owner:
            try:
                meta = get("https://api.github.com/repos/%s/%s" % (owner, repo)).json()
                item.update({"stars": meta.get("stargazers_count"), "forks": meta.get("forks_count"),
                             "open_issues": meta.get("open_issues_count"),
                             "pushed_at": meta.get("pushed_at"), "created_at": meta.get("created_at"),
                             "archived": meta.get("archived"),
                             "license": (meta.get("license") or {}).get("spdx_id"),
                             "description": meta.get("description")})
            except Exception as exc:                           # noqa: BLE001
                item["meta_error"] = str(exc)
            time.sleep(0.5)
            readme, readme_url = readme_for(owner, repo)
            if readme:
                text, _ = clean(readme)
                item.update({"readme_url": readme_url, "text": text,
                             "text_length": len(readme)})
            else:
                item["readme_error"] = "no README found"
        else:
            try:
                resp = get(url, timeout=40)
                item["http_status"] = resp.status_code
                text, images = clean(resp.text)
                item.update({"text": text, "images": images})
            except Exception as exc:                           # noqa: BLE001
                item["fetch_error"] = str(exc)
        record["sources"].append(item)
        time.sleep(0.4)
    return record


def main() -> None:
    audit = json.loads((ROOT / "data/benchmark_project_audit.json").read_text(encoding="utf-8"))["audits"]
    targets = [a for a in audit if a["status"] in ("found", "platform_only", "candidate")]
    previous = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    done = previous.get("entries", {})
    payload = {"fetched_at": time.strftime("%Y-%m-%d"),
               "note": "Local cache of project landing pages and READMEs; not a substitute for reading the code.",
               "entries": done}
    for audit_row in targets:
        name = audit_row["benchmark"]
        if name in done and done[name].get("sources"):
            continue
        try:
            payload["entries"][name] = fetch_entry(audit_row)
            got = sum(1 for s in payload["entries"][name]["sources"] if s.get("text"))
            print("ok   %-30s %d/%d sources with text" % (name, got, len(payload["entries"][name]["sources"])))
        except Exception as exc:                               # noqa: BLE001
            payload["entries"][name] = {"benchmark": name, "status": audit_row["status"],
                                        "sources": [], "error": str(exc)}
            print("fail %-30s %s" % (name, exc))
        CACHE.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("cached %d entries -> %s" % (len(payload["entries"]), CACHE))


if __name__ == "__main__":
    main()
