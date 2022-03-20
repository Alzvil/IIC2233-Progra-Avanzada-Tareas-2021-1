from PyQt5.QtCore import pyqtSignal, QObject
from frontend.preparacion import VentanaInicio

class Controlador(QObject):
    mostrar_ventana_principal_signal = pyqtSignal()
    enviar_signal = pyqtSignal(dict)

    def __init__(self, parent):
        super().__init__()
        self.ventana_inicio = VentanaInicio()

        self.mostrar_ventana_principal_signal.connect(self.abrir_inicio)
        self.ventana_inicio.senal_verificar_usuario.connect()

    def abrir_inicio(self):
        usuario = self.ventana_inicio.abrir()
        return usuario

    def mostrar_principal(self):
        self.ventana_principal.show()
        self.ventana_inicio.close()
        self.ventana_perfil.close()
        self.ventana_matches.close()
        self.ventana_perfiles.close()