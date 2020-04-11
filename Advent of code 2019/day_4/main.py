import re
import logging
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from collections import deque

logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)

INPUT_RANGE = range(236491, 713787)
TEST_CASES = {
    111111: True,
    223450: False,
    123789: False,
    112233: True,
    123444: False,
    111122: True,
    699999: False
}

MAX_POSSIBILITIES = len(INPUT_RANGE)

re_has_double = re.compile(".*?(\d)\1.*?")


def has_dboule(password: int):
    return re_has_double.search(str(password))


def is_valid(password: int) -> bool:
    str_password = str(password)
    sequence_lengths = {}
    for index, digit in enumerate(str_password):
        try:
            next_digit = str_password[index + 1]
            if next_digit:
                if int(next_digit) < int(digit):
                    logger.debug(f"Next digit is smaller than current. Invalid password!")
                    return False
                next_matches_current = digit == next_digit
                if next_matches_current:
                    logger.debug("Next digit matches!")
                    if digit not in sequence_lengths:
                        sequence_lengths[digit] = 1
                    else:
                        sequence_lengths[digit] += 1
                else:
                    logger.debug("Next digit is not the same!")
        except IndexError:
            pass
    has_valid_sequence = next((True for sequence in sequence_lengths.values() if sequence == 1), False)
    return has_valid_sequence


def run_tests():
    for password, validity in TEST_CASES.items():
        result = is_valid(password)
        logger.info(f"{password=} {result=}: {validity=}")


def search_inputs(inputs) -> int:
    MAX_POSSIBILITIES = len(inputs)
    valid = deque()
    invalid = deque()

    def validate(password, valid, invalid):
        if not is_valid(password):
            # logger.warning(f"{password} is invalid!")
            invalid.append(password)
        else:
            # logger.info(f"{password} is valid!")
            valid.append(password)

    for password in inputs:
        if not is_valid(password):
            # logger.warning(f"{password} is invalid!")
            MAX_POSSIBILITIES -= 1
        else:
            logger.info(f"{password} is valid!")
    # with ThreadPoolExecutor() as executor:
    #     futures = {executor.submit(validate, password, valid, invalid): password for password in INPUT_RANGE}
    #     for future in as_completed(futures):
    #         logger.debug("Finished.")
    return MAX_POSSIBILITIES


if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    run_tests()
    possible_passwords = search_inputs(INPUT_RANGE)
    print(possible_passwords)
