from constants import INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS, STONE_TO_NUM
from utils import show_board, parse_user_move
from BoardCase import BoardCase
from MoveGenerator import MoveGenerator
from MoveValidator import MoveValidator


def user_red_play():
    move_validator = MoveValidator()
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

        # TODO: Engine generate move and show board


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
