size = int(input())

matrix = []
submarine = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, -0)
}

for row in range(size):
    inner_line = list(input())
    if "S" in inner_line:
        submarine = [row, inner_line.index("S")]

    matrix.append(inner_line)

mines = 0
sunken_ships = 0

while sunken_ships != 3 and mines != 3:

    direction = input()

    r, c = submarine[0] + directions[direction][0], submarine[1] + directions[direction][1]

    if matrix[r][c] == "*":
        mines += 1
        matrix[r][c] = "-"

        if mines == 3:
            matrix[submarine[0]][submarine[1]] = "-"
            submarine = [r, c]
            matrix[r][c] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            for row in matrix:
                print(''.join(map(str, row)))
            exit(0)

    elif matrix[r][c] == "C":
        sunken_ships += 1
        matrix[r][c] = "-"

        if sunken_ships == 3:
            matrix[submarine[0]][submarine[1]] = "-"
            submarine = [r, c]
            matrix[r][c] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            for row in matrix:
                print(''.join(map(str, row)))
            exit(0)

    matrix[submarine[0]][submarine[1]] = "-"
    submarine = [r, c]
    matrix[r][c] = "S"




