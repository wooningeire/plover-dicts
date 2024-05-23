from plover.steno import Stroke
from plover.system import KEYS
# TODO glitchy behavior when switching systems, and system does not update properly. Due to script or something else?


from collections import defaultdict
from enum import Enum

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    KEYS: tuple[str] = ()

class Modifier(Enum):
    WORD_BOUNDARY = 0
    CAPS = 1
    EXIT = 2
    CONNECT_BEFORE = 3
    CONNECT_AFTER = 4


_CHORDS = {
    # MODIFIERS

    "#": ("", (Modifier.CAPS,)),

    # LEFT BANK

    "S": ("s", ()),
    "T": ("t", ()),
    "K": ("c", ()),
    "P": ("p", ()),
    "W": ("w", ()),
    "H": ("h", ()),
    "R": ("r", ()),

    "STKPW": ("z", ()),
    "SKWR": ("j", ()),
    "SR": ("v", ()),
    "TK": ("d", ()),
    "TKPW": ("g", ()),
    "TP": ("f", ()),
    "TPH": ("n", ()),
    "KP": ("x", ()),
    "KPW": ("k", ()),
    "KW": ("q", ()),
    "KWR": ("y", ()),
    "PW": ("b", ()),
    "PH": ("m", ()),
    "HR": ("l", ()),

    "SWHR": ("shr", ()),
    "TWHR": ("thr", ()),
    "KWHR": ("chr", ()),

    "STK": ("dis", ()),
    "SKP": ("ss", ()),
    "SKPW": ("sk", ()),
    "SWR": ("sr", ()),
    "TKPH": ("kn", ()),
    "TKWHR": ("rh", ()),
    "TPW": ("phl", ()),
    "TPWH": ("ph", ()),
    "TPWR": ("rh", ()),
    "KWH": ("qu", ()),
    "WHR": ("hr", ()),

    "TPHR": ("fl", ()),
    "PHR": ("pl", ()),

    "STPHR": ("'", ()), # mirrors right-hand apostrophe

    # VOWELS

    "A": ("a", ()),
    "O": ("o", ()),
    "E": ("e", ()),
    "U": ("u", ()),
    "AO": ("oo", ()),
    "AE": ("ea", ()),
    "EU": ("i", ()),
    "AOE": ("ee", ()),
    "AOU": ("ue", ()),
    "AEU": ("ai", ()),
    "AOEU": ("eu", ()),

    "A*": ("ia", ()),
    "O*": ("io", ()),
    "*E": ("ie", ()),
    "*U": ("iu", ()),
    "AO*": ("oa", ()),
    "A*E": ("ae", ()),
    "A*U": ("aw", ()),
    "O*E": ("eo", ()),
    "O*U": ("ow", ()),
    "*EU": ("y", ()),
    "AO*E": ("ei", ()),
    "AO*U": ("iou", ()),
    "A*EU": ("ay", ()),
    "O*EU": ("oy", ()),
    "AO*EU": ("ew", ()),

    # RIGHT BANK

    "-F": ("f", ()),
    "-R": ("r", ()),
    "-P": ("p", ()),
    "-B": ("b", ()),
    "-L": ("l", ()),
    "-G": ("g", ()),
    "-T": ("t", ()),
    "-S": ("s", ()),
    "-D": ("d", ()),
    "-Z": ("z", ()),

    "-FB": ("v", ()),
    "-PB": ("n", ()),
    "-PL": ("m", ()),
    "-BGS": ("x", ()),
    "-BG": ("k", ()),

    "-FR": ("rf", ()),
    "-FRP": ("mp", ()),
    "-FRPB": ("rch", ()),
    "-FRPBLG": ("nch", ()),
    "-FRPLG": ("rph", ()),
    "-FRB": ("rv", ()),
    "-FRBL": ("mb", ()),
    "-FRG": ("rgh", ()),
    "-FP": ("ch", ()),
    "-FPB": ("sh", ()),
    "-FPBL": ("tch", ()),
    "-FPBG": ("nk", ()),
    "-FPL": ("sm", ()),
    "-FPLG": ("ph", ()),
    "-FPG": ("sc", ()),
    "-FBLGT": ("ction", ()),
    "-FBG": ("sk", ()),
    "-FLG": ("lk", ()),
    "-FLT": ("st", ()),
    "-FG": ("gh", ()),
    "-PBLGT": ("j", ()),
    "-PBLG": ("dg", ()),
    "-PLG": ("pl", ()),
    "-BLG": ("ck", ()),
    "-BLGT": ("tion", ()),
    "-BGZ": ("ks", ()),
    "-DZ": ("ds", ()),

    "-FSZ": ("ff", ()),
    "-FRSZ": ("hh", ()),
    "-PBSZ": ("nn", ()),
    "-LSZ": ("ll", ()),
    "-SZ": ("ss", ()),
    

    # EXPERIMENTATION ZONE

    # c
    "-PG": ("c", ()),
    "-FRPBG": ("nc", ()),
    # "-FBG": ("c", ()),
    # "-FRBG": ("rc", ()),
    # "-FPBLG": ("nc", ()),

    # h
    "-FRLG": ("h", ()),
    "-FRPBD": ("hn", ()),
    "-FRPBDZ": ("hns", ()),
    "-FRBG": ("hk", ()),
    # "-FRPBL": ("hr", ()),
    # "-FRPBG": ("hk", ()),

    # w
    "-FBL": ("w", ()),
    # "-FPG": ("wn", ()),
    # "-RPG": ("wr", ()),
    # "-PLG": ("wl", ()),
    # "-PG": ("w", ()),

    # q
    "-FPBLG": ("q", ()),

    # th
    # "-PLGT": ("th", ()),
    "-GT": ("th", ()),
    
    
    # ENDING VOWELS

    "-TSDZ": ("y", ()),
    "-TD": ("e", ()),

    "-FRT": ("te", ()),
    "-FRS": ("se", ()),
    "-FRD": ("de", ()),
    "-FRZ": ("ze", ()),
    "-FRTS": ("tes", ()),
    "-FRDZ": ("des", ()),
    "-FRLS": ("lse", ()),
    "-FRGT": ("the", ()),
    "-FPBT": ("ty", ()),
    "-FPBS": ("sy", ()),
    "-FPBD": ("dy", ()),
    "-FPBZ": ("zy", ()),
    "-FPBLS": ("lsy", ()),
    "-FPBGT": ("thy", ()),

    "-FRPBT": ("nte", ()),
    "-FRPBS": ("nse", ()),
    # "-FPBT": ("nty", ()),
    # "-FPBS": ("nsy", ()),

    "-FRPLTD": ("mple", ()),
    "-FRTD": ("he", ()),
    "-FLTD": ("fle", ()),
    "-GTD": ("ge", ()),
    "-FRPLTSDZ": ("mply", ()),

    "-PBLGTD": ("dge", ()),
    "-PBLGTSDZ": ("dgy", ()),

    # "-PLGTD": ("the", ()),
    # "-PLGTSDZ": ("thy", ()),

    # experimentation zone 

    # "-GD": ("y", ()),
    "-GSZ": ("a", ()),
    "-GD": ("i", ()),
    "-GDZ": ("o", ()),
    "-GZ": ("u", ()),


    # PUNCTUATION

    "-FPLT": (".", ()),
    "-FRPLT": ("'", ()),
    "-FPBLT": ("-", (Modifier.CONNECT_AFTER,)),
    "-FPBLTD": ("—", (Modifier.CONNECT_AFTER,)),
}

