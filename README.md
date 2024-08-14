Welcome to the Infinite Tic-Tac-Toe game! This is a Python-based game using the Tkinter library, an enhanced version of the classic Tic-Tac-Toe with some unique twists.

**1. Features**

- Infinite Play Area: Players can place pieces on a 3x3 grid with the rule that only 3 pieces of X or O can be on the board at a time. New moves replace the oldest moves.
- Turn Timer: Each turn is timed with a visible 5-second countdown. A notification pops up if the timer runs out, prompting a turn switch.
- Opponent’s Winning Move Highlight: Potential winning moves of the opponent are highlighted, helping players make strategic decisions.

**2. How to Run**

  To run this game, you'll need Python installed on your system. Ensure you have Tkinter, which is included with Python installations.

  1. Save the Code: Save the provided code into a file named `Infinite Tic-Tac-Toe.py`.

  2. Run the Game: Open a terminal or command prompt and navigate to the directory where you saved the file. Run the following command:
   
   `python Infinite Tic-Tac-Toe.py`

**3. Gameplay**

- Starting the Game: When the game starts, Player X goes first.
- Making a Move: Click on an empty cell to place your piece (X or O). Each player can only place up to 3 pieces on the board. New moves will replace the oldest moves.
- Winning: The game checks for a win condition after each move. If a player achieves a three-in-a-row horizontally, vertically, or diagonally, they win.
- Timer: Each player has 5 seconds per turn. If time runs out, the game automatically switches turns and shows a notification.
