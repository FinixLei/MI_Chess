##########################################################################################
# Move: describes one specific stone moves from "start" position to "end" position
##########################################################################################
class Move:
    def __init__(self,stone,start_pos,end_pos):
        self._stone=stone
        self._start_pos = start_pos
        self._end_pos = end_pos

    def __str__(self):
        return f"{self._stone}_{self._start_pos}_{self._end_pos}"

    def __eq__(self, other):
        return self.stone == other.stone and self.start_pos == other.start_pos and self.end_pos == other.end_pos

    @property
    def stone(self):
        return self._stone

    @property
    def start_pos(self):
        return self._start_pos

    @property
    def end_pos(self):
        return self._end_pos
