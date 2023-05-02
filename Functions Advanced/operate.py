def operate(operator, *args):

    if operator == "+":
        result = 0
        for num in args:
            result += num
        return result
    elif operator == "-":
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result


print(operate("-", 3, 4))