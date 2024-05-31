from plover.steno import Stroke

LONGEST_KEY = 8

_ENTRY_STROKE = Stroke.from_steno("TKWHR")
_EXIT_CHORD = Stroke.from_steno("R")
_LEFT_SPACE_CHORD = Stroke.from_steno("A")
_RIGHT_SPACE_CHORD = Stroke.from_steno("O")

_key_values = {
    "-R": 1 << 3,
    "-B": 1 << 2,
    "-G": 1 << 1,
    "-S": 1 << 0,
    "-U": 0,
}

def lookup(strokes_steno: tuple[str]):
    entry_stroke = Stroke.from_steno(strokes_steno[0])
    if entry_stroke != _ENTRY_STROKE:
        raise KeyError
    

    last_stroke = Stroke.from_steno(strokes_steno[-1])
    
    left_space = False
    right_space = False
    has_exit_stroke = False
    has_exit_chord_separated = False

    if len(strokes_steno) >= 2:
        if _LEFT_SPACE_CHORD in last_stroke:
            last_stroke -= _LEFT_SPACE_CHORD
            left_space = True
        
        if _RIGHT_SPACE_CHORD in last_stroke:
            last_stroke -= _RIGHT_SPACE_CHORD
            right_space = True

        if _EXIT_CHORD in last_stroke:
            if last_stroke == _EXIT_CHORD:
                has_exit_chord_separated = True

            last_stroke -= _EXIT_CHORD
            has_exit_stroke = True
    else:
        return "u+"


    codepoint = 0
    for steno in strokes_steno[1:-1] if has_exit_chord_separated else strokes_steno[1:]:
        codepoint <<= 4

        stroke = Stroke.from_steno(steno)
        for key in stroke.keys():
            if key not in _key_values:
                raise KeyError
            
            codepoint += _key_values[key]    
    valid_codepoint = codepoint < 0x110000


    if not has_exit_stroke:
        return f"u+{codepoint:x}{'' if valid_codepoint else ' [invalid]'}"
    
    if not valid_codepoint:
        return f"[u+{codepoint:x}]"

    
    left_control = "{}" if left_space else "{^}"
    right_control = "{}" if right_space else "{^}"

    return f"{left_control}{chr(codepoint)}{right_control}"
