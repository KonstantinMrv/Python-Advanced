SIZE = 6

matrix = []
rover_pos = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, -0)
}

for row in range(SIZE):
    inner_line = input().split()

    if "E" in inner_line:
        rover_pos = [row, inner_line.index("E")]
    matrix.append(inner_line)

commands = input().split(", ")
materials = [False, False, False]

while commands:
    current_command = commands.pop(0)
    r, c = rover_pos[0] + directions[current_command][0], rover_pos[1] + directions[current_command][1]

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        if r < 0:
            r += 6
        if r > 5:
            r -= 6

        if c < 0:
            c += 6
        if c > 5:
            c -= 6

    if matrix[r][c] == "W":
        print(f"Water deposit found at ({r}, {c})")
        materials[0] = True
    elif matrix[r][c] == "M":
        print(f"Metal deposit found at ({r}, {c})")
        materials[1] = True
    elif matrix[r][c] == "C":
        print(f"Concrete deposit found at ({r}, {c})")
        materials[2] = True
    elif matrix[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

    rover_pos = [r, c]

if all(materials):
    print(f"Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")