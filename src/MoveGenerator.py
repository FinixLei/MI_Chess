from BoardCase import BoardCase
from Move import Move

##########################################################################
#  MoveGenerator: given a specific BoardCase, generate all Moves
##########################################################################

class MoveGenerator:
    def __init__(self, board_case: BoardCase):
        self._board_case = board_case
        self._moves = []

    @property
    def board_case(self):
        return self._board_case

    def gen_moves(self):
        pass