# Entries which are translated normally
_SPECIAL_ENTRIES = {
    "S-P": "{^ ^}",
    "KPA": "{}{-|}",
    "KPA*": "{^}{-|}",
    "SKW-T": "{^}'{^}",
    "TP-PL": "{.}",
    "KW-BG": "{,}",
    "TP-BG": "{!}",
    "KW-PL": "{?}",
    "H-F": "{?}",
    "H-PB": "{^}-{^}",
}


# Change control chords and special entries depending on whether an extended stenotype system is being used

# For regular extended stenotype
if "^-" in KEYS and "_" not in KEYS and "&-" not in KEYS:
    _CHORDS.update({
        # MODIFIERS

        "^": ("", (Modifier.WORD_BOUNDARY,)),
    })

    _SPECIAL_ENTRIES.update({
        "-TSDZ": "{#}{plover:end_solo_dict}",
    })

# For custom extended stenotype
elif "^-" in KEYS and "_" in KEYS and "&-" in KEYS:
    _CHORDS.update({
        # MODIFIERS

        "^": ("", (Modifier.CONNECT_BEFORE,)),
        "_": ("", (Modifier.WORD_BOUNDARY,)),
        "&": ("", (Modifier.EXIT,)),

        # VOWELS

        # "_A": "ua",
        # "_O": "uo",
        # "_E": "ue",
        # "_U": "uu",
        # "_AO": "ao",
        # "_EU": "ui",
        # "_AOE": "ii",

        # "_A*": "ya",
        # "_O*": "yo",
        # "_*E": "ye",
        # "_*U": "yu",
        # "_*EU": "yi",
        # "_AO*E": "ey",
        # "_AO*EU": "eye",
    })

    _SPECIAL_ENTRIES.update({
        "&": "{#}{plover:end_solo_dict}",
        "_": "{^ ^}",
    })

