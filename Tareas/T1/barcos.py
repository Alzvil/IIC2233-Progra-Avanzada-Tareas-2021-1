from abc import ABC, abstractmethod

class Barcos(ABC):
    def __init__(
        self,
        nombre, 
        tipo,
        costo_mantencion, 
        velocidad_base, 
        pasajeros, 
        carga_maxima, 
        moneda_origen, 
        tripulacion,
        mercancia
        ):
        self.nombre = nombre
        self.tipo = tipo
        self.mantencion = float(costo_mantencion)
        self.velocidad = int(velocidad_base)
        self.pasajeros = int(pasajeros)
        self.carga_max = int(carga_maxima)
        self.moneda = moneda_origen
        self.tripulacion = tripulacion
        self.mercancia = mercancia
        self.ocurrio_evento = False
        self.encallado = False
        self.posicion = 0

    @property
    def peso_mercancia(self):
        return self.peso_total
    @peso_mercancia.setter
    def peso_mercancia(self, suma):
        for e in self.mercancia:
            suma += e.peso
        self.peso_total = suma

    @property
    def años_exp(self):
        return self.experiencia
    @años_exp.setter
    def años_exp(self, suma):
        for e in self.tripulacion:
            suma += e.experiencia
        self.experiencia = suma

    def desplazarse(self):
        self.posicion += max(0.1, min(1, \
            (self.carga_max - self.peso_mercancia - 0.3 * self.pasajeros) / \
            self.carga_max)) * self.velocidad

    def efecto_capitan():
        pass

    @property
    def prob_encallar(self):
        return self.encallar
    @prob_encallar.setter
    def prob_encallar(self, valores):
        tendencia_encallar, ponderador_canal = valores[0], valores[1]
        self.años_exp = 0
        self.peso_mercancia = 0
        self.encallar = min(1, (self.velocidad + self.peso_mercancia - self.años_exp) / 120) \
            * tendencia_encallar * ponderador_canal

    def ejecutar_evento_especial():
        pass
    
class BarcoPasajeros(Barcos):
    def __init(
        self,
        nombre, 
        costo_mantencion, 
        velocidad_base, 
        pasajeros, 
        carga_maxima, 
        moneda_origen, 
        tripulacion,
        mercancia
        ):
        super().init(
            nombre, 
            costo_mantencion, 
            velocidad_base, 
            pasajeros, 
            carga_maxima, 
            moneda_origen,  
            tripulacion,
            mercancia
            )

    def ejecutar_evento_especial():
        pass

class BarcoCarguero(Barcos):
    def __init(
        self,
        nombre, 
        costo_mantencion, 
        velocidad_base, 
        pasajeros, 
        carga_maxima, 
        moneda_origen, 
        tripulacion,
        mercancia
        ):
        super().init(
            nombre, 
            costo_mantencion, 
            velocidad_base, 
            pasajeros, 
            carga_maxima, 
            moneda_origen, 
            tripulacion,
            mercancia
            )

    def ejecutar_evento_especial():
        pass

class Buque(Barcos):
    def __init(
        self,
        nombre, 
        costo_mantencion, 
        velocidad_base, 
        pasajeros, 
        carga_maxima, 
        moneda_origen, 
        tripulacion,
        mercancia
        ):
        super().init(
            nombre, 
            costo_mantencion, 
            velocidad_base, 
            pasajeros, 
            carga_maxima, 
            moneda_origen, 
            tripulacion,
            mercancia
            )

    def ejecutar_evento_especial():
        pass
