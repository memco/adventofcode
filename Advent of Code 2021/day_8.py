import timeit
from collections import Counter
from functools import lru_cache

# test_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

test_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

def parse_line(line):
    signal_patterns, output = line.split(' | ')
    return signal_patterns, output

def parse_input(inputs):
    lines = [parse_line(line) for line in inputs]
    # signal_patters = {l[0] for l in lines}
    outputs = [l[1] for l in lines]
    output_vals = []
    for o in outputs:
        vals = [(v, len(v)) for v in o.split(' ')]
        lengths = Counter([v[1] for v in vals])
        unique_vals = [v for v in vals if lengths(v[1]) == 1]
        pass
    # svals = sorted(output_vals, key= lambda v: v[1])
    # subsorted = [(sorted(v[0]), v[1]) for v in svals]
    pass


if __name__ == '__main__':
    times = []
    times.append(timeit.timeit('parse_input(test_input)', setup='from __main__ import parse_input, test_input', number=1))
    print(times)