import numpy as np
from operator import xor

def __init__(self, typeName, white = False):
    self.white = white
    self.typeName = typeName
    pass

def defType(self):
    if (self.typeName == "king"):
        self.type = 1
        self.score = 100
    elif (self.typeName == "queen"):
        self.type = 2
        self.score = 9
    elif (self.typeName == "rook"):
        self.type = 3
        self.score = 5
    elif (self.typeName == "knight"):
        self.type = 4
        self.score = 3
    elif (self.typeName == "bishop"):
        self.type = 5
        self.score = 3
    elif (self.typeName == "pawn"):
        self.type = 6
        self.score = 1

def check(self, fromCoor, toCoor, toPic):
    if ((fromCoor[0] <= 7 & fromCoor[0] >= 0 & fromCoor[1] <= 7 & fromCoor[1] >= 0 & toCoor[0] <= 7 & toCoor[0] >= 0 & toCoor[1] <= 7 & toCoor[1] >= 0) == False):
        return False
    if (self.type == 1):
        if (np.abs(toCoor[0] - fromCoor[0]) == 1 | np.abs(toCoor[1] - fromCoor[1]) == 1):
            return invernalCheck(self, fromCoor, toCoor, cross=((np.abs(toCoor[0] - fromCoor[0]) == 1 & (np.abs(toCoor[1] - fromCoor[1]) == 1))), straight=xor(((np.abs(toCoor[0] - fromCoor[0]) == 1), (np.abs(toCoor[1] - fromCoor[1]) == 1))))
    pass

def invernalCheck(self, fromCoor, toCoor, toPic, cross=False, straight=False):
        if (toPic.white == self.white):
            return False
        if (cross & straight):
            pass