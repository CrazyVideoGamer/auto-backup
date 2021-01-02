import os, tempfile
from pathlib import Path

def is_path_sibling_creatable(pathname: str) -> bool:
	'''
	`True` if the current user has sufficient permissions to create **siblings**
	(i.e., arbitrary files in the parent directory) of the passed pathname;
	`False` otherwise.
	'''
	# Parent directory of the passed path. If empty, we substitute the current
	# working directory (CWD) instead.
	dirname = os.path.dirname(pathname) or os.getcwd()

	try:
		# For safety, explicitly close and hence delete this temporary file
		# immediately after creating it in the passed path's parent directory.
		with tempfile.TemporaryFile(dir=dirname): pass
		return True
	# While the exact type of exception raised by the above function depends on
	# the current version of the Python interpreter, all such types subclass the
	# following exception superclass.
	except EnvironmentError:
		return False

def str2bool(v):
	import argparse
	if isinstance(v, bool):
	   return v
	if v.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif v.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')

def set_directory(path):
	file = Path(path)
	backup_path = ""
	print(is_path_sibling_creatable(backup_path))
	while is_path_sibling_creatable(backup_path) == False or backup_path == "":
		backup_path = input("Backup directory path: ")
	file.write_text(backup_path)

class Minute:
  def __init__(self, mins: int):
    self.val = int(mins)
  def __repr__(self):
    return f'Minutes({self.val})'
  def __str__(self):
    return f'Minutes: {self.val}'
  def __eq__(self, other):
    if isinstance(other, int):
      if self.val == other:
        return True
    if isinstance(other, Minute):
      if self.val == other.val:
        return True
    return False