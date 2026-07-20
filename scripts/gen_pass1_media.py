#!/usr/bin/env python3
"""Generate pass-1 transcript.md + quiz.json for learn_hdl_simulator modules."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(module: str, transcript: str, quiz: dict) -> None:
    d = ROOT / module
    d.mkdir(parents=True, exist_ok=True)
    (d / "transcript.md").write_text(transcript.strip() + "\n", encoding="utf-8")
    (d / "quiz.json").write_text(
        json.dumps(quiz, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("wrote", module)


MODULES: list[tuple[str, str, dict]] = []

# --- 00 intro ---
MODULES.append(
    (
        "module00-intro",
        """
# Module 00 — Welcome to the browser simulator

**Module id:** module00-intro
**Lab:** none (intro)
**Tracks:** A (public simulator) · B (browser literacy)

## Slide 1 — Welcome to the browser simulator

Welcome to learn HDL simulator. This short path teaches the workflow of a browser-based HDL IDE—files, hierarchy, signals, waves, and the console—so you stop getting lost every time you open a session. Browser literacy labs teach the moves; the public HDL Simulator is where you practice for real.

## Slide 2 — What you’ll build toward

Across the course you’ll tour the five IDE panes, load a tiny DUT and use Run, Stop, and Reset, then Step and Continue with a breakpoint mindset. You’ll poke and force safely, read full-sim waves with cursors, link multi-file projects, compare against a golden at a cursor, and glance at style and synth hints. Sibling courses cover Verilog language depth, Icarus, and Verilator—here the job is simulator literacy.

## Slide 3 — Two tracks, one idea

Track A is the public HDL Simulator in a modern browser—Files, Hierarchy, Signals, Wave, and Console in a live session. Track B is the platform’s hdl-sim concept labs: guided challenges for tour, hello DUT, step, poke, waves, multi-file, and golden compare. You may do either track, or both. A good rhythm is browser lab first for the idea, then five minutes in the public IDE to harden it.

## Slide 4 — Set up Track A

Open the public HDL Simulator in a modern browser. Optional: keep a tiny counter or testbench sketch ready from learn Verilog. From this course folder, open module READMEs and EXAMPLES prompts as you go; the course self-check script can grade checklist items when you want them.

## Slide 5 — Set up Track B

![Tools index](assets/tools-index.png)

From the monorepo, serve the platform folder with a simple local web server, then open the tools index and jump to the HDL simulator section. All seven hdl-sim literacy labs ship, plus the style and synth bridge labs. If you prefer, use the published tools site instead. Either way, confirm you can reach the index—the next module sends you into the UI tour lab.

## Slide 6 — How to move through modules

For each module, read the README for the outcome, pick a track—or both—then work the checklist. Prefer Track B when you want graded challenges; prefer Track A when you want muscle memory in the real IDE. When you finish this intro checklist, continue to the UI tour.
""",
        {
            "module": "module00-intro",
            "title": "Welcome to the browser simulator",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "In this course, browser hdl-sim labs primarily…",
                    "choices": [
                        "Teach IDE workflow literacy before free practice in the public simulator",
                        "Replace Icarus and Verilator forever",
                        "Teach place-and-route only",
                        "Replace the need for any DUT or testbench",
                    ],
                    "answer": 0,
                    "explain": "Labs teach moves; the public IDE is the practice surface.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Track A means practice in…",
                    "choices": [
                        "The public HDL Simulator IDE",
                        "Only paper worksheets with no simulator",
                        "Git branching only",
                        "UVM scoreboards only",
                    ],
                    "answer": 0,
                    "explain": "Track A is the live public simulator session.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "A typical IDE session includes which pane set?",
                    "choices": [
                        "Files, Hierarchy, Signals, Wave, and Console",
                        "Only a schematic editor",
                        "Only synthesis reports",
                        "Only a git diff view",
                    ],
                    "answer": 0,
                    "explain": "Those five panes are the tour map for this course.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Deep language and offline-sim fidelity belong mainly in sibling courses like learn_verilog, learn_iverilog, and learn_verilator.",
                    "answer": True,
                    "explain": "This path focuses on browser simulator literacy.",
                },
            ],
        },
    )
)

# --- 01 tour ---
MODULES.append(
    (
        "module01-hdl-sim-tour",
        """
# Module 01 — UI tour

