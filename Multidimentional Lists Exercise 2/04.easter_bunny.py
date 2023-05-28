size = int(input())

matrix = [[el for el in input().split()] for _ in range(size)]
bunny_position = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
max_eggs = 0
best_path = []
best_direction = None

for row in range(size):
    if 'B' in matrix[row]:
        bunny_position = [row, matrix[row].index('B')]

for direction, positions in directions.items():
    row, col = [bunny_position[0] + positions[0], bunny_position[1] + positions[1]]
    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_eggs)



