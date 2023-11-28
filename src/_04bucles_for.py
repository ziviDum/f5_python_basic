"""
Ejercicios de bucles for.
"""

def suma_numeros(lista_numeros):
    """
    Devuelve la suma de todos los números en una lista.
    """
    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma

def producto_numeros(lista_numeros):
    """
    Devuelve el producto de todos los números en una lista.
    Si la lista está vacía, devuelve 1.
    """
    producto = 1
    for numero in lista_numeros:
        producto *= numero
    return producto

def contar_ocurrencias(lista_items, item_buscado):
    """
    Cuenta cuántas veces aparece un item en una lista.
    """
    contador = 0
    for item in lista_items:
        if item == item_buscado:
            contador += 1
    return contador

def crear_lista_cuadrados(n):
    """
    Dada una lista de números hasta n, devuelve una lista de los cuadrados de esos números.
    """
    cuadrados = []
    for numero in range(1, n + 1):
        cuadrados.append(numero ** 2)
    return cuadrados
