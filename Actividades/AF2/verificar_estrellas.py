from cargar_datos import cargar_estrellas, cargar_nombres_estrellas_cercanas


def verificar_alias_estrella(estrella):
    alias = estrella.alias
    if (alias[:2].isdigit() == True) or ("F" in alias):
        raise ValueError("Error: El alias de la estrella es incorrecto.")
    return

def corregir_alias_estrella(estrella):
    try:
        verificar_alias_estrella(estrella)
    except ValueError as err:
        print(err)
        alias = estrella.alias
        if alias[:2].isdigit() == True:
            estrella.alias = alias[2:]+alias[:2]
        if "F" in estrella.alias:
            palabra = ""
            for letra in estrella.alias:
                if letra == "F":
                    palabra += "T"
                else:
                    palabra += letra
            #estrella.alias.replace("F","T") -> No sé por qué no funcionó
            estrella.alias = palabra
        print(f"El alias de {estrella.nombre} fue correctamente corregido.\n")
    return


def verificar_distancia_estrella(estrella):
    if estrella.distancia < 0:
        raise ValueError("Error: Distancia negativa.")
    return

def corregir_distancia_estrella(estrella):
    try:
        verificar_distancia_estrella(estrella)
    except ValueError as err:
        print(err)
        estrella.distancia = estrella.distancia * -1
        print(f"La distancia de la estrella {estrella.nombre} fue corregida.\n")
    return

def verificar_magnitud_estrella(estrella):
    if "." not in str(estrella.magnitud):
        raise TypeError("Error: Magnitud no es del tipo correcto.")
    return

def corregir_magnitud_estrella(estrella):
    try:
        verificar_magnitud_estrella(estrella)
    except TypeError as err:
        print(err)
        #print(estrella.magnitud)
        magnitud = str(estrella.magnitud)
        #print("INICIO: ", magnitud)
        if ";" in magnitud:
            palabra = ""
            for numero in magnitud:
                if numero == ";":
                    palabra += "."
                else:
                    palabra += numero
            estrella.magnitud = float(palabra)
            #print("CAMBIO ; ", estrella.magnitud)
            #print("CAMBIO ", estrella.magnitud)
        estrella.magnitud = float(estrella.magnitud)
        print(f"La magnitud de la estrella {estrella.nombre} fue corregida.\n")
    else:
        estrella.magnitud = float(estrella.magnitud)
    return


def dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas):
    try:
        diccionario_estrellas[nombre_estrella]
    except KeyError as err:
        print(f"Estrella {nombre_estrella} NO está en nuestra base de datos.")
        print("¡Alerta, puede ser una trampa de algún extraterrestre!")
    else:
        print(f"Estrella {nombre_estrella} está en nuestra base de datos.")
        alias_estrella = diccionario_estrellas[nombre_estrella].alias
        print(f"Su alias es {alias_estrella}.")
    return


if __name__ == "__main__":
    diccionario_estrellas = cargar_estrellas("estrellas.csv")
    nombres_estrellas = cargar_nombres_estrellas_cercanas("estrellas_cercanas.txt")

    # Descomenta las funciones que quieras probar de la actividad
    print("Revisando posibles errores en las estrellas...\n")
    for estrella in diccionario_estrellas.values():
        corregir_alias_estrella(estrella)
        corregir_distancia_estrella(estrella)
        corregir_magnitud_estrella(estrella)
        pass

    print("Revisando estrellas inexistentes...\n")
    for nombre_estrella in nombres_estrellas:
        dar_alerta_estrella_cercana(nombre_estrella, diccionario_estrellas)
        pass
