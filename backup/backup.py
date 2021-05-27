"""Usage:
backup.py run [--targets] <- TODO
backup.py add <folder-file-path> <interval>
					(-h | --help)
backup.py config <option> <value>

Explanation:
  run:
    --targets - the targets to backup
  add:
    folder-file-path - The folder or file to backup
    interval - time until new backup <- TODO: allow for only user prompted backups
  config:
    option - Allowed values: defaultDir
"""
# import reset

import json, sys
from pathlib import Path
from helpers import error_message, check_if_use_saved_directory, check_for_duplicates, set_default_directory, default_directory_exists, str2bool, dir_exists

from parser import argc_allowed, create_parser

argc_allowed()

args = create_parser().parse_args()

if args.command == 'add':
  if args.directory == None and not default_directory_exists():
    error_message('Cannot use default directory if default directory not set', 3)

  target = args.target[0]
  directory = check_if_use_saved_directory(args.directory)

  check_for_duplicates(target)

  if not Path(directory).is_dir(): # Checks if directory not found
    error_message("Directory not found (may be a file)", 1)

    create_new = "not bool"
    while create_new == "not bool":
      create_new = str2bool(input(f"Create new directory {directory}: "))

    if create_new:
      Path(directory).mkdir(parents=True)
    else:
      sys.exit()

  # If the target does exist
  if target.exists():
    path = Path('./data/db.json')
    if not path.exists():
      path.touch()
      path.write_text("[]")
    new_entry = {
      'target': str(target),
      'interval': args.interval[0]
    }
    new_entry['directory'] = str(directory)

    queries = json.loads(path.read_text())
    queries.append(new_entry)
    path.write_text(json.dumps(queries))
    print(f"Successfully added {target}")

elif args.command == 'remove':
  target = args.target[0]
  path = Path('./data/db.json')

  if not path.exists():
    error_message(f'Target "{target}" not found. Use `backup.py add <target> <time> <backup_directory>` to add "{target}"', 3)

  queries = json.loads(path.read_text())

  new_queries = filter(lambda query: query['target'] != target, queries)
  # print(f"new_queries {list(new_queries)}")

  str_new_queries = json.dumps(list(new_queries))
  # print(str_new_queries)

  path.write_text(str_new_queries)
  print(f"Successfully removed {target}")

elif args.command == 'config':
	#extract option & value
  option = args.option[0]
  value = args.value[0]

  if option == 'defaultDir':
    if dir_exists(value):
      set_default_directory(value);
    else:
      error_message("Directory doesn't exist.", 3);
  else:
    error_message(f'Option "{option}" is not valid.', 3)