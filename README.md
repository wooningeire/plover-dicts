## Experimental system and theory

**System:** Extended English Stenotype + &_

Below are various additional experimental mechanics present here that have been added to supplement Plover theory.

### `#`
`#` denotes proper nouns (and other parts of speech) and initialisms. It is usually added to the first stroke that comprises the word or phrase. Many of the entries that use this mechanic are found in `#-proper-nouns.json`.
* *[Potential change] Require the `#` modifier for each stroke that starts a new word in the proper noun*
  * *[Unclear] When to use `#` for pascal-case proper nouns*

E.g., `#PHAT` ⇒ `Matt`.

#### Caveats
* Do strokes containing `#` obey rules for prefix strokes? How should compound words and multiword titles be handled?

#### Motivation
This addition has been made due to the high incidence of conflicts between proper words in `main.json`. `main.json` usually uses asterisks and stroke duplications to denote proper nouns, but the high number of combinations between these two make it difficult to determine what the resulting spelling/formatting will be. It is also uncertain whether the entries for common proper nouns will even exist, as seen through the high number of misstroke entries that counteract redundant stroke duplications in `main.json`.

### `^`
`^` denotes affixes and segments of compound words. `^` and `*` (to denote prefixes) are added to all strokes that comprise the affix, but `#` is only added to the first stroke. Many of the entries that use this mechanic are found in `^-affixes.json`.
* `^` alone usually indicates a suffix, e.g., `^HRAOEUBG` ⇒ `{^}like`.
* The addition of `*` usually indicates a prefix, e.g., `^PH*E/^TA*` ⇒ `meta{^}`.
  * The typical uses of `*` for variations, conflicts, and chords that use `*` still apply in some circumstances, e.g., `^WO*RT/^KWREU` ⇒ `{^}worthy`.
  * `*` functions as a toggle (i.e., if a stroke that already contains `*` would need another `*` added to it, then the stroke should not have a `*`), e.g., `^ORT` ⇒ `ortho{^}`. (Find single-stroke entries with the regex `^"[^*]+": ".+\{\^\}",$`)
* The addition of `#` usually indicates hyphenation, e.g., `#^TPRAOE` ⇒ `{^}-free`.
  * `#` can still be used for proper words or proper affixes, e.g., `#^WEUPBG` ⇒ `{*-|}{^}Wing`.
* *[Unclear] When to use `^` or `#` for pascal-case proper nouns*

`^` is also uncommonly used to indicate the letter `A` for briefing purposes.

#### Caveats
* It is still necessary to semantically distinguish between affix strokes and other strokes, and to determine which parts of words are affixes.
  * Since `main.json`'s affix strokes do not have additional modifiers, it is possible to discover some of them through typical syllable splitting without first knowing they are affixes (although this falls apart in the case of conflicts, as described below). All `^` affixes are marked, so this is not possible to do with `^`.
  * If a word can be written using an affix stroke, when should an outline that uses typical syllable splitting without affix strokes be considered incorrect?
* When should `^` strokes be explicitly added to outlines for full words? Only when the root alone is not a word or changes spelling? When can the `^` strokes really be considered "affixes"? (e.g., `TPHUPL/^PAD` ⇒ `numpad`, `TUP/^HRET` ⇒ `tuplet`)
* The rule of adding modifiers to the first stroke may not neccessarily be consistent in the case of ambiguities and potential conflicts; e.g., `{^}alike` should be stroked `^A/^HRAOEUBG` instead of `^A/HRAOEUBG`.

#### Motivation
This addition has been made due to the high incidence/load of conflicts and the unpredictability that arises whenever ad-libbing an affix stroke in `main.json`. The high load of conflicts causes `main.json` to resort to arbitrary phoneme replacements and briefs that are difficult to predict without previous memorization and knowledge of their existence. `main.json` also uses `*` to convert some words into affixes and link together segments of compound words, but this may fall short when a conflict that uses `*` already exists. It is additionally unpredictable whether the affix will be hyphenated or not, and the need for hyphens may vary depending on style.

This is not intended as a complete replacement for the built-in affix strokes, which are at times more convenient and ergonomic, and more easily merged into other strokes.

### `+`
`+` currently has no use.

### `_`
`_` tentatively denotes symbols and punctuation. Many of the entries that use this mechanic are found in `_-symbols-and-text-commands.json`.

### `&`
`&` is used exclusively for entry to/exit from the orthographic spelling system.

## Dictionaries
Located in Plover's AppData directory (where `plover.cfg` is located). For brevity, `@/` is an alias for `./dicts/`.

`./dicts/py/` contains additional documentation regarding the usage of each Python dictionary.

