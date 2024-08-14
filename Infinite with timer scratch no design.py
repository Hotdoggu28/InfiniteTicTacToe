from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('SoftwareDesign - Infinite Tic-Tac-Toe')

# Track the board state and moves
clicked = True
count = 0
x_moves = []
o_moves = []
timer = 10
timer_id = None


# Reset the game
def reset():
    global x_moves, o_moves, clicked, count, timer
    clicked = True
    count = 0
    x_moves = []
    o_moves = []

    # Reset buttons
    b1.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b2.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b3.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b4.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b5.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b6.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b7.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b8.config(text=" ", state=NORMAL, bg="SystemButtonFace")
    b9.config(text=" ", state=NORMAL, bg="SystemButtonFace")

    timer_label.config(text="Time left: 10s")
    start_timer()


# Disable buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# Function to check winner
def check_winner():
    global winner
    winner = False

    # Check all possible win conditions
    def check_condition(a, b, c):
        if a["text"] == b["text"] == c["text"] and a["text"] != " ":
            a.config(bg="green")
            b.config(bg="green")
            c.config(bg="green")
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
        oldest_move.config(text=" ", bg="SystemButtonFace")


# Button click function
def b_click(b):
    global clicked, count, x_moves, o_moves

    if b["text"] == " ":
        if clicked:
            b["text"] = "X"
            x_moves.append(b)
            remove_oldest_move(x_moves)
        else:
            b["text"] = "O"
            o_moves.append(b)
            remove_oldest_move(o_moves)

        clicked = not clicked
        count += 1
        check_winner()
        reset_timer()
    else:
        messagebox.showerror("Tic Tac Toe", "Naagaw na yan, wag kana jan")


# Timer function
def countdown():
    global timer, timer_id

    if timer > 0:
        timer -= 1
        timer_label.config(text=f"Time left: {timer}s")
        timer_id = root.after(1000, countdown)  # Countdown every second
    else:
        stop_timer()
        messagebox.showinfo("Time's up!", "Time's up! Switching turns.")
        switch_turn()


def start_timer():
    global timer, timer_id
    stop_timer()  # Stop any existing timer before starting a new one
    timer = 10
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


# Buttons
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b6))
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
            command=lambda: b_click(b9))

# Position buttons
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
timer_label = Label(root, text="Time left: 10s", font=("Helvetica", 14))
timer_label.grid(row=3, column=0, columnspan=3)

# Start the timer
start_timer()

root.mainloop()
