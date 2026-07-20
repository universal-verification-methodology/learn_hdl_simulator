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
