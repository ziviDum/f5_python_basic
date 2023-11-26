
from src._01variables_tipos_test import obtener_entero, obtener_flotante, obtener_cadena, obtener_booleano


def test_obtener_entero():
    assert type(obtener_entero()) is int

def test_obtener_flotante():
    assert type(obtener_flotante()) is float

def test_obtener_cadena():
    assert type(obtener_cadena()) is str

def test_obtener_booleano():
    assert type(obtener_booleano()) in [bool, int]  # True/False son subtipos de int en Python
