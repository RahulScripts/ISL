# Tic-Tac-Toe with minimax (AI = 'O', Human = 'X')

import math

def print_board(board):
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("---------")


def get_winner(board):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # rows
        (0,3,6),(1,4,7),(2,5,8),  # cols
        (0,4,8),(2,4,6)           # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "draw"
    return None

def minimax(board, is_maximizing):
    winner = get_winner(board)
    if winner == "O":  # AI
        return 1
    elif winner == "X":
        return -1
    elif winner == "draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    board = [" "] * 9
    current = "X"  # human first

    while True:
        print_board(board)
        winner = get_winner(board)
        if winner:
            print("Result:", winner)
            break

        if current == "X":
            pos = int(input("Enter position (0-8): "))
            if 0 <= pos <= 8 and board[pos] == " ":
                board[pos] = "X"
                current = "O"
        else:
            pos = best_move(board)
            board[pos] = "O"
            current = "X"

if __name__ == "__main__":
    main()
