import numpy as np
from piece import Piece

class Game:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=Piece)
        self.start()
        pass

    def start(self):
        self.board[0] = np.array([Piece(True, "rook"), Piece(True, "knight"), Piece(True, "bishop"), Piece(True, "queen"), Piece(True, "king"), Piece(True, "bishop"), Piece(True, "knight"), Piece(True, "rook")])
        self.board[1] = np.array([Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn")])
        self.board[6] = np.array([Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn")])
        self.board[7] = np.array([Piece(False, "rook"), Piece(False, "knight"), Piece(False, "bishop"), Piece(False, "queen"), Piece(False, "king"), Piece(False, "bishop"), Piece(False, "knight"), Piece(False, "rook")])
        pass

