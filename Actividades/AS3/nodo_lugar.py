import cargar_archivos as c
from collections import namedtuple


class NodoLugar:
    # NO MODIFICAR
    def __init__(self, nombre):
        self.nombre = nombre
        # Lista de namedtuples del tipo mafioso (definido en cargar_archivos.py)
        self.mafiosos = []
        # Lista de namedtuples del tipo conexion, con los atributos vecino
        # y peso, que guardan el nodo vecino y el peso de dicha conexion
        self.conexiones = []

    def agregar_conexion(self, destino, peso):
        Conexion = namedtuple("Conexion", ["vecino", "peso"])
        self.conexiones.append(
            Conexion(vecino=destino, peso=peso)
        )

    def __str__(self):
        # Puedes imprimir el nodo :D
        texto = ""
        nombres = ", ".join([habitante.nombre for habitante in self.mafiosos])
        texto += f"En {self.nombre} se encuentran los mafiosos {nombres}.\n"
        conexiones = ", ".join([f"{conexion.vecino} de peso {conexion.peso}"
                                for conexion in self.conexiones])
        texto += f"Desde aqui puedes ir a {conexiones}.\n"
        return texto

def construir_nodo_lugares(nombre, dic_lugares, lista_lugares, contador, lista_nodos):
    if nombre == None:
        print("nombre is none")
        for e in dic_lugares:
            lista_lugares.append(e)
        contador = len(lista_lugares)-1
        nombre_siguiente = lista_lugares[contador]
        contador -= 1
        nodo = construir_nodo_lugares(nombre_siguiente, dic_lugares, lista_lugares, contador, lista_nodos)
        lista_nodos.append(nodo)
    if nombre != None and contador >= 0:
        print(f"El nombre del lugar es: {nombre}")
        nombre_siguiente = lista_lugares[contador]
        contador -= 1
        nodo = NodoLugar(nombre)
        nodo.mafiosos = dic_lugares[nombre]
        nodo = construir_nodo_lugares(nombre_siguiente, dic_lugares, lista_lugares, contador, lista_nodos)
        lista_nodos.append(nodo)
    return lista_nodos

def crear_grafo(dic_lugares, conexiones):
    # COMPLETAR
    # Crea los nodos, teniendo en cuenta sus mafiosos, las conexiones y sus pesos
    print("CONSTRUYENDO NODOS LUGARES")
    nodo = construir_nodo_lugares(None, dic_lugares, [], 0, [])
    #No logré entender por qué retonar [[...],[...]]
    print(nodo)
    for e in conexiones:
        for i in nodo:
            if i.nombre == e[0]:
                i.agregar_conexion(e[1],e[2])
                retornar = i
    return retornar



if __name__ == "__main__":
    # Puedes usar esta parte para probar tu avance
    pass
