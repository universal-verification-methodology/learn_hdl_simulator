---
marp: true
title: Multi-file project
paginate: true
---

# Multi-file project

Real designs are rarely one file

---

## Top, TB, and linkage
- Name the DUT file and the testbench file explicitly
- Know which module is top for the run
- If the IDE links multiple files into one session

---

## Browser lab
![Lab starter](assets/lab-starter.png)

---

## Public simulator practice
- In the public IDE, open a tiny two-file sketch: DUT plus testbench
- Confirm both appear under Files, set top correctly, and elaborate or run once
- Intentionally remove the testbench from the set

---

## Pitfalls to watch
- Do not assume the open editor tab is the top module
- Do not forget packages or included files that the DUT needs
- Do not mix two unrelated testbenches in one run and expect clean waves
- Always reconcile Files with Hierarchy after a change

---

## Your turn
- Complete the checklist for at least one track, preferably both
- Build or restore a coherent DUT-plus-testbench file set and name the top
- When you are ready, take the short quiz, then continue to golden compare

