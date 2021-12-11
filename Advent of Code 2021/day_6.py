import timeit
from functools import lru_cache
from itertools import chain

test_input = [3,4,3,1,2]
day_7_input = [4,3,4,5,2,1,1,5,5,3,3,1,5,1,4,2,2,3,1,5,1,4,1,2,3,4,1,4,1,5,2,1,1,3,3,5,1,1,1,1,4,5,1,2,1,2,1,1,1,5,3,3,1,1,1,1,2,4,2,1,2,3,2,5,3,5,3,1,5,4,5,4,4,4,1,1,2,1,3,1,1,4,2,1,2,1,2,5,4,2,4,2,2,4,2,2,5,1,2,1,2,1,4,4,4,3,2,1,2,4,3,5,1,1,3,4,2,3,3,5,3,1,4,1,1,1,1,2,3,2,1,1,5,5,1,5,2,1,4,4,4,3,2,2,1,2,1,5,1,4,4,1,1,4,1,4,2,4,3,1,4,1,4,2,1,5,1,1,1,3,2,4,1,1,4,1,4,3,1,5,3,3,3,4,1,1,3,1,3,4,1,4,5,1,4,1,2,2,1,3,3,5,3,2,5,1,1,5,1,5,1,4,4,3,1,5,5,2,2,4,1,1,2,1,2,1,4,3,5,5,2,3,4,1,4,2,4,4,1,4,1,1,4,2,4,1,2,1,1,1,1,1,1,3,1,3,3,1,1,1,1,3,2,3,5,4,2,4,3,1,5,3,1,1,1,2,1,4,4,5,1,5,1,1,1,2,2,4,1,4,5,2,4,5,2,2,2,5,4,4]

@lru_cache(maxsize=None)
def change_zeroes(num_zeroes):
    return [8,6] * num_zeroes

def generate_next(inputs):
    next_gen = [i-1 for i in inputs if i != 0]
    zeroes = len(inputs) - len(next_gen)
    return next_gen + change_zeroes(zeroes)


@lru_cache(maxsize=None)
def spawn_created_up_to(next_spawn, days_until_end):
    cycles_in_period = days_until_end / 7
    pass


def string_manip(inputs):
    # as_str = ''.join(map(str,sorted(inputs)))
    i = 1
    s = sorted(inputs)
    as_str = ''.join(map(str, s))
    while i <= 80:
        current_spanws = len(as_str)
        ones_start = as_str.find('1')
        zeroes = as_str[:ones_start]
        numzs = len(zeroes)
        to_decrement = as_str[ones_start:]
        decrement_by = '1' * len(to_decrement)
        new_gen = str((int(to_decrement) - int(decrement_by)))
        has_sevens = new_gen.find('7')
        sevens = has_sevens if has_sevens > -1 else len(new_gen)
        as_str = (new_gen[:sevens] + '6'* numzs + new_gen[sevens:]).zfill(current_spanws)
        if zeroes:
            as_str += '8' * numzs
        # print(f"Day {i}: {as_str}")
        i += 1
    print(len(as_str))

@lru_cache(maxsize=10)
def decrement(a):
    return a-1

@lru_cache(maxsize=None)
def replace_zeroes(zeroes):
    return [6,8] * zeroes

@lru_cache(maxsize=None)
def spawn_next(spawn):
    if spawn == 0:
        return replace_zeroes(1)
    return [decrement(spawn)]

# @lru_cache(maxsize=None)
def spawn_next_generation(inputs):
    if not inputs:
        return []
    this = inputs.pop()
    return spawn_next(this) + spawn_next_generation(inputs) 


def list_manip(inputs, days_to_simulate=80):
    while days_to_simulate:
        s = sorted(inputs, reverse=True)
        current_spawns = len(inputs)
        new_zs = []
        if s[-1] == 0:
            last_z = s.index(0)
            numzs = current_spawns - last_z
            s = s[:last_z]
        # zeroes = s[:zend]
            new_zs = replace_zeroes(numzs)
        inputs = list(map(decrement, s)) + new_zs
        # print(f"Day {i}: {s}")
        days_to_simulate -= 1
    print(len(inputs))

@lru_cache(maxsize=None)
def how_many_spawn(current_age, days_left):
    # print(current_age)
    # cycles_left = days_left // 7
    new_spawn = 0
    while days_left:
        new_age = spawn_next(current_age)
        days_left -= 1
        current_age = new_age[0]
        if len(new_age) == 1:
            continue
        new_spawn += how_many_spawn(new_age[1], days_left)
    print(new_spawn+1)
    return new_spawn + 1
    

def recursive_spawn(inputs, days_to_simulate=80):
    # i = 1
    spawns = sum(how_many_spawn(s, days_to_simulate) for s in inputs)
    print(spawns)
    # while days_to_simulate:
    #     inputs = chain.from_iterable([spawn_next(i) for i in inputs])
    #     # new_spawn_in = days_until_nex_spawn(inputs)
    #     # i += 1
    #     days_to_simulate -= 1
    # print(len(list(inputs)))


def days_until_nex_spawn(inputs):
    return sorted(inputs)[0]


def simulate_growth(inputs, days_to_simulate=80):
    # return list_manip(inputs)
    return recursive_spawn(inputs, days_to_simulate)
    i = 1
    while i <= days_to_simulate:
        # current_sum = sum(inputs)
        inputs = generate_next(inputs)
        # print(f"Day {i}: {inputs}")
        # spawn_created_up_to()
        # new_sum = sum(inputs)
        # print(f'{current_sum} -> {new_sum} ({new_sum - current_sum}): {len(inputs)}')
        i += 1

    print(len(inputs))

if __name__ == '__main__':
    times = []
    # times.append(timeit.timeit('simulate_growth(test_input)', setup='from __main__ import simulate_growth, test_input', number=1))
    # times.append(timeit.timeit('simulate_growth(day_7_input)', setup='from __main__ import simulate_growth, day_7_input', number=1))
    # times.append(timeit.timeit('simulate_growth(test_input, 256)', setup='from __main__ import simulate_growth, test_input', number=1))
    times.append(timeit.timeit('simulate_growth(day_7_input, 256)', setup='from __main__ import simulate_growth, day_7_input', number=1))
    print(times)