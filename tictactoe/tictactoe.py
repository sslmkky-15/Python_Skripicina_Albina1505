def print_board(board):
    print("---------")
    for row in board:
        print(f"| {' '.join(row)} |")
    print("---------")


def check_state(board):
    lines = [
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    if ["X", "X", "X"] in lines:
        return "X wins"
    if ["O", "O", "O"] in lines:
        return "O wins"

    for row in board:
        if "_" in row:
            return "Game not finished"

    return "Draw"


def make_move(board, player):
    while True:
        print(f"It is {player}'s turn.")
        print("Enter the coordinates:")

        coords = input('> ').split()

        if len(coords) != 2:
            print("You should enter two numbers!")
            continue

        if not coords[0].isdigit() or not coords[1].isdigit():
            print("You should enter numbers!")
            continue

        x = int(coords[0])
        y = int(coords[1])

        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        row = x - 1
        col = y - 1

        if board[row][col] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        board[row][col] = player
        break


print("Welcome to Tic-Tac-Toe!")

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

print_board(board)

current_player = "X"

while True:
    make_move(board, current_player)
    print_board(board)

    result = check_state(board)
    if result == "X wins" or result == "O wins" or result == "Draw":
        print(result)
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("Game over. Have a nice day!")
