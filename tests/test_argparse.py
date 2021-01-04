import pytest, sys
from reset import reset_db
sys.path.insert(1, './backup')
from parser import create_parser

@pytest.fixture
def parser():
  '''Creates the parser and returns it'''
  return create_parser()

@pytest.fixture
def parse_args_get_out(parser, capfd):
  '''Automatically parses args and returns output'''
  try:
    parser.parse_args(args)
  except SystemError:
    pass
  out, err = capfd.readouterr()
  return out

@pytest.mark.parametrize('parse_args_get_out', [['var1', 'var2']], indirect=True)
def test_check_if_enter_something_other_than_add_update_remove_run(parse_args_get_out, capfd):
  # with pytest.raises(SystemExit):
  #   parser.parse_args(['foo'])
  #   out, err = capfd.readouterr()
  out = parse_args_get_out()
  if "error: argument command: invalid choice: 'foo'" in out:
    assert True
  else:
    assert False

def test_test_add(parser, capfd):
  reset_db()
  with pytest.raises(SystemExit):
    parser.parse