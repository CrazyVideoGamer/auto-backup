from pathlib import Path
import sys
from helpers import Minute, str2bool, error_message
import argparse

if not len(sys.argv) > 1:
  error_message('No arguments were provided. Use -h or --help for information')
  sys.exit(1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command -h', dest='command') # TODO: Try to add --help as well

add_parser = subparsers.add_parser("add", help="add -h")
add_parser.add_argument('target', nargs=1, type=Path)
add_parser.add_argument('interval', nargs=1, type=Minute)
add_parser.add_argument('--setDirectory', type=str2bool, help='set directory to add backups')