Dictionary | Desc
-|-
`@/hidden/user.json` | The inner machinations of my mind
`@/json/skeletal.json` | Brief-like skeletal entries that contain each syllable of the translated word(s)
`@/hidden/names.json` | Names of people and brands
`@/json/software.json` | Software phrases and terminology
`@/json/math.json` | Math terminology
`@/json/dragon.json` | Dragon terminology and names
`@/json/notion.json` | Shortcuts for Notion
`@/json/latex.json` | LaTeX character and symbol sequences<br />`TWHR` prefix
`@/json/rust.json` | Idioms and terminology from Rust
`@/json/unicode-typography.json` | Unicode characters and their relevant spacing/capitalization<br /><ul><li>Includes IPA symbols</li></ul>
`@/json/custom-commands.json` | Commands<br />`PWH` prefix for text deletion. Right-hand side is based on navigation commands
`@/json/spacing-and-capitalization.json` | Spacing and capitalization commands<br />`KPWAO` prefix. Adding `E` removes the space<br />Some right-hand side commands are partially based on navigation commands; upper row is for uppercase, lower row is for lowercase, symmetric keys for both rows is for spacing, other combinations of the rows for miscellaneous things<br /><ul><li>`-` Reset mode</li><li>`-PBLG` Reset casing mode</li><li>`-PBTS` Reset spacing mode</li><li>`-F` Capitaize last</li><li>`-R` Uncapitalize last</li><li>`-P` Capitalize next</li><li>`-B` Uncapitalize next</li><li>`-L` Caps next</li><li>`-PL` Caps mode</li><li>`-BG` Lower mode</li><li>`-FR` Retro add space</li><li>(`EFR` Retro remove space)</li><li>`-PB` Space next</li></ul>Additional modes:<ul><li>`-PLT` Camel mode</li><li>`*PLT` Pascal mode</li><li>`-BGS` Snake mode</li><li>`-PBLGS` Screaming snake mode</li><li>`-LT` Title mode</li><li>`-GS` Kebab mode</li><li>`-TS` No spaces mode</li></ul>
`@/json/plover-recommended-dictionary-commands.json` | Recommended entries for commands from the [dictionary format](https://github.com/openstenoproject/plover/wiki/Dictionary-Format) wiki page
`@/json/mistakes.json` | Misstrokes and bad habits
`@/json/^-affixes.json` | Main list of entries that experimentally use the `^` key for affixes and compound words
`@/json/_-symbols-and-text-commands.json` | Main list of entries that experimentally use the `_` key for symbols and text commands<br /><ul><li>`*G` suffix for Greek letter fingerspelling, `*PG` for uppercase</li></ul>
`@/json/#-proper-nouns.json` | Main list of entries that use the `#` key for proper nouns and initialisms
`@/json/-frlg-h.json` | Entries that use the chord `-FRLG` to represent right-hand `h`
`@/json/-fb-v.json` | Entries that use the chord `-FB` to represent right-hand `v`
`@/json/kpw-c.json` | Entries that use the chord `KPW-` to represent `c` when it makes an /s/ sound and conflicts with `s`
`@/json/stkpw-z.json` | Entries that use the chord `STKPW-` to represent `z`
`@/json/skw-ex.json` | Experimental entries that use various chords for some words that start with `ex`, depending on the consonant that follows it
`@/json/skpw-inc_enc_anc.json` | Entries that use the chord `SKPW-` for words that start with `inc`, `enc`, `anc`
`@/json/kpw-imp_emp_amp_imb_emb_amb.json` | Entries that use the chord `KPW-` for words that start with `imp`, `emp`, `amp`, `imb`, `emb`, `amb`
`@/json/spw-ind-end-and-ant.json` | Entries that use the chord `SPW-` for words that start with `ant`, `ind`, `end,` `and`
`@/json/raw-solo-dict.json` (DISABLED) | Used for inputing series of raw slash-separated strokes<br />Entered using `PHRAU` from `custom-commands.json` and exited using `PHRAU`
`@/json/main.patch.dicp` | Patch dictionary for removing bad entries from `main.json` that cause boundary conflicts
`./commands.json` | *Builtin*
`./main.json` (DISABLED) | *Builtin*
🡳 *`@/downloads/rh-numpad.json` | [Aerick's right-hand numpad dictionary](https://github.com/aerickt/steno-dictionaries/blob/main/rh-numpad.json)
`@/py/control-seqs/fingerspelling_control_seqs.py` | Python dictionary that defines control sequence combinations, where letters are the accessed the same as through fingerspelling
`@/py/unicode_entry.py` | Python dictionary that allows arbitrary unicode character input based on its codepoint
`@/py/caret-and-number-folding.fold-py` | Python folding dictionary that supports folding `^` and `#` for affixes according to the rules above
`@/py/orth-chording/ipa_chording.py` (DISABLED) | Python dictionary for chording IPA syllables
`@/py/orth-chording/orth_chording.py` (DISABLED) | Python dictionary for orthographic chording

🡳 indicates an external downloaded dictionary.

🡴 indicates a dictionary not located here.