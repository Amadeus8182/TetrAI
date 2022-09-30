from Board import Board
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
                if event.type == pg.KEYDOWN:
                    match event.key:
                        case pg.K_a: self.bd.inpMove('Hold')
                        case pg.K_s: self.bd.inpMove('Left')
                        case pg.K_d: self.bd.inpMove('Down')
                        case pg.K_f: self.bd.inpMove('Right')
                        case pg.K_j: self.bd.inpMove('RotateL')
                        case pg.K_k: self.bd.inpMove('Drop')
                        case pg.K_l: self.bd.inpMove('RotateR')
                        case pg.K_SEMICOLON: self.bd.inpMove('Rotate180')
            frame = (frame+1)%33
            self.bd.update(frame)
            self.bd.show()


         
            
            


            
            
            

