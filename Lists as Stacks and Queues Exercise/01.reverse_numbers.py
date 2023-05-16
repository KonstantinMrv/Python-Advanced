numbers = [int(x) for x in input().split()]

my_stack = []

for num in numbers.copy():
    current_number = numbers.pop()
    my_stack.append(current_number)

print(*my_stack, sep=" ")