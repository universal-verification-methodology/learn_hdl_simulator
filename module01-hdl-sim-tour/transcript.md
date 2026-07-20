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
