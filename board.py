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
    playerName = ""
    if player == " X ":
        playerName = 1
    else:
        playerName = 2
    if rowOne == [player, player, player] or rowTwo == [player, player, player] or rowThree == [player, player, player]:
        gameResult = "Game Over. Player " + str(playerName) + " wins!"
    elif rowOne[0] == player and rowTwo[0] == player and rowThree[0] == player:
        gameResult = "Game Over. Player " + str(playerName) + " wins!"
    elif rowOne[1] == player and rowTwo[1] == player and rowThree[1] == player:
        gameResult = "Game Over. Player " + str(playerName) + " wins!"
    elif rowOne[2] == player and rowTwo[2] == player and rowThree[2] == player:
        gameResult = "Game Over. Player " + str(playerName) + " wins!"
    elif rowOne[0] == player and rowTwo[1] == player and rowThree[2] == player:
        gameResult = "Game Over. Player " + str(playerName) + " wins!"
    elif rowOne[2] == player and rowTwo[1] == player and rowThree[0] == player:
        gameResult = "Game Over. Player " + str(playerName) + " wins!"
    else:
        rowOneFilled = 0
        rowTwoFilled = 0
        rowThreeFilled = 0
        index = 0
        while index < 3:
            if index == 0:
              if rowOne[0] != " _ " and rowOne[1] != " _ " and rowOne[2] != " _ ":
                  rowOneFilled = 1
            elif index == 1:
                if rowTwo[0] != " _ " and rowTwo[1] != " _ " and rowTwo[2] != " _ ":
                  rowTwoFilled = 1
            elif index ==2:
                if rowThree[0] != " _ " and rowThree[1] != " _ " and rowThree[2] != " _ ":
                  rowThreeFilled = 1
            index = index + 1
        if rowOneFilled == 1 and rowTwoFilled == 1 and rowThreeFilled == 1:
            gameResult = "Game Over. Draw."
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
    if gameResult != "":
        break
    else:
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

print(gameResult)