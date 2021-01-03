"""
Just for quickly reseting data
"""

from pathlib import Path
try:
    Path(r"./data/dir.txt").unlink()
except:
    pass
Path(r"./data/db.json").write_text("[]")