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
        messagebox.showinfo("Advertencia", "Debes iniciar el juego primero.")
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

            ganador = player_x_name.get() if current_player == "X" else player_o_name.get()
            messagebox.showinfo("¡Ganador!", f"¡Jugador {current_player}: {ganador} ha ganado!")
            update_score(current_player)
            disable_buttons()
        elif check_draw(board):
            messagebox.showinfo("Empate", "¡Es un empate!")
            update_score("Empate")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
            siguiente = player_x_name.get() if current_player == "X" else player_o_name.get()
            label.config(text=f"Turno de: Jugador {current_player} - {siguiente}")
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
    score_label.config(text=f"Victorias - {player_x_name.get()} (X): {score_x} | {player_o_name.get()} (O): {score_o} | Empates: {draws}")

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
    name_x = player_x_name.get().strip()
    name_o = player_o_name.get().strip()
    current_player = selected_player.get()

    if not name_x or not name_o:
        messagebox.showwarning("Campos vacíos", "Debes ingresar los nombres de ambos jugadores.")
        return

    if current_player not in ["X", "O"]:
        messagebox.showwarning("Selección inválida", "Debes seleccionar quién comienza (X u O).")
        return

    game_started = True
    player_selector.config(state="disabled")
    start_button.config(state="disabled")
    turno = name_x if current_player == "X" else name_o
    label.config(text=f"Turno de: Jugador {current_player} - {turno}")

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

# Nombres de jugadores
tk.Label(window, text="Jugador X - Nombre:").grid(row=0, column=0)
player_x_name = tk.Entry(window)
player_x_name.grid(row=0, column=1)

tk.Label(window, text="Jugador O - Nombre:").grid(row=1, column=0)
player_o_name = tk.Entry(window)
player_o_name.grid(row=1, column=1)

# Selector de jugador inicial
tk.Label(window, text="¿Quién comienza?").grid(row=2, column=0)
selected_player = tk.StringVar()
selected_player.set("Selecciona")
player_selector = tk.OptionMenu(window, selected_player, "X", "O")
player_selector.grid(row=2, column=1)

start_button = tk.Button(window, text="Iniciar juego", command=start_game)
start_button.grid(row=2, column=2)

# Crear botones del tablero
for i in range(9):
    btn = tk.Button(window, text="", width=10, height=5, font=("Arial", 20),
                    command=lambda idx=i: button_click(idx))
    btn.grid(row=(i // 3) + 3, column=i % 3)
    buttons.append(btn)

# Etiqueta de turno
label = tk.Label(window, text="Selecciona quién empieza y presiona 'Iniciar juego'", font=("Arial", 12))
label.grid(row=6, column=0, columnspan=3)

# Etiqueta de marcador
score_label = tk.Label(window, text="Victorias - Jugador X: 0 | Jugador O: 0 | Empates: 0", font=("Arial", 12))
score_label.grid(row=7, column=0, columnspan=3)

# Botón para reiniciar
reset_button = tk.Button(window, text="Reiniciar Juego", command=reset_game)
reset_button.grid(row=8, column=0, columnspan=3, pady=5)

# Instrucciones con Listbox y Scrollbar
instructions_frame = tk.Frame(window)
instructions_frame.grid(row=9, column=0, columnspan=3, pady=5)

scrollbar = tk.Scrollbar(instructions_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

instructions_list = tk.Listbox(instructions_frame, width=50, height=10, yscrollcommand=scrollbar.set)

instrucciones = [
    "INSTRUCCIONES:",
    "1. Escribe los nombres de los jugadores X y O.",
    "2. Selecciona quién comienza (X u O).",
    "3. Presiona el botón 'Iniciar juego'.",
    "4. Cada jugador hará clic en una casilla vacía para colocar su símbolo.",
    "5. El primero en lograr tres en línea (horizontal, vertical o diagonal) gana.",
    "6. Si todas las casillas se llenan sin ganador, es empate.",
    "7. Presiona 'Reiniciar juego' para comenzar una nueva partida.",
    "",
    "SIGNIFICADO DE COLORES:",
    "- X aparece con fondo amarillo.",
    "- O aparece con fondo azul.",
    "- Las casillas ganadoras se pintan de verde.",
    "- Las demás se desactivan en gris tras finalizar la partida."
]

for item in instrucciones:
    instructions_list.insert(tk.END, item)

instructions_list.config(state=tk.DISABLED)
instructions_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=instructions_list.yview)

# Ejecutar la aplicación
window.mainloop()
