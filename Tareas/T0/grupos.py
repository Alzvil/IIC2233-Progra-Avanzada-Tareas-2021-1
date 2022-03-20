from mensajes import separador_chats
from usuarios import inicio_sesion
from parametros import VOLVER_FRASE, ABANDONAR_FRASE
from datetime import datetime, date

def lista_grupos():
    #lee el archivo
    with open('grupos.csv', 'rt') as archivo_grupos:
        lista_grupos = archivo_grupos.readlines()
    for x in range(len(lista_grupos)):
        lista_grupos[x] = lista_grupos[x].strip().split(",")
    return lista_grupos

def dic_grupos():
    #crea un diccionario para agrupar los usuarios de cada grupo
    grupos = {}
    lista_grupos_para_dic = lista_grupos()
    variable = ""
    temporal = []
    nombres_grupos = []
    for elemento in lista_grupos_para_dic:
        if variable == "" or variable != elemento[0]:
            grupos[variable] = temporal
            nombres_grupos.append(variable)
            variable = elemento[0]
            temporal = []
            temporal.append(elemento[1])
        else:
            temporal.append(elemento[1])
    grupos[variable] = temporal
    nombres_grupos.pop(0)
    nombres_grupos.pop(0)
    return grupos, nombres_grupos

def grupos_usuario(ingresado):
    diccionario_grupos, nombres_grupos = dic_grupos()
    grupos_ingresado = []
    for elemento in diccionario_grupos:
        for usuario in diccionario_grupos[elemento]:
            if usuario == ingresado:
                grupos_ingresado.append(elemento)
    return grupos_ingresado

def chat_grupo(grupo):
    chat_grupo = []
    chats_grupos = separador_chats('nada', 'grupo')
    for elemento in chats_grupos:
        if elemento[2] == grupo:
            chat_grupo.append(elemento)
    return chat_grupo

def mostrar_mensaje(grupo):
    chat = chat_grupo(grupo)
    for elemento in chat:
        if chat == "vacio":
            print("Inicia la conversacion con este grupo")
            break
        else:
            print(f"[{elemento[3]}] De {elemento[1]}: '{elemento[4]}'")
    return

def eliminar_usuario(ingresado, grupo):
    lista = lista_grupos()
    for elemento in lista:
        if elemento[0] == grupo and elemento[1] == ingresado:
            lista.pop(lista.index(elemento))
    with open('grupos.csv', 'w') as archivo_grupos:
        for elemento in lista:
            escribir = f"{elemento[0]},{elemento[1]}"+"\n"
            archivo_grupos.write(escribir)
    with open('mensajes.csv', 'a') as archivo_chats:
        archivo_chats.write("\n")
        hora = datetime.now()
        fecha = datetime.today()
        envio = str(fecha.strftime("%Y/%m/%d")) + " " + str(hora.strftime("%H:%M:%S"))
        archivo_chats.write( \
        f"grupo,Sistema,{grupo},{envio},El usuario {ingresado} ha abandonado el grupo")
    mostrar_mensaje(grupo)
    return

def nuevo_mensaje(ingresado, grupo):
    print(f"Escribe una respuesta ¿o ingresa '{VOLVER_FRASE}' para regresar al menu de contactos")
    print(f"Si deseas abandonar el grupo escribe '{ABANDONAR_FRASE}', se notificará al grupo")
    texto = input()
    if texto == VOLVER_FRASE:
        return seleccion_grupo(ingresado)
    elif texto == ABANDONAR_FRASE:
        eliminar_usuario(ingresado, grupo)
        return "menu"
    else:
        hora = datetime.now()
        fecha = datetime.today()
        envio = str(fecha.strftime("%Y/%m/%d")) + " " + str(hora.strftime("%H:%M:%S"))
        mensaje = f"grupo,{ingresado},{grupo},{envio},{texto}"
        with open('mensajes.csv', 'a') as archivo_chats:
            archivo_chats.write("\n")
            archivo_chats.write(mensaje)
        mostrar_mensaje(grupo)
        return nuevo_mensaje(ingresado, grupo)

def seleccion_grupo(ingresado):
    print("***** Ver Grupos *****")
    print("Selecciona un grupo para ver tus conversaciones, o 0 para volver atras:")
    grupos_ingresado = grupos_usuario(ingresado)
    for x in range(len(grupos_ingresado)):
        print(f"[{x+1}] {grupos_ingresado[x]}")
    print("[0] Volver")

    seleccion = input("Ingrese el numero del usuario seleccionado: ")
    if seleccion == "0":
        #indica a menus.py que ejecute menu_grupos()
        return "menu"
    elif seleccion.isdigit() == False:
        print("Solo puedes ingresar numeros")
        return seleccion_grupo(ingresado)
    elif int(seleccion) < 1 or int(seleccion) > len(grupos_ingresado):
        print("El numero ingresado no es valido")
        return seleccion_grupo(ingresado)
    else:
        if grupos_ingresado[int(seleccion)-1] == "vacio":
            print("No tienes ningun grupo en tu lista, crea uno para comenzar a chatear")
            return seleccion_grupo(ingresado)
        else:
            print(f"chat del grupo '{grupos_ingresado[int(seleccion)-1]}'")
            #grupos_ingresado[int(seleccion)-1] -> grupo seleccionado, contraresta print(f"[x+1]")
            mostrar_mensaje(grupos_ingresado[int(seleccion)-1])
            accion = nuevo_mensaje(ingresado, grupos_ingresado[int(seleccion)-1])
            return accion

def crear_grupo(ingresado):
    nombre = input("Ingresa el nombre que tendra el grupo (minimo un caracter): ")
    if len(nombre) < 1:
        print("el nombre ingresado es de menos de un caracter")
        return
    desechable, grupos_existentes = dic_grupos()
    for elemento in grupos_existentes:
        if elemento == nombre:
            print("Este nombre ya esta en uso, ingrese otro")
            return
    print("Ahora debe registrar a los usuarios que formaran parte del grupo")
    print("Para esto deberas incluirte a ti mismo y seguir el siguiente formato:")
    print("tú;usuario2;usuario3;.....;usuarioN")
    print("Como minimo el grupo debe tener dos usuarios incluyendote")
    usuarios = input()
    correcto_1 = False
    correcto_2 = 0
    for elemento in usuarios:
        if elemento == ";":
            correcto_1 = True
            break
    if correcto_1 == True:
        usuarios = usuarios.split(";")
        if len(usuarios) < 2:
            print("No cumples con la cantidad minima de usuarios")
            return
        else:
            if usuarios[0] == ingresado:
                for elemento in usuarios:
                    existente = inicio_sesion(elemento)
                    if existente == True:
                        correcto_2 += 1
                    else:
                        print(f"El nombre de usuario {elemento} no existe")
                        return
            else:
                print("No te ingresaste primero en la lista")
                return
    else:
        print("El formato de la lista de usuarios no coincide con el especificado")
        return
    if correcto_2 == len(usuarios):
        with open('grupos.csv', 'a') as archivo_grupos:
            for elemento in usuarios:
                archivo_grupos.write(f"{nombre},{elemento}"+'\n')
        print("Grupo creado con exito, regresando al menu")
        return
    else:
        print("Ocurrio un error al crear el grupo")
        return