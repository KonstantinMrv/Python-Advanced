first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    if command == "Add First":
        [first_line.add(int(x)) for x in data]
    elif command == "Add Second":
        [second_line.add(int(x)) for x in data]
    elif command == "Remove First":
        [first_line.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second_line.discard(int(x)) for x in data]
    else:
        print(first_line.issubset(second_line) or second_line.issubset(first_line))

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")