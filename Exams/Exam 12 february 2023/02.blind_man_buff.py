n, m = [int(el) for el in input().split()]

matrix = []
my_position = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, -0)
}


for i in range(n):
    row = input().split()
    if 'B' in row:
        my_position = [i, row.index("B")]

    matrix.append(row)

touched_players = 0
moves_made = 0

command = input()
while touched_players != 3 and command != "Finish":

    r, c = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < m) or matrix[r][c] == "O":
        command = input()
        continue
    elif matrix[r][c] == "P":
        matrix[r][c] = "-"
        touched_players += 1

    moves_made += 1
    my_position = [r, c]
    command = input()

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves_made}")
