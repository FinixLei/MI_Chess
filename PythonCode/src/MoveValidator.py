from BoardCase import BoardCase
from constants import R1, R2, R3, B1, B2, B3, EMPTY, ROUTING

class MoveValidator:
    @staticmethod
    def validate_move(board_case: BoardCase, stone: int, end_pos: int):
        if board_case.board[end_pos] != EMPTY:
            print("End position is not empty")
            return False
        if stone in [R1, R2, R3]:
            start_pos = board_case.red_positions[stone]
            if board_case.board[start_pos] != stone:
                print("Exception: red position conflicts with the board")
                return False
        elif stone in [B1, B2, B3]:
            start_pos = board_case.black_positions[stone]
            if board_case.board[start_pos] != stone:
                print("Exception: black position conflicts with the board")
                return False
        else:
            return False
        if end_pos not in ROUTING.get(start_pos):
            print(f"Cannot reach the destination {end_pos} from {start_pos}")
            return False
        return True
