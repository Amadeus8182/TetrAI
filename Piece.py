from blockShapes import blocks

class Piece:
    def __init__(self, bd, shape):

        # Board
        self.board = bd
        self.boardShape = (self.board.shape[1], self.board.shape[0])
        
        # Block Variables
        self.rot = 0
        self.pieceShapes = blocks[shape]
        self.currShape = self.pieceShapes[self.rot]
        self.numberOfRotations = len(self.pieceShapes) - 2
        self.maxDist = self.pieceShapes[self.numberOfRotations]
        self.minDist = self.pieceShapes[self.numberOfRotations+1]
        
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

    def rotateL(self):
        self.rot = (self.rot+1) % self.numberOfRotations
        self.currShape = self.pieceShapes[self.rot]

    def rotateR(self):
        self.rot = (self.rot-1) % self.numberOfRotations
        self.currShape = self.pieceShapes[self.rot]

    def rotate180(self):
        self.rot = (self.rot+2) % self.numberOfRotations
        self.currShape = self.pieceShapes[self.rot]
        