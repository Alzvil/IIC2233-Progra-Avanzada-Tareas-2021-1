from funciones import desencriptar, encriptar, log
from random import uniform, choices


def desencriptar_receta(metodo_original):
    """
    Este decorador debe hacer que el método "leer_recetas" retorne las recetas desencriptadas
    """

    def wrapper(*args, **kwargs):
        temp = []
        dic = metodo_original(*args, **kwargs)
        for key in dic:
            for e in key:
                temp.append(desencriptar(e))
            dic[key] = temp
        return dic
    return wrapper



def encriptar_receta(metodo_original):
    """
    Este decorador debe hacer que el método "escribir_recetas" encripte las
    recetas antes de escribirlas
    """
    def wrapper(*args):
        desencriptado = [*args]
        encriptado = []
        for e in desencriptado:
            encriptado.append(encriptar(e))
        metodo_original(encriptado.split(","))
    return wrapper


def ingredientes_infectados(probabilidad_infectado):
    def decorador(metodo_original):
        """
        Este decorador debe hacer que el método "revisar_despensa" elmine los ingredientes
        que pueden estar infectados, según la probabilidad dada.
         """
        def wrapper(*args, **kwargs):
            dic = metodo_original(*args, **kwargs)
            for key in dic:
                probabilidad = uniform(0, probabilidad_infectado)
                proba_false = probabilidad_infectado - probabilidad
                eleccion = choices([True, False], weights=(probabilidad, \
                        proba_false), k=1)
                if eleccion == True:
                    log("se encontro un ingrediente infectado")
                    dic[key] -= 1
            return dic
        return wrapper
    return decorador
