import random

from constants import MIN_SCORE, MAX_SCORE
from utils import check_red_win, check_black_win
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

    """
        :return: score:int, the score of the board case
        :return: move:Move or None, the best move or None if no available moves
    """
    @staticmethod
    def minimax(board_case: BoardCase, depth: int):
        # print("depth: ", depth)
        if check_red_win(board_case.red_positions.values()):
            return MAX_SCORE, None
        if check_black_win(board_case.black_positions.values()):
            return MIN_SCORE, None
        if depth == 0:
            return 0, None

        move_generator = MoveGenerator(board_case)

        if board_case.red_turn:
            best_score = MIN_SCORE
            best_move = None
            red_moves_and_boardcases = move_generator.gen_red_moves_and_boardcases()
            for move_and_board_case in red_moves_and_boardcases:
                curr_move = move_and_board_case[0]
                curr_board_case = move_and_board_case[1]
                curr_score = Engine.minimax(curr_board_case, depth-1)[0]
                if curr_score == MAX_SCORE:
                    return curr_score, curr_move
                else:
                    if curr_score > best_score:
                        best_score = curr_score
                        best_move = curr_move
            return best_score, best_move

        else:  # turn to black to play
            best_score = MAX_SCORE
            best_move = None
            black_moves_and_boardcases = move_generator.gen_black_moves_and_boardcases()
            for move_and_board_case in black_moves_and_boardcases:
                curr_move = move_and_board_case[0]
                curr_board_case = move_and_board_case[1]
                curr_score = Engine.minimax(curr_board_case, depth-1)[0]
                if curr_score == MIN_SCORE:
                    return curr_score, curr_move
                else:
                    if curr_score < best_score:
                        best_score = curr_score
                        best_move = curr_move
            return best_score, best_move

    @staticmethod
    def gen_move(board_case: BoardCase, depth: int = 10):
        score, move = Engine.minimax(board_case, depth)
        if move is None:
            return None
        return move.stone, move.end_pos, score
