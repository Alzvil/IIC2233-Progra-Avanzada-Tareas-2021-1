from usuarios import inicio_sesion, nuevo_usuario
from contactos import seleccion_contacto, añadir_contacto
from grupos import seleccion_grupo, crear_grupo
    
def menu_contactos(ingresado):
    print("***** Menu de Contactos *****")
    print("Selecciona una opcion:")
    print("[1] Lista contactos")
    print("[2] Añadir contacto")
    print("[0] Volver")
    opcion = input("Indique su opcion (1, 2 o 0): ")

    if opcion == "1":
        # le pide a contactos.py que muestre 'ver contactos', retorna menu si debe volver
        temporal = seleccion_contacto(ingresado)
        if temporal == "menu":
            return menu_contactos(ingresado)
    elif opcion == "2":
        añadiendo = input("Escriba el nombre de usuario que desea agregar: ")
        if añadiendo == ingresado:
            print("No te puedes agregar a ti mismo")
            return menu_contactos(ingresado)
        comprobado = inicio_sesion(añadiendo)
        if comprobado == True:
            # le pide a contactos.py que lo añada
            añadir_contacto(ingresado, añadiendo)
        else: 
            print("Usuario no encontrado")
        return menu_contactos(ingresado)
    elif opcion == "0":
        return menu_chats(ingresado)
    else:
        print("Opcion invalida, por favor ingrese solamente el numero '1', '2' o '3'")
        return menu_contactos(ingresado)

def menu_grupos(ingresado):
    print("***** Menu de Grupos *****")
    print("Selecciona una opcion:")
    print("[1] Lista grupos")
    print("[2] Crear grupo")
    print("[0] Volver")
    opcion = input("Indique su opcion (1, 2 o 0): ")

    if opcion == "1":
        #le pide a grupos.py que muestre 'ver grupos', y ejecuta la funcion para mostrar el chat
        #mostrar el chat se encarga también de llamar a la de salir del grupo, enviar nuevo mensaje
        temporal = seleccion_grupo(ingresado)
        if temporal == "menu":
            return menu_grupos(ingresado)
    elif opcion == "2":
        crear_grupo(ingresado)
        return menu_grupos(ingresado)
    elif opcion == "0":
        return menu_chats(ingresado)
    else:
        print("Opcion invalida, por favor ingrese solamente el numero '1', '2' o '0'")
        return menu_contactos(ingresado)

def menu_chats(ingresado):
    print("***** Menu de Chats *****")
    print("Selecciona una opcion:")
    print("[1] Ver contactos")
    print("[2] Ver grupos")
    print("[0] Volver")
    opcion = input("Indique su opcion (1, 2 o 0): ")

    if opcion == "1":
        return menu_contactos(ingresado)
    elif opcion == "2":
        return menu_grupos(ingresado)
    elif opcion == "0":
        menu_inicio()
    else:
        print("Opcion invalida, por favor ingrese solamente el numero '1', '2' o '3'")
        menu_chats(ingresado)
    return

def menu_inicio():
    print("***** Menu de Inicio *****")
    print("Selecciona una opcion:")
    print("[1] Crear usuario")
    print("[2] Iniciar sesion")
    print("[0] Salir")
    opcion = input("Indique su opcion (1, 2 o 0): ")
    
    if opcion == "1":
        ingresado = input("Ingrese su nuevo usuario (3 a 15 caracteres sin ','): ")
        comprobado = nuevo_usuario(ingresado)
        #siempre me referire al usuario como ingresado, en todos los modulos
        if comprobado == True:
            menu_chats(ingresado)
        else:
            print(comprobado)
            menu_inicio()
    elif opcion == "2":
        ingresado = input("Ingrese su usuario: ")
        comprobado = inicio_sesion(ingresado)
        if comprobado == True:
            return menu_chats(ingresado)
        else:
            print("Nombre de usuario no encontrado")
            return menu_inicio()
    elif opcion == "0":
        print("Adios")
        return
    else:
        print("Opcion invalida, por favor ingrese solamente el numero '1', '2' o '3'")
        return menu_inicio()

#CODIGO PRINCIPAL:
menu_inicio()