from .tests import TEST_PROGRAMS
from .program import Program, PROGRAM_INPUT
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def process_program(program):

    def add_positions(pos1, pos2, pos3):
        logger.debug(program)
        logger.debug(pos1)
        logger.debug(pos2)
        logger.debug(pos3)
        logger.debug(program[pos1])
        logger.debug(program[pos2])
        logger.debug(program[pos3])
        logger.debug(f"{program[pos1]} + {program[pos2]} = {program[pos1] + program[pos2]}")
        program[pos3] = program[pos1] + program[pos2]

    def multiply_positions(pos1, pos2, pos3):
        logger.debug(f"{program[pos1]} * {program[pos2]} = {program[pos1] * program[pos2]}")
        program[pos3] = program[pos1] * program[pos2]

    pos = 0
    opcode = program[pos]
    logger.debug(f"Starting at {pos} with {opcode} for {program}")
    while opcode:
        try:
            if opcode == 99:
                logger.debug("Program should terminate.")
                break
            elif opcode == 1:
                logger.debug("Program should add next two ops into 3rd op.")
                add_positions(program[pos+1], program[pos+2], program[pos+3])
            elif opcode == 2:
                logger.debug("Program should multiply next two ops into 3rd op.")
                multiply_positions(program[pos+1], program[pos+2], program[pos+3])
            else:
                logger.critical("Invalid Opcode ({opcode}!")
            pos += 4
            opcode = program[pos]
        except Exception:
            logger.exception("Exeption occured")
            break
    logger.debug(f"Program is {program}")
    return program


def pre_process(program):
    program[1] = 12
    program[2] = 2
    return program


def run_tests():
    for program in TEST_PROGRAMS:
        result = process_program(program['input'])
        logger.debug(f"{result} : {program['output']}")
        if program['output'] == result:
            logger.debug('Test passed.')
        else:
            logger.debug("Test failed.")


def main():
    result = process_program(pre_process(PROGRAM))
    logger.info(f"Program result[0] = {result[0]}.")


if __name__ == "__main__":
    day_5()

