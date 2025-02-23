import copy

from BoardCase import BoardCase
from Move import Move
from constants import ROUTING_MAP, EMPTY

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

    ########################################################################################################
    # Generate all Red moves and corresponding new BoardCases according to current BoardCase instance
    # @return: a list of (Move, BoardCase)
    ########################################################################################################
    def gen_red_moves_and_boardcases(self):
        moves_and_boardcases = []
        for red_stone in self._board_case.red_positions:
            start_pos = self._board_case.red_positions[red_stone]
            available_positions = ROUTING_MAP[start_pos]
            for end_pos in available_positions:
                if self._board_case.board[end_pos] == EMPTY:
                    # generate new Move instance
                    new_move = Move(red_stone, start_pos, end_pos)

                    # generate basic information of new BoardCase
                    board = copy.deepcopy(self._board_case.board)
                    red_positions = copy.deepcopy(self._board_case.red_positions)
                    black_positions = copy.deepcopy(self._board_case.black_positions)

                    # update board and red_positions
                    board[start_pos] = EMPTY
                    board[end_pos] = red_stone
                    red_positions[red_stone] = end_pos
                    new_boardcases  = BoardCase(board, red_positions, black_positions, False)
                    moves_and_boardcases.append((new_move, new_boardcases))

        return moves_and_boardcases

    ########################################################################################################
    # Generate all Black moves and corresponding new BoardCases according to current BoardCase instance
    # @return: a list of (Move, BoardCase)
    ########################################################################################################
    def gen_black_moves_and_boardcases(self):
        moves_and_boardcases = []
        for black_stone in self._board_case.black_positions:
            start_pos = self._board_case.black_positions[black_stone]
            available_positions = ROUTING_MAP[start_pos]
            for end_pos in available_positions:
                if self._board_case.board[end_pos] == EMPTY:
                    # generate new Move instance
                    new_move = Move(black_stone, start_pos, end_pos)

                    # generate basic information of new BoardCase
                    board = copy.deepcopy(self._board_case.board)
                    red_positions = copy.deepcopy(self._board_case.red_positions)
                    black_positions = copy.deepcopy(self._board_case.black_positions)

                    # update board and red_positions
                    board[start_pos] = EMPTY
                    board[end_pos] = black_stone
                    black_positions[black_stone] = end_pos
                    new_boardcases  = BoardCase(board, red_positions, black_positions, False)
                    moves_and_boardcases.append((new_move, new_boardcases))

        return moves_and_boardcases
