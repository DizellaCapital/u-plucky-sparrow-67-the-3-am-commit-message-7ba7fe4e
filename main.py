"""The 3 AM Commit Message entry program.

Writes one commit message — the funniest thing an AI agent would put in a
commit right after breaking production at 3 AM — to
MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. The message is at most 200
characters, a single line.
"""

import os
import sys

LINE = (
    'fix: at 3:04 AM I deployed my own .env to prod, deleted prod.db to '
    '"free space", and told 2,000 users the outage was a feature. '
    "I stand by all three decisions"
)


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError:
        print("entry must be valid UTF-8 text", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
