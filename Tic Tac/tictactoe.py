"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
from copy import deepcopy

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_moves = 0
    O_moves = 0
    for row in board:
        O_moves = O_moves+ row.count(O)
        X_moves = X_moves+ row.count(X)
    if X_moves <= O_moves:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()

    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                 possible_action.add((row_index, column_index))

    return  possible_action




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_action = player(board)
    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_action

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for win in [X, O]:

        for i in range(3):
            
                
            if all(board[i][j] == win for j in range(3)):
                return win
            if all(board[j][i] == win for j in range(3)):
                return win

        for dia in [[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]:
            if all(board[i][j] == win for (i,j) in dia):
                return win
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            val = 99
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < val:
                    val = maxval
                    optimal_move = action
            return val, optimal_move
        
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            val = -99
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > val:
                    val = minval
                    optimal_move = action
            return val, optimal_move



    current_player = player(board)

    if terminal(board):
        return None

    if current_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]