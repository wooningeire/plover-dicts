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


# `unicode_entry.py`: Arbitrary Unicode codepoint entry
Allows any Unicode character to be typed using its codepoint in hexadecimal.

## Mechanics
A codepoint is preceded by the stroke `TKWHR`.

The keys `-R`, `-B`, `-G`, and `-S` serve as binary place values of each hexadecimal digit of the codepoint. For instance, the stroke `-BGS` corresponds to binary `0111`, or 0x7.

`U` indicates a 0.

Digits are entered one stroke at a time, from left to right (most significant to least significant).

`R` is stroked alone to conclude a codepoint. `E` and `U` can be added to this final stroke to add a space to the left and right sides of the Unicode character respectively; if either are included, then the character will attach to that side instead.

For instance, `TKWHR/-S/-RBGS/-B/U/-RS/REU` maps to `{^ ^}🐉{^ ^}`, which has codepoint u+1f409.

After the initial stroke, `u+` is typed along with any digits entered thereafter, until the final stroke. This also allows the initial stroke to be undoable.