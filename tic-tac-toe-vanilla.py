from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('SoftwareDesign - Tic-Tac-Toe')


# to let X starts first
clicked= True
count = 0


# Reset the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

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

#disable buttons
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


#function to check winner
def check_winner():
    global winner
    winner = False

    # check for X wins
    # Horizontal wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True

    # Vertical wins
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True

    # Diagonal wins
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True

    # check for O wins
    # Horizontal wins
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True

    # Vertical wins
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True

    # Diagonal wins
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True

    # show winner and ask to play again or exit
    if winner:
        if clicked:
            messagebox.showinfo("Tic Tac Toe", "We have a winner, O is the winner, Congrats!")
        else:
            messagebox.showinfo("Tic Tac Toe", "We have a winner, X is the winner, Congrats!")

        result = messagebox.askquestion("Tic Tac Toe", "Do you want to play again?", icon="question")
        if result == 'yes':
            reset()
        else:
            root.quit()

    # if no winner yet and all buttons are clicked
    elif count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "Walang nanalo, nyek!")
        result = messagebox.askquestion("Tic Tac Toe", "Do you want to play again?", icon="question")
        if result == 'yes':
            reset()
        else:
            root.quit()


# button clicked function
def b_click(b):
    global clicked, count
   # b.config(text=" ")
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        check_winner()
    else:
        messagebox.showerror("Tic Tac Toe","Naagaw na yan, wag kana jan")


# buttons here
b1 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b3))
b4 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b6))
b7 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace", command= lambda: b_click(b9))

#position buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()
