import pytest, sys
# from pytest import capfd
print(sys.path)
from test_helpers import reset_db, runargs

# sys.path.insert(1, './backup')
# from parser import create_parser

# Extremely pog: https://github.com/pytest-dev/pytest/issues/2424

# @pytest.fixture
# def parser():
#   '''Creates the parser and returns it'''
#   return create_parser()


def test_check_if_enter_something_other_than_add_update_remove_run():
  # with pytest.raises(SystemExit):
  #   parser.parse_args(['foo'])
  #   out, err = capfd.readouterr()
  out = runargs(["foo"])
  print("parser.py: error: argument command:".index("a"))
  assert "invalid choice: 'foo'" in out.err
  # assert "error: argument command: invalid choice: 'foo'" in out