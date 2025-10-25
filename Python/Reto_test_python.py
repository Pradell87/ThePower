## Ejercicio 1. Funcion contar_caracteres
print("Ejercicio 1")

def contar_caracteres(cadena):
    return len(cadena)
texto = "Hola mundo"

print(contar_caracteres(texto))

## Ejercicio 2. Función calcular_promedio
print()
print("Ejercicio 2")

def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

numeros = [4, 7, 10, 5]

print(calcular_promedio(numeros))

## Ejercicio 3. Función encontrar_duplicado
print()
print("Ejercicio 3")

def encontrar_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

print(encontrar_duplicado([3, 1, 4, 2, 5, 3, 6]))

## Ejercicio 4. Función enmascarado_datos
print()
print("Ejercicio 4")

def enmascarado_datos(dato):
    cadena = str(dato)
    if len(cadena) <= 4:
        return cadena
    return "#" * (len(cadena) - 4) + cadena[-4:]

print(enmascarado_datos("123456789"))

## Ejercicio 5. Función es_anagrama
print()
print("Ejercicio 5")

def es_anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(es_anagrama("roma", "amor"))

## Ejercicio 6. Función buscar_nombre
print()
print("Ejercicio 6")

def buscar_nombre(lista, nombre):
    if nombre in lista:
        print(f"{nombre} fue encontrado en la lista.")
    else:
        print(f"{nombre} no está en la lista.")

nombres = ["Jaime", "Silvia", "Ana"]

buscar_nombre(nombres, "Anna")

## Ejercicio 7. Función fibonacci
print()
print("Ejercicio 7")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
      

for i in range(5):
    print(fibonacci(i))

## Ejercicio 8. Función encontrar_puesto_empleado
print()
print("Ejercicio 8")

def encontrar_puesto_empleado(nombre_completo, empleados):
    for e in empleados:
        if f"{e['nombre']} {e['apellido']}" == nombre_completo:
            return e['puesto']
    return f"{nombre_completo} no trabaja aquí."

empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]

print(encontrar_puesto_empleado("Mabel García", empleados))
print(encontrar_puesto_empleado("Pedro Pérez", empleados))

## Ejercicio 9. Función cubo_numero usando lambdas
print()
print("Ejercicio 9")

cubo_numero = lambda x: x ** 3

print(cubo_numero(3))

## Ejercicio 10. Función resto_division usando lambdas
print()
print("Ejercicio 10")

resto_division = lambda x, y: x % y

print(resto_division(8, 4))

## Ejercicio 11. Función numeros_pares usando lambdas y filter
print()
print("Ejercicio 11")

lista_numeros = [24, 56, 2.3, 19, -1, 0]

numeros_pares = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lista_numeros))

print(numeros_pares)

## Ejercicio 12. Función numeros_suma usando lambdas y map
print()
print("Ejercicio 12")

lista_numeros = [24, 56, 2.3, 19, -1, 0]

numeros_suma = list(map(lambda x: x + 3, lista_numeros))

print(numeros_suma)

## Ejercicio 13. Función sumar_listas usando lambdas
print()
print("Ejercicio 13")

lista_numeros_1 = [1, 4, 5, 6, 7, 7]
lista_numeros_2 = [3, 11, 34, 56]

sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1[:len(l2)], l2))

print(sumar_listas(lista_numeros_1, lista_numeros_2))

## Ejercicio 14. No te vayas por las ramas
print()
print("Ejercicio 14")

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        if 1 <= posicion <= len(self.ramas):
            del self.ramas[posicion - 1]

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas[:]
        }

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)

print(arbol.info_arbol())

## Ejercicio 15. Clase UsuarioBanco
print()
print("Ejercicio 15")

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= otro_usuario.saldo:
            otro_usuario.saldo -= cantidad
            self.saldo += cantidad
        else:
            print(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

alicia.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)

print(f"Alicia: {alicia.saldo}")
print(f"Bob: {bob.saldo}")


## Ejercicio 16. Función procesar_texto
print()
print("Ejercicio 16")

def contar_palabras(texto):
    palabras = texto.lower().replace('.', '').split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    return texto.replace(palabra, '').replace('  ', ' ').strip()

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        return "Opción no válida."

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "texto", "relato"))
print(procesar_texto(texto, "eliminar", "ejemplo"))
