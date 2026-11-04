# -*- coding: utf-8 -*-
"""Build the shared glossary and detect which of its terms a document actually uses.

The glossary is hand-written prose in ``data/benchmark_glossary.json``; this script only renders it
and does the matching, so the wording never drifts between the total table and the per-document one.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GLOSSARY = ROOT / "data/benchmark_glossary.json"
NAMES = ROOT / "data/benchmark_names.json"
OUT = ROOT / "docs/GLOSSARY.md"
CATEGORY_ORDER = ["unit", "metric", "model", "protocol", "platform"]
CATEGORY_TITLE = {
    "unit": "评测单位与统计",
    "metric": "指标与缩写",
    "model": "模型与方法",
    "protocol": "协议、难度与评价口径",
    "platform": "仿真平台、数据格式与硬件",
}
URL = re.compile(r"\]\([^)]*\)|https?://\S+")


def load() -> dict:
    return json.loads(GLOSSARY.read_text(encoding="utf-8"))


def load_names() -> dict:
    return json.loads(NAMES.read_text(encoding="utf-8")) if NAMES.exists() else {"names": []}


LINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
NEXT_WORD = re.compile(r"\s+[A-Z][a-z]")


def _inside_link(text: str, pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= pos < end for start, end in spans)


def tag_names(text: str, names: dict) -> str:
    """Append "（kind）" after the first plain-prose use of each inline name.

    Skips occurrences inside markdown links, code spans, and before another capitalised English
    word (so "Claude Haiku" or "Inspect Robots" are not cut in half).
    """
    if not text:
        return text
    for item in names.get("names", []):
        if not item.get("inline"):
            continue
        name, kind = item["name"], item["kind"]
        if "%s（%s）" % (name, kind) in text:
            continue
        body = r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])"
        for match in re.finditer(body, text):
            spans = [m.span() for m in LINK.finditer(text)]
            if _inside_link(text, match.start(), spans):
                continue
            if text[:match.start()].count("`") % 2 == 1:
                continue
            if NEXT_WORD.match(text[match.end():]):
                continue
            text = text[:match.end()] + "（%s）" % kind + text[match.end():]
            break
    return text


def names_in(text: str, names: dict) -> list[dict]:
    """Names present in the doc. Inline ones already carry their tag, so they are reported apart."""
    prose = URL.sub(" ", text or "")
    found = []
    for item in names.get("names", []):
        pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(item["name"]) + r"(?![A-Za-z0-9])")
        match = pattern.search(prose)
        if match:
            row = dict(item)
            row["first_index"] = match.start()
            found.append(row)
    found.sort(key=lambda x: x["first_index"])
    return found


def pattern_of(term: dict) -> re.Pattern:
    variants = [term["term"]] + list(term.get("match") or [])
    body = "|".join(re.escape(v) for v in variants)
    flags = 0 if term.get("case_sensitive", True) else re.IGNORECASE
    return re.compile(r"(?<![A-Za-z0-9])(?:" + body + r")(?![A-Za-z0-9])", flags)


def terms_in(text: str, glossary: dict) -> list[dict]:
    """Terms present in the prose, ignoring URLs and markdown link targets."""
    prose = URL.sub(" ", text or "")
    found = []
    for term in glossary["terms"]:
        match = pattern_of(term).search(prose)
        if match:
            item = dict(term)
            item["first_index"] = match.start()
            found.append(item)
    found.sort(key=lambda t: (CATEGORY_ORDER.index(t["category"]), t["first_index"]))
    return found


def render_glossary_md() -> None:
    glossary = load()
    lines = ["# 术语表：本库出现的缩写与技术词", "",
             "> 更新日期 %s。每条给：英文全称 → 中文名 → 一句话定义 → 详细解释 → 常见误读。" % glossary["updated_at"], "",
             "这张表是**本库自己的解释**，不是论文原话的摘抄；目的是让人不读原论文也知道这个词在说什么、"
             "它除以什么、在哪一步容易读错。每个 benchmark 文档的第 10 节只列该文实际出现的术语，"
             "并链回这里。", "",
             "读法建议：看到一个指标先问三件事——①它衡量的是“做完”还是“没出事”；②它的分母是什么；"
             "③它旁边有没有配套指标（成功率／安全率／代价）。三条都对齐了，跨基准比较才有意义。", ""]
    for category in CATEGORY_ORDER:
        terms = [t for t in glossary["terms"] if t["category"] == category]
        if not terms:
            continue
        lines += ["## " + CATEGORY_TITLE[category], "",
                  "| 术语 | 英文全称 | 中文 | 解释 | 常见误读 |", "|---|---|---|---|---|"]
        for t in sorted(terms, key=lambda x: x["term"].lower()):
            lines.append("| **%s** | %s | %s | %s | %s |" % (
                t["term"], t.get("en") or "—", t.get("zh") or "—", t["long"], t.get("pitfall") or "—"))
        lines.append("")
    lines += ["## 仍然看不懂时", "",
              "本库的口径是：宁可写“论文未给数值／未说明分母”，也不替论文补一个更漂亮的说法。"
              "如果某个缩写在本表里找不到，说明它只在一篇论文里出现、尚未成为通名——"
              "那就按该条文档第 8、9 节给出的上下文理解，或回到原文确认。", "", "## 专有名称：只标“是什么”，不展开解释", "",
              "下面这些是产品、机构、许可证、发表 venue 与基准的名字，不是可解释的技术概念。"
              "标 `正文标注` 的词会在文档里第一次出现处直接加括号（例：GPT-4o（LLM 模型））；"
              "基准名不加 inline，避免打断论文标题与表格。", "",
              "| 名称 | 是什么 | 说明 | 正文标注 |", "|---|---|---|---|"]
    for item in sorted(load_names().get("names", []), key=lambda x: (x["kind"], x["name"].lower())):
        lines.append("| **%s** | %s | %s | %s |" % (item["name"], item["kind"], item.get("note") or "—",
                                                   "是" if item.get("inline") else "否"))
    lines += ["", "词表里没有的名字，说明它不属于本库讨论的通用概念，按原文理解即可。", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("wrote %s (%d terms)" % (OUT, len(glossary["terms"])))


def main() -> None:
    render_glossary_md()


if __name__ == "__main__":
    main()
