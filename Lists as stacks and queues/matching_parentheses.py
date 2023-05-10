math = input()

my_stack = []


for i in range(len(math)):
    if math[i] == "(":
        my_stack.append(i)
    elif math[i] == ")":
        starting = my_stack.pop()
        closing = i
        expression = math[starting:closing + 1]
        print(expression)

# print(math[starting:i + 1])