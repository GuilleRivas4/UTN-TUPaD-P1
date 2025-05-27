############################################### Funciones ###############################################

""" 1. 
def imprimir_hola_mundo():
    print("Hola Mundo!") """

""" 2.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!") """

""" 3.
def  informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") """

""" 4.
def calcular_area_circulo(radio):
    print(3.1416 * (radio*radio)) 

def calcular_perimetro_circulo(radio):
    print(2 * 3.1416 * radio)  """

""" 5.
def segundos_a_horas(segundos):
    print(segundos/3600) """

""" 6.
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(numero*i) """

""" 7.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return (suma, resta, multiplicacion, division) """

""" 8.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc """

""" 9.
def celsius_a_fahrenheit(celsius):
    print(f"La temperatura en fahrenheit es: {celsius * 9 / 5 + 32}") """

""" 10.
def calcular_promedio(a, b, c):
    print(f"El promedio de los 3 numeros es: {(a + b + c) / 3}") """

############################################### Programa principal ###############################################

""" 1. 
imprimir_hola_mundo() """

""" 2.
saludar_usuario("Marcos") """

""" 3.
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = int(input("Ingrese su edad"))
residencia = input("Ingrese su residencia")
informacion_personal(nombre,apellido,edad,residencia) """

""" 4.
radio = int(input("Ingrese el radio del circulo"))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio) """

""" 5.
segundos = int(input("Ingrese la cantidad de segundos"))
segundos_a_horas(segundos) """

""" 6. 
numero = int(input("Ingrese un numero para conocer su tabla"))
tabla_multiplicar(numero) """

""" 7.
num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))

resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}") """

""" 8.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su IMC es: {imc:.2f}") """

""" 9.
celsius = int(input("Ingrese la temperatura en celsius "))
celsius_a_fahrenheit(celsius) """

""" 10.
num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

calcular_promedio(num1,num2,num3) """




