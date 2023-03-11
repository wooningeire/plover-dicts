## Temporary setup instructions
`orth_entry.py` uses tricky module imports to exactly mimic the behavior of the `orth_fingerspelling.py` dictionary before running the solo dict command.

To set up `orth_entry.py`:
* Set the `_MODULE_PATH` variable to the __absolute path__ of the `orth_fingerspelling.py` file.
* Set the line near the end containing the `{plover:solo_dict:...}` command to customize which dictionaries should still be enabled while in the orth dict mode.

Note that after editing the `orth_fingerspelling.py` Python dictionary and reloading dictionaries from Plover, the orth dict translations from `orth_entry.py` may not be affected until after restarting Plover.