######## CLIENTE ########

import socket
import threading
from interfaz import Controlador

#Sacado de la AF7 y su video de cierre
class Cliente():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.controlador = Controlador(self)
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("> iniciando cliente")
        self.iniciar_cliente()
        self.conectado = False
    
    def iniciar_cliente(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            thread = threading.Thread(target = self.escuchar_servidor)
            thread.start()
            usuario = self.controlador.abrir_inicio()
        except ConnectionResetError:
            print("> error al iniciar cliente")
            self.socket_cliente.close()

    def escuchar_servidor(self):
        try:
            while self.conectado:
                pass
                #mensaje = self.recibir()
                #if not mensaje:
                    #raise ConnectionResetError
                #self.controlador.manejar_mensaje(mensaje)
        except ConnectionResetError:
            print("> error al comunicarse con el servidor")
        finally:
            self.socket_cliente.close()
