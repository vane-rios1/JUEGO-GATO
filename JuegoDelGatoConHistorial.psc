Algoritmo JuegoDelGatoConHistorial
    // Declaración del tablero y variables
    Definir tablero Como Caracter
    Dimension tablero[3,3]
    
    Definir fila, col, turno, i, j Como Entero
    Definir simbolo, ganador, jugarOtro Como Caracter
    Definir victoriasX, victoriasO, empates Como Entero
	
    victoriasX <- 0
    victoriasO <- 0
    empates <- 0
	
    Repetir
        // Inicializar tablero vacío
        turno <- 1
        ganador <- "Ninguno"
        Para i <- 1 Hasta 3
            Para j <- 1 Hasta 3
                tablero[i,j] <- "-"
            FinPara
        FinPara
		
        Repetir
            // Mostrar tablero
            Escribir ""
            Escribir "TABLERO:"
            Para i <- 1 Hasta 3
                Para j <- 1 Hasta 3
                    Escribir Sin Saltar tablero[i,j] + " "
                FinPara
                Escribir ""
            FinPara
			
            // Determinar símbolo del jugador
            Si turno MOD 2 = 1 Entonces
                simbolo <- "X"
                Escribir "Turno del Jugador 1 (X)"
            Sino
                simbolo <- "O"
                Escribir "Turno del Jugador 2 (O)"
            FinSi
			
            // Pedir fila y columna válidas
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
			
            // Colocar el símbolo
            tablero[fila,col] <- simbolo
			
            // Verificar si hay ganador
            Para i <- 1 Hasta 3
                Si tablero[i,1] = simbolo Y tablero[i,2] = simbolo Y tablero[i,3] = simbolo Entonces
                    ganador <- simbolo
                FinSi
                Si tablero[1,i] = simbolo Y tablero[2,i] = simbolo Y tablero[3,i] = simbolo Entonces
                    ganador <- simbolo
                FinSi
            FinPara
			
            Si tablero[1,1] = simbolo Y tablero[2,2] = simbolo Y tablero[3,3] = simbolo Entonces
                ganador <- simbolo
            FinSi
            Si tablero[1,3] = simbolo Y tablero[2,2] = simbolo Y tablero[3,1] = simbolo Entonces
                ganador <- simbolo
            FinSi
			
            turno <- turno + 1
        Hasta Que ganador <> "Ninguno" O turno > 9
		
        // Mostrar resultado
        Escribir ""
        Escribir "RESULTADO:"
        Para i <- 1 Hasta 3
            Para j <- 1 Hasta 3
                Escribir Sin Saltar tablero[i,j] + " "
            FinPara
            Escribir ""
        FinPara
		
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
