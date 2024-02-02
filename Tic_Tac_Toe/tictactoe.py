"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    countx = 0
    counto = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countx += 1
            if board[row][col] == O:
                counto += 1

    if countx > counto:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    AllPossibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                AllPossibleActions.add((row,col))

    return AllPossibleActions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not Valid Action !")
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)

    return board_copy

def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        
    return False

def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        
    return False

def checkDiag(board, player):
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkCol(board, X) or checkRow(board, X) or checkDiag(board, X):
        return X
    elif checkCol(board, O) or checkRow(board, O) or checkDiag(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
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
    elif winner(board) == None:
        return 0

def MaxV(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, MinV(result(board, action))) # type: ignore
    
    return v


def MinV(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, MaxV(result(board, action))) # type: ignore

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # Case of player is X (max-player)
    elif player(board) == X:
        plays = []
        # Loop over the possible actions
        for action in actions(board):
            # Add in plays list a tuple with the MinV and the action results to its value
            plays.append([MinV(result(board, action)), action])

        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]    
    
    # Case of player is O (min-player)
    elif player(board) == O:
        plays = []
        # Loop over the possible actions
        for action in actions(board):
            # Add in plays list a tuple with the MaxV and the action results to its value
            plays.append([MaxV(result(board, action)), action])

        # Reverse sort for the plays list and get the action that should take
        return sorted(plays, key=lambda x: x[0])[0][1]    

