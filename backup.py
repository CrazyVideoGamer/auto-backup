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

import json
from pathlib import Path
from helpers import *

import parser

args = parser.parser.parse_args()
target = args.target[0]

check_for_duplicates(target)

setup(args) # Sets up all the setDirectory things

# If the target does exist
if args.command == 'add':
  path = Path('db.json')
  if not path.exists():
    path.touch()
    path.write_text(json.dumps([]))
  new_entry = {
    'target': str(args.target[0]),
    'interval': str(args.interval)
  }
  old = json.loads(path.read_text())
  old.append(new_entry)
  path.write_text(json.dumps(old))