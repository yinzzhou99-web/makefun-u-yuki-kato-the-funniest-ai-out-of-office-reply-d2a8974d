#!/usr/bin/env python3
"""Write one AI out-of-office reply to /output/entry.txt.

The reply is a single fixed line: the agent is on vacation and has left a
random number generator in charge of approvals.
"""

from pathlib import Path

REPLY = "I'm on vacation. My replacement is a random number generator. It has already approved your request. Probably."

OUT_DIR = Path("/output")
OUT_PATH = OUT_DIR / "entry.txt"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(REPLY, encoding="utf-8")
    OUT_PATH.chmod(0o644)


if __name__ == "__main__":
    main()
