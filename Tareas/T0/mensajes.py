from parametros import VOLVER_FRASE
from datetime import datetime, date

def lista_chats():
    with open('mensajes.csv', 'rt') as archivo_chats:
        lista_chats = archivo_chats.readlines()
    for x in range(len(lista_chats)):
        lista_chats[x] = lista_chats[x].strip().split(",")
    return lista_chats

def separador_chats(regular, grupo):
    lista_regular = []
    lista_grupo = []
    for elemento in lista_chats():
        if elemento[0] == "grupo":
            lista_grupo.append(elemento)
        elif elemento[0] == "regular":
            lista_regular.append(elemento)
    if regular == "regular":
        return lista_regular
    elif grupo == "grupo":
        return lista_grupo

def mostrar_mensajes(ingresado, receptor):
    chats_regulares = separador_chats("regular", "nada")
    chat_solicitado = []
    for elemento in chats_regulares:
        if elemento[1] == ingresado and elemento[2] == receptor:
            chat_solicitado.append(elemento)
        if elemento[1] == receptor and elemento[2] == ingresado:
            chat_solicitado.append(elemento)
    #HACER QUE ORDENE EN FORMA ASCENDENTE
    if chat_solicitado == []:
        return "vacio"
    else:
        return chat_solicitado

def enviar_mensaje(ingresado, receptor):
    print(f"Escribe una respuesta o ingresa '{VOLVER_FRASE}' para regresar al menu de contactos")
    texto = input()
    if texto == VOLVER_FRASE:
        return True
    else:
        hora = datetime.now()
        fecha = datetime.today()
        envio = str(fecha.strftime("%Y/%m/%d")) + " " + str(hora.strftime("%H:%M:%S"))
        mensaje = f"regular,{ingresado},{receptor},{envio},{texto}"
        with open('mensajes.csv', 'a') as archivo_chats:
            archivo_chats.write("\n")
            archivo_chats.write(mensaje)
        chat = mostrar_mensajes(ingresado, receptor)
        for elemento in chat:
            print(f"[{elemento[3]}] De {elemento[1]}: '{elemento[4]}'")
        return enviar_mensaje(ingresado, receptor)