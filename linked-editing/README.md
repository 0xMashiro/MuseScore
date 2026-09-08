# Linked editing regression inputs

Checked against official MuseScore main `8d6bbe95efef28ccf2c05d6773cebcd364e505b6`.

- `delete-linked-rests.zip`: open the MSCX, create its part, and delete the first measure's contents. The native regression checks that both scores replace the four quarter rests with one measure rest without retaining empty rhythmic segments. No visible engraving difference is claimed.
- `linked-hairpin-range.zip`: a three-measure score with two linked staves and no hairpins. Add a crescendo across the first two measures. Delete measure 1's contents on both staves, undo, redo, undo; delete measure 2's contents on both staves, undo, redo. Save, close, and reopen. Unpatched main can write the linked hairpin before its main element and fail on reopening in a Debug build.
- `explode-linked-ties.zip`: a two-voice, two-measure score with its Piano part already created. In the full score, select all and choose Tools > Explode. Open the existing Piano part: unpatched main loses the lower staff's ties. Undo and redo demonstrate the same difference.

These are prepared input scores, not corrupted output files. Use a fresh copy for each before/after comparison. The Explode example is a reduced reproduction of the behavior reported in official issue #31825.
