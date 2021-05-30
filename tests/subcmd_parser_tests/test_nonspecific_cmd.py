# import pytest, sys
from helpers_for_tests import reset_db, runargs as runargs

# sys.path.insert(1, './backup')
# from parser import create_parser

def test_no_args():
  result = runargs([])
  assert "No arguments were provided." in result.err

def test_check_if_enter_something_other_than_config_add_update_remove_run():
  # with pytest.raises(SystemExit):
  #   parser.parse_args(['foo'])
  #   out, err = capfd.readouterr()
  result = runargs(["foo"])
  assert "invalid choice: 'foo'" in result.err
  # assert "error: argument command: invalid choice: 'foo'" in out