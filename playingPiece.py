from pieceType import PieceType

class PlayingPiece:
    def __init__(self,piece :PieceType):
        if isinstance(piece,PieceType):
            self.piece = piece
        else:
            print("Wrong PieceType has been choosed")
            raise ValueError(f"invalid PieceType")
        
class CirclePiece(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)

class CrossPiece(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)

class SlashPiece(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.I)