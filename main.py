import random

def drawBoard(board):
    print(board[7] + "|" + board[8] + "|" +board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" +board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" +board[3])

def choseAletter():
    # Make the user chose a Letter X OR O
    # return an array [X, O] OR [O, X]
    letter = ""
    while not(letter == "X" or letter == "O"):
        letter = input("Choose a letter X or O: ").upper()

    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]
    
def randomTurn():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def isSpacefree(board, move):
    return board[move] == " "

def getUserMove(board):
    move = ' '
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpacefree(board,int(move)):
        print("What is your next move? (1-9)")
        move = input()
    
    return int(move)

def makeMove(board,move,letter):
    board[move] = letter

def isWinner(bo, le):
    return(bo[7] == le and bo[8] == le and bo[9] == le or 
           bo[4] == le and bo[5] == le and bo[6] == le or
           bo[1] == le and bo[2] == le and bo[3] == le or
           bo[7] == le and bo[4] == le and bo[1] == le or
           bo[8] == le and bo[5] == le and bo[2] == le or
           bo[9] == le and bo[6] == le and bo[3] == le or
           bo[4] == le and bo[5] == le and bo[6] == le or
           bo[7] == le and bo[5] == le and bo[3] == le or
           bo[9] == le and bo[5] == le and bo[1] == le)

def isBoardFull(board):
    for i in range(1,10):
        if board[i] == " ":
            return False
    return True

def getComputerMove(board, computerLetter, playerLetter):
    possibleMoves = getPossibleMoves(board)
    
    for i in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, i, computerLetter)
        if isWinner(boardCopy, computerLetter):
            return i
        
    # block player to winning
    for i in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, i, playerLetter)
        if isWinner(boardCopy, playerLetter):
            return i
    
    #choose a corner
    move = chooseRandomMoveFromList(board, [7,1,9,3])
    if move != None:
        return move
    
    #choose the center
    if isSpacefree(board, 5):
        return 5
    
    return chooseRandomMoveFromList(board, [2,6,8,4])
    




def getPossibleMoves(board):
    possibleMoves = []
    for i in range(1,10):
        if isSpacefree(board,i):
            possibleMoves.append(i)
    if possibleMoves != 0:
        return possibleMoves
    else:
        return None
    
def getBoardCopy(board):
    copyBoard = []
    for i in board:
        copyBoard.append(i)

    return copyBoard

def chooseRandomMoveFromList(board, list):
    possibleMoves = []

    for i in list:
        if isSpacefree(board,i):
            possibleMoves.append(i)
        
    if len(possibleMoves) > 0:
        return random.choice(possibleMoves)
    else:
        return None

   

    

def run():
    while True:
        board = [" "] * 10
        playerLetter ,letterComputer = choseAletter()
        turn = randomTurn()
        print(f"The {turn} will go first.")
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == "player":
                drawBoard(board)
                move = getUserMove(board)
                makeMove(board,move,playerLetter)

                if isWinner(board, playerLetter):
                    print("Congradulation you win")
                    drawBoard(board)
                    gameIsPlaying = False
                    continue
                else:
                    if isBoardFull(board):
                        print("The game is tie!")
                        break
                    else:
                        turn = "computer"
            else:
                move = getComputerMove(board, letterComputer, playerLetter)
                makeMove(board, move, letterComputer)

                if isWinner(board, letterComputer):
                    print("Sorry you lost agaist me!")
                    drawBoard(board)
                    gameIsPlaying = False
                    continue
                else:
                    if isBoardFull(board):
                        print("The game is tie!")
                        break
                    else:
                        turn = "player"


        print("Do you want to play again? (Yes or no)")
        if not input().lower().startswith("y"):
            break

    
   

          
       


if __name__ == "__main__":
    run()

