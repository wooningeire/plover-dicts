from plover.steno import Stroke

from collections import defaultdict

# TODO temp, not ideal
_WORD_BOUNDARY = " "
_CAPS = "{-|}"
_EXIT = "<exit>"
_CONNECT = "^"

_CHORDS = {
    # Extended stenotype control chords
    "^": _WORD_BOUNDARY,
    "#": _CAPS,
    ".": _EXIT,
    "+": _EXIT,
    
    # "#": _WORD_BOUNDARY,  # for non-extended stenotype

    "STKPW": "z",
    "SKWR": "j",
    "STK": "dis",
    "SKP": "ss",
    "SKPW": "sk",
    "SWHR": "shr",
    "SWR": "sr",
    "SR": "v",
    "S": "s",
    "TKPW": "g",
    # "TKPH": "dem",
    "TKPH": "kn",
    # "TKHR": "del",
    "TKWHR": "rh",
    "TKP": "dep",
    "TK": "d",
    "TPHR": "fl",
    "TPWH": "ph",
    "TPW": "phl",
    "TPWR": "rh",
    "TPH": "n",
    "TP": "f",
    "TWHR": "thr",
    "T": "t",
    "KWR": "y",
    "KP": "x",
    "KW": "q",
    "KWHR": "chr",
    "KWH": "qu",
    "KHR": "cl",
    "KH": "ch",
    "KPW": "k",
    "K": "c",
    "PW": "b",
    "WHR": "hr",
    "W": "w",
    "PHR": "pl",
    "PH": "m",
    "P": "p",
    "HR": "l",
    "H": "h",
    "R": "r",

    "AOEU": "y",
    "AOE": "ee",
    "AOU": "ue",
    "AO": "oo",
    "AEU": "ai",
    "AE": "ea",
    "A": "a",
    "O": "o",
    "EU": "i",
    "E": "e",
    "U": "u",

    "AO*EU": "ew",
    "AO*E": "ei",
    "AO*U": "iou",
    "AO*": "oa",
    "A*EU": "ay",
    "A*E": "ae",
    "A*U": "aw",
    "A*": "ia",
    "O*EU": "oy",
    "O*E": "eo",
    "O*U": "ow",
    "O*": "io",
    "*EU": "eu",
    "*E": "ie",
    "*U": "iu",

    "-FRPBLG": "nch",
    "-FRPB": "rch",
    "-FRPL": "rph",
    "-FPL": "ph",
    "-FSZ": "ff",
    "-FRBL": "rv",
    "-FRB": "rf",
    "-FP": "ch",
    "-FPBL": "tch",
    "-FPBG": "nk",
    "-FLG": "lk",
    "-FPB": "sh",
    "-FPBS": "cious",
    "-FLT": "st",
    "-FB": "v",
    "-FG": "gh",
    "-FRG": "rgh",
    "-FRP": "mp",
    "-F": "f",
    "-R": "r",
    "-PBSZ": "nn",
    "-PBLGT": "j",
    "-PBLG": "dg",
    "-PB": "n",
    "-PL": "m",
    "-P": "p",
    "-BLG": "ck",
    "-BGS": "x",
    # "-BGD": "by",
    "-BGZ": "ks",
    "-BG": "k",
    "-B": "b",
    "-LSZ": "ll",
    "-L": "l",
    "-PLGT": "th",
    "-G": "g",
    "-T": "t",
    "-SZ": "ss",
    "-S": "s",
    "-DZ": "ds",  # for extended stenotype
    # "-TDZ": "{-|}t",  # for non-extended stenotype
    # "-DZ": "{-|}",  # for non-extended stenotype
    "-D": "d",
    "-Z": "z",
    

    # EXPERIMENTATION ZONE

    # c
    "-PG": "c",
    "-FPG": "nc",
    # "-FBG": "c",
    # "-FRBG": "rc",
    # "-FPBLG": "nc",

    # h
    "-FR": "h",
    "-FRPBL": "hr",
    "-FRPBG": "hk",

    # w
    "-FBG": "w",
    # "-FPG": "wn",
    # "-RPG": "wr",
    # "-PLG": "wl",
    # "-PG": "w",

    # q
    "-FPBLG": "q",
    
    
    # ENDING VOWELS

    "-TD": "e",
    "-TSDZ": "y",
    # "-GD": "y",
    "-GD": "a",
    "-GDZ": "i",
    "-TDZ": "u",  # shift
    "-SD": "a",  # shift
    "-SDZ": "o",  # shift

    "-FRT": "te",
    "-FRS": "se",
    "-FRD": "de",
    "-FRZ": "ze",
    "-FRTS": "tse",
    "-FRDZ": "dse",
    "-FRLS": "lse",

    "-FLTD": "fle",

    "-PBLGTD": "dge",
    "-PBLGTSDZ": "dgy",

    "-FPLTD": "phe",
    "-FPLTSDZ": "phy",
    "-FRPLTD": "rphe",
    "-FRPLTSDZ": "rphy",

    "-PLGTD": "the",
    "-PLGTSDZ": "thy",


    # PUNCTUATION

    "-FPLT": ".",
    "-FRPLT": "'",
    "-FPBLT": "-" + _CONNECT,
    "-FPBLTD": "—" + _CONNECT,
}

