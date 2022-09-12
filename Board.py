from turtle import color
import numpy as np
import os
import time
from Piece import Piece
from random import choice
import pygame as pg

class Board:
    

    def __init__(self, gravity, surface):
        self.board = np.zeros([20,10])
        self.size = (len(self.board[0]), len(self.board))           # (w,h)
        self.grav = gravity
        self.WIN = surface
        self.possiblePieces = ['O', 'T', 'I', 'L', 'J', 'S', 'Z']
        
        self.piece = Piece(self.board, choice(self.possiblePieces), 48)
        self.holdPiece = None

    def move_handler(self, move=None):
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
                    self.piece = Piece(self.board, choice(self.possiblePieces), 30)
                else:
                    temp = self.piece
                    self.piece = self.holdPiece
                    self.holdPiece = temp

    def inpMove(self, move):      
        self.move_handler(move)

    def update(self, frame):
        if frame == 32:
            self.piece.fall()

    def show(self):
        for x, y in self.piece.currShape:
            xPos = x+self.piece.pos[0]
            yPos = y+self.piece.pos[1]
            if yPos >= 0:
                self.board[yPos][xPos] = 1

        for y in range(self.size[1]):
            for x in range(self.size[0]):
                sWIDTH = self.WIN.get_width()
                sHEIGHT = self.WIN.get_height()
                WIDTH = (sWIDTH)/self.size[0]
                HEIGHT = (sHEIGHT)/self.size[1]
                if self.board[y][x] == 1:
                    c = (255,255,255)
                else:
                    c = (0,0,0)
                
                p = ((sWIDTH-self.size[0]*WIDTH)/2+x*WIDTH, (sHEIGHT-self.size[1]*HEIGHT)/2+y*HEIGHT)
                pg.draw.rect(self.WIN, c, pg.Rect(p[0], p[1], WIDTH-1, HEIGHT-1))
                

        for x, y in self.piece.currShape:
            xPos = x+self.piece.pos[0]
            yPos = y+self.piece.pos[1]
            if yPos >= 0:
                self.board[yPos][xPos] = 0
        
        pg.display.flip()
        pg.display.update()


