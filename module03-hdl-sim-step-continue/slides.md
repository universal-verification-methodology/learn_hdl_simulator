---
marp: true
title: Step & continue
paginate: true
---

# Step & continue

Run is coarse

---

## Breakpoints and halt
- A breakpoint pauses Continue when simulation time reaches a chosen tick
- A system stop from the testbench is like a dynamic breakpoint
- Practice all three moves

---

## Browser lab
![Lab starter](assets/lab-starter.png)

---

## Public simulator practice
- In the public IDE
- Continue until you hit a deliberate stop in the testbench or a breakpoint you set
- Say whether you are paused after Step, continuing, or halted, and why

---

## Pitfalls to watch
- Do not mash Run when you meant Step, you will overshoot the interesting edge
- Do not forget that Continue without a stop condition can race to the end of the window
- And do not confuse a halted session with a crashed compile

---

## Your turn
- Complete the checklist for at least one track, preferably both
- Practice Step, Continue, and a halt once each
- When you are ready, take the short quiz, then continue to poke, force, and release

