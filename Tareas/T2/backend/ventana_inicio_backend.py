#Fragmentos del código sacados de la Actividad Sumativa 2
import os
import sys
import parametros as p
import utiles as u

from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication


class VentanaInicioBackend(QObject):
    senal_preparacion = pyqtSignal()
    senal_error = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.musica = Musica(p.RUTA_CANCION)
        self.start()
    
    def verificar_usuario(self, usuario):
        comprobante = True
        if usuario == "":
            comprobante = False
        else:
            if usuario.isalnum() == True:
                comprobante = True
            else:
                comprobante = False
        if comprobante == True:
            u.usuario = usuario
            self.senal_preparacion.emit()
        else:
            self.senal_error.emit()

    def start(self):
        # NO MODIFICAR ESTE MÉTODO
        self.musica.comenzar()



class Musica(QObject):
    # NO MODIFICAR ESTA CLASE

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion

    def comenzar(self):
        try:
            self.cancion = QtMultimedia.QSound(self.ruta_cancion)
            self.cancion.Loop()
            self.cancion.play()
        except Exception as error:
            print('No se pudo iniciar la cancion', error)