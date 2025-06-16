import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    """Comprueba si el jugador ha ganado."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    """Comprueba si hay un empate."""
    return all(cell != "" for cell in board)

def button_click(button_index):
    """Maneja los clics de los botones."""
    global current_player, board
    if board[button_index] == "":
        board[button_index] = current_player
        buttons[button_index].config(text=current_player)
        if check_win(board, current_player):
            messagebox.showinfo("¡Ganador!", f"¡El jugador {current_player} ha ganado!")
            update_score(current_player)
            disable_buttons()
        elif check_draw(board):
            messagebox.showinfo("Empate", "¡Es un empate!")
            update_score("Empate")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Turno del jugador: {current_player}")

def update_score(winner):
    """Actualiza el historial de resultados."""
    global score_x, score_o, draws
    if winner == "X":
        score_x += 1
    elif winner == "O":
        score_o += 1
    elif winner == "Empate":
        draws += 1
    score_label.config(text=f"Victorias - X: {score_x} | O: {score_o} | Empates: {draws}")

def disable_buttons():
    """Desactiva los botones después de que alguien gane o haya un empate."""
    for button in buttons:
        button.config(state=tk.DISABLED)

def reset_game():
    """Reinicia el tablero para una nueva partida."""
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", state=tk.NORMAL)
    label.config(text=f"Turno del jugador: {current_player}")

# Variables de puntaje
score_x = 0
score_o = 0
draws = 0

# Crea la ventana principal
window = tk.Tk()
window.title("Tres en Raya")

# Crea las variables del juego
board = [""] * 9
current_player = "X"

# Crea los botones del tablero
buttons = []
for i in range(9):
    button = tk.Button(window, text="", width=10, height=5,
                       command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Etiqueta del turno del jugador
label = tk.Label(window, text=f"Turno del jugador: {current_player}")
label.grid(row=3, column=0, columnspan=3)

# Etiqueta del historial
score_label = tk.Label(window, text="Victorias - X: 0 | O: 0 | Empates: 0")
score_label.grid(row=4, column=0, columnspan=3)

# Botón para reiniciar
reset_button = tk.Button(window, text="Reiniciar Juego", command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, pady=5)

# Instrucciones del juego
instructions = (
    "Instrucciones:\n"
    "1. Dos jugadores se turnan para colocar sus marcas (X u O) en un tablero de 3x3.\n"
    "2. El primer jugador en obtener tres marcas en fila, columna o diagonal gana.\n"
    "3. Si el tablero se llena sin que ningún jugador gane, es un empate."
)
instructions_label = tk.Label(window, text=instructions, justify="left")
instructions_label.grid(row=6, column=0, columnspan=3, pady=5)

window.mainloop()