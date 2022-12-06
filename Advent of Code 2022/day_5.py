from collections import deque
from more_itertools import chunked
from os import path
from utils import PUZZLE_INPUT, logger

sample_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()


def main():
    # data = sample_input
    box_width = 3
    data = PUZZLE_INPUT
    logger.info(f"Starting.")
    starting_stacks = []
    stack_number = 0
    procedures = []
    for line in data:
        if "[" in line:
            starting_stacks.append(line)
            continue
        elif line.startswith('1'):
            stack_number = max([int(c) for c in line if c.strip()])

            # stack_number = max(map(int, stacks))
            continue
        if not line.strip():
            continue
        procedures.append(line)
    stacks = [deque() for s in range(stack_number)]
    stacks_list = [[] for s in range(stack_number)]
    for row in starting_stacks:
        for i, box in enumerate(chunked(row, 4)):
            if box[1] == ' ':
                continue
            stacks[i].append(box[1])
            stacks_list[i].append(box[1])
    for move in procedures:
        actions = move.split(' ')
        quantity = int(actions[1])
        source = int(actions[3]) - 1
        dest = int(actions[5]) - 1
        group = stacks_list[source][:quantity]
        reamining = stacks_list[source][quantity:]
        # stacks_list[dest] = list(reversed(group)) + stacks_list[dest]
        stacks_list[dest] = group + stacks_list[dest]
        stacks_list[source] = reamining
        logger.info("Moved.")
    top = ''.join([s[0] for s in stacks_list])
    logger.info(f"{top=}")
    logger.info(f"Done.")


if __name__ == "__main__":
    main()