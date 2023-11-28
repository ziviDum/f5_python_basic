# listas.py

def agregar_elemento(lista, elemento):
    """
    Agrega un elemento al final de la lista.
    """
    lista.append(elemento)
    return lista

def eliminar_elemento(lista, elemento):
    """
    Elimina el primer elemento igual al proporcionado de la lista.
    Si el elemento no está en la lista, devuelve la lista original.
    """
    if elemento in lista:
        lista.remove(elemento)
    return lista

def obtener_elemento(lista, indice):
    """
    Devuelve el elemento de la lista en la posición índice.
    Si el índice está fuera de rango, devuelve None.
    """
    if 0 <= indice < len(lista):
        return lista[indice]
    else:
        return None

def concatenar_listas(lista1, lista2):
    """
    Devuelve una nueva lista que es la concatenación de lista1 y lista2.
    """
    return lista1 + lista2
