#Ordenacion burbuja
def bubbleSort (lst):
    n= len(lst)
    for i in range(n):
        for j in range (0, n-1):
            if lst[j] > lst [j+1]:
                lst[j], lst [j+1] = lst[j+1], lst[j]
    return lst

def insertionSort(lst):
    for step in range(1,len(lst)):
        key = lst[step]
    j=step - 1 
    while j >= 0 and key <lst [j]:
        lst [j+1] = lst[j]
        j= j-1
    lst [j+1]= key
    return lst

lst=[1,3,2,5,6,7,8,3,2]
prueba= insertionSort(lst)

print (prueba)

def selectionSort(lst):
    n=len(lst)
    for step in range (n):
        j= step
        for i in range (step + 1, n):
            if lst[i] < lst [j]:
                j=i 
        lst [step], lst[j] = lst [j], lst[step]
        return lst

