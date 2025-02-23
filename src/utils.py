from constants import LINES, STONE_SHOW_MAP, STONE_TO_NUM, EMPTY


def check_red_win(red_position_list):
    red_position_list = sorted(red_position_list)
    for line in LINES:
        if red_position_list == line and line != [0, 1, 2]:
            return True
    return False


def check_black_win(black_position_list):
    black_position_list = sorted(black_position_list)
    for line in LINES:
        if black_position_list == line and line != [6, 7, 8]:
            return True
    return False


def simple_show_board(board):
    for pos in range(9):
        stone = STONE_SHOW_MAP.get(board[pos])
        print(stone, end=" ")
        if (pos + 1) % 3 == 0:
            print("")
    print("-" * 30)

###################################
# @param board: a list of stones
###################################
def show_board(board):
    show_stone_list = []
    ONE_SPACE = " "
    ONE_DASH = "-"
    for i in range(9):
        stone = board[i]
        if stone == EMPTY:
            if i in [0, 3, 6]:
                stone = str(i+1) + ONE_SPACE + ONE_DASH
            elif i in [1, 4, 7]:
                stone = ONE_SPACE + str(i+1) + ONE_DASH
            else:  # i in [2, 5, 8]
                stone = ONE_SPACE*2 + str(i+1)
        else:
            stone = STONE_SHOW_MAP[board[i]]
            if i in [0, 3, 6]:
                stone = stone + ONE_DASH
            elif i in [1, 4, 7]:
                stone = stone + ONE_DASH
            else:  # i in [2, 5, 8]:
                stone = ONE_SPACE + stone
        show_stone_list.append(stone)

    line_list = [
        f"{show_stone_list[0]}{show_stone_list[1]}{show_stone_list[2]}",
        f"| \\ | / |",
        f"{show_stone_list[3]}{show_stone_list[4]}{show_stone_list[5]}",
        f"| / | \\ |",
        f"{show_stone_list[6]}{show_stone_list[7]}{show_stone_list[8]}",
    ]
    for line in line_list:
        print(line)
    print("-" * 30)

###########################################
# Example of user move: "R1->4", "B2->6"
###########################################
def parse_user_move(user_move, part='R'):
    try:
        if len(user_move) != 5:
            return False, None, None
        if user_move[0].upper() != part.upper():
            print("You may not belong to this part")
            return False, None, None
        if user_move[2:4] != '->':
            return False, None, None
        if user_move[1] not in ['1', '2', '3']:
            return False, None, None
        end_pos = int(user_move[4]) - 1
        if end_pos not in range(9):
            return False, None, None
        stone = STONE_TO_NUM[user_move[:2].upper()]
        return True, stone, end_pos
    except Exception as ex:
        print(f"Exception happened when parsing user move {user_move}: {str(ex)}")
        return False, None, None
