import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return condition
    return None

def check_draw(board):
    return all(cell != "" for cell in board)

def button_click(index):
    global current_player
    if not game_started:
        messagebox.showinfo("Advertencia", "Selecciona el jugador inicial y presiona 'Iniciar juego'")
        return

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if current_player == "X":
            buttons[index].config(bg="yellow")
        else:
            buttons[index].config(bg="light blue")

        win_positions = check_win(board, current_player)
        if win_positions:
            for i in range(9):
                buttons[i].config(bg="light gray")
            for i in win_positions:
                buttons[i].config(bg="light green")
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
        messagebox.showwarning("Casilla ocupada", "Esa casilla ya está ocupada.")

def update_score(winner):
    global score_x, score_o, draws
    if winner == "X":
        score_x += 1
    elif winner == "O":
        score_o += 1
    else:
        draws += 1
    score_label.config(text=f"Victorias - X: {score_x} | O: {score_o} | Empates: {draws}")

def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

def reset_game():
    global board, current_player, game_started
    board = [""] * 9
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")
    label.config(text="Selecciona quién empieza y presiona 'Iniciar juego'")
    player_selector.config(state="normal")
    start_button.config(state="normal")
    game_started = False

def start_game():
    global current_player, game_started
    current_player = selected_player.get()
    if current_player not in ["X", "O"]:
        messagebox.showwarning("Selección inválida", "Debes seleccionar X u O.")
        return
    label.config(text=f"Turno del jugador: {current_player}")
    player_selector.config(state="disabled")
    start_button.config(state="disabled")
    game_started = True

# Inicializar ventana y variables
window = tk.Tk()
window.title("Tres en Raya")

score_x = 0
score_o = 0
draws = 0
board = [""] * 9
buttons = []
current_player = ""
game_started = False

# Selector de jugador inicial
selected_player = tk.StringVar()
selected_player.set("Selecciona")

selector_label = tk.Label(window, text="¿Quién comienza primero?")
selector_label.grid(row=0, column=0, columnspan=1)
player_selector = tk.OptionMenu(window, selected_player, "X", "O")
player_selector.grid(row=0, column=1)

start_button = tk.Button(window, text="Iniciar juego", command=start_game)
start_button.grid(row=0, column=2)

# Crear botones del tablero
for i in range(9):
    btn = tk.Button(window, text="", width=10, height=5, font=("Arial", 20),
                    command=lambda idx=i: button_click(idx))
    btn.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(btn)

# Etiqueta de turno
label = tk.Label(window, text="Selecciona quién empieza y presiona 'Iniciar juego'", font=("Arial", 12))
label.grid(row=4, column=0, columnspan=3)

# Etiqueta del historial
score_label = tk.Label(window, text="Victorias - X: 0 | O: 0 | Empates: 0", font=("Arial", 12))
score_label.grid(row=5, column=0, columnspan=3)

# Botón de reinicio
reset_button = tk.Button(window, text="Reiniciar Juego", command=reset_game)
reset_button.grid(row=6, column=0, columnspan=3, pady=5)

# Instrucciones
instructions = (
    "Instrucciones:\n"
    "1. Elige un jugador (X u O) para que empieze a jugar primero. \n"
    "2. Dale click en boton Inicar juego. \n"
    "3. Dos jugadores se turnan para colocar sus marcas (X u O) en un tablero de 3x3.\n"
    "4. El primer jugador en obtener tres marcas en fila, columna o diagonal gana.\n"
    "5. Si el tablero se llena sin que ningún jugador gane, es un empate\n"
    "6. Presiona 'Reiniciar Juego' para volver a jugar\n"
    
    
    "Significado de los colores:\n"
    "- X aparece con fondo amarillo\n"
    "- O aparece con fondo azul\n"
    "- Al ganar, las celdas ganadoras se pintan de verde\n"
    
)
instructions_label = tk.Label(window, text=instructions, justify="left")
instructions_label.grid(row=7, column=0, columnspan=3, pady=5)

window.mainloop()
