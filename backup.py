"""Usage:
backup.py run [--targets] <- TODO
backup.py add <folder-file-path> <interval> [--setDirectory=<path>]
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

import parser

args = parser.parser.parse_args()

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

interval = args.interval[0]
print(interval == 5)