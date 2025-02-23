ROUTING_MAP = {
    0: [1, 3, 4],
    1: [0, 2, 4],
    2: [1, 4, 5],
    3: [0, 4, 6],
    4: [0, 1, 2, 3, 5, 6, 7, 8],
    5: [2, 4, 8],
    6: [3, 4, 7],
    7: [4, 6, 8],
    8: [4, 5, 7]
}

LINES = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

R1 = 0x11
R2 = 0x12
R3 = 0x13
B1 = 0x21
B2 = 0x22
B3 = 0x23
EMPTY = 0x00

STONE_TO_NUM = {
    'R1': R1,
    'R2': R2,
    'R3': R3,
    'B1': B1,
    'B2': B2,
    'B3': B3
}

STONE_SHOW_MAP = {
    R1: 'R1',
    R2: 'R2',
    R3: 'R3',
    B1: 'B1',
    B2: 'B2',
    B3: 'B3',
    EMPTY: 'E '
}

RED_STONES   = [R1, R2, R3]
BLACK_STONES = [B1, B2, B3]

RED_INIT_POSITIONS = {
    R1: 0,
    R2: 1,
    R3: 2
}

BLACK_INIT_POSITIONS = {
    B1: 6,
    B2: 7,
    B3: 8
}

INIT_BOARD = [R1, R2, R3, EMPTY, EMPTY, EMPTY, B1, B2, B3]
