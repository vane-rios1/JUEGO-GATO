ELABORADO POR VANESSA RIOS PEREZ


En este archivo voy a dar la explicación de mis modificaciones en tkinter que en mi caso son 4.  Las voy a ir comparando con las modificaciones anteriores para ver la evolucion de programa.



# CAMBIOS CLAVE ENTRE EL CÓDIGO ORIGINAL Y EL MODIFICADO 1

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Elemento / Función              | Código Original                              | Código Modificado 1                                                                 |
| ------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Función `check_win`**         | Retorna `True` si hay un ganador.            | Retorna la **lista de posiciones ganadoras** (`condition`) en lugar de solo `True`. |
| **Colores de X y O**            | No tiene colores, solo texto plano.          | X aparece en **amarillo**, O en **azul**.                                           |
| **Colorear casillas ganadoras** | No se distingue visualmente.                 | Las casillas ganadoras se colorean de **verde** (`fg="green"`).                     |
| **Casilla ocupada**             | No hay advertencia si ya está ocupada.       | Muestra `messagebox.showwarning` si la casilla está ocupada.                        |
| **Fuente y estilo visual**      | Botones sin fuente personalizada (pequeños). | Usa fuente `"Arial", 20` para botones y mejora estética general.                    |
| **Texto de instrucciones**      | Más general, sin mención de colores.         | Explica que **X es amarillo**, **O es azul** y casillas ganadoras **verdes**.       |
| **Color al reiniciar**          | No reinicia el color (`fg`) de los botones.  | Reinicia el color de los botones a **negro** (`fg="black"`).                        |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# RESUMEN DE LAS MEJORAS APORTADAS
- Mayor claridad visual: colores para X, O y ganadores.
- Mejor experiencia de usuario: advertencias si una casilla ya está ocupada.
- Retroalimentación visual más intuitiva: destacar combinaciones ganadoras.
- Código más informativo y reutilizable: check_win ahora da posiciones, no solo True/False.
- Diseño mejorado: fuentes legibles y layout más claro.


_______________________________________________________________________________________________________________________________________________________________________________________________________________________



# COMPARACIÓN ENTRE PROGRAMA MODIFICADO 1 Y MODIFICADO 2

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Elemento / Función                   | **Modificación 1**                                                  | **Modificación 2**                                                                                       | **Propósito del Cambio**                                |
| ------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Inicio del juego**                 | El juego comienza de inmediato con `X`.                             | Se requiere **seleccionar el jugador inicial** (X u O) y presionar **“Iniciar juego”**.                  | Brinda control al usuario sobre quién inicia.           |
| **Validación al inicio**             | No hay verificación, se puede jugar desde el primer clic.           | Si no se ha iniciado el juego, muestra advertencia con `messagebox`.                                     | Mejora el flujo del juego y evita errores de inicio.    |
| **Colores por jugador**              | X en **amarillo**, O en **azul** (solo cambia el color del texto).  | X con **fondo amarillo**, O con **fondo azul claro**.                                                    | Mejora la distinción visual entre jugadores.            |
| **Colorear celdas ganadoras**        | Se pintan las letras ganadoras de **verde** (texto).                | Se pinta el **fondo** de las celdas ganadoras de **verde claro**.                                        | Mayor visibilidad de la jugada ganadora.                |
| **Fuente del texto en botones**      | `"Arial", 20` para los botones.                                     | Igual que en Modificado 1.                                                                               | Se mantiene consistencia visual.                        |
| **Instrucciones**                    | Explican colores y reglas básicas del juego.                        | Instrucciones **más completas**, incluyendo pasos para iniciar el juego y el **significado de colores**. | Facilita el entendimiento del funcionamiento del juego. |
| **Cambio de turno**                  | Se alterna automáticamente entre X y O.                             | Igual, pero después de verificar que el juego haya iniciado.                                             | Lógica de turnos controlada.                            |
| **Reinicio del juego**               | Limpia el texto y habilita botones, color del texto vuelve a negro. | Limpia texto, **restaura fondo a color original**, y reinicia controles de inicio.                       | Mejor limpieza del tablero y reinicio más completo.     |
| **Selector de jugador (OptionMenu)** | No incluido.                                                        | **Incluido** con opción de elegir quién inicia (X u O).                                                  | Mejora personalización del juego.                       |
| **Botón "Iniciar juego"**            | No existe, el juego inicia directo.                                 | **Sí existe**, obligatorio para empezar a jugar.                                                         | Controla el inicio del juego.                           |
| **Variable `game_started`**          | No existe.                                                          | Usada para validar si el juego ya comenzó.                                                               | Mejora control del flujo del juego.                     |
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# RESUMEN DE LAS DIFERENCIAS CLAVE
- Modificado 2 mejora el control del juego (no se puede jugar sin seleccionar y empezar).
- Cambia los colores del texto (Modificado 1) por colores de fondo (Modificado 2).
- Mejora las instrucciones y la interacción del usuario (flujo más guiado y visual).
- Introduce variables nuevas como game_started, selected_player, y elementos GUI adicionales (OptionMenu, start_button, selector_label).


