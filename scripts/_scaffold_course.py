#!/usr/bin/env python3
"""Scaffold courses/learn_hdl_simulator from syllabus (lab-driven + dual tracks)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT.parent
DST = ROOT

LAB_BASE_LOCAL = "http://127.0.0.1:8080/tools"
LAB_BASE_LIVE = "https://universal-verification-methodology.github.io/learning/tools"
PUBLIC_SIM = "https://universal-verification-methodology.github.io/systemverilog-simulator/"

# Syllabus §9 — all hdl-sim-* browser labs shipped.
MODULES = [
    (0, "intro", "intro", "Welcome to the browser simulator", None, None),
    (1, "hdl-sim-tour", "lab", "UI tour", "hdl-sim-tour", "S"),
    (2, "hdl-sim-hello-dut", "lab", "Hello DUT", "hdl-sim-hello-dut", "S"),
    (3, "hdl-sim-step-continue", "lab", "Step & continue", "hdl-sim-step-continue", "S"),
    (4, "hdl-sim-poke-force", "lab", "Poke / force / release", "hdl-sim-poke-force", "S"),
    (5, "hdl-sim-waves", "lab", "Full-sim waves", "hdl-sim-waves", "S"),
    (6, "hdl-sim-multi-file", "lab", "Multi-file project", "hdl-sim-multi-file", "S"),
    (7, "hdl-sim-compare-golden", "lab", "Golden compare", "hdl-sim-compare-golden", "S"),
    (8, "style-synth-bridge", "bridge", "Style & synth hints in the IDE", "hdl-style", "S"),
    (9, "offline-public-sim", "offline", "Open public simulator — free practice", None, None),
    (10, "wrap", "wrap", "Simulator path complete", None, None),
]


def mod_dir(num: int, slug: str) -> Path:
    return DST / f"module{num:02d}-{slug}"


def lab_urls(lab_id: str) -> tuple[str, str]:
    return (f"{LAB_BASE_LOCAL}/{lab_id}/index.html", f"{LAB_BASE_LIVE}/{lab_id}/")


def write_module_readme(
    num: int, slug: str, kind: str, title: str, lab_id: str | None, status: str | None
) -> None:
    d = mod_dir(num, slug)
    d.mkdir(parents=True, exist_ok=True)
    nn = f"{num:02d}"
    prev = next((m for m in MODULES if m[0] == num - 1), None)
    nxt = next((m for m in MODULES if m[0] == num + 1), None)

    nav = []
    if prev:
        nav.append(f"[← {prev[3]}](../module{prev[0]:02d}-{prev[1]}/README.md)")
    else:
        nav.append("← Start")
    nav.append("[Course README](../README.md)")
    if nxt:
        nav.append(f"[{nxt[3]} →](../module{nxt[0]:02d}-{nxt[1]}/README.md)")
    else:
        nav.append("End →")
    nav_line = " · ".join(nav)

    if kind == "intro":
        body = f"""# Module {nn}: {title}

**Kind:** `intro` · Dual-track course welcome

{nav_line}

## What this course is

**learn_hdl_simulator** is the guided path for the public
[HDL Simulator]({PUBLIC_SIM}).
Browser `hdl-sim-*` labs teach IDE workflow; the live simulator is the practice surface.

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Public simulator** | Live IDE: Files / Hierarchy / Signals / Wave / Console | Muscle memory in a real session |
| **B — Browser literacy** | Platform `hdl-sim-*` concept labs | Tour, poke/force, waves, multi-file, golden compare |

Sibling courses: **learn_verilog**, **learn_iverilog**, **learn_verilator**.

## Setup (Track A)

1. Open the [HDL Simulator]({PUBLIC_SIM}) in a modern browser.
2. Optional: keep a tiny counter / TB sketch ready from **learn_verilog**.
3. Open this repo at `courses/learn_hdl_simulator`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html#hdl-simulator
3. Start with [`hdl-sim-tour`]({LAB_BASE_LOCAL}/hdl-sim-tour/index.html).

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
"""
    elif kind == "wrap":
        body = f"""# Module {nn}: {title}

