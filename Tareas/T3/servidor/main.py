######## SERVIDOR ########

#Codigo basado en los contenidos de la semana 14 y la AF7
import json
import socket
import threading
from logica import Logica

#Copiado de AF7
class Servidor:
    clientes_conectados_lock = threading.Lock()

    def __init__(self, host, port):
        self.host = host
        self.port = port
        print("> iniciando servidor")
        self.iniciar_servidor()
        self._id_cliente = 0
        self.clientes_conectados = dict()
        self.clientes_cola = dict()
        self.ids_cola = []
        thread = threading.Thread(target = self.aceptar_clientes, daemon = True)
        thread.start()

    def iniciar_servidor(self):
        print("> abriendo socket de recepción")
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen()

    def aceptar_clientes(self):
        print("> se esta conectado un cliente al servidor")
        while True:
            socket_cliente, address = self.socket_servidor.accept()
            with self.clientes_conectados_lock:
                id_cliente = self._id_cliente
                print(f"> cliente conectado con el id {id_cliente}")
                if len(self.clientes_conectados) < 4:
                    self.clientes_conectados[id_cliente] = socket_cliente
                    print(f"> el cliente {id_cliente} se encuentra en la sala")
                else:
                    self.clientes_cola[id_cliente] = socket_cliente
                    self.ids_cola.append(id_cliente)
                    print(f"> el cliente {id_cliente} se encuentra en la cola")
                self._id_cliente += 1
            threading.Thread(targe = self.escuchar_cliente, arg = (id_cliente,))
            thread_cliente.start()

    def escuchar_cliente(self, id_cliente):
        try:
            socket_cliente = self.clientes_conectados[id_cliente]
            while True:
                mensaje = self.recibir(socket_cliente)
                if not mensaje:
                    raise ConnectionResetError
                respuesta, targets = self.logica.manejar_mensaje(mensaje, id_cliente)
                if respuesta:
                    for e in targets:
                        self.enviar(respuesta, e)
        except ConnectionResetError:
            print(f"> Ocurrió un error con el cliente {id_cliente}, se ha desconectado")
            self.eliminar_cliente(id_cliente)

    def enviar(self, mensaje, socket_cliente):
        bytes_mensaje = self.codificar_mensaje(mensaje)
        largo_mensaje = len(bytes_mensaje).to_bytes(5, byteorder = 'little')
        socket_cliente.sendall(largo_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            json_mensaje = json.dumps(mensaje)
            bytes_mensaje = json_mensaje.encode()
            return bytes_mensaje
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo codificar el mensaje")
            return b""

    def recibir(self, socket_cliente):
        bytes_mensaje = bytearray()
        bytes_largo_mensaje = socket_cliente.recv(5)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder = 'little')
        while len(bytes_mensaje) < largo_mensaje:
            bytes_mensaje += socket_cliente.recv(min(64, largo_mensaje - len(bytes_mensaje)))
        return self.decodificar_mensaje(bytes_mensaje)

    def decodificar_mensaje(self, bytes_mensaje):
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo decodificar el mensaje")
            return dict()

    def eliminar_cliente(self, id_cliente):
        with self.clientes_conectados_lock:
            print(f"> Borrando socket del cliente {id_cliente}")
            socket_cliente = self.clientes_conectados[id_cliente]
            socket_cliente.close()
            del self.clientes_conectados[id_cliente]
        if len(self.clientes_conectados) < 4:
            id = self.ids_cola.pop(0)
            self.aceptar_clientes(self.clientes_cola[id])
            del self.clientes_cola[id]

    def cerrar_servidor(self):
        print("> desconectando clientes")
        for id_cliente in list(self.clientes_conectados.keys()):
            self.eliminar_cliente(id_cliente)
        print("> cerrando socket de recepción")
        self.socket_servidor.close()
        print("> servidor cerrado")

if __name__ == "__main__":
    with open('parametros.json', 'r') as archivo:
        parametros = json.loads(archivo)

    HOST = parametros["host"]
    PORT = parametros["port"]

    SERVIDOR = Servidor(HOST, PORT)

    try:
        while True:
            input("> presione Ctrl+C para cerrar el servidor")
    except KeyboardInterrupt:
        print("> cerrando servidor")
        SERVIDOR.cerrar_servidor()
