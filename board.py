from player import Player
from playingPiece import PlayingPiece,CirclePiece,CrossPiece,SlashPiece

class Board:

    def __init__(self,size):
        self.size = size
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]

    def addPiece(self,row,col,pieceType):
        if row < 0 or col < 0 or row > self.size or col > self.size:
            return False
        if self.board[row-1][col-1] != None:
            return False
        self.board[row-1][col-1] = pieceType
        return True

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != None:
                    print(self.board[i][j].piece.name,end="")
                else:
                    print(" ",end="")
                print(" | ",end="")
            print()
    
    def getFreeCells(self):
        freeCells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    freeCells.append([i,j])
        return freeCells
