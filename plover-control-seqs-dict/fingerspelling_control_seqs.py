from plover.steno import Stroke

_KEYMAP = {
    ("A-",): "a",
    ("P-", "W-"): "b",
    ("K-", "R-"): "c",
    ("T-", "K-"): "d",
    ("-E",): "e",
    ("T-", "P-"): "f",
    ("T-", "K-", "P-", "W-"): "g",
    ("H-",): "h",
    ("-E", "-U"): "i",
    ("S-", "K-", "W-", "R-"): "j",
    ("H-", "R-"): "l",
    ("P-", "H-"): "m",
    ("T-", "P-", "H-"): "n",
    ("O-",): "o",
    ("P-",): "p",
    ("K-", "W-"): "q",
    ("R-",): "r",
    ("S-",): "s",
    ("T-",): "t",
    ("-U",): "u",
    ("S-", "R-"): "v",
    ("W-",): "w",
    ("K-", "P-"): "x",
    ("K-", "W-", "R-"): "y",
    ("S-", "T-", "K-"): "z",
    ("S-", "T-", "K-", "P-", "W-"): "z",

    ("#", "S-"): "1",
    ("#", "T-"): "2",
    ("#", "P-"): "3",
    ("#", "H-"): "4",
    ("#", "A-"): "5",
    ("#", "O-"): "0",
    ("#", "K-"): "6",
    ("#", "W-"): "7",
    ("#", "R-"): "8",
    ("#", "-E"): "9",

    # ("K-", "H-"): "tilde",

    ("R-", "-R"): "return",
    ("P-", "W-", "H-", "R-"): "backspace",
    ("P-", "W-", "H-"): "delete",
    ("S-", "P-"): "space",
    ("T-", "A-"): "tab",
    ("T-", "P-", "-E"): "escape",
    ("P-", "H-", "R-"): "plus",
    ("K-", "W-", "H-", "R-"): "equals",
    ("S-", "H-"): "minus",

    ("#", "S-", "-R"): "f1",
    ("#", "T-", "-R"): "f2",
    ("#", "P-", "-R"): "f4",
    ("#", "H-", "-R"): "f4",
    ("#", "A-", "-R"): "f5",
    ("#", "S-", "T-", "-R"): "f12",

    ("*",): "",
}

# _CONTROL_IDENTIFIER_SUBSTROKE = Stroke.from_keys(["-L", "-G", "-T", "-S"])

# _NO_CTRL_SUBSTROKE = Stroke.from_keys(["-B"])
# _MODIFIER_SUBSTROKE_CMDS = (
#     (Stroke.from_keys(["-P"]), "shift_l"),
#     (Stroke.from_keys(["-F"]), "alt_l"),
#     (Stroke.from_keys(["-R"]), "meta_l"),
# )

_CONTROL_IDENTIFIER_SUBSTROKE = Stroke.from_keys(["-T", "-S", "-D", "-Z"])

_NO_CTRL_SUBSTROKE = Stroke.from_keys(["-G"])
_MODIFIER_SUBSTROKE_CMDS = (
    (Stroke.from_keys(["-P"]), "shift_l"),
    (Stroke.from_keys(["-L"]), "alt_l"),
    (Stroke.from_keys(["-F"]), "super_l"),
)

#region Exports

LONGEST_KEY = 1


def lookup(key: tuple[str]) -> str:
    stroke: Stroke = Stroke.from_steno(key[0])

    if _CONTROL_IDENTIFIER_SUBSTROKE not in stroke: raise KeyError
    stroke -= _CONTROL_IDENTIFIER_SUBSTROKE


    if _NO_CTRL_SUBSTROKE in stroke:
        translation = "{}"
        stroke -= _NO_CTRL_SUBSTROKE
    else:
        translation = "control_l({})"

    for (substroke, command) in _MODIFIER_SUBSTROKE_CMDS:
        if substroke in stroke:
            translation = translation.format(f"{command}({{}})")
            stroke -= substroke

    # if translation == "{}": raise KeyError


    fingerspell_sequence = stroke.keys()
    if fingerspell_sequence not in _KEYMAP: raise KeyError
    target_key = _KEYMAP[fingerspell_sequence]

    return f"{{#{translation.format(target_key)}}}"


#endregion
