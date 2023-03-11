# Orthographic chording

## Objectives

### Goals
* Provide a faster and more ergonomic alternative to fingerspelling
* (mostly) Mimic the intuition for syllable-by-syllable writeouts

### Nongoals
* Replace nonorthographic theories

## Mechanics

### Left bank letters
Roughly a superset of fingerspelling. All vowels and left-hand consonants can be individually chorded the same as with fingerspelling, with two exceptions:
* `K`: c
* `KPW`: k

The `*` key does not need to be pressed for each stroke.

#### Additional left bank chords
By default, `_HR` will translate to `_l`, so `SHR`, `THR`, `KHR` will produce `sl`, `tl`, `cl`. Use `WHR` to split it into `hr` (`SWHR`, `TWHR`, `KWHR` for `shr`, `thr`, `chr`); e.g. `throttle` could be stroked `TWHROT/THRE`.

### Vowels
When vowels are in a stroke, `*` is used as an additional vowel key.

### Right bank letters
All single-key chords represent their key values. Other chords include:
* `-PG`: c
* `-FR`: h
* `-PBLGT`: j
    * `-PBLG`: dg
* `-BG`: k
    * `-BLG`: ck
* `-FPBLG`: q
* `-FB`: v
* `-FBG`: w
* `-BGS`: x
    * `-BGZ`: ks

#### Additional right bank chords
These chords can be individually chorded the same as in Plover theory:
* `-FP`: ch

These chords have been changed:
* `-FPB`: sh (`-RB`: rb)
* `-FPBG`: nk

These chords have been introduced:
*

#### Ending vowels
* `-TD`: e
* `-TSDZ`: y

#### Ending punctuation
Punctation chords all contain `-FPLT`. The punctuation characters are included in the glue and do not affect spacing or capitalization.
* `-FPLT`: . (period)
* `-FRPLT`: ' (apostrophe)
* `-FPBLT`: - (hyphen)
* `-FPBLTD`: — (em dash)

### Minutiae
* Unlike fingerspelling, letters will not be forced to lowercase (e.g., `KPA: "{-|}"` will affect the casing).