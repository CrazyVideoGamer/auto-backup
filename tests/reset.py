"""
Just for quickly reseting data
"""
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