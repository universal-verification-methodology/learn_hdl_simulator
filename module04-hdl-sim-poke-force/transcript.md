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
