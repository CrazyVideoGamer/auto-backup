'''Contains parser function and argc check function.'''

from pathlib import Path
# from colorama import Fore, Style
import sys
# import os
# sys.path.insert(1, os.getcwd())
# print(f'{Fore.RED}{sys.path}{Style.RESET_ALL}')
from helpers import error_message, str2bool
import argparse

def argc_allowed() -> None:
  if len(sys.argv) <= 1:
    error_message('No arguments were provided. Use -h or --help for information\n', 3)
    sys.exit(1)

def create_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(help='sub-command -h', dest='command') # TODO: Try to add --help as well

  add_parser = subparsers.add_parser("add", help="add -h")
  add_parser.add_argument('target', nargs=1, type=Path)
  add_parser.add_argument('interval', nargs=1, type=float)
  add_parser.add_argument('directory', nargs='?', type=Path, const=None)

  remove_parser = subparsers.add_parser("remove", help="remove -h")
  remove_parser.add_argument('target', nargs=1, type=Path)

  config_parser = subparsers.add_parser("config", help="config -h")
  config_parser.add_argument('option', nargs=1, type=str)
  config_parser.add_argument('value', nargs=1, type=str);

  return parser

if __name__ == "__main__":
  args = create_parser().parse_args()
  print(args)