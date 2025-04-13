# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

""" for i in range (101) :
    print(i) """

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

""" numero = int(input("Ingrese un numero"))
cantidadDigitos = len(str(numero))
print("La cantidad de digitos es: ", cantidadDigitos) """

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

""" valorInicial = int(input("Ingrese el valor inicial de la suma"))
valorFinal = int(input("Ingrese el valor final de la suma"))
sumaValores = 0

for i in range (valorInicial+1, valorFinal):
    sumaValores += i

print("La suma de los numeros entre los dos valores otorgados es: ", sumaValores) """

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

""" numeroUsuario = int(input("Ingrese un numero entero |Ingrese 0 para detener el programa| "))
suma = 0

while numeroUsuario != 0:
    suma += numeroUsuario
    numeroUsuario = int(input("Ingrese otro numero entero |Ingrese 0 para detener el programa| "))

if suma == 0:
    print("Usted no ingreso ningun numero")
else:
    print("La suma de los numeros ingresados es: ", suma) """

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

""" import random

numeroAleatorio = random.randint(1, 9)
intentos = 0
numeroUsuario = int(input("Ingrese un numero"))
intentos += 1

while numeroUsuario != numeroAleatorio :
    print("No acertaste al numero aleatorio")
    intentos += 1
    numeroUsuario = int(input("Ingrese otro numero"))

print(f"Acertaste al numero aleatorio en {intentos} intentos") """

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

""" for i in range (100, 0, -2):
    print(i) """

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

""" numeroUsuario = int(input("Ingrese un número entero positivo"))
suma = 0

if numeroUsuario > 0:
    for i in range (0, numeroUsuario):
        suma += i
else:
    print("Usted no ingreso un número entero positivo")

print(f"La suma de todos los números entre 0 y {numeroUsuario} es {suma}") """

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

""" sonPares = 0
sonImpares = 0
sonPositivos = 0
sonNegativos = 0

for i in range (100):
    numeroUsuario = int(input("Ingrese un numero"))
    if numeroUsuario % 2 == 0:
        sonPares += 1
    else:
        sonImpares +=1
    if numeroUsuario > 0:
        sonPositivos += 1
    else:
        sonNegativos += 1

print(f"La cantidad de numeros pares ingresados fue de :{sonPares}")
print(f"La cantidad de numeros impares ingresados fue de :{sonImpares}")
print(f"La cantidad de numeros positivos ingresados fue de :{sonPositivos}")
print(f"La cantidad de numeros negativos ingresados fue de :{sonNegativos}") """

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

""" suma = 0

for i in range (100):
    numeroUsuario = int(input("Ingrese un numero"))
    suma += numeroUsuario

print(f"La media de los numeros ingresados es: {suma / 100}") """

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

""" numero = int(input("Ingresa un número entero"))
numero_invertido = 0

while numero != 0:
    digito = numero % 10                
    numero_invertido = (numero_invertido * 10) + digito
    numero = numero // 10    

print(f"Número invertido: {numero_invertido}") """