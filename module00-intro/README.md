# Module 00: Welcome to the browser simulator

**Kind:** `intro` · Dual-track course welcome

← Start · [Course README](../README.md) · [UI tour →](../module01-hdl-sim-tour/README.md)

## What this course is

**learn_hdl_simulator** is the guided path for the public
[HDL Simulator](https://universal-verification-methodology.github.io/systemverilog-simulator/).
Browser `hdl-sim-*` labs teach IDE workflow; the live simulator is the practice surface.

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Public simulator** | Live IDE: Files / Hierarchy / Signals / Wave / Console | Muscle memory in a real session |
| **B — Browser literacy** | Platform `hdl-sim-*` concept labs | Tour, poke/force, waves, multi-file, golden compare |

Sibling courses: **learn_verilog**, **learn_iverilog**, **learn_verilator**.

## Setup (Track A)

1. Open the [HDL Simulator](https://universal-verification-methodology.github.io/systemverilog-simulator/) in a modern browser.
2. Optional: keep a tiny counter / TB sketch ready from **learn_verilog**.
3. Open this repo at `courses/learn_hdl_simulator`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html#hdl-simulator
3. Start with [`hdl-sim-tour`](http://127.0.0.1:8080/tools/hdl-sim-tour/index.html).

## How to move through modules

1. Read the module **README** (outcomes).
2. Prefer Track B for literacy, then try the same idea in the public IDE (Track A).
3. Check off **CHECKLIST.md**.
4. Expand `transcript.md` / regenerate media with **module-slides** when recording.

## Media (module-slides ready)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript | [transcript.md](transcript.md) |
| Slides / video | generate with **module-slides** |

## Next

→ [Module 01: UI tour](../module01-hdl-sim-tour/README.md)
