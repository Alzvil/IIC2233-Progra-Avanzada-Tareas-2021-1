import pyrematch as re


# ------------------------------------------------------------------------------------------------
# DEFINIR AQUI LOS PATRONES PARA CONSTRUIR CADA EXPRESION REGULAR
# NO CAMBIAR LOS NOMBRES DE LAS VARIABLES
PATRON_1 = "^#((\s)+)?!titulo{(\w)+}\n"
PATRON_2 = "(###?)((\s)+)?!subseccion{(\w)+}\n"
PATRON_3 = "<img(\s)?src=(\'|\")!imagen{(\w|/|\.|:)+}(\'|\")(\s)?alt>"
PATRON_4 = "`+!lenguaje{(\w)+}\n!bloque{(\w|\W)+([^`]+)}`+"
PATRON_5 = "\*(\s)?\[X\](\s)?!check{(\S)(\w|\W)([^(\n)]+)}\n"
PATRON_6 = "\n!texto{(\S)(\w|\W)+((\s)+)?\(!link{(\w|\W)+}\)([^(\n)]+)}\n"
#mas cuidado con los enunciados pls

# ------------------------------------------------------------------------------------------------
# Completar a continuación el código de cada consulta. Cada consulta recibe el patrón
# correspondiente para construir la expresión regular, y el texto sobre el cual se aplicará.
# Cada consulta debe retornar una lista de diccionarios, donde cada diccionario contiene dos
# llaves: "contenido" (el texto del match encontrado) y "posicion" (lista con dos elementos: la
# posición de inicio y la posición de término del match encontrado).


# CONSULTA 1
def consulta_1(texto, patron):
    retornar = []
    rgx = re.compile(patron)
    for match in rgx.finditer(texto):
        dic = {"contenido" : match.group("titulo"), "posicion" : match.span("titulo")}
        retornar.append(dic)
    return retornar
    #LISTA


# CONSULTA 2
def consulta_2(texto, patron):
    retornar = []
    rgx = re.compile(patron)
    for match in rgx.finditer(texto):
        print(match)
        dic = {"contenido" : match.group("subseccion"), "posicion" : match.span("subseccion")}
        retornar.append(dic)
    return retornar
    #LISTA


# CONSULTA 3
def consulta_3(texto, patron):
    retornar = []
    rgx = re.compile(patron)
    for match in rgx.finditer(texto):
        dic = {"contenido" : match.group("imagen"), "posicion" : match.span("imagen")}
        retornar.append(dic)
    return retornar
    #LISTA


# CONSULTA 4
def consulta_4(texto, patron):
    retornar = []
    rgx = re.compile(patron)
    for match in rgx.finditer(texto):
        dic = {"contenido" : match.group("lenguaje"), "posicion" : match.span("bloque")}
        retornar.append(dic)
    return retornar
    #LISTA


# CONSULTA 5
def consulta_5(texto, patron):
    retornar = []
    rgx = re.compile(patron)
    for match in rgx.finditer(texto):
        dic = {"contenido" : match.group("check"), "posicion" : match.span("check")}
        retornar.append(dic)
    return retornar


# CONSULTA 6
def consulta_6(texto, patron):
    retornar = []
    rgx = re.compile(patron)
    for match in rgx.finditer(texto):
        dic = {"contenido" : match.group("texto"), "posicion" : match.span("link")}
        retornar.append(dic)
    return retornar
