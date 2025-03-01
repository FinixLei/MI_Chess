from constants import LINES, INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS
from constants import R1, R2, R3, B1, B2, B3, EMPTY
from utils import check_red_win, check_black_win, show_board, show_board_case, parse_user_move, gen_red_black_positions
from BoardCase import BoardCase
from Move import Move
from MoveGenerator import MoveGenerator
from Engine import Engine


def test_check_red_win():
    assert check_red_win([0, 1, 2]) == False
    for line in LINES:
        if line != [0, 1, 2]:
            assert check_red_win(line) == True


def test_check_black_win():
    assert check_black_win([6, 7, 8]) == False
    for line in LINES:
        if line != [6, 7, 8]:
            assert check_black_win(line) == True


def test_gen_red_moves():
    print("Test Gen Red Moves")
    init_board_case = BoardCase(INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS, True)
    move_generator = MoveGenerator(init_board_case)
    moves_and_new_board_cases = move_generator.gen_moves_and_board_cases()
    for (move, board_case) in moves_and_new_board_cases:
        print("Move: ", move)
        show_board_case(board_case)
    moves = [item[0] for item in moves_and_new_board_cases]
    expected_moves = [
        Move(R1, 0, 3),
        Move(R1, 0, 4),
        Move(R2, 1, 4),
        Move(R3, 2, 4),
        Move(R3, 2, 5)
    ]
    assert len(moves) == len(expected_moves)
    for i in range(len(moves)):
        assert moves[i] == expected_moves[i]

    new_board_cases = [item[1] for item in moves_and_new_board_cases]
    for board_case in new_board_cases:
        assert (not board_case.red_turn)

def test_gen_black_moves():
    print("Test Gen Black Moves")
    init_board_case = BoardCase(INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS, False)
    move_generator = MoveGenerator(init_board_case)
    moves_and_new_board_cases = move_generator.gen_moves_and_board_cases()
    for item in moves_and_new_board_cases:
        print("Move: ", item[0])
        show_board(item[1].board)
    moves = [item[0] for item in moves_and_new_board_cases]
    expected_moves = [
        Move(B1, 6, 3),
        Move(B1, 6, 4),
        Move(B2, 7, 4),
        Move(B3, 8, 4),
        Move(B3, 8, 5)
    ]
    assert len(moves) == len(expected_moves)
    for i in range(len(moves)):
        assert moves[i] == expected_moves[i]

    new_board_cases = [item[1] for item in moves_and_new_board_cases]
    for board_case in new_board_cases:
        assert board_case.red_turn


def test_show_board(board):
    show_board(board)


def test_parse_user_move():
    user_move = 'R1->4'
    expected_values = (True, R1, 3)
    returned_values = parse_user_move(user_move)
    assert expected_values == returned_values

    user_move = 'B3->6'
    expected_values = (True, B3, 5)
    returned_values = parse_user_move(user_move, part='B')
    assert expected_values == returned_values

    user_move = 'B2=>5'
    expected_values = (False, None, None)
    returned_values = parse_user_move(user_move, part='B')
    assert expected_values == returned_values


def test_min_max():
    init_board = [B1, R2, R3, EMPTY, R1, B3, EMPTY, B2, EMPTY]
    init_board = [B1, R2, R3, R1, EMPTY, B3, B2, EMPTY, EMPTY]
    init_board = [R2, EMPTY, R3, R1, B1, B3, B2, EMPTY, EMPTY]
    init_board = [EMPTY, B1, R3, R1, R2, B3, B2, EMPTY, EMPTY]
    init_board = [R1, B2, EMPTY, EMPTY, B1, R3, R2, EMPTY, B3]
    red_positions, black_positions = gen_red_black_positions(init_board)
    board_case = BoardCase(init_board, red_positions, black_positions, False)
    show_board_case(board_case)

    score, move_list = Engine.min_max(board_case, 10)
    move = move_list[-1]
    print(f"Score = {score}, Move = {move}")
    moves = ""
    for mv in move_list[::-1]:
        moves += str(mv) + ", "
    print(f"move list = {moves}")
    board_case.make_move(move.stone, move.end_pos)
    show_board_case(board_case)


def main():
    test_check_red_win()
    test_check_black_win()

    test_show_board(INIT_BOARD)

    test_gen_red_moves()
    test_gen_black_moves()

    test_parse_user_move()
    test_min_max()


if __name__ == "__main__":
    main()
