"""
Este módulo contiene funciones para el manejo general de los bytes de las
imágenes

Corresponde a la parte de Bytes
"""


def tuplas_desde_bytes(bytes_):
    """
    Recibe un bytearray proveniente de una imagen, que representa la información
    condensada de cada pixel. Se deben separar los pixeles (un pixel son 4 bytes
    en el bytearray) en una lista de tuplas.

    Argumentos:
        bytes_ (bytearray): La información a separar en tuplas.

    Retorna:
        list[tuple[int]]: lista de tuplas separadas
    """
    # Debes modificar esta función
    numeros = ""
    tuplas = []
    for e in bytes_:
        numeros += str(e)
    for i in range(0, len(numeros), 4):
        chunck = numeros[i:i+4]
        tuplas.append((int(chunck[0]), int(chunck[1]), int(chunck[2]), int(chunck[3])))
    return tuplas


def bytes_desde_tuplas(tuplas):
    """
    Recibe una lista de tuplas, y las transforma en un bytearray. Realiza la
    función inversa de tuples_from_bytes.

    Argumentos:
        tuplas (list[tuple[int]]): Lista de tuplas a juntar

    Retorna:
        bytearray: bytes resultantes de juntar las información de las tuplas
    """
    # Debes modificar esta función
    numeros = ""
    temp = []
    for e in tuplas:
        for a in e:
            numeros += str(a)
    for i in range(0, len(numeros), 3):
        chunck = numeros[i:i+3]
        temp.append(chunck)
    int(numeros)
    for e in numeros:
        temp.append(int(e))
    numeros = int(numeros)
    temp = numeros.to_bytes(length=(8 + (numeros + (numeros < 0)).bit_length()) // 8, byteorder='little', signed=True)
    return bytearray(str(temp), 'ascii', 'backslashreplace')


def recuperar_contenido(ruta):
    """
    Recibe una ruta referente al archivo corrompido, tu tienes que sobreescrivir ese mismo archivo
    despues de corrigirlo con el algoritimo mencionado en el Enunciado.
    """
    # Debes modificar esta función
    pass


def organizar_bmp(info_bytes):
    """
    Separa la información de la imagen en formato bmp en sus componentes
    principales

    Argumentos:
        info_bytes (bytearray): bytes representando la info de la imagen bmp

    Retorna:
        tuple[bytearray]: contiene el header, DIB Header, los pixeles, y el EOF
    """
    # No debes modificar esta función
    header = info_bytes[:15]
    dib_header = info_bytes[15:125]
    pixel_data = info_bytes[125:-1]
    eof = [info_bytes[-1]]
    return header, dib_header, pixel_data, eof


def int_desde_bytes(bytes_):
    """
    Decodifica el valor de un bytearray a un int con codificación little endian

    Argumentos:
        bytes_ (bytearray): Los bytes a decodificar

    Retorna:
        int: valor numérico correspondiente a los bytes
    """
    # No debes modificar esta función
    return int.from_bytes(bytes_, byteorder="little")


if __name__ == "__main__":
    """
    PUEDES PROBAR TU CÓDIGO AQUÍ
    """
    test = bytearray("qwertyui", 'ascii')
    a = tuplas_desde_bytes(test)
    print(a)
    b = bytes_desde_tuplas(a)
    print(b)
    print(b == test)