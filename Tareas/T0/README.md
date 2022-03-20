# Tarea 0: DCConectado

======================================================================================================

## Consideraciones generales 

La tarea realiza todas las funciones solicitadas por "TO Distribución de Puntaje", lo único que no fue implementado es que el programa ordene manualmente el historial de mensajes según la fecha en la que fue enviado. Para mostrarlos se asume que estan ordenados cronologicamente y se muestran ascendentemente.                                     

======================================================================================================

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Menú de inicio: Hecha completa
* Flujo de programa: Hecha completa
    * Menú de chats: Hecho completa
    * Menú de contactos: Hecha completa. Se asume que mensajes.csv tiene orden cronológico
    * Menú de grupos: Hecha completa 
* Chat regulares y grupo: Hecha completa. Se asume que mensajes.csv tiene orden cronológico
* Manejo de archivos: Hecha completa

======================================================================================================

## Ejecución
El módulo principal de la tarea a ejecutar es  ```menus.py```. Todos los modulos (5 + parametros.py) se deben encontrar en la misma carpeta.
Además todos los archivos .csv deben encontrarse en la misma carpeta puesto que son llamados con el path: "nombre.csv"

======================================================================================================

### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. La libreria entregada ```parametros.py``` 
2. ```datetime```: para colocar la fecha ```.now/.today/.strftime``` en los mensajes nuevos en los modulos mensajes.py y grupos.py

======================================================================================================

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus.py```: Se encarga de trabajar todos los menús, no incluye a "ver contactos" ni "ver grupos"
    1. A) Trabaja con los modulos usuarios, contactos y grupos.py

2. ```usuarios.py```: Es solicitada por el menú de inicio para el registro e inicio de sesión. La función ```inicio de sesión``` al ser la que trabaja con el archivo "usuarios.csv" será la encargada de comprobar la existencia del usuario en todo el programa

3. ```contactos.py```: Crea un diccionario donde se almacena la lista de contactos de cada usuario, también se encarga de ejecutar el menú ```ver contactos``` y realizar la función de ```añadir contacto```
    3. A) Trabaja con el modulo mensajes.py cuando se selecciona un historial en "ver contactos"

4. ```mensajes.py```: Entrega la función ```separador``` que da dos listas independientes, una con los "chats regulares" (para contactos.py) y otra con los "chats grupales" (para grupos.py). También se encarga de ```mostrar mensajes``` y ```nuevo mensaje``` para los "chats regulares" de "contactos.py"
    4. A) Trabaja con los modulos "parametros.py" y "datatime" como se explica en "Librerías externas"

5. ```grupos.py```: El modulo trabaja todas las funciones solicitadas por "menú de chats" y se encarga de mostrar "ver grupos" en  ```seleccionar_grupo```, además de ejecutar todas sus funciones.
    5. A) Trabaja con los modulos "parametros.py" y "datatime" como se explica en "Librerías externas"
    5. B) Trabaja con los modulos "usuarios.py" (tal como se explica en el punto 2) y "mensajes.py" (como dice el punto 4)

======================================================================================================

## Supuestos y consideraciones adicionales
Los supuestos que realicé durante la tarea son los siguientes:

1. El archivo ```mensajes.csv``` contiene los chats en orden cronológico, puesto que al revisarlo no se encontraron fallos en esto y los nuevos mensajes son agregados respetando lo anterior.

2. Por un error de tipeo en los menús en algún momento saldrá ```ingrese solamente el numero '1', '2' o '3'``` aunque debiera decir ```1, 2 o <<0>>```. Aunque esto no afecta el funcionamiento del código y la opción de ```volver``` siempre correspondera a ```0``` y no ```3```

3. El ```menú de contactos``` considera los siguientes aspectos no contemplados en el enunciado:
    A) No te puedes añadir a ti mismo en contactos
    B) No puedes añadir más de una vez al mismo contacto
    C) Cuando no se tiene ningún contacto agregado se muestra como primera opción "vacio", para un correcto funcionamiento del resto de partes del código. Se puede abrir una instancia de chat con "vacio", pero una vez añadido el primer contacto se borrará su acceso desde el menú "ver contactos" (ya no se podrá ver el chat con "vacio") aunque el historial seguirá presente en "mensajes.csv"
    D) ```inicio_sesion``` solo comprueba si es que existe un usuario con ```exactamente``` el mismo nombre, y es valido poder registrarse como "Alzvil" aunque "alzvil" ya exista.
    E) El programa tirará un error al momento de eliminar todos los contactos, puesto que la variable "vacio" del punto 3.C no se volverá a crear y esto afectará al resto de las funciones que leen el diccionario de contactos.

3. El ```menú de grupos``` considera los siguientes aspectos:
    A) Los mensajes de ```abandonar grupo``` tienen como emisor a "El Sistema", y una vez abandonado se printeara por última vez el chat
    B) Aunque el requerimiento para crear un grupo sea de 2 usuarios, si uno de estos lo abandona y queda solo con un ususario registrado, el grupo no se eliminará hasta que el usuario restante también lo abandone
    C) Al igual que el punto 3.C, también se considera la variable "vacio" para usuarios recién registrados y puede llegar a presentar los problemas del punto 3.E

4. ```ESTO NO DEBERÍA PASAR``` pero si en algún momento el programa tira un error de ```lista fuera de index``` es porque un ```\n``` se ejecuto mal a la hora de agregar una nueva variable en los ```archivos.csv``` (dejando una linea en blanco) lo que afecta al código que lee las listas cuando estos se abren. Ya fue testeado y cada archivo.csv tiene un \n (antes o al final de la línea) según su configuración en el syllabus.

======================================================================================================

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>
1. El archivo ```mensajes.csv``` contiene los chats en orden cronológico, puesto que al revisarlo no se encontraron fallos en esto y los nuevos mensajes son agregados respetando lo anterior.

======================================================================================================

## Referencias de código externo

Para realizar mi tarea saqué código de:
1. ```datetime``` de la página: https://www.programiz.com/python-programming/datetime

