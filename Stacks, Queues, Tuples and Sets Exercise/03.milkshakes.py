from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:

    last_chocolate = chocolates.pop()
    first_milk = cups_of_milk.popleft()

    if last_chocolate <= 0 and first_milk <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(first_milk)
        continue
    elif first_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == first_milk:
        milkshakes += 1

    else:
        cups_of_milk.append(first_milk)
        chocolates.append(last_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(c) for c in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(c) for c in cups_of_milk)}")
else:
    print("Milk: empty")