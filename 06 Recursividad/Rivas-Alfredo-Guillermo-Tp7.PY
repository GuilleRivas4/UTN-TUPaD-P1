""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario


def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
def mostrar_factorial(n, actual=1):
    if actual > n:
        return
    print(f"{actual}! = {factorial(actual)}")
    mostrar_factorial(n, actual + 1)

limite = int(input("Ingrese un número entero "))
mostrar_factorial(limite)
"""

"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta, actual=0):
    if actual > hasta:
        return
    print(f"Fibonacci({actual}) = {fibonacci(actual)}")
    mostrar_fibonacci(hasta, actual + 1)


posicion = int(input("Ingrese la posición hasta la cual mostrar la serie de Fibonacci: "))
mostrar_fibonacci(posicion)
"""

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula n 𝑚 = n * n(𝑚-1).
Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (número entero positivo): "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")
"""

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


numero = int(input("Ingresá un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
"""