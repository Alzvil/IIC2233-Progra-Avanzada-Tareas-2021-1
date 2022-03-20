import sys
from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicio import VentanaInicio, VentanaError
from backend.ventana_inicio_backend import VentanaInicioBackend
from frontend.ventana_juego import Preparacion, VentanaJuego
from backend.logica_juego import Juego

def hook(type_error, traceback):
    print(type_error)
    print(traceback)

if __name__ == '__main__':
    # No modificar ->
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    ventana_inicio = VentanaInicio()
    ventana_inicio_back = VentanaInicioBackend()
    ventana_error = VentanaError()
    v_preparacion = Preparacion()
    ventana_juego = VentanaJuego()
    logica_juego = Juego()

    ventana_inicio.senal_verificar_usuario.connect(ventana_inicio_back.verificar_usuario)
    ventana_inicio_back.senal_error.connect(ventana_error.abrir)
    ventana_inicio_back.senal_preparacion.connect(v_preparacion.abrir)
    ventana_inicio_back.senal_preparacion.connect(ventana_inicio.ocultar)
    v_preparacion.senal_juego.connect(ventana_juego.imagen_mapa)
    v_preparacion.senal_juego.connect(ventana_juego.abrir)
    v_preparacion.senal_juego.connect(logica_juego.obstaculos)
    logica_juego.senal_obstaculos.connect(ventana_juego.aparecer_obstaculo)

    sys.exit(app.exec_())
    app.exec()