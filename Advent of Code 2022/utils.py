import logging
import sys
from os import path
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

def get_puzzle_input(day_path):
    PUZZLE_INPUT = []
    if path.exists(day_path):
        PUZZLE_INPUT = [l.strip() for l in open(day_path).readlines()]
    return PUZZLE_INPUT