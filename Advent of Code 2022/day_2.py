import sys
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))

part_1_test = """
A Y
B X
C Z
"""

meaning = {
    "A": 'rock',
    "X": 'rock',
    "rock": 'rock',
    "B": 'paper',
    "Y": 'paper',
    "paper": 'paper',
    "C": 'scissors',
    "Z": 'scissors',
    "scissors": 'scissors',
}

ranking = {
    "A": "Z",
    "B": "X",
    "C": "Y",
    "X": "C",
    "Y": "A",
    "Z": "B",
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

match_ending = {
    "X": 'lose',
    "Y": "tie",
    "Z": "win"
}

scoring = {
    "A": 1,
    "X": 1,
    "rock": 1,
    "B": 2,
    "Y": 2,
    "paper": 2,
    "C": 3,
    "Z": 3,
    "scissors": 3,
}

match_scoring = {
    "lose": 0,
    "tie": 3,
    "win": 6,
}

game_moves = [
    {
        "move": "rock",
        "lose": "scissors",
        "tie": "rock",
        "win": "paper",
        "points": 1
    },
    {
        "move": "paper",
        "lose": "rock",
        "tie": "paper",
        "win": "scissors",
        "points": 2
    },
    {
        "move": "scissors",
        "lose": "paper",
        "tie": "scissors",
        "win": "rock"
        ,
        "points": 3
    },
]


def parse_input(puzzle):
    return [l for l in puzzle.splitlines() if l]

# def i_won(opponent, me):
#     if me == opponent:
#         return False
#     if opponent.get()

def match_score(opponent, me):
    if meaning.get(opponent) == meaning.get(me):
        return match_scoring.get('tie')
    if ranking.get(me) == meaning.get(opponent):
        return match_scoring.get('win')
    return match_scoring.get('lose')

def decide_move(opponent, outcome):
    key = match_ending.get(outcome)
    omove = next(m for m in game_moves if meaning.get(opponent) == m.get("move"))
    decision = omove.get(key)
    return decision

def calc_game_score(game_str):
    game = parse_input(game_str)
    totals = []
    for match in game:
        opponent, result = match.split(" ")
        # op_score = scoring.get(opponent)
        me = decide_move(opponent, result)
        my_score = scoring.get(me)
        round_score = match_score(opponent, me)
        total = my_score + round_score
        totals.append(total)
    game_score = sum(totals)
    logger.info(f"{game_score=}")
        
PUZZLE_INPUT = """
B Y
C Z
C Y
C Y
A X
C Y
C Y
C Y
A X
B X
B Y
B Y
B Z
C Z
C Z
C Z
B Y
A Z
C Y
C X
B Z
C Y
C Z
B Y
B Y
A X
B Y
A X
C Y
B Y
B X
A Y
C X
A Y
B Y
B Y
A Y
B Y
A Z
B Y
B X
C Z
B X
B Y
A Z
B X
C Y
C X
C Y
C Y
B Y
C Z
C Z
B Y
B Y
B Y
C X
B Y
B Z
B Y
B X
C X
B X
A Y
C Z
C X
B Y
B Y
C Z
B X
C X
C Y
C Y
C Y
B X
C Z
C Z
B Z
B Y
C Y
C Y
B Z
A Y
B Y
A X
B Y
A X
A X
B Y
B Z
A X
C Y
C Z
C Y
C Z
B X
C Y
A X
B Y
C Y
C Z
A Z
A Z
C Z
A Y
C Y
B Y
B Z
C X
A Z
A Y
C Z
B X
C Y
C Y
B Z
C X
B Y
C Y
A X
C X
B Y
C Y
B Y
C X
B Z
C Y
C Z
B Y
B Y
B Y
B Y
B Z
C Y
B Z
A Y
C Z
C Z
C Z
B Y
B X
C Z
C Z
C Z
C Z
C Z
B Y
C Y
A Z
B Y
C Y
A Y
B Y
C X
A X
A Y
C Z
C Y
B X
C Z
B Y
C Y
C Y
C X
B Z
B Z
C Z
A X
B Z
C Y
C X
C Z
A X
A X
C X
B Y
C Y
B Y
B Y
B X
C X
B Y
B Y
C Y
A Y
C Y
B Y
C Y
A Y
B Z
C Y
B Y
C Y
B Z
A X
C Z
C Y
B Y
C Y
C Y
A X
B Y
C Y
A Z
C X
A X
B Y
A X
A X
C Z
B Y
C Z
C Z
C Z
C Z
B Y
C Y
A Z
A X
B Y
C Z
B Z
C X
C X
B Y
C Y
B Y
B Z
B Z
C X
B Y
C X
C X
A Z
B Y
B X
A Z
A Y
A X
A Y
C Y
A X
A Y
C Y
C Z
B Y
A Y
C Y
B X
A Y
B Y
A Y
B Y
C Y
A Y
B Y
C Y
C Y
C Y
B Y
C Z
C Z
A Z
B Y
C X
B Z
C Y
A X
B X
B Z
A Y
C Z
A X
A Z
C Y
B Y
B Y
B X
B Y
B Y
B Z
A Y
B Y
A X
C Y
C Z
C Z
B Y
C Y
B Y
C X
C Y
A Y
B Y
C Z
B Y
C Y
C Y
B X
A Z
A Y
A Y
C Y
C Y
B Y
B Z
B Y
A Z
B Y
A X
C Y
A X
C Z
C Z
C Y
C Y
A Y
C Z
C Z
C Y
B Y
C Z
B Z
A X
C Z
A Y
B Y
A X
A X
A X
B Z
B Y
A Y
A X
B X
C Z
B Y
C X
C Z
A Z
C Y
A Z
A Y
A Z
C Y
A Z
C Y
B Y
B Y
A X
A Y
B Y
B X
A Y
C Z
B Y
C Y
C Z
B Y
C Y
A X
A X
B Y
B Y
C Z
A X
B Z
A X
C Y
B X
C Z
B Y
C Y
A Z
C Z
C Y
C Z
C Y
B X
B X
C Z
A Z
C X
C X
A X
B Z
A X
B X
A Y
B Y
C Y
C Z
C Y
C Z
C Z
B Y
C Y
B Z
C Z
C Z
C Y
B Y
C Y
A Y
B Y
C Z
B Y
A X
C Y
C X
C Z
B Y
B X
B Y
C Y
B Z
A Z
C Z
C Y
C Z
C Y
A X
B Y
A X
B Y
B Y
A X
C Y
B X
A X
C Z
C Z
A X
A Y
A Y
C X
B Y
A X
B Y
A Z
A X
C Y
A X
C Y
C Z
C Y
B Z
A X
B Z
B Z
A Z
C X
C Y
B Y
C X
C Y
C X
C X
B X
C X
C Z
A X
A Y
A X
B X
B Y
B Y
C Z
B Z
B Z
B Y
C Z
C Y
C Z
B X
C Y
C Y
C Z
B X
C Y
C Z
B Y
B Z
C X
B Z
C Y
A X
A X
A Z
B Y
C X
C Y
B X
A X
A Y
C Z
A Y
C Y
C Z
C X
C Z
C Z
A X
B Y
A X
A Z
B X
C X
B X
B Y
C Y
C Y
C Z
C Y
C Y
C X
C Z
C Y
B Z
C Y
B Y
A Y
B Y
C Y
A X
C Y
B Z
B Y
C X
C X
C Z
C Y
B Y
C Y
B Y
B Y
C X
C X
C Y
B Y
B Y
B X
C X
A Z
B X
C Y
B X
C Y
C Y
B X
B X
C Y
A X
B Y
A Y
B Y
B Y
B Y
A X
C Z
A Y
C X
A Y
C Y
A X
C Y
C Z
B Y
B Y
A Y
C Y
B Y
C Y
C Y
A Z
B Y
A X
C Z
C Y
A X
A X
C X
B Y
A X
A Z
C Y
C Z
B Y
A X
C Z
C Z
B Y
B X
C Y
B Y
B Y
C Z
B X
B Z
C Y
C Y
B X
C Z
C X
A Y
B X
C Y
B Y
C Z
C Y
B Y
C Z
C X
A Y
B Y
C Z
C Y
A Y
C Y
B Y
B Y
C Y
B Z
C Y
C Y
B Z
C Y
B Y
A X
C Z
C Y
C Z
C Y
A X
A Z
C Y
A Y
C X
B X
A X
C Y
C Z
A X
C Y
C Y
A Z
C X
B Z
C X
C Y
B Z
A X
A X
B Z
A X
A Y
B X
C Y
A Y
C Y
A Z
C Y
B X
B Y
A Y
C Y
C Y
C Y
C Z
B X
C Z
C Y
B Y
B Y
C Z
B Z
B Y
A X
C Y
C X
A Y
B Z
C X
A Z
B Z
C Z
C Z
C Y
C Y
B Y
B Y
B X
A Z
C Y
A Y
C Z
A Y
A X
C Z
C Y
A X
B Y
C Z
C Y
C Z
C Y
C X
B Z
B Y
B Y
A Z
B Z
B Y
C Z
B Y
B X
C Z
B Y
C Z
C Y
C Y
A X
B Y
B Z
A X
C X
A Y
B X
B Y
A Y
A X
A Z
A X
C Y
B Z
A Z
C Z
C X
A X
C X
A X
B Z
C Y
B Z
C Z
C Z
A X
A Z
C X
B Y
C Z
A X
C Y
A Y
B Y
C Y
B X
A X
B X
C Y
A Z
B X
B Y
C X
B Y
A Y
B Y
A Z
C Z
C Z
C Z
C Y
B Y
B Y
C Z
C Y
A Y
A Y
C Z
A Z
C Y
C Z
C Y
C Z
A X
C X
C Z
B Y
C Z
C Y
B Y
B Y
A Z
A Z
C Y
C Z
C Z
C Z
C X
B Z
C Y
A Z
C Y
B X
B Y
C Y
B Y
C Z
C Z
B Y
C Y
A Z
B Y
B Y
B Y
B Y
C Y
B Y
A X
C Y
A Y
C Y
C Z
A Y
A Z
C Y
C Y
C Y
C Z
B Y
A Y
B Y
C X
B Y
B Y
B Y
C Y
B X
C Z
A X
B Y
C Z
C Z
B Z
B Y
C Y
B Y
B Y
C X
B X
A Y
A Z
C Z
A Z
C Z
C Z
C Z
A Z
C Y
C X
A X
C X
A Z
C Y
C Z
C Z
B Y
C Y
A X
C X
C Y
C Z
A X
A Z
C X
A X
B Y
A X
C X
A X
C Y
B Y
C Z
B X
A Z
C Z
B Z
C Z
C Y
B Y
C Z
C Y
A Y
B X
B X
A Z
B Y
A X
C Y
C Y
B Y
A X
B Y
B Y
C Z
A Y
C Z
C Z
B Y
C Z
C Z
C Y
C Y
C X
C Y
A Z
C Y
A Z
C Z
B X
A X
C Z
C Z
B Y
C Y
C Y
A X
C Y
A X
C Y
C Z
B Y
B Z
A X
B Y
A Y
B X
C X
A Y
A X
C Y
C Z
A X
C Y
A Y
C Y
B Y
C X
C Z
C Y
A X
B Y
B Y
A X
C Y
B Y
C Y
A Y
B Y
B Z
B X
B Y
C Y
B Y
A Y
C Z
C Y
C Z
C Y
B Z
C X
C Z
C Y
C X
A X
C Y
C X
B Y
C Y
C Z
C Y
B Y
B Y
C Y
C Z
B Z
C Y
C Z
B Y
C Z
C X
C Y
C Y
C Z
A X
A Y
C X
C Y
C X
C Y
A X
C Y
A X
B Y
B Y
A X
B X
A Y
B Y
C Z
C Y
C Y
B Y
A Z
C Z
A Z
B Y
B Y
C Y
C Z
B Y
C Z
B Z
C Z
C Y
A X
C Z
B Y
A Z
C Y
C Z
A Y
C Y
B Y
C Z
B Z
B Y
B Z
B Y
C Y
C Y
C Z
B Y
A X
B Y
B Y
C Y
B Z
B Y
C Y
C X
C Z
C Z
B Y
C Y
C Z
B Z
C Z
C Z
B Y
C X
C X
B Y
C Z
B Y
B Y
C X
A Z
B Z
B X
B X
C Z
C Z
B Z
A Y
C Y
B Y
C X
C Z
A Z
B Z
C Y
B Y
B Z
C Z
A X
C Z
B Y
A Y
B Y
B Z
A X
C Y
A Z
C Z
C Y
B Y
A Y
B Y
B Y
C Y
A X
B Y
C Z
C Z
C Y
B Z
B Y
B Z
B X
C Y
A X
B Y
C Z
C Y
C Z
C Z
C X
C Y
C Z
B Y
A X
C Y
C Y
C Y
A Y
A Y
A Y
C X
B Y
B Y
A Y
C Z
C Z
B Z
C Y
B Y
A X
C X
B Y
C Y
B Y
B Z
C Z
A Y
B Z
C X
B Y
C Z
C Z
C Y
B Y
B Z
B Y
B X
B X
C Z
A Y
B Y
C Z
C Y
A Z
A Z
C Z
C Y
B Y
A Y
B Y
B Y
A X
C Y
A X
C Z
B Y
B Y
B Y
A Y
C Y
C Z
B Y
C Y
C Y
B Y
A X
C Y
C Y
B Y
B Y
C Z
A X
C Y
C Y
C Y
B Y
C Y
A Z
B Y
C Y
A Z
A Z
C Z
C Z
B Y
A Y
B Z
C Z
B Y
B Z
A Y
C X
A X
C Y
B X
B Y
A Y
B Y
C Z
A Z
B Y
C Z
B Y
C Z
C Z
A X
C Y
A Z
B Y
B Y
B Y
B Z
A Y
C Z
A Y
B Y
B Y
B Y
B X
A Y
C Y
A X
C Y
A X
A X
B Y
B Z
B Y
B Y
C Y
C Y
B Y
C Z
A X
A Z
A Y
C Y
C X
B Z
A X
A Y
C Y
C Z
B Y
C X
B Y
B X
B Y
A Y
A Z
B Z
A X
A Z
B Y
B Z
C Y
C Y
C Y
A Y
B Y
B Y
B Y
A Z
B Y
C Y
B Y
A Y
A X
B Y
C Y
A Y
C Y
C Y
A Z
C X
C Y
C Y
B X
A Y
B Z
A Z
B Y
C Z
C Z
C Z
B Y
A Y
B Z
C Y
A X
B Y
A Y
B Y
B Y
C Y
B X
C X
C Y
C Z
B Y
C Z
A Y
A X
C Y
B Y
C X
A X
C Z
C Y
C Z
C Y
A X
C Y
C X
C Z
B Y
B Y
A Z
A Y
B Z
C Z
C Z
C Z
C Y
A Z
B Y
A X
C Y
A X
B Z
B Y
B Y
B Y
A X
B Y
C X
A X
A X
B X
B Y
C Y
A X
B Y
B X
B Z
B Y
B Y
C Y
B Y
C Z
A Z
C Y
C Y
A X
A X
C Y
B Y
C Z
C Y
B Y
B Z
B Z
A X
C Y
C Y
B Y
A Y
C Z
A Z
C X
B Y
B Y
C Z
A Z
B Y
B Y
C Y
C Z
A X
B Y
B Y
C Y
B Y
C Y
C Y
C Y
A X
C Y
B Y
B Y
A X
A Y
B Y
B Y
C Z
C X
C Z
A X
A X
C Y
C X
B Z
B X
C Z
C Z
B Y
B Y
C Y
C Y
C Z
C Y
A X
B Z
B Y
C Z
C X
C Y
B Y
B Y
B Y
C Z
B Y
A X
C Z
B X
B Z
A Y
A Z
B Y
B X
A X
B Y
B Y
A Z
A X
C X
A Z
A X
A Z
C Z
A X
C Y
B Y
B Y
C Y
B Z
B X
C Y
B Y
A Z
C X
C Y
B Y
A Z
C Y
C Y
A X
C X
C Y
C X
A Y
B Z
A Z
C Z
B Y
C Z
C Y
A Z
B Y
A Z
C Y
A X
A Z
B Y
B Y
B Z
B Y
A X
C Y
B Y
C Y
B Y
A X
C Z
B Y
C Y
A X
C Y
B Y
B X
C X
A X
B Y
C Y
B Y
B Y
C Z
B X
C Z
A X
C Z
A X
A Z
C Y
C Y
B Y
B Y
A Z
A X
C Z
B Y
B Y
A Y
C Y
C Z
C X
C Y
A Y
B Z
C Z
A Z
C Y
C X
C X
B Z
A X
C Y
A X
C Z
B Y
C Y
A Z
A X
B Y
B Y
B X
C Z
C X
B Y
C X
A Y
A Y
C Z
C Z
C Z
B Z
C Z
A Y
C Z
A X
A Y
C Z
B Y
C Y
C X
C Z
B Y
A X
B X
B Y
B X
C Y
A X
B Y
C Y
C Y
B Y
B Y
A X
A Y
C X
C Y
B Y
C Z
A X
C Z
B Z
C Z
C Y
C X
C Y
A X
B Y
C X
A X
C Y
C X
C Y
A Z
C Y
B Y
C X
C Z
C Y
B Y
C Y
A Y
A X
C Y
C Y
C Z
A X
B Y
C Y
B Z
C Y
B Y
A X
B Z
C Z
C Z
C Y
C X
B Z
C Z
C Z
B Y
B X
A Z
A X
C Y
A X
B X
A X
A Z
C Z
C Y
C Z
C Z
B Z
C Z
B Y
C Y
B Y
A Z
C Y
B Y
C Z
A Y
B Z
B X
B Y
B Y
C Y
C Y
B Y
B X
B X
A X
C Z
B Y
C Z
C Y
B Y
A X
C X
C Z
B Z
C Y
C Y
B Y
B Y
C Z
A X
B Y
C Z
C Y
C Z
C Y
B Y
C Y
C X
C X
A X
A X
B Z
B Y
B Y
C Z
A X
B Y
A Y
B Y
A Z
C Z
C Y
A Y
A X
B Y
B Y
C X
A X
C Z
C Y
A Z
B Y
C Z
C X
B Z
C Z
B Y
A Y
B Y
B Y
A X
B Z
B Y
C Z
C Y
B X
A Z
C Z
B Y
C Y
A Z
B Y
A Y
B Y
B Z
A Z
B Y
C Y
C Y
C Y
A X
B Y
C X
C Y
A X
B Z
A Y
C Z
B Y
B Z
B Y
C Y
B Z
B Y
B Z
C Y
B Z
B Y
B Z
C Y
A Y
C Z
C Y
C Y
B Y
A Y
A Z
A X
C Z
B Z
C X
B Y
B Y
C Z
A X
C Z
C Y
B Z
A Z
B Y
C Y
C Y
A X
B Y
C X
A X
B Y
A Y
A X
B Z
C Z
C X
A Z
C Y
A Y
C Y
A X
C Z
B Y
A X
B Y
B Y
A Z
C Z
A X
A X
A X
A X
C Y
B Y
C Y
C X
C Y
A Y
C Z
A X
B X
B Y
C Z
B Y
B Z
A X
C Y
B Y
C Y
B Y
C Z
C Y
C X
A Y
A Y
C Y
A Z
B Y
A Y
B Z
B Y
C Y
A Y
B Y
C X
C Y
C Z
C Z
A X
C Z
B Y
B X
B X
A Y
C Z
A Y
C X
A X
C Z
C Y
C X
C X
C Z
A Z
C Z
B Y
B Z
C Z
C Y
A X
A X
C X
B X
C Y
B Y
B Z
C Z
C Z
B Y
B Y
B Z
A X
B Y
A X
B Y
C Y
B X
C Z
C Z
C Y
A Y
B Y
B Y
B Y
C Z
A Z
A Z
A Y
A Y
B Y
C Z
C Z
A Z
A Z
B Y
A Z
A Y
C Y
B Y
B Y
A X
C Z
C Z
B Y
A X
B Y
A Z
B Y
A X
A X
C Z
C Y
B Y
C Y
B X
B Y
A Y
B Y
B X
C Y
B Y
C Y
C Y
B Y
C X
C Y
A X
B Y
C Y
A Y
B Y
A X
C Z
B Y
C Y
B Y
C X
A Y
C Z
B Y
B Y
B Z
B Z
C Z
C Z
C Z
A Y
B Y
A Z
A X
C Z
B Y
A X
B Y
B X
C Z
B Y
C Y
B X
C X
C X
A Z
C X
A Z
C Z
B X
C Y
A X
C Y
B Y
C Y
B Y
C Z
C Z
C Z
C Z
C Z
C Y
A X
B X
B X
B Z
A X
C Y
A X
C Z
C Z
C Y
A X
C Z
A X
A X
A X
C Z
C X
B Y
C Y
B Z
C Y
B Y
A X
A Y
C Z
B Y
B Y
B X
C Z
C Z
A Y
A X
C Y
A X
C Y
C Y
B Z
B Y
B X
C Y
A Y
A X
B Y
B Y
C Y
A Y
B Y
B Y
B X
A Z
C Y
C Y
B Z
C Y
B Z
B Y
C Y
A Y
B Y
A X
C Y
C Z
C Y
A X
C Z
B Y
B Z
A X
C Y
C Y
C Y
C Z
B Y
B Y
A X
C Y
B Y
A Y
C Z
C X
C Y
A X
C Y
C Z
A X
C Y
A Z
B Y
B X
B Y
B Z
B Y
B Y
B Y
C X
A X
B Y
A X
A Y
C Z
C Y
C Z
C Y
B Y
B X
B X
C X
B Y
A X
A X
C Y
C X
B X
C X
C Z
C Z
B Z
C Z
C X
B Y
B X
B Y
C Y
A Y
A Y
C Z
B X
B Y
B Z
A X
C Y
A Y
C Y
C Z
C X
B Z
A X
A X
A Y
A Y
A Z
B Y
C X
C Z
C Z
B Y
B Z
C Y
B Y
C Y
B Y
B Y
B Y
C Y
C Y
C Y
A X
B X
C Z
C Y
A X
B Y
A Y
C Y
A X
B Y
B X
B Y
C X
C Z
A X
C Y
B Y
A Y
C Z
C Y
B Z
C Z
B Y
A X
B Y
C Z
A Y
B Y
A Y
B Y
B X
C X
C Y
A Y
B Z
A X
A Z
B Y
A X
C Y
B Y
A Y
A X
B X
B X
B Y
A Z
C Z
C Y
C X
C X
C Z
C Y
B X
A Y
C Y
B Y
B Y
A X
B Y
B Y
A Z
A Y
B X
A Z
B Z
B Y
A X
A X
C Y
A Y
C Y
C Z
A Y
C Y
C X
C X
C Y
B X
A X
A Y
B X
A Y
C X
B Y
B Z
B Y
A Y
C Y
B X
A Z
A X
B Y
C X
C Y
C Y
B Y
A Y
C Y
C Y
B Y
C Y
B Z
B Y
B Y
A Y
B Y
C Z
B Y
B Y
B X
B Y
B Z
C X
B X
C Z
B Z
C Z
A X
C X
A X
B Y
B X
B Y
C Y
C X
B Y
A X
B Y
B Y
C Y
A X
C Y
C X
B Z
A Z
C Y
B Z
A X
B Y
A X
B Y
A Y
C Y
C Y
C Y
C X
C Z
A X
B Y
C Y
B Z
C Z
C Z
C Z
C Y
C Y
C Y
A X
B Y
B Y
B Y
B Y
B Y
C Z
A Z
C X
A X
C Z
A X
C Y
C Y
C Z
C Y
C Y
C Y
C Y
C Z
A Y
B Y
B Z
C Z
A X
A Y
C Z
C Z
A Y
C X
A Z
B Y
B Y
A Y
C Z
A X
C Y
A X
C X
B Y
B Y
B Y
A Z
B Z
C Y
A X
B Y
B Z
B Y
B Y
C Z
A Y
B Y
C Z
A X
C Y
C X
C Y
B X
C Z
C Z
B Y
A Z
A Y
C Z
B X
B Y
B Y
A Y
C X
C Y
B Y
A Y
A X
B Y
C X
B Y
B X
C Z
C Z
C Y
C Z
C Z
C X
A X
A Y
C Y
B Y
B Y
C Y
A Y
C Z
A Y
A X
B X
C X
C Z
C Z
B X
C Y
A Z
C Z
C Z
C Y
A X
C Z
B Y
A Y
A X
C Y
C Y
C Y
B Y
A Z
C Y
C Y
C Y
B Y
B X
C Y
A Z
B Y
B Y
C Y
C Z
C Y
A X
A X
C Y
C Y
B Z
A Y
B Y
A X
A X
C Y
B Y
B Z
C Z
C Y
C Y
C X
B Z
A Z
B X
B Y
B Y
A Y
A X
C Z
C X
C Z
A Z
B Y
A Z
A X
A X
B Z
B Y
A Z
A X
A Z
B Y
B Y
C Z
C Y
A Y
A Y
B Y
A Y
C Z
C Y
C Z
C Y
C Z
C Z
C X
C X
C X
B Y
C X
C Z
B Y
B Y
C Y
B Y
C Y
B X
B Y
B Z
C Z
B Y
C Y
B Y
C Y
A X
B Y
B Y
C Z
B Y
"""

def main():
    # calc_game_score(part_1_test)
    calc_game_score(PUZZLE_INPUT)

if __name__ == "__main__":
    main()