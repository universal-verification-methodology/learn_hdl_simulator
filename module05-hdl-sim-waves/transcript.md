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
