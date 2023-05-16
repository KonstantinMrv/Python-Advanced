from collections import deque

my_stack = deque()

lines = int(input())

for _ in range(lines):
    line = input()
    data = line.split()
    command = int(data[0])

    if command == 1:
        my_stack.append(int(data[1]))
    elif command == 2:
        if my_stack:
            my_stack.pop()
    elif command == 3:
        if my_stack:
            print(max(my_stack))
    else:
        if my_stack:
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep=", ")