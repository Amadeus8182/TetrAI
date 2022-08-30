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
        self.pos = (0,-self.minDist[self.rot][1]-1)                      # (w, h)

    def fall(self):
        self.pos = (self.pos[0], self.pos[1]+1)             

    def left(self):
        self.pos = (self.pos[0]-1, self.pos[1]+1)

    def right(self):
        self.pos = (self.pos[0]+1, self.pos[1]+1)

    def drop(self):
        pass
        