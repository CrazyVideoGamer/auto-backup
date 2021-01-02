from pathlib import Path
from helpers import Minute, str2bool
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command -h') # TODO: Try to add --help as well

add_parser = subparsers.add_parser("add", help="add -h")
add_parser.add_argument('target', nargs=1, type=Path)
add_parser.add_argument('interval', nargs=1, type=Minute)
add_parser.add_argument('--setDirectory', type=str2bool, help='set directory to add backups')