# Este código iría en test_operaciones.py

from src._02operaciones import sumar, restar, multiplicar, dividir, concatenar, longitud, a_mayusculas, a_minusculas

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 2) == 3

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(8, 2) == 4
    assert dividir(5, 0) == "Error: División por cero."

def test_concatenar():
    assert concatenar("Hola ", "Mundo") == "Hola Mundo"

def test_longitud():
    assert longitud("Python") == 6

def test_a_mayusculas():
    assert a_mayusculas("python") == "PYTHON"

def test_a_minusculas():
    assert a_minusculas("PYTHON") == "python"
