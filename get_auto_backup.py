# linux: curl https://raw.githubusercontent.com/CrazyVideoGamer/auto-backup/main/get_auto_backup.py | python3      <-- not yet tested
# windows cmd: curl https://raw.githubusercontent.com/CrazyVideoGamer/auto-backup/main/get_auto_backup.py | python <-- not yet tested 
from pathlib import Path
import argparse

import sys, platform, subprocess

def does_git_exist():
  system = platform.system()
  if system == "Linux":
    log = subprocess.run("command -v git >/dev/null 2>&1 || { echo 'error: git not found' >&2;}", shell=True)
    if log.stdout == b'error: git not found':
      return False
    return True
  elif system == "Windows":
    log = subprocess.run("where git >nul 2>&1 || ( echo error: git not found )", shell=True)
    if log.stdout == b'error: git not found':
      return False
    return True


def error_message(message: str) -> None:
  # \u001b[31m makes it red, \u001b[0m makes the color reset
  system = platform.system()

  if system == "Linux":
    print("\u001b[31m" + message + "\u001b[0m", file=sys.stderr)
  elif system == "Windows":
    # Taken from https://www.burgaud.com/bring-colors-to-the-windows-console-with-python
    # Also looked at colorama code (take a look at https://github.com/tartley/colorama/blob/7a85efbc6d5b59665badb50b953d12390047b5f8/colorama/winterm.py and https://github.com/tartley/colorama/blob/7a85efbc6d5b59665badb50b953d12390047b5f8/colorama/win32.py)

    from ctypes import windll, Structure, c_short, c_ushort, byref
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    FOREGROUND_RED = 0x0004
    stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
    GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo

    SHORT = c_short
    WORD = c_ushort

    class COORD(Structure):
      """struct in wincon.h."""
      _fields_ = [
        ("X", SHORT),
        ("Y", SHORT)]

    class SMALL_RECT(Structure):
      """struct in wincon.h."""
      _fields_ = [
        ("Left", SHORT),
        ("Top", SHORT),
        ("Right", SHORT),
        ("Bottom", SHORT)]
    class CONSOLE_SCREEN_BUFFER_INFO(Structure):
      """struct in wincon.h."""
      _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD)]

    def get_text_attr(stream_id=stdout_handle):
      """Returns the character attributes (colors of the console screen
      buffer.)"""
      csbi = CONSOLE_SCREEN_BUFFER_INFO()
      GetConsoleScreenBufferInfo(stream_id, byref(csbi))
      return csbi.wAttributes

    def set_text_attr(color, stream_id=stdout_handle):
      """Sets the character attributes (colors) of the console screen
      buffer. Color is a combination of foreground and background color,
      foreground and background intensity."""
      SetConsoleTextAttribute(stream_id, color)

    attrs = get_text_attr()
    fore = attrs & 7
    back = (attrs >> 4) & 7

    FOREGROUND_INTENSITY = 0x08
    BACKGROUND_INTENSITY = 0x80

    style = attrs & (FOREGROUND_INTENSITY | BACKGROUND_INTENSITY)

    set_text_attr(FOREGROUND_RED | back | style)

    print(message, file=sys.stderr)

    set_text_attr(fore | back | style)

  sys.exit(0)

def create_parser() -> argparse.ArgumentParser:
  parser = argparse.ArgumentParser(description="Install or uninstall auto-backup")
  parser.add_argument("--uninstall", action='store_true')

  return parser

args = create_parser().parse_args()

system = platform.system()

if system == "Linux":
  install_path = Path.home() / ".auto-backup"
  
  if not args.uninstall:
    if (install_path.exists() and (install_path / '.is-auto-backup').exists()):
      error_message("Already installed auto-backup")
    elif (install_path.exists() and not (install_path / '.is-auto-backup').exists()):
      error_message("Could not create the ~/.auto-backup directory: directory already exists")
    else: # this else statement only runs if ~/.auto-backup doesn't exist
      install_path.mkdir(exist_ok=True)
      (install_path / ".is-auto-backup").touch()

      # add this git repository (and also leave out the .git directory and name it `backup`)
      if does_git_exist():
        if not (install_path / "backup").exists():
          print("Installing auto-backup...")

          subprocess.run("git clone --quiet --depth=1 --branch=main https://github.com/CrazyVideoGamer/auto-backup.git backup", cwd=install_path, shell=True)
          subprocess.run("rm -rf ./backup/.git", cwd=install_path, shell=True)
          subprocess.run("pip install -r requirements.txt -t lib2 > /dev/null 2>&1", cwd=(install_path / "backup"), shell=True)

          print("Done!\n")
      else:
        error_message("Please install git using `sudo apt install git`")

      print(f"add `export PATH={str(install_path / 'auto-backup' / 'backup' / 'bin')}:$PATH` to ~/.bashrc to complete the installation")
  else:
    if (not install_path.exists() or (install_path.exists() and not (install_path / '.is-auto-backup').exists())):
      error_message("auto-backup is not installed")
    print("Uninstalling auto-backup...")
    subprocess.run(f"rm -r {str(install_path)}", shell=True)
    print("Done!")
elif system == "Windows":
  install_path = Path.home() / "auto-backup"

  if not args.uninstall:

    if (install_path.exists() and (install_path / 'is-auto-backup').exists()):
      error_message("Already installed auto-backup")
    elif (install_path.exists() and not (install_path / 'is-auto-backup').exists()):
      error_message(f"Could not create the {str(install_path)} directory: directory already exists")
    else:
      install_path.mkdir(exist_ok=True)
      (install_path / "is-auto-backup").touch() # note that it is "is-auto-backup", not ".is-auto-backup"

      # add this git repository (and also leave out the .git directory and name it `backup`)
      if does_git_exist():
        if not (install_path / "backup").exists():
          print("Installing auto-backup...")

          subprocess.run("git clone --quiet --depth=1 --branch=main https://github.com/CrazyVideoGamer/auto-backup.git backup", cwd=install_path, shell=True)
          subprocess.run("rd /s /q \"backup/.git\"", cwd=install_path, shell=True)
          subprocess.run("pip install -r requirements.txt -t lib > nul 2>&1", cwd=(install_path / "backup"), shell=True)
        
          print("Done!\n")
      else:
        error_message("Please install git first (go to https://git-scm.com/) ")

      print(f"add {str(install_path / 'auto-backup' / 'backup' / 'bin')} to PATH to complete the installation")
  else:
    if (not install_path.exists() or (install_path.exists() and not (install_path / 'is-auto-backup').exists())):
      error_message("auto-backup is not installed")
    print("Uninstalling auto-backup...")
    subprocess.run(f"rd /s /q {str(install_path)}", shell=True)
    print("Done!")
else:
  error_message("System {system} is not supported")
