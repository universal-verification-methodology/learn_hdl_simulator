#!/usr/bin/env python3
"""Capture lab/tools snapshots for learn_hdl_simulator."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / ".cursor/skills/module-slides/scripts/capture_lab_snapshot.py"
BASE = "http://127.0.0.1:8080/tools"
COURSE = ROOT / "courses/learn_hdl_simulator"

CAPTURES = [
    ("module00-intro", "index", "tools-index.png"),
    ("module01-hdl-sim-tour", "hdl-sim-tour", None),
    ("module02-hdl-sim-hello-dut", "hdl-sim-hello-dut", None),
    ("module03-hdl-sim-step-continue", "hdl-sim-step-continue", None),
    ("module04-hdl-sim-poke-force", "hdl-sim-poke-force", None),
    ("module05-hdl-sim-waves", "hdl-sim-waves", None),
    ("module06-hdl-sim-multi-file", "hdl-sim-multi-file", None),
    ("module07-hdl-sim-compare-golden", "hdl-sim-compare-golden", None),
    ("module08-style-synth-bridge", "hdl-style", None),
    ("module10-wrap", "index", "tools-index.png"),
]


def main() -> int:
    rc = 0
    for slug, lab, name in CAPTURES:
        mod = COURSE / slug
        cmd = [
            sys.executable,
            str(SCRIPT),
            str(mod.relative_to(ROOT)).replace("\\", "/"),
            "--lab",
            lab,
            "--base",
            BASE,
            "--wait-ms",
            "2000",
            "--height",
            "900",
        ]
        if name:
            cmd.extend(["--name", name])
        print(f"\n=== {slug} ({lab}) ===")
        r = subprocess.run(cmd, cwd=ROOT).returncode
        if r != 0:
            rc = r
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
