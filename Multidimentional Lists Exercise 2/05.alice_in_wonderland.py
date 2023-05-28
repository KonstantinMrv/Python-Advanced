size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
alice_position = []
collected_tea = 0

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]

matrix[alice_position[0]][alice_position[1]] = "*"
while collected_tea < 10:
    command = input()

    rows, cols = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if not (0 <= rows < size and 0 <= cols < size):
        print("Alice didn't make it to the tea party.")
        break

    if matrix[rows][cols] == "R":
        print("Alice didn't make it to the tea party.")
        alice_position = rows, cols
        matrix[rows][cols] = "*"
        break

    if matrix[rows][cols].isdigit():
        collected_tea += int(matrix[rows][cols])

    alice_position = rows, cols
    matrix[rows][cols] = "*"


if collected_tea >= 10:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]