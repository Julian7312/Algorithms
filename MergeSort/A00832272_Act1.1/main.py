#Julian Lawrence Gil Soares - A00832272
#20/8/2022
#Actividad 1.1 Implementación de la técnica de programación "divide y vencerás"

#function recives an array then recursively seperates it and orders it.
def mergeSort(arr):
    if len(arr) > 1:
        
        tempArr1 = arr[:len(arr)//2] #array recives first half of the array
        tempArr2 = arr[len(arr)//2:] #array recives second half of the array
        
        mergeSort(tempArr1)
        mergeSort(tempArr2)
        
        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merged array index
        
        while i < len(tempArr1) and j < len(tempArr2):
            if tempArr1[i] < tempArr2[j]:
                arr[k] = tempArr1[i]
                i += 1
            else:
                arr[k] = tempArr2[j]
                j += 1
            k += 1
        
        while i < len(tempArr1):
            arr[k] = tempArr1[i]
            i += 1
            k += 1
        
        while j < len(tempArr2):
            arr[k] = tempArr2[j]
            j += 1
            k += 1
        
            
            
        return(arr)   
            


length = int(input("What length will the list have? "))
lst = []
middle = (length-1)/2

  
for i in range(0, length):
    ele = int(input())
    lst.append(ele)
    
    final = str(mergeSort(lst))
    
    with open('ListaOrdenada.txt', 'w') as f:
        f.write(final)
      
print(mergeSort(lst))
