#  1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

""" edad = int(input("Por favor ingrese su edad"))
if edad > 18:
    print("Es mayor de edad") """

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

""" nota = int(input("Ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado") """

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

""" numero = int(input("Ingrese un numero par"))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par") """

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años. """

""" edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Usted pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoria Adolecente")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoria Adulto/a joven")
else:
    print("Usted pertenece a la categoria Adulto/a") """

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

""" contraseña = input("Introduzca una contraseña de entre 8 y 14 caracteres")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") """

""" from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(media)
print(mediana)
print(moda)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo") """

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

""" string = input("Ingrese una frase o una palabra")

if string[-1] == "a" or string[-1] == "e" or string[-1] == "i" or string[-1] == "o" or string[-1] == "u":
    print(string + "!")
else:
    print(string) """

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

""" nombre = input("Por favor ingrese su nombre")
opcion = int(input("Por favor ingrese un numero para seleccionar una opcion: 1 - Si quiere su nombre en mayúsculas. 2 - Si quiere su nombre en minúsculas. 3 - Si quiere su nombre con la primera letra mayúscula."))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Ingrese una opcion valida") """

""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

""" escala = float(input("Ingrese la magnitud del terremoto en escala de Richter"))

if escala < 3:
    print(" Muy leve (imperceptible) ")
elif escala >= 3 and escala < 4:
    print("Leve (ligeramente perceptible)")
elif escala >= 4 and escala < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif escala >= 5 and escala < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif escala >= 6 and escala < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)") """

""" 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
Periodo del año                                     Estación en el hemisferio norte                         Estación en el hemisferio sur
Desde el 21 de diciembre hasta el 20 de
marzo (incluidos)                                           Invierno                                                        Verano
Desde el 21 de marzo hasta el 20 de junio
(incluidos)                                                 Primavera                                                       Otoño
Desde el 21 de junio hasta el 20 de
septiembre (incluidos)                                      Verano                                                          Invierno
Desde el 21 de septiembre hasta el 20 de
diciembre (incluidos)                                       Otoño                                                           Primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. """

""" mes = (input("Ingrese el mes en curso"))
dia = int(input("Ingrese el numero de día en curso"))
hemisferio = (input("Ingrese 'N' si esta en el hemisferio Norte - ingrese 'S' si se encuentra en el hemisferio Sur"))

if (mes.lower() == "diciembre" and dia >= 21) or mes.lower() == "enero" or mes.lower() == "febrero" or (mes.lower() == "marzo" and dia <= 20):
    if hemisferio.upper() == "N":
        print("La estacion actual es invierno")
    else:
        print("La estacion actual es verano")
elif (mes.lower() == "marzo" and dia >= 21) or mes.lower() == "abril" or mes.lower() == "mayo" or (mes.lower() == "junio" and dia <= 20):
    if hemisferio.upper() == "N":
        print("La estacion actual es primavera")
    else:
        print("La estacion actual es otoño")
elif (mes.lower() == "junio" and dia >= 21) or mes.lower() == "julio" or mes.lower() == "agosto" or (mes.lower() == "septiembre" and dia <= 20):
    if hemisferio.upper() == "N":
        print("La estacion actual es verano")
    else:
        print("La estacion actual es invierno")
elif (mes.lower() == "septiembre" and dia >= 21) or mes.lower() == "octubre" or mes.lower() == "novimebre" or (mes.lower() == "diciembre" and dia <= 20):
    if hemisferio.upper() == "N":
        print("La estacion actual es otoño")
    else:
        print("La estacion actual es primavera")
else:
    print("Ingrese un valor valido") """