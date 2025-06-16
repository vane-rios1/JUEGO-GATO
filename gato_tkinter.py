import tkinter as tk
from tkinter import messagebox

# Función que revisa si hay una combinación ganadora y retorna los índices ganadores
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return condition  # Se retorna la lista de posiciones ganadoras
    return None

# Revisa si hay empate
def check_draw(board):
    return all(cell != "" for cell in board)

# Función principal que responde al clic del botón
def button_click(button_index):
    global current_player, board
    if board[button_index] == "":
        board[button_index] = current_player
        buttons[button_index].config(text=current_player,
                                     fg="yellow" if current_player == "X" else "blue")
        
        win_positions = check_win(board, current_player)
        if win_positions:
            for i in range(9):
                buttons[i].config(fg="gray")  # Desactiva colores anteriores
            for i in win_positions:
                buttons[i].config(fg="green")  # Colorea las celdas ganadoras
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
    else:
        messagebox.showwarning("Casilla ocupada", "Esa casilla ya está ocupada. Elige otra.")

# Actualiza los puntajes
def update_score(winner):
    global score_x, score_o, draws
    if winner == "X":
        score_x += 1
    elif winner == "O":
        score_o += 1
    elif winner == "Empate":
        draws += 1
    score_label.config(text=f"Victorias - X: {score_x} | O: {score_o} | Empates: {draws}")

# Desactiva los botones después del juego
def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Reinicia el juego
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="", state=tk.NORMAL, fg="black")
    label.config(text=f"Turno del jugador: {current_player}")

# Variables de puntaje
score_x = 0
score_o = 0
draws = 0

# Crear ventana
window = tk.Tk()
window.title("Tres en Raya")

# Crear estado del juego
board = [""] * 9
current_player = "X"

# Crear botones del tablero
buttons = []
for i in range(9):
    button = tk.Button(window, text="", width=10, height=5,
                       font=("Arial", 20),
                       command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Etiqueta de turno
label = tk.Label(window, text=f"Turno del jugador: {current_player}",
                 font=("Arial", 12, "bold"))
label.grid(row=3, column=0, columnspan=3)

# Etiqueta de historial
score_label = tk.Label(window, text="Victorias - X: 0 | O: 0 | Empates: 0",
                       font=("Arial", 12))
score_label.grid(row=4, column=0, columnspan=3)

# Botón para reiniciar
reset_button = tk.Button(window, text="Reiniciar Juego", command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, pady=5)

# Instrucciones del juego
instructions = (
    "Instrucciones:\n"
    "1. Dos jugadores se turnan para colocar sus marcas (X en amarillo, O en azul).\n"
    "2. El primero que forme una línea de 3 gana (se marcará en verde).\n"
    "3. Si el tablero se llena sin ganador, es un empate."
)
instructions_label = tk.Label(window, text=instructions, justify="left")
instructions_label.grid(row=6, column=0, columnspan=3, pady=5)

window.mainloop()
