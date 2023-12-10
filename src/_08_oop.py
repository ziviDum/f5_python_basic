import math
# Ejercicios de POO en Python

# Ejercicio 1: Clase Libro
# Crea una clase `Libro` que tenga dos atributos: `titulo` y `autor`.
# Además, debe tener un método `mostrar_informacion` que imprima "Título: [titulo], Autor: [autor]".

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

# Ejercicio 2: Herencia
# Crea una clase `Vehiculo` con atributos `marca` y `modelo`.
# Luego crea una clase `Coche` que herede de `Vehiculo` y añade un atributo `cilindrada`.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

# Ejercicio 3: Encapsulación
# Crea una clase CuentaBancaria que tenga dos atributos privados:
# _saldo y _titular. Implementa métodos para depositar y retirar dinero, 
# además de un método para ver el saldo actual.
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

    def ver_saldo(self):
        return self._saldo

# Ejercicio 4: Polimorfismo
# Crea una clase base Forma con un método area. Luego, crea dos clases derivadas, 
# Circulo y Cuadrado, que implementen el método area.
class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2