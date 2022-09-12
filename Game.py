from lib2to3 import pygram
from Board import Board
import os
import pygame as pg

class Game:
    def __init__(self):
        WIN = pg.display.set_mode((500,900))
        WIN.fill((25,25,25))
        self.bd = Board(1, WIN)
        self.possibleMoves = ['Left', 'Right', 'Down', 'Drop', 'RotateR', 'RotateL', 'Rotate180', "Hold"]
        self.score = 0
        
    def play(self):
        loss = False
        frame = 0
        clock = pg.time.Clock()

        while not loss:
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    loss = True
            frame = (frame+1)%33
            self.bd.update(frame)
            self.bd.show()
                                  
            
            


            
            
            

