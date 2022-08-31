from Board import Board
import os

class Game:
    def __init__(self):
        self.bd = Board(1)
        self.possibleMoves = ['Left', 'Right', 'Down', 'Drop', 'RotateR', 'RotateL', 'Rotate180']
        self.score = 0
        
    def play(self):
        loss = False
        while not loss:
            while True:                                     # MIGHT REMOVE BECAUSE AI WILL PLAY
                try:                                        # KEEP IF WANT HUMAN PLAYERS TO PLAY
                    move = self.possibleMoves[int(input())]
                except ValueError:
                    print("Enter a valid move")
                    continue

                break
            
######################################################################

            self.bd.update(move)
            self.bd.show()
            

