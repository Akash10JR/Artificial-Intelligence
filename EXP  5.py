def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(b, player):
    return any([
        all(cell == player for cell in row) for row in b
    ]) or any([
        all(b[i][col] == player for i in range(3)) for col in range(3)
    ]) or all([
        b[i][i] == player for i in range(3)
    ]) or all([
        b[i][2 - i] == player for i in range(3)
    ])

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = [[' ']*3 for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
        except:
            print("Invalid input. Try again.")
            continue

        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

play_game()
