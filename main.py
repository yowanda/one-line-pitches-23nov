"""Write one original one-line pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, no network, no input files: the pitch is embedded below.
"""
import os
from pathlib import Path

PITCH = (
    "Just tell me your app idea in plain words and let an AI agent on "
    "make.fun build a working first version for you \u2014 no code, nothing "
    "to install, and you can watch it take shape and stop it anytime."
)


def main() -> None:
    if not 1 <= len(PITCH) <= 240:
        raise ValueError(f"pitch must be 1-240 characters, got {len(PITCH)}")
    if not PITCH.strip():
        raise ValueError("pitch must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(PITCH.encode("utf-8"))


if __name__ == "__main__":
    main()
