n = int(input("What is the value of n?")) #number of vertices
INF = 999 #value asigned if there is no conection between two nodes

def floyd(G):
    arr2 = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr2[i][j] = min(arr2[i][j], arr2[i][k] + arr2[k][j])
    print_solution(arr2)

def print_solution(arr2):
    for i in range(n):
        for j in range(n):
            if(arr2[i][j] == INF):
                print("-1", end=" ")
            else:
                print(arr2[i][j], end="  ")
        print(" ")


arr = [[0]*n for _ in range(n)]

for i in range (len(arr)):
    for j in range(n):
        print("What is the value of at?", i , ", ",j)
        num = int(input())
        if(num == -1):
            num = INF
        arr[i][j] = num
        
print(arr)

floyd(arr)