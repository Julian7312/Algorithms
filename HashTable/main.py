#Julian Lawrence Gil Soares
#Jose Andres Lozano Alanis
#A00832272
#A01284569
#09/10/2022
#Actividad 2.1 Implementación de "Hash String""
#complejidad: O(n)

import sys
import codecs

fileI = sys.argv[0]

class HashTable:
    def __init__(self):
         self.mod = 100
         self.table = []
        
    def add(self,key):
        self.table.append(key)
         
    def generateHash(self, text):
        i = 0
    
        while(i < len(text)):
            char = text[i]
            hashT = ord(char)
            self.add(hashT % self.mod)
            i += 1
global N
N = int(input("Introduce un numero entre 16 y 64 que sea un multiplo de 4"))

if((N % 4 != 0) or (N < 16 or N > 64)):
    while((N % 4 != 0) or (N < 16 or N > 64)):
        N = int(input("Introduce un numero entre 16 y 64 que sea un multiplo de 4"))
        
f = open(fileI, "r")
textFile = f.read()
ht = HashTable()
ht.generateHash(textFile)

f.close()

for i in ht.table:
    print(hex(i))

print(ht.table)
