import os


def runargs(cmd):
  newcmd = ["python", "backup/parser.py"] + cmd
  return os.popen(" ".join(newcmd)).read()

if __name__ == "__main__":
  x = runargs(["foo"])
  print(x)
  print(x, "foo" in x)