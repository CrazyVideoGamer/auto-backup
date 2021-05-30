import sys
sys.path.append("./tests")
from helpers_for_tests import run_args_on_parser as runargs
print(runargs(["add", "targets/x", "3", "."]))