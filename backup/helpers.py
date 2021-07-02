"""Helpers used for backup package"""


from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "lib")) # add libraries to path

from colorama import Fore, Style, init # type: ignore
init()

from typing import Union

def error_message(text: str, level: int) -> None:
  """Gives a colored error message to user. When level is 3, the program exits"""

  if level == 3:
    print(f'{Fore.RED}{text}{Style.RESET_ALL}', file=sys.stderr)
    sys.exit(1)
  elif level == 2:
    # orange
    pass
  elif level == 1:
    print(f'{Fore.YELLOW}{text}{Style.RESET_ALL}')


def getDataFolder() -> Path:
  return Path(__file__).parents[2] / "data" 

def file_exists(filename: str) -> bool:
  """Check if file exists"""
  file = Path(filename)
  if file.is_file():
    return True
  else:
    return False

def dir_exists(directory: str) -> bool:
  dir = Path(directory)
  if dir.is_dir():
    return True
  else:
    return False

def str2bool(v: str) -> Union[str, bool]:
  """Convert string to bool"""
  if isinstance(v, bool):
    return v
  if v.lower() in ('yes', 'true', 't', 'y', '1'):
    return True
  elif v.lower() in ('no', 'false', 'f', 'n', '0'):
    return False
  else:
      return "not bool"

def set_default_directory(directory: str) -> None:
  """Set the default directory"""
  (getDataFolder() / 'dir.txt').write_text(str(directory));

def default_directory_exists():
  return (getDataFolder() / 'dir.txt').exists()

def check_for_duplicates(target):
  """Check for target duplicates in database"""
  contents = (getDataFolder() / 'db.json').read_text()
  if contents.find(f'"target": "{str(target)}"') != -1:
    error_message(f"Target {target} already exists. Use update to update a queriy, or use remove to remove it.", 3)

def check_if_use_saved_directory(directory: str)-> str:
  """Returns args.directory if not None, otherwise return saved directory at ./data/dir.txt"""
  if directory == None:
    return (getDataFolder() / 'dir.txt').read_text()
  else:
    return directory
