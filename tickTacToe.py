from collections import deque

from playingPiece import *
from board import Board
from pieceType import PieceType
from player import Player


class TickTacToe:
    
    players = deque()

    def intializeGame(self):
        crossPiece = CrossPiece()
        player1 = Player("rushi",crossPiece)
        circlePiece = CirclePiece()
        player2 = Player("shwetu",circlePiece)
        self.players.append(player1)
        self.players.append(player2)
        self.gameBoard = Board(3)
        self.board = self.gameBoard.board
    
    def startGame(self):
        self.noWinner = True
        while self.noWinner:
            playerTurn = self.players.popleft()
            self.gameBoard.printBoard()
            freeSpace = self.gameBoard.getFreeCells()
            if len(freeSpace) == 0:
                self.noWinner = False
                continue

            print(f"Player {playerTurn.name} Enter row,column")
            row ,col  = map(int,input().split()) 
            pieceAddedSuccesfully = self.gameBoard.addPiece(row,col,playerTurn.playingPiece)
            if not pieceAddedSuccesfully:
                print("Incorrect Position selected.Please Try again !")
                self.players.appendleft(playerTurn)
                continue
            self.players.append(playerTurn)

            winner = self.isThereWinner(row-1,col-1,playerTurn.playingPiece.piece)
            if winner:
                print("winner rushi")
                return playerTurn.name
        return "tie"
    
    def isThereWinner(self,row,col,pieceType):
        rowMatch = True
        colMatch = True
        diagMatch = True
        antiDiagMatch = True

        
        for i in range(self.gameBoard.size):
            
            # check for rows --
            if(self.board[row][i] == None or self.board[row][i].piece != pieceType):
                rowMatch = False
                continue

        for i in range(self.gameBoard.size):  
            # check for cols |
            if(self.board[i][col] == None or self.board[i][col].piece != pieceType):
                colMatch = False
                continue

        for i, j in zip(range(self.gameBoard.size), range(self.gameBoard.size)):

            # check for diagonal \
            if(self.board[i][j]==None or self.board[i][j].piece != pieceType):
                diagMatch = False
                continue

        for i, k in zip(range(self.gameBoard.size),range(self.gameBoard.size - 1, -1, -1)):
            # check for antidiagonal /
            if(self.board[i][k] == None or self.board[i][k].piece != pieceType):
                antiDiagMatch = False
                continue

        return rowMatch or colMatch or diagMatch or antiDiagMatch