**Module id:** module01-hdl-sim-tour
**Lab:** hdl-sim-tour
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — UI tour

Before you debug a DUT, you need a mental map of the IDE. Five panes do almost all the work: Files for sources and top selection, Hierarchy for the instance tree, Signals for nets in a scope, Wave for the timeline, and Console for messages and errors. This module orients you so you always know which pane answers which question.

## Slide 2 — The five panes

Files hold project sources—open, edit, and pick the top or testbench files for the run. Hierarchy is the elaborated instance tree—pick a scope like the top, the DUT, or the testbench. Signals lists nets in that scope so you can add them to waves. Wave is the timeline—cursors, zoom, and radix live there. Console shows tool messages, display text, errors, and run or stop status.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser tour lab, load the starter example and visit every pane until the status reads oriented. Try a fresh tour and click panes yourself, or load a mid-tour preset that has only Files and Hierarchy visited. Challenges quiz what each pane is for—sources, instance tree, timeline, and messages.

## Slide 4 — Public simulator practice

In the public IDE, open a tiny project and deliberately click each pane once. Say out loud what you would look for there: which file is top, which instance is the DUT, which signal to wave, and whether the console shows a clean compile. That spoken map sticks better than skimming icons.

## Slide 5 — Pitfalls to watch

Do not hunt for values in Files when you need Hierarchy and Signals. Do not treat the concept lab as a full simulator—it teaches orientation, not cycle-accurate HDL. And do not skip Console when a run fails; many “wave mysteries” are compile or elaboration messages you never read.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, reach oriented by visiting all five panes. In the public IDE, name each pane’s job in one sentence. When you are ready, take the short quiz, then continue to Hello DUT.
""",
        {
            "module": "module01-hdl-sim-tour",
            "title": "UI tour",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "The Files pane is mainly for…",
                    "choices": [
                        "Project sources and picking top / TB files",
                        "Only zooming waveforms",
                        "Only forcing clocks",
                        "Only synthesis timing paths",
                    ],
                    "answer": 0,
                    "explain": "Files = sources and top selection.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Hierarchy shows…",
                    "choices": [
                        "The instance tree of the elaborated design",
                        "Only raw filesystem directories",
                        "Only golden hex dumps",
                        "Only lint rule catalogs",
                    ],
                    "answer": 0,
                    "explain": "Hierarchy is the instance tree.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "The Wave pane is where you…",
                    "choices": [
                        "Inspect the timeline of sampled values (cursors, zoom, radix)",
                        "Edit only Makefile variables",
                        "Replace the need for a Console",
                        "Pick the top file for compile",
                    ],
                    "answer": 0,
                    "explain": "Wave = timeline / cursors.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Console typically shows tool messages, $display output, errors, and run/stop status.",
                    "answer": True,
                    "explain": "Console is the message surface for the sim session.",
                },
            ],
        },
    )
)

# --- 02 hello dut ---
MODULES.append(
    (
        "module02-hdl-sim-hello-dut",
        """
# Module 02 — Hello DUT

**Module id:** module02-hdl-sim-hello-dut
**Lab:** hdl-sim-hello-dut
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — Hello DUT

Orientation is not enough—you need a tiny design under control. Hello DUT means load a small module, start time with Run, freeze with Stop, and return to a known state with Reset. Those three controls are the heartbeat of every later debug session.

## Slide 2 — Run, Stop, Reset

Run starts or resumes simulation time so the DUT updates each step. Stop freezes time so you can inspect state without advancing the model. Reset returns the DUT to its initial state and leaves the sim stopped. Load picks which tiny sketch sits in the sandbox—counter, toggle flip-flop, or a simple combo AND for literacy.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser lab, load the starter counter and practice the full Run, Stop, Reset triad until status reads ready. Switch DUT sketches and watch how q behaves while running—count up, toggle, or hold a combo result. Challenges ask you to load a DUT and complete the control triad without leaving a run hanging forever.

## Slide 4 — Public simulator practice

In the public IDE, open or paste a tiny counter with a short testbench. Compile or elaborate, then hit Run, Stop, and Reset once each. Confirm Console stays clean and that Reset actually clears the output you care about. Keep the design tiny—this module is control literacy, not a full test plan.

## Slide 5 — Pitfalls to watch

