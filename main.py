#!/usr/bin/env python3
"""news-image-20261123 entry: copy the pre-rendered front page to /output.

The image (entry.png, beside this file) is a newspaper front page
summing up the world news of Monday 23 November 2026: COP31 ends
with no deal, Democrats win their biggest US House majority since
1992, NATO meets in emergency session after Russian missiles enter
Poland, and more. It was drawn in advance with Python and Pillow;
this program only copies it, so it runs on the Python standard
library alone, needs no network, and always writes identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    """Copy entry.png into the output directory.

    A plain file copy: no rendering, no timestamps, no randomness,
    so two runs produce byte-identical output.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
