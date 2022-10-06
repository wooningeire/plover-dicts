from plover.steno import Stroke

_FINGERSPELL_LETTERS = {
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

    # ("K-", "H-"): "tilde",
    
    ("R-", "-R"): "return",
    ("P-", "W-", "H-"): "delete",
    ("S-", "P-"): "space",
    ("T-", "A-"): "tab",
}

_CONTROL_IDENTIFIER_SUBSTROKE = Stroke.from_keys(["-L", "-T", "-S"])

_SHIFT_SUBSTROKE = Stroke.from_keys(["-P"])

#region Exports

LONGEST_KEY = 1

def lookup(key: tuple[Stroke]) -> str:
    stroke = Stroke.from_steno(key[0])

    if _CONTROL_IDENTIFIER_SUBSTROKE not in stroke: raise KeyError

    if _SHIFT_SUBSTROKE in stroke:
        shift = True
        stroke -= _SHIFT_SUBSTROKE
    else:
        shift = False


    fingerspell_sequence = (stroke - _CONTROL_IDENTIFIER_SUBSTROKE).keys()
    if fingerspell_sequence not in _FINGERSPELL_LETTERS: raise KeyError

    letter = _FINGERSPELL_LETTERS[fingerspell_sequence]


    if shift:
        return f"{{#Control_L(Shift_L({letter}))}}"
    else:
        return f"{{#Control_L({letter})}}"
        

#endregion