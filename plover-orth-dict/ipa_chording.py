from plover.steno import Stroke
from plover.system import KEYS


from collections import defaultdict
from enum import Enum

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    KEYS: tuple[str] = ()

class Modifier(Enum):
    EXIT = 0


_CHORDS = {
    "STKPWH": ("ʒ", ()),
    "SKWR": ("d͡ʒ", ()),
    "SH": ("ʃ", ()),
    "TH": ("θ", ()),
    "KH": ("t͡ʃ", ()),
    "R": ("ɹ", ()),

    "TWH": ("ð", ()),


    "A": ("æ", ()),
    "AO": ("ʊ", ()),
    "AOE": ("iː", ()),
    "AOEU": ("aɪ", ()),
    "AE": ("ə", ()),
    "AEU": ("eɪ", ()),
    "AER": ("ɚ", ()),
    "AU": ("ɔ", ()),
    "AR": ("ɑɹ", ()),
    "O": ("ɑ", ()),
    "O*": ("ɒ", ()),
    "OE": ("oʊ", ()),
    "OEU": ("ɔɪ", ()),
    "OU": ("aʊ", ()),
    "OR": ("ɔr", ()),
    "E": ("ɛ", ()),
    "EU": ("ɪ", ()),
    "ER": ("ɝ", ()),
    "U": ("ʌ", ()),
    "UR": ("ɚ", ()),
    "EFRPB": ("ɝt͡ʃ", ()),
    "UFRPB": ("ɚt͡ʃ", ()),

    "-FRPBLG": ("nt͡ʃ", ()),
    "-FRPB": ("ɹt͡ʃ", ()),
    "-FP": ("t͡ʃ", ()),
    "-FPB": ("ʃ", ()),
    "-RB": ("ʒ", ()),
    "-R": ("ɹ", ()),
    "-PBLG": ("d͡ʒ", ()),
    "-PBG": ("ŋ", ()),

    "EFRPBLG": ("ɛnt͡ʃ", ()),
    "UFRPBLG": ("ʌnt͡ʃ", ()),

    
    "S": ("s", ()),
    "T": ("t", ()),
    "K": ("k", ()),
    "P": ("p", ()),
    "W": ("w", ()),
    "H": ("h", ()),

    "STKPW": ("z", ()),
    "SKWR": ("j", ()),
    "SR": ("v", ()),
    "TK": ("d", ()),
    "TKPW": ("g", ()),
    "TP": ("f", ()),
    "TPH": ("n", ()),
    "KWR": ("j", ()),
    "PW": ("b", ()),
    "PH": ("m", ()),
    "HR": ("l", ()),

    "-F": ("f", ()),
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
    "-BG": ("k", ()),
}

# Entries which are translated normally
_SPECIAL_ENTRIES = {
    "TPWOPBG": "{plover:end_solo_dict}{^}/",

    "#STRES": "{^}ˈ{^}",
    "#STR*ES": "{^}ˌ{^}",
    "#EPLT": "{^}◌{^}",
    "#HROPBG": "{^}ː{^}",

    "#STOP": "{^}ʔ{^}",
    "SKWR*": "ʤ",
    "TH*": "ð",
    "*T": "ð",
    "KH*": "ʧ",
    "H*": "ʰ",
    "TPH*": "n̩",

    "S-P": "{^ ^}",
}


# Change control chords and special entries depending on whether an extended stenotype system is being used

# # For regular extended stenotype
# if "^-" in KEYS and "_" not in KEYS and "&-" not in KEYS:

# For custom extended stenotype
if "^-" in KEYS and "_" in KEYS and "&-" in KEYS:
    _CHORDS.update({
        "&": ("", (Modifier.EXIT,)),
    })

    _SPECIAL_ENTRIES.update({
        "&": "{#}{plover:end_solo_dict}",
        "_": "{^ ^}",
    })

# # For regular English stenotype and other systems
# else:

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

    if Modifier.EXIT in modifiers:
        translation += "{plover:end_solo_dict}"

    return translation


#endregion
