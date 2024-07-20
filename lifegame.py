from copy import deepcopy
from pprint import pprint
class Lifegame:
    def __init__(self, size: int = 50, rule = lambda x: x in range(2, 4)):
        self.size = 50
        self.rule = rule
        self.board: list[list[int]] = [[0] * (size)] * (size)
    def setup(self, dots: list[list[int]]):
        for dot in dots:
            self.board[dot[0]][dot[1]] = 1 if self.board[dot[0]][dot[1]]==1 else 0
    def step(self, n = 1):
        tmp = deepcopy(self.board)
        for _ in range(n):
            for i, j in zip(range(self.size), range(self.size)):
                if tmp[i][j] == 1:
                    countneighbors = 0
                    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    for x, y in directions:
                        if i+x in range(self.size) and j+y in range(self.size):
                            countneighbors += tmp[i+x][j+y]
                    self[i][j] = 1 if self.rule(countneighbors) else 0
    def print(self):
        pprint(self.board)

        #abbaabba