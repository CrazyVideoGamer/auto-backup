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

from parser import parser

args = parser.parse_args()
target = args.target[0]

check_for_duplicates(target)

setup(args) # Sets up all the setDirectory things

# directory_set = False # So we don't repeat directory checking

# # Creates a new dir.txt if this is the first time they are using it
# # And calls set_directory
# if not Path('dir.txt').exists():
# 	Path('dir.txt').touch()
# 	set_directory(r'./dir.txt')
# 	directory_set = True

# # If they want to set directory
# if args.setDirectory:
# 	if not directory_set:
# 		set_directory(r'./dir.txt')

# if not Path(args.target[0]).exists(): # Checks if target exists
# 	print(f'{Fore.RED}File/directory not found{Style.RESET_ALL}')
# 	sys.exit(1)

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