def move(direction, steps):
    r, c = my_position[0] + directions[direction][0] * steps, my_position[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if matrix[r][c] == 'x':
        return my_position

    return [r, c]


SIZE = 5

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

my_position = []
all_targets = 0
targets_hit = 0
targets_hit_positions = []

for row in range(SIZE):
    matrix.append(input().split())
    if "A" in matrix[row]:
        my_position = [row, matrix[row].index("A")]
    if "x" in matrix[row]:
        all_targets += matrix[row].count("x")

n = int(input())

for _ in range(n):
    command_info = input().split()
    command = command_info[0]
    direction = command_info[1]

    if command == "move":
        steps = int(command_info[2])
        my_position = move(direction, steps)

    elif command == "shoot":
        row, col = my_position[0] + directions[direction][0], my_position[1] + directions[direction][1]
        target_down = []

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                target_down.append([row, col])
                matrix[row][col] = "."
                break

            row += directions[direction][0]
            col += directions[direction][1]

        if target_down:
            targets_hit_positions.append(target_down)
            targets_hit += 1

    if targets_hit == all_targets:
        print(f"Training completed! All {all_targets} targets hit.")
        break

if targets_hit < all_targets:
    print(f"Training not completed! {all_targets - targets_hit} targets left.")

[print(*row) for row in targets_hit_positions]



