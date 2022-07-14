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
    if int(row) == 0:
        if rowOne[int(column)] != " _ ":
            print("There is something already on this square. Please try again")
        else:
            squareCheck = "True"
            print(squareCheck)
    elif int(row) == 1:
        if rowTwo[int(column)] != " _ ":
            print("There is something already on this square. Please try again")
        else:
            squareCheck = "True"
    elif int(row) == 2:
        if rowThree[int(column)] != " _ ":
            print("There is something already on this square. Please try again")
        else:
            squareCheck = "True"
    else:
        print("Please make sure that the row is between 0 and 2.")
    return(squareCheck)

def placeMark(row, column, player):
    if row == 0:
        rowOne[int(column)] = player
    elif row == 1:
        rowTwo[int(column)] = player
    elif row == 2:
        rowThree[int(column)] = player
    


def gameOver(player):
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
        pass
    return gameResult

def round():
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
        print(squareCheck)
    placeMark(row, column, player)
    gameOver(player)
    printBoard()
    print("Player 2's turn.")
    player = " O "
    while squareCheck == "False":
        print("Enter a row number from 0-2:")
        row=input()
        print("Enter a column number from 0-2")
        column=input()
        checkMark(row, column)
    placeMark(row, column, player)
    gameOver(player)

while gameResult == "":
    round()
    
