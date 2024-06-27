from plover.steno import Stroke

_CHORD_KEYMAP = {
    "A": "a",
    "PW": "b",
    "KR": "c",
    "KPW": "c",
    "TK": "d",
    "E": "e",
    "TP": "f",
    "TKPW": "g",
    "H": "h",
    "EU": "i",
    "SKWR": "j",
    "K": "k",
    "HR": "l",
    "PH": "m",
    "TPH": "n",
    "O": "o",
    "P": "p",
    "KW": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "SR": "v",
    "W": "w",
    "KP": "x",
    "KWR": "y",
    "STK": "z",
    "STKPW": "z",

    "#": "0",
    "#R": "1",
    "#W": "2",
    "#K": "3",
    "#HR": "4",
    "#PW": "5",
    "#TK": "6",
    "#H": "7",
    "#P": "8",
    "#T": "9",

    "R-R": "return",
    "PWHR": "backspace",
    "PWH": "delete",
    "SP": "space",
    "TA": "tab",
    "TPE": "escape",
    "PHR": "plus",
    "KWHR": "equals",
    "SH": "minus",
    "KH": "asciitilde", # backtick ("grave" will not work)
    "OEU": "slash",

    "#R-R": "f1",
    "#W-R": "f2",
    "#K-R": "f3",
    "#HR-R": "f4",
    "#PW-R": "f5",
    "#TK-R": "f6",
    "#H-R": "f7",
    "#P-R": "f8",
    "#T-R": "f9",
    "#-R": "f10",
    "#RAR": "f11",
    "#WAR": "f12",
    "#KAR": "f13",
    "#HRAR": "f14",
    "#PWAR": "f15",
    "#TKAR": "f16",
    "#HAR": "f17",
    "#PAR": "f18",
    "#TAR": "f19",
    "#AR": "f20",
    "#ROR": "f21",
    "#WOR": "f22",
    "#KOR": "f23",
    "#HROR": "f24",

    "KEU": "left",
    "WEU": "down",
    "REU": "right",
    "PEU": "up",

    "*": "",
}

_KEYMAP = {
    Stroke.from_steno(chord).keys(): keyname
    for chord, keyname in _CHORD_KEYMAP.items()
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


def lookup(key: tuple[str, ...]) -> str:
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
