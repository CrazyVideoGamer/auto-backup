'''Contains parser function and argc check function.'''

from pathlib import Path
# from colorama import Fore, Style
import sys
# import os
# sys.path.insert(1, os.getcwd())
# print(f'{Fore.RED}{sys.path}{Style.RESET_ALL}')
from helpers import error_message, str2bool
import argparse

usage = """
backup.py run [--targets] <- TODO
backup.py add <folder-file-path> <interval>
					(-h | --help)
backup.py config <option> <value>

Explanation:
  run:
    --targets - the targets to backup
  add:
    folder-file-path - The folder or file to backup
    interval - time until new backup <- TODO: allow for only user prompted backups
  config:
    option - Allowed values: defaultDir\n
"""

def argc_allowed() -> None:
  if len(sys.argv) <= 1:
    error_message('No arguments were provided. Use -h or --help for information\n', 3)
    sys.exit(1)

def create_parser() -> argparse.ArgumentParser:
  # parser = argparse.ArgumentParser(description="Automatically back up your files/directories", usage=usage)
  parser = argparse.ArgumentParser(description="Automatically back up your files/directories")
  subparsers = parser.add_subparsers(help='sub-command -h', dest='command') # TODO: Try to add --help as well

  add_parser = subparsers.add_parser("add", help="add -h")
  add_parser.add_argument('target', type=Path)
  add_parser.add_argument('interval', type=float)
  add_parser.add_argument('directory', nargs='?', type=Path, const=None)

  remove_parser = subparsers.add_parser("remove", help="remove -h")
  remove_parser.add_argument('target', type=Path)

  config_parser = subparsers.add_parser("config", help="config -h")
  config_parser.add_argument('option', type=str)
  config_parser.add_argument('value', type=str);

  return parser

if __name__ == "__main__": # Used for testing parser
  argc_allowed()
  args = create_parser().parse_args()
  
  dictionary = vars(args) # use vars to get the underlying dictionary from Namespace object
  no_paths_dictionary = {} # extra dict to get rid of all the pathlib paths so json.dumps is happy

  import pathlib

  for key, value in dictionary.items():
    if isinstance(value, pathlib.PurePath):
      no_paths_dictionary[key] = str(value)

  import json

  print(json.dumps(no_paths_dictionary), end="") # dumps it so i can use it in testing by using json.loads