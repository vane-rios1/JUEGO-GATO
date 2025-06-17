ELABORADO POR VANESSA RIOS PEREZ

Descripción del Diagrama UML del Juego del Gato (Tres en Línea)

El siguiente diagrama UML representa la estructura de clases del programa "Juego del Gato", también conocido como Tres en Línea o Tic-Tac-Toe. Este juego es un clásico entre dos jugadores, en el que se turnan para marcar espacios en una cuadrícula de 3x3 con los símbolos “X” y “O”, buscando formar una línea recta de tres símbolos iguales.

El sistema está compuesto por dos clases principales:

# Clase Jugador
- Esta clase representa a cada uno de los participantes del juego. Contiene dos atributos: nombre, que almacena el nombre del jugador, y simbolo, que puede ser “X” u “O”. Su único método, el constructor __init__, se encarga de inicializar estos atributos cuando se crea un nuevo jugador. Esta clase permite identificar a los jugadores y distinguir sus jugadas en el tablero.

# Clase JuegoGato
- Esta clase gestiona todo el funcionamiento del juego. Contiene la lógica necesaria para jugar una o varias partidas, incluyendo:

- El tablero del juego, representado como una lista de nueve elementos.

- La lista de jugadores, que incluye dos objetos de la clase Jugador.

- El atributo turno, que indica a qué jugador le corresponde jugar.

- Un historial que guarda los resultados de partidas anteriores.

- Un contador de empates, que registra cuántas veces terminó el juego sin un ganador.

Además, la clase JuegoGato contiene varios métodos que permiten ejecutar diferentes acciones, como mostrar el tablero, validar jugadas, registrar turnos, detectar un ganador o un empate, e iniciar nuevas partidas. También incluye una función para mostrar el historial completo de resultados.

# Relación entre las clases
La clase JuegoGato utiliza objetos de la clase Jugador, lo cual se representa en el diagrama UML mediante una relación de uso (flecha que apunta desde JuegoGato hacia Jugador). Esto refleja que el sistema principal del juego depende de la creación e interacción de los jugadores.

# Conclusión
Este diseño en clases permite que el juego esté bien organizado, sea fácil de mantener y escalar. Por ejemplo, en el futuro se podrían agregar nuevas funciones como niveles de dificultad, juego contra la computadora o interfaz gráfica, manteniendo esta estructura base. El uso del diagrama UML facilita la comprensión del código y la comunicación entre programadores y diseñadores.

