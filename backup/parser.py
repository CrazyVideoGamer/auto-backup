'''Contains parser function and argc check function.'''

from pathlib import Path
import sys
from backup.helpers import error_message, str2bool
import argparse

def argc_allowed() -> None:
  if len(sys.argv) <= 1:
    error_message('No arguments were provided. Use -h or --help for information', 3)
    sys.exit(1)

def create_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(help='sub-command -h', dest='command') # TODO: Try to add --help as well

  add_parser = subparsers.add_parser("add", help="add -h")
  add_parser.add_argument('target', nargs=1, type=Path)
  add_parser.add_argument('interval', nargs=1, type=int)

  add_parser.add_argument('directory', nargs='?', type=Path, const=None)
  add_parser.add_argument('--setDefaultDir', action='store_true',help='if want to set a default directory')


  return parser

if __name__ == "__main__":
  args = create_parser().parse_args()
  print(args)