import logging
import sys
from os import path
import inspect
from collections.abc import Mapping
from concurrent.futures import as_completed
from typing import Iterable, Sequence
from functools import lru_cache

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

def yield_from_futures(futs):
    is_mapping = isinstance(futs, Mapping)
    for f in as_completed(futs):
        try:
            fut = futs[f] if is_mapping else f
            r = fut.result()
            yield r
        except Exception:
            logger.debug("Failed to get result.", exc_info=True)

GRID_TYPE = Sequence[Sequence]

def walk_grid(grid: GRID_TYPE) -> Iterable:
    for r, _r in enumerate(grid):
        for c,_ in enumerate(_r):
            yield grid[r][c], r, c

def grid_colum(column_no: int, grid: GRID_TYPE):
    cols = list(map(list, zip(*grid)))
    return cols[column_no]

def grid_cardinals_from_cell(grid: GRID_TYPE):
    height = len(grid)
    width = len(grid[0])
    for i in walk_grid(grid):
        row = grid[i[1]]
        column = grid_colum(i[2], grid)
        above = column[:i[2]]
        below = column[min(i[2]+1, height):]
        to_left = row[:i[1]]
        to_right = row[min(i[1]+1, width):]
        yield i, above, below, to_left, to_right


@lru_cache(maxsize=1000)
def has_item_before(rnum):
    return rnum > 0 


@lru_cache(maxsize=1000)
def has_item_after(rnum, max_num):
    return rnum < max_num


@lru_cache(maxsize=10000)
def neighbor_locations(cell: tuple, width, height):
    """ Return the indexes of neighboring cells from a given grid cell if one exists.
    Does not tell where the neighbor is in relation to the current cell.
    """
    rnum = cell[0]
    cnum = cell[1]
    has_col_above = has_item_before(rnum)
    has_col_below = has_item_after(rnum, height)
    has_col_left = has_item_before(cnum)
    has_col_right = has_item_after(cnum, width)
    col_left = (rnum, cnum - 1) if has_col_left else None
    col_right = (rnum, cnum + 1) if has_col_right else None
    col_above = (rnum - 1, cnum) if has_col_above else None
    col_below = (rnum + 1, cnum) if has_col_below else None
    return col_left,col_right,col_above,col_below


def non_empty_neighbors(neighbors):
    return {c for c in neighbors if c is not None}


def collect_neighbors_if(cell: tuple, grid: GRID_TYPE, visited=None):
    """ Return neighboring items of a point in a grid cell and mark it visited
    From AOC 2019 Day 9
    """
    visited |= {cell}
    width = len(grid[0]) - 1
    height = len(grid) - 1
    neighbors = non_empty_neighbors(neighbor_locations(cell, width, height))
    if not neighbors:
        return
    (rnum,cnum) = cell
    val = grid[rnum][cnum]
    # TODO: Generalize filtering
    filtered_neighbors = [(r,c) for r,c in neighbors if grid[r][c] >= val and (r,c) not in visited]
    if not filtered_neighbors:
        return
    for n in filtered_neighbors:
        collect_neighbors_if(n, grid, visited=visited)