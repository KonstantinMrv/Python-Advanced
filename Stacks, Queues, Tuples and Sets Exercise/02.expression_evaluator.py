from math import floor
from collections import deque
from functools import reduce


def append_result(res):
    queue.clear()
    queue.append(res)


expression = input().split()
queue = deque()


for element in expression:

    if element == "*":
        result = reduce(lambda x, y: x * y, queue)
        append_result(result)
    elif element == "+":
        result = reduce(lambda x, y: x + y, queue)
        append_result(result)
    elif element == "/":
        result = reduce(lambda x, y: x / y, queue)
        append_result(floor(result))
    elif element == "-":
        result = reduce(lambda x, y: x - y, queue)
        append_result(result)
    else:
        queue.append(int(element))

print(*queue)