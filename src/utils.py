from constants import LINES, ROUTING_MAP, EMPTY, STONE_SHOW_MAP
from structure import Move

def check_red_win(red_positions):
    red_positions = sorted(red_positions)
    for line in LINES:
        if red_positions == line and line != [0, 1, 2]:
            return True
    return False

def check_black_win(black_positions):
    black_positions = sorted(black_positions)
    for line in LINES:
        if black_positions == line and line != [6, 7, 8]:
            return True
    return False


"""
    @param board: the board presented as a list like INIT_BOARD
    @param red_positions: a map with key as red stones and value as position in board
"""
def gen_red_moves(board, red_positions):
    moves = []
    for red_stone in red_positions:
        position = red_positions[red_stone]
        available_positions = ROUTING_MAP[position]
        for pos in available_positions:
            if board[pos] == EMPTY:
                moves.append(Move(red_stone, position, pos))
    return moves

"""
    @param board: the board presented as a list like INIT_BOARD
    @param black_positions: a map with key as black stones and value as position in board
"""
def gen_black_moves(board, black_positions):
    moves = []
    for black_stone in black_positions:
        position = black_positions[black_stone]
        available_positions = ROUTING_MAP[position]
        for pos in available_positions:
            if board[pos] == EMPTY:
                moves.append(Move(black_stone, position, pos))
    return moves

def show_board(board):
    for pos in range(9):
        stone = STONE_SHOW_MAP.get(board[pos])
        print(stone, end=" ")
        if (pos + 1) % 3 == 0:
            print("")
