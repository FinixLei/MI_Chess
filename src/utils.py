from constants import LINES, ROUTING_MAP, EMPTY, STONE_SHOW_MAP
from Move import Move


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


def show_board(board):
    for pos in range(9):
        stone = STONE_SHOW_MAP.get(board[pos])
        print(stone, end=" ")
        if (pos + 1) % 3 == 0:
            print("")
