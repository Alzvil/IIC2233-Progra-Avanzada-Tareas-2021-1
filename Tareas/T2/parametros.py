import os

#PERSONAJES
VELOCIDAD_HOMERO = 6
PONDERADOR_VIDA_HOMERO = 1
VELOCIDAD_LISA = 9
PONDERADOR_TIEMPO_LISA = 1
VELOCIDAD_MOE = 8
VELOCIDAD_KRUSTY = 7

#OBJETOS
APARICION_DIFICULTAD_INTRO = 15 #segundos
APARICION_DIFICULTAD_AVANZADA = 45 #segundos
TIEMPO_OBJETO_INTRO = 10
TIEMPO_OBJETO_AVANZADA = 3

#EXTRAS
ALTO_FILAS = 8-1 #ES IMPORTANTE EL -1
ANCHO_COLUMNAS = 12-1 #ES IMPORTANTE EL -1

#RUTAS FRONTEND
VENTANA_INICIO = os.path.join("frontend", "assets", "templates", "ventana_inicio.ui")
VENTANA_ERROR = os.path.join("frontend", "assets", "templates", "error.ui")
PREPARACION = os.path.join("frontend", "assets", "templates", "preparacion.ui")
VENTANA_JUEGO = os.path.join("frontend", "assets", "templates", "juego.ui")
RUTA_CANCION = os.path.join("frontend", "assets", "canciones", "musica.wav")

#MAPA
MAPA_HOMERO = os.path.join("frontend", "assets", "sprites", "Mapa", "Planta_nuclear", "mapa.png")
MAPA_LISA = os.path.join("frontend", "assets", "sprites", "Mapa", "Primaria", "Mapa.png")
MAPA_MOE = os.path.join("frontend", "assets", "sprites", "Mapa", "Bar", "Mapa.png")
MAPA_KRUSTY = os.path.join("frontend", "assets", "sprites", "Mapa", "Krustyland", "Mapa.png")

#OBJETOS
OBJ_CORAZON = os.path.join("frontend", "assets", "sprites", "Objetos", "Corazon.png")
OBJ_VENENO = os.path.join("frontend", "assets", "sprites", "Objetos", "Veneno.png")
OBJ_HOMERO = os.path.join("frontend", "assets", "sprites", "Objetos", "Dona.png")
OBJ_HOMERO_X2 = os.path.join("frontend", "assets", "sprites", "Objetos", "DonaX2.png")
OBJ_LISA = os.path.join("frontend", "assets", "sprites", "Objetos", "Saxofon.png")
OBJ_LISA_X2 = os.path.join("frontend", "assets", "sprites", "Objetos", "SaxofonX2.png")
OBJ_MOE = os.path.join("frontend", "assets", "sprites", "Objetos", "Cerveza.png")
OBJ_MOE_X2 = os.path.join("frontend", "assets", "sprites", "Objetos", "CervezaX2.png")
OBJ_KRUSTY = os.path.join("frontend", "assets", "sprites", "Objetos", "Krusty.png")
OBJ_KRUSTY_X2 = os.path.join("frontend", "assets", "sprites", "Objetos", "KrustyX2.png")

#OBSTACULOS
OBS_HOMERO_1 = os.path.join("frontend", "assets", "sprites", "Mapa", "Planta_nuclear",  "Obstaculo1.png")
OBS_HOMERO_2 = os.path.join("frontend", "assets", "sprites", "Mapa", "Planta_nuclear",  "Obstaculo2.png")
OBS_HOMERO_3 = os.path.join("frontend", "assets", "sprites", "Mapa", "Planta_nuclear",  "Obstaculo3.png")
OBS_LISA_1 = os.path.join("frontend", "assets", "sprites", "Mapa", "Primaria",  "Obstaculo1.png")
OBS_LISA_2 = os.path.join("frontend", "assets", "sprites", "Mapa", "Primaria",  "Obstaculo2.png")
OBS_LISA_3 = os.path.join("frontend", "assets", "sprites", "Mapa", "Primaria",  "Obstaculo3.png")
OBS_MOE_1 = os.path.join("frontend", "assets", "sprites", "Mapa", "Bar",  "Obstaculo1.png")
OBS_MOE_2 = os.path.join("frontend", "assets", "sprites", "Mapa", "Bar",  "Obstaculo2.png")
OBS_MOE_3 = os.path.join("frontend", "assets", "sprites", "Mapa", "Bar",  "Obstaculo3.png")
OBS_KRUSTY_1 = os.path.join("frontend", "assets", "sprites", "Mapa", "Krustyland",  "Obstaculo1.png")
OBS_KRUSTY_2 = os.path.join("frontend", "assets", "sprites", "Mapa", "Krustyland",  "Obstaculo2.png")
OBS_KRUSTY_3 = os.path.join("frontend", "assets", "sprites", "Mapa", "Krustyland",  "Obstaculo3.png")

