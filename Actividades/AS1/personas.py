from abc import ABC, abstractmethod
import random


# Completar
class Persona:

    def __init__(self, nombre, edad, contagiado):
        # No modificar
        self.nombre = nombre
        self.edad = edad
        self.contagiado = contagiado

    @abstractmethod
    def saludar(self):
        pass


# Completar
class Cliente(Persona):

    def __init__(self, nombre, edad, contagiado, nombre_local_favorito, dinero):
        Persona.__init__(self, nombre, int(edad), contagiado)
        self.nombre_local_favorito = nombre_local_favorito
        self.dinero = int(dinero)

    def saludar(self):
        # No modificar
        print(f"Hola me llamo {self.nombre} y mi local favorito es {self.nombre_local_favorito}")


# Completar
class Trabajador(Persona):

    def __init__(self, nombre, edad, contagiado, sueldo, nombre_local):
        Persona.__init__(self, nombre, int(edad), contagiado)
        self.sueldo = int(sueldo)
        self.nombre_local = nombre_local

    def generar_posible_contagio(self):
        # No modificar
        probabilidad_contagio = random.uniform(0, 1)
        if probabilidad_contagio < 0.1:
            self.contagiado = True

    def saludar(self):
        # No modificar
        print((
            f"Hola me llamo {self.nombre}, trabajo en {self.nombre_local}"
            f" y mi sueldo es {self.sueldo}"
        ))
