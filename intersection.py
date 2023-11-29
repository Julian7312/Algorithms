#Julian Lawrence Gil Soares
#A00832272
#4/9/2022
#Actividad 4.1 Implementación Intersección y proximidad aplicando geometría computacional."
  
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
def onLine(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
  
def orientation(p, q, r):
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):

        return 1
    elif (val < 0):

        return 2
    else:

        return 0

def doIntersect(x1,y1,x2,y2):
      
    o1 = orientation(x1, y1, x2)
    o2 = orientation(x1, y1, y2)
    o3 = orientation(x2, y2, x1)
    o4 = orientation(x2, y2, y1)

    if ((o1 != o2) and (o3 != o4)):
        return True
    
    if ((o1 == 0) and onLine(x1, x2, y1)):
        return True

    if ((o2 == 0) and onLine(x1, y2, y1)):
        return True

    if ((o3 == 0) and onLine(x2, x1, y2)):
        return True

    if ((o4 == 0) and onLine(x2, y1, y2)):
        return True
  
    return False
  
n = int(input("Cuantos conjuntos se analizaran?"))


if(n % 4 != 0):
    while(n % 4 != 0):
        n = int(input("Cuantos conjuntos se analizaran?"))
        
lst = [True] * int(n/4)
print(lst)

for i in range (int(n / 4)):
    #first line
    print("First line")
    print("Introduce valor de la coordenada x")
    numX = int(input())
    print("Introduce valor de la coordenada y")
    numY = int(input())
    
    x1 = Point(numX, numY)
    
    print("Introduce valor de la coordenada x")
    numX = int(input())
    print("Introduce valor de la coordenada y")
    numY = int(input())
    
    y1 = Point(numX, numY)
    
    #second line
    print("Second line")
    print("Introduce valor de la coordenada x")
    numX = int(input())
    print("Introduce valor de la coordenada y")
    numY = int(input())
    
    x2 = Point(numX, numY)
    
    print("Introduce valor de la coordenada x")
    numX = int(input())
    print("Introduce valor de la coordenada y")
    numY = int(input())
    
    y2 = Point(numX, numY)

    
    if doIntersect(x1, y1, x2, y2):
        lst[i] = True
    else:
        lst[i] = False
    
    
print(lst)
    