#Fragmentos del código sacados de la Actividad Sumativa 2
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication

class VentanaInicioBackend(QObject):
    senal_preparacion = pyqtSignal()
    senal_error = pyqtSignal()

    def __init__(self):
        super().__init__()
    
    def verificar_usuario(self, usuario):
        comprobante = True
        if len(usuario) > 14:
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