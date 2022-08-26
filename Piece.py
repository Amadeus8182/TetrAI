from blockShapes import blocks

class Piece:
    def __init__(self, board, shape):
        self.rot = 0
        self.board = board
        self.shape = blocks[shape]
        self.pos = board.width/2
        
        