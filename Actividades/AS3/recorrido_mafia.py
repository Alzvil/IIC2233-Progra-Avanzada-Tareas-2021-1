from collections import deque
import parametros as p


# Funciones que revisan todos los nodos para desmantelar la organización


def recorrer_mafia(inicio):
    # COMPLETAR
    visitados = []
    mafiosos = []
    cola = deque([inicio])

    while len(cola) > 0:
        lugar = cola.popleft()
        if lugar in visitado:
            continue
        print(f"Se ha desmantelado {lugar.nombre}")
        for e in lugar.mafiosos:
            if e.frase == p.frase_lider_1 or e.frase == p.frase_lider_2:
                mafiosos.append(lugar)
    return mafiosos


# BONUS
# Recibe como inicio el nodo en el que está uno de los líderes de la mafia
# y como termino el nodo en el que esta el otro lider
def minima_peligrosidad(inicio, termino):
    # COMPLETAR
    pass
