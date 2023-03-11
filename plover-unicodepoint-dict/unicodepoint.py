from plover.steno import Stroke

LONGEST_KEY = 2

_ENTRY_STENO = "TKWHR"

_key_values = {
    key: 1 << i
    for i, key in enumerate(reversed((
        "-E", "-U",
        "#", "S-", "T-", "K-",
        "P-", "W-", "H-", "R-",
        "-F", "-R", "-P", "-B",
        "-L", "-G", "-T", "-S",
    )))
}

def lookup(key):
    # assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    if _ENTRY_STENO != key[0]:
        raise KeyError
    if len(key) == 1:
        return "u+"
    
    left_space = False
    right_space = False

    codepoint = 0
    for key in Stroke.from_steno(key[1]).keys():
        if key not in _key_values: 
            if key == "A-":
                left_space = True
            if key == "O-":
                right_space = True

            continue
        
        codepoint += _key_values[key]

    
    left_control = "{}" if left_space else "{^}"
    right_control = "{}" if right_space else "{^}"

    return f"{left_control}{chr(codepoint)}{right_control}"
