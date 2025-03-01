import copy

from BoardCase import BoardCase
from Move import Move
from constants import ROUTING, EMPTY

#####################################################################################################
#  MoveGenerator: given a specific BoardCase, generate all Moves and corresponding new BoardCases
#####################################################################################################

class MoveGenerator:
    def __init__(self, board_case: BoardCase):
        self._board_case = board_case

    @property
    def board_case(self):
        return self._board_case

    @board_case.setter
    def board_case(self, value):
        self._board_case = value

    """
        Generate all moves and corresponding board cases per the given BoardCase instance and player side
        :return a list of (Move, BoardCase)
    """
    def gen_moves_and_board_cases(self):
        moves_and_board_cases = []
        stone_positions = self._board_case.red_positions if self._board_case.red_turn else self._board_case.black_positions
        for stone in stone_positions:
            start_pos = stone_positions[stone]
            available_positions = ROUTING[start_pos]
            for end_pos in available_positions:
                if self._board_case.board[end_pos] == EMPTY:
                    # generate new Move instance
                    new_move = Move(stone, start_pos, end_pos)

                    # generate basic information of new BoardCase
                    board = copy.deepcopy(self._board_case.board)
                    red_positions = copy.deepcopy(self._board_case.red_positions)
                    black_positions = copy.deepcopy(self._board_case.black_positions)

                    # update board and red_positions
                    board[start_pos] = EMPTY
                    board[end_pos] = stone
                    if self._board_case.red_turn:
                        red_positions[stone] = end_pos
                    else:
                        black_positions[stone] = end_pos
                    new_board_case  = BoardCase(board, red_positions, black_positions, not self._board_case.red_turn)
                    moves_and_board_cases.append((new_move, new_board_case))

        return moves_and_board_cases
