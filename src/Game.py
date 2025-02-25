from constants import STONE_SHOW_MAP
from utils import show_board, parse_user_move, check_red_win, check_black_win
from BoardCase import BoardCase
from MoveValidator import MoveValidator
from Engine import Engine


def user_play():
    def _check_win(board_case: BoardCase):
        if check_red_win(board_case.red_positions.values()):
            print("Red Win!")
            exit(0)
        if check_black_win(board_case.black_positions.values()):
            print("Black Win!")
            exit(0)

    is_user_red = True
    while True:
        print("Please choose RED or BLACK (R or B): ")
        user_choice = input().upper()
        if user_choice == 'R':
            is_user_red = True
            break
        elif user_choice == 'B':
            is_user_red = False
            break
        else:
            continue

    move_validator = MoveValidator()
    engine = Engine()
    current_board_case = BoardCase()
    show_board(current_board_case.board)

    if not is_user_red:
        # stone, end_pos = engine.gen_random_move(current_board_case)
        stone, end_pos = engine.gen_move(current_board_case)
        current_board_case.make_move(stone, end_pos)
        engine_move = f"{STONE_SHOW_MAP[stone]}->{end_pos+1}"
        print(f"Engine Move: {engine_move}")
        show_board(current_board_case.board)

    while True:
        print("Please enter your move (e.g. R1->4): ")
        user_move = input().upper()
        if user_move == 'QUIT':
            return  # end the game

        # Validate the syntax of user input
        user_part = 'R' if is_user_red else 'B'
        valid_move, user_stone, end_pos = parse_user_move(user_move, part=user_part)
        if not valid_move:
            print("Not a valid input")
            continue

        # Validate the user move per current board
        if not move_validator.validate_move(current_board_case, user_stone, end_pos):
            print("Not a valid move")
            continue

        # make user move and show board, then check if user wins
        current_board_case.make_move(user_stone, end_pos)
        show_board(current_board_case.board)
        _check_win(current_board_case)

        # Turn to Engine to play
        # stone, end_pos = engine.gen_random_move(current_board_case)
        stone, end_pos = engine.gen_move(current_board_case)
        if stone is None:
            print("No Available Moves, Pass!")
            current_board_case.red_turn(not current_board_case.red_turn)
        else:
            current_board_case.make_move(stone, end_pos)

        engine_move = f"{STONE_SHOW_MAP[stone]}->{end_pos+1}"
        print(f"Engine Move: {engine_move}")
        show_board(current_board_case.board)
        _check_win(current_board_case)


def main():
    user_play()


if __name__ == '__main__':
    main()
