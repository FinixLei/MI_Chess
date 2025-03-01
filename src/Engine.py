import copy
import random

from constants import MIN_SCORE, MAX_SCORE
from utils import check_red_win, check_black_win, show_board
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
            moves_and_new_board_cases = move_generator.gen_moves_and_board_cases()
        else:
            moves_and_new_board_cases = move_generator.gen_moves_and_board_cases()

        if len(moves_and_new_board_cases) == 0:
            return None, None

        move = moves_and_new_board_cases[random.randint(0, len(moves_and_new_board_cases)-1)][0]
        return move.stone, move.end_pos

    """
        :return: score:int, the score of the board case
        :return: move_list: A list of move sequence, including current move for current board case
    """
    @staticmethod
    def min_max(board_case: BoardCase, depth: int):
        if check_red_win(board_case.red_positions.values()):
            return MAX_SCORE, []
        if check_black_win(board_case.black_positions.values()):
            return MIN_SCORE, []
        if depth == 0:
            return 0, []

        # print(f"<<<<<<<<<<<<<<<<< depth = {depth} <<<<<<<<<<<<<<<<<<<<<")
        move_generator = MoveGenerator(board_case)
        best_score = 0
        best_move = None
        best_move_list = []

        if board_case.red_turn:
            best_score = MIN_SCORE
            red_moves_and_board_cases = move_generator.gen_moves_and_board_cases()
            if len(red_moves_and_board_cases) == 0:
                best_score = 0
            for move_and_board_case in red_moves_and_board_cases:
                curr_move = move_and_board_case[0]
                curr_board_case = move_and_board_case[1]
                curr_score, move_list = Engine.min_max(curr_board_case, depth-1)
                # print(f"my_depth={depth}, curr_move={str(curr_move)}, curr_score={curr_score}, move_list={[str(item) for item in move_list]}")
                if curr_score > best_score or best_move is None:
                    best_score = curr_score
                    best_move = copy.deepcopy(curr_move)
                    best_move_list = copy.deepcopy(move_list)
                    if curr_score == MAX_SCORE:
                        break
        else:  # turn to black to play
            best_score = MAX_SCORE
            black_moves_and_board_cases = move_generator.gen_moves_and_board_cases()
            len_available_move_list = len(black_moves_and_board_cases)
            if len(black_moves_and_board_cases) == 0:
                best_score = 0
            for move_and_board_case in black_moves_and_board_cases:
                curr_move = move_and_board_case[0]
                curr_board_case = move_and_board_case[1]
                curr_score, move_list = Engine.min_max(curr_board_case, depth-1)
                # print(f"my_depth={depth}, curr_move={str(curr_move)}, curr_score={curr_score}, move_list={[str(item) for item in move_list]}")
                if curr_score < best_score or best_move is None:
                    best_score = curr_score
                    best_move = copy.deepcopy(curr_move)
                    best_move_list = copy.deepcopy(move_list)
                    if curr_score == MIN_SCORE:
                        break

        best_move_list.append(best_move)
        # show_list = ", ".join([str(item) for item in best_move_list[::-1]])
        # print(f"Depth={depth}, Score={best_score}, best_move={str(best_move)}, Move List: {show_list}")
        # show_board(curr_board_case.board)
        return best_score, best_move_list

    @staticmethod
    def gen_move(board_case: BoardCase, depth: int = 10):
        score, move_list = Engine.min_max(board_case, depth)
        if len(move_list) == 0:
            return None
        move = move_list[-1]
        return move.stone, move.end_pos, score
