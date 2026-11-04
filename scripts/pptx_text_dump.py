# -*- coding: utf-8 -*-
"""Dump the visible text of a .pptx slide by slide into Markdown.

Reads the OOXML directly (no python-pptx). Text is grouped by text body (table cell or text box),
in document order, and the soft line breaks a generator may have written are folded back so the
Markdown stays readable.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

KICKER = re.compile(r"^\d{2}\s*/\s*")
PAGENO = re.compile(r"^\d{2}$")
CJK = r"\u2e80-\u9fff\uff00-\uffef\u3000-\u303f"


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def fold(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"(?<=[" + CJK + r"])\s+(?=[" + CJK + r"])", "", text)


def text_groups(root):
    """One entry per text body, in document order."""
    groups = []

    def walk(node):
        if local(node.tag) == "txBody":
            paras = []
            for para in node.iter():
                if local(para.tag) != "p":
                    continue
                text = fold("".join(t.text or "" for t in para.iter() if local(t.tag) == "t"))
                if text:
                    paras.append(text)
            if paras:
                groups.append(fold(" ".join(paras)))
            return
        for child in node:
            walk(child)

    walk(root)
    return groups


def dump(pptx: Path, out: Path, title: str) -> int:
    with zipfile.ZipFile(pptx) as z:
        slides = sorted((n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
                        key=lambda n: int(re.search(r"(\d+)", n).group(1)))
        lines = ["# " + title, "",
                 "来源：`%s`。按幻灯片顺序抽取可见文字（表格按单元格、文本框按段落合并），供不打开 PPT 时核对。"
                 % pptx.name, ""]
        for idx, name in enumerate(slides, 1):
            groups = [g for g in text_groups(ET.fromstring(z.read(name))) if not PAGENO.fullmatch(g)]
            heading = next((g for g in groups if not KICKER.match(g)), groups[0] if groups else "第 %d 页" % idx)
            lines += ["## %d. %s" % (idx, heading), ""]
            for value in groups:
                if value != heading:
                    lines.append(("- " if len(value) < 48 else "") + value)
            lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return len(slides)


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("usage: pptx_text_dump.py <deck.pptx> <out.md> [title]")
    deck, out = Path(sys.argv[1]), Path(sys.argv[2])
    title = sys.argv[3] if len(sys.argv) > 3 else deck.stem + " · 逐页文字稿"
    print("dumped %d slides -> %s" % (dump(deck, out, title), out.name))


if __name__ == "__main__":
    main()