#SPIRTES PERSONAJES
PJ_HOMERO_D1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "down_1.png")
PJ_HOMERO_D2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "down_2.png")
PJ_HOMERO_D3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "down_3.png")
PJ_HOMERO_L1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "left_1.png")
PJ_HOMERO_L2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "left_2.png")
PJ_HOMERO_L3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "left_3.png")
PJ_HOMERO_R1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "right_1.png")
PJ_HOMERO_R2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "right_2.png")
PJ_HOMERO_R3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "right_3.png")
PJ_HOMERO_U1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "up_1.png")
PJ_HOMERO_U2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "up_2.png")
PJ_HOMERO_U3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Homero", "up_3.png")

PJ_LISA_D1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "down_1.png")
PJ_LISA_D2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "down_2.png")
PJ_LISA_D3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "down_3.png")
PJ_LISA_L1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "left_1.png")
PJ_LISA_L2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "left_2.png")
PJ_LISA_L3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "left_3.png")
PJ_LISA_R1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "right_1.png")
PJ_LISA_R2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "right_2.png")
PJ_LISA_R3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "right_3.png")
PJ_LISA_U1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "up_1.png")
PJ_LISA_U2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "up_2.png")
PJ_LISA_U3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Lisa", "up_3.png")

PJ_MOE_D1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "down_1.png")
PJ_MOE_D2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "down_2.png")
PJ_MOE_D3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "down_3.png")
PJ_MOE_L1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "left_1.png")
PJ_MOE_L2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "left_2.png")
PJ_MOE_L3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "left_3.png")
PJ_MOE_R1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "right_1.png")
PJ_MOE_R2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "right_2.png")
PJ_MOE_R3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "right_3.png")
PJ_MOE_U1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "up_1.png")
PJ_MOE_U2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "up_2.png")
PJ_MOE_U3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Moe", "up_3.png")

PJ_KRUSTY_D1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "down_1.png")
PJ_KRUSTY_D2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "down_2.png")
PJ_KRUSTY_D3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "down_3.png")
PJ_KRUSTY_L1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "left_1.png")
PJ_KRUSTY_L2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "left_2.png")
PJ_KRUSTY_L3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "left_3.png")
PJ_KRUSTY_R1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "right_1.png")
PJ_KRUSTY_R2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "right_2.png")
PJ_KRUSTY_R3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "right_3.png")
PJ_KRUSTY_U1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "up_1.png")
PJ_KRUSTY_U2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "up_2.png")
PJ_KRUSTY_U3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Krusty", "up_3.png")

PJ_GORGORY_D1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "down_1.png")
PJ_GORGORY_D2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "down_2.png")
PJ_GORGORY_D3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "down_3.png")
PJ_GORGORY_L1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "left_1.png")
PJ_GORGORY_L2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "left_2.png")
PJ_GORGORY_L3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "left_3.png")
PJ_GORGORY_R1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "right_1.png")
PJ_GORGORY_R2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "right_2.png")
PJ_GORGORY_R3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "right_3.png")
PJ_GORGORY_U1 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "up_1.png")
PJ_GORGORY_U2 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "up_2.png")
PJ_GORGORY_U3 = os.path.join("frontend", "assets", "sprites", "Personajes", "Gorgory", "up_3.png")