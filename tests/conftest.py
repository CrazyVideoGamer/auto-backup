import pytest, sys

sys.path.insert(1, './backup')
from parser import create_parser

@pytest.fixture
def parser():
  '''Creates the parser and returns it'''
  return create_parser()