from abc import ABC, abstractmethod

class Objeto(ABC):
    def __init__(self):
        pass

class Normales(Objeto):
    def __init__(self, *args, *kwargs):
        super.__init__(self)
        self.tipo = "normal"
        self.sprite = sprite

class Buenos(Objeto):
    def __init__(self):
        super.__init__(self)
        self.tipo = "bueno"
        self.sprite = "vida"

class Peligrosos(Objeto):
    def __init__(self):
        super.__init__(self)
        self.tipo = "peligroso"
        self.sprite = "veneno"