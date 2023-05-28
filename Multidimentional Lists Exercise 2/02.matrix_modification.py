size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size)]

command = input()
while command != "END":
    command_info = command.split()
    first_index = int(command_info[1])
    second_index = int(command_info[2])

    if not (0 <= int(first_index) < size and 0 <= second_index < size):
        print("Invalid coordinates")
    else:
        if command_info[0] == "Add":
            matrix[first_index][second_index] += int(command_info[3])
        elif command_info[0] == "Subtract":
            matrix[first_index][second_index] -= int(command_info[3])

    command = input()

[print(*row) for row in matrix]