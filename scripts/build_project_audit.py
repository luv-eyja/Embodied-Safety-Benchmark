"""Build an audit of official benchmark project URLs.

The audit deliberately distinguishes a benchmark's own project/code page from
the platform it happens to use (for example, LIBERO, CARLA or nuScenes).
"""
from __future__ import annotations

import concurrent.futures
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARDS = json.loads((ROOT / "data/benchmark_cards.json").read_text(encoding="utf-8"))["cards"]

# These are explicit project/platform pages checked against official search
# results or the benchmark paper. `platform_only` means no independent page was
# confirmed for this benchmark, but the underlying platform has a canonical
# page that is useful for reproduction.
MANUAL = {
    "ASIMOV Benchmark": ("found", ["https://asimov-benchmark.github.io/"], "Official ASIMOV Benchmark project page."),
    "ForesightSafety-VLA": ("found", ["https://github.com/tuotuoLyu/ForesightSafety-VLA"], "GitHub repository found by exact benchmark-title search."),
    "ManiPhysicsBench": ("candidate", ["https://github.com/sangwu99/ManiPhysicsBench_Arxiv"], "Repository matches the benchmark title, but the paper page does not link it explicitly."),
    "RoboHarm": ("candidate", ["https://github.com/robocurve/roboharm"], "Repository matches the benchmark title, but authorship/official status needs confirmation."),
    "SafeStage": ("candidate", ["https://github.com/reeta-042/safestage"], "Repository matches the title but is not confirmed as an official author repository."),
    "AgiBot World": ("found", ["https://agibot-world.com/", "https://github.com/OpenDriveLab/AgiBot-World"], "Official project site and code repository."),
    "BEHAVIOR-1K": ("platform_only", ["https://behavior.stanford.edu/"], "Canonical BEHAVIOR platform page; no separate project page for the registry entry was confirmed."),
    "CALVIN": ("platform_only", ["https://calvin-robot.github.io/", "https://github.com/mees/calvin"], "Canonical CALVIN project/code page."),
    "LIBERO（基础套件）": ("platform_only", ["https://libero-project.github.io/main.html"], "Canonical LIBERO project page."),
    "ManiSkill / ManiSkill2": ("platform_only", ["https://maniskill2.github.io/"], "Canonical ManiSkill2 project page."),
    "Open X-Embodiment": ("platform_only", ["https://robotics-transformer-x.github.io/", "https://github.com/google-deepmind/open_x_embodiment"], "Canonical OXE project/code pages."),
    "RoboCasa": ("platform_only", ["https://robocasa.ai/"], "Canonical RoboCasa project page."),
    "RoboCasa365": ("platform_only", ["https://robocasa.ai/"], "Canonical RoboCasa project page hosts RoboCasa365."),
    "RoboTwin": ("platform_only", ["https://robotwin-platform.github.io/", "https://github.com/robotwin-Platform/robotwin"], "Canonical RoboTwin Platform pages."),
    "SimplerEnv": ("platform_only", ["https://simpler-env.github.io/"], "Canonical SimplerEnv project page."),
    "VLABench": ("platform_only", ["https://vlabench.github.io/"], "Canonical VLABench project page."),
    "CARLA / CARLA Leaderboard": ("platform_only", ["https://carla.org/", "https://github.com/carla-simulator/carla"], "Canonical CARLA simulator pages; leaderboard-specific project page not confirmed."),
    "NAVSIM": ("found", ["https://github.com/autonomousvision/navsim"], "Official NAVSIM repository."),
    "nuScenes": ("platform_only", ["https://www.nuscenes.org/"], "Canonical nuScenes dataset/evaluation page."),
}

GENERIC_HOSTS = {
    "arxiv.org", "doi.org", "huggingface.co", "bibsonomy.org", "reddit.com",
    "www.bibsonomy.org", "www.reddit.com", "schema.org", "creativecommons.org",
}


def paper_id(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9.]+)", url or "")
    return m.group(1) if m else None


def clean_url(url: str) -> str:
    return html.unescape(url).rstrip(".,);/ ")


def arxiv_candidates(card: dict) -> tuple[str, list[str], str]:
    aid = paper_id(card.get("source_link", ""))
    if not aid:
        return "not_arxiv", [], "The registry source is a DOI/publisher URL; no arXiv project links were available."
    try:
        request = urllib.request.Request(
            f"https://arxiv.org/abs/{aid}",
            headers={"User-Agent": "Embodied-Safety-Benchmark project audit/1.0"},
        )
        body = urllib.request.urlopen(request, timeout=25).read().decode("utf-8", "ignore")
    except Exception as exc:  # pragma: no cover - network-dependent
        return "fetch_error", [], type(exc).__name__

    found: list[str] = []
    # Both href attributes and plain URLs occur in arXiv comments/metadata.
    values = re.findall(r"(?:href|content)=[\"']([^\"']+)[\"']|(?:https?://[^\s\"'<>]+)", body, re.I)
    for value in values:
        if isinstance(value, tuple):
            value = next((v for v in value if v), "")
        if not value.startswith("http"):
            continue
        url = clean_url(value)
        parsed = urllib.parse.urlparse(url)
        host = parsed.netloc.lower()
        path = parsed.path.lower()
        if host in GENERIC_HOSTS or host.endswith("arxiv.org"):
            continue
        is_project = (
            "github.com" in host
            or "gitlab.com" in host
            or "gitee.com" in host
            or host.endswith(".github.io")
            or "project" in path
            or "code" in path
            or "dataset" in path
        )
        if is_project and url not in found:
            found.append(url)
    return "arxiv_abs", found, f"Project/code links extracted from arXiv abs page {aid}."