Do not confuse Reset of the DUT with closing the browser tab. Do not leave Run forever when you meant to inspect a frozen state—Stop first. And remember: concept clocks in the literacy lab are not the same as a real testbench clock generator; the public IDE still needs a proper TB for meaningful time.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish Run, Stop, and Reset on a loaded DUT. In the public IDE, do the same triad on one tiny design. When you are ready, take the short quiz, then continue to Step and Continue.
""",
        {
            "module": "module02-hdl-sim-hello-dut",
            "title": "Hello DUT",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "Run in the simulator mainly…",
                    "choices": [
                        "Starts or resumes simulation time so the DUT updates",
                        "Deletes all source files",
                        "Forces every net permanently",
                        "Exports a GDSII layout",
                    ],
                    "answer": 0,
                    "explain": "Run advances sim time.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Stop is for…",
                    "choices": [
                        "Freezing time to inspect state without advancing",
                        "Always clearing all waves forever",
                        "Choosing the top module only",
                        "Releasing all forces automatically",
                    ],
                    "answer": 0,
                    "explain": "Stop freezes time for inspection.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "Reset typically…",
                    "choices": [
                        "Returns the DUT to an initial state and leaves sim stopped",
                        "Compiles the design for ASIC tapeout",
                        "Creates a new git branch",
                        "Enables forcing the clock safely forever",
                    ],
                    "answer": 0,
                    "explain": "Reset restores initial DUT state.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Hello DUT literacy is about loading a tiny design and practicing Run / Stop / Reset before deeper debug.",
                    "answer": True,
                    "explain": "Control triad before poke, step, and waves depth.",
                },
            ],
        },
    )
)

# --- 03 step continue ---
MODULES.append(
    (
        "module03-hdl-sim-step-continue",
        """
# Module 03 — Step & continue

**Module id:** module03-hdl-sim-step-continue
**Lab:** hdl-sim-step-continue
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — Step & continue

Run is coarse. When something looks wrong, you need finer control: Step advances one conceptual time unit and pauses; Continue runs until a breakpoint, a system stop, or the end of a short window. Together with a halt, that triad is how you walk a bug without staring at a free-running clock.

## Slide 2 — Breakpoints and halt

A breakpoint pauses Continue when simulation time reaches a chosen tick. A system stop from the testbench is like a dynamic breakpoint—it halts the run so you can inspect. Practice all three moves: one Step, one Continue that hits a stop point, and recognizing that you are halted—not still running.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser lab, load the starter where Step and Continue-to-breakpoint are already practiced, then try idle at time zero with a breakpoint armed. Step once, then Continue until the breakpoint hits. Challenges lock in the difference between a single Step and a Continue that runs to a halt.

## Slide 4 — Public simulator practice

In the public IDE, set or use whatever stop or breakpoint style the tool offers, then Step through a few edges of a tiny counter. Continue until you hit a deliberate stop in the testbench or a breakpoint you set. Say whether you are paused after Step, continuing, or halted—and why.

## Slide 5 — Pitfalls to watch

Do not mash Run when you meant Step—you will overshoot the interesting edge. Do not forget that Continue without a stop condition can race to the end of the window. And do not confuse a halted session with a crashed compile; check Console if nothing advances.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Practice Step, Continue, and a halt once each. When you are ready, take the short quiz, then continue to poke, force, and release.
""",
        {
            "module": "module03-hdl-sim-step-continue",
            "title": "Step & continue",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "Step mainly…",
                    "choices": [
                        "Advances one conceptual time unit, then pauses",
                        "Always forces the clock high",
                        "Deletes the wave window",
                        "Chooses the Files pane only",
                    ],
                    "answer": 0,
                    "explain": "Step = fine-grained advance + pause.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Continue typically runs until…",
                    "choices": [
                        "A breakpoint, a system stop, or the end of a short window",
                        "The chip is taped out",
                        "All forces are released automatically",
                        "Hierarchy is empty",
                    ],
                    "answer": 0,
                    "explain": "Continue runs to a stop condition.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "A breakpoint is meant to…",
                    "choices": [
                        "Pause Continue when simulation time reaches a chosen tick",
                        "Replace the need for any testbench",
                        "Force every data net permanently",
                        "Export PDF waves only",
                    ],
                    "answer": 0,
                    "explain": "Breakpoint pauses at a time or condition.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "A testbench system stop can halt a run much like hitting a breakpoint.",
                    "answer": True,
                    "explain": "System stop is a dynamic halt from the TB.",
                },
            ],
        },
    )
)

# --- 04 poke force ---
MODULES.append(
    (
        "module04-hdl-sim-poke-force",
        """
