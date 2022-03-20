#Fragmentos del código sacados de la Actividad Sumativa 2
import random
import sys
#background-color: red;

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QThread
from PyQt5.QtWidgets import QApplication

import parametros as p
import utiles as u
import random

class Juego(QObject):
    senal_obstaculos = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.list_objetos = []
        self.pos_ocupadas = []
        self.filas = p.ALTO_FILAS
        self.columnas = p.ANCHO_COLUMNAS

    def obstaculos(self):
        pos_obst = []
        pos_ocupadas = []
        contador = 0
        while contador < 3:
            pos_fila = random.randint(0, p.ALTO_FILAS)
            pos_col = random.randint(0, p.ANCHO_COLUMNAS)
            if [pos_fila, pos_col] not in pos_ocupadas:
                pos_obst.append([pos_fila, pos_col])
                pos_ocupadas.append([pos_fila, pos_col])
                pos_ocupadas.append([pos_fila - 1, pos_col])
                pos_ocupadas.append([pos_fila + 1, pos_col])
                pos_ocupadas.append([pos_fila, pos_col - 1])
                pos_ocupadas.append([pos_fila - 1, pos_col - 1])
                pos_ocupadas.append([pos_fila + 1, pos_col - 1])
                pos_ocupadas.append([pos_fila, pos_col + 1])
                pos_ocupadas.append([pos_fila - 1, pos_col + 1])
                pos_ocupadas.append([pos_fila + 1, pos_col + 1])
                contador += 1
        self.senal_obstaculos.emit(pos_obst)

    def objetos(self):
        pass

