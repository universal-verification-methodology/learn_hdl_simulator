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
