from plover.steno import Stroke

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .orth_chording import LONGEST_KEY, lookup as _lookup
else:
	# https://stackoverflow.com/questions/67631/how-can-i-import-a-module-dynamically-given-the-full-path
	import importlib.util
	import sys
	import os
	_MODULE_NAME = "orth_chording"
	_MODULE_PATH = "C:/orth_chording.py"
	_spec = importlib.util.spec_from_file_location(_MODULE_NAME, _MODULE_PATH)
	_module = importlib.util.module_from_spec(_spec)
	_spec.loader.exec_module(_module)

	_lookup = _module.lookup


LONGEST_KEY = 1

_ENABLED_DICTS = [
	r"orth_chording.py",
	r"commands.json",
]

_solo_dict_command = f"{{plover:solo_dict:{','.join(f'+{dict_url}' for dict_url in _ENABLED_DICTS)}}}"

_IDENTIFIER_SUBSTROKE = Stroke.from_steno("&")

def lookup(strokes_steno: tuple[str]) -> str:
	stroke = Stroke.from_steno(strokes_steno[0])

	enter = True

	if _IDENTIFIER_SUBSTROKE not in stroke:
		raise KeyError
	

	stroke -= _IDENTIFIER_SUBSTROKE

	# # If both entry keys are present, skip entering the solo dict mode to avoid the brief lag
	# if Stroke.from_steno("&") in stroke:
	# 	enter = False

	# 	stroke -= Stroke.from_steno("&")

	out = _lookup((stroke.rtfcre,))


	if enter:
		out = _solo_dict_command + out
	
	return out