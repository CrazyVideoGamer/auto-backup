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

import json, sys
from pathlib import Path
from helpers import error_message, check_if_use_saved_directory, check_for_duplicates, set_default_directory, str2bool

from parser import argc_allowed, create_parser

argc_allowed()

args = create_parser().parse_args()

if args.directory == None and args.setDefaultDir:
  error_message('Cannot set default directory when directory not given', 3)

target = args.target[0]
directory = check_if_use_saved_directory(args.directory)

check_for_duplicates(target)

if args.setDefaultDir:
  set_default_directory(directory)

if not Path(directory).is_dir(): # Checks if directory not found
  error_message("Directory not found (may be a file)", 1)

  create_new = None
  while create_new == "not bool":
    create_new = str2bool(input(f"Create new directory {directory}: "))

  if create_new:
    Path(directory).mkdir(parents=True)
  else:
    sys.exit()

# If the target does exist
if args.command == 'add':
  path = Path('./data/db.json')
  if not path.exists():
    path.touch()
    path.write_text("[]")
  new_entry = {
    'target': str(target),
    'interval': args.interval[0]
  }
  if args.setDefaultDir:
    set_default_directory(directory)
  else:
    new_entry['directory'] = str(directory)

  old = json.loads(path.read_text())
  old.append(new_entry)
  path.write_text(json.dumps(old))