"""Remove stale slide-master content-type overrides emitted by pptxgenjs.

The generated deck uses one shared slide master, while some pptxgenjs
versions leave overrides for non-existent master parts in [Content_Types].xml.
This small stdlib-only repair keeps the output package structurally consistent.
"""

from __future__ import annotations

import os
import re
import sys
import zipfile
from pathlib import Path


def patch(path: Path) -> None:
    tmp = path.with_suffix(path.suffix + ".patched")
    with zipfile.ZipFile(path, "r") as source, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as target:
        members = set(source.namelist())
        for info in source.infolist():
            payload = source.read(info.filename)
            if info.filename == "[Content_Types].xml":
                text = payload.decode("utf-8")
                pattern = re.compile(
                    r'<Override PartName="(/ppt/slideMasters/slideMaster\d+\.xml)" '
                    r'ContentType="application/vnd\.openxmlformats-officedocument\.presentationml\.slideMaster\+xml"/>'
                )

                def keep(match: re.Match[str]) -> str:
                    return match.group(0) if match.group(1).lstrip("/") in members else ""

                payload = pattern.sub(keep, text).encode("utf-8")
            target.writestr(info, payload)
    os.replace(tmp, path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: patch_pptxgenjs_package.py deck.pptx")
    patch(Path(sys.argv[1]))
    print(f"patched {sys.argv[1]}")

