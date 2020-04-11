from enum import Enum
import logging
import sys
from collections import namedtuple, deque
from itertools import permutations
from concurrent.futures import ThreadPoolExecutor
from tests import TEST_PROGRAMS, DAY_5_PART2_TESTS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

PROGRAM_INPUT = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 5, 19, 23, 2, 6, 23, 27, 1, 27, 5, 31, 2, 9, 31, 35, 1, 5, 35, 39, 2, 6, 39, 43, 2, 6, 43, 47, 1, 5, 47, 51, 2, 9, 51, 55, 1, 5, 55, 59, 1, 10, 59, 63, 1, 63, 6, 67, 1, 9, 67, 71, 1, 71, 6, 75, 1, 75, 13, 79, 2, 79, 13, 83, 2, 9, 83, 87, 1, 87, 5, 91, 1, 9, 91, 95, 2, 10, 95, 99, 1, 5, 99, 103, 1, 103, 9, 107, 1, 13, 107, 111, 2, 111, 10, 115, 1, 115, 5, 119, 2, 13, 119, 123, 1, 9, 123, 127, 1, 5, 127, 131, 2, 131, 6, 135, 1, 135, 5, 139, 1, 139, 6, 143, 1, 143, 6, 147, 1, 2, 147, 151, 1, 151, 5, 0, 99, 2, 14, 0, 0]

Param = namedtuple('Param', 'value mode')


