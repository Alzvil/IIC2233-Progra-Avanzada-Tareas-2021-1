from funciones import encontrar_preferencia, log


# Debes completar este archivo

def improvisar_toppings(metodo_original):
    """
    Este decorador se encarga de escoger un topping nuevo en caso de que no quede del
    que pide el método original
    """
    def wrapper(self, *args, **kwargs):
        if self.ingredientes_disponibles[nombre_ingrediente] > 0:
            metodo_original(*args, **kwargs)
        else:
            preferencia = encontrar_preferencia(nombre_ingrediente)
            if self.ingredientes_disponibles[preferencia] > 0:
                log(f"cambiando el ingrediente {nombre_ingrediente} por {preferencia}")
                nombre_ingrediente = preferencia
                metodo_original(*args, **kwargs)
            else:
                preferencia = encontrar_preferencia(nombre_ingrediente)
                log(f"cambiando el ingrediente {nombre_ingrediente} por {preferencia}")
                nombre_ingrediente = preferencia
                metodo_original(*args, **kwargs)
        return wrapper
    return
 

def capa_relleno(tipo_relleno):
    def decorador(metodo_original):
        """
        Este decorador chequea que quede del relleno pedido, si los hay, lo agrega,
        si no, termina la torta
        """
        def wrapper(self, *args, **kwargs):
            cant_relleno = self.relleno_restante
            if cant_relleno <= 0:
                log("no queda suficiente relleno")
            else:
                log(f"añadiendo {tipo_relleno} a la torta")
                self.relleno_restante -= 1
                torta.append(tipo_relleno)
            metodo_original(*args, **kwargs)
            return wrapper
    return decorador


def revisar_ingredientes(metodo_original):
    """
    Este decorador revisa que hayan suficientes ingredientes antes de empezar una torta.
    En caso contrario, debe levantar una excepción del tipo ValueError
    """
    def wrapper(self, *args, **kwargs):
        cant_ingredientes = 0
        cant_disponible = 0
        for ingrediente in receta:
            cant_ingredientes += 1
            if self.ingredientes_diponibles[ingrediente] > 0:
                cant_diponible += 1
        if cant_ingredientes >= cant_disponible:
            metodo_original(*args, **kwargs)
        else:
            join("No hay ingredientes suficientes")
            raise ValueError("No hay ingredientes suficientes")
<<<<<<< HEAD
        return wrapper
=======
        return wrapper
>>>>>>> 3508d42037fa1cf8e9afd5b9baf97c6aaa6db7c8
