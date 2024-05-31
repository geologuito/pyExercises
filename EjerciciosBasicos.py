#importaciones que uso para limpiar la consola luego de unos segundos
import time
import os

# 1)Escribe un programa muestre por pantalla “Hello World”.

print("Hello World!")

# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.

print(3+5)

# 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”

user_name = input("Ingrese su nombre de Usuario: ")
print("Hello", user_name)

time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Comando para Windows
else :
    os.system('clear')  # Comando para Unix/Linux/Mac

# 4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números

num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese otro numero: "))
print(num1,"+",num2,"=",num1+num2)


# 5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor. (usaremos los 2 numeros que ya pedimos)

if num1 == num2 :
    print("los numeros son iguales")
elif num1 > num2:
    print(num1,"es mayor que",num2)
else :
    print(num2,"es mayor que",num1) 

time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Comando para Windows
else :
    os.system('clear')  # Comando para Unix/Linux/Mac

# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres. (haremos que pida varios numeros)

"""
    seteo la cantidad de numeros que voy a usar
"""
contador = int(input("¿cuantos numeros desea ingresar?"))

"""
    validamos que se ingrese al menos 1 numero
"""
if contador <= 0:
    print("ingrese por lo menos un numero")
else :

    """
        creo una lista vacia para almacenar los numeros
    """
    numeros = []

    """
        utilizo un for para iterar sobre la cantidad de numeros que setie previamente y asi agregar cada numero a la lista.
        la letra 'f' antes de un string formatea la cadena de texto para que nos permita colocar expresiones dentro de {expresion}.
    """
    for i in range(contador):
        elemento = float(input(f"ingrese el {i + 1} numero: "))
        numeros.append(elemento)

    """
        guardo el primer valor de la lista en una variable
    """
    mayor = numeros [0]

    """
        itero sobre la lista y comparo cada elemento con mi variable,
        si el valor del elemento es mayor que el mi variable entonces, guardo este valor en la misma 
    """
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    print(f"en la siguiente lista: {numeros} el numero {mayor} es el mayor")

    #7) Escribe un programa que pida un número y diga si es divisible por 2
    # (esta pregunta esta mal formulada pero basicamente lo que nos pide es que busquemos los numeros pares)
    # para este programa usaremos la lista del punto anterior ( numeros = [] )

    """ for numero in numeros:
        if numero % 2 == 0:
            print(f"el numero {numero} es par") """

    #8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
    # similar al anterior por lo tanto dejare comentado el ejercicio de arriba y lo hare nuevamente.

    #itero sobre mi lista de numeros
    for numero in numeros:

        divisor = None #inicializo una variable para almacenar el divisor

        #busco si el numero es divisible por alguno de los 4 numeros
        if numero % 2 == 0:
            divisor = 2
        elif numero % 3 == 0:
            divisor = 3
        elif numero % 5 == 0:
            divisor = 5
        elif numero % 7 == 0:
            divisor = 7

        #imprimo el mensaje
        if divisor is not None:
            print(f"el numero {numero} es divisible por {divisor}")
        else :
            print(f"el numero {numero} no es divisible por 2, 3, 5 o 7")
    #para checkear todos los casos sugiero agregar 5 numeros a la lista: 4, 9, 25, 49, 11

    time.sleep(3)
    if os.name == 'nt':
        os.system('cls')  # Comando para Windows
    else :
        os.system('clear')  # Comando para Unix/Linux/Mac

    #9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay 
    #   que decir todos por los que es divisible)
        """es lo mismo que el anterior nada mas que divisor ahora sera una lista ademas tendremos 4 if"""
    
    #nuevamente itero sobre mi lista de numeros
    for numero in numeros:

        divisores = [] #inicializo mi lista de divisores vacia

        #busco todos los divisores que me pide el ejercicio, si cumple condicion, agrega el divisor a la lista
        if numero % 2 == 0:
            divisores.append(2)
        if numero % 3 == 0:
            divisores.append(3)
        if numero % 5 == 0:
            divisores.append(5)
        if numero % 7 == 0:
            divisores.append(7)

        #si mi lista tiene al menos 1 elemento entonces imprimo el mensaje de que el numero tiene al menos 1 divisor
        if divisores :
            #mapeo divisores y los convierto en string, luego los uno con join y los separo por comas
            divisores_str = ", ".join(map(str, divisores))
            print(f"el numero {numero} es divisible por {divisores_str}")
        else :
            print(f"el numero {numero} no es divisible por 2, 3, 5 o 7")
#fin del else del punto 6 (linea 58)

# 10) Escribir un programa que escriba en pantalla los divisores de un número dado
import math

while True :
    
    numero = int(input("ingrese un numero entero positivo: ")) #lo convierto a entero por las dudas

    #verifico que se ingrese un numero positivo
    if numero > 0 :
        break

    print("por favor ingrese un numero entero positivo valido")

#calculo la raiz cuadrada de mi numero y la convierto a entero(por las dudas por ej raiz de 28 = 5.29)
raiz = int (math.sqrt(numero))

divisores = []

for i in range(1, raiz+1):
    #verifico si i es divisor de mi numero
    if numero % i == 0 :
        divisores.append(i)

        # Si i * i no es igual a numero (es lo mismo si ponemos i != numero // i), entonces agrego numero // i como divisor
        if i * i != numero :
            divisores.append(numero // i) #nota: hacemos la division entera (//) porque sino / devuelve un float ej: 4 / 2 = 2.0 pero 4 // 2 = 2
        """
            la condicion es para no repetir divisores en el caso que sea un cuadrado perfecto
            por ejemplo si mi numero es 36 -> raiz de 36 = 6 -> 36 // 6 = 6 por lo tanto i * i == numero
            por lo tanto no agregaremos numero // i a la lista ya que sino este estara repetido
            "->" significa "entonces"
        """
#ordeno los divisores
divisores.sort()
#armo un string separado por comas
divisores_str = ", ".join(map(str, divisores))
#imprimo los divisores
print(f"los divisores de {numero} son {divisores_str}")

'''
    y completamos tambien el ejercicio que sigue:
    # 11) Escribir un programa que nos diga si un número dado es primo (no es divisible 
    por ninguno otro número que no sea él mismo o la unidad)
'''

if len(divisores) == 2 : #que pasa? si es == 2 significa que solo es divisible por 1 y por si mismo entonces es primo
    print(f"{numero} es un numero primo")
else :
    print(f"{numero} no es un numero primo")