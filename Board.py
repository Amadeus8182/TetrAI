import numpy as np
from Piece import Piece
from random import choice
class Board:
    def __init__(self, gravity):
        self.board = np.zeros([20,10])
        self.size = (len(self.board[0]), len(self.board))           # (w,h)
        self.grav = gravity

        self.possiblePieces = ['O', 'T', 'I', 'L', 'J', 'S', 'Z']
        self.piece = Piece(self.board, 'Z')

    def update(self):
        self.piece.fall()
        for x, y in self.piece.currShape:
            self.board[y+self.piece.pos[1]][x+self.piece.pos[0]] = 1
        print(self.board)
        for x, y in self.piece.currShape:
            self.board[y+self.piece.pos[1]][x+self.piece.pos[0]] = 0

