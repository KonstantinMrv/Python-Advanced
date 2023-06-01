from collections import deque

string = deque(input().split())

colors = ["red", "yellow", "blue", "orange", "purple", "green"]

secondary = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

while len(string) > 0:
    if len(string) == 1:
        last_colour = string.pop()
        if last_colour in colors:
            result.append(last_colour)
        continue

    first, second = string.popleft(), string.pop()

    if first + second in colors:
        result.append(first + second)

    elif second + first in colors:
        result.append(second + first)

    else:
        first, second = first[:-1], second[:-1]
        middle = len(string) // 2
        if first != "":
            string.insert(middle, first)
        if second != "":
            string.insert(middle, second)

for color in result:
    if color in secondary.keys():
        for element in secondary[color]:
            if element not in result:
                result.remove(color)

print(result)


