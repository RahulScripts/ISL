# N-Queens using backtracking

def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n):
    if row == n:
        return True  # one solution is enough

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack
    return False

def main():
    n = int(input("Enter N for N-Queens: "))
    board = [[0]*n for _ in range(n)]

    if solve_nqueens(board, 0, n):
        print("Solution:")
        for row in board:
            print(row)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
