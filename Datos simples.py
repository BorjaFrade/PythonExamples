# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
cadena = "¡Hola Mundo!"
print(cadena)

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
print("introduzca su nombre: ")
nombre = input()
print("¡Hola " + nombre +"!")

# Ejercicio 4
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
print("introduzca su nombre: ")
nombre = input()
print("Introduzca un número: ")
numero = int(input())

for x in range(numero):
    print(nombre)

# Ejercicio 5
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
print("Introduzca su nombre: ")
nombre = input()
print(nombre, "tiene ", len(nombre), " letras")

# Ejercicio 6
# Escribir un programa que realice la siguiente operación aritmética .
print( ((3+2)/(2*5))**2)

# Ejercicio 7
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
print("Número de horas trabajadas: ")
numero = float(input())
print("Coste horario: ")
coste = float(input())
print("Coste total ", coste * numero)

# Ejercicio 8
# Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los
#primeros enteros positivos puede ser calculada de la siguiente forma:
print("Introduzca número: ")
numero = int(input())
print("Suma ", 0.5*numero*(numero+1))

# Ejercicio 9
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
print("Introduzca masa: ")
masa = float(input())
print("Introduzca altura: ")
altura = float(input())
imc =round( masa / (altura**2), 2)
print("Índice de masa: ", imc)

# Ejercicio 10

# Ejercicio 11

# Ejercicio 12

# Ejercicio 13

# Ejercicio 14

# Ejercicio 15
