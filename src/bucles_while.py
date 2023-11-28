# bucles_while.py

def encontrar_primer_negativo(lista_numeros):
    """
    Devuelve el primer número negativo en la lista.
    Si no hay negativos, devuelve None.
    """
    i = 0
    while i < len(lista_numeros):
        if lista_numeros[i] < 0:
            return lista_numeros[i]
        i += 1
    return None

def cuenta_regresiva(n):
    """
    Crea una cuenta regresiva desde n hasta 0.
    Devuelve una lista con la cuenta regresiva.
    """
    cuenta_regresiva = []
    while n >= 0:
        cuenta_regresiva.append(n)
        print(n)
        n -= 1
    return cuenta_regresiva

def sumar_hasta_limite(limite):
    """
    Suma números consecutivos desde 0 y devuelve la suma total
    justo antes de que esta suma sobrepase el límite.
    """
    total = 0
    numero = 1
    while total + numero <= limite:
        total += numero
        numero += 1
    return total
