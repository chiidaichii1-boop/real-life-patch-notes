"""One-line patch note for a real-life bug: the bladder only warns you
once the meeting has already started. Written in dry release-note tone."""

import os

NOTE = "v2.7.3: fixed a bug where the bladder waited until the meeting started to send its low-battery warning."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
