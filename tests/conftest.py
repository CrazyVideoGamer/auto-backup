import pytest, sys, argparse
sys.path.insert(0, './backup')
from parser import create_parser

@pytest.fixture
def parser() -> argparse.ArgumentParser:
  '''Creates the parser and returns it'''
  return create_parser()