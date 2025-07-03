N = 8  

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    if row == N:
        print_solution(board)
        return True

    result = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            result = solve_nqueens(board, row + 1) or result
            board[row][col] = 0  
    return result

board = [[0 for _ in range(N)] for _ in range(N)]
if not solve_nqueens(board, 0):
    print("No solution exists.")
