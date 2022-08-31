import numpy as np
import os
import time
from Piece import Piece
from random import choice

class Board:
    

    def __init__(self, gravity):
        self.board = np.zeros([20,10])
        self.size = (len(self.board[0]), len(self.board))           # (w,h)
        self.grav = gravity

        self.possiblePieces = ['O', 'T', 'I', 'L', 'J', 'S', 'Z']
        
        self.piece = Piece(self.board, 'I')
        self.holdPiece = None

    def move_handler(self, move):
        match move:
            case 'Left':
                self.piece.left()
            case 'Right':
                self.piece.right()
            case 'Down':
                self.piece.fall()
            case 'Drop':
                self.piece.drop()
            case 'RotateL':
                self.piece.rotateL()
            case 'RotateR':
                self.piece.rotateR()
            case 'Rotate180':
                self.piece.rotate180()
            case 'Hold':
                if self.holdPiece == None:
                    self.holdPiece = self.piece
                    self.piece = Piece(self.board, choice(self.possiblePieces))
                else:
                    temp = self.piece
                    self.piece = self.holdPiece
                    self.holdPiece = temp

    def update(self, move):      
        self.move_handler(move)
        self.piece.fall()
        

    def show(self):

        os.system('clear')
        for x, y in self.piece.currShape:
            self.board[y+self.piece.pos[1]][x+self.piece.pos[0]] = 1

        print(self.board)

        for x, y in self.piece.currShape:
            self.board[y+self.piece.pos[1]][x+self.piece.pos[0]] = 0


