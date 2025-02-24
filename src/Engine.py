import random

from BoardCase import BoardCase
from MoveGenerator import MoveGenerator

class Engine:
    def __init__(self):
        pass

    """
        :return: stone:int, end_pos:int or None if no available moves
    """
    @staticmethod
    def gen_random_move(board_case: BoardCase):
        if board_case is None:
            return None, None

        move_generator = MoveGenerator(board_case)
        if board_case.red_turn:
            moves_and_new_boardcases = move_generator.gen_red_moves_and_boardcases()
        else:
            moves_and_new_boardcases = move_generator.gen_black_moves_and_boardcases()

        if len(moves_and_new_boardcases) == 0:
            return None, None

        move = moves_and_new_boardcases[random.randint(0, len(moves_and_new_boardcases)-1)][0]
        return move.stone, move.end_pos