# Module 04 — Poke / force / release

**Module id:** module04-hdl-sim-poke-force
**Lab:** hdl-sim-poke-force
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — Poke / force / release

Sometimes you need to deposit a value while the sim is live. Poke is a soft deposit for the next evaluation. Force hard-overrides a net until you Release. Release clears the force so normal drivers resume. Used carefully, these tools save hours; used carelessly, they create mysteries that look like RTL bugs.

## Slide 2 — Soft poke vs sticky force

Prefer poke when you want a temporary live value. Prefer force only when you must hold a net against its drivers—and always release when you are done. Reset nets can be held for debug; data nets are the usual poke or force targets. Clocks are a special hazard: forcing a clock is unsafe and easy to forget.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser lab, load the starter that pokes and forces data then releases—status should read ready with no force left active. Try forcing the clock and watch the hazard status appear; release it immediately. Challenges require the poke, force, and release triad and a clean exit with no leftover forces.

## Slide 4 — Public simulator practice

In the public IDE, poke a data net once and observe the wave. Force the same net, run a little, then release and confirm drivers resume. Avoid forcing the clock. If the tool warns about active forces, treat that as a first-class debug clue—not noise.

## Slide 5 — Pitfalls to watch

Do not leave forces active and then “debug” wrong RTL. Do not force clocks to “make time move.” Do not confuse poke with force—poke does not stick the same way. And always know which signal you selected before you deposit a value.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Practice poke, force, and release, and leave the session with no active forces. When you are ready, take the short quiz, then continue to full-sim waves.
""",
        {
            "module": "module04-hdl-sim-poke-force",
            "title": "Poke / force / release",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "Poke is best described as…",
                    "choices": [
                        "A soft live deposit for the next evaluation",
                        "A permanent override that never needs release",
                        "A compile flag for synthesis",
                        "A Hierarchy filter only",
                    ],
                    "answer": 0,
                    "explain": "Poke = soft deposit.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Force…",
                    "choices": [
                        "Hard-overrides a net until Release",
                        "Always clears itself after one delta",
                        "Only works on the Console pane",
                        "Deletes the selected signal from waves",
                    ],
                    "answer": 0,
                    "explain": "Force sticks until release.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "Forcing the clock is…",
                    "choices": [
                        "A hazard—prefer not to; release immediately if you did",
                        "The recommended way to advance all sims",
                        "Required before every poke",
                        "Harmless in every tool forever",
                    ],
                    "answer": 0,
                    "explain": "Clock force is unsafe / easy to forget.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "After a debug force, you should release so normal drivers can resume.",
                    "answer": True,
                    "explain": "Leftover forces create false bugs.",
                },
            ],
        },
    )
)

# --- 05 waves ---
MODULES.append(
    (
        "module05-hdl-sim-waves",
        """
# Module 05 — Full-sim waves

**Module id:** module05-hdl-sim-waves
**Lab:** hdl-sim-waves
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — Full-sim waves

Waves turn time into a picture. You add signals from a scope, run or step, then read values with cursors. Cursor one and cursor two let you measure intervals; radix changes how numbers appear—binary, hex, or unsigned. Full-sim waves means you are reading a real timeline, not a static sketch.

## Slide 2 — Add, cursor, radix

Pick a scope in Hierarchy, select signals, and add them to the wave pane. Place cursor one at an interesting edge; place cursor two to measure a delay or pulse width. Switch radix when hex is clearer than a long binary string. Zoom so the region you care about fills the view without losing context.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser waves lab, load the starter with signals already on the wave and cursors placed. Practice adding a signal, moving cursors, and changing radix until the challenges pass. Treat the verdict as a coach: it tells you whether the wave set and cursors match the ask.

## Slide 4 — Public simulator practice

In the public IDE, add clock, reset, and a data output to the wave. Run a short window, set two cursors around one interesting transition, and read the value at cursor one in hex. If a signal is missing, go back to Hierarchy and Signals—waves only show what you added.

## Slide 5 — Pitfalls to watch

