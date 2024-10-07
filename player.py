from playingPiece import PlayingPiece

class Player:
    name = ""

    def __init__(self,name,playingPiece):
        self.name = name
        self.playingPiece = playingPiece
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def getPiece(self):
        return self.playingPiece
    
    def setPiece(self,playingPiece):
        self.playingPiece = playingPiece