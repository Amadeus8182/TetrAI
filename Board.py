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
        
        self.piece = Piece(self.board, 'T')
        self.holdPiece = None

    def update(self, move):      
        self.move_handler(move)
        self.piece.fall()
        for x, y in self.piece.currShape:
            self.board[y+self.piece.pos[1]][x+self.piece.pos[0]] = 1
        
        print(self.board)
        time.sleep(0.5)
        os.system('clear')

        for x, y in self.piece.currShape:
            self.board[y+self.piece.pos[1]][x+self.piece.pos[0]] = 0
        
    def move_handler(self, move):
        match move:
            case 'Left':
                self.piece.left()
            case 'Right':
                self.piece.right()
            case 'Down':
                self.piece.down()
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


