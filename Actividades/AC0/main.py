# Debes completar esta función para que retorne la información de los ayudantes
def cargar_datos(path):
    b=[]
    a= open(path)
    a=a.readlines()
    for e in a:
        #print(e)
        e=e.strip().split(",")#.strip()
        b.append(e)
    #print(a)
    #print(b)
    return b


# Completa esta función para encontrar la información del ayudante entregado
def buscar_info_ayudante(usuario, lista_ayudantes):
    #b=[]
    k=""
    #print(usuario)
    #for e in lista_ayudantes:
        #e=e.split(",")
        #b.append(e)
    for e in lista_ayudantes:
        #print(e)
        #print(e[2])
        if usuario==e[2]:
            k=e
    return k


# Completa esta función para que los ayudnates puedan saludar
def saludar_ayudante(info_ayudante):
    #print("No habia ejemplo asi que invente un saludo :)")
    #print("Hola soy "+info_ayudante[0]+" mi cargo es "+info_ayudante[1]+" y me puedes encontrar en discord como "+info_ayudante[2])
    return f"Hola soy {info_ayudante[0]} mi cargo es {info_ayudante[1]} y me puedes encontrar en discord como {info_ayudante[2]}"


if __name__ == '__main__':
    # ===================== NO MODIFICAR ESTA SECCIÓN =========================
    print(" TEST DE FUNCIONES ".center(80, "="))
    datos = cargar_datos('C:\\Users\\ville\\Desktop\\GitHub\\[IIC2233] Programación Avanzada (2021-1)\\Alzvil-iic2233-2021-1\\Actividades\\AC0\\ayudantes.csv')
    if datos is not None:
        print('Se lograron leer los datos')
    else:
        print('Debes completar la carga de datos')

    test_info_ayudante = buscar_info_ayudante("DCCollao", datos)
    if test_info_ayudante is not None and test_info_ayudante[2] == "DCCollao":
        print('\nSe logró buscar la información de los ayudantes')
    else:
        print('\nNo se ha completado la función: buscar_info_ayudante')

    test_saludo = saludar_ayudante(["Test", "niguno", "test_ayudante"])
    if test_saludo is not None and type(test_saludo) is str:
        print('\nLos ayudantes saludan correctamente.')
    else:
        print('\nDebes completar el saludo de ayudantes')

    print("="*80)
    if datos:
        print('\n Los ayudantes son:')
        for i in range(0, len(datos), 4):
            line = f"@{datos[i][2]:20s}"
            if i + 1 < len(datos):
                line += f"@{datos[i+1][2]:20s}"
            if i + 2 < len(datos):
                line += f"@{datos[i+2][2]:20s}"
            print(line)

    if test_info_ayudante and test_saludo:
        print('\nIngresa el usuario de un ayudante para saludarlo')
        ayudante = input("@")
        if ayudante:
            print(saludar_ayudante(buscar_info_ayudante(ayudante, datos)))
