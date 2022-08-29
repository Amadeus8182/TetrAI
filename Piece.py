from blockShapes import blocks

class Piece:
    def __init__(self, bd, shape):

        # Board
        self.board = bd
        self.boardShape = (self.board.shape[1], self.board.shape[0])
        
        # Block Variables
        self.rot = 0
        pieceShapes = blocks[shape]
        self.currShape = pieceShapes[self.rot]
        self.numberOfRotations = len(pieceShapes) - 2
        self.maxDist = pieceShapes[self.numberOfRotations]
        self.minDist = pieceShapes[self.numberOfRotations+1]
        
        # Position
        self.pos = (0,0)                      # (w, h)

    def moveLeft(self):
        print(self.boardShape)
        