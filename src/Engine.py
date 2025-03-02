import copy
import random

from constants import MIN_SCORE, MAX_SCORE, PlayerColor
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
                if curr_score > best_score or best_move is None:
                    best_score = curr_score
                    best_move = copy.deepcopy(curr_move)
                    best_move_list = copy.deepcopy(move_list)
                    if curr_score == MAX_SCORE:
                        break
        else:  # turn to black to play
            best_score = MAX_SCORE
            black_moves_and_board_cases = move_generator.gen_moves_and_board_cases()
            if len(black_moves_and_board_cases) == 0:
                best_score = 0
            for move_and_board_case in black_moves_and_board_cases:
                curr_move = move_and_board_case[0]
                curr_board_case = move_and_board_case[1]
                curr_score, move_list = Engine.min_max(curr_board_case, depth-1)
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

    """
        Generate a move for the given board case
        Note, this function calculate the depths from 5 to the given depth
        If the search finds a winning move, it will return immediately
        Why do this? 
        Because when a killer move is found in depth 5 but if the search depth is 10, 
        several other moves are also considered as killer moves but actually they are not, 
        as they could waste several rounds and then execute the real killer move.
        This way will make the generated move is not the real killer move, so that it cannot beat the opponent.
        So we need to start from depth 5 and if a winning move is found, we return immediately.
        
        :param board_case: the current board case
        :param depth: the depth of the search
        :return: stone:int, or None if no available moves
        :return: end_pos:int 
        :return: score:int, the score of the board case
    """
    @staticmethod
    def gen_move(board_case: BoardCase, depth: int = 10):
        player_side = PlayerColor.RED if board_case.red_turn else PlayerColor.BLACK
        least_depth = 5
        if depth < least_depth:
            depth = least_depth

        di = least_depth
        move = None
        score = 0
        while di <= depth:
            print(f"Engine is thinking for depth = {di}...")
            score, move_list = Engine.min_max(board_case, di)
            if len(move_list) == 0:
                return None, -1, 0

            move = move_list[-1]
            if score == MAX_SCORE and player_side == PlayerColor.RED:
                return move.stone, move.end_pos, score
            elif score == MIN_SCORE and player_side == PlayerColor.BLACK:
                return move.stone, move.end_pos, score
            else:
                di += 1

        return move.stone, move.end_pos, score
