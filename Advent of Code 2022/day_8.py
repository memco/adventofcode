from more_itertools import chunked
from os import path
from utils import PUZZLE_INPUT, logger


sample_input = """30373
25512
65332
33549
35390""".splitlines()


def can_see(row):
    can_see = 0
    visible_cols = []
    for i, t in enumerate(row):
        to_consider = row[:i]
        if not all(v < t for v in to_consider):
            if all(v <= t for v in row[i:]):
                break
            continue
        can_see += 1
        visible_cols.append(i)
        if all(v <= t for v in row[i:]):
            break
    return can_see, visible_cols

def main():
    # data = sample_input
    data = PUZZLE_INPUT
    grid = [[int(c) for c in l] for l in data]
    vgrid = [[False for c in r] for r in data]
    for i, row in enumerate(grid):
        visibility = can_see(row)
        for j in visibility[1]:
            vgrid[i][j] = True
        visibility = can_see(list(reversed(row)))
        for j in visibility[1]:
            vgrid[i][-j - 1] = True
    cols = list(map(list, zip(*grid)))
    for i, col in enumerate(cols):
        visibility = can_see(col)
        for j in visibility[1]:
            vgrid[j][i] = True
        visibility = can_see(list(reversed(col)))
        for j in visibility[1]:
            vgrid[-j - 1][i] = True
    part_1 = sum(1 for r in vgrid for c in r if c is True)
    logger.info(f"{part_1=}")

    part_2 = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            trees_up = reversed([grid[r][j] for r,rr in enumerate(grid) if r < i])
            trees_down = [grid[r][j] for r,rr in enumerate(grid) if r > i]
            trees_left = reversed(row[:j])
            trees_right = row[min(len(row), j+1):]
            distance_up = trees_visible_to(col, trees_up)
            distance_down = trees_visible_to(col, trees_down)
            distance_right = trees_visible_to(col, trees_right)
            distance_left = trees_visible_to(col, trees_left)
            scenic_score = distance_up * distance_down  * distance_right * distance_left
            if scenic_score > part_2:
                part_2 = scenic_score
    logger.info(f"{part_2=}")
    logger.info(f"Done.")

def trees_visible_to(tree, trees):
    visible = 0
    for t in trees:
        visible += 1
        if t >= tree:
            break
    return visible

if __name__ == "__main__":
    main()