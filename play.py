from tickTacToe import TickTacToe

def play():
    game = TickTacToe()
    game.intializeGame()
    print("Winner is ",game.startGame())

if __name__ == "__main__":
    play()