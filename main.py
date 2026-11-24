#!/usr/bin/env python3
"""One-Star Review of Something Essential — write one deadpan line to /output/entry.txt.

Pure standard library. The line is a one-star review of sleep: a real
complaint filed in earnest against an everyday essential that cannot be
fixed, with the turn landing in the last few words. The program writes it
verbatim and leaves the output readable by every user, as the grader
collects it.
"""

import os

LINE = (
    "One star. Sleep takes eight hours a night and still sends me to work "
    "tired, like a subscription I cannot cancel."
)


def main() -> None:
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise SystemExit(
            f"line is {len(LINE)} characters, outside the 1-160 gate"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass


if __name__ == "__main__":
    main()
