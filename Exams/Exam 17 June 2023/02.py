n, m = [int(el) for el in input().split(",")]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, -0)
}

matrix = []
mouse_pos = []
cheese = 0
trapped = False
went_out = False

for row in range(n):
    inner_line = list(input())

    if "M" in inner_line:
        mouse_pos = [row, inner_line.index("M")]

    if "C" in inner_line:
        cheese += inner_line.count("C")
    matrix.append(inner_line)


command = input()
while command != "danger":

    r, c = mouse_pos[0] + directions[command][0], mouse_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < m):
        print("No more cheese for tonight!")
        went_out = True
        break

    if matrix[r][c] == "C":
        cheese -= 1
        matrix[r][c] = "*"
        if cheese == 0:
            matrix[r][c] = "M"
            matrix[mouse_pos[0]][mouse_pos[1]] = "*"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[r][c] == "T":
        matrix[r][c] = "M"
        matrix[mouse_pos[0]][mouse_pos[1]] = "*"
        print("Mouse is trapped!")
        trapped = True
        break

    elif matrix[r][c] == "@":
        command = input()
        continue

    matrix[mouse_pos[0]][mouse_pos[1]] = "*"
    matrix[r][c] = "M"
    mouse_pos = [r, c]
    command = input()

if cheese and not trapped and not went_out:
    print("Mouse will come back later!")

for row in matrix:
    print(''.join(str(cell) for cell in row))