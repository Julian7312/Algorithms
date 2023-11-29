#Julian Lawrence Gil Soares
#A00832272
#4/9/2022
#Actividad 1.2 Implementación de la técnica de programación "Programación dinámica" y "algoritmos avaros"

#complejidad: o(logn)
#avaro
def coinCheck(price,total,arr):
    i = 0 #iteration index
    c = 0 #number of coins used
    lst = [] #how many of each coin is used
    while i < len(arr):
        if(total >= arr[i]):
            total = total - arr[i]
            c += 1
        else:
            lst.append(c)
            c = 0
            i += 1

        
    for coin in range(0, len(arr)):
        print(arr[coin]," = ", lst[coin])
            

#complejidad: o(logn)
#dinamico
def coinChecker(price,total,arr):
    lst = [0] * (total + 1) #how many of each coin is used
    lst[0] = 1
    for coin in range(0, (len(arr))):
        for i in range(1, len(lst)):
            if(i >= arr[coin]):
                lst[i] += lst[i-arr[coin]]
            
    print("Number of combinations = ",lst[-1])

coinTotal = int(input("How many types of coins will be used? "))
lst = [] #list of coin values
for coin in range(0, coinTotal):
    coinTotal = int(input("How much is the coin worth? "))
    if coin > 0:
        while(coinTotal > lst[coin - 1]):
            coinTotal = int(input("INVALID Must be in descending values"))
    lst.append(coinTotal)
    
    
price = int(input("What is the total for the product? "))
amountPayed = int(input("How much are you paying for the product? "))

coinCheck(price,amountPayed,lst)
coinChecker(price,amountPayed,lst)
