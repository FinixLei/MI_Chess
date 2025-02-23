from constants import LINES, STONE_SHOW_MAP, STONE_TO_NUM
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


###########################################
# Example of user move: "R1->4", "B2->6"
###########################################
def parse_user_move(user_move, part='R'):
    try:
        if len(user_move) != 5:
            return False
        if user_move[0].upper() != part.upper():
            return False
        if user_move[2:4] != '->':
            return False
        if user_move[1] not in ['1', '2', '3']:
            return False
        end_pos = int(user_move[4]) - 1
        if end_pos not in range(9):
            return False
        stone = STONE_TO_NUM[user_move[:2].upper()]
        return True, stone, end_pos
    except Exception as ex:
        print(f"Exception happened when parsing user move {user_move}: {str(ex)}")
        return False
