import requests


# ------------------------------------------------------------------------------------------------
# DEFINIR AQUI LAS CONSTANTES QUE SERAN UTILIZADAS PARA INTERACTUAR CON LA API
NOMBRE = "Alan Guzman"
USERNAME = "Alzvil"
DOCUMENTO = 1


# ------------------------------------------------------------------------------------------------
# Completar a continuación el código para realizar las solicitudes necesarias a la API. Cada
# función recibe los argumentos necesarios para realizar la consulta y aplicar lógica adicional,
# en caso de ser necesario

# Registro en aplicación
#EXTRAIDO DE CONTENIDOS DEL CURSO
def registro(nombre, username):
    datos_alumno = {
        "nombre": nombre,
        "usuario": username,
    }
    respuesta = requests.post(
        "https://actividad-bonusiic2233.herokuapp.com"
        .format("/estudiantes"), data=datos_alumno
    )
    return respuesta.status_code


# Descarga de documento Markdown
def descargar_documento(identificador_documento, ruta_documento):
    # Obtener documento Markdown
    # Guardar texto en un archivo
    pass


# Probar una de las consulas
def entregar_consulta(n_consulta, identificador_documento, patron, respuesta):
    # Subir resultados a API
    # Retornar identificador de proceso
    pass
