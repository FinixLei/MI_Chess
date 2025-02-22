from constants import LINES, INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS
from constants import R1, R2, R3, B1, B2, B3
from utils import check_red_win, check_black_win, gen_red_moves, gen_black_moves, show_board
from Move import Move


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
    moves = gen_red_moves(INIT_BOARD, RED_INIT_POSITIONS)
    for move in moves:
        print(move)
    expected_moves = [
        Move(R1, 0, 3),
        Move(R1, 0, 4),
        Move(R2, 1, 4),
        Move(R3, 2, 4),
        Move(R3, 2, 5)
    ]
    assert len(moves) == len(expected_moves)
    i = 0
    while i < len(moves):
        assert moves[i] == expected_moves[i]
        i += 1


def test_gen_black_moves():
    moves = gen_black_moves(INIT_BOARD, BLACK_INIT_POSITIONS)
    for move in moves:
        print(move)
    expected_moves = [
        Move(B1, 6, 3),
        Move(B1, 6, 4),
        Move(B2, 7, 4),
        Move(B3, 8, 4),
        Move(B3, 8, 5)
    ]
    assert len(moves) == len(expected_moves)
    i = 0
    while i < len(moves):
        assert moves[i] == expected_moves[i]
        i += 1


def test_show_board(board):
    show_board(board)


def main():
    test_check_red_win()
    test_check_black_win()

    test_gen_red_moves()
    test_gen_black_moves()

    test_show_board(INIT_BOARD)


if __name__ == "__main__":
    main()
