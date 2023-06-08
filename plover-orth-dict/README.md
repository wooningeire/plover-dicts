# Orthographic chording

## Objectives

### Goals
* Provide a faster and more ergonomic alternative to fingerspelling
* (mostly) Mimic the intuition for syllable-by-syllable writeouts

### Nongoals
* Replace nonorthographic theories

## Mechanics
`orth_fingerspelling.py` is the main orthographic dictionary. It should be disabled initially and can be thought of as a "mode" which you enter into or exit from.

*(`orth_entry.py` is an extra, experimental dictionary that allows you to enter the orthographic dictionary by folding a certain chord into a stroke. It may be clunky to use without extra keys, and it is not required in order to use the main orthographic dictionary.)*

See setup instructions in `SETUP.md`.

### Example outlines
* sedenion `SEFRD/TPHO*PB`
* apeirogon `A/PAO*ERGDZ/TKPWOPB`
* Sierpinski `#S*ER/PEUPB/SKPWEU` <!-- * Kubernetes `#KPWU/PWER/TPHEFRTS` -->
* dopaminergic `TKO/PAPLGD/TPHER/TKPWEUPG`
* dactylopatagium `TKAPG/T*EULGDZ/PA/TA/TKPW*UPL`
* rhombicosidodecahedron `TPWROPL/PWEU/KOS/EU/TKOFRD/KAFRTD/TKROPB`
* Pafnuty Lvovich Chebyshev `#PAF/TPHUFPBT/S-P/#HR/SRO/SREUFP/S-P/#KHEBTSDZ/SHEFB`
    * (extended stenotype: `#PAF/TPHUFPBT/#^HR/SRO/SREUFP/#^KHEBTSDZ/SHEFB`)

