#Clase 2 
#Listas anidadas - Diccionarios
#Ejemplo
#Hacer una funcion para buscar el DNI
import os
def clear():
    command='clear'
    if os.name in ('nt', 'dos'):
        command= 'cls'
    os.system(command)
alumnos=[]
def itdni():
    clear()
    dnibuscar= input('Ingrese un numero de documento: \n Presiona 0 para terminar: ')
    if dnibuscar== '0':
        print('Fin del programa')
    else:
        while len(dnibuscar)!=8:
            dnibuscar= input('Ingresa un DNI valido \n Presiona 0 para terminar: ')
            if dnibuscar== '0':
                print('Fin del programa')
                break
        while str.isdigit(dnibuscar) == False:
            dnibuscar=input('Ingresa un NUMERO de DNI\n Presiona 0 para terminar: ')
            if dnibuscar== '0':
                print('Fin del programa')
                break    
        else: 
            dnibuscar=int(dnibuscar)
            return dnibuscar
def registro():
    clear()
    dni='1'
    while dni!= '0':
        clear()
        alumno=[]
        dni= input('Ingrese un numero de documento: \n Presiona 0 para terminar: ')
        if dni == '0':
            print ('Fin del programa')
            break
        else:
            while len(dni)!=8:
                dni= input('Ingresa un DNI valido \n Presiona 0 para terminar: ')
            while str.isdigit(dni) == False:
                dni=input('Ingresa un NUMERO de DNI')
            else:
                dni=int(dni)
            alumno.append(dni)
        nombre= input('Ingrese nombre del alumno')
        alumno.append(nombre)

        nota= float(input('Ingrese la nota del alumno'))
        while nota > 10 or nota < 0:
            nota = float(input('Ingresa una nota valida'))
            
        else:
            alumno.append(nota)
        alumnos.append(alumno)

def mostrarAlumnos(alumnos):
    print (f'''---Nombre---  ---Nota---''')
    for i in alumnos:
        print (f'{i[1]}, {i[2]}')

def buscarAlumno():
    clear()
    dnibuscar=itdni()
    for i in alumnos:
        if i[0]==dnibuscar:
            print (f'El alumno es {i[1]}, y su nota es  {i[2]}')
            break
    else:
        print('El alumno no se encuentra registrado')

def modificar():
    clear()
    dnibuscar= itdni()
    for i in alumnos:
        if i[0]==dnibuscar:
            print(f'''
            1. Modificar nombre
            2. Modificar nota''')
            opcion=int(input('Ingresa la opcion que deseas'))
            if opcion == 1:
                i[1]= input('Ingresa el nuevo nombre del alumno')
            elif opcion == 2:
                i[2]= int(input('Ingresa la nueva nota del alumno '))
            else:
                print('La opcion ingresada no es correcta')
            break
        else:
            print('El alumno no se encuentra registrado')

def eliminar():
    clear()
    dnibuscar=itdni()
    for i in alumnos:
        cont=0
        if i[0] == dnibuscar:
            alumnos.pop(cont)
            print('El alumno se ha eliminado correctamente')
        else:
            cont+=1
        
    print(alumnos)

def promedio():
    clear()
    suma=0
    contador=0
    for i in alumnos:
        print (i[2])
        suma+=i[2]
        contador+=1
        print (suma,contador)
    if contador !=0:
        promedio = suma/contador
        print (f'El promedio de las notas es de {promedio}')
    else:
        print('No se puede realizar la division por 0. ')





#Registra alumnos

opcion=0

while opcion != 7:
    clear()
    print (f'''Bienvenido al registro de alumnos de la UNJu
Opcion 1: Registrar Alumnos
Opcion 2: Mostrar el listado de alumnos y sus notas
Opcion 3: Buscar alumnos
Opcion 4: Modificar datos
Opcion 5: Eliminar alumno
Opcion 6: Mostrar promedio
Opcion 7: Salir del programa''')
    opcion= int(input('Ingresa una opcion'))
    if opcion == 1:
        registro()
        clear()
    elif opcion == 2:
        clear()
        mostrarAlumnos(alumnos)
        input('Presionar Enter para continuar')
    elif opcion == 3:
        clear()
        buscarAlumno()
        input('Presionar Enter para continuar')
    elif opcion == 4:
        clear()
        modificar()
        input('Presionar Enter para continuar')
    elif opcion == 5:
        clear()
        eliminar()
        input('Presionar Enter para continuar')
    elif opcion == 6:
        clear()
        promedio()
        input('Presionar Enter para continuar')
    elif opcion == 7:
        print ('Fin del programa')
        break

