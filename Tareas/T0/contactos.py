from mensajes import mostrar_mensajes, enviar_mensaje

def lista_contactos():
    #lee el archivo
    with open('contactos.csv', 'rt') as archivo_contactos:
        lista_contactos = archivo_contactos.readlines()
    for x in range(len(lista_contactos)):
        lista_contactos[x] = lista_contactos[x].strip().split(",")
    return lista_contactos

def dic_contactos():
    #crea un diccionario para agrupar los contactos de cada usuario
    contactos = {}
    lista_contactos_para_dic = lista_contactos()
    variable = ""
    temporal = []
    for elemento in lista_contactos_para_dic:
        if variable == "" or variable != elemento[0]:
            contactos[variable] = temporal
            variable = elemento[0]
            temporal = []
            temporal.append(elemento[1])
        else:
            temporal.append(elemento[1])
    contactos[variable] = temporal
    return contactos

def seleccion_contacto(ingresado):
    #implementa el menu de contactos y llama a la funcion de mensajes.py para los chats regulares
    print("***** Ver Contactos *****")
    print("Selecciona un usuario para ver tus conversaciones, o 0 para volver atras:")
    contactos = dic_contactos()
    contactos_ingresado = contactos[ingresado]
    # QUE HACER CUANDO NO TIENE UNA LISTA DE CONTACTOS
    for x in range(len(contactos_ingresado)):
        print(f"[{x+1}] {contactos_ingresado[x]}")
    print("[0] Volver")

    seleccion = input("Ingrese el numero del usuario seleccionado: ")
    if seleccion == "0":
        #indica a menus.py que ejecute menu_chats()
        return "menu"
    elif seleccion.isdigit() == False:
        print("Solo puedes ingresar numeros")
        return seleccion_contacto(ingresado)
    elif int(seleccion) < 1 or int(seleccion) > len(contactos_ingresado):
        print("El numero ingresado no es valido")
        return seleccion_contacto(ingresado)
    else:
        if contactos_ingresado[int(seleccion)-1] == "vacio":
            print("No tienes ningun contacto en tu lista, añade uno para comenzar a chatear")
            return seleccion_contacto(ingresado)
        else:
            print(f"chat con [{seleccion}] '{contactos_ingresado[int(seleccion)-1]}'")
        #llama a mensajes.py para ver los mensajes regulares
        #contactos_ingresado[int(seleccion)-1] -> contacto seleccionado, contraresta print(f"[x+1]")
            chat = mostrar_mensajes(ingresado, contactos_ingresado[int(seleccion)-1])
            for elemento in chat:
                if chat == "vacio":
                    print("Inicia la conversacion con este usuario")
                    break
                else:
                    print(f"[{elemento[3]}] De {elemento[1]}: '{elemento[4]}'")
        #llama a mensajes.py para enviar un nuevo mensaje y retorna True si escribre //volver
            regresar = enviar_mensaje(ingresado, contactos_ingresado[int(seleccion)-1])
            if regresar == True:
                return seleccion_contacto(ingresado)

def añadir_contacto(ingresado, añadiendo):
    directo = [ingresado, añadiendo]
    inverso = [añadiendo, ingresado]
    contactos = lista_contactos()
    for elemento in contactos:
        if elemento == [ingresado, añadiendo] or elemento == [añadiendo, ingresado]:
            print("Ya tienes agregado a este contacto")
            return 
        elif elemento[0] == ingresado:
            indice_directo = contactos.index(elemento)
            if elemento[1] == "vacio":
                contactos.pop(contactos.index(elemento))
        elif elemento[0] == añadiendo:
            indice_inverso = contactos.index(elemento)
            if elemento[1] == "vacio":
                contactos.pop(contactos.index(elemento))
    contactos.insert(indice_directo, directo)
    contactos.insert(indice_inverso, inverso)
    with open('contactos.csv', 'w') as archivo_contactos:
        for elemento in contactos:
            escribir = f"{elemento[0]},{elemento[1]}"+"\n"
            archivo_contactos.write(escribir)
    return
