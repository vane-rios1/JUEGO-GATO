class Jugador:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo

class JuegoGato:
    def __init__(self):
        self.tablero = [" " for _ in range(9)]
        self.jugadores = []
        self.turno = 0
        self.historial = []

    def mostrar_tablero(self):
        print()
        for i in range(3):
            fila = self.tablero[i*3:(i+1)*3]
            print(" | ".join(fila))
            if i < 2:
                print("--+---+--")
        print()

    def verificar_ganador(self, simbolo):
        combinaciones = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for combo in combinaciones:
            if all(self.tablero[i] == simbolo for i in combo):
                return True
        return False

    def tablero_lleno(self):
        return all(c != " " for c in self.tablero)

    def jugar_turno(self):
        jugador = self.jugadores[self.turno]
        while True:
            try:
                posicion = int(input(f"{jugador.nombre} ({jugador.simbolo}), elige una posición (1-9): ")) - 1
                if 0 <= posicion <= 8 and self.tablero[posicion] == " ":
                    self.tablero[posicion] = jugador.simbolo
                    break
                else:
                    print("Posición inválida o ya ocupada. Intenta otra vez.")
            except ValueError:
                print("Entrada inválida. Escribe un número del 1 al 9.")

    def jugar_partida(self):
        self.tablero = [" " for _ in range(9)]
        self.turno = 0
        print("\n¡Comienza el juego del gato!")
        self.mostrar_tablero()

        while True:
            self.jugar_turno()
            self.mostrar_tablero()

            jugador_actual = self.jugadores[self.turno]
            if self.verificar_ganador(jugador_actual.simbolo):
                print(f"¡{jugador_actual.nombre} ha ganado!")
                self.historial.append(jugador_actual.nombre)
                break
            elif self.tablero_lleno():
                print("¡Empate!")
                self.historial.append("Empate")
                break
            else:
                self.turno = 1 - self.turno  # Alternar entre 0 y 1

    def mostrar_historial(self):
        print("\n📜 Historial de Partidas:")
        for i, ganador in enumerate(self.historial, start=1):
            print(f"Partida {i}: {ganador}")

    def iniciar(self):
        print("🎮 Bienvenido al Juego del Gato (3 en línea)\n")
        nombre1 = input("Nombre del Jugador 1 (X): ")
        nombre2 = input("Nombre del Jugador 2 (O): ")
        self.jugadores = [Jugador(nombre1, "X"), Jugador(nombre2, "O")]

        while True:
            self.jugar_partida()
            self.mostrar_historial()
            continuar = input("\n¿Deseas jugar otra partida? (s/n): ").lower()
            if continuar != 's':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break

# Ejecutar el juego
if __name__ == "__main__":
    juego = JuegoGato()
    juego.iniciar()


    