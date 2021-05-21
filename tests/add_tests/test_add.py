import pytest, sys
sys.path.append("..")
from helpers_for_tests import runargs

def add_add_to_args(args):
  return [["add"] + arg for arg in args]

not_enough_args = [[], ["target"]]
not_enough_args = add_add_to_args(not_enough_args)

@pytest.mark.parametrize('args', not_enough_args)
def test_not_enough_args(args):
  test = runargs(args)

  assert "the following arguments are required" in test.err

# Bad fname and bad dir are checked during backup/backup.py, so we don't test it here (actually, not implemented yet)
wrong_type = [ 
  ["fname", "bad min type", "./dir"],

]
wrong_type = add_add_to_args(wrong_type)

@pytest.mark.parametrize('args', wrong_type)
def test_wrong_type(args):
  test = runargs(args)
  print(test.err)
  print(str(args) + "\n")