_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



# COMPARACIÓN ENTRE PROGRAMA MODIFICADO 2 Y MODIFICADO 3

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Elemento / Función                   | **Modificación 2**                                                                                  | **Modificación 3**                                                                                      | **Propósito / Mejora**                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Sistema de instrucciones**         | Instrucciones mostradas en un `Label`, texto fijo sin posibilidad de desplazarse.                   | Instrucciones mostradas en un **widget `Text` con `Scrollbar`**, desplazables.                          | Mejora la **usabilidad y visibilidad** si las instrucciones son largas.                |
| **Diseño del área de instrucciones** | Solo texto en un `Label` sin marco ni barra de desplazamiento.                                      | Instrucciones dentro de un **Frame** con `Scrollbar`, usando `Text` con modo solo lectura (`DISABLED`). | Permite al usuario **leer todo cómodamente** sin ocupar demasiado espacio en pantalla. |
| **Scroll automático de texto**       | No disponible.                                                                                      | Implementado mediante `Scrollbar` vertical.                                                             | Aumenta la accesibilidad de contenido extenso.                                         |
| **Resto del código**                 | Todo lo demás (tablero, turnos, validaciones, colores, reinicio, marcador) **igual que en Mod. 3**. | Igual, sin cambios en la lógica principal del juego o interfaz de botones.                              | Se mantiene consistencia funcional.                                                    |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# RESUMEN DEL CAMBIO
- El Programa Modificado 3 es una mejora directa del Modificado 2, centrada en hacer las instrucciones más accesibles y legibles gracias al uso de un Text con Scrollbar. No se modificó la mecánica del juego ni la interacción, lo cual mantiene la estabilidad y jugabilidad, pero mejora la experiencia del usuario con mejor presentación del contenido explicativo.


_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



# COMPARACIÓN ENTRE PROGRAMA MODIFICADO 3 Y MODIFICADO 4

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Elemento / Función                  | **Modificación 3**                                    | **Modificación 4**                                                         | **Propósito / Mejora**                                                            |                                                                                                       
| ----------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Ingreso de nombres de jugadores** | No permite ingresar nombres personalizados.           |  Se agregan dos `Entry`: uno para el jugador X y otro para el jugador O.   | Personaliza la experiencia, mostrando el nombre junto con el símbolo del jugador. |                                                                                            
| **Turno mostrado con nombre**       | Solo muestra "Turno del jugador: X" o "O".            |  Muestra también el nombre: "Turno de: Jugador X - Ana".                   | Hace más claro y personalizado el turno de cada jugador.                          |                                                                                            
| **Mensaje de victoria**             | "¡El jugador X ha ganado!"                            |  "¡Jugador X: Ana ha ganado!"                                              | Mejora la claridad e identifica al jugador por su nombre.                         |                                                                                             
| **Marcador personalizado**          | "Victorias - X: 0                                     | O: 0                                                                       | Empates: 0"                                                                       | 
| **Instrucciones**                   | Usaba un widget `Text` con `Scrollbar`, modo lectura. |  Usa un `Listbox` con `Scrollbar`, también en modo visual de solo lectura. | Alternativa visual más limpia, cada línea es una entrada del `Listbox`.           |                                                                                             
| **Validación al iniciar juego**     | Solo valida si se eligió X u O.                       |  También valida que **ambos nombres estén escritos**.                      | Previene errores y asegura una mejor experiencia inicial.                         |                                                                                            
| **Diseño visual general**           | Compacto, pero sin personalización de jugadores.      |  Más completo y amigable al incluir nombres reales.                        | Aporta **más interacción** y sentido de participación a los jugadores.            |                            
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# El Programa Modificado 4 representa la versión más avanzada hasta ahora. Añade:
- Interacción personalizada con nombres reales.
- Validaciones más completas.
- Mejor experiencia de usuario tanto en la jugabilidad como en la presentación de turnos y marcador.
