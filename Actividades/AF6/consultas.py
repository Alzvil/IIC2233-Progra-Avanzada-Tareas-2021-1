from functools import reduce
from cargar import cargar_comidas, cargar_mascotas
from parametros import RUTA_ANIMALES, RUTA_COMIDAS, TAMANOS


def obtener_comidas():
    '''
    Retorna una lista con todos los nombres de las comidas
    '''
    comidas = cargar_comidas(RUTA_COMIDAS)
    nombre_comidas = map(lambda x: x.nombre, comidas)
    lista_comidas = sorted(nombre_comidas, key=lambda t: t[1])
    return lista_comidas


def agrupar_por_tamano(tamanos):
    '''
    Recibe los un diccionario con los tamaños desde parametros.py
    Retorna una lista de listas con las instancias de mascota agrupadas
    '''
    peque1, peque2 = tamanos["PEQUENO"][0], tamanos["PEQUENO"][1]
    med1, med2 = tamanos["MEDIANO"][0], tamanos["MEDIANO"][1]
    gran1, gran2 = tamanos["GRANDE"][0], tamanos["GRANDE"][1]
    mascotas = cargar_mascotas(RUTA_ANIMALES)
    small = list(filter(lambda s: s.estatura in range(peque1, peque2), mascotas))
    mascotas = cargar_mascotas(RUTA_ANIMALES)
    medium = list(filter(lambda m: m.estatura in range(med1, med2), mascotas))
    mascotas = cargar_mascotas(RUTA_ANIMALES)
    big = list(filter(lambda b: b.estatura in range(gran1, gran2), mascotas))
    lista_mascotas_tamano = [small, medium, big]
    return lista_mascotas_tamano


def precio_total(especie):
    '''
    Recibe una especie
    Retorna precio total mascotas + comidas
    '''
    mascotas = cargar_mascotas(RUTA_ANIMALES)
    filtro_especie = list(filter(lambda b: b.especie == especie, mascotas))
    precios = map(lambda x: x.precio, filtro_especie)
    suma_mascotas = reduce(lambda x, y: x + y, (precios, 0))
    comidas = cargar_comidas(RUTA_COMIDAS)
    filtro_especie = list(filter(lambda b: b.especie == especie, comidas))
    precios = map(lambda x: x.precio, filtro_especie)
    suma_comidas = reduce(lambda x, y: x + y, (precios, 0))
    return sumas_mascotas + suma_comidas


def comida_ideal(raza, especie):
    '''
    FUNCION GENERADORA
    Recibe una raza y una especie
    Retorna instancias de comida
    '''
    comidas = cargar_comidas(RUTA_COMIDAS)
    for e in comidas:
        if e.raza == raza and e.especie == especie:
            yield e


def precio_comidas(raza, especie):
    '''
    Debes usar la funcion generadora comida_ideal
    Retorna el precio total de las comidas ideales
    '''
    comidas = cargar_comidas(RUTA_COMIDAS)
    filtro_especie = list(filter(lambda b: b.especie == especie and b.raza == raza, comidas))
    precios = map(lambda x: x.precio, filtro_especie)
    suma_comidas = reduce(lambda x, y: x + y, (precios, 0))
    return suma_comidas