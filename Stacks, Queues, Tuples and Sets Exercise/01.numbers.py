first_sequence = set(int(el) for el in input().split())
second_sequence = set(int(el) for el in input().split())


for _ in range(int(input())):
    command, location, *data = input().split()

    if command == "Add":

        if location == "First":
            [first_sequence.add(int(el)) for el in data]
        elif location == "Second":
            [second_sequence.add(int(el)) for el in data]

    elif command == "Remove":

        if location == "First":
            [first_sequence.discard(int(el)) for el in data]
        elif location == "Second":
            [second_sequence.discard(int(el)) for el in data]

    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
