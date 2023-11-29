#Julian Lawrence Gil Soares
#Jose Andres Lozano Alanis
#A00832272
#A01284569
#27/09/2022
#Actividad 5.1 Implementación backtracking: El problema The Knight’s tour

n = 8 
 
def checkMove(x, y, board):
    if((x >= 0 and y >= 0) and (x < n and y < n) and (board[x][y] == -1)):
        return True
    return False
 
def printBoard(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
 
def solveK(n):
 
    board = [[-1 for i in range(n)]for i in range(n)]
    x = [2, 1, -1, -2, -2, -1, 1, 2]
    y = [1, 2, 2, 1, -1, -2, -2, -1]
 
    board[0][0] = 0
 

    pos = 1
 
    if(not solveKHelper(n, board, 0, 0, x, y, pos)):
        print("Invalid")
    else:
        printBoard(n, board)
 
 
def solveKHelper(n, board, currX, currY, x, y, pos):

 
    if(pos == n**2):
        return True
 
    for i in range(8):
        newX = currX + x[i]
        newY = currY + y[i]
        if(checkMove(newX, newY, board)):
            board[newX][newY] = pos
            if(solveKHelper(n, board, newX, newY, x, y, pos+1)):
                return True
 
            board[newX][newY] = -1
    return False
 
     

solveK(n)
 
