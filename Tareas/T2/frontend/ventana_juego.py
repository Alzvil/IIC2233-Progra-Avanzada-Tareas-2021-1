#Fragmentos del código sacados de la Actividad Sumativa 2
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel
from collections import defaultdict, OrderedDict

import parametros as p
import utiles as u
import random

window_name_prepa, base_class_prepa = uic.loadUiType(p.PREPARACION)
window_name_juego, base_class_juego = uic.loadUiType(p.VENTANA_JUEGO)

class Preparacion(window_name_prepa, base_class_prepa):
    senal_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radio_homero.personaje = "homero"
        self.radio_lisa.personaje = "lisa"
        self.radio_moe.personaje = "moe"
        self.radio_krusty.personaje = "krusty"
        self.radio_homero.toggled.connect(self.boton_personaje)
        self.radio_lisa.toggled.connect(self.boton_personaje)
        self.radio_moe.toggled.connect(self.boton_personaje)
        self.radio_krusty.toggled.connect(self.boton_personaje)
        self.contador = 2

    def iniciar_juego(self):
        if self.nombre_pj == "homero":
            if self.personaje.geometry().intersects(self.planta.geometry()):
                self.senal_juego.emit(self.nombre_pj)
                self.hide()
        elif self.nombre_pj == "lisa":
            if self.personaje.geometry().intersects(self.escuela.geometry()):
                self.senal_juego.emit(self.nombre_pj)
                self.hide()
        elif self.nombre_pj == "moe":
            if self.personaje.geometry().intersects(self.bar.geometry()):
                self.senal_juego.emit(self.nombre_pj)
                self.hide()
        elif self.nombre_pj == "krusty":
            if self.personaje.geometry().intersects(self.krusty.geometry()):
                self.senal_juego.emit(self.nombre_pj)
                self.hide()

    def abrir(self):
        self.show()

    def boton_personaje(self):
        if self.sender().isChecked():
            self.sprites_personajes(self.sender().personaje)

    def sprites_personajes(self, personaje):
        if personaje == "homero":
            self.sprites = u.LISTA_HOMERO
            self.velocidad = p.VELOCIDAD_HOMERO
            self.personaje.setPixmap(QPixmap(self.sprites[0][2]))
            self.nombre_pj = "homero"
        elif personaje == "lisa":
            self.sprites = u.LISTA_LISA
            self.velocidad = p.VELOCIDAD_LISA
            self.personaje.setPixmap(QPixmap(self.sprites[1][0]))
            self.nombre_pj = "lisa"
        elif personaje == "moe":
            self.sprites = u.LISTA_MOE
            self.velocidad = p.VELOCIDAD_MOE
            self.personaje.setPixmap(QPixmap(self.sprites[2][0]))
            self.nombre_pj = "moe"
        elif personaje == "krusty":
            self.sprites = u.LISTA_KRUSTY
            self.velocidad = p.VELOCIDAD_KRUSTY
            self.personaje.setPixmap(QPixmap(self.sprites[3][0]))
            self.nombre_pj = "krusty"

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            if not self.personaje.geometry().intersects(self.superior_1.geometry()):
                self.personaje.move(self.personaje.pos() + QPoint(0, -self.velocidad))
                self.iniciar_juego()
            self.animacion("w")
        if event.key() == Qt.Key_A:
            if not self.personaje.geometry().intersects(self.costado_i.geometry()):
                self.personaje.move(self.personaje.pos() + QPoint(-self.velocidad, 0))
                self.iniciar_juego()
            self.animacion("a")
        if event.key() == Qt.Key_S:
            if not self.personaje.geometry().intersects(self.abajo.geometry()):
                self.personaje.move(self.personaje.pos() + QPoint(0, self.velocidad))
                self.iniciar_juego()
            self.animacion("s")
        if event.key() == Qt.Key_D:
            if not self.personaje.geometry().intersects(self.costado_d.geometry()):
                self.personaje.move(self.personaje.pos() + QPoint(self.velocidad, 0))
                self.iniciar_juego()
            self.animacion("d")

    def animacion(self, direccion):
        if direccion == "w":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[0][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[0][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[0][0]))
                self.contador = 1
        elif direccion == "a":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[1][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[1][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[1][0]))
                self.contador = 1
        elif direccion == "s":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[2][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[2][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[2][0]))
                self.contador = 1
        if direccion == "d":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[3][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[3][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[3][0]))
                self.contador = 1
            

