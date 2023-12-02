# diccionarios.py

def agregar_par_clave_valor(diccionario, clave, valor):
    """
    Agrega un par clave-valor al diccionario.
    """
    diccionario[clave] = valor
    return diccionario

def eliminar_par_clave_valor(diccionario, clave):
    """
    Elimina el par clave-valor del diccionario usando la clave.
    Si la clave no existe, devuelve el diccionario sin cambios.
    """
    diccionario.pop(clave, None)
    return diccionario

def obtener_valor(diccionario, clave):
    """
    Devuelve el valor asociado con la clave en el diccionario.
    Si la clave no existe, devuelve None.
    """
    return diccionario.get(clave)

def combinar_diccionarios(diccionario1, diccionario2):
    """
    Combina dos diccionarios en uno nuevo y lo devuelve.
    Si hay claves duplicadas, los valores de diccionario2 prevalecerán.
    """
    nuevo_diccionario = diccionario1.copy()
    nuevo_diccionario.update(diccionario2)
    return nuevo_diccionario
