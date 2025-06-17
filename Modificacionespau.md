ELABORADO POR: PAULINA SANCHEZ RAMIREZ

Este es mi archivo modificado en el que explicare que se cambio y las justificaciones de las mejoras en el programa de POO sin excepciones. Voy a usar unas comparaciones con los cambios que hice
en el codigo original, que en su mayoria son mas comentarios, para que se noten los cambios que realice. 

 REGISTRO DE LOS CAMBIOS MAS IMPORTANTES:

 Archivo: juego_gato.py

### Cambio 1
- Se cambió la función `es_entero` por una validación `try/except` en `entrada_valida`.
- Justificación: `isdigit()` no detecta números negativos ni letras; `try/except` es más robusto.
- Autora: Paulina

### Cambio 2
- Se agregó contador de empates (`self.empates`) y se muestra al final del juego.
- Justificación: Añade funcionalidad útil para jugadores.
- Autoar: Paulina

### Cambio 3
- Se movió el código de ejecución a un `if __name__ == "__main__":`
- Justificación: Mejora la estructura y permite importar la clase sin ejecutar el juego.
- Autora: Paulina


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








