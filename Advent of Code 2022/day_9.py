from more_itertools import chunked
from os import path
from utils import *

sample_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".strip().splitlines()

sample_input_2 ="""
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip().splitlines()


def main(data, tail_count=1):
    logger.info(f"Starting.")
    head, tails = [0,0], [[0,0] for _ in range(tail_count)]
    tail_path = {tuple(tails[-1])}
    for line in data:
        direction, distance = line.split(" ")
        magnitude = 1 if direction in {'R', 'U'} else -1
        index = 0 if direction in {'L', 'R'} else 1
        for d in range(int(distance)):
            new_position = 1 * magnitude
            head[index] += new_position
            cur_head = head
            for i, tail in enumerate(tails):
                diff_in_tail_x = abs(cur_head[0] - tail[0])
                diff_in_tail_y = abs(cur_head[1] - tail[1])
                tail_should_move = diff_in_tail_x > 1 or diff_in_tail_y > 1
                if tail_should_move:
                    new_tail_x = min(diff_in_tail_x, 1)
                    tail_x_magnitude = 1 if tail[0] < cur_head[0] else -1
                    new_tail_y = min(diff_in_tail_y, 1)
                    tail_y_magnitude = 1 if tail[1] < cur_head[1] else -1
                    new_tail = [tail[0] + new_tail_x*tail_x_magnitude, tail[1] + new_tail_y*tail_y_magnitude]
                    tails[i] = new_tail
                cur_head = tails[i]
            tail_path.add(tuple(tails[-1]))
    logger.info("Done.")
    return len(tail_path)


if __name__ == "__main__":
    logger.info(f"Part 1 sample: {main(sample_input)}")
    logger.info(f"Part 1 full: {main(PUZZLE_INPUT)}")
    logger.info(f"Part 2 sample_input: {main(sample_input, 9)}")
    logger.info(f"Part 2 sample_input_2: {main(sample_input_2, 9)}")
    logger.info(f"Part 2 PUZZLE_INPUT: {main(PUZZLE_INPUT, 9)}")