size = int(input())
chess_board = [list(input()) for _ in range(size)]

positions = (
    (-2, -1),
    (-1, -2),
    (-2, 1),
    (-1, 2),
    (1, -2),
    (2, -1),
    (1, 2),
    (2, 1)
)

removed_knights = 0

while True:
    max_attacks = 0
    best_knight = []

    for row in range(size):
        for col in range(size):
            if chess_board[row][col] == "K":
                current_attacks = 0

                for pos in positions:
                    pos_row = pos[0] + row
                    pos_col = pos[1] + col

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if chess_board[pos_row][pos_col] == "K":
                            current_attacks += 1

                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    best_knight = [row, col]

    if best_knight:
        row, col = best_knight
        chess_board[row][col] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
