"""
Este módulo contiene la clase Logica
"""
import json
from threading import Lock
from base64 import b64encode
from datetime import datetime
from random import choice

class Logica:
    ingreso_lock = Lock()
    usuarios_activos_lock = Lock()

    def __init__(self, log_activado=True):
        self.log_activado = log_activado
        self.usuarios_activos = dict()

    def validar_nombre_usuario(self, nombre_usuario):
        with self.usuarios_activos_lock:
            if len(nombre_usuario) >= 15:
                print("El nombre de usuario excede los caracteres maximos")
                return False
            if nombre_usuario in self.usuarios_activos.values():
                print("Este usuario está siendo usado por otro jugador")
                return False
            return True

    def desconectar_usuario(self, id_cliente):
        with self.usuarios_activos_lock:
            try:
                del self.usuarios_activos[id_cliente]
                self.log(f"Se ha eliminado al cliente {id_cliente} de la lista de usuarios activos")
            except KeyError:
                self.log(f"El cliente {id_cliente} no figura como usuario activo")

    @staticmethod
    def obtener_bytes_imagen(ruta):
        """
        Recibe un ruta de una imagen, y codifica sus bytes a un string utf-8
        """
        with open(ruta, "rb") as archivo_imagen:
            imagen_bytes = archivo_imagen.read()
            imagen_codificada = b64encode(imagen_bytes).decode(encoding='ASCII')
        return imagen_codificada

    def manejar_mensaje(self, mensaje, id_cliente):
        pass
        #return respuesta, destinatarios

    def guardar_variables(self):
        # usuarios.json (guardar bio)
        with open("db/usuarios.json", "w", encoding='utf-8') as archivo:
            dict_usuarios = dict()
            for key in self.diccionario_usuarios:
                usuario = self.diccionario_usuarios[key]
                dict_usuarios[key] = {
                    "bio": usuario.bio,
                    "edad": usuario.edad,
                    "nombre": usuario.nombre,
                    "ruta_imagen": usuario.ruta_imagen,
                }
            json.dump(dict_usuarios, archivo, indent=4, sort_keys=True)
            del dict_usuarios
        # likes.csv
        with open("db/likes.csv", "w", encoding='utf-8') as archivo:
            archivo.write("usuario_da,usuario_recibe\n")
            for key in self.diccionario_usuarios:
                usuario = self.diccionario_usuarios[key]
                for liked_user in usuario.lista_likes:
                    archivo.write(f"{usuario.nombre},{liked_user}\n")
        # mensajes.csv
        with open("db/mensajes.csv", "w", encoding='utf-8') as archivo:
            archivo.write("usuario_envia,usuario_recibe,fecha,mensaje\n")
            for key in self.diccionario_usuarios:
                usuario = self.diccionario_usuarios[key]
                for destinatario_user in usuario.mensajes:
                    for tup_mensaje in usuario.mensajes[destinatario_user]:
                        out = f"{tup_mensaje[0]},{destinatario_user},{tup_mensaje[1]},{tup_mensaje[2]}\n"
                        archivo.write(out)

    def log(self, mensaje_consola):
        """Imprime un mensaje a la consola, sólo si la funcionalidad está activada.

        Argumentos:
            mensaje_consola (str): mensaje a imprimir.
        """
        if self.log_activado:
            print(mensaje_consola)
