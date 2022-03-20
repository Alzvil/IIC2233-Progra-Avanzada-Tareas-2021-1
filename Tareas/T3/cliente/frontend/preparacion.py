#Fragmentos del código sacados de la Actividad Sumativa 2
from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap

import parametros as p

window_name_main, base_class_main = uic.loadUiType(p.VENTANA_INICIO)
window_name_error, base_class_error = uic.loadUiType(p.VENTANA_ERROR)

class VentanaInicio(window_name_main, base_class_main):
    senal_verificar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_comenzar.clicked.connect(self.verificar_usuario)

    def abrir(self):
        nombre_usuario = self.input_usuario.text()
        return nombre_usuario