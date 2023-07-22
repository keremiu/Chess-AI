import numpy as np
from operator import xor

class Piece:
    def __init__(self, typeName, white = False):
        self.white = white
        self.typeName = typeName
        self.defType()
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

    def check(self, fromCoor, toCoor, board):
        if ((fromCoor[0] <= 7 & fromCoor[0] >= 0 & fromCoor[1] <= 7 & fromCoor[1] >= 0 & toCoor[0] <= 7 & toCoor[0] >= 0 & toCoor[1] <= 7 & toCoor[1] >= 0) == False):
            return False
        if (self.type == 1):
            if (np.abs(toCoor[0] - fromCoor[0]) <= 1 | np.abs(toCoor[1] - fromCoor[1]) <= 1):
                return invernalCheck(self, fromCoor, toCoor, board, cross=True, straight=True)
            else:
                return False
        elif (self.type == 2):
            # if (np.abs(toCoor[0] - fromCoor[0]) == np.abs(toCoor[1] - fromCoor[1]))
            pass
        pass

    def invernalCheck(self, fromCoor, toCoor, board, cross=False, straight=False):
            toPic = board[toCoor[0], toCoor[1]]
            if (toPic.white == self.white & toPic != None):
                return False
            if (cross & straight): # that means the piece is either a king or a queen
                crossCheck(self, fromCoor, toCoor, board)
                straightCheck(self, fromCoor, toCoor, board)
            if (cross & straight == False):
                crossCheck(self, fromCoor, toCoor, board)
            if (cross == False & straight):
                straightCheck(self, fromCoor, toCoor, board)
            if (cross == False & straight == False): # that means the piece is knight
                #knightCheck()
                pass

    def crossCheck(self, fromCoor, toCoor, board):
        #do the +45 degree
        c1 = oneWayCrossCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=1)
        #do the +135 degree
        c2 = oneWayCrossCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=2)
        #do the -135 degree
        c3 = oneWayCrossCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=3)
        #do the -45 degree
        c4 = oneWayCrossCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=4)
        return (c1 & c2 & c3 & c4)

    def oneWayCrossCheck(self, fromCoor, toCoor, board, way=1):
        if (fromCoor == toCoor):
            return True
        if (board[fromCoor[0], fromCoor[1]] != 0):
            return False
        if (way == 1): # +45 degree
            return oneWayCrossCheck(self, fromCoor=(fromCoor[0] + 1, fromCoor[1] - 1), toCoor=toCoor, board=board, way=way)
        if (way == 2): # +135 degree
            return oneWayCrossCheck(self, fromCoor=(fromCoor[0] - 1, fromCoor[1] - 1), toCoor=toCoor, board=board, way=way)
        if (way == 3): # -135 degree
            return oneWayCrossCheck(self, fromCoor=(fromCoor[0] - 1, fromCoor[1] + 1), toCoor=toCoor, board=board, way=way)
        if (way == 4): # -45 degree
            return oneWayCrossCheck(self, fromCoor=(fromCoor[0] + 1, fromCoor[1] + 1), toCoor=toCoor, board=board, way=way)
        pass

    def straightCheck(self, fromCoor, toCoor, board):
        #do the 0 degree
        c1 = oneWayStraightCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=1)
        #do the +90 degree
        c2 = oneWayStraightCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=2)
        #do the -90 degree
        c3 = oneWayStraightCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=3)
        #do the 180 degree
        c4 = oneWayStraightCheck(self, fromCoor=fromCoor, toCoor=toCoor, board=board, way=4)
        return (c1 & c2 & c3 & c4)

    def oneWayStraightCheck(self, fromCoor, toCoor, board, way=1):
        if (fromCoor == toCoor):
            return True
        if (board[fromCoor[0], fromCoor[1]] != 0):
            return False
        if (way == 1): # 0 degree
            return oneWayStraightCheck(self, fromCoor=(fromCoor[0] + 1, fromCoor[1]), toCoor=toCoor, board=board, way=way)
        if (way == 2): # +90 degree
            return oneWayStraightCheck(self, fromCoor=(fromCoor[0], fromCoor[1] - 1), toCoor=toCoor, board=board, way=way)
        if (way == 3): # 180 degree
            return oneWayStraightCheck(self, fromCoor=(fromCoor[0] - 1, fromCoor[1]), toCoor=toCoor, board=board, way=way)
        if (way == 4): # -90 degree
            return oneWayStraightCheck(self, fromCoor=(fromCoor[0], fromCoor[1] + 1), toCoor=toCoor, board=board, way=way)
        pass

    def knightCheck(self, fromCoor, toCoor, board):
        
        pass