class VentanaJuego(window_name_juego, base_class_juego):
    senal_teclas = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dic_grilla = defaultdict(lambda: [])
        self.lista_grilla()
        self.pausa = False

    def imagen_mapa(self, personaje):
        self.mapa.setAttribute(Qt.WA_TranslucentBackground)
        self.personaje.setAttribute(Qt.WA_TranslucentBackground)
        if personaje == "homero":
            self.sprites = u.LISTA_HOMERO
            self.items = [p.OBJ_HOMERO, p.OBJ_HOMERO_X2, p.OBS_HOMERO_1, p.OBS_HOMERO_2, p.OBS_HOMERO_3]
            self.personaje.setPixmap(QPixmap(self.sprites[0][2]))
            self.mapa.setPixmap(QPixmap(p.MAPA_HOMERO))
            self.velocidad = p.VELOCIDAD_HOMERO
            self.contador = 3
        elif personaje == "lisa":
            self.sprites = u.LISTA_LISA
            self.items = [p.OBJ_LISA, p.OBJ_LISA_X2, p.OBS_LISA_1, p.OBS_LISA_2, p.OBS_LISA_3]
            self.personaje.setPixmap(QPixmap(self.sprites[0][0]))
            self.mapa.setPixmap(QPixmap(p.MAPA_LISA))
            self.velocidad = p.VELOCIDAD_LISA
            self.contador = 1
        elif personaje == "moe":
            self.sprites = u.LISTA_MOE
            self.items = [p.OBJ_MOE, p.OBJ_MOE_X2, p.OBS_MOE_1, p.OBS_MOE_2, p.OBS_MOE_3]
            self.personaje.setPixmap(QPixmap(self.sprites[0][0]))
            self.mapa.setPixmap(QPixmap(p.MAPA_MOE))
            self.velocidad = p.VELOCIDAD_MOE
            self.contador = 1
        elif personaje == "krusty":
            self.sprites = u.LISTA_KRUSTY
            self.items = [p.OBJ_KRUSTY, p.OBJ_KRUSTY_X2, p.OBS_KRUSTY_1, p.OBS_KRUSTY_2, p.OBS_KRUSTY_3]
            self.personaje.setPixmap(QPixmap(self.sprites[0][2]))
            self.mapa.setPixmap(QPixmap(p.MAPA_KRUSTY))
            self.velocidad = p.VELOCIDAD_KRUSTY
            self.contador = 3
        self.mapa.setScaledContents(True)
        self.personaje.setScaledContents(True)

    def abrir(self):
        self.show()

    def keyPressEvent(self, event):
        if not self.pausa:
            if event.key() == Qt.Key_W:
                if not self.colisiones("w"):
                    self.personaje.move(self.personaje.pos() + QPoint(0, -self.velocidad))
                self.animacion("w")
            if event.key() == Qt.Key_A:
                if not self.colisiones("a"):
                    self.personaje.move(self.personaje.pos() + QPoint(-self.velocidad, 0))
                self.animacion("a")
            if event.key() == Qt.Key_S:
                if not self.colisiones("s"):
                    self.personaje.move(self.personaje.pos() + QPoint(0, self.velocidad))
                self.animacion("s")
            if event.key() == Qt.Key_D:
                if not self.colisiones("d"):
                    self.personaje.move(self.personaje.pos() + QPoint(self.velocidad, 0))
                self.animacion("d")
            ##############ARREGLAR:
            if event.key() == Qt.Key_V and event.key() == Qt.Key_I and event.key() == Qt.Key_D:
                print("====EVENTO VID====")
            if event.key() == Qt.Key_N and event.key() == Qt.Key_I and event.key() == Qt.Key_V:
                print("====EVENTO NIV====")

    def animacion(self, direccion):
        if direccion == "w":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[0][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[0][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[0][0]))
                self.contador = 1
        elif direccion == "a":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[1][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[1][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[1][0]))
                self.contador = 1
        elif direccion == "s":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[2][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[2][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[2][0]))
                self.contador = 1
        if direccion == "d":
            if self.contador == 1:
                self.personaje.setPixmap(QPixmap(self.sprites[3][2]))
                self.contador = 2
            elif self.contador == 2:
                self.personaje.setPixmap(QPixmap(self.sprites[3][1]))
                self.contador = 3
            elif self.contador == 3:
                self.personaje.setPixmap(QPixmap(self.sprites[3][0]))
                self.contador = 1

    def lista_grilla(self):
        self.lista_labels = [[],[],[],[],[],[],[],[],[],[],[],[]]
        self.atributos_clases = self.__dict__
        self.atributos_clases = OrderedDict(sorted(self.atributos_clases.items()))
        for elemento in self.atributos_clases:
            if "pos" in elemento:
                for col in range(12):
                    if "_{}__".format(str(col+1)) in elemento:
                        self.lista_labels[col].append([self.atributos_clases[elemento], "vacio"])

    def aparecer_obstaculo(self, posiciones):
        fila_1, col_1 = posiciones[0]
        fila_2, col_2 = posiciones[1]
        fila_3, col_3 = posiciones[2]
        self.lista_labels[col_1][fila_1][0].setPixmap(QPixmap(self.items[2]))
        self.lista_labels[col_1][fila_1][0].setScaledContents(True)
        self.lista_labels[col_1][fila_1][1] = "obstaculo"
        self.lista_labels[col_2][fila_2][0].setPixmap(QPixmap(self.items[3]))
        self.lista_labels[col_2][fila_2][0].setScaledContents(True)
        self.lista_labels[col_2][fila_2][1] = "obstaculo"
        self.lista_labels[col_3][fila_3][0].setPixmap(QPixmap(self.items[4]))
        self.lista_labels[col_3][fila_3][0].setScaledContents(True)
        self.lista_labels[col_3][fila_3][1] = "obstaculo"

    def colisiones(self, direccion):
        colisiona = False
        if direccion == "w":
            if self.personaje.geometry().intersects(self.superior_1.geometry()):
                colisiona = True
        elif direccion == "a":
            if self.personaje.geometry().intersects(self.costado_i.geometry()):
                colisiona = True
        elif direccion == "s":
            if self.personaje.geometry().intersects(self.abajo.geometry()):
                colisiona = True
        elif direccion == "d":
            if self.personaje.geometry().intersects(self.costado_d.geometry()):
                colisiona = True
        for columna in self.lista_labels:
            for casilla in columna:
                if casilla[1] == "obstaculo":
                    if self.personaje.geometry().intersects(casilla[0].geometry()):
                        colisiona = True
        return colisiona