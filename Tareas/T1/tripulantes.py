from abc import ABC, abstractmethod
from parametros import CARGA_EXTRA_CARGUERO

class Tripulantes(ABC):
    def __init__(self, nombre, tipo, años_experiencia):
        self.nombre = nombre
        self.tipo = tipo
        self.experiencia = int(años_experiencia)
        self.efecto_aplicado = False

    @abstractmethod
    def aplicar_efecto():
        pass

class Capitan(Tripulantes):
    def aplicar_efecto(self, barco):
        if self.efecto_aplicado == False:
            if barco.encallado == True:
                barco.encallado = False
                self.efecto_aplicado = True
        return

class Cocinero(Tripulantes):
    def aplicar_efecto(self, mercancia):
        if self.efecto_aplicado == False:
            mercancia.expira = mercancia.expira*2
            self.efecto_aplicado = True
        return

class Carguero(Tripulantes):
    def aplicar_efecto(self, barco):
        if self.efecto_aplicado == False:
            barco.carga_max += CARGA_EXTRA_CARGUERO
        return

class CajaMercancia:
    def __init__(
        self,
        numero_de_lote,
        tipo,
        peso,
        tiempo_expiracion
        ):
        self.lote = int(numero_de_lote)
        self.tipo = tipo
        self.peso = int(peso)
        self.expira = int(tiempo_expiracion)
        self.expirado = False

    def expirar(self, canal):
        if canal.hora > self.expira:
            self.expirado = True