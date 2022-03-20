"""
Modulo para funciones de codificacion y decodificacion para envio de mensajes.
Recuerda, no debes modificar los argumentos que recibe cada funcion,
y debes entregar exactamente lo que esta pide en el enunciado.
"""


# Codificar un mensaje a un bytearray segun el protocolo especificado.
def codificar_mensaje(mensaje):
    # COMPLETAR ESTA FUNCION
    b_mensaje = bytes(json.dumps(mensaje), "utf-8")
    b_largo_mensaje = (len(b_mensaje)).to_bytes(4, byteorder = "big")
    b_tipo_mensaje = (2).to_bytes(4, byteorder = "little")
    if len(b_mensaje)% 60 == 0:
        n_bloques = len(b_mensaje) // 60 
        completo = True
    else:
        n_bloques = len(b_mensaje) // 60 + 1
        completo = False
    b_mensaje_codificado = bytearray(b_largo_mensaje + b_tipo_mensaje)
    for i in range(n_bloques):
        b_mensaje_codificado += (i).to_bytes(4, byteorder = "little")
        if completo:
            b_mensaje_codificado += b_mensaje[60 * i : 60 * i + 60]
        elif i + 1 == n_bloques:
            contador = 0
            for byte in list(map(bytes, zip(b_mensaje[60 * i:]))):
                b_mensaje_codificado += byte
                contador += 1
            resto = 60 - contador
            resto_2 = b"\x00" * resto
            b_mensaje_codificado += resto_2
        else:
            b_mensaje_codificado += b_mensaje[60 * i : 60 * i + 60]

    return b_mensaje_codificado


# Decodificar un bytearray para obtener el mensaje original.
def decodificar_mensaje(mensaje):
    # COMPLETAR ESTA FUNCION
    pass


# Codificar una imagen a un bytearray segun el protocolo especificado.
def codificar_imagen(ruta):
    # COMPLETAR ESTA FUNCION
    pass


# Decodificar un bytearray a una lista segun el protocolo especificado.
def decodificar_imagen(mensaje):
    # COMPLETAR ESTA FUNCION
    pass
