"""Helpers for my tests"""

from subprocess import Popen, PIPE
from collections import namedtuple

# Runargs function
Output = namedtuple('Output', 'out, err')

def run_args_on_parser(cmd: list):
  """Run arguments to parser (doesn't create side effects).
Note: the output.out will return with no pathlib objects, so make sure to convert to a pathlib object if wanting to do something with the path file / dir."""
  if not isinstance(cmd, list):
    raise TypeError("cmd arg is not a list")
  p = Popen("python ./backup/parser.py " + " ".join(cmd), shell=True, stdout=PIPE, stderr=PIPE)

  out, err = [byte_str.decode("utf-8") for byte_str in p.communicate()]
  
  if not out == "":
    json_loaded_out = json.loads(out)
  else:
    json_loaded_out = ""

  output = Output(json_loaded_out, err)
  return output

import json

def get_queries() -> list:
  try:
    return json.loads(Path("./data/db.json").read_text())
  except:
    return []

# Reset Functions
from pathlib import Path

def rm_default_dir():
  try:
    Path("./data/dir.txt").unlink()
  except:
    #file not found error
    pass

def reset_queries():
  Path("./data/db.json").write_text("[]")

if __name__ == '__main__':
  rm_default_dir()
  reset_queries()