Do not debug from Console alone when the bug is timing—open the wave. Do not forget which cursor is active when you read a value. Do not overload the pane with every net in the design; start with clock, reset, and the outputs you own. And remember concept labs animate literacy—the public IDE is where real TB time lives.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Add signals, place two cursors, and read one value with a sensible radix. When you are ready, take the short quiz, then continue to multi-file projects.
""",
        {
            "module": "module05-hdl-sim-waves",
            "title": "Full-sim waves",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "Cursors on a wave pane mainly help you…",
                    "choices": [
                        "Mark times and measure intervals between interesting edges",
                        "Edit SystemVerilog packages",
                        "Force clocks safely forever",
                        "Replace Hierarchy entirely",
                    ],
                    "answer": 0,
                    "explain": "C1/C2 mark and measure time.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Radix on waves is for…",
                    "choices": [
                        "Choosing how values display (e.g. binary vs hex)",
                        "Choosing the top file name only",
                        "Deleting unused source files",
                        "Enabling synthesis",
                    ],
                    "answer": 0,
                    "explain": "Radix = display base / format.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "If a signal is missing from the wave, first…",
                    "choices": [
                        "Select the right scope and add it from Signals",
                        "Force the clock permanently",
                        "Delete the Console log",
                        "Ignore Hierarchy forever",
                    ],
                    "answer": 0,
                    "explain": "Waves show what you add from a scope.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "A useful starter wave set often includes clock, reset, and the outputs you care about.",
                    "answer": True,
                    "explain": "Start focused; add more nets as needed.",
                },
            ],
        },
    )
)

# --- 06 multi-file ---
MODULES.append(
    (
        "module06-hdl-sim-multi-file",
        """
# Module 06 — Multi-file project

**Module id:** module06-hdl-sim-multi-file
**Lab:** hdl-sim-multi-file
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — Multi-file project

Real designs are rarely one file. Multi-file literacy means knowing which sources are in the project, which file is the top or testbench, and how include or compile order affects elaboration. Get the file set wrong and you will debug the wrong module for an hour.

## Slide 2 — Top, TB, and linkage

Name the DUT file and the testbench file explicitly. Know which module is top for the run. If the IDE links multiple files into one session, confirm every needed source is present—missing a package or a sub-module shows up as hierarchy holes or compile errors in the Console.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser multi-file lab, load the starter project and inspect how files are listed and which one is marked top. Try presets that drop a file or mis-mark top, and watch status leave ready. Challenges ask you to restore a coherent multi-file set before you “run.”

## Slide 4 — Public simulator practice

In the public IDE, open a tiny two-file sketch: DUT plus testbench. Confirm both appear under Files, set top correctly, and elaborate or run once. Intentionally remove the testbench from the set, note the Console error, then restore it—that muscle memory prevents silent wrong builds.

## Slide 5 — Pitfalls to watch

Do not assume the open editor tab is the top module. Do not forget packages or included files that the DUT needs. Do not mix two unrelated testbenches in one run and expect clean waves. Always reconcile Files with Hierarchy after a change.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Build or restore a coherent DUT-plus-testbench file set and name the top. When you are ready, take the short quiz, then continue to golden compare.
""",
        {
            "module": "module06-hdl-sim-multi-file",
            "title": "Multi-file project",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "In a multi-file sim session you must know…",
                    "choices": [
                        "Which sources are included and which module is top / TB",
                        "Only the wave radix",
                        "Only the git remote URL",
                        "Only the force list",
                    ],
                    "answer": 0,
                    "explain": "File set + top selection drive elaboration.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "A missing DUT or package file often shows up as…",
                    "choices": [
                        "Compile/elaboration errors or holes in Hierarchy",
                        "A faster clock automatically",
                        "A permanent poke on reset",
                        "A green golden compare with no run",
                    ],
                    "answer": 0,
                    "explain": "Console and Hierarchy reveal missing sources.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "The open editor tab…",
                    "choices": [
                        "Is not automatically the top module—you must set top intentionally",
                        "Always overrides Hierarchy forever",
                        "Disables the Console",
                        "Forces all clocks",
                    ],
                    "answer": 0,
                    "explain": "Top is an explicit project choice.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "A minimal multi-file practice set is often a DUT file plus a testbench file.",
                    "answer": True,
                    "explain": "DUT + TB is the classic two-file starter.",
                },
            ],
        },
    )
)

# --- 07 golden ---
MODULES.append(
    (
        "module07-hdl-sim-compare-golden",
        """
