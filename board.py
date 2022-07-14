rowOne = [" _ ", " _ ", " _ "]
rowTwo = [" _ ", " _ ", " _ "]
rowThree = [" _ ", " _ ", " _ "]
gameBoard = [rowOne, rowTwo, rowThree]
gameResult = ""
player = " X "
global squareCheck
squareCheck = "False"


def printBoard():
 index = 0
 while index < 3:
    print(gameBoard[index])
    index = index + 1

def checkMark(row, column):
    if int(row) == 0 and int(column) < 3:
        if rowOne[int(column)] != " _ ":
            print("There is something already on this square. Please try again")
            squareCheck = "False"
        else:
            squareCheck = "True"
    elif int(row) == 1 and int(column) < 3:
        if rowTwo[int(column)] != " _ ":
            print("There is something already on this square. Please try again")
            squareCheck = "False"
        else:
            squareCheck = "True"
    elif int(row) == 2 and int(column) < 3:
        if rowThree[int(column)] != " _ ":
            print("There is something already on this square. Please try again")
            squareCheck = "False"
        else:
            squareCheck = "True"
    else:
        print("Please make sure that the row and column are between 0 and 2.")
        squareCheck = "False"
    return(squareCheck)

def placeMark(row, column, player):
    if int(row) == 0:
        rowOne[int(column)] = player
    elif int(row) == 1:
        rowTwo[int(column)] = player
    elif int(row) == 2:
        rowThree[int(column)] = player
    


def gameOver(player):
    gameResult = ""
    if rowOne == [player, player, player] or rowTwo == [player, player, player] or rowThree == [player, player, player]:
        gameResult = "Game Over"
    elif rowOne[0] == player and rowTwo[0] == player and rowThree[0] == player:
        gameResult = "Game Over"
    elif rowOne[1] == player and rowTwo[1] == player and rowThree[1] == player:
        gameResult = "Game Over"
    elif rowOne[2] == player and rowTwo[2] == player and rowThree[2] == player:
        gameResult = "Game Over"
    elif rowOne[0] == player and rowTwo[1] == player and rowThree[2] == player:
        gameResult = "Game Over"
    elif rowOne[2] == player and rowTwo[1] == player and rowThree[0] == player:
        gameResult = "Game Over"
    else:
        gameResult = ""
    return gameResult


while gameResult == "":
    printBoard()
    print("Player 1's turn.")
    player = " X "
    squareCheck = "False"
    while squareCheck == "False":
        print("Enter a row number from 0-2:")
        row=input()
        print("Enter a column number from 0-2")
        column=input()
        squareCheck = checkMark(row, column)
    placeMark(row, column, player)
    gameResult = gameOver(player)
    printBoard()
    squareCheck = "False"
    print("Player 2's turn.")
    player = " O "
    while squareCheck == "False":
        print("Enter a row number from 0-2:")
        row=input()
        print("Enter a column number from 0-2")
        column=input()
        squareCheck = checkMark(row, column)
    placeMark(row, column, player)
    gameResult = gameOver(player)