**Kind:** `wrap`

{nav_line}

## You can now

- Name the IDE panes (Files · Hierarchy · Signals · Wave · Console)
- Run / stop / reset a tiny DUT and use Step / Continue / poke / force safely
- Add waves with C1/C2 · radix, link multi-file projects, and golden-compare at C1
- Practice freely in the [public HDL Simulator]({PUBLIC_SIM})

## Dual-track recap

If you mainly used **browser labs**, open the public IDE and recreate one tour + waves session.  
If you mainly used the **public simulator**, revisit any `hdl-sim-*` lab for graded challenges.

## Next courses

→ **learn_iverilog** · **learn_verilator** · **learn_uart** / **learn_spi** / **learn_i2c**  
Syllabus ladder: [../../syllabus.md](../../syllabus.md#suggested-learning-ladder)

## Checklist

- [ ] I completed Track A and/or Track B for the modules I care about
- [ ] I can open the public simulator without getting lost in the UI
- [ ] I know when to switch to iverilog / Verilator for offline fidelity
"""
    elif kind == "bridge":
        local, live = lab_urls("hdl-style")
        body = f"""# Module {nn}: {title}

**Kind:** `bridge` · Labs: `hdl-style` + `synth-lint` · **Shipped**

{nav_line}

## Outcomes

Connect IDE workflow to coding style and synthesizability cues (short bridge — not a full RTL course).

## Two tracks

### Track A — Public simulator

Open a small DUT in the [HDL Simulator]({PUBLIC_SIM}) and note style / lint warnings if shown.

### Track B — Browser labs

1. [`hdl-style`]({local}) · [live]({live})
2. [`synth-lint`]({LAB_BASE_LOCAL}/synth-lint/index.html) · [live]({LAB_BASE_LIVE}/synth-lint/)

## Media (module-slides ready)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript | [transcript.md](transcript.md) |
"""
    elif kind == "offline":
        body = f"""# Module {nn}: {title}

**Kind:** `offline` · Practice surface: public HDL Simulator

{nav_line}

## Outcomes

Spend unstructured time in the live IDE — open a DUT, run, wave, and poke without a graded browser lab.

## Practice

1. Open [{PUBLIC_SIM}]({PUBLIC_SIM})
2. Load or paste a tiny counter + TB (from **learn_verilog** or your notes)
3. Practice: Run / Stop / Reset · Step · add waves · optional poke
4. Check off [CHECKLIST.md](CHECKLIST.md)

> This module has **no** browser tool id — fidelity is the public simulator itself.

## Media (module-slides ready)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript | [transcript.md](transcript.md) |
"""
    else:
        assert lab_id and status
        local, live = lab_urls(lab_id)
        body = f"""# Module {nn}: {title}

**Kind:** `lab` · Primary lab: `{lab_id}` · **Shipped**

{nav_line}

## Outcomes

After this module you can explain and practice the ideas taught by **`{lab_id}`**, in the browser literacy lab and/or the public HDL Simulator.

## Two tracks (pick one or both)

### Track A — Public simulator (hands-on)

1. Open [EXAMPLES.md](EXAMPLES.md) and try the same workflow in the [HDL Simulator]({PUBLIC_SIM}).
2. Complete [CHECKLIST.md](CHECKLIST.md).
3. Optional self-check: `./scripts/module.sh {nn} --check` (from course root).

### Track B — Browser lab (online)

1. Local: [{local}]({local})
2. Live: [{live}]({live})
3. Load the **starter example**, then work challenges.
4. Check off the Track B items in [CHECKLIST.md](CHECKLIST.md).

> Concept labs are literacy tools — they do not replace time in the public simulator IDE.

## Media (module-slides ready)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript | [transcript.md](transcript.md) |
| Slides / video | generate with **module-slides** |

## Files

```
module{nn}-{slug}/
├── README.md
├── CHECKLIST.md
├── EXAMPLES.md
├── outline.yaml
├── transcript.md
└── (optional) assets/ examples/
```
"""
    (d / "README.md").write_text(body, encoding="utf-8")


def write_checklist(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "intro":
        text = f"""# Module {nn} checklist — {title}

## Setup

- [ ] Opened the [public HDL Simulator]({PUBLIC_SIM}) once
- [ ] Opened this repo at `courses/learn_hdl_simulator`
- [ ] Opened the [tools index]({LAB_BASE_LOCAL}/index.html#hdl-simulator)

## Mindset

- [ ] I understand browser labs teach workflow; the public IDE is the practice surface
- [ ] I know iverilog / Verilator remain the offline fidelity path
"""
    elif kind == "wrap":
        text = f"""# Module {nn} checklist — {title}

- [ ] Reviewed outcomes in [README.md](README.md)
- [ ] Ready for iverilog / Verilator / protocol courses as needed
"""
    elif kind == "offline":
        text = f"""# Module {nn} checklist — {title}

- [ ] Opened the [public HDL Simulator]({PUBLIC_SIM})
- [ ] Ran at least one tiny DUT (Run / Stop / Reset)
- [ ] Added a signal to waves or poked a net once
"""
    elif kind == "bridge":
        text = f"""# Module {nn} checklist — {title}

## Track B

- [ ] Opened `hdl-style` and/or `synth-lint`
- [ ] Can name one style or lint idea to watch in the IDE

## Track A

- [ ] Noted the same idea while using the public simulator (optional)
"""
    else:
        text = f"""# Module {nn} checklist — {title}

## Track A — Public simulator

- [ ] Worked through at least one prompt in [EXAMPLES.md](EXAMPLES.md)
- [ ] Can explain the outcome in my own words

## Track B — Browser lab (`{lab_id}`)

- [ ] Opened the lab (local or live)
- [ ] Loaded starter + completed a few challenges

## Done when

- [ ] I can do the task in the public IDE **or** I finished the browser challenges (preferably both)
"""
    (d / "CHECKLIST.md").write_text(text, encoding="utf-8")


def write_examples_md(num: int, slug: str, kind: str, title: str) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "lab":
        text = f"""# Module {nn} examples — {title}

Track A (public HDL Simulator). Track B is the matching `hdl-sim-*` lab.

## Prompts

1. Restate the core idea of **{title}** in one sentence.
2. In the [public simulator]({PUBLIC_SIM}), practice the same workflow once.
3. Optional: use a tiny counter DUT from **learn_verilog** notes.

## Stretch

Redo the browser lab challenges after the IDE practice.
"""
    elif kind == "offline":
        text = f"""# Module {nn} examples — free practice

1. Open [{PUBLIC_SIM}]({PUBLIC_SIM})
2. Paste or open a tiny DUT + TB
3. Run, wave, optional poke — no graded checklist beyond CHECKLIST.md
"""
    else:
        text = f"""# Module {nn} — no example trees

This is an `{kind}` module. See [README.md](README.md).
"""
    (d / "EXAMPLES.md").write_text(text, encoding="utf-8")


def write_outline_transcript(
    num: int, slug: str, kind: str, title: str, lab_id: str | None
) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    lab_line = lab_id or "none"
    track_line = {
        "intro": "A (public simulator) · B (browser literacy)",
        "wrap": "recap only",
        "offline": "A (public simulator free practice)",
        "bridge": "A (public IDE) · B (hdl-style / synth-lint)",
        "lab": "A (public simulator) · B (browser lab)",
    }.get(kind, "A · B")

    (d / "outline.yaml").write_text(
        f"""# Module {nn} outline — stub for module-slides
# Replace notes when expanding transcript.md, then run transcript_to_outline.py
title: "{title}"
kind: {kind}
lab: {lab_id or "null"}
footer: "learn_hdl_simulator — {slug}"
slides:
  - type: title
    title: "{title}"
    subtitle: "learn_hdl_simulator module {nn}"
    notes: "Welcome. This module is {title}."
  - type: bullets
    title: Core idea
    bullets:
      - One concept for this module
      - Why it matters in the simulator IDE
    notes: "Teach the core idea in spoken prose — expand in transcript.md."
  - type: bullets
    title: Track B browser lab
    bullets:
      - Open the matching hdl-sim lab if shipped
      - Load starter · challenges
    notes: "Show the browser literacy lab starter when available."
  - type: bullets
    title: Track A public IDE
    bullets:
      - Open the public HDL Simulator
      - Practice the same workflow
    notes: "Point at the live IDE practice surface."
  - type: bullets
    title: Your turn
    bullets:
      - Complete the checklist for at least one track
      - Optional short quiz
    notes: "Send learners to CHECKLIST.md, then the next module."
duration_minutes: 6
""",
        encoding="utf-8",
    )

    if kind == "lab" and lab_id:
        show_b = (
            f"Open the browser lab `{lab_id}`: load the starter example, "
            "then walk a couple of challenges so the idea sticks."
        )
        show_a = (
            f"In the public HDL Simulator, practice the same workflow once — "
            f"link: {PUBLIC_SIM}"
        )
    elif kind == "offline":
        show_b = "There is no graded browser lab for this module."
        show_a = f"Open the public simulator and practice freely: {PUBLIC_SIM}"
    elif kind == "bridge":
        show_b = "Open `hdl-style` and `synth-lint` on the tools shelf."
        show_a = "In the public IDE, notice style or lint cues if your session shows them."
    else:
        show_b = "Point at the course map and the HDL simulator tools section."
        show_a = f"Open the public IDE once so learners know the destination: {PUBLIC_SIM}"

    (d / "transcript.md").write_text(
        f"""# Module {nn} — {title}

**Module id:** module{nn}-{slug}  
**Lab:** {lab_line}  
**Tracks:** {track_line}

## Slide 1 — {title}

Welcome to this module of learn HDL simulator. Today we focus on **{title}**. Browser literacy labs teach the workflow; the public HDL Simulator is where you practice for real.

## Slide 2 — Why this matters

In chip bring-up and coursework, getting lost in the simulator UI costs hours. This module gives you one clear skill you can reuse in every later HDL session.

## Slide 3 — Track B browser lab

{show_b}

## Slide 4 — Track A public simulator

{show_a}

## Slide 5 — Pitfalls

Do not treat the concept lab as a full simulator. Do not force clocks carelessly. Prefer poke for soft deposits and release forces when you are done. Always know which file is top.

## Slide 6 — Your turn

Complete the checklist for at least one track — preferably both. When you finish, continue to the next module in docs/MODULES.md.
""",
        encoding="utf-8",
    )


def write_docs_index() -> None:
    docs = DST / "docs"
    docs.mkdir(exist_ok=True)
    rows = []
    for num, slug, kind, title, lab_id, status in MODULES:
        if lab_id and kind == "bridge":
            lab = "`hdl-style` / `synth-lint`"
        elif lab_id:
            lab = f"`{lab_id}`"
        else:
            lab = "—"
        st = status or "—"
        rows.append(
            f"| {num:02d} | `{kind}` | [{title}](../module{num:02d}-{slug}/README.md) | {lab} | {st} |"
        )
    (docs / "MODULES.md").write_text(
        f"""# learn_hdl_simulator — module index

Lab-driven syllabus (pass 3). Full product syllabus: [../../syllabus.md](../../syllabus.md#9-learn_hdl_simulator).

| # | Kind | Module | Lab | Status |
|---|------|--------|-----|--------|
{chr(10).join(rows)}

## Dual tracks

See [TWO_TRACKS.md](TWO_TRACKS.md). Practice surface: [HDL Simulator]({PUBLIC_SIM}).
""",
        encoding="utf-8",
    )
    (docs / "TWO_TRACKS.md").write_text(
        f"""# Two learning tracks

## Track A — Public HDL Simulator

Practice in the live IDE:

- [{PUBLIC_SIM}]({PUBLIC_SIM})
- Prompts under each `moduleNN-*/EXAMPLES.md`
- Self-check: `./scripts/module.sh NN --check`

## Track B — Browser literacy (`hdl-sim-*`)

- Local tools: {LAB_BASE_LOCAL}/#hdl-simulator
- Live: {LAB_BASE_LIVE}/
- **Shipped:** `hdl-sim-tour`, `hdl-sim-hello-dut`, `hdl-sim-step-continue`, `hdl-sim-poke-force`, `hdl-sim-waves`, `hdl-sim-multi-file`, `hdl-sim-compare-golden`, plus bridge labs `hdl-style` / `synth-lint`

## Recommended path

1. Intro + UI tour (`hdl-sim-tour`)
2. Hello DUT → step/continue → poke/force
3. Waves → multi-file → golden compare
4. Style/synth bridge → free practice in the public IDE
""",
        encoding="utf-8",
    )


def write_course_readme() -> None:
    landing = [
        f"| {num:02d} — {title} | [module{num:02d}-{slug}](module{num:02d}-{slug}/README.md) |"
        for num, slug, _k, title, *_ in MODULES
    ]
    shipped = sum(1 for m in MODULES if m[5] == "S")
    (DST / "README.md").write_text(
        "\n".join(
            [
                "# learn_hdl_simulator",
                "",
                "[![GitHub](https://img.shields.io/badge/GitHub-learn__hdl__simulator-181717?logo=github)](https://github.com/universal-verification-methodology/learn_hdl_simulator)",
                "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)",
                "[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)",
                "[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)",
                "[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)",
                "[![Domain](https://img.shields.io/badge/domain-HDL%20Simulator%20%7C%20browser%20IDE-purple)](https://github.com/universal-verification-methodology/learn_hdl_simulator)",
                "",
                "**learn_hdl_simulator** is the open learning path for the *browser HDL Simulator* — guided `hdl-sim-*` literacy plus free practice in the public IDE.",
                "",
                "Authors rebuild slides/audio with **module-slides** in the parent monorepo.",
                "",
                "## Table of contents",
                "",
                "- [Contents](#contents)",
                "- [Browse or clone](#browse-or-clone)",
                "- [Author: module-slides](#author-module-slides)",
                "- [Two learning tracks](#two-learning-tracks)",
                "- [Module landings](#module-landings)",
                "- [Browser labs](#browser-labs)",
                "- [License](#license)",
                "",
                "## Contents",
                "",
                "```text",
                "learn_hdl_simulator/",
                "├── README.md",
                "├── LICENSE",
                "├── docs/",
                "│   ├── MODULES.md",
                "│   └── TWO_TRACKS.md",
                "├── scripts/",
                "│   └── module.sh",
                "├── module00-intro/",
                "├── module01-hdl-sim-tour/",
                "├── …",
                "└── module10-wrap/",
                "```",
                "",
                "## Browse or clone",
                "",
                f"- **Public IDE:** [{PUBLIC_SIM}]({PUBLIC_SIM})",
                "- **Browser labs:** [tools/#hdl-simulator](https://universal-verification-methodology.github.io/learning/tools/#hdl-simulator)",
                "- **Syllabus:** [`syllabus.md` § learn_hdl_simulator](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#9-learn_hdl_simulator)",
                "",
                "```bash",
                "git clone --recurse-submodules \\",
                "  git@github.com:universal-verification-methodology/learning.git",
                "ls courses/learn_hdl_simulator",
                "./scripts/module.sh 01 --check",
                "```",
                "",
                "## Author: module-slides",
                "",
                "```bash",
                "cd ../..   # monorepo root",
                "python .cursor/skills/module-slides/scripts/transcript_to_outline.py \\",
                "  courses/learn_hdl_simulator/module01-hdl-sim-tour",
                "bash .cursor/skills/module-slides/scripts/narrate_clips.sh \\",
                "  courses/learn_hdl_simulator/module01-hdl-sim-tour",
                "```",
                "",
                "## Two learning tracks",
                "",
                "Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).",
                "",
                "| Track | Practice surface | Start here |",
                "|-------|------------------|------------|",
                f"| **A — Public simulator** | [HDL Simulator]({PUBLIC_SIM}) | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |",
                f"| **B — Browser literacy** | `hdl-sim-*` labs | [hdl-sim-tour]({LAB_BASE_LIVE}/hdl-sim-tour/) |",
                "",
                f"Lab status snapshot: **{shipped} shipped** browser/bridge labs (see [docs/MODULES.md](docs/MODULES.md)).",
                "",
                "## Module landings",
                "",
                "Full status table: **[docs/MODULES.md](docs/MODULES.md)**.",
                "",
                "| Module | Landing |",
                "|--------|---------|",
                *landing,
                "",
                "## Browser labs",
                "",
                f"**Shipped:** [hdl-sim-tour]({LAB_BASE_LIVE}/hdl-sim-tour/) · [hdl-sim-hello-dut]({LAB_BASE_LIVE}/hdl-sim-hello-dut/) · [hdl-sim-step-continue]({LAB_BASE_LIVE}/hdl-sim-step-continue/) · [hdl-sim-poke-force]({LAB_BASE_LIVE}/hdl-sim-poke-force/) · [hdl-sim-waves]({LAB_BASE_LIVE}/hdl-sim-waves/) · [hdl-sim-multi-file]({LAB_BASE_LIVE}/hdl-sim-multi-file/) · [hdl-sim-compare-golden]({LAB_BASE_LIVE}/hdl-sim-compare-golden/) · [hdl-style]({LAB_BASE_LIVE}/hdl-style/) · [synth-lint]({LAB_BASE_LIVE}/synth-lint/).",
                "",
                "## License",
                "",
                "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_scripts() -> None:
    scripts = DST / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "module.sh").write_text(
        r"""#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    [[ -f "$MOD_DIR/EXAMPLES.md" ]] && echo "[OK] EXAMPLES.md"
    [[ -f "$MOD_DIR/CHECKLIST.md" ]] && echo "[OK] CHECKLIST.md"
    [[ -f "$MOD_DIR/transcript.md" ]] && echo "[OK] transcript.md (module-slides)"
    echo "[INFO] Practice surface: https://universal-verification-methodology.github.io/systemverilog-simulator/"
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
""",
        encoding="utf-8",
    )
    (scripts / "README.md").write_text(
        """# Scripts

| Script | Purpose |
|--------|---------|
| `module.sh NN` | `--check` / `--demo` for module number `NN` |
| `_scaffold_course.py` | Regenerate course stubs from syllabus (authors) |

```bash
chmod +x scripts/*.sh
./scripts/module.sh 01 --check
```
""",
        encoding="utf-8",
    )
    # keep scaffold next to scripts for authors
    pass


def write_license() -> None:
    src = COURSES / "learn_unix" / "LICENSE"
    dst = DST / "LICENSE"
    if src.exists():
        dst.write_text(
            src.read_text(encoding="utf-8").replace("learn_unix", "learn_hdl_simulator"),
            encoding="utf-8",
        )
    else:
        dst.write_text(
            "Creative Commons Attribution 4.0 International (CC BY 4.0)\n\n"
            "Copyright (c) The learn_hdl_simulator contributors.\n\n"
            "https://creativecommons.org/licenses/by/4.0/\n",
            encoding="utf-8",
        )


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    write_license()
    write_course_readme()
    write_docs_index()
    write_scripts()
    # copy this file into scripts/ if run from elsewhere — authors keep it here
    for num, slug, kind, title, lab_id, status in MODULES:
        print(f"module{num:02d}-{slug} …")
        write_module_readme(num, slug, kind, title, lab_id, status)
        write_checklist(num, slug, kind, title, lab_id)
        write_examples_md(num, slug, kind, title)
        write_outline_transcript(num, slug, kind, title, lab_id)
    print(f"scaffolded {DST}")


if __name__ == "__main__":
    main()
