import logging
import sys
from os import path
import inspect


logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)


def get_puzzle_input(day_path = None):
    # get_importer_path()
    day_path = day_path or importer_path.replace('.py', '.txt')
    PUZZLE_INPUT = []
    if path.exists(day_path):
        PUZZLE_INPUT = [l.strip() for l in open(day_path).readlines()]
    return PUZZLE_INPUT

# Hacky way to not have to make every day need to figure out where to import puzzle data from.
# from utils import PUZZLE_INPUT will populate PUZZLE_INPUT with day_<num>.txt's contents if possible.
# Assumes the .txt lives in the same folder as the day's .py file.
importer_path = [f.filename for f in inspect.stack()[1:] if f.filename != __file__ and path.dirname(__file__) in f.filename][0]
PUZZLE_INPUT = get_puzzle_input() 