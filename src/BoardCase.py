from constants import INIT_BOARD, RED_INIT_POSITIONS, BLACK_INIT_POSITIONS

############################################################################################
#  BoardCase: describes a board case in the game, including:
#  - board: the board presented as a list like INIT_BOARD
#  - red_positions: a map with key as red stones and value as position in board
#  - black_positions: a map with key as black stones and value as position in board
#  - red_turn: whether it's red's turn
############################################################################################
class BoardCase:
    def __init__(self,
                 board=INIT_BOARD,
                 red_positions=RED_INIT_POSITIONS,
                 black_positions=BLACK_INIT_POSITIONS,
                 red_turn=True):
        self._board = board
        self._red_positions = red_positions
        self._black_positions = black_positions
        self._red_turn = red_turn

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, value):
        self._board = value

    @property
    def red_positions(self):
        return self._red_positions

    @red_positions.setter
    def red_positions(self, value):
        self._red_positions = value

    @property
    def black_positions(self):
        return self._black_positions

    @black_positions.setter
    def black_positions(self, value):
        self._black_positions = value

    @property
    def red_turn(self):
        return self._red_turn

    @red_turn.setter
    def red_turn(self, value):
        self._red_turn = value
