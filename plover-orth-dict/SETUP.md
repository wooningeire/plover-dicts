`orth_chording.py` is the main orthographic dictionary.

`orth_chording.py` is a Python dictionaries and thus requires the [`plover-python-dictionary`](https://pypi.org/project/plover-python-dictionary/) plugin to be installed. This plugin can be installed from the Plugin Manager.

By default, this dictionary uses commands from the [`plover-dict-commands`](https://pypi.org/project/plover-dict-commands/) plugin to enter and exit the orthographic dictionary, namely `{plover:solo_dict}` and `{plover:end_solo_dict}`.  This plugin can also be installed from the Plugin Manager.

When manually defining an entry to enter the orthographic dictionary, you can use `{plover:solo_dict}` to disable all other dictionaries and enable only the orthographic dictionary. For instance, you can define an entry for `{plover:solo_dict:+orth_chording.py}` and also include in the command whatever other dictionaries you wish to have available.

The orthographic dictionary should be <u>disabled</u> when not in solo dict mode, since it can generate translations for (essentially) every stroke, which interferes with folding and untranslates.

Exit is handled by a special entry which translates to `{plover:end_solo_dict}`. By default, the stroke `-TSDZ` is mapped to this.