# Module 07 — Golden compare

**Module id:** module07-hdl-sim-compare-golden
**Lab:** hdl-sim-compare-golden
**Tracks:** A (public simulator) · B (browser lab)

## Slide 1 — Golden compare

A golden is an expected value or trace you trust. Golden compare means reading the design at a known time—often cursor one—and checking it against that expectation. It is the simplest self-check before you build a full scoreboard: did q match the hex you wrote down?

## Slide 2 — Compare at a cursor

Pick the signal, place cursor one at the check time, read the value with a clear radix, and compare to the golden. A mismatch is not failure of the method—it is information: wrong time, wrong signal, wrong radix, or real DUT bug. Match means you earned a ready status for that check.

## Slide 3 — Browser lab

![Lab starter](assets/lab-starter.png)

In the browser golden lab, load the starter that already compares at cursor one. Change the cursor or the expected value and watch the compare fail, then restore a passing check. Challenges train you to compare the right net at the right time—not just to hit Run.

## Slide 4 — Public simulator practice

In the public IDE, run a tiny counter to a known time, place cursor one, and write down the expected q in hex before you look. Then read the wave and compare. Optional stretch: change the testbench stimulus and update the golden deliberately so you see a real mismatch.

## Slide 5 — Pitfalls to watch

Do not compare at the wrong cursor or before the edge you meant. Do not mix binary expectations with hex displays. Do not treat a concept-lab pass as proof of silicon. And do not skip naming which signal was compared—orphaned goldens confuse future you.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. Perform one golden compare at cursor one on a tiny DUT. When you are ready, take the short quiz, then continue to the style and synth bridge.
""",
        {
            "module": "module07-hdl-sim-compare-golden",
            "title": "Golden compare",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "A golden compare checks…",
                    "choices": [
                        "Observed values against an expected reference at a known time",
                        "Only whether Files is empty",
                        "Only git commit messages",
                        "Only synthesis area reports",
                    ],
                    "answer": 0,
                    "explain": "Golden = expected vs observed.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "Comparing at cursor one means…",
                    "choices": [
                        "Reading the signal value at the time marked by C1",
                        "Always forcing reset",
                        "Ignoring radix",
                        "Deleting the wave pane",
                    ],
                    "answer": 0,
                    "explain": "C1 marks the check time.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "A mismatch might mean…",
                    "choices": [
                        "Wrong time, wrong signal/radix, or a real DUT/TB issue",
                        "The Console must be closed",
                        "Hierarchy is optional forever",
                        "You must force the clock",
                    ],
                    "answer": 0,
                    "explain": "Mismatch is diagnostic information.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Golden compare is a simple self-check idea before heavier scoreboards.",
                    "answer": True,
                    "explain": "Literacy step toward stronger checking.",
                },
            ],
        },
    )
)

# --- 08 bridge ---
MODULES.append(
    (
        "module08-style-synth-bridge",
        """
# Module 08 — Style & synth hints in the IDE

**Module id:** module08-style-synth-bridge
**Lab:** hdl-style / synth-lint
**Tracks:** A (public simulator) · B (browser labs)

## Slide 1 — Style & synth hints

Simulator literacy is not only Run and waves. Style and synthesizability cues catch problems early—messy naming, risky constructs, or lint that would hurt an FPGA or ASIC path. This short bridge connects the IDE session to those hints without becoming a full RTL course.

## Slide 2 — What to notice

In style practice, watch naming, module structure, and readability cues that keep reviews sane. In synth-lint practice, watch constructs that simulate fine but synthesize poorly—or warnings that deserve a second look. One named idea you will watch for later is enough for this module.

## Slide 3 — Browser labs

![Lab starter](assets/lab-starter.png)

Open the HDL style lab and the synth-lint lab from the tools index. Load a starter in each, read one finding or challenge prompt, and restate it in your own words. You do not need to finish every challenge—capture one style idea and one synth or lint idea.

## Slide 4 — Public simulator practice

In the public IDE, open a small DUT and notice any style or lint warnings the tool surfaces. Even if the IDE is quiet, ask yourself one synth question: would this reset or latch pattern survive a real build? Carry that question into later Verilog and Verilator work.

