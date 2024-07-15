from plover.steno import Stroke

_MAIN_SYMBOL_KEYMAP = {
    "": "{^ ^}",

    #region qwerty shift + number
    "S": "!",
    "T": "@",
    "P": "#",
    "H": "$",
    "A": "%",
    "-F": "^",
    "-P": "&",
    "-L": "*",
    #endregion

    "-T": "\"",
    "-D": "'",

    "-S": ":",
    "-Z": ";",

    "R": ".",
    "-R": ",",
    "ST": "?",
    "KWR": "...",
    "SKWR": "…",

    #region brackets
    "K": "(",
    "W": r"\{",
    "KW": "[",
    "TKP": "⟨",
    "KP": "<",
    "KPW": "≤",

    "-PBG": "≥",
    "-PG": ">",
    "-PLG": "⟩",
    "-BG": "]",
    "-B": r"\}",
    "-G": ")",
    #endregion

    "-FP": "-",
    "-RB": "_",
    "-FRPB": "=",
    "-FRPBLG": "≡",
    "-FR": "|",
    "-FPL": "–",
    "-FPLT": "—",

    "PH": "+",
    "WR": "×",
    "PWHR-RP": "≠",

    "PR": "\\",
    "-RP": "/",

    "TK": "~",
    "KH": "`",
    
    "T*P": "ᵀ",

    #region control sequences
    "R-R": r"\n",
    #endregion


    #region compounds
    "R-T": ". \"",
    "R*T": "\".",
    "RA*T": ".\"",

    "-RT": ", \"",
    "*RT": "\",",
    "A*RT": ",\"",

    "KR": ". (",

    "R-G": ").",
    "R*G": ".)",

    "-RG": "),",

    "K-G": "()",
    "W-B": r"\{\}",
    "KW-BG": "[]",
    "KP-PG": "<>",

    "K-T": "(\"",
    "-GT": "\")",
    #endregion


    #region mnemonics
    "H-F": "?",
    "KW-PL": "?",
    "TP-BG": "!",
    "SKP": "&",
    "KPWR-FPBD": "&",
    "TKHR-R": "$",
    "P-RS": "%",
    "KW-LS": "=",
    "PHR-S": "+",
    "T-PLS": "×",
    "PH-PBS": "−",
    "TK-FD": "/",
    "TPH-RB": "–",
    "PH-RB": "—",
    "HR-PB": "<",
    "HR-BG": "≤",
    "TKPW-PB": ">",
    "TKPWR-PB": ">",
    "TKPW-BG": "≥",
    "TKPWR-BG": "≥",
    "T-LD": "~",
    "KH-BG": "✓",
    "KR-S": "✗",
    #endregion
}

_FORMATTED_SYMBOL_MAP = {
    ".": "{.}",
    "...": "{^}...",
    "…": "{^}…",
    ",": "{,}",
    "!": "{!}",
    "?": "{?}",
    ":": "{:}",
    ";": "{;}",
    "%": "{^}%",
    "(": "{~|(^}",
    "[": "{~|[^}",
    "{": r"{~|\{^}",
    ")": "{^~|)}",
    "]": "{^~|]}",
    "}": r"{^~|\}}",
    "\"": "{~|\"^}",
    "'": "{~|'^}",
    ". \"": "{^}. \"{^}{-|}",
    ", \"": "{^}, \"{^}",
    ".\"": "{^}.\"{-|}",
    "\".": "{^}\"{.}",
    ",\"": "{^~|,\"}",
    "\",": "{^}\"{,}",
    ").": "{^}){.}",
    ".)": "{^}.){-|}",
    "),": "{^}){,}",
    ". (": "{^}. ({^}{-|}",
}
_ASTERISK_FORMATTED_SYMBOL_MAP = {
    ".": "{^}.",
    "...": "{^}... {-|}",
    "…": "{^}… {-|}",
    "!": "{^}!",
    "?": "{^}?",
    "\"": "{^~|\"}",
    "'": "{^~|'}",
}

_KEYMAP = {
    Stroke.from_steno(chord).keys(): keyname
    for chord, keyname in _MAIN_SYMBOL_KEYMAP.items()
}

_IDENTIFIER_SUBSTROKE = Stroke.from_steno("_")

_FORMATTED_SUBSTROKE = Stroke.from_steno("O")

_SPACING_BEFORE_SUBSTROKE = Stroke.from_steno("E")
_SPACING_AFTER_SUBSTROKE = Stroke.from_steno("U")

_DOUBLE_SUBSTROKE = Stroke.from_steno("+")
_TRIPLE_SUBSTROKE = Stroke.from_steno("^")

_ASTERISK_SUBSTROKE = Stroke.from_steno("*")

#region Exports

LONGEST_KEY = 1


def lookup(key: tuple[str, ...]) -> str:
    stroke: Stroke = Stroke.from_steno(key[0])

    if _IDENTIFIER_SUBSTROKE not in stroke: raise KeyError
    stroke -= _IDENTIFIER_SUBSTROKE

    translation = "{}"
    n_repetitions = 1
    use_formatted = False
    use_asterisk_formatted = False

    if _FORMATTED_SUBSTROKE in stroke:
        use_formatted = True
        stroke -= _FORMATTED_SUBSTROKE

    if _SPACING_BEFORE_SUBSTROKE in stroke:
        translation = "{{^ ^}} " + translation
        stroke -= _SPACING_BEFORE_SUBSTROKE
    else:
        translation = "{{^}} " + translation

    if _SPACING_AFTER_SUBSTROKE in stroke:
        translation += " {{^ ^}}"
        stroke -= _SPACING_AFTER_SUBSTROKE
    else:
        translation += " {{^}}"

    if _DOUBLE_SUBSTROKE in stroke:
        n_repetitions += 1
        stroke -= _DOUBLE_SUBSTROKE

    if _TRIPLE_SUBSTROKE in stroke:
        n_repetitions += 2
        stroke -= _TRIPLE_SUBSTROKE


    keys = stroke.keys()
    if keys not in _KEYMAP and use_formatted and _ASTERISK_SUBSTROKE in stroke:
        use_asterisk_formatted = True
        stroke -= _ASTERISK_SUBSTROKE
        keys = stroke.keys()

    if keys not in _KEYMAP:
        raise KeyError
    symbol = _KEYMAP[keys]

    if use_asterisk_formatted and symbol in _ASTERISK_FORMATTED_SYMBOL_MAP:
        translation = "{}"
        symbol = _ASTERISK_FORMATTED_SYMBOL_MAP[symbol]

    elif use_formatted and symbol in _FORMATTED_SYMBOL_MAP:
        translation = "{}"
        symbol = _FORMATTED_SYMBOL_MAP[symbol]

    translation = translation.format(symbol * n_repetitions)
    
    return translation


#endregion
