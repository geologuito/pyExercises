
# 1)Escribe un programa muestre por pantalla “Hello World”.

print("Hello World!")

# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.

print(3+5)

# 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”

user_name = input("Ingrese su nombre de Usuario: ")
print("Hello", user_name)

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

# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres. (que pida mas de 2 numeros)

"""
seteo la cantidad de numeros que voy a usar
"""
contador = int(input("cuantos numeros desea ingresar?"))

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