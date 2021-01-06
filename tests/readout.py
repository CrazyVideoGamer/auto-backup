from subprocess import Popen, PIPE
from collections import namedtuple

Output = namedtuple('Output', 'out, err')

def runargs(cmd):
  p = Popen("python ./backup/parser.py " + " ".join(cmd), shell=True, stdout=PIPE, stderr=PIPE)
  finished_running_output = [byte_str.decode("utf-8") for byte_str in p.communicate()]
  return Output(*finished_running_output)

if __name__ == "__main__":
  print(runargs(["foo", "hoho"]))