# Tarea X: Nombre de la tarea :school_satchel:


Sinceramente la tarea hace muy poco, solo está implementada la parte del servidor y el inicio del cliente. Lamentablemente, me veo en obligación de llorar un poco. En realidad solo necesito un 3.0, puesto que lo único que me falta es el promedio sobre 3.95 en tareas, no contaba con esta condición, lamentablemente me enteré pocos días antes de la entrega original y todo fue un desastre. Pero en fin, solo necesitaba desahogarme un poco :(

<En la seccion de "LibreriasPropias" se encuentra un desgloce de todo lo que hace el código>

### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Networking>: Hecha casi completa
    - Está el server se inicia e intenta sacar el host y puerto de parametros pero el json no funciona
    - Tiene un archivo de logica donde se encuentra la funcion que verifica la validez del usuario
* <Arquitectura cliente-servidor>: Hecha casi completa
    - Separacion de backend y frontend
    - Se llama a la ventana de inicio
* <Manejo de bytes>: No realizado
* <Interfaz gráfica>: Están todas las plantillas y solo se encuentra implementada la ventana de inicio (login)
* <Grafo>: No realizado
* <Reglas de DCCópteros>: No realizado
* <General>: Intenté hacer parametros pero no funciona
* <Bonus>: Nada

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py``` de la carpeta servidor y cliente. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```sprites``` en ```frontend``` en ```cliente```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

<a "IMPORTANTE" a>

1. ```servidor/main```: Contiene a ```Clase Servidor```
    - Capaz de iniciar llamando al host y port de parametros.json (no funciona el json)
    - Añade hasta 4 clientes al servidor de forma activa (en partida) y ademas incorpora una cola para aceptar a los usuarios extras (arriba de 4 clientes) e irlos añadiendo a medida que los otros activos salen del servidor
    - elimina a clientes y cierra el servidor
    - log implementado
    - lock implementado
2. ```servidor/logica```: Hecha como backend de servidor
    - Revisa las restricciones en el nombre de usuario
3. ```cliente/main```: Contiene a ```Clase Cliente```
    - inicia el cliente en los puertos correspondientes
4. ```cliente/interfaz```: Hecha para manejar las conexiones de backend y frontend y ademas entregar la parte grafica al cliente
    - llama a ventana de inicio, considera que se envie el nombre de usuario para verificarlo al servidor (pero no llega a este)
5. ```cliente/frontend/preparacion```: Contiene a ```Clase Cliente```
    - contiene a la clase de ventana inicio, considera enviar el nombre de usuario para ser verificado al servidor y no al backend

## PD :thinking:

1. Piedad :(
2. Gracias :(

-------