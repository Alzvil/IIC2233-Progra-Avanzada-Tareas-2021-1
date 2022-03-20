from collections import namedtuple


def cargar_platos(ruta_archivo):
    platos = []
    platos_dic = {}

    with open(ruta_archivo,'rt') as archivo_platos:
        archivo_platos = archivo_platos.readlines()

    for elemento in archivo_platos:
        temporal = elemento.strip().split(",")
        for x in range(len(temporal)):
            numero = temporal[x].isdigit()
            if numero == True:
                temporal[x] = int(temporal[x])

        lista_ingredientes = temporal[4:]
        set_ingredientes = set(lista_ingredientes)

        nombre_tupla = temporal[0]
        nombre_tupla = nombre_tupla.lower()
        nombre_tupla = nombre_tupla.replace(" ","")

        categoria = temporal[1]
        tiempo_preparación = temporal[2]
        precio = temporal[3]

        tupla_plato = namedtuple(nombre_tupla, ['categoria', 'tiempo_preparación', 'precio','ingredientes'])
        plato = tupla_plato(categoria, tiempo_preparación, precio, set_ingredientes)

        platos_dic[temporal[0]] = plato
    return platos_dic


def cargar_ingredientes(ruta_archivo):
    # COMPLETAR ESTA FUNCIÖN
    with open(ruta_archivo,'rt') as archivo_ingredientes:
        archivo_ingredientes = archivo_ingredientes.readlines()


if __name__ == "__main__":
    # ================== PUEDES PROBAR TUS FUNCIONES AQUÍ =====================
    print(" PRUEBA CARGAR ".center(80, "="))
    a=cargar_platos("C:\\Users\\ville\\Desktop\\GitHub\\[IIC2233] Programación Avanzada (2021-1)\\Alzvil-iic2233-2021-1\\Actividades\\AF1\\platos.csv")
    print(a)