### Entry and exit
You may need to manually define an entry to enter the orthographic dictionary using the `{plover:solo_dict}` command from the [`plover-dict-commands`](https://pypi.org/project/plover-dict-commands/) plugin; see `SETUP.md`.

Exit is handled by a special entry which translates to `{plover:end_solo_dict}`. By default, the stroke `-TSDZ` is mapped to this.

### Left bank

#### Left bank letters
Roughly a superset of fingerspelling. All vowels and left-hand consonants can be individually chorded the same as with fingerspelling, with two exceptions:
* `K`: c
* `KPW`: k

The `*` key does not need to be pressed for each stroke.

#### `WHR-` as `hr`
By default, `...HR-` will translate to `...l`, so `SHR`, `THR`, `KHR` will produce `sl`, `tl`, `cl`. Use `WHR` to split `l` into `hr`; e.g. `throttle` could be stroked `TWHROT/THRE`.
* `SWHR`: shr
* `TWHR`: thr
* `KWHR`: chr

#### Additional left bank chords
Other various chords have been introduced:
* `STPHR`: ' *(apostrophe)*
* `SKP`: ss
* `SKPW`: sk
* `SWR`: sr
* `TKPH`: kn
* `TPWH`: ph
    * `TPW`: phl
* `TPWR`: rh
* `TPHR`: fl
* `KWH`: qu
* `PHR`: pl
* `WHR`: hr

### Vowels
When vowels are in a stroke, `*` is used as an additional vowel key.

No asterisk | Asterisk
-|-
` `: *(none)* | `*`: *[undecided]*
`A`: a | `A*`: ia
`O`: o | `O*`: io
`E`: e | `*E`: ie
`U`: u | `*U`: iu
`AO`: oo | `AO*`: oa
`AE`: ea | `A*E`: ae
`AU`: au | `A*U`: aw
`OE`: oe | `O*E`: eo
`OU`: ou | `O*U`: ow
`EU`: i | `*EU`: y
`AOE`: ee | `AO*E`: ei
`AOU`: ue | `AO*U`: iou
`AEU`: ai | `A*EU`: ay
`OEU`: oi | `O*EU`: oy
`AOEU`: eu | `AO*EU`: ew

### Right bank

#### Right bank letters
All single-key chords represent their key values. Other chords include:
* `-PG`: c
* `-FR`: h
* `-PBLGT`: j (`-PBLG`: dg)
* `-BG`: k (`-BLG`: ck)
* `-PL`: m
* `-PB`: n
* `-FPBLG`: q
* `-FB`: v
* `-FBL`: w
* `-BGS`: x (`-BGZ`: ks)
* `-TSDZ`: y

#### Right bank Plover clusters
These clusters can be individually chorded the same as in Plover theory:
* `-FRP`: mp
* `-FRPB`: rch
* `-FRPBLG`: nch
* `-FP`: ch
* `-FPL`: sm
* `-FBG`: sk

These clusters have been changed:
* `-FPB`: sh (`-RB`: rb)
* `-FPBG`: nk

#### `-SZ` as doubler
`-SZ` is sometimes used to double an ending consonant.
* `-FSZ`: ff
* `-FRSZ`: hh
* `-PBSZ`: nn
* `-LSZ`: ll
* `-SZ`: ss

#### Additional right bank chords
Other various chords have been introduced:
* `-FRPBG`: hr
* `-FRPBD`: hn
* `-FRPBDZ`: hns
* `-FRB`: rf
* `-FRBL`: rv
* `-FPBL`: tch
* `-FPBG`: nk
* `-FPLG`: ph
    * `-FRPLG`: rph
* `-FBLG`: sc
* `-FPG`: nc
* `-FLG`: lk
* `-FG`: gh
    * `-FRG`: rgh
* `-FLT`: st
* `-PBLG`: dg
* `-BLG`: ck
* `-BLGT`: tion (`-GS`: gs)
    * `-FBLGT`: ction (`-BGS`: x)
* `-BGZ`: ks
* `-DZ`: ds

#### Ending vowels
`e` and `y` are given chords which only use columns 4/5. 
* `-TD`: e
* `-TSDZ`: y

The remaining ending vowels are assigned to chords that contain `-G`. From there, 4 uncommon chords are available for the remaining 4 vowels, so they have been arbitrarily assigned according to steno order.
* `-GSZ`: a
* `-GD`: i
* `-GDZ`: o
* `-GZ`: u

##### Inverted ending vowels
Some chords in columns 1/2 can be used to add vowels after chords that use columns 4/5.
* `-FR`: e (normally h)
* `-FPB`: y (normally sh)

These are simply added to the stroke, e.g.,
* `-FRT`: te
* `-FRS`: se
* `-FRD`: de
* `-FRZ`: ze
* `-FRLS`: lse
* `-FRGT`: the
* `-FRPBT`: nte
* `-FRPBS`: nse
* `-FPBT`: ty
* `-FPBS`: sy
* `-FPBGT`: thy
* etc.
#### Ending punctuation
Punctation chords all contain `-FPLT`. The punctuation characters are included in the glue and do not affect spacing or capitalization.
* `-FPLT`: . *(period)*
* `-FRPLT`: ' *(apostrophe)*
* `-FPBLT`: - *(hyphen & attach after)*
* `-FPBLTD`: — *(em dash & attach after)*

### Stroke modifiers
The remaining symbol keys are used to add modifiers onto the stroke.

For the standard English stenotype system:
* `#`: *(capitalize)*

For an [extended stenotype system](https://pypi.org/project/plover-stenotype-extended/) that provides `^`:
* `#`: *(capitalize)*
* `^`: *(space before)*
* `+`: *[undecided]*

### Misc details

#### Minutiae
* Unlike fingerspelling, letters will not be forced to lowercase (e.g., `KPA: "{-|}"` will affect the casing).

#### Chord identification
Stroke translations are constructed by checking each key in a stroke, in steno order. Chords are identified progressively as keys are checked.
* Any keys that are checked and which have not yet been translated into a chord are tracked. For each key that is checked, if we can constrct a larger chord out of that key and all the other keys that have not yet been translated, then the key is also tracked.
* Once a key is encountered that cannot continue the chord (or we reach the end of the stroke), the chord is appended to the translation.

This means that chords cannot be "stacked" nor overlap each other. This method also causes some strokes to not be translated how one might expect them to; several chords are included whose purpose are to resolve conflicts if the original result is uncommon or inconsistent (like `-FLTD`: "`fle`" vs "`std`"). (This also means some right-bank consonant clusters cannot be used with certain ending vowel chords for now, which may be changed later.)

Chord-by-chord translations are placed inside a glue; i.e., `PA*PBGDZ` maps to "`{&piano}`" instead of just "`piano`".

Chords and their translations are defined in `orth_fingerspelling.py` under the variable `_CHORDS`.

#### Special entries
Special entries function like normal dictionary entries and are not split up chord-by-chord like other strokes. They are defined in `orth_fingerspelling.py` under the variable `_SPECIAL_ENTRIES`.

By default, these entries are:

    "S-P": "{^ ^}",
    "KPA": "{}{-|}",
    "KPA*": "{^}{-|}",
    "SKW-T": "{^}'{^}",
    "TP-PL": "{.}",
    "KW-BG": "{,}",
    "TP-BG": "{!}",
    "KW-PL": "{?}",
    "H-F": "{?}",
    "H-PB": "{^}-{^}",
    "-TSDZ": "{#}{plover:end_solo_dict}",

Additional special entries can be added by editing `orth_fingerspelling.py`. Alternatively, you can also specify additional dictionaries to the command you use to enter the orthographic dictionary.