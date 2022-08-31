from Board import Board

class Game:
    def __init__(self):
        self.bd = Board(1)
        self.possibleMoves = ['Left', 'Right', 'Down', 'Drop', 'RotateR', 'RotateL', 'Rotate180']
        self.score = 0
        
    def play(self):
        loss = False
        while not loss:
            self.bd.update()
