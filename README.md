# Local time signature deletion/undo: evidence for MuseScore #29789

Official report: https://github.com/musescore/MuseScore/issues/29789

Baseline: `a64e0d0c8725a89af2b4b9f8e058a75be20c01d3` (unmodified official main).
Candidate: `add1935c15bf477b116159faf215624f13e44585`.
Environment: Linux desktop, Qt 6.10.2, GCC 14, Debug/ASan build; agent-operated X11 GUI.

## Reproduce

Extract `scores.zip` and open a fresh copy of `repro.mscz`. It derives from the existing native `timeSig-11.mscz` fixture, with a local 7/8 in Clarinet measure 2 and local 5/4 in measure 3, prepared through native editing commands.

1. Select the Clarinet 5/4 in measure 3.
2. Delete it.
3. Undo (Ctrl+Z).
4. Save (Ctrl+S).

`before.mp4`: the unmodified baseline restores the visible 5/4 but shows the score-corruption warning on save.
`after.mp4`: the candidate performs the same sequence and saves successfully with 5/4 restored. No corruption warning appears; the unsaved tab marker clears.

`before.mscz` is the baseline result after choosing **Save anyway**, outside the recording. It is intentionally the corrupted result, not the reproduction input. `after.mscz` is the successfully saved candidate result.

## Native regression

Filter: `--gtest_filter=Engraving_TimesigTests.*`.

- The maintained regression on the unmodified baseline fails: the restored TimeSig object is 5/4 but the full-score staff map still returns 7/8. `sanityCheck()` reports incomplete measures (found 10/7, expected 4/4).
- Candidate: all 16 native time signature tests pass, including the new regression.
- The new regression covers deletion from the full score and Clarinet excerpt, undo and redo, both staff-map queries, score integrity, and production-format MSCZ save/reopen with excerpts.
- The excerpt lookup itself restores correctly before the fix; the stale full-score map is the failing query from either deletion entry point.

Logs: `final-before-test.log` and `fixed-test.log`. Code style and `git diff --check` pass. No claim is made that this is a previously unreported issue, or that unrelated local time signature problems are fixed.

Published test logs normalize local checkout paths to `/workspace/MuseScore`; test results and diagnostics are unchanged.
