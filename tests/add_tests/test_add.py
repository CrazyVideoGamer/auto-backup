import pytest, sys
sys.path.append("..")
from readout import runargs

def add_add_to_args(args):
  return [["add"] + arg for arg in args]

not_enough_args = [[], ["target"]]
not_enough_args = add_add_to_args(not_enough_args)

@pytest.mark.parametrize('args', not_enough_args)
def test_not_enough_args(parser, args):
  test = runargs(args)

  assert "the following arguments are required" in test.err

wrong_type = [
  ["////badfilename", 10, "./cooldirn"], ["coolfilename", "bad minute num", "./cooldir"
  ],
  ["coolfilename", 10, "/////baddir"]
]
wrong_type = add_add_to_args(not_enough_args)

@pytest.mark.parametrize('args', wrong_type)
def test_wrong_type(parser, args):
  test = runargs(args)
  print(test.err)