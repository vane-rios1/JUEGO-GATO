Algoritmo JuegoDelGatoConHistorial
    // Declaración del tablero y variables
    Definir tablero Como Caracter
    Dimension tablero[3,3]
    
    Definir fila, col, turno, i, j Como Entero
    Definir simbolo, jugadorGanador, jugarOtro Como Caracter
    Definir victoriasX, victoriasO, empates Como Entero
	
    victoriasX <- 0
    victoriasO <- 0
    empates <- 0
	
    Repetir
        // Inicializar tablero vacío
        turno <- 1
        jugadorGanador <- "Ninguno"
        
        Llamar inicializarTablero(tablero)
        Repetir:
         Llamar mostrarTablero(tablero)
       
            // Determinar símbolo del jugador
            Si turno MOD 2 = 1 Entonces
                simbolo <- "X"
                Escribir "Turno del Jugador 1 (X)"
            Sino
                simbolo <- "O"
                Escribir "Turno del Jugador 2 (O)"
            FinSi
            
            Llamar leerJugada(fila,col,tablero)
	    tablero[fila,col] <- simbolo
            
            Llamar verificarGanador(tablero, simbolo, jugadorGanador)
			
            turno <- turno + 1
        Hasta Que ganador <> "Ninguno" O turno > 9
		
        // Mostrar resultado
        Escribir ""
        Escribir "RESULTADO:"
        Llamar mostrarTablero(tablero)
		
        Si ganador = "X" Entonces
            Escribir "¡Ganó el Jugador 1 (X)!"
            victoriasX <- victoriasX + 1
        Sino
            Si ganador = "O" Entonces
                Escribir "¡Ganó el Jugador 2 (O)!"
                victoriasO <- victoriasO + 1
            Sino
                Escribir "¡Empate!"
                empates <- empates + 1
            FinSi
        FinSi
		
        // Mostrar historial
        Escribir ""
        Escribir "HISTORIAL DE PARTIDAS:"
        Escribir "Jugador 1 (X): ", victoriasX, " victorias"
        Escribir "Jugador 2 (O): ", victoriasO, " victorias"
        Escribir "Empates: ", empates
		
        // Preguntar si desea jugar otra vez
        Escribir ""
        Escribir "¿Desean jugar otra partida? (S/N): "
        Leer jugarOtro
    Hasta Que jugarOtro = "N" O jugarOtro = "n"
	
    Escribir ""
    Escribir "¡Gracias por jugar!"

FinAlgoritmo
SubProceso inicializarTablero(tablero)
    Para i <- 1 Hasta 3
        Para j <- 1 Hasta 3
            tablero[i,j] <- "-"
        FinPara
    FinPara
FinSubProceso

SubProceso mostrarTablero(tablero)
    Escribir ""
    Escribir "TABLERO:"
    Para i <- 1 Hasta 3
        Para j <- 1 Hasta 3
            Escribir Sin Saltar tablero[i,j] + " "
        FinPara
        Escribir ""
    FinPara
FinSubProceso

SubProceso leerJugada(Referencias fila, col, tablero)
    Repetir
        Escribir "Ingrese fila (1 a 3): "
        Leer fila
        Escribir "Ingrese columna (1 a 3): "
        Leer col

        Si fila < 1 O fila > 3 O col < 1 O col > 3 Entonces
            Escribir "¡Posición fuera del tablero!"
        Sino
            Si tablero[fila,col] <> "-" Entonces
                Escribir "¡Casilla ocupada!"
            FinSi
        FinSi
    Hasta Que fila >= 1 Y fila <= 3 Y col >= 1 Y col <= 3 Y tablero[fila,col] = "-"
FinSubProceso

SubProceso verificarGanador(tablero, simbolo, Referencia jugadorGanador)
    Para i <- 1 Hasta 3
        Si tablero[i,1] = simbolo Y tablero[i,2] = simbolo Y tablero[i,3] = simbolo Entonces
            jugadorGanador <- simbolo
        FinSi
        Si tablero[1,i] = simbolo Y tablero[2,i] = simbolo Y tablero[3,i] = simbolo Entonces
            jugadorGanador <- simbolo
        FinSi
    FinPara

    Si tablero[1,1] = simbolo Y tablero[2,2] = simbolo Y tablero[3,3] = simbolo Entonces
        jugadorGanador <- simbolo
    FinSi
    Si tablero[1,3] = simbolo Y tablero[2,2] = simbolo Y tablero[3,1] = simbolo Entonces
        jugadorGanador <- simbolo
    FinSi
FinSubProceso


# Registro de Modificaciones

*Archivo modificado:* JuegoDelGatoConHistorial.psc

---

## Modificación 1: Modularización del código
*Qué se cambió:*  
Se creó un conjunto de subprocesos: inicializarTablero, mostrarTablero, leerJugada y verificarGanador.

*Justificación:*  
Permite reutilizar código, mejora la organización, facilita mantenimiento y la legibilidad.

---

## Modificación 2: Mejora en los nombres de variables
*Qué se cambió:*  
Renombrada la variable ganador a jugadorGanador, para mayor claridad semántica.

*Justificación:*  
Nombres más descriptivos ayudan a entender el propósito del código.

---

## Modificación 3: Validación de entrada encapsulada
*Qué se cambió:*  
La validación de fila y columna ingresada por el usuario se movió al subproceso leerJugada.

*Justificación:*  
Evita duplicación de lógica, centraliza la validación en un solo lugar y reduce errores.

---

## Modificación 4: Contador de empates
*Qué se cambió:*  
Se agregó la instrucción empates <- empates + 1 en la sección de resultado.

*Justificación:*  
Cumple con el requerimiento funcional de mostrar cuántas partidas terminaron en empate.

---

## Modificación 5: Limpieza de estilo
*Qué se cambió:*  
Indentación uniforme, separación de responsabilidades, comentarios claros y consistentes.

*Justificación:*  
Mejora la lectura del código, se apega a buenas prácticas de programación estructurada.

##Nombre del que realizo los cambios: Dalila Yusaví
