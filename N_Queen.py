#Julian Lawrence Gil Soares
#Jose Andres Lozano Alanis
#A00832272
#A01284569
#25/09/2022
#Actividad 5.3 Implementación backtracking con poda pesada
#complejidad O(n^2)

def printBoard(board): 
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
        print() 
  

def checkPos(board, row, col):
  
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    return True
  
def solvenQUtil(board, col):
      
    if col >= n:
        return True
  
    for i in range(n):
  
        if checkPos(board, i, col):
            board[i][col] = 1
            if solvenQUtil(board, col + 1) == True:
                return True

            board[i][col] = 0

    return False
  
def solvenQ(n):
    board = [[0]*n for _ in range(n)]
  
    if solvenQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
  
    printBoard(board)
    return True
  
global n
n = int(input("How many squares per row? "))
solvenQ(n)
  
