
TEST_1_INPUT = [
    {
        'input': """
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA = > 1 FUEL """,
        'output': 31
    },
    {
        'input': """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E = > 1 FUEL """,
        'output': 165
    }
]

class Chemical():
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount

    @staticmethod
    def from_str(str):
        name, amount = str.split(' ')
        return Chemical(name, int(amount))


class Reaction():
    def __init__(self, formula):
        self.inputs = []
        input_chemicals, output_chemical = formula.split(' => ')        
        self.output = Chemical.from_str(output_chemical)
        for chemical in input_chemicals.split(', '):
            self.inputs.append(Chemical.from_str(chemical))
        
    def 


class NanoFactory():
    def __init__(self, reactions=None):
        self.reactions = []

    @staticmethod
    def from_reactions_str(reactions):
        factory = NanoFactory()
        for reaction in reactions.splitlines():
            # reaction = reaction.strip()
            # if not reaction:
            #     continue
            if reaction := reaction.strip():
                factory.reactions.append(Reaction(reaction))

    def calculate_ore_required_per_unit_of_fuel(self):
        materials_required = set()
        for reaction in reversed(self.reactions):
            for chemical in reaction.inputs:
                if chemical not in chemicals_required:
                    chemicals_required.add(chemical)
                else:
                    


def parse_reaction_list(reaction_str):
    for line in reaction_str.splitlines():
        line = line.strip()
        if not line:
            continue
        input_chemicals, output_chemical = line.split(' => ')


def test_1():
    for test in TEST_1_INPUT:
        # reactions = parese_reactions(test['input'])
        factory = NanoFactory(test['input'])



if __name__ == "__main__":
    test_1()