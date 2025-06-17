1. Eliminación de espacios innecesarios con .strip()
¿Qué mejora hice?
Limpié los nombres que ingresan los jugadores eliminando espacios en blanco al principio y al final.

¿Por qué es importante?
Porque mejora la presentación del nombre del jugador. Evita que aparezcan espacios raros cuando se muestra el turno o el ganador. Además, previene confusiones si un jugador sin querer escribe espacios antes o después de su nombre.

2. Asignación de nombres por defecto
¿Qué mejora hice?
Si un jugador no escribe su nombre y simplemente presiona "Enter", el programa le asigna un nombre genérico como “Jugador 1” o “Jugador 2”.

¿Por qué es útil?
Porque evita que el juego continúe con un nombre vacío, lo que podría hacer que los mensajes se vean mal o resulten confusos. También hace que el juego sea más fluido y fácil de usar, incluso si el jugador no quiere escribir su nombre.

3. Mensajes más claros y ordenados entre rondas
¿Qué mejora hice?
Agregué saltos de línea entre partidas y mensajes informativos cuando se inicia o reinicia el juego.

¿Por qué ayuda?
Porque mejora la experiencia visual del usuario. Hace que el juego sea más fácil de seguir en la consola y que las distintas fases del juego (inicio, victoria, empate, reinicio) estén claramente separadas. 

4. Validaciones más amigables para los movimientos
¿Qué ya estaba bien implementado y mantuve correctamente?
Si el jugador escribe un valor no numérico o fuera del rango permitido, el juego muestra un mensaje de error amigable y le permite intentarlo de nuevo.

¿Por qué esto es importante?
Porque hace que el juego no se bloquee por un error del usuario. Esto mejora la robustez del programa y permite que personas con menos experiencia puedan jugar sin frustrarse.

5. Estructura organizada del código
¿Qué se nota en mi código?
Separé bien las funciones según su propósito: una para mostrar el tablero, otra para verificar ganadores, otra para validar movimientos, etc.

¿Por qué esto es valioso?
Porque hace que el código sea más fácil de entender, mantener y modificar. 
En resumen, las mejoras aumentan la usabilidad, la claridad y la resistencia a errores del juego. Hice que se vea más profesional, fácil de jugar y más pulido para los usuarios. 



