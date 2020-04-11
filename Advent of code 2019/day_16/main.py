from itertools import cycle, repeat
from operator import iconcat
from functools import reduce

PUZZLE_INPUT = [int(digit) for digit in "59718730609456731351293131043954182702121108074562978243742884161871544398977055503320958653307507508966449714414337735187580549358362555889812919496045724040642138706110661041990885362374435198119936583163910712480088609327792784217885605021161016819501165393890652993818130542242768441596060007838133531024988331598293657823801146846652173678159937295632636340994166521987674402071483406418370292035144241585262551324299766286455164775266890428904814988362921594953203336562273760946178800473700853809323954113201123479775212494228741821718730597221148998454224256326346654873824296052279974200167736410629219931381311353792034748731880630444730593"]

TEST_1_INPUTS = [
    {
        'input': [1, 2, 3, 4, 5, 6, 7, 8],
        'phases': 4,
        'output': int("01029498")
    },
    {
        'input': [int(digit) for digit in "80871224585914546619083218645595"],
        'phases': 100,
        'output': 24176176
    },
    {
        'input': [int(digit) for digit in "19617804207202209144916044189917"],
        'phases': 100,
        'output': 73745418
    },
    {
        'input': [int(digit) for digit in "69317163492948606335995924319873"],
        'phases': 100,
        'output': 52432133
    },
]


def flatten(iterator):
    return reduce(iconcat, iterator, [])


class FFT():
    def __init__(self, input_signal: list, pattern: list = [0, 1, 0, -1]):
        self.pattern = pattern
        self.current_pattern = cycle(self.pattern)
        self.input_signal = input_signal
        self.output_signal = input_signal

    def cycle_for_position(self, position: int):
        return cycle(self.pattern_for_position(position))

    def pattern_for_position(self, position: int):
        return flatten(((repeat(digit, position+1)) for digit in self.pattern))

    def next_element(self, pattern):
        next(pattern)
        yield int(str(sum([element * next(pattern) for index, element in enumerate(self.output_signal)]))[-1:])

    def phase(self):
        yield [next(self.next_element(self.cycle_for_position(index))) for index, element in enumerate(self.output_signal)]

    def run(self, phases: int = 1):
        while phases > 0:
            print(f"Starting next phase ({phases} to go)")
            self.output_signal = next(self.phase())
            phases -= 1
            # print(f"{self.output_signal=}")

    @property
    def output(self):
        return int(''.join((str(digit) for digit in self.output_signal)))

REAL_PUZZLE_INPUT = flatten(repeat(PUZZLE_INPUT, 1000))

def test_1():
    for test in TEST_1_INPUTS:
        fft = FFT(test['input'])
        fft.run(test['phases'])
        result = fft.output
        # print(f"{result=} should beginwith {test['output']=}")
        if str(result)[:len(str(test['output']))] == str(test['output']):
            print("TEST PASSED!")
        else:
            print("TEST FAILED!")
    pass

def part_1():
    fft = FFT(PUZZLE_INPUT)
    result = fft.run(100)
    print(f"Part 1 on 100 phases: {result}")

def part_2():
    message_offset = int(''.join((str(digit) for digit in PUZZLE_INPUT[:7])))
    fft = FFT(REAL_PUZZLE_INPUT)
    fft.run(100)
    result = fft.output_signal[message_offset:message_offset + 8]
    print(''.join((str(digit) for digit in result)))

if __name__ == "__main__":
    # test_1()
    # part_1()
    part_2()