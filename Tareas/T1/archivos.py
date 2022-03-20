from parametros import (TENDENCIA_ENCALLAR_PASAJEROS, TENDENCIA_ENCALLAR_CARGUERO, \
    TENDENCIA_ENCALLAR_BUQUE)
from barcos import BarcoPasajeros, BarcoCarguero, Buque
from tripulantes import Capitan, Cocinero, Carguero

def lista_barcos():
    with open('barcos.csv', 'rt') as archivo_barcos:
        lista_barcos = archivo_barcos.readlines()
    for x in range(len(lista_barcos)):
        lista_barcos[x] = lista_barcos[x].strip().split(",")
    lista_barcos.pop(0)
    return lista_barcos

def lista_canales():
    with open('canales.csv', 'rt') as archivo_canales:
        lista_canales = archivo_canales.readlines()
    for x in range(len(lista_canales)):
        lista_canales[x] = lista_canales[x].strip().split(",")
    lista_canales.pop(0)
    return lista_canales

def creacion_instancias_barco():
    entidades_barcos = []
    for barco in lista_barcos():
        tripulacion = creacion_instancias_tripulante(barco[7].split(";"))
        mercancia = creacion_instancias_mercancia(barco[8].split(";"))
        if barco[1] == "Pasajero":
            temp = BarcoPasajeros(
                barco[0],
                barco[1],
                barco[2],
                barco[3],
                barco[4],
                barco[5],
                barco[6],
                tripulacion,
                mercancia
                )
            entidades_barcos.append(temp)
        elif barco[1] == "Carguero":
            temp = BarcoCarguero(
                barco[0],
                barco[1],
                barco[2],
                barco[3],
                barco[4],
                barco[5],
                barco[6],
                tripulacion,
                mercancia
                )
            entidades_barcos.append(temp)
        elif barco[1] == "Buque":
            temp = Buque(
                barco[0],
                barco[1],
                barco[2],
                barco[3],
                barco[4],
                barco[5],
                barco[6],
                tripulacion,
                mercancia
                )
            entidades_barcos.append(temp)
        else:
            print("Existe un error en la base de datos de barcos.csv")
            print("Los tipos no estan indicados como 'Pasajero', 'Carguero' o 'Buque'")
            print("LA INSTANCIA NO SE GENERARA")
            print(barco)
    return entidades_barcos

def creacion_instancias_tripulante(tripulantes):
    lista_instancias = []
    with open('tripulantes.csv', 'rt') as archivo_tripulantes:
        lista_tripulantes = archivo_tripulantes.readlines()
    for x in range(len(lista_tripulantes)):
        lista_tripulantes[x] = lista_tripulantes[x].strip().split(",")
    lista_tripulantes.pop(0)
    for canal in tripulantes:
        for archivo in lista_tripulantes:
            if canal == archivo[0]:
                if archivo[1] == "DCCapitán":
                    instancia = Capitan(
                        archivo[0],
                        archivo[1],
                        archivo[2]
                    )
                    lista_instancias.append(instancia)
                elif archivo[1] == "DCCocinero":
                    instancia = Cocinero(
                        archivo[0],
                        archivo[1],
                        archivo[2]
                    )
                    lista_instancias.append(instancia)
                elif archivo[1] == "DCCarguero":
                    instancia = Carguero(
                        archivo[0],
                        archivo[1],
                        archivo[2]
                    )
                    lista_instancias.append(instancia)
    return lista_instancias

def creacion_instancias_mercancia(mercancia):
    lista_instancias = []
    with open('mercancia.csv', 'rt') as archivo_mercancia:
        lista_mercancia = archivo_mercancia.readlines()
    for x in range(len(lista_mercancia)):
        lista_mercancia[x] = lista_mercancia[x].strip().split(",")
    lista_mercancia.pop(0)
    for canal in mercancia:
        for archivo in lista_mercancia:
            if archivo[0] == canal:
                if archivo[1] == "DCCapitán":
                    instancia = Capitan(
                        archivo[0],
                        archivo[1],
                        archivo[2],
                        archivo[3]
                    )
                    lista_instancias.append(instancia)
    return lista_instancias
