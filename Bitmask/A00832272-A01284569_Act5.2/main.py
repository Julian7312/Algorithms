"""
Julian Lawrence Gil Soares
Jose Andres Lozano Alanis
A00832272
A01284569
Complejidad O(N^2)
"""

from collections import defaultdict
  
class Gorra:
  
    def __init__(self):
  
            self.todas_personas = 0
  
            self.total_gorras = 100
  
            self.gorras = defaultdict(list)
  
  
    def contarManerasExtra(self,dp, persona, numero_gorra):
          
        if persona == self.todas_personas:
            return 1
  
        if numero_gorra > self.total_gorras:
            return 0

        if dp[persona][numero_gorra]!= -1 :
            return dp[persona][numero_gorra]

        maneras = self.contarManerasExtra(dp, persona, numero_gorra + 1)

        if numero_gorra in self.gorras:
  
            for ppl in self.gorras[numero_gorra]:

                if persona & (1 << ppl) : continue

                maneras += self.contarManerasExtra(dp, persona | (1 << ppl), numero_gorra + 1) 
  
                maneras = maneras % (10**9 + 7)

        dp[persona][numero_gorra] = maneras
        
        return dp[persona][numero_gorra]
  
  
  
    def countManeras(self,N):

        for ppl in range(N):
  
            gorras_por_persona = map(int, input().strip().split())
  
            for i in gorras_por_persona:
  
                self.gorras[i].append(ppl)

        self.todas_personas = (1 << N) -1

        dp = [[-1 for j in range(self.total_gorras + 1)] for i in range(2 ** N)]
  
        print(self.contarManerasExtra(dp, 0, 1,))
  
def main():
    n = int(input("Introduzca el número de personas con gorra: "))
    while(n < 1 or n > 10):
        n = int(input("\nError, favor de ingresar un valor mayor a 1 y menor a 10\n"))
    Gorra().countManeras(n)
  
  
if __name__ == '__main__':
    main()

