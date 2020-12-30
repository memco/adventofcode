import re
from pprint import pprint

TEST_1_INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()

content_bag_re = r"(\d+)\s(.*?)\sbag"


def parse_input(input_list: list):
    rules = {}
    for ruleset in input_list:
        bag_color, content = ruleset.split(" bags contain ")
        rules[bag_color] = {}
        contents = content.split(", ")
        for contained_bag in contents:
            if (match := re.match(content_bag_re, contained_bag)) is not None:
                bag_count = match.group(1)
                content_color = match.group(2)
                rules[bag_color][content_color] = bag_count
    pprint(rules)
    return rules


def search_for_bag(input_str, target="shiny gold"):
    parsed = parse_input(input_str)
    contains_target = contains_bag(parsed, target)
    contains_containers = [
        contains_bag(parsed, con_target) for con_target in contains_bag
    ]
    total = contains_target + contains_containers
    print(total)


def contains_bag(bag_dict, target):
    return [bag for bag, contents in bag_dict.items() if target in contents.keys()]


if __name__ == "__main__":
    search_for_bag(TEST_1_INPUT)