## Slide 5 — Pitfalls to watch

Do not treat this bridge as a complete coding-standard course. Do not ignore lint just because the sim passed. Do not “fix” synth issues by forcing signals in the wave—that hides the problem. Keep the scope small: awareness now, depth in sibling courses.

## Slide 6 — Your turn

Complete the checklist: open at least one of the bridge labs and name one style or lint idea to watch in the IDE. Optional: note the same idea once in the public simulator. When you are ready, take the short quiz, then spend free practice time in the public IDE.
""",
        {
            "module": "module08-style-synth-bridge",
            "title": "Style & synth hints",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "This bridge module’s job is to…",
                    "choices": [
                        "Connect IDE workflow to style and synthesizability awareness",
                        "Replace learn_verilog entirely",
                        "Teach UVM factory overrides",
                        "Teach PCB layout",
                    ],
                    "answer": 0,
                    "explain": "Short bridge, not a full RTL course.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "A sim pass with lint warnings means…",
                    "choices": [
                        "You should still read the warnings—sim ≠ synth readiness",
                        "Lint is always false and can be ignored forever",
                        "You must delete the DUT",
                        "Waves are illegal",
                    ],
                    "answer": 0,
                    "explain": "Simulation success does not erase lint.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "Track B for this module points at…",
                    "choices": [
                        "The hdl-style and synth-lint browser labs",
                        "Only the UART VIP",
                        "Only Git rebase",
                        "Only place-and-route",
                    ],
                    "answer": 0,
                    "explain": "Bridge labs are hdl-style and synth-lint.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Forcing signals in the wave is not a fix for synthesizability problems.",
                    "answer": True,
                    "explain": "Forces hide issues; they do not make RTL synth-clean.",
                },
            ],
        },
    )
)

# --- 09 offline ---
MODULES.append(
    (
        "module09-offline-public-sim",
        """
# Module 09 — Open public simulator — free practice

**Module id:** module09-offline-public-sim
**Lab:** none (public IDE practice)
**Tracks:** A (public simulator)

## Slide 1 — Free practice in the public IDE

No graded browser lab this time. Open the public HDL Simulator and spend unstructured time: load a tiny DUT, run, stop, reset, step, add waves, and optional poke. The point is fluency without a challenge checklist steering every click.

## Slide 2 — A simple practice loop

Paste or open a tiny counter plus testbench. Compile or elaborate until Console is clean. Run a short window, Stop, Reset once. Step a few times. Add clock and q to the wave, place a cursor, and optionally poke a data net then release. Stop when the loop feels boring—that is fluency.

## Slide 3 — What success looks like

Success is not a score. Success is: you can open the IDE without hunting for panes, you can control time, and you can read one value from the wave with confidence. If you get stuck, revisit the matching hdl-sim literacy lab, then return to the public IDE.

## Slide 4 — Optional depth

Stretch: mis-set top on purpose, read the Console error, fix it. Or force a net, watch the hazard, release it. Or compare q at cursor one to a handwritten golden. Keep the design tiny so the IDE skills stay the focus.

## Slide 5 — Pitfalls to watch

Do not turn free practice into a day-long RTL rewrite. Do not skip Console when something fails. Do not leave forces active. And do not confuse this browser IDE with offline Icarus or Verilator fidelity—those paths come next when you need them.

## Slide 6 — Your turn

Open the public simulator, run at least one tiny DUT through Run, Stop, and Reset, and either add a wave signal or poke once. Check off the module checklist, take the short quiz if you want a pulse check, then continue to the wrap.
""",
        {
            "module": "module09-offline-public-sim",
            "title": "Free practice in the public IDE",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "Module 09’s practice surface is…",
                    "choices": [
                        "The public HDL Simulator itself (no graded hdl-sim lab id)",
                        "Only a paper quiz with no IDE",
                        "Only synth-lint forever",
                        "Only GitHub Actions",
                    ],
                    "answer": 0,
                    "explain": "Free practice = public IDE.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "A good free-practice loop includes…",
                    "choices": [
                        "Load a tiny DUT, control time, and read a wave or poke once",
                        "Only renaming folders",
                        "Only writing a UVM agent",
                        "Only forcing clocks permanently",
                    ],
                    "answer": 0,
                    "explain": "Fluency loop: load, control, observe.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "If you get lost in the public IDE…",
                    "choices": [
                        "Revisit the matching browser literacy lab, then return",
                        "Delete all sources immediately",
                        "Ignore the Console forever",
                        "Skip to tapeout",
                    ],
                    "answer": 0,
                    "explain": "Labs reinforce; IDE builds muscle memory.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Browser IDE practice does not replace offline iverilog / Verilator when you need that fidelity.",
                    "answer": True,
                    "explain": "Sibling courses cover offline simulators.",
                },
            ],
        },
    )
)

# --- 10 wrap ---
MODULES.append(
    (
        "module10-wrap",
        """
