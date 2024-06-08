""" 
    13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente 
    forma:
    1
    22
    333
    4444
    55555
    666666
    ………
"""
#como en el ejercicio 14 pide que el usuario ingrese un numero ya vamos a hacerlo aca.
#por lo tanto no se imprimiran 30 numeros sino que se imprimiran la cantidad de numeros que se indiquen.
#para imprimir 30 solo hay que cambiar el rango desde 0 hasta 31
rango = int(input("ingrese un numero entero positivo: "))

for i in range(0,rango+1):
    numero = i
    for j in range (0,i):
        print(f"{numero:02}",end=' ')
    print()

""" 
    14) Haz un programa que escriba una pirámide inversa de los números del 1 al 
    número que indique el usuario de la siguiente forma (suponiendo que indica 6):
    666666
    55555
    4444
    333
    22
    1 
"""

for i in range(rango,0,-1):
    numero = i
    for j in range (0,i):
        print(f"{numero:02}",end=' ')
    print()