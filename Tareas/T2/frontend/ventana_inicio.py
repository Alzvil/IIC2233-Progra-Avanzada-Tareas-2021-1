#Fragmentos del código sacados de la Actividad Sumativa 2
from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
import sys

import parametros as p

window_name_main, base_class_main = uic.loadUiType(p.VENTANA_INICIO)
window_name_error, base_class_error = uic.loadUiType(p.VENTANA_ERROR)

class VentanaInicio(window_name_main, base_class_main):
    senal_verificar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_comenzar.clicked.connect(self.verificar_usuario)
        self.boton_ranking.clicked.connect(self.mostrar_ranking)
        self.boton_salir.clicked.connect(self.cerrar_programa)
        self.show()

    def verificar_usuario(self):
        nombre_usuario = self.input_usuario.text()
        self.senal_verificar_usuario.emit(nombre_usuario)

    def mostrar_ranking(self):
        pass

    def ocultar(self):
        self.hide()

    def cerrar_programa(self):
        sys.exit()

class VentanaError(window_name_error, base_class_error):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.volver.clicked.connect(self.cerrar)

    def abrir(self):
        self.show()

    def cerrar(self):
        self.hide()