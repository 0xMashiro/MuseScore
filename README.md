# Historical TAB beam-mode editing evidence

Before: official MuseScore main `ce7067126406142e51eb7772b11fac239a1dc873`.
After: fix commit `676a5b677a26cb8f4e6749c2cbaaba8877e6dec7`.

Both videos use the same musical score and initial AUTO/AUTO beam modes: the existing `vtest/scores/tabfont-14.mscz`, saved in the development desktop app. Select the first half-note chord and apply **Break beam left**, then the following quarter-note chord and apply **Join beams**.

- Before: the two duration symbols do not change, Undo stays disabled, and saved modes remain `auto/auto`.
- After: the symbols change to plain vertical strokes, saved modes become `begin/mid`; the video also shows undo/redo and Reset beams restoring `auto/auto`.

Each recording is 20 seconds at 1600x1000 and 100% score zoom. The score position differs between videos. These are agent-operated desktop recordings through Xvfb/xdotool on Ubuntu 24.04.2, Qt 6.10.2, GCC 14, APP Debug with ASan. No audio behavior is demonstrated.

`scores.zip` contains the original repository fixture, the AUTO/AUTO recording input, and the saved BEGIN/MID result. This evidence concerns mode editing; it does not claim to fix the separate horizontal grid-connector layout issue.
