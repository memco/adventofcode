TEST_PROGRAMS = [
  {
    'input': [1,0,0,0,99],
    'output': [2,0,0,0,99]
  },
  {
    'input': [2,3,0,3,99],
    'output': [2,3,0,6,99]
  },
  {
    'input': [2,4,4,5,99,0],
    'output': [2,4,4,5,99,9801]
  },
  {
    'input': [1,1,1,4,99,5,6,0,99],
    'output': [30,1,1,4,2,5,6,0,99]
  },
  {
      'input': [1002, 4, 3, 4, 33],
      'output': [1002, 4, 3, 4, 99]
  },
  {
      'input': [1101, 100, -1, 4, 0],
      'output': [1101, 100, -1, 4, 99]
  },
]

DAY_5_PART2_TESTS = [
    # {
    #     'input': [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],
    #     'mode': 0
    # },
    # {
    #     'input': [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],
    #     'mode': 0
    # },
    # {
    #     'input': [3, 3, 1108, -1, 8, 3, 4, 3, 99],
    #     'mode': 1
    # },
    # {
    #     'input': [3, 3, 1107, -1, 8, 3, 4, 3, 99],
    #     'mode': 1
    # },
    # {
    #     'input': [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
    #     'mode': 0
    # },
    # {
    #     'input': [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
    #     'mode': 1
    # },
    {
        'input': [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                  1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                  999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99],
        'mode': 0
    }
]
