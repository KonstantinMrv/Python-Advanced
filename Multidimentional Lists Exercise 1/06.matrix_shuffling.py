def is_valid(action, info):
    valid_command = False
    valid_indices = True

    if len(info) != 4:
        return False

    if action == "swap":
        valid_command = True

    for el in info:
        if int(el) > cols or int(el) < 0:
            valid_indices = False
            break

    return valid_indices and valid_command


rows, cols = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

while True:
    command = input()

    if command == "END":
        break

    action, *info = command.split()

    if is_valid(action, info):
        info = [int(el) for el in info]
        matrix[info[0]][info[1]], matrix[info[2]][info[3]] = matrix[info[2]][info[3]], matrix[info[0]][info[1]]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")