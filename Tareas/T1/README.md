# Tarea 1: DCCanales
# Alan Guzmán Villena

======================================================================================================

## Consideraciones generales 

La tarea realiza casi todas las funciones solicitadas en "T1 Distribución de Puntaje", cada punto se explica en detalle abajo.
El archivo principal es "main.py" y se debe encontrar en la misma carpeta que todos los modulos y archivos.csv

======================================================================================================

### Cosas implementadas y no implementadas :white_check_mark: :x:
* Hecho en base a la distribución de puntaje

*PD*: Programar (Está escrito en el código), Falto Implementar (No es ejecutado en main.py ni usado, solo está escrito)

* Programación orientada a objetos: Programada casi completa
    * Barcos: Me falto programar el evento especial de barcos
    * Mercancía: Programada, aunque expiración no es implementada
    * Tripulación: Programada, aunque los efectos especiales no son implementados
    * Canales: Hecha completa
    * Clases abstractas: Corresponde a Barco y Tripulante, los métodos abstractos están en algunos programados pero no todos implementados
    * Relaciones: las indicadas por el diagrama, perdón por que algunas flechas se vean mal, me quedé sin tiempo :(

* Simulaciones: Hecha completa
    * Menú de canales: Hecha completa
    * Instanciar canal: Hecha completa
    * Instanciar barco: Hecha completa
    * Instanciar tripulantes: Hecha completa
    * Instanciar mercancias: Hecha completa

* Barcos: Programada casi completa, lo programado está todo implementado
    * Menú de barcos en simular hora: Hecha completa
    * Desplazarce: Hecha completa
    * Encallar: Hecha completa
    * Atributos: Eventos especiales no programados

* Tripulantes: Programada completa, no todo está implementado
    * Habilidades: Las habilidades de los tripulantes están programadas pero no implementadas
    * Asignación: Hecha completa

* Mercancía: Programada completa, no todo está implementado
    * Asignación: Hecha completa
    * Expirar: Programado pero no implementado
    * Multas: No hecho

* Canales: Hecha completa
    * Desencallar: Hecha completa
    * Divisas: Hecha completa
    * Ingresar barcos: Hecha completa

* Menus: Hechos completos

======================================================================================================

## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```. Todos los modulos se deben encontrar en la misma carpeta.
Además todos los archivos .csv deben encontrarse en la misma carpeta puesto que son llamados con el path: "nombre.csv"

======================================================================================================

### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:
 
2. ```Currency Converter```: para la transformación de divisas, es ejecutada como "c.funcion"
3. ```Random```: Se utiliza la funcion "choice" para efectuar la probabilidad de un evento en el resultado True-False, se explica con más detalle como comentario en "parametros.py"

======================================================================================================

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

0. La libreria creada ```parametros.py```

1. ```main.py```: Implementa los menus y todas sus acciones menos simular nueva hora

2. ```canales.py```: Define a la clase Canales y tiene la función ```Simular nueva hora```

3. ```archivos.py```: Lee los archivos "barcos.csv", "tripulantes.csv" y "mercancia.csv" y también crea sus respectivas instancias.

4. ```barcos.py```: Define a la clase Barco y sus 3 subsclases

5. ```tripulantes.py```: Define a la clase Tripulante y sus 3 subclases, incluye a la clase ```Caja de Mercancias```

======================================================================================================

## Supuestos y consideraciones adicionales
Los supuestos que realicé durante la tarea son los siguientes:

1. No alcance a implementar los efectos especiales, pero varios de ellos si están programados

2. No alcance a implementar a mercancía, pero si se encuentra programada.

3. Los efectos especiales de los tripulantes están escritos, en la super() corresponde a un @abstractmethod pero no se ejecuta en el código

3. Caja de mercancía está escrita por completo pero la expiración no es utilizada por el código

4. Se añadieron parametros extra, es importante usar "parametros.py" implementado y también leer algunos comentarios en el código para entender el calculo de probabilidades con random.choice

======================================================================================================

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>
1. Por favor considerar las cosas no implementadas según el código que se encuentra escrito de ellas, lo único que falta por completo es el evento especial de la clase barco.

======================================================================================================

## Referencias de código externo

Para realizar mi tarea saqué código de:
1. La implementación de random.choice la busque entre varias paginas de internet hasta que funcionó
2. Para currencyconvert copie lo adjuntado en el link del enunciado

