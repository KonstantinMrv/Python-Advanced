def even_odd(*args):
    command = args[-1]
    result = []

    if command == "even":
        for i in range(0, len(args) - 1):
            if args[i] % 2 == 0:
                result.append(args[i])
        return result
    else:
        for i in range(0, len(args) - 1):
            if args[i] % 2 == 1:
                result.append(args[i])
        return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))