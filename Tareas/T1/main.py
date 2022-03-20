from parametros import DINERO_INICIAL
from canales import Canales, simular_nueva_hora, barcos_no_ingresados
from archivos import lista_canales, lista_barcos, creacion_instancias_barco

def menu_inicio():
    print("====[ Bienvenido a DCCanal ]====")
    print("> Selecciona una opcion:")
    print(">>> [1] Iniciar nueva simulacion")
    print(">>> [0] Salir del programa")
    selec_inicio = input("Ingresa 1 o 0: ")
    if selec_inicio == "1":
        return menu_canales()
    elif selec_inicio == "0":
        print("> Finalizando programa")
        return
    else:
        print("> Opcion invalida, ingrese solamente 1 o 0")
        return menu_inicio()
    
def menu_canales():
    canales = lista_canales()
    print("====[ Seleccion de canal ]====")
    print("> Selecciona una opcion:")
    for x in range(len(canales)):
        print(f">>> [{x+1}] {canales[x][0]}, dificultad: {canales[x][2]}")
    print(">>> [0] Volver")
    selec_canal = input("Ingresa el numero correspondiente: ")

    if selec_canal == "0":
        return menu_inicio()
    elif errores_seleccion(selec_canal, len(canales)) == False:
        print(f"> Iniciando simulacion de {canales[int(selec_canal)-1][0]}")
        simulacion = Canales(
            canales[int(selec_canal)-1][0],
            DINERO_INICIAL,
            canales[int(selec_canal)-1][1],
            canales[int(selec_canal)-1][2]
            )
        return menu_acciones(simulacion)
    else:
        return menu_canales()

def menu_acciones(canal):
    ingresado = False
    print("====[ Menu de acciones ]====")
    print(f"> Estado: Canal {canal.nombre}, Dificultad {canal.dificultad}")
    print("> Selecciona una accion:")
    print(">>> [1] Mostrar riesgo de encallamiento")
    print(">>> [2] Desencallar barco")
    print(">>> [3] Simular nueva hora")
    print(">>> [4] Mostrar estado de la simulacion")
    print(">>> [0] Volver")
    selec_accion = input("Ingresa el numero correspondiente: ")

    if selec_accion == "0":
        return menu_canales()

    elif selec_accion == "1":
        if canal.barcos == []:
            print("> No hay barcos cruzando ahora por el canal")
        else:
            for barco in canal.barcos:
                print(f">> {barco.nombre}, probabilidad de encallar: {barco.prob_encallar}")
        return menu_acciones(canal)

    elif selec_accion == "2":
        if canal.barcos == []:
            print("> No hay barcos cruzando ahora por el canal")
        else:
            encallados = []
            for barco in canal.barcos:
                if barco.encallado == True:
                    encallados.append(barco)
            if encallados == []:
                print()
            else:
                print("> Selecciona una opcion:")
                for x in range(len(encallados)):
                    print(f">>> [{x+1}] {encallados[x].nombre}")
                print(">>> [0] Volver")
                selec_desenc = input("Ingresa el numero correspondiente: ")
                if selec_desenc == "0":
                    return menu_acciones(canal)
                elif errores_seleccion(selec_desenc, len(encallados)) == False:
                    canal.desencallar_barcos(encallados[int(selec_desenc)-1])
                else:
                    return menu_acciones(canal)
        return menu_acciones(canal)

    elif selec_accion == "3":
        accion = simular_nueva_hora(canal, barcos)
        if accion == "inicio":
            return menu_inicio()
        elif accion == "acciones":
            return menu_acciones(canal)

    elif selec_accion == "4":
        print("------------------------------------------------------------------")
        print("                         Estado del canal                         ")
        print("------------------------------------------------------------------")
        print(f"{canal.nombre} de {canal.largo} Km de largo, con dificultad {canal.dificultad}")
        print(f"Horas simuladas: {canal.hora}")
        print(f"Dinero disponible: {canal.dinero}")
        print(f"Dinero gastado: {canal.gastado}")
        print(f"Dinero recibido: {canal.recibido}")
        print(f"Numero de barcos que pasaron: {canal.pasaron}")
        print(f"Numero de barcos que encallaron: {canal.encallados}")
        print(f"Eventos especiales ocurridos: {canal.eventos}")
        return menu_acciones(canal)

    else:
        print("> Opcion invalida, ingrese solamente 1, 2, 3, 4 o 0")
        return menu_acciones(canal)

def errores_seleccion(selec, rango):
    if selec.isdigit() == False: 
        print("> Opcion invalida, ingrese solamente los numeros disponibles")
        return True
    elif int(selec) < 0 or int(selec) > rango:
        print("> Opcion invalida, ingrese solamente los numeros disponibles")
        return True
    else:
        return False

#main
barcos = creacion_instancias_barco()
menu_inicio()