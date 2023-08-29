#!/usr/bin/env python
#2048 Game
#Github: mammaddrik

#::::: Library :::::
import os
import random
import copy

def clearScr():
    "A Function To Clean Up The Command Prompt or Terminal."
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
        
boardSize = 4

def display():
    "This Function will print out the current board in the way we want."
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    numSpaces = len(str(largest))
    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + "|"
            else:
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
        print(currRow)
    print()

def mergeOneRowL(row):
    "This Function merges one row left."
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    
    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    
    for i in range (boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row

def merge_left(currentBoard):
    "This Function merges the whole board to the left."
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard

def reverse(row):
    "This Function reverses the order of one row."
    new = []
    for i in range(boardSize -1 , -1, -1):
        new.append(row[i])
    return new

def merge_right(currentBoard):
    "This Function merges the whole board right."
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

def transpose(currentBoard):
    "This Function transposes the whole board."
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

def merge_up(currentBoard):
    "This function merges the whole board up."
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def merge_down(currentBoard):
    "This function merges the whole board down."
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def pickNewValue():
    "This Function picks a new value for the board."
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2

def addNewValue():
    "This Function adds a value to the Board in one of the empty spaces."
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)
    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)

    board[rowNum][colNum] = pickNewValue()
    
def won():
    "This Function tests if the user has won."
    for row in board:
        if 2048 in row:
            return True
    return False
    
def noMove():
    "This Function tests if the user has lost."
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)
    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_left(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False
    
board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)
    
    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1
clearScr()
print("""Welcome to the 2048.
Simply move the tiles swiping on the board.
Tow tiles with the same number merge when
they touch. Reach the 2048 tile to win!\n
Tile Movement
Swiping up type: w
Swiping down type: s
Swiping left type: a 
Swiping right type: d
restart: r
Exit: q\n""")
display()

gameOver = False
while not gameOver:
    move = input("Which way do you want to merge: ")
    clearScr()
    validInput = True
    tempBoard = copy.deepcopy(board)
    if move == "w":
        board = merge_up(board)
    elif move == "s":
        board = merge_down(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "d":
        board = merge_right(board)
    else:
        validInput = False
        
    if not validInput:
        print("Your input was not valid, please try again")
    else:
        if board == tempBoard:
            print("Try a different direction!\n")
            display()
        else:
            if won():
                display()
                print("You Won!")
                gameOver = True
            else:
                addNewValue()
                display()
            if noMove():
                print("Game over!")
                gameOver = True