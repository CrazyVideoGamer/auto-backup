import pytest, sys
sys.path.append("..")
from helpers_for_tests import run_args_on_parser as runargs

def add_add_to_args(args):
  """Helper function that puts the add subcommand add in front for dev convience"""

  return [["add"] + arg for arg in args]

not_enough_args = [[], ["target"]]
not_enough_args = add_add_to_args(not_enough_args)

@pytest.mark.parametrize('args', not_enough_args)
def test_not_enough_args(args):
  result = runargs(args)

  assert "the following arguments are required" in result.err

# Bad fname and bad dir are checked during backup/backup.py, so we don't test it here (actually, checks may not be implemented yet)
wrong_type = [ 
  ["fname", "bad min type", "./dir"],
]
wrong_type = add_add_to_args(wrong_type)

@pytest.mark.parametrize('args', wrong_type)
def test_wrong_type(args):
  error = runargs(args).err

  worked = ("parser.py add: error: argument" in error) and ("invalid" in error) and ("value" in error) # check invalid type in error message. btw in the error message, it is invalid <type> value, so it is spit up.

  assert worked