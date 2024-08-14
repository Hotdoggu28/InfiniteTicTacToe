from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Infinite Tic-Tac-Toe')
root.configure(bg="#1C1C1C")

# Fixed size, para hindi ma re-adjust
root.resizable(False, False)
root.geometry("375x500")  # window size

# Track the board state
clicked = True
count = 0
x_moves = []
o_moves = []
timer = 5
timer_id = None


# Reset the game
def reset():
    global x_moves, o_moves, clicked, count, timer
    clicked = True
    count = 0
    x_moves = []
    o_moves = []

    # Reset buttons
    for button in buttons:
        button.config(text=" ", state=NORMAL, bg="#D3D3D3", fg="#1C1C1C")

    timer_label.config(text="Time left: 5s")
    start_timer()


# Disable buttons
def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)


# Function to check winner
def check_winner():
    global winner
    winner = False

    # Check all possible win conditions
    def check_condition(a, b, c):
        if a["text"] == b["text"] == c["text"] and a["text"] != " ":
            a.config(bg="#32CD32")
            b.config(bg="#32CD32")
            c.config(bg="#32CD32")
            return True
        return False

    # Horizontal, vertical, diagonal checks
    if (check_condition(b1, b2, b3) or check_condition(b4, b5, b6) or check_condition(b7, b8, b9) or
            check_condition(b1, b4, b7) or check_condition(b2, b5, b8) or check_condition(b3, b6, b9) or
            check_condition(b1, b5, b9) or check_condition(b3, b5, b7)):
        winner = True

    if winner:
        stop_timer()
        if clicked:
            messagebox.showinfo("Tic Tac Toe", "We have a winner, O is the winner, Congrats!")
        else:
            messagebox.showinfo("Tic Tac Toe", "We have a winner, X is the winner, Congrats!")

        result = messagebox.askquestion("Tic Tac Toe", "Do you want to play again?", icon="question")
        if result == 'yes':
            reset()
        else:
            root.quit()


# Remove the oldest move from the board
def remove_oldest_move(moves):
    if len(moves) > 3:
        oldest_move = moves.pop(0)
        oldest_move.config(text=" ", bg="#D3D3D3")


# Highlight opponent's potential winning moves
def highlight_opponent_winning_move():
    clear_highlights()
    opponent = "O" if clicked else "X"  # Opponent is the opposite of the current player

    # Check each button to see if it could lead to a win for the opponent
    def check_potential_win(a, b, c):
        if a["text"] == " " and b["text"] == opponent and c["text"] == opponent:
            a.config(bg="#FFD700")  # Highlight the possible winning move
        elif a["text"] == opponent and b["text"] == " " and c["text"] == opponent:
            b.config(bg="#FFD700")
        elif a["text"] == opponent and b["text"] == opponent and c["text"] == " ":
            c.config(bg="#FFD700")

    # Check all possible win conditions for opponent's potential winning moves
    check_potential_win(b1, b2, b3)
    check_potential_win(b4, b5, b6)
    check_potential_win(b7, b8, b9)
    check_potential_win(b1, b4, b7)
    check_potential_win(b2, b5, b8)
    check_potential_win(b3, b6, b9)
    check_potential_win(b1, b5, b9)
    check_potential_win(b3, b5, b7)


# Clear all highlights
def clear_highlights():
    for button in buttons:
        if button["bg"] == "#FFD700":
            button.config(bg="#D3D3D3")


# Button click function
def b_click(b):
    global clicked, count, x_moves, o_moves

    if b["text"] == " ":
        if clicked:
            b["text"] = "X"
            b.config(fg="#FF4500")  # Orange for X
            x_moves.append(b)
            remove_oldest_move(x_moves)
        else:
            b["text"] = "O"
            b.config(fg="#1E90FF")  # Blue for O
            o_moves.append(b)
            remove_oldest_move(o_moves)

        clicked = not clicked
        count += 1
        check_winner()
        reset_timer()
        highlight_opponent_winning_move()
    else:
        messagebox.showerror("Tic Tac Toe", "The spot already taken, try harder?")


# Timer
def countdown():
    global timer, timer_id

    if timer > 0:
        timer -= 1
        timer_label.config(text=f"Time left: {timer}s")
        timer_id = root.after(1000, countdown)  # 1000ms = 1 sec
    else:
        stop_timer()
        messagebox.showinfo("Time's up!", "Time's up! Switching turns.")
        switch_turn()


def start_timer():
    global timer, timer_id
    stop_timer()
    timer = 5
    timer_label.config(text=f"Time left: {timer}s")
    timer_id = root.after(1000, countdown)


def reset_timer():
    start_timer()


def stop_timer():
    global timer_id
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None


def switch_turn():
    global clicked
    clicked = not clicked
    reset_timer()
    highlight_opponent_winning_move()


# Board design
# Create a frame for the game board
board_frame = Frame(root, bg="#2F4F4F", bd=5)
board_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

# Buttons
buttons = []
b1 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b1))
b2 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b2))
b3 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b3))
b4 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b4))
b5 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b5))
b6 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b6))
b7 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b7))
b8 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b8))
b9 = Button(board_frame, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#D3D3D3", fg="#1C1C1C",
            command=lambda: b_click(b9))

# Add buttons to the list for easier management
buttons.extend([b1, b2, b3, b4, b5, b6, b7, b8, b9])

# Buttons positions
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# Timer label
timer_label = Label(root, text="Time left: 10s", font=("Helvetica", 14), bg="#1C1C1C", fg="white")
timer_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))

# Game title label
title_label = Label(root, text="Infinite Tic-Tac-Toe", font=("Helvetica", 24), bg="#1C1C1C", fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Start the timer
start_timer()
highlight_opponent_winning_move()  # Highlight the opponent's potential winning move at the start

root.mainloop()
