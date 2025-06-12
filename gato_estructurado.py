# Juego del Gato (Tic Tac Toe) - Programación estructurada con reinicio y nombres de jugadores

def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print("  0 1 2")
    for i, fila in enumerate(tablero):
        print(f"{i} {'|'.join(fila)}")
        if i < 2:
            print("  -----")

def es_movimiento_valido(tablero, fila, columna):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " "

def realizar_movimiento(tablero, fila, columna, jugador):
    tablero[fila][columna] = jugador

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    return all(tablero[i][j] != " " for i in range(3) for j in range(3))

def cambiar_turno(jugador_actual, jugadores):
    return jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]

def obtener_simbolo(jugador, jugadores, simbolos):
    return simbolos[0] if jugador == jugadores[0] else simbolos[1]

def jugar_una_partida(jugadores, simbolos):
    tablero = inicializar_tablero()
    jugador_actual = jugadores[0]
    
    while True:
        mostrar_tablero(tablero)
        simbolo_actual = obtener_simbolo(jugador_actual, jugadores, simbolos)
        print(f"Turno de {jugador_actual} ({simbolo_actual})")

        try:
            fila = int(input("Ingrese la fila (0-2): "))
            columna = int(input("Ingrese la columna (0-2): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if not es_movimiento_valido(tablero, fila, columna):
            print("Movimiento inválido, intenta de nuevo.")
            continue

        realizar_movimiento(tablero, fila, columna, simbolo_actual)

        if verificar_ganador(tablero, simbolo_actual):
            mostrar_tablero(tablero)
            print(f"¡Felicidades! {jugador_actual} ha ganado.")
            break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = cambiar_turno(jugador_actual, jugadores)

def juego_del_gato():
    print("Bienvenidos al juego del Gato (Tic Tac Toe)!")
    nombre_jugador1 = input("Ingrese el nombre del Jugador 1 (usará 'X'): ")
    nombre_jugador2 = input("Ingrese el nombre del Jugador 2 (usará 'O'): ")

    jugadores = [nombre_jugador1, nombre_jugador2]
    simbolos = ["X", "O"]

    while True:
        jugar_una_partida(jugadores, simbolos)
        respuesta = input("¿Desean jugar otra partida? (s/n): ").strip().lower()
        if respuesta != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

# Ejecutar el juego
if __name__ == "__main__":
    juego_del_gato()