from constants import LINES, INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS
from constants import R1, R2, R3, B1, B2, B3
from utils import check_red_win, check_black_win, show_board
from BoardCase import BoardCase
from Move import Move
from MoveGenerator import MoveGenerator


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
    init_boardcase = BoardCase(INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS, True)
    move_generator = MoveGenerator(init_boardcase)
    moves_and_new_boardcases = move_generator.gen_red_moves_and_boardcases()
    for item in moves_and_new_boardcases:
        print("Move: ", item[0])
        show_board(item[1].board)
    moves = [item[0] for item in moves_and_new_boardcases]
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


def test_gen_black_moves():
    print("Test Gen Black Moves")
    init_boardcase = BoardCase(INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS, False)
    move_generator = MoveGenerator(init_boardcase)
    moves_and_new_boardcases = move_generator.gen_black_moves_and_boardcases()
    for item in moves_and_new_boardcases:
        print("Move: ", item[0])
        show_board(item[1].board)
    moves = [item[0] for item in moves_and_new_boardcases]
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


def test_show_board(board):
    show_board(board)


def main():
    test_check_red_win()
    test_check_black_win()

    test_show_board(INIT_BOARD)

    test_gen_red_moves()
    test_gen_black_moves()


if __name__ == "__main__":
    main()
