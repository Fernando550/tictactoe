from random import randint

def drawBoard(board):
    print(board[7] + "|" + board[8] + "|" +board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" +board[6])
    print("-+-+-")
    print(board[3] + "|" + board[2] + "|" +board[1])

def choseAletter():
    # Make the user chose a Letter X OR O
    # return an array [X, O] OR [O, X]
    letter = ""
    while not(letter == "X" or letter == "O"):
        letter = input("Chose a letter X or O: ").upper()

    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]
    
def randomTurn():
    if randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def makeAmove(move,letter,board):
    board[move] = letter

def isSpacefree(board, move):
    return board[move] == " "

def getUserMove(board):
    move = ' '
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpacefree(board,int(move)):
        print("What is your next move? (1-9)")
        move = input()
    
    return int(move)

def run():
    board = [" "] * 10
    letterPlayer ,letterComputer = choseAletter()
    turn = randomTurn()
    print(f"The {turn} will go first.")
    gameIsPlaying = True

    move = getUserMove(board)
    print(move)

    
    
    


if __name__ == "__main__":
    run()