def audit_card(card: dict) -> dict:
    name = card["name"]
    if name in MANUAL:
        status, urls, note = MANUAL[name]
        return {
            "benchmark": name,
            "status": status,
            "project_url": urls[0] if urls else None,
            "project_urls": urls,
            "discovery": "manual_official_or_platform_check",
            "paper_url": card.get("source_link"),
            "note": note,
        }
    status, urls, note = arxiv_candidates(card)
    if urls:
        return {
            "benchmark": name,
            "status": "found",
            "project_url": urls[0],
            "project_urls": urls,
            "discovery": status,
            "paper_url": card.get("source_link"),
            "note": note,
        }
    return {
        "benchmark": name,
        "status": "not_found",
        "project_url": None,
        "project_urls": [],
        "discovery": status,
        "paper_url": card.get("source_link"),
        "note": "截至审计日期，未从论文项目链接中确认独立项目地址；需后续继续检索作者主页、代码仓库和数据发布页。",
    }


def main() -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        audits = list(executor.map(audit_card, CARDS))
    audits.sort(key=lambda x: x["benchmark"])
    counts = {s: sum(a["status"] == s for a in audits) for s in ["found", "platform_only", "candidate", "not_found"]}
    out = {
        "schema_version": 1,
        "generated_by": "scripts/build_project_audit.py",
        "audit_date": "2026-11-01",
        "scope": "122 benchmark entries in data/benchmark_cards.json",
        "status_definition": {
            "found": "论文项目链接或官方项目/代码页已确认",
            "platform_only": "只确认到依托平台的官方地址，未确认该条目的独立项目页",
            "candidate": "找到名称匹配的仓库，但尚未确认官方归属",
            "not_found": "本轮检索未确认项目地址",
        },
        "counts": counts,
        "audits": audits,
    }
    (ROOT / "data/benchmark_project_audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Benchmark 项目地址审计",
        "",
        "审计范围：`data/benchmark_cards.json` 中的 122 个 benchmark；审计日期：2026-11-01。",
        "本表区分 benchmark 自己的项目地址和它依托的平台地址，避免把 LIBERO、CARLA、nuScenes 等基础平台误当成每个派生 benchmark 的独立项目。",
        "",
        "| 状态 | 含义 | 数量 |",
        "|---|---|---:|",
        f"| `found` | 已确认论文项目链接或官方项目/代码页 | {counts['found']} |",
        f"| `platform_only` | 只有依托平台地址 | {counts['platform_only']} |",
        f"| `candidate` | 名称匹配但官方归属待确认 | {counts['candidate']} |",
        f"| `not_found` | 本轮未确认项目地址 | {counts['not_found']} |",
        "",
        "## 全量清单",
        "",
        "| Benchmark | 状态 | 项目地址 | 论文来源 | 发现方式 / 备注 |",
        "|---|---|---|---|---|",
    ]
    for a in audits:
        project = "、".join(f"[{u}]({u})" for u in a["project_urls"]) if a["project_urls"] else "—"
        paper = f"[论文]({a['paper_url']})" if a.get("paper_url") else "—"
        lines.append(f"| {a['benchmark']} | `{a['status']}` | {project} | {paper} | {a['discovery']}；{a['note']} |")
    lines += [
        "",
        "## 判定边界",
        "",
        "- `found` 只表示地址已找到，不表示已逐项验证代码、数据和论文版本完全一致。",
        "- `platform_only` 可以作为复现入口，但不能证明该 benchmark 有独立维护的项目仓库。",
        "- `candidate` 不纳入正式来源统计；需要作者主页、论文项目页或仓库 README 的明确关联后再升级为 `found`。",
        "- `not_found` 表示本轮没有确认到地址，并不证明项目绝对不存在；论文只有 DOI、项目未公开或搜索引擎未收录时都可能出现这种结果。",
        "",
    ]
    (ROOT / "analysis/benchmark-project-audit.md").write_text("\n".join(lines), encoding="utf-8")

    # Add a concise, machine-readable marker to every benchmark card. This is
    # additive and preserves the existing generated card fields.
    cards_path = ROOT / "data/benchmark_cards.json"
    cards_obj = json.loads(cards_path.read_text(encoding="utf-8"))
    by_name = {a["benchmark"]: a for a in audits}
    for card in cards_obj["cards"]:
        a = by_name[card["name"]]
        card["project_audit"] = {
            "status": a["status"],
            "project_url": a["project_url"],
            "project_urls": a["project_urls"],
            "audit_date": out["audit_date"],
        }
    cards_path.write_text(json.dumps(cards_obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Mark each generated benchmark document at the top. Keep the catch-all
    # protocol document untouched because it is not a benchmark entry.
    doc_by_name = {card["name"]: card["document"] for card in cards_obj["cards"]}
    for name, filename in doc_by_name.items():
        path = ROOT / "benchmarks" / filename
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        marker = "**项目地址审计**"
        if marker in content:
            continue
        a = by_name[name]
        if a["project_urls"]:
            project_text = "；".join(f"[{u}]({u})" for u in a["project_urls"])
        elif a["status"] == "not_found":
            project_text = "未查到可确认的官方项目地址（详见 [项目地址审计](../analysis/benchmark-project-audit.md)）"
        else:
            project_text = "—"
        insert = f"\n> **项目地址审计**：`{a['status']}`；{project_text}\n"
        lines = content.splitlines(keepends=True)
        idx = 0
        while idx < len(lines) and not lines[idx].startswith("> **证据级别**"):
            idx += 1
        if idx < len(lines):
            lines.insert(idx + 1, insert)
            path.write_text("".join(lines), encoding="utf-8")

    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()

