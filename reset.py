"""
Just for quickly reseting dir.txt
"""

from pathlib import Path
try:
    Path(r"dir.txt").unlink()
except:
    pass