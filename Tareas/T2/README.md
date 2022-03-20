# Tarea 2: DCCimpsons :school_satchel:


Para economizar espacio, en este readme se abordarán solo los puntos implementados, se puede asumir que lo no nombrado aquí no se encuentra implementado.

## Consideraciones generales :octocat:

La tarea abre todas las ventanas hasta la de la juego, permite moverse, colisionar y aparecen los obstaculos. (solo eso)

### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Ventana inicio>: Hecha completa
    - Funcionan todos los botones y revisa que el nombre sea alfanumerico
* <Ventana ranking>: Planificada, <no muestra las puntuaciones y no se genera el archivo>
    - Abre y se encuentra implementada, pero no genera el archivo y no muestra los puntajes
* <Ventana preparacion>: Casi completa, <no funcionan los botones ni estadisticas>
    - Se puede seleccionar cualquiera de los personajes, este se mueve solo dentro del espacio de la calle
    - Se puede colisionar con un edificio, solo el que le corresponda para iniciar inmediatamente el juego
* <Ventana juego>: Casi completa <no funcionan los botones, no cuenta tiempo, no esta implementado gorgory, no aparecen objetos, no funcionan las habilidades, los atajos de teclado, pausa, y existe un bug con la colision con obstaculos>
    - Se puede desplazar a través del tablero
    - Se personaliza la ventana de acuerdo al personaje seleccionado
* <Ventana post-ronda>: No implementada
* <Mecanicas de juego>: Casi completa, se verá abajo
    - Movimiento: de personajes fluido, respeta colisiones con obstaculos, chequea con qué tipo de entidad chocó
    - Objetos teóricamente implementados
    - Aparecen los obstaculos con el sprite correspondiente al personaje de forma aleatoria y no contiguos uno del otro
* <Cheatcodes>: No implementada
* <Bonus>: Música
    - La música se encuentra implementada

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. Carpeta ```assets``` en carpeta ```frontend```
2. Carpeta ```sprites``` en ```assets```, contiene las carpetas entregas en el Syllabus con todos los sprites (se pueden ver detalles de los paths en parametros.py)
3. Carpeta ```canciones``` en ```assets```, contiene la musica


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5 y PyQt5-tools```: Se debe tener instalado, librería principal del programa utilizada en el 90% de los modulos
2. ```sys```: ```ejecución del programa / main.py ventana_inicio.py```
3. ```abc```: ```clases de entidades / objetos.py personajes.py```
4. ```os```: ```paths relativos / parametros.py```
5. ```collections```: ```diccionario con la grilla del tablero de juego / ventana_juego.py```
6. ```random```: ```determinar la aparición de los obstaculos / logica_juego.py```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```parametros```: Contiene a las rutas y parametros especificados en el enunciado
2. ```utiles```: Esta libreria fue pensada para optimizar ciertos mecanismos en el codigo y ahorrar en el uso de señales
    - Mantiene los datos de puntaje, nombre usuario, cantidad de objetos y demás aspectos que son generales para todos los modulos del programa
    - Organiza los sprites de personajes para entregarlos en una sola lista que es usada dentro del juego para generar el movimiento fluido
3. ```objetos```: Contiene toda la logica que utilizarían los tres tipos de objetos en el juego
    - No se alcanzó a implementar pero favor considerar las cosas planificadas
4. ```personajes```: Contiene toda la logica que utilizarían los cuatro personajes en el juego
    - No se alcanzó a implementar pero favor considerar las cosas planificadas
5. ```ventana_inicio```: (Frontend) Maneja las clases VentanaInicio y VentanaRanking
    - VentanaRanking está implementada, abre y tiene una grilla para mostrar los puntajes
6. ```ventana_juego```: (Frontend) Maneja las clases VentanaPreparacion y VentanaJuego
    - La planificación de pausa está realizada y semi implementada en algunas partes
    - Se intentó implementar los cheatcodes pero estos no funcionan
    - Bug de colision: solo cuando el personaje colisiona con un objeto, estos se clipean y el programa determina que quedan en constante colision, de igual forma, comprueba con qué elemento es el que está colisionando, y esto no ocurre con los bordes del mapa
    - Todos los aspectos de las ventanas se encuentran diseños en la plantilla, aunque no todos son funcionales
7. ```logica_juego```: (Backend) Maneja la aparición de los obstaculos
8. ```ventana_inicio_backend```: (Backend) Ve que el usuario sea alfanumerico y contiene a la función encargada de la música

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
0. Gran parte de la tarea está inspirada en la <Actividad Sumativa 2>, especificamente:
    - La inicialización de las clases
    - La música
    - La lista que maneja los qlabels del tablero es una modificación del diccionario usado en la AS2
    - El evento de presionar teclas
    - Entre otros
1. \<https://pythonbasics.org/pyqt-radiobutton/>: este hace \<Cómo usar el Radiobutton> y está implementado en el archivo ```ventana_juego.py``` en la clase <VentanaPreparacion>
2. \<https://youtu.be/eM8SNjgo2Y0/>: este hace \<Como mover el personaje> y está implementado en el archivo ```ventana_juego.py``` en ambas clases

## útlimo mensaje

Favor considerar los detalles expuestos en librerias propias y otorgar el máximo puntaje posible :(
Fue una semana horrible que me dejó muy poco tiempo para poder continuar la tarea, la realicé considerando que lo principal eran los aspectos del juegos, por ende las ventanas secuendarias y botones secundarios no se encuentran implementados. La mayoría del código responde a ejecutar aspectos del movimiento, interacción con el tablero y manejo de sprites.
Piedad pls :(