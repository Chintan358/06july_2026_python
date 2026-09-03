import tkinter as tk
import random

# =========================
# GAME SETTINGS
# =========================

WIDTH = 600
HEIGHT = 500
CELL_SIZE = 20
SPEED = 100

BG_COLOR = "#111827"
SNAKE_COLOR = "#22c55e"
HEAD_COLOR = "#16a34a"
FOOD_COLOR = "#ef4444"
TEXT_COLOR = "white"

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Snake Game")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# =========================
# VARIABLES
# =========================

snake = []
food = None

direction = "Right"
next_direction = "Right"

score = 0
high_score = 0

game_running = False
game_paused = False

# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="🐍 SNAKE GAME",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

title_label.pack(pady=10)

# =========================
# SCORE
# =========================

score_frame = tk.Frame(root, bg=BG_COLOR)
score_frame.pack()

score_label = tk.Label(
    score_frame,
    text="Score: 0",
    font=("Arial", 14, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

score_label.pack(side="left", padx=50)

high_score_label = tk.Label(
    score_frame,
    text="High Score: 0",
    font=("Arial", 14, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

high_score_label.pack(side="left", padx=50)

# =========================
# CANVAS
# =========================

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#1f2937",
    highlightthickness=2,
    highlightbackground="#374151"
)

canvas.pack(pady=10)

# =========================
# CREATE SNAKE
# =========================

def create_snake():

    global snake

    snake = [
        (300, 240),
        (280, 240),
        (260, 240)
    ]

# =========================
# CREATE FOOD
# =========================

def create_food():

    global food

    while True:

        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)

        if (x, y) not in snake:
            food = (x, y)
            break

# =========================
# DRAW GAME
# =========================

def draw_game():

    canvas.delete("all")

    for index, (x, y) in enumerate(snake):

        if index == 0:

            canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill=HEAD_COLOR,
                outline="#86efac"
            )

            canvas.create_oval(
                x + 4,
                y + 4,
                x + 8,
                y + 8,
                fill="white"
            )

            canvas.create_oval(
                x + 12,
                y + 4,
                x + 16,
                y + 8,
                fill="white"
            )

        else:

            canvas.create_rectangle(
                x,
                y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill=SNAKE_COLOR,
                outline="#14532d"
            )

    if food:

        x, y = food

        canvas.create_oval(
            x + 2,
            y + 2,
            x + CELL_SIZE - 2,
            y + CELL_SIZE - 2,
            fill=FOOD_COLOR,
            outline="#fecaca"
        )

# =========================
# MOVE SNAKE
# =========================

def move_snake():

    global direction
    global food
    global score

    if not game_running or game_paused:
        return

    direction = next_direction

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= CELL_SIZE

    elif direction == "Down":
        head_y += CELL_SIZE

    elif direction == "Left":
        head_x -= CELL_SIZE

    elif direction == "Right":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)

    # Wall collision

    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        game_over()
        return

    # Self collision

    if new_head in snake:
        game_over()
        return

    snake.insert(0, new_head)

    # Food collision

    if new_head == food:

        score += 10

        score_label.config(
            text=f"Score: {score}"
        )

        update_high_score()

        create_food()

    else:

        snake.pop()

    draw_game()

    root.after(SPEED, move_snake)

# =========================
# CHANGE DIRECTION
# =========================

def change_direction(new_direction):

    global next_direction

    opposite = {
        "Up": "Down",
        "Down": "Up",
        "Left": "Right",
        "Right": "Left"
    }

    if new_direction != opposite[direction]:
        next_direction = new_direction

# =========================
# KEYBOARD
# =========================

def key_pressed(event):

    key = event.keysym

    if key == "Up":
        change_direction("Up")

    elif key == "Down":
        change_direction("Down")

    elif key == "Left":
        change_direction("Left")

    elif key == "Right":
        change_direction("Right")

    elif key.lower() == "p":
        pause_game()

    elif key.lower() == "r":
        start_game()

# =========================
# START GAME
# =========================

def start_game():

    global score
    global direction
    global next_direction
    global game_running
    global game_paused

    score = 0

    direction = "Right"
    next_direction = "Right"

    game_running = True
    game_paused = False

    score_label.config(text="Score: 0")

    create_snake()
    create_food()
    draw_game()

    move_snake()

# =========================
# PAUSE GAME
# =========================

def pause_game():

    global game_paused

    if not game_running:
        return

    game_paused = not game_paused

    if game_paused:

        canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text="PAUSED",
            font=("Arial", 35, "bold"),
            fill="white",
            tags="pause"
        )

    else:

        canvas.delete("pause")
        move_snake()

# =========================
# HIGH SCORE
# =========================

def update_high_score():

    global high_score

    if score > high_score:

        high_score = score

        high_score_label.config(
            text=f"High Score: {high_score}"
        )

# =========================
# GAME OVER
# =========================

def game_over():

    global game_running

    game_running = False

    canvas.create_rectangle(
        150,
        180,
        450,
        320,
        fill="#111827",
        outline="#ef4444",
        width=3
    )

    canvas.create_text(
        WIDTH // 2,
        220,
        text="GAME OVER",
        font=("Arial", 30, "bold"),
        fill="#ef4444"
    )

    canvas.create_text(
        WIDTH // 2,
        260,
        text=f"Score: {score}",
        font=("Arial", 18, "bold"),
        fill="white"
    )

    canvas.create_text(
        WIDTH // 2,
        290,
        text="Press R or Restart",
        font=("Arial", 13),
        fill="white"
    )

# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="▶ Start",
    font=("Arial", 11, "bold"),
    bg="#16a34a",
    fg="white",
    width=12,
    command=start_game
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="⏸ Pause",
    font=("Arial", 11, "bold"),
    bg="#f59e0b",
    fg="white",
    width=12,
    command=pause_game
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="🔄 Restart",
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    width=12,
    command=start_game
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="❌ Exit",
    font=("Arial", 11, "bold"),
    bg="#dc2626",
    fg="white",
    width=12,
    command=root.destroy
).pack(side="left", padx=5)

# =========================
# INSTRUCTIONS
# =========================

tk.Label(
    root,
    text="Arrow Keys: Move   |   P: Pause   |   R: Restart",
    font=("Arial", 10),
    bg=BG_COLOR,
    fg="#d1d5db"
).pack(pady=5)

# =========================
# KEY BINDING
# =========================

root.bind("<KeyPress>", key_pressed)

# =========================
# INITIAL DRAW
# =========================

create_snake()
create_food()
draw_game()

# =========================
# RUN APPLICATION
# =========================

root.mainloop()