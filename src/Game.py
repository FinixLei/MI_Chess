from constants import STONE_SHOW_MAP
from utils import show_board, parse_user_move, check_red_win, check_black_win
from BoardCase import BoardCase
from MoveValidator import MoveValidator
from Engine import Engine

def user_red_play():
    move_validator = MoveValidator()
    engine = Engine()
    current_board_case = BoardCase()
    show_board(current_board_case.board)
    while True:
        print("Please enter your move (e.g. R1->4): ")
        user_move = input().upper()
        if user_move == 'QUIT':
            return  # end the game

        # Validate the syntax of user input
        valid_move, red_stone, end_pos = parse_user_move(user_move, part='R')
        if not valid_move:
            print("Not a valid input")
            continue

        # Validate the user move per current board
        if not move_validator.validate_move(current_board_case, red_stone, end_pos):
            print("Not a valid move")
            continue

        # make user move and show board
        current_board_case.make_move(red_stone, end_pos)
        show_board(current_board_case.board)

        if check_red_win(current_board_case.red_positions.values()):
            print("Red Win!")
            exit(0)

        engine.set_board_case(current_board_case)
        black_stone, end_pos = engine.gen_random_move()
        if black_stone is None:
            print("No Available Moves, Pass!")
            current_board_case.red_turn(not current_board_case.red_turn)
        else:
            current_board_case.make_move(black_stone, end_pos)

        engine_move = f"{STONE_SHOW_MAP[black_stone]}->{end_pos+1}"
        print(f"Engine Move: {engine_move}")
        show_board(current_board_case.board)
        if check_black_win(current_board_case.black_positions.values()):
            print("Black Win!")
            exit(0)


def user_black_play():
    print("Not Support yet")

def main():
    print("Please choose RED or BLACK (R or B): ")
    user_choice = input().upper()
    if user_choice == 'R':
        user_red_play()
    elif user_choice == 'B':
        user_black_play()


if __name__ == '__main__':
    main()
