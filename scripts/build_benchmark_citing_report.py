# -*- coding: utf-8 -*-
"""Render the citing-works data into a readable report, without re-querying the network."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INLINE_LIMIT = 8


def cell(value) -> str:
    return (str(value or "").replace("|", "／").replace("\n", " ")).strip()


def load(name):
    return json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))


def link(work) -> str:
    if work.get("doi"):
        return "[%s](%s)" % (cell(work.get("title")), work["doi"])
    return "[%s](https://openalex.org/%s)" % (cell(work.get("title")), work.get("id"))


def span(by_year: dict) -> str:
    years = sorted(y for y in by_year if y.isdigit())
    if not years:
        return "—"
    return years[0] if len(years) == 1 else "%s–%s" % (years[0], years[-1])


def main() -> None:
    data = load("benchmark_citing_works.json")
    snapshot = load("benchmark_citation_snapshot.json")
    counts = {e["benchmark"]: e for e in snapshot["entries"]}
    entries = data["entries"]
    cited = [e for e in entries if (e.get("cites") or {}).get("total")]
    mentioned_only = [e for e in entries if not (e.get("cites") or {}).get("total")
                      and (e.get("mentioned") or {}).get("total")]
    silent = [e for e in entries if not (e.get("cites") or {}).get("total")
              and not (e.get("mentioned") or {}).get("total")]
    failed = [e for e in entries if e.get("status") != "matched"]

    L = ["# 引用了这些 Benchmark 的论文：清单与口径", "",
         "> 观测日期 %s。结构化清单：[benchmark_citing_works.json](../data/benchmark_citing_works.json)；"
         "计数来源：[引用快照](../data/benchmark_citation_snapshot.json)。" % data["generated_at"], "",
         "范围为主目录 **%d 个已分类条目**，每条只取一个选定论文记录（预印本与正式版不合并、不相加）。"
         "本文件由 `scripts/build_benchmark_citing_report.py` 从上述 JSON 渲染，数字与清单同源。" % len(entries), "",
         "## 1. 三个不同的数字", "",
         "| 字段 | 含义 | 不能推出 |", "|---|---|---|",
         "| `cited_by_count` | OpenAlex 在该 Work 记录上统计的被引次数 | Google Scholar／Scopus 的数值相同；benchmark 被独立采用 |",
         "| `cites` 清单 | OpenAlex 引文图中把本记录列为参考文献的论文 | 参考文献解析完整；只“提到名字”的论文也在其中 |",
         "| `mentioned` | 全文检索出现 benchmark 名字的论文 | 该论文引用了原论文；该论文用了这个 benchmark |", "",
         "三个数字来自同一数据库的不同接口，收录延迟和解析错误同时存在。**未查到不等于没人引用**，"
         "0 只是该记录在观测时的计数。引用数也不等于独立采用：作者自用、只做背景引用、"
         "和真正在该 benchmark 上跑实验是不同强度的证据，本文件不替读者下这个结论。", "",
         "## 2. 总览", "",
         "| 条目 | 被引 | 引文年份 | 已列/总引文 | 全文提及 | 状态 |", "|---|---:|---|---:|---:|---|"]

    for e in sorted(entries, key=lambda x: ((x.get("cites") or {}).get("total") or -1), reverse=True):
        c = e.get("cites") or {}
        m = e.get("mentioned") or {}
        listed = "%s/%s" % (c.get("listed", 0), c.get("total")) if c.get("total") is not None else "—"
        if e.get("status") != "matched":
            state = "记录未匹配"
        elif c.get("total") is None:
            state = "引文查询失败"
        elif not c.get("total"):
            state = "无引文" if m.get("total") else "无引文、无提及"
        else:
            state = "有引文" if c.get("complete") else "有引文（列表为前 %d 条）" % c.get("listed", 0)
        L.append("| [%s](../benchmarks/%s) | %s | %s | %s | %s | %s |" % (
            cell(e["benchmark"]), e["document"],
            counts.get(e["benchmark"], {}).get("openalex", {}).get("cited_by_count")
            if counts.get(e["benchmark"], {}).get("openalex", {}).get("status") == "matched" else "未核验",
            span(c.get("by_year") or {}), listed,
            m.get("total") if m.get("total") is not None else "—", state))

    L += ["", "合计：%d 条有至少一篇可列出的引文论文，%d 条只有全文提及、暂无引文，%d 条两者皆无。"
          % (len(cited), len(mentioned_only), len(silent)), "",
          "## 3. 有引文的条目：谁在引用", "",
          "按被引数从高到低。每条列出被引最高的引文（至多 %d 篇），完整列表见 JSON。"
          "“类型”来自 OpenAlex 的 `type` 字段，不是对论文内容的判断。" % INLINE_LIMIT, ""]

    for e in sorted(cited, key=lambda x: x["cites"]["total"] or 0, reverse=True):
        c = e["cites"]
        by_year = c.get("by_year") or {}
        year_text = "、".join("%s 年 %d 篇" % (y, n) for y, n in sorted(by_year.items(), reverse=True)) or "—"
        L += ["### %s（被引 %d）" % (cell(e["benchmark"]), c["total"]), "",
              "来源论文：[%s](%s)；OpenAlex 记录：[%s](https://openalex.org/%s)。引文年份分布：%s。"
              % (cell(e["paper"]), e["source_link"], e["openalex_id"], e["openalex_id"], year_text), ""]
        if c.get("by_year"):
            L += ["| 年份 | " + " | ".join(y for y, _ in sorted(by_year.items(), reverse=True)) + " |",
                  "|---|" + "---:|" * len(by_year),
                  "| 引文数 | " + " | ".join(str(n) for _, n in sorted(by_year.items(), reverse=True)) + " |", ""]
        L += ["| 年份 | 论文 | 类型 | 被引 |", "|---|---|---|---:|"]
        for w in c["works"][:INLINE_LIMIT]:
            L.append("| %s | %s | %s | %s |" % (w.get("year") or "—", link(w),
                                                cell(w.get("type") or "—"), w.get("cited_by_count")))
        if not c["complete"]:
            L += ["", "> 该记录共有 %d 篇引文，这里只列被引最高的 %d 篇；其余见结构化清单。"
                  % (c["total"], c["listed"])]
        elif c["total"] > INLINE_LIMIT:
            L += ["", "> 共 %d 篇，文档内只列 %d 篇，结构化清单中为完整列表。" % (c["total"], c["listed"])]
        L.append("")

    L += ["## 4. 暂无引文、但全文提到该 benchmark 的论文", "",
          "下列论文的全文出现该 benchmark 名字，但 OpenAlex 引文图尚未把源论文记为其参考文献。"
          "可能是新论文的引文解析延迟、参考文献格式问题，也可能只是提到名字而未引用。"
          "这些条目是**最值得先手工核对**的候选，不能直接记为“已引用”。", ""]
    if not mentioned_only:
        L.append("（无）")
    for e in sorted(mentioned_only, key=lambda x: (x.get("mentioned") or {}).get("total") or 0, reverse=True):
        m = e["mentioned"]
        L += ["### %s（全文提及 %s 篇；命名词：`%s`）" % (cell(e["benchmark"]), m.get("total"), m.get("query")), "",
              "来源论文：[%s](%s)。" % (cell(e["paper"]), e["source_link"]), "",
              "| 年份 | 论文 | 是否在引文图中 | 类型 |", "|---|---|---|---|"]
        for w in m["works"][:INLINE_LIMIT]:
            flag = {True: "是", False: "否（已核对完整引文列表）", None: "未核对"}[w.get("cites_source")]
            L.append("| %s | %s | %s | %s |" % (w.get("year") or "—", link(w), flag, cell(w.get("type") or "—")))
        if (m.get("total") or 0) > len(m["works"]):
            L += ["", "> 命中 %s 条（含源论文自身时已减 1），此处列被引最高的 %d 条。"
                  % (m.get("total"), len(m["works"]))]
        L.append("")

    L += ["## 5. 两种口径下都没有线索的条目", "",
          "既无 OpenAlex 引文，全文检索也没有命中。多数是 2026 年的新条目，收录与引用都有延迟；"
          "这只是“本轮没查到”，不是“无人使用”。", ""]
    if silent:
        L += ["| 条目 | 来源论文 | 观测 |", "|---|---|---|"]
        for e in silent:
            L.append("| [%s](../benchmarks/%s) | %s | %s |" % (cell(e["benchmark"]), e["document"],
                                                              cell(e["paper"]),
                                                              "记录未匹配" if e.get("status") != "matched" else "被引 0，无提及"))
    else:
        L.append("（无）")

    if failed:
        L += ["", "未匹配到记录的条目：%s。这些条目的计数留空，不按 0 处理。"
              % "、".join(cell(e["benchmark"]) for e in failed)]

    errors = [(e["benchmark"], err) for e in entries for err in e.get("errors") or []]
    L += ["", "## 6. 查询记录与后续", "",
          "查询接口与参数见 JSON 的 `queries`／`errors` 字段；所有计数均为单条记录的单一观测，"
          "跨日期比较时须带上观测日期。", ""]
    if errors:
        L += ["本轮失败的查询（对应字段留空，不当 0）：", "",
              "| 条目 | 通道 | 错误 |", "|---|---|---|"]
        L += ["| %s | %s | %s |" % (cell(b), cell(x["channel"]), cell(x["error"])[:120]) for b, x in errors]
        L.append("")
    L += ["后续若要把它升级为“采用审计”，需要逐篇打开引文论文，记录实验章节／表格、所用任务版本、"
          "作者与原团队的关系，以及是运行基准还是仅引用。当前清单只提供入口，不提供这个结论。", ""]

    (ROOT / "analysis/benchmark-citing-papers.md").write_text("\n".join(L), encoding="utf-8")
    print("Wrote analysis/benchmark-citing-papers.md; cited=%d mentioned_only=%d silent=%d"
          % (len(cited), len(mentioned_only), len(silent)))


if __name__ == "__main__":
    main()
