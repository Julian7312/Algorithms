def solveK(board, step, visitedRow, visitedCol):
    
    foundPos = False
    currentCol = 0
    currentRow = 0
    
    while(foundPos == False):
        #up left
        if(board[currentRow - 2][currentCol - 1] == 0):
            board[currentRow - 2][currentCol - 1] = step
            step += 1
            visitedCol.append(currentCol - 1)
            visitedRow.append(currentRow - 2)
            foundPos = True
            
        #up right
        if(board[currentRow - 2][currentCol + 1] == 0):
            board[currentRow - 2][currentCol + 1] = step
            step += 1
            visitedCol.append(currentCol + 1)
            visitedRow.append(currentRow - 2)
            foundPos = True
            
        #left up
        if(board[currentRow - 1][currentCol - 2] == 0):
            board[currentRow - 1][currentCol - 2] = step
            step += 1
            visitedCol.append(currentCol - 2)
            visitedRow.append(currentRow - 1)
            foundPos = True
            
        #left down
        if(board[currentRow - 1][currentCol + 2] == 0):
            board[currentRow - 1][currentCol + 2] = step
            step += 1
            visitedCol.append(currentCol - 2)
            visitedRow.append(currentRow - 1)
            foundPos = True
            
        #down left
        if(board[currentRow + 2][currentCol - 1] == 0):
            board[currentRow + 2][currentCol - 1] = step
            step += 1
            visitedCol.append(currentCol - 1)
            visitedRow.append(currentRow + 2)
            foundPos = True
        
        #down right
        if(board[currentRow + 2][currentCol + 1] == 0):
            board[currentRow + 2][currentCol + 1] = step
            step += 1
            visitedCol.append(currentCol + 1)
            visitedRow.append(currentRow + 2)
            foundPos = True
            
        #right up
        if(board[currentRow - 1][currentCol + 2] == 0):
            board[currentRow - 1][currentCol + 2] = step
            step += 1
            visitedCol.append(currentCol + 2)
            visitedRow.append(currentRow - 1)
            foundPos = True
             
        #right down
        if(board[currentRow + 1][currentCol + 2] == 0):
            board[currentRow + 1][currentCol + 2] = step
            step += 1
            visitedCol.append(currentCol + 2)
            visitedRow.append(currentRow + 1)
            foundPos = True
    if(foundPos == True):
        print(board)
        solveK(board, step, visitedRow, visitedCol)


n = 8
step = 1
visitedCol = [0]
visitedRow = [0]
board = [[0]*n for _ in range(n)]
solveK(board,step,visitedRow,visitedCol)