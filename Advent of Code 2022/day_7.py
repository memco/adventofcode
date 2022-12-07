from more_itertools import chunked
from os import path
from utils import PUZZLE_INPUT, logger

sample_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".strip().splitlines()


def main():
    # data = sample_input
    data = PUZZLE_INPUT
    total_disk_size = 70000000
    needed_space = 30000000
    logger.info(f"Starting.")
    dirs = {}
    cwd = None
    pwd = None
    cur_path = []
    for line in data:
        parts = line.strip().split(' ')
        if parts[0].startswith('dir'):
            continue
        if parts[0].startswith('$'):
            if parts[1].startswith('ls'):
                continue
            if parts[1] == 'cd':
                target = parts[2]
                if target == '..':
                    csize = dirs[pwd]['size']
                    cur_path.pop()
                    cwd = cur_path[-1]
                    dirs[''.join(cur_path)]['size'] += csize
                else:
                    cur_path.append(target)
                    cwd = target
            pwd = ''.join(cur_path)
            if ''.join(cur_path) not in dirs:
                dirs[''.join(cur_path)] = {'size': 0, 'children': {}}
            continue
        size = int(parts[0])
        d = ''.join(cur_path)
        dirs[d]['size'] += size
        dirs[d]['children'][parts[1]] = size
    while len(cur_path) > 1:
        csize = dirs[pwd]['size']
        cur_path.pop()
        cwd = cur_path[-1]
        # csize = sum(dirs[''.join(cur_path)]['children'].values())
        dirs[''.join(cur_path)]['size'] += csize
    large_dirs = [d['size'] for d in dirs.values() if d['size'] <= 100000]
    part_1 = sum(large_dirs)
    logger.info(f"{part_1=}")
    used = dirs['/']['size']
    free = total_disk_size - used
    remaining_needed = needed_space - free
    candidates = sorted([d['size'] for d in dirs.values() if d['size'] >= remaining_needed])
    part_2 = candidates[0]
    logger.info(f'{part_2=}')
    logger.info(f"Done.")


if __name__ == "__main__":
    main()