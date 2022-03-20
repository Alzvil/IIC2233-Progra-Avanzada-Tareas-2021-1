from abc import ABC, abstractmethod
import parametros as p
from objeto import Normales

class Personajes(ABC):
    def __init__(self):
        vida = 1

    @abstractmethod
    def habilidad_especial(self):
        return

class Homero(Personajes):
    def __init__(self):
        super.__init__(self)
        self.velocidad = p.VELOCIDAD_HOMERO
        self.objeto = Normales(sprite = "donas")
        self.objetos_atrapados = 0
        self.lugar = "planta"

    def habilidad_especial(self):
        if self.objetos_atrapados >= 10:
            self.vida += p.PONDERADOR_VIDA_HOMERO
            if self.vida > 1:
                self.vida = 1

    def colision_objeto(self, objeto):
        if objeto.tipo == "normal":
            self.objetos_atrapados += 1
        elif objeto.tipo == "peligroso":
            self.objetos_atrapados = 0
        return

class Lisa(Personajes):
    def __init__(self):
        super.__init__(self)
        self.velocidad = p.VELOCIDAD_LISA
        self.objeto = Normales(sprite = "saxofones")
        self.objetos_atrapados = 0
        self.lugar = "escuela"
    
    def habilidad_especial(self):
        #los objetos duren una cantidad de tiempo PONDERADOR_TIEMPO_LISA mas en pantalla