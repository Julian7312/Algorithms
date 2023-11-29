#Julian Lawrence Gil Soares
#Jose Andres Lozano Alanis
#A00832272
#A01284569
#09/10/2022
#Actividad 1.3 Implementación de la técnica de programación "backtracking" y "ramificación y poda"
#complejidad: O(n^2)


def checkMove(n, maze, x, y, res):
    
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False
 
 
 
def mazeUtil(n, maze, newX, newY, x, y, res):
    
    if x == n-1 and y == n-1:
        return True
    for i in range(4):
        tempX = x + newX[i]
        tempY = y + newY[i]
 
        if checkMove(n, maze, tempX, tempY, res):
 
            res[tempX][tempY] = 1
            if mazeUtil(n, maze, newX, newY, tempX, tempY, res):
                return True
            res[tempX][tempY] = 0
    return False
 
 
def solveMaze(maze):
    
    res = [[0 for i in range(n)] for i in range(n)]
    res[0][0] = 1
    newX = [-1, 1, 0, 0]
    newY = [0, 0, -1, 1]
 
    if mazeUtil(n, maze, newX, newY, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
    else:
        print("No solution")

m = int(input("What is the value of M?"))
n = int(input("What is the value of N?"))
arr = [[0]*m for _ in range(n)]

for i in range (len(arr)):
    for j in range(n):
        print("What is the value of at?", i , ", ",j)
        num = int(input())
        arr[i][j] = num
        
#print(arr)
solveMaze(arr)