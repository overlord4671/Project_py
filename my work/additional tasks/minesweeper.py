import tkinter as tk
import random
import time

buttons = []
game_numbers = []
size = 20
mine_count = None
mines = []
first_click = True
game_started = False
mines_marked = 0
start_time = None
timer_id = None


def set_difficulty():
    global mine_count, root
    root = tk.Tk()
    root.title("Выберите сложность")
    root.geometry("300x200")
    root.resizable(False, False)

    def set_mines(difficulty):
        global mine_count
        if difficulty == "easy":
            mine_count = random.randint(20, 30)
        elif difficulty == "medium":
            mine_count = random.randint(35, 45)
        else:
            mine_count = random.randint(50, 60)
        root.destroy()
        create_main_window()

    title_label = tk.Label(root, text="Выберите уровень сложности", font=("Arial", 14))
    title_label.pack(pady=20)

    easy_btn = tk.Button(root, text="Легкий", command=lambda: set_mines("easy"), width=15)
    medium_btn = tk.Button(root, text="Средний", command=lambda: set_mines("medium"), width=15)
    hard_btn = tk.Button(root, text="Сложный", command=lambda: set_mines("hard"), width=15)

    easy_btn.pack(pady=5)
    medium_btn.pack(pady=5)
    hard_btn.pack(pady=5)

    root.mainloop()


def place_mines(size=20, exclude_x=None, exclude_y=None):
    field = [[0 for _ in range(size)] for _ in range(size)]
    mines_placed = 0
    excluded_cells = set()

    if exclude_x is not None and exclude_y is not None:
        for i in range(max(0, exclude_x - 1), min(size, exclude_x + 2)):
            for j in range(max(0, exclude_y - 1), min(size, exclude_y + 2)):
                excluded_cells.add((i, j))

    while mines_placed < mine_count:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if field[x][y] == 0 and (x, y) not in excluded_cells:
            field[x][y] = 1
            mines_placed += 1
    return field


def update_mines_counter():
    remaining_mines = mine_count - mines_marked
    mines_counter_label.config(text=f"Мины: {remaining_mines}")


def update_timer():
    global timer_id
    if game_started and start_time is not None:
        elapsed_time = int(time.time() - start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"Время: {minutes:02d}:{seconds:02d}")
        timer_id = root.after(1000, update_timer)


def start_game():
    global game_started, start_time
    if not game_started:
        game_started = True
        start_time = time.time()
        update_timer()


def stop_timer():
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None


def get_number_color(number):
    colors = {1: "#0000FF", 2: "#008000", 3: "#FF0000", 4: "#000080",
              5: "#800000", 6: "#008080", 7: "#000000", 8: "#808080"}
    return colors.get(number, "black")


def calculate_numbers(mines):
    size = len(mines)
    numbers = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if mines[i][j] == 1:
                numbers[i][j] = -1
                continue
            for x in range(max(0, i - 1), min(size, i + 2)):
                for y in range(max(0, j - 1), min(size, j + 2)):
                    if mines[x][y] == 1:
                        numbers[i][j] += 1
    return numbers


def end_game():
    global game_started
    game_started = False
    stop_timer()

    for i in range(size):
        for j in range(size):
            buttons[i][j].destroy()

    mines_counter_label.destroy()
    timer_label.destroy()

    center_frame = tk.Frame(root, bg="white")
    center_frame.place(relx=0.5, rely=0.5, anchor="center")
    root.configure(bg="white")

    game_over_label = tk.Label(center_frame, text="Игра окончена!",
                               font=("Arial", 24, "bold"), fg="red", bg="white")
    game_over_label.pack(pady=20)

    restart_button = tk.Button(center_frame, text="Начать заново",
                               command=restart_game, font=("Arial", 16),
                               bg="lightblue", padx=20, pady=10)
    restart_button.pack(pady=10)


def on_cell_click(x, y):
    global first_click, game_numbers, mines

    if not game_started:
        start_game()

    if first_click:
        mines = place_mines(size=size, exclude_x=x, exclude_y=y)
        game_numbers = calculate_numbers(mines)
        first_click = False

    if game_numbers[x][y] == -1:
        buttons[x][y].config(text="*", bg="red")
        end_game()
    else:
        reveal_cell(x, y)


def reveal_cell(x, y):
    if buttons[x][y]["state"] == "disabled":
        return

    number = game_numbers[x][y]
    buttons[x][y].config(text=str(number) if number > 0 else "",
                         state="disabled", relief="sunken",
                         bg="lightgrey", fg=get_number_color(number) if number > 0 else "black",
                         font=("Arial", 12))

    if number == 0:
        for i in range(max(0, x - 1), min(size, x + 2)):
            for j in range(max(0, y - 1), min(size, y + 2)):
                reveal_cell(i, j)


def on_right_click(x, y):
    global mines_marked
    current_text = buttons[x][y]["text"]
    if current_text == "⚑":
        buttons[x][y].config(text="", bg="SystemButtonFace")
        mines_marked -= 1
    elif buttons[x][y]["state"] != "disabled":
        buttons[x][y].config(text="⚑", fg="red", bg="lightyellow")
        mines_marked += 1
    update_mines_counter()


def restart_game():
    global buttons, game_numbers, mines, first_click, game_started, mines_marked, start_time
    root.destroy()
    main()


def create_info_panel():
    global mines_counter_label, timer_label

    info_frame = tk.Frame(root)
    info_frame.grid(row=0, column=0, columnspan=size, sticky="ew", pady=5)

    mines_counter_label = tk.Label(info_frame, text=f"Мины: {mine_count}",
                                   font=("Arial", 12))
    mines_counter_label.pack(side=tk.LEFT, padx=10)

    timer_label = tk.Label(info_frame, text="Время: 00:00",
                           font=("Arial", 12))
    timer_label.pack(side=tk.RIGHT, padx=10)


def create_field(root, size):
    buttons = []
    game_frame = tk.Frame(root)
    game_frame.grid(row=1, column=0, columnspan=size)

    for i in range(size):
        row = []
        for j in range(size):
            btn = tk.Button(game_frame, width=3, height=1,
                            font=("Arial", 12), text="",
                            command=lambda x=i, y=j: on_cell_click(x, y))
            btn.grid(row=i, column=j, sticky="nsew")
            btn.bind("<Button-3>", lambda event, x=i, y=j: on_right_click(x, y))
            row.append(btn)
        buttons.append(row)
    return buttons


def create_main_window():
    global root, buttons, game_numbers
    root = tk.Tk()
    root.title("Сапер")
    root.resizable(False, False)

    create_info_panel()
    buttons = create_field(root, size)
    root.mainloop()


def main():
    global first_click, game_started, mines_marked, start_time
    first_click = True
    game_started = False
    mines_marked = 0
    start_time = None
    set_difficulty()


if __name__ == "__main__":
    main()
