import random
import os
def clear():
    command = 'clear'
    if os.name in ('dos' 'nt'):
        command = 'cls'

    os.system(command)
#1

clear()
decision= 'y' 
while decision == 'y':
    numero = int(input('Ingresa un numero entre 1 y 3;'))
    if numero == 1:
        print ('Uno')
    elif numero == 2:
        print ('Dos')
    elif numero == 3:
        print ('Tres')
    else:
        print ('Error')
    decision= input('Deseas ingresar otro numero? Y/N')
else:
    print ('Fin del programa')

#2
def esPrimo(num):
    for n in range (2,num):
        if num%n ==0:
            print (f'{num} no es primo, {n} es divisor')
            return False
        if n == num-1:
            print (f'{num} Es primo')

A=int(input('Ingresa un valor A'))
B= int(input('Ingresa un valor B'))
while A!=0 or B != 0:
    if A>0 and B>0:
        if A == 0 or B==0:
            print('El programa ha terminado')
            break
        else:
            if A<B:
                for i in range (A,B+1):
                    esPrimo(i)
        A= int(input('Ingresa otro numero'))
        B= int(input('Ingresa'))
        
    else:
        print('Ingresa un numero mayor a 0')
        A= int(input('Ingresa otro numero'))
        B= int(input('Ingresa'))
else:
    print('El programa ha terminado')

#3
numeros=int(input('Ingrese una cantidad de numeros a generar: '))
lista=[]
#Genera y guarda en lista
if numeros >0:
    for i in range(0,numeros):
        lista.append (random.randint(0,100))
#a
print(lista)

#b

primero=int(input('Ingresa un numero para mostrar los primeros M valores: '))
valorM=[]
lenlista= len(lista)
while primero > lenlista:
    primero=int(input(f'Ingresa un numero menor al tamaño de la lista ({lenlista}) : '))
else:
    for i in range(0,primero):
        numerolista=lista[i]
        valorM.append(numerolista)
    print (valorM)

#c
suma=0
for i in (lista):
    if i%2==0:
        suma+= i

print(suma)

#d
lista1=lista 
if lista1.sort(reverse=True)==lista:
    print('La lista se encuentra ordenada en forma descendente')
else:
    print(f'La lista {lista} no se encuentra ordenada de manera descendente.')
print(f'La lista se encuentra ahora ordenada descendentemente {lista1}')
    
#a
lista=[]
count=0
while count<30:
    numero=random.randint(1,1000)
    if numero not in lista:
            lista.append(numero)
            count+=1
    else:
        print('Numero en la lista')
#b
print(lista)

#c

largo=len(lista)
posicion=0
multiplos=[]
cuadrado=[]
for i in lista:
    if i%3==0:
        multiplos.append(i)
        i=i**2
        cuadrado.append(i)
        lista[posicion]=i
        posicion+=1
print (f'Los multiplos hallados son {multiplos} ')
print (f'Los cuadrados son {cuadrado}')
print (lista)
print (len(lista))