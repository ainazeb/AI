This repository contains two Python files that implement a two-player Tic-Tac-Toe game with an AI opponent. The first file (tictactoe.py) contains the game logic, and the second file (runner.py) uses the pygame library to provide a graphical interface for the game. The AI opponent uses the Minimax algorithm to make optimal moves.

1. tictactoe.py (Game Logic)
This file contains the core logic for the Tic-Tac-Toe game. It defines a set of functions that handle the game state, player turns, move validation, and game outcome. The key functions in this file are:

initial_state(): Returns the initial empty state of the Tic-Tac-Toe board.
player(board): Determines which player (X or O) has the next move, based on the current board state.
actions(board): Returns a set of available actions (empty spots) on the board.
result(board, action): Returns a new board state after making a move at a specific position.
winner(board): Determines the winner of the game, if any.
terminal(board): Checks if the game has ended (either by a win or a tie).
utility(board): Returns the utility value of the board: 1 for X win, -1 for O win, and 0 for a tie.
minimax(board): Implements the Minimax algorithm to compute the best move for the current player based on the board state. It calls helper functions max_value() and min_value() to evaluate possible moves and select the optimal one.
2. runner.py (Graphical User Interface)
This file creates a graphical interface for playing Tic-Tac-Toe using pygame. The player can choose to play as either X or O, and the game board is displayed interactively. The AI opponent uses the minimax function from tictactoe.py to make its moves. The key features of the graphical interface are:

User Selection: The user selects whether they want to play as X or O at the beginning of the game.
Game Board: The game board is drawn using pygame's drawing functions. It shows the current state of the board with X's and O's, and updates in real-time as players make their moves.
Game Over Handling: Once the game ends (either by a win or a tie), the result is displayed, and the player is prompted to play again.
AI vs Player: The AI opponent makes optimal moves using the minimax algorithm. If it's the player's turn, they can click on the board to make a move, and the AI will take its turn afterward.
Play Again: After a game ends, the player can restart the game with a new board.
How to Play
Start the Game: Upon running the runner.py file, the player will be prompted to choose whether to play as X or O.
Gameplay: The game board is displayed with empty squares. Click on an empty square to make your move.
If you're playing against the AI, it will automatically take its turn after you.
Game Over: The game will end when either player wins, or if there’s a tie. The result will be displayed at the top of the screen.
Play Again: After the game ends, click the "Play Again" button to restart with a new game.
Dependencies
pygame: A library used for creating the graphical interface.
sys, time: Standard Python libraries for managing system operations and timing.
Installation and Running
To run this game, follow these steps:

Install pygame if you haven't already:
Copy code
pip install pygame
Download the repository or copy both tictactoe.py and runner.py into the same directory.
Run the runner.py file:
Copy code
python runner.py
Enjoy playing Tic-Tac-Toe with the AI!












