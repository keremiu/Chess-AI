from piece import Piece

def __init__(self, board, white=False):
    self.board = board
    self.white = white
    pass

def move(self, fromCoor, toCoor):
    fromPic = self.board[fromCoor[0], fromCoor[1]]
    toPic = self.board[toCoor[0], toCoor[1]]
    if (fromPic == 0):
        return "No piece selected"
    fromPic.check(fromCoor, toCoor, self.board)
    pass
