import pytest, sys
sys.path.insert(1, './backup')
from parser import create_parser

@pytest.fixture
def parser():
  '''Creates the parser and returns it'''
  return create_parser()

def test_check_if_entering_a_bad_command_works_1(parser, capfd):
  parser.parse_args(['foo'])
  print("test")
  out, err = capfd.readouterr()
  if "error: argument command: invalid choice: 'foo'" in out:
    assert True
  else:
    assert False


print(create_parser())