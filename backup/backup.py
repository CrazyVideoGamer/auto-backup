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
directory = args.directory[0]

check_for_duplicates(target)

if args.setDefaultDir:
  set_default_directory(directory)

if not Path(directory).is_dir(): # Checks if target exists
  error_message("Directory not found (may be a file)", 1)
  if Path(target).exists():
    Path(target).unlink()
  create_new = "not bool"
  while create_new == "not bool":
    create_new = str2bool(input("Create new directory: "), isargparse=False)

  if create_new:
    directory.mkdir(parents=True)

# If the target does exist
if args.command == 'add':
  path = Path('./data/db.json')
  if not path.exists():
    path.touch()
    path.write_text("[]")
  new_entry = {
    'target': str(target),
    'interval': args.interval[0].val
  }
  if args.setDefaultDir:
    set_default_directory(directory)
  else:
    new_entry['directory'] = directory

  old = json.loads(path.read_text())
  old.append(new_entry)
  path.write_text(json.dumps(old))