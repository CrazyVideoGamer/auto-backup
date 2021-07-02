from pathlib import Path
import shutil

import platform, subprocess

def doesGitExist():
  import sys
  out = subprocess.run("git", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

system = platform.system()

if system == "Linux":
  install_path = Path.home() / ".auto-backup";
  if (install_path.exists() and not (install_path / '.is-auto-backup').exists() ):
    # \u001b[31m makes it red, \u001b[0m makes the color reset
    print("\u001b[31m" + "Could not create the ~/.auto-backup directory: directory already exists" + "\u001b[0m")	
  else: # this else statement only runs if auto-backup installer was already used (~/.auto-backup exists and .is-auto-backup exists, ), or ~/.auto-backup doesn't exist
    install_path.mkdir(exist_ok=True)
    (install_path / ".is-auto-backup").touch()
    shutil.copy("./bin/auto-backup", "/usr/local/bin/auto-backup")
elif system == "Windows":
  install_path = Path.home() / "auto-backup"
  if (install_path.exists() and not (install_path / 'is-auto-backup').exists() ):
    # \u001b[31m makes it red, \u001b[0m makes the color reset
    print("\u001b[31m" + "Could not create the ~/.auto-backup directory: directory already exists" + "\u001b[0m")	
  else:
    install_path.mkdir(exist_ok=True)
    (install_path / "is-auto-backup").touch() # note that it is "is-auto-backup", not ".is-auto-backup"
    subprocess.run
    print(f"add {install_path / 'auto-backup' / 'backup' / ''}")


