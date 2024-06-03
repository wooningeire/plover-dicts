from plover.steno import Stroke

_CHORD_KEYMAP = {
    "K": "(",
    "W": "\\{",
    "WR": "[",
    "PH": "<",

    "-FP": ">",
    "-RB": "]",
    "-B": "\\}",
    "-G": ")",

    "S": "!",
    "T*P": "ᵀ",
    "KW-L": "=",
    "PHR-S": "+",
    "R": ".",
    "A": "%",
    "-R": ",",
    "-S": ":",
    "-Z": ";",
}

_KEYMAP = {
    Stroke.from_steno(chord).keys(): keyname
    for chord, keyname in _CHORD_KEYMAP.items()
}

_IDENTIFIER_SUBSTROKE = Stroke.from_steno("_^")

_SPACING_SUBSTROKE_BEFORE = Stroke.from_steno("E")
_SPACING_SUBSTROKE_AFTER = Stroke.from_steno("U")

#region Exports

LONGEST_KEY = 1


def lookup(key: tuple[str]) -> str:
    stroke: Stroke = Stroke.from_steno(key[0])

    if _IDENTIFIER_SUBSTROKE not in stroke: raise KeyError
    stroke -= _IDENTIFIER_SUBSTROKE

    translation = "{}"

    if _SPACING_SUBSTROKE_BEFORE not in stroke:
        translation = "{{^}}" + translation
    else:
        stroke -= _SPACING_SUBSTROKE_BEFORE

    if _SPACING_SUBSTROKE_AFTER not in stroke:
        translation += "{{^}}"
    else:
        stroke -= _SPACING_SUBSTROKE_AFTER

    keys = stroke.keys()
    if keys not in _KEYMAP: raise KeyError
    target_key = _KEYMAP[keys]

    translation = translation.format(target_key)
    
    return translation


#endregion
