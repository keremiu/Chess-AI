import numpy as np
from piece import Piece

class Game:
    def __init__(self):
        self.board = np.empty((8, 8), dtype=Piece)
        self.start()
        pass

    def start(self):
        self.board[0] = np.array([Piece(True, "rook"), Piece(True, "knight"), Piece(True, "bishop"), Piece(True, "queen"), Piece(True, "king"), Piece(True, "bishop"), Piece(True, "knight"), Piece(True, "rook")])
        self.board[1] = np.array([Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn"), Piece(True, "pawn")])
        self.board[6] = np.array([Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn"), Piece(False, "pawn")])
        self.board[7] = np.array([Piece(False, "rook"), Piece(False, "knight"), Piece(False, "bishop"), Piece(False, "queen"), Piece(False, "king"), Piece(False, "bishop"), Piece(False, "knight"), Piece(False, "rook")])
        for i in range(2, 6):
            self.board[i] = np.full(8, Piece("none"))

