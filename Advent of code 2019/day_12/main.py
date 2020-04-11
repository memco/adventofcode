from itertools import combinations
from dataclasses import dataclass
from math import gcd

PART_1_TESTS = [
    {
        'input': """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
""",
        'steps': 10,
        'total_energy': 179
    },
    {
        'input': """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
""",
        'steps': 100,
        'total_energy': 1940
    }
]

PUZZLE_INPUT = """
<x=-7, y=-8, z=9>
<x=-12, y=-3, z=-4>
<x=6, y=-17, z=-9>
<x=4, y=-10, z=-6>
"""


def lcm(a, b):
    return a*b // gcd(a, b)


@dataclass
class Vector():
    x: int = 0
    y: int = 0
    z: int = 0

    def __mul__(self, scalar: int):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def sum(self):
        return sum((abs(value) for value in (self.x, self.y, self.z)))


@dataclass
class Body():
    position: Vector = Vector()
    velocity: Vector = Vector()

    @property
    def potential_energy(self):
        return self.position.sum()

    @property
    def kinetic_energy(self):
        return self.velocity.sum()

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy


class Simulation():
    def __init__(self, bodies):
        self.bodies = bodies
        self.invert_velocities = True
        self.energies_seen = set()

    def step(self):
        self.apply_gravity()
        self.apply_velocity()

    def apply_gravity(self):
        for body1, body2 in combinations(self.bodies, 2):
            for axis in Vector.__dataclass_fields__:
                body1_val = getattr(body1.position, axis)
                body2_val = getattr(body2.position, axis)
                setattr(body1.velocity, axis, getattr(body1.velocity, axis) + self.ternary_compare(body1_val, body2_val))
                setattr(body2.velocity, axis, getattr(body2.velocity, axis) + self.ternary_compare(body2_val, body1_val))

    def ternary_compare(self, left: int, right: int):
        if left < right:
            return 1
        if left == right:
            return 0
        if left > right:
            return -1

    def apply_velocity(self):
        for body in self.bodies:
            for axis in Vector.__dataclass_fields__:
                setattr(body.position, axis, getattr(body.position, axis) + getattr(body.velocity, axis))

    def step_to(self, time: int = 1):
        while time > 0:
            self.step()
            time -= 1

    def find_steps_to_match_previous_state(self):
        steps = 0
        found = False
        while True:
            try:
                self.step()
                steps += 1
                if self.total_energy in self.energies_seen:
                    found = True
                    break
                self.energies_seen.add(self.total_energy)
            except Exception:
                print("Error! Exiting.")
                break
        if found:
            print(f"Matching state found after {steps} steps.")
        else:
            print("No match found after {steps} steps.")

    @property
    def total_energy(self):
        return sum(body.total_energy for body in self.bodies)

    def part2():
        return lcm(lcm(xs, ys), zs)


def parse_inputs(inputs):
    BODIES = []
    for line in inputs.splitlines():
        line = line.strip()
        if not line:
            continue
        attrs = line[1:-1].split(', ')
        position = []
        for setting in attrs:
            attr, value = setting.split('=')
            position.append(int(value))
        BODIES.append(Body(Vector(*position), Vector()))
    sim = Simulation(BODIES)
    return sim


def part1_test():
    for test in PART_1_TESTS:
        sim = parse_inputs(test['input'])
        sim.step_to(test['steps'])
        if sim.total_energy == test['total_energy']:
            print("TEST PASSED!")
        else:
            print("TEST FAILED!")


def part_1():
    sim = parse_inputs(PUZZLE_INPUT)
    sim.step_to(1000)
    print(sim.total_energy)


def part_2():
    sim = parse_inputs(PUZZLE_INPUT)
    sim.find_steps_to_match_previous_state()


if __name__ == "__main__":
    # part1_test()
    # part_1()
    part_2()