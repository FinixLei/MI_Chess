from constants import INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS
from utils import show_board
from BoardCase import BoardCase
from MoveGenerator import MoveGenerator

def main():
    print("Please choose RED or BLACK (R or B): ")
    user_choice = input().upper()
    init_boardcase = BoardCase()
    show_board(init_boardcase.board)

    if user_choice == 'R':
        print('Input your move as red side, e.g. R1->4: ')


if __name__ == '__main__':
    main()
