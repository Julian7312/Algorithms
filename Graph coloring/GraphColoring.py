"""
Julian Lawrence Gil Soares
Jose Andres Lozano Alanis
A00832272
A01284569
complejidad O(N^2)
"""

def buildNode(adjacent, v, w):
      
    adjacent[v].append(w)
    #adjacent[w].append(v)  
    return adjacent
  

def color(adjacent, V):
      
    result = [-1] * V
    result[0] = 0;
    check = [False] * V
  
    for u in range(1, V):
        for i in adjacent[u]:
            if (result[i] != -1):
                check[result[i]] = True
  
        cr = 0
        while cr < V:
            if (check[cr] == False):
                break
              
            cr += 1
              
        result[u] = cr 
  
        for i in adjacent[u]:
            if (result[i] != -1):
                check[result[i]] = False

    for u in range(V):
        print("Node: ", u, " , Assigned Color: ", result[u])
  


n = int(input("How many nodes will the graph have?\n"))  
garph = [[] for i in range(n)]
arr = [[0]*n for _ in range(n)]
print(garph)

for i in range (len(arr)):
    for j in range(n):
        print("What is the value of at?", i , ", ",j)
        num = int(input())
        arr[i][j] = num
        
for i in range (len(arr)):
    for j in range(n):
        if(arr[i][j] == 1 ):
            garph = buildNode(garph, i, j)

#print(garph)
color(garph, 5)
  

