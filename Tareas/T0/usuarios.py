def lista_usuarios():
    with open('usuarios.csv', 'rt') as archivo_usuarios:
        lista_usuarios = archivo_usuarios.readlines()
    for x in range(len(lista_usuarios)):
        lista_usuarios[x] = lista_usuarios[x].strip()
    return lista_usuarios

def inicio_sesion(ingresado):
    comprobado = False
    usuarios = lista_usuarios()
    for usuario in usuarios:
        if usuario == ingresado:
            comprobado = True
    if comprobado == True:
        return True
    else:
        return False

def nuevo_usuario(ingresado):
    ocupado = inicio_sesion(ingresado)
    if ocupado == True:
        return "Nombre de usuario no disponible"
    if len(ingresado) >= 3 and len(ingresado) <= 15:
        pass
    else:
        return "El nombre no tiene de 3 a 15 caracteres"
    for elemento in ingresado:
        if elemento == ',':
            return "El nombre contiene ','"
    with open('usuarios.csv', 'a') as archivo_usuarios:
        archivo_usuarios.write("\n")
        archivo_usuarios.write(ingresado)
    with open('contactos.csv', 'a') as archivo_contactos:
        nuevo_texto = f"{ingresado},vacio"+"\n"
        archivo_contactos.write(nuevo_texto)
    return True