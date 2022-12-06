from more_itertools import chunked, sliding_window
from collections import Counter
from os import path
from utils import PUZZLE_INPUT, logger


sample_input = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjws
""".strip().splitlines()


def main():
    data = sample_input
    # data = PUZZLE_INPUT
    logger.info(f"Starting.")
    for line in data:
        for w in sliding_window(line, 4):
            c = Counter(w)
            if any(v > 1 for v in c.values()):
                continue
            part_1 = line.index(''.join(w))+len(w)
            logger.info(f"{part_1=}")
            break
        for w in sliding_window(line, 14):
            c = Counter(w)
            if any(v > 1 for v in c.values()):
                continue
            part_two = line.index(''.join(w))+len(w)
            logger.info(f"{part_two=}")
            break
    logger.info(f"Done.")


if __name__ == "__main__":
    main()