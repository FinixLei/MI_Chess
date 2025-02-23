import random

from BoardCase import BoardCase
from MoveGenerator import MoveGenerator

class Engine:
    def __init__(self):
        self._board_case = None

    def set_board_case(self, board_case: BoardCase):
        self._board_case = board_case

    ###################################################################
    # @return: stone:int, end_pos:int or None if no available moves
    ###################################################################
    def gen_random_move(self):
        if self._board_case is None:
            return None, None

        move_generator = MoveGenerator(self._board_case)
        if self._board_case.red_turn:
            moves_and_new_boardcases = move_generator.gen_red_moves_and_boardcases()
        else:
            moves_and_new_boardcases = move_generator.gen_black_moves_and_boardcases()

        if len(moves_and_new_boardcases) == 0:
            return None, None

        move = moves_and_new_boardcases[random.randint(0, len(moves_and_new_boardcases)-1)][0]
        return move.stone, move.end_pos
