`orth_chording.py` is the main orthographic dictionary. *(`orth_entry.py` is an extra, experimental dictionary that allows you to enter the orthographic dictionary by folding a certain chord into a stroke. It may be clunky to use without extra keys, and it is not required in order to use the main orthographic dictionary.)*

Both `orth_chording.py` and `orth_entry.py` are Python dictionaries and thus require the [`plover-python-dictionary`](https://pypi.org/project/plover-python-dictionary/) plugin to be installed. This plugin can be installed from the Plugin Manager.

By default, these dictionaries use commands from the [`plover-dict-commands`](https://pypi.org/project/plover-dict-commands/) plugin to enter and exit the orthographic dictionary, namely `{plover:solo_dict}` and `{plover:end_solo_dict}`.  This plugin can also be installed from the Plugin Manager.

When manually defining an entry to enter the orthographic dictionary, you can use `{plover:solo_dict}` to disable all other dictionaries and enable only the orthographic dictionary. For instance, you can define an entry for `{plover:solo_dict:+orth_chording.py}` and also include in the command whatever other dictionaries you wish to have available.

The orthographic dictionary should be <u>disabled</u> when not in solo dict mode, since it can generate translations for (essentially) every stroke, which interferes with folding and untranslates.

Exit is handled by a special entry which translates to `{plover:end_solo_dict}`. By default, the stroke `-TSDZ` is mapped to this.

## Setting up `orth_entry.py` (experimental)
`orth_entry.py` uses tricky janky module imports to exactly mimic the behavior of the `orth_chording.py` dictionary even while it is disabled.

To set up `orth_entry.py`, open it in a text editor and:
* Set the `_MODULE_PATH` variable to the <u>absolute path</u> of the `orth_chording.py` file.
* Update the `_ENABLED_DICTS` list to customize which dictionaries should still be enabled while in the orth dict mode.

Note that after editing the `orth_chording.py` Python dictionary and reloading dictionaries from Plover, the orth dict translations from `orth_entry.py` may not be affected until after restarting Plover.