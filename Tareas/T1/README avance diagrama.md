´´README PARA EL AVANCE DEL DIAGRAMA DE CLASES´´

0. Para el diagrama de clases no se tuvo en cuenta la simulación de menús, pero si las posibles interacciones entre Clases.
1. Se considera como clase principal a "Canales", manteniendo una relación de composición con "Barcos" y "Tripulante", puesto que no hay razón para que estas últimas existan sin la simulación principal de Canal.
2. A la clase "Barcos", aparte de lo pedido en pauta le añadí los parametros de:
    2. a) Ocurrió evento: este parametro se rellana cuando la clase "Tripulante" (en específico "Capitán") ejecuta su "Evento Especial".
    2. b) Encallado: un Booleano que indica si el barco está encallado o no.
    2. c) Aparte, se consideró para el flujo del programa que "Tripulación" y "Mercancía" contendrán sus datos en una lista cada uno.
3. En la clase "Barcos" se consideraron como abstractmethod a "Encallar" y "Ejecutar evento especial", que contendrá un código general que posteriormente variará en el llamado de cada subclase según el tipo de barco. (tal como Locales.py en la AS1).
4. En la clase "Barcos" la función "Efecto capitán" comprobará a los atributos "Ocurrió evento" y "Encallado" para llamar a "Desencallar" de la clase "Capitán".
5. "Caja de mercancía" tiene una relación de agregación con "Barcos"
6. No tengo claro si el efecto especial de "Cocinero" y "Carguero" también se realizan solo una vez al igual que "Capitán" o se hacen una vez por turno.
7. En la clase "Canales", el "Cobro de uso" es "None" porque el método "Establecer cobro" se encargará de cálcular el valor y asignarlo, con respecto a la dificultad de la simulación.
8. Ninguna función retona algo porque todas las asignaciones de atributo las realizan interna y directamente según los procedimientos que deba realizar por enunciado, por lo que no es necesario retornar algo.
9. Al no saber que poner en los atributos de las subclases, solo puse "Superclase.__init__()"
8. No supe poner solo una flecha para la herencia de "Tripulante" por eso quedaron 3 flechas mal superpuestas :(