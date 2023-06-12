size = int(input())

commands = input().split(", ")
matrix = [[el for el in list(input())] for _ in range(size)]
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, -0)
}

squirrel_position = []

for row in range(size):
    if "s" in matrix[row]:
        squirrel_position = [row, matrix[row].index("s")]

hazelnuts = 0

while hazelnuts != 3:
    if commands:
        current_direction = commands.pop(0)
    else:
        print("There are more hazelnuts to collect.")
        break

    r = squirrel_position[0] + directions[current_direction][0]
    c = squirrel_position[1] + directions[current_direction][1]

    if not (0 <= r < size and 0 <= c < size):
        print("The squirrel is out of the field.")
        break

    if matrix[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if matrix[r][c] == "h":
        hazelnuts += 1
        matrix[r][c] = "*"

    squirrel_position = [r, c]

if hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
print(f"Hazelnuts collected: {hazelnuts}")