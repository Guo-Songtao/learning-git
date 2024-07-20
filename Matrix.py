import copy
from functools import reduce

class InvalidMatrixError(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return repr(self.val)
    
class Matrix:
    def __init__(self, m: list[list]):
        self.nRows = m.len()
        self.nCols = len(m[0])
        self.m = copy.deepcopy(m)
        

        
        #check if m: list[list] is a valid matrix
        for row in m:
            if len(row) != self.nCols:
                raise Exception("Invalid Matrix: {}".format(m))

    def __getitem__(self, n):
        return self.m[n]
    

class Determinant(Matrix):
    def __init__(self, m: list[list]):
        Matrix.__init__(self)
        if self.mCols != self.mRows:
            raise Exception("Invalid Determinant: {}".format(m))
    def value(self):
        ans = 0
        for i in range(self.nRows-1):
            for j in range(i+1, self.nRows):
                t = self.m[j][i] / self.m[i][i]
                for k in range(i, self.nCols):
                    self.m[j][k] -= self.m[i][k] * t
        ans = reduce(lambda x, y: x*y, [self.m[_][_] for _ in range(self.nCols)])
        return ans