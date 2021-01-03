from colorama import Fore, Style, init
init()

import os, tempfile, sys, argparse
from typing import Literal
from pathlib import Path

def error_message(text, level: Literal[1,2,3]):
  if level == 3:
    print(f'{Fore.RED}{text}{Style.RESET_ALL}')
    sys.exit(1)
  elif level == 2:
    # orange
    pass
  elif level == 1:
    print(f'{Fore.YELLOW}{text}{Style.RESET_ALL}')

def is_path_sibling_creatable(pathname):
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

def str2bool(v, isargparse=True):
  if isinstance(v, bool):
    return v
  if v.lower() in ('yes', 'true', 't', 'y', '1'):
    return True
  elif v.lower() in ('no', 'false', 'f', 'n', '0'):
    return False
  else:
    if isargparse:
      raise argparse.ArgumentTypeError('Boolean value expected.')
    else:
      return "not bool"

def set_default_directory(directory):
  file = Path("./data/dir.txt")
  file.write_text(str(directory))

class Minute:
  def __init__(self, mins: int):
    self.val = int(mins)
  def __eq__(self, other):
    if isinstance(other, int):
      if self.val == other:
        return True
    if isinstance(other, Minute):
      if self.val == other.val:
        return True
    return False

def check_for_duplicates(target):
  path = Path('./data/db.json')
  contents = path.read_text()
  if contents.find(f'"target": "{str(target)}"') != -1:
    error_message(f"Target {target} already exists. Use update to update a queriy, or use remove to remove it.", 3)