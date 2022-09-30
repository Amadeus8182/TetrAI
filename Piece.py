from blockShapes import blocks

class Piece:
    def __init__(self, bd, shape, lftime):

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
        self.lifetime_const = lftime
        self.lifetime = self.lifetime_const

        # Position
        self.pos_const = (3,-self.minDist[self.rot][1])
        self.pos = self.pos_const                      # (w, h)

    def fall(self):
        if self.canFall((self.pos[0], self.pos[1]+1)):
            self.pos = (self.pos[0], self.pos[1]+1)   

    def drop(self):
        while True:
            if self.canFall((self.pos[0], self.pos[1]+1)):
                self.pos = (self.pos[0], self.pos[1]+1)
            else:
                self.lifetime=0
                break

    def right(self):
        if self.wallCheck(self.pos[0]+1) and self.collisionCheck((self.pos[0]+1, self.pos[1]), self.currShape):
            self.pos = (self.pos[0]+1, self.pos[1])
        
    def left(self):
        if self.wallCheck(self.pos[0]-1) and self.collisionCheck((self.pos[0]-1, self.pos[1]), self.currShape):
            self.pos = (self.pos[0]-1, self.pos[1])

    def rotateR(self):
        if self.collisionCheck(self.adjustPos(self.pos), self.pieceShapes[(self.rot+1) % self.numberOfRotations]):
            self.rot = (self.rot+1) % self.numberOfRotations
            self.currShape = self.pieceShapes[self.rot]
            self.pos = self.adjustPos(self.pos)

    def rotateL(self):
        self.rot = (self.rot-1) % self.numberOfRotations
        self.currShape = self.pieceShapes[self.rot]
        self.pos = self.adjustPos(self.pos)

    def rotate180(self):
        self.rot = (self.rot+2) % self.numberOfRotations
        self.currShape = self.pieceShapes[self.rot]
        self.pos = self.adjustPos(self.pos)

    def wallCheck(self, p):
        return p+self.minDist[self.rot][0] >= 0 and p+self.maxDist[self.rot][0] < self.boardShape[0]

    def floorCheck(self, p):
        return p+self.maxDist[self.rot][1] < self.boardShape[1]
 
    def collisionCheck(self, p, shape):
        for x, y in shape:
            xPos = x+p[0]
            yPos = y+p[1]
            if self.board[yPos][xPos] == 1:
                return False
        return True

    def canFall(self, p):
        return self.floorCheck(p[1]) and self.collisionCheck(p, self.currShape)

    def adjustPos(self, p):
        x = max(-self.minDist[self.rot][0], min(self.boardShape[0]-self.maxDist[self.rot][0]-1, p[0]))
        y = min(self.boardShape[1]-self.maxDist[self.rot][1]-1, p[1])
        return (x,y)

    def resetPos(self):
        self.pos = self.pos_const

    def update(self, frame):
        if frame == 32:
            self.fall()
        
        if not self.canFall((self.pos[0], self.pos[1]+1)):
            self.lifetime -= 1
        else:
            self.lifetime = self.lifetime_const