# Module 10 — Simulator path complete

**Module id:** module10-wrap
**Lab:** none (wrap)
**Tracks:** A · B recap

## Slide 1 — Simulator path complete

You now have a working map of the browser HDL Simulator path. You can name the IDE panes, control a tiny DUT with Run, Stop, and Reset, step and continue with a halt mindset, poke and force safely, read waves with cursors, link multi-file projects, and golden-compare at a cursor—then practice freely in the public IDE.

## Slide 2 — Skills you can reuse

Files, Hierarchy, Signals, Wave, and Console are reusable in almost any HDL IDE. Soft poke versus sticky force, and releasing when done, transfers to professional tools. Golden compare at a known time is the seed of stronger checking. Style and synth awareness keeps sim-only habits from becoming silicon surprises.

## Slide 3 — Dual-track recap

![Tools index](assets/tools-index.png)

If you mainly used browser labs, open the public IDE and recreate one tour plus waves session. If you mainly used the public simulator, revisit any hdl-sim lab for graded challenges. Either way, confirm you can open the public simulator without getting lost.

## Slide 4 — Where to go next

For offline compile and sim fidelity, continue to learn Icarus Verilog or learn Verilator. For protocol bring-up, UART, SPI, and I²C courses reuse the same wave and TB habits. For deeper SystemVerilog and UVM, climb the syllabus ladder when you are ready.

## Slide 5 — Mindset to keep

Prefer tiny DUTs when learning tools. Read the Console before blaming the RTL. Never leave forces on. Know which file is top. And remember: literacy labs teach the moves; real confidence comes from time in the IDE and, later, in offline simulators.

## Slide 6 — Closing

Check off the wrap checklist. You finished the learn HDL simulator path. Open the public IDE once more if you want a victory lap, then pick the next course that matches your goal—language depth, offline sim, or protocols.
""",
        {
            "module": "module10-wrap",
            "title": "Simulator path complete",
            "passing_score": 0.67,
            "items": [
                {
                    "id": "q1",
                    "type": "multiple_choice",
                    "prompt": "After this course you should be able to…",
                    "choices": [
                        "Navigate panes, control time, wave, and poke/force safely in the IDE",
                        "Skip Console messages forever",
                        "Replace all offline simulators",
                        "Tape out without a testbench",
                    ],
                    "answer": 0,
                    "explain": "Core IDE literacy outcomes.",
                },
                {
                    "id": "q2",
                    "type": "multiple_choice",
                    "prompt": "A sensible next course for offline fidelity is…",
                    "choices": [
                        "learn_iverilog or learn_verilator",
                        "Only PCB silkscreen design",
                        "Only GitHub stars",
                        "Only forcing clocks in waves",
                    ],
                    "answer": 0,
                    "explain": "Offline sim courses follow this path.",
                },
                {
                    "id": "q3",
                    "type": "multiple_choice",
                    "prompt": "If you mostly did browser labs, a good wrap action is…",
                    "choices": [
                        "Recreate a tour + waves session in the public IDE",
                        "Delete the tools index",
                        "Ignore Hierarchy permanently",
                        "Force clk and leave it",
                    ],
                    "answer": 0,
                    "explain": "Transfer literacy into the live IDE.",
                },
                {
                    "id": "q4",
                    "type": "true_false",
                    "prompt": "Knowing which file is top and reading the Console are lasting simulator habits.",
                    "answer": True,
                    "explain": "Top + Console prevent many false debug paths.",
                },
            ],
        },
    )
)


def main() -> None:
    for module, transcript, quiz in MODULES:
        write(module, transcript, quiz)
    print("done", len(MODULES), "modules")


if __name__ == "__main__":
    main()
