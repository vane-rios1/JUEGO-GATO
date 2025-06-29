# JUEGO DEL GATO
En esta práctica colaborativa realizamos la creación de códigos de un juego llamado Gato (también conocido como Tres en Línea o Tic Tac Toe). Los programas que creamos fueron:

- Algoritmo en PSeInt ----- Vanessa Ríos Pérez
- Programacion Esctructurada en Python ------ Elías Coyotzi Sosa
- Programacion Orientada a Objetos ------- Melanie Sosa Degabriel
- Programacion en Tkinter -------- Dalila Yusaví Conde Flores
- Diagrama de clases ---------- Paulina Sánchez Ramírez
- Programacion Orientada a Objetos sin excepciones --------- Melanie Sosa Degabriel

# ALGORITMO EN PSEINT
Es un algoritmo del juego del Gato (también conocido como Tres en Línea o Tic Tac Toe) para dos jugadores, hecho en pseudocódigo con PSeInt. El programa permite jugar varias partidas y llevar un historial de victorias y empates.
Funcionamiento paso a paso:

1. Inicializa variables:
- Crea un tablero de 3x3 vacío con guiones -.
- Define contadores para las victorias del jugador 1 (X), del jugador 2 (O) y los empates.
- Usa una variable turno para saber qué jugador juega.

2. Ciclo principal de juego:
- El programa entra en un bucle para repetir el juego mientras los jugadores deseen seguir jugando.

3. Inicio de cada partida:
- El tablero se reinicia con guiones (-) en todas las posiciones.
- Se determina quién juega según si el turno es impar (Jugador 1 - X) o par (Jugador 2 - O).

4. Cada turno de juego:
- Se muestra el tablero.
- Se pide al jugador que indique una fila y columna para colocar su símbolo (X o O).
- Si la posición es válida y está libre, se coloca el símbolo.
- Se verifica si el jugador actual ganó (comprobando filas, columnas o diagonales).
- Si no hay ganador, se pasa el turno al siguiente jugador.

5. Fin de la partida:
- Si alguien gana, se muestra el mensaje correspondiente.
- Si se completan los 9 turnos sin ganador, se declara un empate.
- Se actualizan los contadores del historial (victoriasX, victoriasO, empates).

6. Mostrar historial:
- Al final de cada partida se muestra el número de victorias de cada jugador y los empates acumulados.

7. Repetir o salir:
- Se pregunta si desean jugar otra partida (S para sí, N para no).
- Si eligen no, el programa termina mostrando un mensaje de despedida.


# PROGRAMACION ESTRUCTURADO EN PYTHON

1.Inicio:
Se piden los nombres de los dos jugadores.

2. Bucle de juego:
Permite jugar varias partidas seguidas.

3. Inicio de partida:
Se crea un tablero vacío y comienza el Jugador 1.

4. Turnos:

Muestra el tablero.

Pide al jugador la fila y columna.

Valida si la casilla está libre.

Coloca el símbolo (X o O).

Verifica si alguien ganó o si hubo empate.

Si no, cambia de turno.

5. Fin de partida:
Anuncia el ganador o el empate.

6. Repetir o salir:
Pregunta si desean jugar otra partida. Si no, termina el juego.

# PROGRAMACION ORIENTADO A OBJETOS EN PYTHON

El código es un juego de Gato (Tres en línea) para dos jugadores en consola. Está dividido en clases:
	•	Jugador: guarda el nombre y símbolo (X u O).
	•	JuegoGato: maneja el tablero, turnos, historial, y la lógica del juego.

El jugador elige una posición (del 1 al 9), se actualiza el tablero, y se verifica si alguien ganó o si hay empate. Al final, se puede jugar otra partida y se muestra el historial de resultados.

Es un programa bien organizado, fácil de entender y jugar.

# PROGRAMACION TKINTER EN PYTHON

Este programa en Python crea un juego del gato usando la biblioteca  tkinter .  El código implementa la lógica del juego, incluyendo la comprobación de victorias, empates, y la actualización de la puntuación.  La interfaz gráfica de usuario (GUI) permite a dos jugadores interactuar con el tablero, haciendo clic en los botones para colocar sus marcas ('X' u 'O').  Después de cada turno, el programa verifica si hay un ganador o un empate, mostrando un mensaje correspondiente.  También incluye un botón para reiniciar el juego y una sección que muestra la puntuación actual.


# DIAGRAMA DE CLASES

Este diagrama muestra cómo está organizado el código de nuestro juego del gato. Hay dos clases principales:

1. Jugador: 
Representa a cada jugador. Guarda su nombre y el símbolo que va a usar ('X' o 'O'). Ademas, su constructor se encarga de inicializar esos datos cuando se crea el jugador.

2. JuegoGato:
Es la clase que maneja toda la lógica del juego. Tiene atributos como el tablero (una lista con 9 posiciones), los dos jugadores, el turno actual y un historial de jugadas.
Incluye métodos para mostrar el tablero, verificar si alguien ganó, revisar si el tablero está lleno, jugar un turno, mostrar el historial y arrancar el juego completo.
Además, se indica que JuegoGato usa a la clase Jugador, ya que necesita crear dos jugadores para que la partida funcione.

En resumen, este diagrama organiza de forma clara cómo se estructura un juego del gato usando programación orientada a objetos. La clase Jugador se encarga de representar a los participantes, mientras que JuegoGato gestiona toda la lógica del juego. 
Gracias a esta separación de responsabilidades, el código es más ordenado, fácil de entender y de mantener.

# POO sin excepciones
Se usan dos clases:
	•	Jugador: guarda el nombre y símbolo (X u O).
	•	JuegoGato: contiene el tablero, la lógica del juego y el turno.
	•	El juego valida las entradas del usuario sin usar try-except.
	•	El juego termina usando una variable juego_activo = False, sin usar exit().
	•	Se detecta si hay un ganador o si hay empate y se muestra el resultado.

