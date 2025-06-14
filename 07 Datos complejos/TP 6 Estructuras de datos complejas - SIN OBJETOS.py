""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800


precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

frutas = list(precios_frutas.keys())
print(frutas)
"""

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe

agenda_telefonica = {}
for i in range(1,6):
    nombre = input("Ingrese el nombre que quiera agendar ")
    telefono = input("Ingrese el número que quiera agendar ")
    agenda_telefonica[nombre] = telefono

nombre_consultado = input("Ingrese un nombre para buscar en la agenda ")
if nombre_consultado in agenda_telefonica:
    print(f"El numero de la persona es: {agenda_telefonica[nombre_consultado]}")
else:
    print("La persona no se encuentra en la agenda")
"""

""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.


frase = input("Ingresá una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas: ", palabras_unicas)

cantidad_palabra= {}
for palabra in palabras:
    if palabra in cantidad_palabra:
        cantidad_palabra[palabra] +=1
    else:
        cantidad_palabra[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
for palabra, cantidad in cantidad_palabra.items():
    print(f"{palabra}: {cantidad}")
"""

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:
alumnos = {
"Sofia": (10,9,8)
"Luis": (6,7,7)
}


alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    notas = input(f"Ingresá 3 notas para {nombre}: ")

    lista_notas = list(map(int, notas.split()))

    alumnos[nombre] = tuple(lista_notas)

print("Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
"""

""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {"Ana", "Luis", "María", "Pedro", "Sofía"}
parcial2 = {"Pedro", "Sofía", "Julián", "Marta", "Laura"}

ambos = parcial1.intersection(parcial2)

solo_uno = parcial1.symmetric_difference(parcial2)

al_menos_uno = parcial1.union(parcial2)

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los parciales:", solo_uno)
print("Aprobaron al menos uno de los parciales:", al_menos_uno)
"""

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe. 

stock_productos = {
    "manzana": 50,
    "banana": 30,
    "naranja": 20,
    "pera": 15,
    "uva": 40
}

while True:
    accion = input("\n¿Qué querés hacer? (consultar/agregar/salir): ").lower()

    if accion == "salir":
        print("¡Hasta luego!")
        break

    elif accion == "consultar":
        producto = input("Ingresá el nombre del producto a consultar: ").lower()
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]} unidades.")
        else:
            print(f"El producto {producto} no existe en el stock.")

    elif accion == "agregar":
        producto = input("Ingresá el nombre del producto para agregar stock: ").lower()
        cantidad = int(input("Ingresá la cantidad a agregar: "))

        if producto in stock_productos:
            stock_productos[producto] += cantidad
            print(f"Se agregaron {cantidad} unidades a {producto}. Stock actual: {stock_productos[producto]}")
        else:
            stock_productos[producto] = cantidad
            print(f"Producto nuevo agregado: {producto} con stock {cantidad} unidades.")

    else:
        print("Acción no válida. Por favor, ingresá 'consultar', 'agregar' o 'salir'.")

"""

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("Lunes", "10:00") : "Reunion",
    ("Martes", "15:00") : "Clases", 
    ("Miercoles", "09:00") : "Desayuno", 
    ("Jueves", "11:00") : "Llamada",
    ("Viernes", "19:00") : "Gimnasio" 
}

print("Agenda semanal:")
for (dia,hora), evento in agenda.items():
    print(f"{dia} a las {hora} : {evento}")
"""
""" 
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores 

original = {"Argentina":"Buenos Aires", "Chile":"Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario original")
print(original)
print("Diccionario invertido:")
print(invertido)
"""


