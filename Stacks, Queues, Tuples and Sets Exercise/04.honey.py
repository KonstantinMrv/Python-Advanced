from collections import deque


def honey_made(bee, nectar):
    sign = honey_making.popleft()

    if sign == "*":
        return bee * nectar
    elif sign == "+":
        return bee + nectar
    elif sign == "/":
        return bee / nectar
    elif sign == "-":
        return bee - nectar


working_bees = deque(int(el) for el in input().split())
nectar = deque(int(el) for el in input().split())
honey_making = deque(input().split())

total_honey = 0

while working_bees and nectar:

    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if first_bee <= last_nectar:
        if last_nectar > 0:
            total_honey += abs(honey_made(first_bee, last_nectar))
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(b) for b in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(b) for b in nectar)}")