# For regular English stenotype and other systems
else:
    _SPECIAL_ENTRIES.update({
        "-TSDZ": "{#}{plover:end_solo_dict}",
    })


# Build the dictionary which is used to identify chords in a stroke

_CHORD_RESULT = "chord" # arbitrary string

_construct_trie = lambda: defaultdict(_construct_trie)
_trie = _construct_trie()
for chord, entry in _CHORDS.items():
    current_dict = _trie
    for key in Stroke.from_steno(chord).keys():
        current_dict = current_dict[key]
    
    current_dict[_CHORD_RESULT] = entry


_UNDO_STROKE = "*"


#region Exports

LONGEST_KEY = 1


def lookup(strokes_steno: tuple[str]) -> str:
    steno = strokes_steno[0]

    if steno == _UNDO_STROKE: raise KeyError

    if steno in _SPECIAL_ENTRIES:
        return _SPECIAL_ENTRIES[steno]


    out = ""
    modifiers: set[Modifier] = set()

    keys: tuple[str] = Stroke.from_steno(strokes_steno[0]).keys()

    chord_start_index = 0
    while chord_start_index < len(keys):
        current_trie = _trie

        longest_chord_found, longest_chord_modifiers = ("", ())
        longest_chord_end_index = chord_start_index

        for seek_index in range(chord_start_index, len(keys)):
            key = keys[seek_index]
            
            if key not in current_trie: break
            current_trie = current_trie[key]

            if _CHORD_RESULT in current_trie:
                longest_chord_found, longest_chord_modifiers = current_trie[_CHORD_RESULT]
                longest_chord_end_index = seek_index


        out += longest_chord_found
        modifiers.update(longest_chord_modifiers)

        chord_start_index = longest_chord_end_index + 1


    translation = f"{{&{out}}}" if len(out) > 0 else ""
    
    if Modifier.WORD_BOUNDARY in modifiers:
        translation = "{~|}" + translation
    if Modifier.CAPS in modifiers:
        translation = "{-|}" + translation
    if Modifier.CONNECT_BEFORE in modifiers:
        translation = "{^}" + translation
    if Modifier.EXIT in modifiers:
        translation += "{plover:end_solo_dict}"
    if Modifier.CONNECT_AFTER in modifiers:
        translation += "{^}"

    return translation


#endregion
