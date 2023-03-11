## Dictionaries
Located in `./user-dicts/` relative to Plover AppData directory

Dictionary | Desc
-|-
`user.json` | The inner machinations of my mind
`names.json` | Names of people and brands
`math.json` | Math terminology
`dragon.json` | Dragon terminology and names
`class.json` | Terms for various class subjects
`notion.json` | Shortcuts for Notion
`latex.json` | LaTeX character and symbol sequences<br />`TWHR` prefix
`rust.json` | Idioms and terminology from Rust
`unicode-typography.json` | Unicode characters and their relevant spacing/capitalization
`custom-commands.json` | Commands<br />`PWH` prefix for text deletion. Right-hand side is based on navigation commands
`spacing-and-capitalization.json` | Spacing and capitalization commands<br />`KPWAO` prefix. Adding `E` removes the space<br />Some right-hand side commands are partially based on navigation commands; upper row is for uppercase, lower row is for lowercase, symmetric keys for both rows is for spacing, other combinations of the rows for miscellaneous things<br /><ul><li>`-` Reset mode</li><li>`-PBLG` Reset casing mode</li><li>`-PBTS` Reset spacing mode</li><li>`-F` Capitaize last</li><li>`-R` Uncapitalize last</li><li>`-P` Capitalize next</li><li>`-B` Uncapitalize next</li><li>`-L` Caps next</li><li>`-PL` Caps mode</li><li>`-BG` Lower mode</li><li>`-FR` Retro add space</li><li>(`EFR` Retro remove space)</li><li>`-PB` Space next</li></ul>Additional modes:<ul><li>`-PLT` Camel mode</li><li>`*PLT` Pascal mode</li><li>`-BGS` Snake mode</li><li>`-PBLGS` Screaming snake mode</li><li>`-LT` Title mode</li><li>`-GS` Kebab mode</li><li>`-TS` No spaces mode</li></ul>
`plover-recommended-dictionary-commands.json` | Recommended entries for commands from the [dictionary format](https://github.com/openstenoproject/plover/wiki/Dictionary-Format) wiki page
`mistakes.json` | Misstrokes and bad habits
`spw-inc_enc_anc_ant.json` | Entries that use the chord `SPW-` for words that start with `ant`, `inc`, `enc`, `anc`
`kpw-imp_emp_amp_imb_emb_amb.json` | Entries that use the chord `KPW-` for words that start with `imp`, `emp`, `amp`, `imb`, `emb`, `amb`
`../commands.json` | *Builtin*
`main.patch.dicp` | Patch dictionary for removing bad entries from `main.json` that cause boundary conflicts
`../main.json` | *Builtin*