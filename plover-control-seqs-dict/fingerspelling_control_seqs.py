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
    ("K-",): "k",
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

    ("#", "R-"): "1",
    ("#", "W-"): "2",
    ("#", "K-"): "3",
    ("#", "H-", "R-"): "4",
    ("#", "P-", "W-"): "5",
    ("#",): "0",
    ("#", "T-", "K-"): "6",
    ("#", "H-"): "7",
    ("#", "P-"): "8",
    ("#", "T-"): "9",

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

    ("#", "R-", "-R"): "f1",
    ("#", "W-", "-R"): "f2",
    ("#", "K-", "-R"): "f3",
    ("#", "H-", "R-", "-R"): "f4",
    ("#", "P-", "W-", "-R"): "f5",
    ("#", "W-", "A-", "-R"): "f12",

    ("K-", "-E", "-U"): "left",
    ("W-", "-E", "-U"): "down",
    ("R-", "-E", "-U"): "right",
    ("P-", "-E", "-U"): "up",

    ("*",): "",
}

# _CONTROL_IDENTIFIER_SUBSTROKE = Stroke.from_keys(["-L", "-G", "-T", "-S"])

# _NO_CTRL_SUBSTROKE = Stroke.from_keys(["-B"])
# _MODIFIER_SUBSTROKE_CMDS = (
#     (Stroke.from_keys(["-P"]), "shift_l"),
#     (Stroke.from_keys(["-F"]), "alt_l"),
#     (Stroke.from_keys(["-R"]), "meta_l"),
# )

_CONTROL_IDENTIFIER_SUBSTROKE = Stroke.from_steno("-TSDZ")

# _NO_CTRL_SUBSTROKE = Stroke.from_keys(["-G"])
_MODIFIER_SUBSTROKE_CMDS = (
    (Stroke.from_steno("-B"), "control_l"),
    (Stroke.from_steno("-P"), "shift_l"),
    (Stroke.from_steno("-L"), "alt_l"),
    (Stroke.from_steno("-G"), "super_l"),
)

_NO_SPACE_SUBSTROKE = Stroke.from_steno("-F")

#region Exports

LONGEST_KEY = 1


def lookup(key: tuple[str]) -> str:
    stroke: Stroke = Stroke.from_steno(key[0])

    if _CONTROL_IDENTIFIER_SUBSTROKE not in stroke: raise KeyError
    stroke -= _CONTROL_IDENTIFIER_SUBSTROKE

    translation = "{}"

    for (substroke, command) in _MODIFIER_SUBSTROKE_CMDS:
        if substroke in stroke:
            translation = translation.format(f"{command}({{}})")
            stroke -= substroke

    if translation == "{}":
        translation = "control_l({})"

    no_space = False
    if _NO_SPACE_SUBSTROKE in stroke:
        no_space = True
        stroke -= _NO_SPACE_SUBSTROKE


    fingerspell_sequence = stroke.keys()
    if fingerspell_sequence not in _KEYMAP: raise KeyError
    target_key = _KEYMAP[fingerspell_sequence]


    translation = f"{{#{translation.format(target_key)}}}"
    if no_space:
        translation += "{^}"
    return translation


#endregion
