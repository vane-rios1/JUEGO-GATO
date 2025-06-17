ELABORADO POR: PAULINA SANCHEZ RAMIREZ

Este es mi archivo modificado en el que explicare que se cambio y las justificaciones de las mejoras en el programa de POO sin excepciones. Voy a usar unas comparaciones con los cambios que hice
en el codigo original, que en su mayoria son mas comentarios, para que se noten los cambios que realice. 

 REGISTRO DE LOS CAMBIOS MAS IMPORTANTES:

 Cambio 1: Mejora en la validación de entrada
 
- Qué se cambió: Reemplaze el uso de `isdigit()` por un bloque `try/except` dentro de la función `entrada_valida()`.
- Justificación: El método `isdigit()` no maneja letras, espacios ni caracteres especiales, lo que podía generar errores o fallos silenciosos. El uso de `try/except` mejora la robustez de la validación.
- Autor: Paulina

Cambio 2: Función `reiniciar_tablero()`

- Qué se cambió: Agregue un nuevo método llamado `reiniciar_tablero()` en la clase `JuegoGato`.
- Justificación: Facilita reutilizar la lógica de reinicio entre rondas, mejora la legibilidad y evita duplicación de código.
- Autor: Paulina

Cambio 3: Agregar contador de empates

- Qué se cambió: Añadi un atributo `self.empates` en `__init__`, y se incrementa cada vez que hay empate.
- Justificación: Mejora funcional que permite hacer seguimiento de empates acumulados, lo que puede ser útil para estadísticas o experiencia del usuario.
- Autora: Paulina

 Cambio 4: Reestructuración de método `jugar()`
 
- Qué se cambió: El método `jugar()` lo modifique para permitir reiniciar el juego automáticamente al finalizar una partida, preguntando al usuario si quiere jugar otra vez.
- Justificación: Mejora la experiencia del usuario y permite jugar múltiples rondas sin reiniciar manualmente el script.
- Autor: Paulina

Cambio 5: Bloque `if __name__ == "__main__"`

- Qué se cambió: Encapsule la ejecución del juego dentro de `if __name__ == "__main__":`.
- Justificación: Mejora técnica que permite que el archivo sea importable como módulo sin que se ejecute automáticamente.
- Autor: Paulina


RECOMENDACIONES Y MEJORAS (LOS PRIMEROS COMENTARIOS QUE HICE)

1. Validación más robusta de la entrada: 
def entrada_valida(self, entrada):
    try:
        posicion = int(entrada) - 1
        return 0 <= posicion < 9 and self.tablero[posicion] == " "
    except ValueError:
        return False
   
2. Separar lógica de entrada del juego:
Extraer la entrada del jugador a una función obtener_entrada()
Facilita la migración a interfaz gráfica.

3. Usar constantes para combinaciones ganadoras:
Para evitar definirlas en cada llamada.
COMBINACIONES_GANADORAS = [...]

4. Estilo: PEP8
El nombre JuegoGato podría llamarse JuegoDelGato o TresEnRaya si se quiere más claridad.
Dejar líneas en blanco entre métodos (visualmente ya está bien).

5. Agrega docstrings y comentarios más explícitos:
def verificar_ganador(self, simbolo):
    """Verifica si el jugador con el símbolo dado ha ganado el juego."""
   
6. Posibilidad de reiniciar el juego:
Luego de terminar, se podria preguntar si quieren jugar otra partida.


REMPLAZO DE FUNCIONES Y JUSTIFICACION

1. Cambio de la función entrada_valida para usar try/except (más robusto)
 Reemplaze esta función:
def entrada_valida(self, entrada):
    if not self.es_entero(entrada):
        return False
    posicion = int(entrada) - 1
    return 0 <= posicion < 9 and self.tablero[posicion] == " "
   
Por esta:

def entrada_valida(self, entrada):
    try:
        posicion = int(entrada) - 1
        return 0 <= posicion < 9 and self.tablero[posicion] == " "
    except ValueError:
        return False

Justificación: 
isdigit() no detecta letras, negativos o espacios. try/except lo maneja todo mejor.

2. Creacion de una nueva función reiniciar_tablero() (reutilizable)
Agregue esta función dentro de la clase JuegoGato:

def reiniciar_tablero(self):
    """Reinicia el tablero y el turno inicial."""
    self.tablero = [" " for _ in range(9)]
    self.turno = 0

Justificación:
Función útil para reiniciar la partida sin duplicar código.

3. Mejora de las estructura: agregue if __name__ == "__main__"
Reemplaze esto que estába fuera de la clase:
juego = JuegoGato()
juego.jugar()

Por esto: 
if __name__ == "__main__":
    juego = JuegoGato()
    juego.jugar()

 Justificación:
 Permite que el archivo sea importable sin ejecutar automáticamente el juego.

CONTADOR DE EMPATES Y REINICIO DEL JUEGO

1. Agregue el contador de empates en el constructor:
 Modifique el método __init__ de la clase JuegoGato así:
def __init__(self):
    self.tablero = [" " for _ in range(9)]
    self.jugadores = []
    self.turno = 0
    self.empates = 0                       # Contador de empates

2. Mejora el método jugar() para soportar múltiples rondas
   Reemplaze TODO el método jugar() con esta versión mejorada:
def jugar(self):
    print("¡Bienvenido al Juego del Gato!")
    nombre1 = input("Nombre del Jugador 1 (X): ")
    nombre2 = input("Nombre del Jugador 2 (O): ")
    self.jugadores = [Jugador(nombre1, "X"), Jugador(nombre2, "O")]

    while True:                   #Permite múltiples juegos sin reiniciar el programa
        self.reiniciar_tablero()
        juego_activo = True
        while juego_activo:
            self.mostrar_tablero()
            jugador_actual = self.jugadores[self.turno % 2]
            print(f"\nTurno de {jugador_actual.nombre} ({jugador_actual.simbolo})")
            entrada = input("Elige una posición (1-9): ")
            if self.entrada_valida(entrada):
                posicion = int(entrada) - 1
                self.tablero[posicion] = jugador_actual.simbolo
                if self.verificar_ganador(jugador_actual.simbolo):
                    self.mostrar_tablero()
                    print(f"\n¡{jugador_actual.nombre} ha ganado!")
                    juego_activo = False
                elif " " not in self.tablero:
                    self.mostrar_tablero()
                    print("\n¡Empate!")
                    self.empates += 1                    # Sumar empate
                    juego_activo = False
                else:
                    self.turno += 1
            else:
                print("Entrada inválida. Elige un número entre 1 y 9 sin repetir.")
        print(f"\n Empates acumulados: {self.empates}")
        jugar_otra = input("¿Jugar otra vez? (s/n): ").lower()
        if jugar_otra != 's':
            print("¡Gracias por jugar!")
            break
   
Con esto ya cumple el requisito de "mejora funcional o técnica" y el juego se vuelve más robusto y completo, y ya no tiene errores
