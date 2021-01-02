"""Usage:
backup.py <folder-file-path> [--setDirectory=<path>]
					(-h | --help)
							

Options:
	-h          Show this help
	-i          Convert image to vertical scroll box
	-t          Convert text to vertical scroll box
	-c          Convert command list to html
"""
# import reset

from colorama import Fore, Style, init
init()

import sys
import argparse
import json
from pathlib import Path
from helpers import *

parser = argparse.ArgumentParser()
parser.add_argument('target', nargs=1, type=Path)
parser.add_argument('interval', nargs=1, type=Minute)
parser.add_argument('--setDirectory', type=str2bool, help='set directory to add backups')

args = parser.parse_args()

directory_set = False # So we don't repeat directory checking

# Creates a new dir.txt if this is the first time they are using it
# And calls set_directory
if not Path('dir.txt').exists():
	Path('dir.txt').touch()
	set_directory(r'./dir.txt')
	directory_set = True

# If they want to set directory
if args.setDirectory:
	if not directory_set:
		set_directory(r'./dir.txt')

if not Path(args.target[0]).exists(): # Checks if target exists
	print(f'{Fore.RED}File/directory not found{Style.RESET_ALL}')
	sys.exit(1)

# If the target does exist

print(args.interval[0].val)