Python dictionaries; these require the [`plover-python-dictionary`](https://pypi.org/project/plover-python-dictionary/) plugin, which can be installed from the Plugin Manager.

# `control_seqs.py`: Procedural control sequences
Allows control sequences like `{#control_l(shift_l(a))}` to be stroked using rules similar to fingerspelling.

## Objectives
* Plover's default dictionaries only provide a small number of control sequences, which use a separate right-bank fingerspelling convention
* Make letters strokeable using typical fingerspelling chords so they are easier to guess

## Mechanics
The chord used to identify a stroke is `-TSDZ`.

The keys `-P`, `-B`, `-L`, and `-G` determine which modifiers are added to the translation:
* `-P`: `shift_l`
* `-B`: `control_l`
* `-L`: `alt_l`
* `-G`: `super_l` (meta/Windows/command key)

If none of these keys are included in a stroke, then the dictionary will default to `control_l` only.

For instance, `S-PLTSDZ` maps to `{#shift_l(alt_l(s))}`, and `KP-TSDZ` maps to `{#control_l(x)}`. (This does mean, however, that `-TSDZ` and `-BTSDZ` result in the same translations).

The key `-F` is experimentally used to include an attach operator in the transaltion. `PWH-FTSDZ` will map to `{#control_l(delete)}{^}`.

All other keys are used to identify which keys to emulate while holding down the modifier keys. Available chords include all English letters, which are accessible using usual fingerspelling chords, as well as some punctuation, numbers, and non-character keys like tab and backspace. These chords and all their keys can all be seen in the dictionary file under the variable `_CHORD_KEYMAP`.