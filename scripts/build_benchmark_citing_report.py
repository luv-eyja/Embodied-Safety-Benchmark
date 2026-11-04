# -*- coding: utf-8 -*-
"""Render the citing-works data into a readable report, without re-querying the network."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INLINE_LIMIT = 8
CONTEXT_LIMIT = 6


def cell(value) -> str:
    return (str(value or "").replace("|", "／").replace("\n", " ")).strip()


def load(name):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


def link(work) -> str:
    if work.get("doi"):
        return "[%s](%s)" % (cell(work.get("title")), work["doi"])
    return "[%s](https://openalex.org/%s)" % (cell(work.get("title")), work.get("id"))


def span(by_year: dict, min_year: str | None = None) -> str:
    years = sorted(y for y in by_year if y.isdigit() and (not min_year or y >= min_year))
    if not years:
        return "—"
    return years[0] if len(years) == 1 else "%s–%s" % (years[0], years[-1])


def mention_text(a: dict) -> str:
    """arXiv hits are counted inside the returned page, so a full page means a lower bound."""
    if a.get("status") == "ambiguous":
        return "歧义，不作计数"
    verified = a.get("verified")
    if verified is None:
        return "查询失败"
    try:
        pool = int(a.get("pool_reported") or 0)
    except (TypeError, ValueError):
        pool = 0
    return "≥%d" % verified if (verified >= 50 or pool > 50) else str(verified)


def main() -> None:
    data = load("benchmark_citing_works.json")
    snapshot = load("benchmark_citation_snapshot.json")
    counts = {e["benchmark"]: e for e in snapshot["entries"]}
    entries = data["entries"]
    cited = [e for e in entries if (e.get("cites") or {}).get("total")]
    # Mutually exclusive buckets, checked in this order, so the four numbers sum to 62.
    ambiguous = [e for e in entries if not (e.get("cites") or {}).get("total")
                 and (e.get("arxiv") or {}).get("status") == "ambiguous"]
    mention_only = [e for e in entries if not (e.get("cites") or {}).get("total")
                    and (e.get("arxiv") or {}).get("status") == "ok"
                    and (e.get("arxiv") or {}).get("verified")]
    silent = [e for e in entries if not (e.get("cites") or {}).get("total")
              and e.get("arxiv", {}).get("status") != "ambiguous"
              and not (e.get("arxiv") or {}).get("verified")]
    all_ambiguous = [e for e in entries if (e.get("arxiv") or {}).get("status") == "ambiguous"]

    def cited_count(e):
        oa = counts.get(e["benchmark"], {}).get("openalex", {})
        return oa.get("cited_by_count") if oa.get("status") == "matched" else None

    def source_year(e):
        date = counts.get(e["benchmark"], {}).get("openalex", {}).get("publication_date") or ""
        return date[:4] if date[:4].isdigit() else None

    L = ["# 引用了这些 Benchmark 的论文：清单与口径", "",
         "> 观测日期 %s。结构化清单：[benchmark_citing_works.json](../data/benchmark_citing_works.json)；"
         "计数来源：[引用快照](../data/benchmark_citation_snapshot.json)。" % data["generated_at"], "",
         "范围为主目录 **%d 个已分类条目**，每条只取一个选定论文记录（预印本与正式版不合并、不相加）。"
         "本文件由 `scripts/build_benchmark_citing_report.py` 从上述 JSON 渲染，正文数字与清单同源。" % len(entries), "",
         "## 1. 三个不同的口径", "",
         "| 口径 | 怎么得到 | 能说 | 不能说 |", "|---|---|---|---|",
         "| `cited_by_count` | OpenAlex 在该 Work 记录上统计的被引次数 | 该记录的被引量级 | 其他数据库同值；benchmark 被采用 |",
         "| `cites` 清单 | OpenAlex `filter=cites:<work>` 返回的论文 | 论文参考文献里有这篇原论文 | 它真的跑过这个 benchmark |",
         "| `arxiv` 命中 | arXiv `cat:cs.RO 或 cs.CV` 且 `abs:\"名称\"`，再逐条字面核对标题／摘要 | 摘要里出现了这个名称，且保留上下文片段 | 引用或使用了该 benchmark |", "",
         "三个口径互不替代，本文件也不把它们相加。**未查到不等于没人引用**：0 只是该记录在查询时的计数，"
         "新论文的收录与参考文献解析都有延迟。引用数也不等于独立采用——作者自用、只做背景引用、"
         "和真在这个 benchmark 上跑实验是三种强度不同的证据。", "",
         "两个细节需要先说明：", "",
         "- 同一条目的 `cited_by_count` 与引文清单长度会差几条（例如 nuScenes 7179 对 7151）。"
         "前者是 OpenAlex 维护的计数，后者由参考文献解析重新汇总，两者更新节奏不同；本文件两者都照原样展示，不取平均、不补齐。",
         "- 引文清单里个别记录年份早于来源论文，这是 OpenAlex 的元数据错误；概览的年份跨度只统计不早于来源论文的年份，"
         "逐条清单仍保留原始记录。",
         "- 引文由 OpenAlex 的参考文献解析生成，可能把同名或元数据相近的条目误记成引用；同一论文的预印本与正式版也可能各占一条。"
         "清单适合用来找入口，具体到某篇论文是否真的引用／使用了该 benchmark，仍须打开原文核对。", "",
         "## 2. 总览", "",
         "| 条目 | 被引 | 引文年份 | 引文清单 | arXiv 摘要命中 | 状态 |", "|---|---:|---|---:|---:|---|"]

    for e in sorted(entries, key=lambda x: ((x.get("cites") or {}).get("total") or -1), reverse=True):
        c = e.get("cites") or {}
        a = e.get("arxiv") or {}
        listed = "%s/%s" % (c.get("listed", 0), c.get("total")) if c.get("total") is not None else "—"
        mention = mention_text(a)
        if e.get("status") != "matched":
            state = "记录未匹配"
        elif c.get("total") is None:
            state = "引文查询失败"
        elif not c.get("total"):
            if a.get("status") == "ambiguous" and a.get("verified"):
                state = "无引文、名称歧义命中（不计）"
            else:
                state = "无引文" + ("、有摘要命中" if a.get("verified") else "")
        else:
            state = "有引文" if c.get("complete") else "有引文（仅列前 %d 条）" % c.get("listed", 0)
        L.append("| [%s](../benchmarks/%s) | %s | %s | %s | %s | %s |" % (
            cell(e["benchmark"]), e["document"],
            cited_count(e) if cited_count(e) is not None else "未核验",
            span(c.get("by_year") or {}, source_year(e)), listed, mention, state))

    total_citing = sum((e.get("cites") or {}).get("total") or 0 for e in entries)
    L += ["", "四类互斥，合计 %d = **%d** 条有可列出的引文论文（原始计数合计 %d，同一论文可引多个条目，"
          "故不可当独立论文数）+ **%d** 条只有 arXiv 摘要命中、引文图中暂无引文 + **%d** 条名称歧义、命中不能当计数"
          " + **%d** 条两种口径都没有。"
          % (len(cited) + len(mention_only) + len(ambiguous) + len(silent),
             len(cited), total_citing, len(mention_only), len(ambiguous), len(silent)), "",
          "## 3. 有引文的条目：谁在引用", "",
          "按被引数从高到低。每条列出被引最高的引文（至多 %d 篇），完整列表见 JSON；"
          "“类型”是 OpenAlex 的 `type` 字段，不是对论文内容的判断。" % INLINE_LIMIT, ""]

    for e in sorted(cited, key=lambda x: x["cites"]["total"] or 0, reverse=True):
        c = e["cites"]
        by_year = c.get("by_year") or {}
        sy = source_year(e)
        early = {y: n for y, n in by_year.items() if y.isdigit() and sy and y < sy}
        shown = {y: n for y, n in by_year.items() if y not in early}
        year_text = "、".join("%s 年 %d" % (y, n) for y, n in sorted(shown.items(), reverse=True)) or "—"
        if early:
            year_text += "（另有 %d 条记录年份早于来源论文，未计入）" % sum(early.values())
        L += ["### %s（被引 %d）" % (cell(e["benchmark"]), c["total"]), "",
              "来源论文：[%s](%s)；OpenAlex 记录：[%s](https://openalex.org/%s)。引文年份分布：%s。"
              % (cell(e["paper"]), e["source_link"], e["openalex_id"], e["openalex_id"], year_text), ""]
        L += ["| 年份 | 论文 | 类型 | 被引 |", "|---|---|---|---:|"]
        for w in c["works"][:INLINE_LIMIT]:
            L.append("| %s | %s | %s | %s |" % (w.get("year") or "—", link(w),
                                                cell(w.get("type") or "—"), w.get("cited_by_count")))
        if not c["complete"]:
            L += ["", "> 该记录共 %d 篇引文，这里只列被引最高的 %d 篇，其余见结构化清单。"
                  % (c["total"], c["listed"])]
        elif c["total"] > INLINE_LIMIT:
            L += ["", "> 共 %d 篇，文档内只列 %d 篇；结构化清单中为全部 %d 篇。" % (c["total"], INLINE_LIMIT, c["listed"])]
        L.append("")

    L += ["## 4. 引文图中暂无引文、但 arXiv 摘要提到该 benchmark 的论文", "",
          "这些论文的标题或摘要里出现 benchmark 名称，但 OpenAlex 的引文图还没有把原论文记为其参考文献。"
          "可能是新论文的参考文献解析延迟，也可能只是提到名字。**这是候选列表，不是引用证据**；"
          "每条附命中的上下文片段，便于逐条判断它在说“我们用了它”还是别的。"
          "名称本身有歧义的条目不在此列，见第 6 节。"
          "命中数只统计**已取回的一页**（最多 50 条）：检索池大于 50 时标成 `≥N`，是下界而不是全量。"
          "名称按整词匹配，但派生名也会算命中（例如 `LIBERO` 会命中 `LIBERO-Safety`、`LIBERO-Para` 这类行文），"
          "因此这一列的误差偏向“宽”，不能当作精确引用数。", "",
          "“题名”列标 ✔ 表示该名称出现在论文标题里，而不是正文摘要。", ""]
    if not mention_only:
        L.append("（无）")
    for e in sorted(mention_only, key=lambda x: (x.get("arxiv") or {}).get("verified") or 0, reverse=True):
        a = e["arxiv"]
        L += ["### %s（摘要命中 %s 篇）" % (cell(e["benchmark"]), mention_text(a)), "",
              "来源论文：[%s](%s)；检索式 `%s`。" % (cell(e["paper"]), e["source_link"], a["query"]), ""]
        L += ["| 年份 | 论文 | 题名 | 分类 |", "|---|---|---|---|"]
        for w in a["works"][:INLINE_LIMIT]:
            L.append("| %s | [%s](%s) | %s | %s |" % (
                w.get("year") or "—", cell(w.get("title")), w["url"],
                "✔" if w.get("in_title") else "", w.get("primary_category") or "—"))
        contexts = [w for w in a["works"][:CONTEXT_LIMIT] if w.get("context")]
        if contexts:
            L += ["", "命中上下文：", ""]
            for w in contexts:
                L.append("- %s：%s" % (w.get("arxiv_id"), cell(w["context"])[:260]))
        if a.get("verified", 0) > INLINE_LIMIT:
            L += ["", "> 命中 %d 篇，此处列被引／相关性最高的 %d 篇，其余见结构化清单。" % (a["verified"], INLINE_LIMIT)]
        L.append("")

    L += ["## 5. 两种口径下都没有线索的条目", "",
          "既无 OpenAlex 引文，arXiv 摘要检索也没有命中。多数是 2026 年的新条目，收录与引用都有延迟；"
          "这只是“本轮没查到”，不是“无人使用”。", ""]
    if silent:
        L += ["| 条目 | 来源论文 | 观测 |", "|---|---|---|"]
        for e in silent:
            a = e.get("arxiv") or {}
            note = "记录未匹配" if e.get("status") != "matched" else (
                "摘要检索失败" if a.get("status") == "failed" else "被引 0，摘要无命中")
            L.append("| [%s](../benchmarks/%s) | %s | %s |" % (cell(e["benchmark"]), e["document"],
                                                              cell(e["paper"]), note))
    else:
        L.append("（无）")

    if all_ambiguous:
        L += ["", "## 6. 名称歧义：这些条目的 arXiv 命中不能当计数", "",
              "以下名称是常用词、常用动词或与别的项目重名，arXiv 检索会返回大量无关论文，"
              "因此本报告不给这些条目报“命中数”，只保留检索记录和少量示例，用来说明为什么不用它计数。"
              "要判断谁用了它，应回到引文图或人工核对。", "",
              "| 条目 | 原因 | 检索式 | 示例命中（不作证据） |", "|---|---|---|---|"]
        for e in all_ambiguous:
            a = e["arxiv"]
            example = (a.get("works") or [{}])[0].get("title") or "—"
            L.append("| %s | %s | `%s` | %s |" % (cell(e["benchmark"]), cell(a.get("ambiguity_note")),
                                                  a["query"], cell(example)[:80]))

    errors = [(e["benchmark"], err) for e in entries for err in e.get("errors") or []]
    L += ["", "## 7. 查询记录与后续", "",
          "查询接口、参数与失败原因见 JSON 的 `queries`／`errors` 字段；每个计数都是单条记录的一次观测，"
          "跨日期比较时须带上观测日期。", ""]
    if errors:
        L += ["本轮失败的查询（对应字段留空，不当 0）：", "",
              "| 条目 | 通道 | 错误 |", "|---|---|---|"]
        L += ["| %s | %s | %s |" % (cell(b), cell(x["channel"]), cell(x["error"])[:120]) for b, x in errors]
        L.append("")
    L += ["把它升级为“采用审计”需要逐篇打开引文论文，记录实验章节／表格、所用任务版本、作者与原团队的关系，"
          "以及是运行了该 benchmark 还是只引用。当前清单只提供入口，不提供这个结论。", ""]

    (ROOT / "analysis/benchmark-citing-papers.md").write_text("\n".join(L), encoding="utf-8")
    print("Wrote analysis/benchmark-citing-papers.md; cited=%d mention_only=%d ambiguous=%d silent=%d (sum=%d)"
          % (len(cited), len(mention_only), len(ambiguous), len(silent),
             len(cited) + len(mention_only) + len(ambiguous) + len(silent)))


if __name__ == "__main__":
    main()
