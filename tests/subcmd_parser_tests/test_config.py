import pytest, sys
sys.path.append("..")
from helpers_for_tests import run_args_on_parser as runargs

def add_config_to_args(args):
	"""Helper function that puts the config subcommand add in front for dev convience"""

	return [["config"] + arg for arg in args]

not_enough_args = [[], ["config_value"]]
not_enough_args = add_config_to_args(not_enough_args)

@pytest.mark.parametrize("args", not_enough_args)
def test_not_enough_args(args):
  result = runargs(args)
  assert "the following arguments are required" in result.err
