import numpy as np
import piece as pic

def __init__(self):
    self.board = np.zeros((8, 8))
    self.start()
    pass

def start(self):
    self.board[0] = np.array({pic(True, "rook"), pic(True, "knight"), pic(True, "bishop"), pic(True, "queen"), pic(True, "king"), pic(True, "bishop"), pic(True, "knight"), pic(True, "rook")})
    self.board[1] = np.array({pic(True, "pawn"), pic(True, "pawn"), pic(True, "pawn"), pic(True, "pawn"), pic(True, "pawn"), pic(True, "pawn"), pic(True, "pawn"), pic(True, "pawn")})
    self.board[6] = np.array({pic(False, "pawn"), pic(False, "pawn"), pic(False, "pawn"), pic(False, "pawn"), pic(False, "pawn"), pic(False, "pawn"), pic(False, "pawn"), pic(False, "pawn")})
    self.board[7] = np.array({pic("rook"), pic("knight"), pic("bishop"), pic("queen"), pic("king"), pic("bishop"), pic("knight"), pic("rook")})
    pass

