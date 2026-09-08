# Page lock / multimeasure-rest desktop evidence

Before: official main `ce7067126406142e51eb7772b11fac239a1dc873`.
After: `5b6df75a3642c70d9e20a15479be0b910a7deacf`.
Both recordings use identical copies of `repro.mscz`, at 100% zoom in the native APP Debug build (Ubuntu 24.04.2, Qt 6.10.2/GCC 14, ASan). GUI operations were performed by an agent through Xvfb/xdotool. Each video is 20 seconds, 1600x1000. The score's screen position differs. The music layout alone is not a reliable visual indicator of this defect; inspect the saved lock endpoints below.

## Reproduce

1. Extract `scores.zip` and open `repro.mscz`.
2. Open Format > Style > Rests.
3. Uncheck Multimeasure rests and click OK.
4. Save the score.

The supplied input was prepared in the desktop app from the official `page_locks_data/page_locks-1.mscx`: enable Multimeasure rests, remove the remaining page lock, then lock the compressed layout again. A temporary shortcut (Ctrl+Alt+P) was assigned in Edit > Preferences > Shortcuts to **Lock/unlock selected page(s)**; selecting the compressed rest and invoking it twice removed and re-added the lock. No custom shortcut is needed when using the supplied input.

## Saved-file evidence

A pageLock's endMeasure is an EID reference. Before the fix, expansion leaves a reference to `9oIdnbJLpXJ_4BKqCbAdIvH`, which no longer occurs as an element EID in the saved score. After the fix, the affected page lock is removed.

| Saved state | Multimeasure rests enabled | Page locks | Missing endpoint EIDs |
| --- | --- | --- | --- |
| repro.mscz | 1 | 1 | 0 |
| before.mscz | 0 | 1 | 1 |
| after.mscz | 0 | 0 | 0 |
| after-undo.mscz | 1 | 1 | 0 |
| after-redo.mscz | 0 | 0 | 0 |
| after-reopened-resaved.mscz | 0 | 0 | 0 |

The after-undo and after-redo files were saved after Ctrl+Z and Ctrl+Shift+Z in the fixed desktop app. The after-reopened-resaved file was loaded in a fresh fixed desktop process, then written with Save As. All listed results were checked with the included `inspect_scores.py` (Python standard library only). Extract scores.zip beside the script and run `python3 inspect_scores.py`.

Native command-state proof: the original five page-lock tests pass and the added probe fails before the correction; all six pass with endpoint cleanup. The final regression additionally asserts that the original lock ends on a generated MMRest. It reuses the original fixture included in scores.zip. Both changed C++ files pass upstream Uncrustify.

This evidence does not claim a release-version boundary, a crash, or first discovery. The correction adds constant endpoint checks per existing lock; it does not remap locks or change unrelated layout behavior.
