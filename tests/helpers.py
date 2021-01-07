"""Helpers for my tests"""

from subprocess import Popen, PIPE
from collections import namedtuple

# Runargs function
Output = namedtuple('Output', 'out, err')

def runargs(cmd: list):
  if not isinstance(cmd, list):
    raise TypeError("cmd arg is not a list")
  p = Popen("python ./backup/parser.py " + " ".join(cmd), shell=True, stdout=PIPE, stderr=PIPE)
  finished_running_output = [byte_str.decode("utf-8") for byte_str in p.communicate()]
  return Output(*finished_running_output)

# Reset Functions
from pathlib import Path

def del_dir():
  try:
      Path(r"./data/dir.txt").unlink()
  except:
      pass

def reset_db():
  Path(r"./data/db.json").write_text("[]")

if __name__ == '__main__':
  del_dir()
  reset_db()