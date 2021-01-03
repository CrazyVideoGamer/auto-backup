from pathlib import Path
import sys
from helpers import Minute, str2bool, error_message
import argparse

if len(sys.argv) <= 1:
  error_message('No arguments were provided. Use -h or --help for information', 3)
  sys.exit(1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command -h', dest='command') # TODO: Try to add --help as well

add_parser = subparsers.add_parser("add", help="add -h")
add_parser.add_argument('target', nargs=1, type=Path)
add_parser.add_argument('interval', nargs=1, type=Minute)

add_parser.add_argument('directory', nargs='?', type=Path, const=None)
add_parser.add_argument('--setDefaultDir', nargs=0, help='if want to set a default directory')

# add_subparsers = add_parser.add_subparsers(help='sub-command -h', dest='command')
# directory_parser = add_subparsers.add_parser("directory", help="directory -h")
# directory_parser.add_argument('--setDefaultDir', nargs="?", type=str2bool, help='if want to set a default directory', const=False)