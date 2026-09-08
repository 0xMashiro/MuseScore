# Historical TAB duration grid reproduction

For MuseScore issue #34839 and PR #34840.

`scores.zip` contains the recording input (all beam modes AUTO), the result
saved through the fixed native desktop application, and the visual regression
score included in the PR. The input uses Italian duration symbols, two
quarters followed by four eighth notes, and symbol repetition set to Always.

Apply Break beam left to notes 1 and 3. Apply Join beams to note 2 and notes
4–6. The two quarter notes should have two horizontal lines; the four eighth
notes should have three. Undo and redo the final Join beams operation.

The previous edit-only PR revision accepts the changes but draws bare stems.
The revised implementation computes connectors after horizontal spacing and
keeps individual duration signs when this grid cannot express their values.
The earlier mixed half/quarter demonstration is superseded by this example.

Native Debug build: Ubuntu 24.04.2, Qt 6.10.2, GCC 14, ASan. All 21 enabled
Engraving_BeamTests pass after the revision; the same suite has four failing
historical TAB cases on the previous edit-only revision (17 passing).
Four pre-existing tests are disabled. Recordings use the native desktop at
300% zoom and are operated using Xvfb/xdotool.