_CHORD_RESULT = "chord"

_construct_trie = lambda: defaultdict(_construct_trie)
_trie = _construct_trie()
for chord, entry in _CHORDS.items():
    current_dict = _trie
    for key in Stroke.from_steno(chord).keys():
        current_dict = current_dict[key]
    
    current_dict[_CHORD_RESULT] = entry


_UNDO_STROKE = "*"

_special_entries = {
    "-TSDZ": "{#}{plover:end_solo_dict}",
    ".": "{#}{plover:end_solo_dict}",
    "+": "{#}{plover:end_solo_dict}",
    "S-P": "{^ ^}",
    "KPA": "{}{-|}",
    "KPA*": "{^}{-|}",
    "SKW-T": "{^}'{^}",
    "TP-PL": "{.}",
    "KW-BG": "{,}",
    "TP-BG": "{!}",
    "H-PB": "{^}-{^}",
    "H-F": "{?}",
}

#region Exports

LONGEST_KEY = 1


def lookup(strokes_steno: tuple[str]) -> str:
    steno = strokes_steno[0]

    if steno == _UNDO_STROKE: raise KeyError

    if steno in _special_entries:
        return _special_entries[steno]


    out = ""
    prefix_word_boundary = False
    capitalize = False
    exit = False
    connect = False

    keys: tuple[str] = Stroke.from_steno(strokes_steno[0]).keys()

    chord_start_index = 0
    while chord_start_index < len(keys):
        current_trie = _trie

        longest_chord_found = ""
        longest_chord_end_index = chord_start_index

        for seek_index in range(chord_start_index, len(keys)):
            key = keys[seek_index]
            
            if key not in current_trie: break
            current_trie = current_trie[key]

            if _CHORD_RESULT in current_trie:
                longest_chord_found = current_trie[_CHORD_RESULT]
                longest_chord_end_index = seek_index


        if longest_chord_found.startswith(_WORD_BOUNDARY):
            prefix_word_boundary = True
            longest_chord_found = longest_chord_found[len(_WORD_BOUNDARY):]
        if longest_chord_found.startswith(_CAPS):
            capitalize = True
            longest_chord_found = longest_chord_found[len(_CAPS):]

        if longest_chord_found.endswith(_EXIT):
            exit = True
            longest_chord_found = longest_chord_found[:-len(_EXIT)]
        if longest_chord_found.endswith(_CONNECT):
            connect = True
            longest_chord_found = longest_chord_found[:-len(_CONNECT)]

        out += longest_chord_found

        chord_start_index = longest_chord_end_index + 1


    translation = f"{{&{out}}}" if len(out) > 0 else ""
    
    if capitalize:
        translation = "{-|}" + translation
    if prefix_word_boundary:
        translation = "{~|}" + translation
    if exit:
        translation += "{plover:end_solo_dict}"
    if connect:
        translation += "{^}"

    return translation


#endregion
