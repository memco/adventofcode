from more_itertools import chunked
from os import path
from utils import *

sample_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".strip().splitlines()


def main():
    # data = sample_input
    data = PUZZLE_INPUT
    logger.info(f"Starting.")
    register_x = 1
    cycles = 0
    interesting_signal = 20
    interesting_signals = 0
    isigs = []
    crt_row = ['.' for _ in range(40)]
    crt = [list(crt_row), list(crt_row), list(crt_row), list(crt_row), list(crt_row), list(crt_row)]
    for line in data:
        parts = line.split(" ")
        op_cycles = 1 if parts[0] == 'noop' else 2
        for c in range(op_cycles):
            current_row, i = divmod(cycles, 40)
            sprite_positions = range(max(0, register_x -1),min(39, register_x+2))
            if i in sprite_positions:
                crt[current_row][i] = '#'
            cycles += 1
            if cycles == interesting_signal:
                signal_strength = register_x * cycles
                interesting_signals += signal_strength
                isigs.append((cycles, signal_strength))
                interesting_signal += 40
        if parts[0] == 'addx':
            register_x += int(parts[1])
    logger.info(f"Part 1: {interesting_signals}")
    for l in crt:
        print(l)
    logger.info(f"Done.")


if __name__ == "__main__":
    main()