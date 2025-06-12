# JUEGO DEL GATO
En esta práctica colaborativa realizamos la creación de códigos de un juego llamado Gato (también conocido como Tres en Línea o Tic Tac Toe). Los programas que creamos fueron:

- Algoritmo en PSeInt ----- Vanessa Ríos Pérez
- Programacion Esctructurada en Python ------ Elías Coyotzi Sosa
- Programacion Orientada a Objetos ------- Melanie Sosa Degabriel
- Programacion en Tkinter -------- Dalila Yusaví Conde Flores
- Diagrama de clases ---------- Paulina Sánchez Ramírez

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


#PROGRAMACION ESTRUCTURADO EN PYTHON

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