class ParameterModes(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Program():
    NOUN_VERB_RANGE = range(0, 99)
    OPCODES = {
        99: {'move': 1, 'args': 0},
        1: {'move': 4, 'args': 3},
        2: {'move': 4, 'args': 3},
        3: {'move': 2, 'args': 1},
        4: {'move': 2, 'args': 1},
        5: {'move': 3, 'args': 2},
        6: {'move': 3, 'args': 2},
        7: {'move': 4, 'args': 3},
        8: {'move': 4, 'args': 3},
    }

    def __init__(self, memory: list = [], parameter_mode=None, default_inputs=None):
        self.initial_state = memory
        self.memory = []
        self.instruction_pointer = 0
        self.parameter_mode = ParameterModes.POSITION.value if not parameter_mode else parameter_mode
        self.default_inputs = deque(default_inputs) if default_inputs is not None else None
        self.outputs = deque()
        self.terminated = False
        self.initialize()

    def initialize(self):
        self.memory = self.initial_state.copy()
        self.instruction_pointer = 0
        self.thread = ThreadPoolExecutor()

    def change_mode(self, mode: int):
        self.parameter_mode = mode
        self.initialize()

    def init_noun_and_verb(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb

    @property
    def noun(self):
        return self.memory[1]

    @property
    def verb(self):
        return self.memory[2]

    def get_param_value(self, param: Param):
        param_mode = param.mode if param.mode is not None else self.parameter_mode
        if param_mode == ParameterModes.POSITION.value:
            return self.memory[param.value]
        if param_mode == ParameterModes.IMMEDIATE.value:
            return param.value
        logger.error("INVALID PARAMETER MODE!")

    def add_positions(self, param1: Param, param2: Param, param3: Param):
        self.memory[param3.value] = self.get_param_value(param1) + self.get_param_value(param2)
        return True

    def multiply_positions(self, param1: Param, param2: Param, param3: Param):
        self.memory[param3.value] = self.get_param_value(param1) * self.get_param_value(param2)
        return True

    def store_at(self, param1: Param):
        op_input = None
        while not op_input:
            try:
                op_input = self.default_inputs.popleft()
            except Exception:
                
        # if self.default_inputs:
        #     try:
        #         op_input = self.default_inputs.popleft()
        #     except Exception:
        #         pass
        # if op_input is None:
        #     op_input = input(f"Opcode 3 needs input to store in address {param1.value}: ")
        self.memory[param1.value] = int(op_input)
        return True

    def read_from(self, param1: Param):
        print(f"Reading value {self.get_param_value(param1)}")
        self.outputs.append(self.get_param_value(param1))
        return True

    def terminate(self):
        self.terminated = True
        return self.memory[0]

    def jump_if_true(self, param1: Param, param2: Param):
        if self.get_param_value(param1):
            self.instruction_pointer = self.get_param_value(param2)
            return False
        return True

    def jump_if_false(self, param1: Param, param2: Param):
        if not self.get_param_value(param1):
            self.instruction_pointer = self.get_param_value(param2)
            return False
        return True

    def less_than(self, param1: Param, param2: Param, param3: Param):
        self.memory[param3.value] = 1 if self.get_param_value(param1) < self.get_param_value(param2) else 0
        return True

    def equals(self, param1: Param, param2: Param, param3: Param):
        self.memory[param3.value] = 1 if self.get_param_value(param1) == self.get_param_value(param2) else 0
        return True

    def get_procedure_for_opcode(self, opcode: int):
        if opcode == 99:
            logger.debug("Program should terminate.")
            return self.terminate
        elif opcode == 1:
            logger.debug("Program should add next two ops into 3rd op.")
            return self.add_positions
        elif opcode == 2:
            logger.debug("Program should multiply next two ops into 3rd op.")
            return self.multiply_positions
        elif opcode == 3:
            logger.debug("Program should save input into address.")
            return self.store_at
        elif opcode == 4:
            logger.debug("Program should read from address.")
            return self.read_from
        elif opcode == 5:
            logger.debug("Program should jump if true.")
            return self.jump_if_true
        elif opcode == 6:
            logger.debug("Program should jump if false.")
            return self.jump_if_false
        elif opcode == 7:
            logger.debug("Program should check value is less than.")
            return self.less_than
        elif opcode == 8:
            logger.debug("Program should check value is equal.")
            return self.equals
        else:
            logger.error("Invalid Opcode ({opcode}!")

    def run(self):
        while True:
            str_instruction = str(self.memory[self.instruction_pointer])
            opcode = int(str_instruction[-2:])
            instruction_modes = list(str_instruction[:-2])
            instruction_modes.reverse()
            number_of_parameters = self.OPCODES[opcode]['args']
            parameters = {}
            for param in range(0, number_of_parameters):
                mode = None
                try:
                    mode = int(instruction_modes[param])
                except (KeyError, TypeError, IndexError):
                    pass
                param_location = self.instruction_pointer + (param + 1)
                parameters[param] = Param(self.memory[param_location], mode)
            should_move = self.get_procedure_for_opcode(opcode)(*parameters.values())
            if should_move:
                self.instruction_pointer += self.OPCODES[opcode]['move']
            if opcode == 99:
                break

    def process_program(self):
        pos = self.instruction_pointer
        opcode = self.memory[self.instruction_pointer]
        logger.debug(f"Starting at {pos} with {opcode} for {self.memory}")
        while opcode:
            pos = self.instruction_pointer
            try:
                move = self.OPCODES[opcode]
                if opcode == 99:
                    logger.debug("Program should terminate.")
                    break
                elif opcode == 1:
                    logger.debug("Program should add next two ops into 3rd op.")
                    self.add_positions(self.memory[pos+1], self.memory[pos+2], self.memory[pos+3])
                elif opcode == 2:
                    logger.debug("Program should multiply next two ops into 3rd op.")
                    self.multiply_positions(self.memory[pos + 1], self.memory[pos + 2], self.memory[pos + 3])
                elif opcode == 3:
                    logger.debug("Program should save input into address.")
                    self.store_at(self.memory[pos + 1], self.memory[pos + 2])
                else:
                    logger.error("Invalid Opcode ({opcode}!")
                self.instruction_pointer += move
                opcode = self.memory[pos]
            except Exception:
                logger.exception("Exeption occured")
                break
        logger.debug(f"Program is {self.memory}")
        return self.memory

    def find_noun_and_verb_for(self, output: int):
        for noun, verb in ((noun, verb) for noun in self.NOUN_VERB_RANGE for verb in self.NOUN_VERB_RANGE):
            self.initialize()
            self.init_noun_and_verb(noun, verb)
            self.process_program()
            if self.memory[0] == output:
                logger.info(f"Solution found. {noun}, {verb}: {100 * noun + verb}")
                break
        if self.memory[0] != output:
            logger.info("No solution found.")


class AmplifierController():
    POSSIBLE_SEQUENCE_INPUTS = range(0, 5)
    PHASE_2_SEQUENCE_INPUTS = range(5, 10)

    def __init__(self, program=[], phase_sequence=[]):
        self.program = program
        self.phase_sequence = deque(phase_sequence)
        self.programs = []
        self.possible_sequences = []

    def calculate_phase_sequence(self):
        if self.phase_sequence:
            self.possible_sequences.append({'sequence': self.phase_sequence, 'output': self.process_phase_sequence(self.phase_sequence)})
        else:
            for phase_sequence in permutations(self.POSSIBLE_SEQUENCE_INPUTS):
                output = self.process_phase_sequence(phase_sequence)
                self.possible_sequences.append({'sequence': phase_sequence, 'output': output})

    @property
    def max_output_signal(self):
        if not self.possible_sequences:
            self.calculate_phase_sequence()
        return sorted(self.possible_sequences, key=lambda s: s['output'])[-1:][0]['output']

    def calculate_feedback_sequence(self):
        if self.phase_sequence:
            self.possible_sequences.append({'sequence': self.phase_sequence, 'output': self.process_feedback_loop(self.phase_sequence)})
        else:
            for phase_sequence in permutations(self.PHASE_2_SEQUENCE_INPUTS):
                output = self.process_feedback_loop(phase_sequence)
                self.possible_sequences.append({'sequence': phase_sequence, 'output': output})

    @property
    def max_output_from_feedback_loop(self):
        if not self.possible_sequences:
            self.calculate_feedback_sequence()
        return sorted(self.possible_sequences, key=lambda s: s['output'])[-1:][0]['output']

    @property
    def all_terminated(self):
        return all(prog.terminated for prog in self.programs)

    def process_feedback_loop(self, phase_sequence, last_output=0):
        program_a = Program(self.program, default_inputs=[phase_sequence[0]])
        program_b = Program(self.program, default_inputs=[phase_sequence[1]])
        program_c = Program(self.program, default_inputs=[phase_sequence[2]])
        program_d = Program(self.program, default_inputs=[phase_sequence[3]])
        program_e = Program(self.program, default_inputs=[phase_sequence[4]])
        self.programs = [program_a, program_b, program_c, program_d, program_e]
        while not self.all_terminated:
            for prog in self.programs:
                if not prog.terminated:
                    prog.default_inputs.append(last_output)
                    prog.run()
                    last_output = prog.outputs.pop()
        return last_output

    def process_phase_sequence(self, phase_sequence):
        program_a = Program(self.program, default_inputs=[phase_sequence[0], 0])
        program_a.run()
        program_b = Program(self.program, default_inputs=[phase_sequence[1], program_a.outputs.pop()])
        program_b.run()
        program_c = Program(self.program, default_inputs=[phase_sequence[2], program_b.outputs.pop()])
        program_c.run()
        program_d = Program(self.program, default_inputs=[phase_sequence[3], program_c.outputs.pop()])
        program_d.run()
        program_e = Program(self.program, default_inputs=[phase_sequence[4], program_d.outputs.pop()])
        program_e.run()
        return program_e.outputs.pop()


def run_tests():
    for program in TEST_PROGRAMS:
        current_program = Program(program['input'])
        current_program.run()
        if current_program.memory == program['output']:
            logger.info("TEST PASSED!")
        else:
            logger.warning("TEST FAILED!")


def run_day5_part_2_tests():
    for program in DAY_5_PART2_TESTS:
        current_program = Program(program['input'], program['mode'])
        current_program.run()
        current_program.initialize()
        current_program.run()


def day_5():
    DAY5_INPUT = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1002, 114, 19, 224, 1001, 224, -646, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1101, 40, 62, 225, 1101, 60, 38, 225, 1101, 30, 29, 225, 2, 195, 148, 224, 1001, 224, -40, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1001, 143, 40, 224, 101, -125, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 224, 223, 223, 101, 29, 139, 224, 1001, 224, -99, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 224, 223, 223, 1101, 14, 34, 225, 102, 57, 39, 224, 101, -3420, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1101, 70, 40, 225, 1102, 85, 69, 225, 1102, 94, 5, 225, 1, 36, 43, 224, 101, -92, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 1, 224, 224, 1, 224, 223, 223, 1102, 94, 24, 224, 1001, 224, -2256, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 1, 224, 1, 223, 224, 223, 1102, 8, 13, 225, 1101, 36, 65, 224, 1001, 224, -101, 224, 4, 224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 329, 1001, 223, 1, 223, 1108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 344, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 359, 101, 1, 223, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 374, 101, 1, 223, 223, 1107, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 389, 101, 1, 223, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 404, 101, 1, 223, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 419, 101, 1, 223, 223, 108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 434, 101, 1, 223, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 449, 101, 1, 223, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 464, 1001, 223, 1, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 7, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 494, 1001, 223, 1, 223, 8, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 509, 101, 1, 223, 223, 107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 524, 1001, 223, 1, 223, 7, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 539, 1001, 223, 1, 223, 1007, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 554, 1001, 223, 1, 223, 8, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 569, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 584, 1001, 223, 1, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1, 223, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 614, 101, 1, 223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 629, 101, 1, 223, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 659, 1001, 223, 1, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 674, 101, 1, 223, 223, 4, 223, 99, 226]
    program = Program(DAY5_INPUT)
    program.run()


def day_7_test_1():
    DAY_7_TEST_INPUT = [
        {
            'program': [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
            'phase_sequence': [4, 3, 2, 1, 0],
            'output': 43210
        },
        {
            'program': [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
            'phase_sequence': [0, 1, 2, 3, 4],
            'output': 54321
        },
        {
            'program': [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0],
            'phase_sequence': [1,0,4,3,2],
            'output': 65210
        },
    ]
    for test in DAY_7_TEST_INPUT:
        amplifier = AmplifierController(test['program'], test['phase_sequence'])
        if amplifier.max_output_signal == test['output']:
            print("TEST PASSED!")
        else:
            print("TEST FAILED!")


DAY_7_INPUT = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
def day_7_part_1():
    amp = AmplifierController(DAY_7_INPUT)
    print(amp.max_output_signal)


def day_7_test_2():
    DAY_7_TEST_INPUT = [
        {
            'program': [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
            'phase_sequence': [9, 8, 7, 6, 5],
            'output': 139629729
        },
        {
            'program': [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10],
            'phase_sequence': [9, 8, 7, 6, 5],
            'output': 18216
        },
    ]
    for test in DAY_7_TEST_INPUT:
        amplifier = AmplifierController(test['program'], test['phase_sequence'])
        if amplifier.max_output_from_feedback_loop == test['output']:
            print("TEST PASSED!")
        else:
            print("TEST FAILED!")

if __name__ == "__main__":
    # program = Program(PROGRAM_INPUT)
    # program.find_noun_and_verb_for(19690720)
    # run_tests()
    # day_5()
    # run_day5_part_2_tests()
    # day_7_test_1()
    # day_7_part_1()
    day_7_test_2()