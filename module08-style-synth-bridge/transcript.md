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
