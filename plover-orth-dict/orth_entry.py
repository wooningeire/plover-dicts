from plover.steno import Stroke

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .orth_fingerspelling import LONGEST_KEY, lookup as _lookup
else:
	# https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
	import importlib.util
	import sys
	import os
	_MODULE_NAME = "orth_fingerspelling"
	_MODULE_PATH = "C:/orth_fingerspelling.py"
	_spec = importlib.util.spec_from_file_location(_MODULE_NAME, _MODULE_PATH)
	_module = importlib.util.module_from_spec(_spec)
	_spec.loader.exec_module(_module)

	_lookup = _module.lookup


LONGEST_KEY = 1

_ENABLED_DICTS = [
	r"~\dev\other\plover_orth_dict\orth_fingerspelling.py",
	r"user-dicts\custom-commands.json",
	# r"~\dev\other\plover_control_seq_dict\fingerspelling_control_seqs.py",
	r"user-dicts\plover_recommended_dictionary_commands.json",
	r"commands.json",
	r"user-dicts\downloads\emily-symbols.py",
]

def lookup(strokes_steno: tuple[str]) -> str:
	stroke = Stroke.from_steno(strokes_steno[0])

	enter = True


	# if (identifier := Stroke.from_steno("#-S")) not in stroke:
	# 	raise KeyError

	if ((identifier := Stroke.from_steno(".")) not in stroke
			and (identifier := Stroke.from_steno("&")) not in stroke):
		raise KeyError


	# if (suffix := Stroke.from_steno("-TSZ")) in stroke:
	# 	if Stroke.from_steno("-D") in stroke:
	# 		raise KeyError

	# 	capitalize = False

	# elif (suffix := Stroke.from_steno("-TDZ")) in stroke:
	# 	if Stroke.from_steno("-S") in stroke:
	# 		raise KeyError

	# 	capitalize = True

	# else:
	# 	raise KeyError

	stroke -= identifier

	# Skip entering the solo dict mode to avoid the brief lag
	if Stroke.from_steno("&") in stroke:
		if Stroke.from_steno("HR") not in stroke: #temp, hopefully, for until a better layout is implemented
			enter = False

		stroke -= Stroke.from_steno("&")

	out = _lookup((stroke.rtfcre,))
	
	# if capitalize:
		# return "{-|}" + out


	if enter:
		out = (f"{{plover:solo_dict:{','.join(f'+{dict_url}' for dict_url in _ENABLED_DICTS)}}}"
				+ out)
	
	return out